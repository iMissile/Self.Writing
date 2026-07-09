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

## General for Cloud

- Respond concisely but comprehensively. Save tokens.
- If input data is insufficient — ask.
