# Quarto `.vdoc.*.py`: убрать мерцание Problems в IDE

Инструкция для Cursor / VS Code. Применять в каждом репозитории с `.qmd` (и один раз глобально).

## В чём проблема

Расширение Quarto для каждой Python-ячейки создаёт временный «виртуальный документ»:

```text
.vdoc.<uuid>.py
```

Часто лежит в `%TEMP%` (Windows) или рядом с `.qmd`. Pylint / Pylance анализируют его **как обычный `.py`**, но **каждый чанк изолированно** — без переменных из соседних ячеек. В панели **Problems** появляются ложные `undefined-variable` / `used-before-assignment`, файлы постоянно пересоздаются → панель мерцает.

Это не ошибки вашего кода.

---

## 1. Глобально (User settings) — сделать один раз

Файл: `%APPDATA%\Cursor\User\settings.json`  
(Cursor: `Ctrl+Shift+P` → **Preferences: Open User Settings (JSON)**)

Добавить:

```json
{
  "quarto.cells.diagnostics.enabled": false,
  "quarto.cells.diagnostics.debounceDelay": 1000,
  "pylint.ignorePatterns": [
    "*\\.vdoc.*.py"
  ]
}
```

| Ключ | Зачем |
|------|--------|
| `quarto.cells.diagnostics.enabled: false` | Quarto не публикует диагностики ячеек в Problems |
| `pylint.ignorePatterns` | Pylint не линтит `.vdoc.*.py` даже в `%TEMP%` |
| `debounceDelay` | Если diagnostics всё же включите — реже дёргать панель |

После правки: `Ctrl+Shift+P` → **Developer: Reload Window**.  
Если хвост остался: **Pylint: Restart Server**.

---

## 2. В репозитории (workspace) — для каждого проекта с `.qmd`

### 2.1. `.vscode/settings.json`

Если файл в `.gitignore` (как в `boq`) — создать локально. Пример:

```json
{
  "python.linting.pylintArgs": [
    "--ignore-patterns=^\\.vdoc\\..*\\.py$"
  ],
  "pylint.ignorePatterns": [
    "*\\.vdoc.*.py"
  ],
  "python.analysis.exclude": [
    "**/.vdoc.*.py"
  ],
  "files.watcherExclude": {
    "**/.vdoc.*.py": true
  }
}
```

| Ключ | Зачем |
|------|--------|
| `pylintArgs` / `ignorePatterns` | Игнор на уровне workspace |
| `python.analysis.exclude` | Pylance не анализирует vdoc |
| `files.watcherExclude` | Меньше мерцания от пересоздания файлов |

Опционально в том же файле (дубль глобального, если User settings не подхватились):

```json
"quarto.cells.diagnostics.enabled": false
```

### 2.2. `pyproject.toml` (если используете Pylint из CLI / конфига проекта)

```toml
[tool.pylint.main]
ignore-patterns = ["^\\.vdoc\\..*\\.py$"]
```

Старое имя секции тоже встречается: `[tool.pylint.MASTER]` — эквивалентно для многих версий; предпочтительно `[tool.pylint.main]`.

**Важно:** vdoc в `%TEMP%` часто **не видит** `pyproject.toml` репозитория. Для IDE критичны User/workspace settings (п. 1–2.1), а не только `pyproject.toml`.

### 2.3. `.gitignore`

```gitignore
**/.vdoc.*.py
```

Чтобы временные файлы не попадали в Source Control, если Quarto положит их рядом с `.qmd`.

### 2.4. (Опционально) `.pylintrc` в корне

Нужен, если хотите явно указать rcfile для файлов вне репо (Temp):

```ini
[MAIN]
ignore-patterns=^\.vdoc\..*\.py$
```

И в `.vscode/settings.json`:

```json
"pylint.args": ["--rcfile=${workspaceFolder}/.pylintrc"]
```

Обычно достаточно п. 1 + 2.1; `.pylintrc` — запасной вариант.

---

## 3. Внутри `.qmd` (точечно, не замена игнора)

Если Problems всё ещё ругается на переменные «из другого чанка» в самом редакторе ячейки, в начало Python-чанка:

```python
# pylint: disable=undefined-variable,used-before-assignment
```

Или для всего файла-чанка:

```python
# pylint: skip-file
```

Это костыль на уровне ячейки. Сначала применяйте п. 1–2.

---

## Чеклист на новый репозиторий

- [ ] Глобально уже есть `quarto.cells.diagnostics.enabled: false` и `pylint.ignorePatterns` (п. 1)
- [ ] В проекте: `.vscode/settings.json` с exclude / ignore / watcherExclude (п. 2.1)
- [ ] В `.gitignore`: `**/.vdoc.*.py` (п. 2.3)
- [ ] По желанию: `[tool.pylint.main] ignore-patterns` в `pyproject.toml` (п. 2.2)
- [ ] `Developer: Reload Window`
- [ ] Закрыть уже открытые вкладки `.vdoc.*.py`, если остались

---

## Как проверить, что сработало

1. Открыть любой `.qmd` с несколькими Python-чанками.
2. Панель **Problems** не должна заполняться ошибками из путей вида `…\Temp\…\.vdoc….py`.
3. При правке/сохранении `.qmd` счётчик Problems не должен резко скакать из‑за пересоздания vdoc.

Если мерцание осталось — смотреть источник диагностики в Problems (Quarto / Pylint / Pylance) и усилить соответствующий слой из таблицы выше.
