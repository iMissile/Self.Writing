# Russian

## Polars и data-пайплайны (для Python/Qmd/Jupyter)

- Пиши polars-идиоматичный код: цепочки, векторизация, без циклов по строкам.
- Regexp в Polars: lookahead/lookbehind не поддерживаются — переписывай паттерн или разбивай на шаги.
- Где уместно — polars selectors (`cs`) для пайплайнов.
- Колонки во фреймах — английские имена; подписи в таблицах/графиках — через name/label.
- Избегай pandas: держи в Polars; в pandas — только финальный шаг вывода графика, если без этого никак.
- Пиши компактный код.

## Общее

- Отвечай лаконично, но исчерпывающе. Экономь токены.
- Если не хватает входных данных — запрашивай.
- Python 3.13 — можно использовать актуальные конструкции языка.



# English

## IDE
- Always respond in Russian
- Always use git --no-pager to void interactivity during agent mode
- Always use venv if it present.
- When executing CLI functions, detect the execution OS at runtime and apply the appropriate code page settings for terminal commands. I work equally across Windows 10, macOS, and Linux.


## Polars and Data Pipelines (for Python/Qmd/Jupyter)

- Write polars-idiomatic code: chains, vectorization, no row-wise loops.
- Regexp in Polars: lookahead/lookbehind are not supported — rewrite the pattern or break into steps.
- Where appropriate — use polars selectors (`cs`) for pipelines.
- Column names in frames — English; labels in tables/charts — via name/label.
- Avoid pandas: stay in Polars; use pandas only for the final chart output step if unavoidable.
- Write compact code.
- Python 3.13 — feel free to use modern language features.
- Don’t remove commented lines, as they are part of the investigation. I will explicitly tell you if I need comments removed
- In Jupyter/Quarto, only the last expression is automatically displayed in a cell. Expressions in the if branch are not rendered automatically. All output must be framed in forced rendering.

## Code quality standards (explicit)

- Column names: English in all DataFrames; Russian display labels pushed to output layer via gt(..., labels=...), react(..., names=...), labs()/scale_* in plotnine
- Polars-first: Maximum Polars usage; pandas only at final plotting step
- Axis ordering: Use pl.Enum for axis ordering in plotnine — no patsy-style reorder() expressions
- Selectors: Use polars.selectors (cs.by_dtype()) over manual dtype string comparisons
- Table font size: table_font_size="14px" minimum in great_tables — never smaller
- DuckDB columns: All in Latin; Russian names via localization table and views only

## Tools & resources

- Data processing: Polars (primary), DuckDB, pandas (conversion at final plotting step only if polars only impossible)
- Report/visualization: Quarto (.qmd), plotnine, echarts, great_tables (GT), reactable, pointblank
- LLM integration: chatlas.ChatDeepSeek with local JSON cache keyed by PROMPT_VERSION|input
- Excel output: xlsxwriter (constant_memory=True for large sheets); bold black headers on 
  #D9E1F2 background; freeze panes; autofilter; fixed-width columns for large text columns
- PDF parsing: pdfplumber
- Storage: DuckDB + parquet; long form as base table, wide form as view
- Environment: Windows+Linux+MacOS, local production DuckDB at fixed path with path switcher in three mutex chunks in .qmd

## General for Web-chat AI like Claude Web

- Respond concisely but comprehensively. Save tokens.
- If input data is insufficient — ask.
