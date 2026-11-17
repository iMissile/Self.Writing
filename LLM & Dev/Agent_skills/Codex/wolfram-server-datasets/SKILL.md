---
name: wolfram-server-datasets
description: Создание, чтение и передача типизированных версий таблиц Parquet и native-объектов Wolfram; используйте для явных форматов, SHA-256, provenance, точности и datasets API/MCP.
---

# Наборы данных

Используйте этот skill для версионированных таблиц и сложных объектов Wolfram. Бинарные данные передаются процессом по HTTP/SDK и не помещаются в контекст модели.
Используйте только подключённые в текущем сеансе операции; описанные source-level names не являются подтверждением production rollout.

## Контракт набора

- Для новых типизированных данных используйте datasets v2 с явными `source_format` и `storage_format`. Допустимы `csv → parquet`, `parquet → parquet` и сохранение native в том же формате: `wxf`, `mx`, `wdx`, `expressionjson`, `wlnet`, `wmlf`. Native не превращается в таблицу автоматически. Действующий v1 сохраняет прежний табличный контракт.
- Native upload требует `native_descriptor` с объявленным описанием структуры вместо фиктивных колонок. Для MX обязательна `compatibility`: `wolfram_version`, `system_id`, `system_word_length`. SHA подтверждает байты, а не возможность восстановить произвольный объект в другой версии Wolfram. Не выполняйте `Get`/`Import` или десериализацию стороннего содержимого автоматически.
- Перед типизированной передачей прочтите [контракт форматов](references/typed-formats.md); сначала проверьте, что подключённый сервер объявил нужные операции и формат.

- До upload задайте `dataset_id`, `version`, описание, `provenance`, формат источника, SHA-256 и число байтов источника, резерв диска. Для табличных данных обязательна полная схема колонок: `name`, `type`, `nullable`, `unit`, `precision`; для native используется descriptor выше.
- На `wolfram-server.ru` 28.10.2026 `max_source_bytes` поднят до 1 ГиБ (1 073 741 824 байта); перед upload подтвердите значение через capabilities. Объявляйте собственный клиентский budget и `reservation_bytes` с учётом лимитов metadata и общей квоты. Размер принятого WXF не является оценкой RAM при десериализации или доказательством прохождения крупного end-to-end transfer. Для compute bundle отдельно учитываются код, остальные inputs и ZIP overhead.
- Допустимые типы: `int64`, `float64`, `string`, `bool`, `decimal128(p,s)`. Для точных измерений предпочитайте `int64` или `decimal128`; CSV `float64` требует явного `float_conversion` (`exact` либо `allow_rounding`). Не разрешайте округление молча.
- Для v1 CSV и Parquet сохраняют прежний табличный контракт с каноническим Parquet. В v2 CSV с явной схемой сохраняется как Parquet, Parquet сохраняется как Parquet, а native сохраняется в том же явно заданном формате.
- В manifest различайте `source.sha256/bytes/format` и `parquet.sha256/bytes/format`: первый описывает исходные байты, второй — проверенный сохранённый Parquet. Схема, единицы, точность и provenance являются частью метаданных версии.

## Машинные операции

- Точные MCP names v1: `datasets_list`, `datasets_get`, `datasets_metadata`, `datasets_schema`, `datasets_preview`, `datasets_begin_upload`, `datasets_finalize_upload`.
- Точные MCP names v2: `datasets_v2_capabilities`, `datasets_v2_list`, `datasets_v2_metadata`, `datasets_v2_manifest`, `datasets_v2_schema`, `datasets_v2_preview`, `datasets_v2_begin_upload`, `datasets_v2_finalize_upload`.
- Для v2 upload явно задавайте `source_format` и `storage_format`; формат каждого binary chunk должен совпадать с форматом handle. Для `datasets_v2_schema` и `datasets_v2_preview` задавайте `expected_format`; на download он обязателен. `datasets_v2_list`, `datasets_v2_manifest` и metadata discovery показывают объявленный формат, но сами bytes не читают.
- `datasets_begin_upload` возвращает opaque `upload_handle`. Передавайте исходный файл бинарными блоками через поддержанный transfer client, затем вызывайте `datasets_finalize_upload`; не включайте байты файла в MCP/LLM payload.
- Используйте настроенный native-binary transfer process для блоков файла; не сериализуйте байты в JSON/MCP. Процесс читает credential из закрытого файла, ограничивает размер файла/ответа и timeout и не следует redirect на другой origin. Если доступен CLI, проверяйте его точный invocation через `--help`; запускайте Python только через `uv`.
- Проверяйте offset ACK для каждого бинарного блока. Не меняйте origin credential через `--base-url` и не разрешайте перенаправление на другой origin.
- Версия `(dataset_id, version)` неизменяема. После неопределённого ответа финализации сначала прочитайте список/manifest и сравните source и storage SHA; не создавайте новую версию и не загружайте файл заново вслепую. V2 подтверждает повтор того же опубликованного handle через receipt и сверку версии; не переносите это обещание на v1 без проверки manifest.
- Чтение используйте через `datasets_get`/`datasets_metadata`/`datasets_schema`; `datasets_preview` ограничен и сериализует значения в строки. Для точных численных данных используйте скачивание Parquet, а не preview.
- Для v1 backup allowlist состоит из `manifest.json` и `data.parquet`. Для v2 сохраняйте manifest и ровно объявленный storage payload с его форматом/размером/SHA; не включайте transient upload, raw CSV и системные секреты.

## Учётные данные

Credential-файл читает transfer process через общий client/private-file механизм. Не читайте его содержимое моделью, не передавайте токен в argv, вывод, MCP arguments или commit.
Для binary Parquet и native downloads нужен scope `datasets:download`; MCP передаёт только metadata, сами bytes скачиваются отдельным HTTP/SDK-клиентом с обязательным `expected_format`.

## Финализация вычисленного результата

- Используйте карточку задачи как источник заявленной схемы, provenance, плана блоков и критериев проверки; публикация Parquet фиксирует вычисленные байты и метаданные, но не подтверждает научную интерпретацию.
- Сохраняйте схему и точность из неизменяемой спецификации. Не объединяйте результаты независимых блоков иначе, чем разрешает исходный метод; повторная финализация не должна создавать новые вычислительные задания. Длительная server-side задача не зависит от времени жизни агента или клиента.

`compute_complete` означает завершение вычисления; публикация конечного Parquet выполняется отдельно. Используйте установленный `scripts/finalize-compute.py`, проверив `--help`: команда принимает `--job-id`, `--spec`, `--credential-file`, `--output-root` и явные бюджеты времени, frame, источников, скачивания и chunk. В spec версии 1 задайте `dataset_id`, описание, `reservation_bytes` и упорядоченные `columns`; каждая колонка содержит `name`, `type`, `nullable`, `unit`, `precision`, `source_field`. Для `float64` обязательна политика `float_conversion`; для CSV-блоков необходим явный `csv` dialect. Не выводите единицы или точность из значений.

Финализатор проверяет manifest задания, checkpoint и хеши перечисленных закрытых блоков, публикует детерминированную версию и скачивает Parquet с точным manifest. Сверяйте итоговый JSON receipt: `job_id`, `run_id`, `dataset_id`, `version`, `rows`, `manifest_sha256`, `parquet_sha256`, `bytes`. Для повторения после обрыва используйте те же задание и spec; изменение схемы создаёт другую версию. Не подменяйте исходные checkpoint/JSON/CSV файлы и не объявляйте `scientific_acceptance` подтверждённой из-за успешной публикации Parquet.


## Локальная установка

Фактические пути клиента и конфигурации указаны в [локаторе установки](references/local-installation.json). Локатор содержит публичные параметры и пути. Содержимое credential-файла читает только процесс клиента.
