- # Russian

  ## Общее

  - Всегда отвечай на русском.
  - Лаконично, но исчерпывающе; экономь токены.
  - Не хватает входных данных — спрашивай, не додумывай.
  - Не удаляй закомментированные строки — это часть исследования. Только по явной просьбе.
  - Python 3.13: современные конструкции приветствуются. Код компактный.

  ## Окружение и CLI

  - `git` — всегда с `--no-pager`.
  - Использовать `venv`, если он есть.
  - Определять ОС в рантайме (Windows 10 / macOS / Linux) и выставлять кодовую страницу терминала.
  - Прод-DuckDB по фиксированному пути; переключатель путей — три взаимоисключающих чанка в `.qmd`.

  ## Импорты — только верхний уровень

  - `.py`: все импорты вверху (после shebang/docstring). Запрещены импорты внутри функций/классов/условий/по ходу кода. Исключение — ленивый импорт при циклических зависимостях, с комментарием.
  - `.qmd`: все импорты в setup-чанке в самом начале; в других чанках запрещены.
  - Нарушение = ошибка стиля.

  ## Polars

  - Идиоматичный Polars: цепочки, векторизация, никаких построчных циклов.
  - `polars.selectors` (`cs`) вместо ручных сравнений dtype-строк.
  - Regexp: lookahead/lookbehind не поддерживаются — переписать паттерн или разбить на шаги.
  - pandas избегать всячески. Допустим только если задача без него нерешаема (обычно — финальный шаг отрисовки графика); при использовании — узкий локальный участок, обратно в Polars как можно раньше.
  - Имена колонок — английские; русские подписи только на слое вывода (`gt(labels=)`, `react(names=)`, `labs()`/`scale_*`).

  ## DuckDB

  - Колонки в латинице; русские имена — через таблицу локализации и вьюхи.
  - Polars → DuckDB напрямую (Arrow, zero-copy): без `.to_pandas()` и без `.register()`.
  - `CREATE OR REPLACE TABLE ... AS SELECT * FROM df` вместо защитных ветвлений.
  - Соединение — `with duckdb.connect(...) as con`, не `try/finally`.
  - Хранилище: DuckDB + parquet.

  ## Таблицы

  - `reactable` — если строк потенциально больше 10–15 или нужны сортировка/поиск.
  - `great_tables` (GT) — маленькие фиксированные выборки.
  - ColumnGroup / spanner — поясняющее средство, не декор.
  - **GT + `tab_spanner`:** неспаннированные колонки переносятся в начало шапки, а тело остаётся в исходном порядке → подписи расходятся с данными. Перед `tab_spanner` явно фиксировать порядок колонок (порядок в DataFrame / `cols_move`) и сверять каждую таблицу.
  - `table_font_size="14px"` минимум, меньше — нельзя.

  ## Графики

  - Интерактив: приоритет — echarts; plotly допустим как альтернатива. Статика — plotnine.
  - Порядок категорий на осях — через `pl.Enum`, без `reorder()`-выражений в стиле patsy.

  ## Jupyter / Quarto

  - Автоматически отображается только последнее выражение ячейки; в ветке `if` — не отображается. Любой вывод — через явную отрисовку.
  - Однородность отчёта: в пределах одного `.qmd` держать единый набор библиотек и подходов (один графический движок, один табличный стиль, одна схема именования). Не смешивать echarts и plotly в одном отчёте без причины.

  ## Стек

  - Обработка: Polars (основной), DuckDB, pandas (крайняя мера)
  - Отчёты/визуализация: Quarto (`.qmd`), echarts (приоритет), plotly, plotnine, great_tables, reactable, pointblank
  - LLM: `chatlas.ChatDeepSeek` + локальный JSON-кеш по ключу `PROMPT_VERSION|input`
  - Excel: xlsxwriter (`constant_memory=True` для больших листов); жирные чёрные заголовки на фоне `#D9E1F2`; freeze panes; autofilter; фиксированная ширина для колонок с длинным текстом
  - PDF: pdfplumber

  ---

  # English

  ## General

  - Always respond in Russian.
  - Concise but comprehensive; save tokens.
  - If input data is insufficient — ask, don't guess.
  - Never delete commented-out lines — they are part of the investigation. Only on explicit request.
  - Python 3.13: modern language features welcome. Keep code compact.

  ## Environment & CLI

  - `git` — always with `--no-pager`.
  - Use `venv` if present.
  - Detect the OS at runtime (Windows 10 / macOS / Linux) and apply the right terminal code page.
  - Production DuckDB at a fixed path; path switcher = three mutually exclusive chunks in `.qmd`.

  ## Imports — top-level only

  - `.py`: all imports at the top (after shebang/docstring). Forbidden inside functions/classes/conditionals/mid-code. Exception — lazy import for circular deps, with a comment.
  - `.qmd`: all imports in the setup chunk at the very beginning; forbidden in other chunks.
  - Violation = style error.

  ## Polars

  - Polars-idiomatic: chains, vectorization, no row-wise loops.
  - `polars.selectors` (`cs`) over manual dtype-string comparisons.
  - Regexp: lookahead/lookbehind unsupported — rewrite the pattern or split into steps.
  - Avoid pandas by every means. Acceptable only when the task is unsolvable without it (usually the final plotting step); keep it to a narrow local segment and return to Polars as early as possible.
  - Column names in English; Russian labels only at the output layer (`gt(labels=)`, `react(names=)`, `labs()`/`scale_*`).

  ## DuckDB

  - Latin column names; Russian names via localization table and views.
  - Polars → DuckDB directly (Arrow, zero-copy): no `.to_pandas()`, no `.register()`.
  - `CREATE OR REPLACE TABLE ... AS SELECT * FROM df` instead of defensive branching.
  - Connections via `with duckdb.connect(...) as con`, not `try/finally`.
  - Storage: DuckDB + parquet.

  ## Tables

  - `reactable` — when rows potentially exceed 10–15, or sorting/search is needed.
  - `great_tables` (GT) — small fixed selections.
  - ColumnGroup / spanner — an explanatory device, not decoration.
  - **GT + `tab_spanner`:** un-spanned columns get moved to the front of the header while the body keeps its original order → labels drift out of sync with data. Pin column order explicitly before `tab_spanner` (DataFrame order / `cols_move`) and verify every table.
  - `table_font_size="14px"` minimum, never smaller.

  ## Charts

  - Interactive: echarts is the priority; plotly is an acceptable alternative. Static — plotnine.
  - Axis category ordering via `pl.Enum`, no patsy-style `reorder()` expressions.

  ## Jupyter / Quarto

  - Only the last expression in a cell renders automatically; expressions inside an `if` branch do not. All output must be forced explicitly.
  - Report homogeneity: within a single `.qmd`, keep one consistent set of libraries and approaches (one chart engine, one table style, one naming scheme). Don't mix echarts and plotly in the same report without a reason.

  ## Stack

  - Processing: Polars (primary), DuckDB, pandas (last resort)
  - Reports/visualization: Quarto (`.qmd`), echarts (priority), plotly, plotnine, great_tables, reactable, pointblank
  - LLM: `chatlas.ChatDeepSeek` + local JSON cache keyed by `PROMPT_VERSION|input`
  - Excel: xlsxwriter (`constant_memory=True` for large sheets); bold black headers on `#D9E1F2`; freeze panes; autofilter; fixed-width columns for large text columns
  - PDF: pdfplumber
