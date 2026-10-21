# Seasons AI — организация данных, репозитория и миграции

**Статус:** предлагаемая адаптация `DATA_ARCHITECTURE.md` от 2026-10-21 (документ-образец относится к Android: Netrunner).  
**Проект:** Seasons AI, 2026-10-21.  
**Связанный план:** `PLAN_SEASONS_AI_R0000.md`.  
**Приёмка:** этот файл — архитектурная постановка, а не доказательство выполненного экспорта или верификации.

## 1. Принятое архитектурное направление

1. **Seasons-Arch (в Arch-Lib) — единственная каноническая БЗ.** Здесь принимаются факты, редакции, локализации, источники и спорные решения; архивные и первичные материалы остаются под его контролем.
2. **Seasons AI — потребитель версионируемых снимков.** В репозитории `db/*.parquet` — детерминированная, **не редактируемая вручную** проекция *конкретного* checkpoint Arch-Lib. Отдельной канонической БЗ в AI нет.
3. **DuckDB — движок запросов к Parquet.** Runtime использует `read_parquet()` и SQL-view, а не версионируемую вторую базу `.duckdb`. Имеющаяся `Seasons-Arch/10_database/seasons.duckdb` — существующий источник/индекс Arch-Lib, её миграционный статус проверяется отдельно.
4. **Python движок — собственный код репозитория.** Сохраняем `src/seasons_agent`, `src/seasons_effects`, тесты, сценарии, DSL/AST, контракты, фикстуры; экспериментальные модули не объявляются реализованными без oracle/regression.
5. **`research/` — компактные материалы для проверки, не канон.** Непроверенные observations, открытые вопросы и отчёты допускаются, но исходные «аналитические пакеты» должны быть интегрированы/адресованы и выведены из активной структуры.
6. **Сканы и первичные PDF в Git не копируем.** Их байты остаются в Arch-Lib; в репозитории только стабильные ссылки, хеши, версии, ROI/page anchors и права использования.
7. **Нет удаления без доказанной интеграции.** Неизменённый начальный ZIP, уникальные доказательства, история и исправные реализации не теряются.

## 2. Источники истины и право изменять карточные факты

| Слой | Назначение | Может принимать карточный факт? |
|---|---|---|
| Official/physical source bytes в Arch-Lib | Основание для проверки печатного текста и правил | Нет — доказательство |
| `research/` / intake | Наблюдения, OCR, расхождения, сценарии проверки | Нет — только кандидаты |
| **Arch-Lib / Seasons-Arch** | Стабильные сущности, revisions, source refs, решения | **Да, после проверки** |
| `db/*.parquet` в Seasons AI | Воспроизводимый снимок версии Arch-Lib | Нет — экспорт |
| DuckDB runtime VIEW | Фильтрация принятых фактов по pool/ruleset/дате | Нет — чтение |
| `src/`, `tests/` | Алгоритмы, состояния, воспроизведение правил | Нет — реализуют, но не переопределяют факты |

**Запрещённый цикл:** править `db/cards.parquet` или Python handler для исправления текста карты, не изменив сначала принятую запись и source chain в Arch-Lib.

## 3. Размещение на рабочем Google Drive

```text
<seasons-ai-working-root>/
  seasons-ai.zip                    # исходный неизменяемый архив, SHA сохранён
  00_seasons-ai_unpacked/          # полный исходный snapshot: только для сверки
  01_seasons-ai_curated/           # очищенный репозиторий, целевой release
  02_intake_and_disposition/      # временная миграция аналитики, не в релизе
  90_evidence_vault/              # уникальная история/доказательства вне Git
```

Текущая папка `00_seasons-ai_unpacked` в Google Drive создана, но на момент составления этой редакции **ещё не заполнена**: локальная распаковка не равнозначна загрузке в Drive.

## 4. Целевая структура `01_seasons-ai_curated/`

```text
README.md
pyproject.toml
uv.lock
.gitignore
src/
  seasons_agent/
  seasons_effects/
tests/
  fixtures/                         # минимальные адресуемые и проверенные фикстуры
db/
  manifest.json                     # checkpoint + hash + schema + status/coverage
  schema.json
  products.parquet
  product_editions.parquet
  cards.parquet
  card_printings.parquet
  card_text_versions.parquet
  card_costs.parquet
  effects.parquet
  rules_documents.parquet
  rules_sections.parquet
  rule_atoms.parquet                # появится только после верифицированной атомизации
  rulings.parquet
  season_dice.parquet
  die_faces.parquet
  transmutation_rates.parquet
  season_resource_rates.parquet
  sources.parquet
  image_assets.parquet
  image_card_map.parquet
  card_pools.parquet                 # если поддерживается принятым Arch-Lib срезом
  pool_membership.parquet           # если поддерживается принятым Arch-Lib срезом
  queries.sql                       # accepted runtime views + отдельные QA views
research/
  status.md                         # текущая картина только с ссылками на source
  coverage.csv
  open_questions.csv
  decisions.md                      # ссылки на решения в Arch-Lib, не их дубликат
  candidates/                       # только текущие нерешённые наблюдения
  source_crosswalk.csv
tools/
  export_archlib.py
  build_parquet.py
  validate_export.py
  compare_checkpoints.py
docs/
  architecture.md
  mechanics.md
  effect_ast_contract.md
  mapping_archlib_to_runtime.md
qa/
  BASELINE.md
  coverage.json
  release_validation.json
  disposition_ledger.csv
```

Примечания:
- Список Parquet файлов — **целевая логическая схема**, не утверждение, что каждый набор данных уже принят или вообще существует в указанной форме. Наличие таблиц проверяем до экспорта; отсутствующие не подменяем пустыми «успешными» таблицами.
- `rule_atoms` — предлагаемый новый слой на основе `rules_sections`, FAQ/errata и эффектов. **96 секций правил != 96 проверенных атомов**.
- `image_assets` и `image_card_map` фиксируют адресуемые источники; никаких больших графических файлов и PDF в репозитории.
- `card_pools`/`pool_membership` нужны для явного сценария (base, Enchanted Kingdom, Path of Destiny, promos) с привязкой к официальным ограничениям, но не требуют дробления на отдельные БД.
- Исторический `.git` бережно сохраняется в исходном snapshot/evidence, новое чистое дерево получает самостоятельную прозрачную историю после проверки lineage.

## 5. Таблицы и ключи Seasons

- **`cards`** — логическая идентичность; стабильный `card_id`, не название и не номер скана.
- **`card_printings`** — физическая печать `printing_id` с product/edition/language/copies и `source_id`; печать не равна логической карте.
- **`card_text_versions`** — `printed`, `errata`, `translation`, `effective`; `valid_from/valid_to` отличны от `recorded_at`.
- **`card_costs`** — напечатанная стоимость, цена применения и правила оплаты не смешиваются; UNKNOWN не записывать как 0.
- **`effects`** — card/text -> AST/DSL, parser version, source refs и **два независимых статуса**: (а) факт/текст проверен; (б) семантика/реализация прошла oracle. `SUPPORTED` означает доказанную поддержку, не наличие handler.
- **`rules_documents`, `rules_sections`, `rule_atoms`, `rulings`** — официальные документы, точные цитатные якоря, тайминг, триггеры, приоритет, исключения, source lineage, revision.
- **`season_dice`, `die_faces`, `transmutation_rates`, `season_resource_rates`** — кубики, значения граней и сезонная экономика. Для каждой ячейки — источник и область действия.
- **`products`, `product_editions`, `card_pools`, `pool_membership`** — base/EK/PoD/promo, редакции, локализации, число физических экземпляров и фильтр конкретной партии; будущие продукты входят в один `dataset_id`.
- **`sources`, `image_assets`, `image_card_map`** — source IDs, authority, rights, versions, SHA, locators, image/ROI mapping.

Все FK/identity crosswalk проверяются; структурированный эффект не заменяет оригинальный текст.

## 6. Проверенный корпус vs исполняемая реализация

Статусы должны быть ортогональными:

| Измерение | Примеры |
|---|---|
| Наличие источника | acquired / missing / inaccessible |
| Статус записи | candidate / accepted / conflicted / rejected / withdrawn |
| Тип текста | printed / errata / translation / effective |
| Парсинг эффекта | unparsed / parsed / partial |
| Готовность Python | unsupported / partial / implemented |
| Внешняя проверка | no oracle / scenario verified / oracle verified |

Нельзя выводить `implemented` из наличия исходного текста или кода и считать «схема валидна» равнозначным «игра реализована».

## 7. Manifest и детерминированный экспорт

`db/manifest.json` фиксирует:

- `dataset_id`, `archlib_checkpoint_id`, `schema_version`, `build_tool_version`, `export_policy_version`;
- `knowledge_as_of`, выбранные правила, языки, продуктовые scope, `pool_id` и `ruleset_id`;
- файлы Parquet: `table_name`, `row_count`, SHA-256, schema fingerprint, lineage/checkpoint;
- отклонения, warnings и coverage по источникам/печатным полям/эффектам/правилам;
- версии writer/dependencies и зафиксированные параметры, влияющие на воспроизводимость байтов.

Два последовательных экспорта одного checkpoint с одним окружением должны давать одинаковые row sets и хеши. Runtime-view **пропускает только принятые и применимые** записи. Спорные/candidate — доступны лишь диагностикой или в `research/`, никогда не внедряются в игру незаметно.

## 8. Переход от нынешнего Seasons AI

1. Заморозить исходный ZIP и текущую Seasons-Arch: исходные хеши, `R0000` ledger.
2. Провести diff существующей `Seasons-Arch/10_database/seasons.duckdb` и её CSV/Parquet/receipts, а также включённых в архив Python data releases. **75 таблиц — число из исторического `duckdb_build_report.json`, не подтверждённое текущее состояние.**
3. Построить карту `Arch-Lib table/field -> runtime Parquet -> Python consumer`; выявить ручное дублирование правил/текстов в коде.
4. Переносить только нужные для игры и QA таблицы, сохраняя все FK и исходные ссылки. Отдельно проверить 95 `cards`, 147 `card_printings`, 146 `card_text_versions`, 162 `effects` (47 structured), 120 `die_faces`, 96 `rules_sections`, 25 `rulings` из исторического отчёта; не объявлять их current/accepted без свежего readback.
5. Сохранить и проверить `src/seasons_agent`, `src/seasons_effects`, CLI, fixtures, тесты и пригодные инструменты; не переносить `.venv`, `.pyc`, bytecode, дубликаты `.duckdb`, тяжёлые исходники PDF/изображений.
6. Для каждого `insights/`, `strategy/`, `formalization/`, `reports/`, `quarantine/` и остальных аналитических входов — `disposition_ledger`: `INTEGRATED`, `ALREADY_IN_ARCHLIB`, `ARCHIVED_EVIDENCE`, `UNRESOLVED_KEEP`, `DERIVED_REGENERABLE`, `EXACT_DUPLICATE`.
7. Удаление из активного проекта — **только** после проверки `source -> assertion -> accepted record/decision -> consumer` и наличия восстановимого архивного источника.
8. Сгенерировать Parquet, выполнить запросы DuckDB, regression/negative/source-gated тесты; зафиксировать coverage и список известных ограничений.
9. Только после QA опубликовать `LATEST` нового release; Архив/история остаются доступными по адресуемым локаторам.

## 9. Ворота приёмки

- Записи с `candidate/conflicted` не попадают в runtime VIEW.
- Каждая `accepted` карточка, печать, версия текста и правило имеет source ref и корректный edition/ruleset scope.
- FK, count, schema, SHA, source locators проходят автоматические проверки.
- Для всего исполняемого действия известны legal timing, resource/cost и choice semantics либо явно показано `UNSUPPORTED`.
- Перезапуск export одного checkpoint не меняет содержательные строки и хеши.
- Все исторические аналитические файлы имеют disposition; нет неучтённых зависимостей.
- Все пригодные наработки Python и тесты сохранены; отделены experimental от verified.
- Никакие прежние неподтверждённые эффекты не становятся «верифицированными» автоматически.

## 10. Решение относительно R0000

Содержимое прошлого плана R0000 **сохраняется как граф работ**, но целевой раздел `knowledge/` заменяется на `db/*.parquet + db/manifest.json + db/queries.sql`; `research/` остаётся компактным входом для проверки, а не местом для пожизненного хранения разрозненных аналитических ZIP. Полные первичные source bytes и evidence живут в Arch-Lib/вне Git. Не требуется хранить готовый `seasons.duckdb` как вторую редактируемую БЗ в Python-репозитории.

**Следующее действие (R0001):** инвентаризация реального канонического checkpoint и runtime dependencies, затем таблица `KEEP / GENERATE / ARCHIVE / DROP_AFTER_VERIFICATION` по каждому файлу и каждой требуемой таблице.
