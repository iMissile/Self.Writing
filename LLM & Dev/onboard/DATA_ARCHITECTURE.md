# Организация базы Android: Netrunner в репозитории

Статус: проект решения, 2026-10-21.

## 1. Короткое решение

- Arch-Lib остаётся канонической базой знаний и историей принятых решений.
- Репозиторий содержит компактный, версионируемый снимок данных для AI-движка.
- Parquet — формат таблиц снимка в каталоге db/.
- DuckDB читает Parquet напрямую через read_parquet(); отдельный файл
  netrunner.duckdb не обязателен.
- Markdown/CSV/JSONL в research/ сохраняют источники, пояснения и непроверенные
  кандидаты. Это слой для чтения и ревью, а не вторая каноническая база.
- Скан-картинки и исходные PDF в репозиторий не копируются; фиксируются их
  SHA-256, путь, версия и локатор.

Такой формат оставляет содержимое читаемым в Git, а Parquet даёт типизированные
таблицы, которые можно запрашивать без ETL-копии в DuckDB.

## 2. Границы источников истины

| Слой | Назначение | Может менять карточные факты? |
|---|---|---|
| Исходные сканы и документы | Доказательства; байты неизменяемы | Нет |
| research/ | Отчёты, источники, OCR-кандидаты и заметки проверки | Только создаёт кандидатов |
| Arch-Lib | Канонические сущности, ревизии, evidence и решения | Да, после проверки |
| db/*.parquet | Детерминированная проекция выбранного checkpoint Arch-Lib | Нет, генерируется |
| DuckDB-запрос | Временное чтение Parquet для движка, аналитики или AI | Нет |

Репозиторий не становится второй редактируемой БЗ. Изменение принятой карты или
правила сначала оформляется в Arch-Lib с source refs и record/domain revision;
затем экспортируется новый checkpoint в Parquet.

## 3. Предлагаемая структура репозитория

    README.md
    research/
      core_set/                         # компактный корпус исследования
        report.md
        rules_model.md
        sources.csv
        coverage.csv
        open_questions.csv
        artifacts/
          card_printing_candidates.jsonl
          card_scan_crosswalk_candidate.csv
          scan_manifest.csv
          scan_ocr_candidates.jsonl
    db/
      manifest.json
      schema.json
      products.parquet
      cards.parquet
      printings.parquet
      card_text_versions.parquet
      card_effects.parquet
      rules.parquet
      card_pools.parquet
      pool_membership.parquet
      sources.parquet
      scan_assets.parquet
      queries.sql
    tools/
      export_archlib.py
      build_parquet.py
      validate_export.py

Для текущего небольшого корпуса не нужны подпапки по каждому паку, циклу,
фракции или году. Core и Revised Core — разные products/printings в одной
схеме. Не создаём отдельную базу на каждую коробку.

Parquet-файлы — основной queryable snapshot репозитория. Каталог research/
остаётся человеко- и ИИ-читаемым журналом исследования. Будущие партии и
обучающие траектории не смешиваются со статической карточной БЗ; для них можно
отдельно добавить game_logs/ после появления реального формата событий.

## 4. Таблицы

### products.parquet

Одна строка на продукт:

- product_id — внутренний стабильный идентификатор;
- product_code — AND01, ADN49 и последующие FFG-коды;
- title, publisher, rules_namespace, language, release_date;
- source_id и product_status.

### cards.parquet

Одна строка на логическую идентичность карты, а не на картинку:

- card_id — стабильный внутренний ID, не имя карты и не scan prefix;
- canonical_title, side, faction, card_type, subtypes, uniqueness;
- identity/agenda-specific fields, когда они будут приняты;
- record_status и ссылки на принятую текущую text revision.

Переиздание не создаёт новую логическую карту автоматически. Совпадение имён
или текста также само по себе не доказывает, что две печати имеют одну
идентичность: crosswalk должен ссылаться на evidence и решение.

### printings.parquet

Одна строка на физическую печать:

- printing_id, card_id, product_id/product_code;
- printed_card_code, language, artwork_id;
- copies_in_product;
- scan_asset_id, printed_text_version_id, record_status.

Количество копий относится к конкретному product/printing. Его нельзя смешивать
с лимитом копий в deck.

### card_text_versions.parquet

Отдельная строка на каждую версию текста:

- text_version_id, card_id, printing_id;
- text_kind: printed, errata, effective, translation;
- text, rules_namespace, valid_from, valid_to;
- recorded_at, record_status, source_refs.

valid_from/valid_to описывают, когда версия применялась в игре; recorded_at —
когда знание было зафиксировано. Поздно найденная errata не меняет старый
knowledge checkpoint.

### card_effects.parquet

Машинное представление не заменяет текст карты:

- effect_id, text_version_id, parser/schema version;
- effect_ast_json;
- implementation_status: supported, partial, unsupported;
- review_status и source_refs.

AST разделяет trigger, condition, cost, target, choice и effect. Пока карта не
разобрана и не проверена, движок видит её как unimplemented/unsupported, а не
как пустой эффект.

### rules.parquet

Атомарные общие правила:

- rule_id, ruleset_id, rules_namespace;
- timing_window, trigger, condition, cost, effect/precedence;
- valid_from, valid_to, record_status, source_refs.

Card-specific FAQ и errata хранятся в card_text_versions/card_effects, а не
теряются внутри общей строки правил.

### card_pools.parquet и pool_membership.parquet

card_pools содержит профиль набора (например, core_2012_casual или
revised_core_2017_casual), его namespace, date/as-of и policy. pool_membership
связывает pool_id с card_id и периодом применимости.

Core-only — пользовательский pool profile. Его нельзя называть FFG Standard:
легальность зависит от даты, формата, ротации и списка ограничений.

### sources.parquet и scan_assets.parquet

sources хранит source_id, authority, версию, URL/local path, SHA-256, язык,
lineage, права и статус проверки. scan_assets хранит asset_id, source_id,
имя файла, SHA-256, размеры изображения и OCR status.

OCR-текст ссылается на scan_asset_id и не заменяет оригинальные байты.

## 5. Parquet и DuckDB

На текущем объёме записываем по одному Parquet-файлу на таблицу. Hive partitioning
по продуктам или фракциям не нужен: файлов будет больше, чем пользы от
партиционирования. Если корпус вырастет существенно, схему можно пересмотреть
по фактическим размерам и планам запросов.

DuckDB открывает снимок без отдельной базы:

    SELECT c.card_id, c.canonical_title, p.product_code, p.copies_in_product
    FROM read_parquet('db/cards.parquet') AS c
    JOIN read_parquet('db/printings.parquet') AS p USING (card_id)
    WHERE c.record_status = 'accepted'
      AND p.record_status = 'accepted';

Для повторяющихся запросов db/queries.sql содержит VIEW-определения над
read_parquet(). Если понадобится быстрый AI-контекст, запрос может отдать
выбранные принятые записи в JSONL; второй ручной каталог с теми же данными не
ведётся.

Движок задаёт pool_id и ruleset_id явно. Runtime views по умолчанию показывают
только accepted-строки. Candidate/conflicted строки доступны отдельными
диагностическими запросами и никогда не попадают в игру молча.

## 6. Manifest, версии и воспроизводимость

db/manifest.json фиксирует:

- dataset_id и checkpoint_id Arch-Lib;
- schema_version и build tool version;
- scope: продукты/языки/пространство правил;
- ruleset_id и knowledge_as_of;
- список Parquet-файлов, row count и SHA-256 каждого файла;
- исходный checkpoint и версию policy экспортёра.

Экспортёр работает офлайн по локальным принятым данным, сортирует строки по
стабильным ID и не вставляет текущее время в сами таблицы. Один и тот же
checkpoint должен давать те же содержательные строки и хеши.

Каждый record status один из candidate, accepted, conflicted, rejected,
withdrawn. Новое понимание исправляет или закрывает предыдущую revision со
ссылкой на источник; история не переписывается молча.

## 7. Git и размер

- Коммитить Parquet snapshot и manifest: тогда clone репозитория сразу
  queryable, без скачивания изображений или запуска отдельной БД.
- Коммитить небольшой DuckDB SQL-файл с запросами и представлениями.
- Не коммитить .duckdb runtime-файл: он строится DuckDB из Parquet и создаёт
  дублируемое состояние.
- Не коммитить raw сканы/PDF. В Git остаются метаданные, source refs и хеши.
- Parquet бинарный и плохо показывает смысловой diff; содержательные решения
  ревьюятся в отчёте/changeset Arch-Lib, а manifest показывает, какой snapshot
  экспортирован.
- Пока корпус укладывается примерно в текущие 1.5 МБ, не нужны Git LFS,
  отдельный сервер, SQLite, миграции между двумя БД или пакетные копии по
  каждому продукту.

## 8. Поток обновления

1. Получить/зафиксировать источник; сохранить его SHA и locator. Raw bytes
   остаются в архиве, не в репозитории.
2. Создать research observation со статусом candidate и source refs.
3. Независимо проверить физическую печать, card identity, версии текста и
   применимость правил.
4. Принять/отклонить/conflict решение в Arch-Lib; записать domain revision,
   record revision и checkpoint.
5. Экспортировать выбранный checkpoint в db/*.parquet и обновить manifest.
6. DuckDB запросами сравнить количество строк, ключи, связи и хеши с manifest.
7. AI runtime выбирает принятый card pool и ruleset; candidates остаются
   исключены из рабочих VIEW.

## 9. Перенос текущего Core корпуса

Текущий исследовательский каталог содержит 245 карточных записей в статусе
candidate_unreviewed и 246 OCR-кандидатов. Это хорошее сырьё для первого
Parquet snapshot, но его пока нельзя публиковать как accepted runtime data.
Перед сборкой accepted views нужны:

1. ручная проверка roster-to-scan joins и printed card codes;
2. проверка символов, чисел, типов и подтипов OCR;
3. Core-specific FAQ 4.2/errata join;
4. stable card_id и printing_id crosswalk, особенно для identity title/subtitle;
5. решение о pool profile: Core 2012, Revised Core 2017 или оба.

Первый экспорт может включать candidate-строки с явным status. Запрос AI-игры
возвращает пустой/ограниченный принятый пул до прохождения этих ворот; это
сохраняет безопасность данных без дополнительных баз и копий.

## 10. Порядок внедрения

1. Утвердить этот контракт каталогов и ключевых сущностей.
2. Добавить db/schema.json, db/manifest.json и детерминированный экспортёр.
3. Сгенерировать Parquet из текущих кандидатов, проверить чтение через DuckDB.
4. После ручной приёмки включить accepted rows в runtime views.
5. Добавлять card-effect AST и новые продуктовые scope только по отдельным
   решениям/changeset; все продукты остаются в едином dataset_id.
