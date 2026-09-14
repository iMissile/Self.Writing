# Диагностика конфликтов LSP для Python в Cursor

## Проблема

В Cursor могут одновременно работать несколько Language Server Protocol (LSP) серверов для Python, что приводит к конфликтам:
- **Pyright/Pylance** (встроенный в Cursor)
- **Python Language Server (pylsp)** с плагинами (mypy, pylint и др.)
- **Jedi** (старый, но иногда активируется)

## Диагностика

### Шаг 1: Проверка активных LSP серверов

1. Откройте **Output** панель:
   - `Ctrl+Shift+P` → `Output: Show Output Channel`
   - Проверьте каналы:
     - `Python` или `Pylance`
     - `Pyright`
     - `Python Language Server` или `pylsp`
     - `Jedi`

2. Проверьте статус-бар (внизу справа):
   - Должен быть только один индикатор Python LSP
   - Если видите несколько - это конфликт

3. Проверьте расширения:
   - `Ctrl+Shift+X` → откройте Extensions
   - Найдите установленные расширения Python:
     - **Python** (Microsoft) - использует Pylance/Pyright
     - **Python Language Server** - использует pylsp
     - **Jedi** - старый LSP сервер

### Шаг 2: Проверка конфигурации

В вашем проекте есть:
- `pyrightconfig.json` - конфигурация для Pyright
- `pylsp-mypy.cfg` - конфигурация для pylsp-mypy (указывает на использование pylsp)

## Решения

### Решение 1: Использовать только Pyright/Pylance (рекомендуется для Cursor)

Pyright/Pylance - это встроенный и рекомендуемый LSP для Cursor. Отключите pylsp:

1. **Создайте/отредактируйте `.vscode/settings.json`**:

```json
{
  "python.languageServer": "Pylance",
  "python.analysis.typeCheckingMode": "basic",
  "python.analysis.autoImportCompletions": true,
  "python.analysis.indexing": true,
  "python.analysis.diagnosticMode": "workspace",

  // Отключить другие LSP серверы
  "python.languageServer": "Pylance",
  "jedi.enabled": false,

  // Если установлен pylsp, отключите его
  "python.languageServer": "Pylance"
}
```

2. **Удалите или переименуйте `pylsp-mypy.cfg`** (если не используете pylsp):
   ```powershell
   Rename-Item pylsp-mypy.cfg pylsp-mypy.cfg.disabled
   ```

3. **Перезапустите Cursor**:
   - `Ctrl+Shift+P` → `Developer: Reload Window`

### Решение 2: Использовать только pylsp (если нужны специфичные плагины)

Если вам нужны плагины pylsp (mypy, pylint и др.):

1. **Создайте/отредактируйте `.vscode/settings.json`**:

```json
{
  "python.languageServer": "Pylsp",
  "pylsp.plugins.pylsp_mypy.enabled": true,
  "pylsp.plugins.pylsp_mypy.live_mode": true,
  "pylsp.plugins.pylsp_mypy.strict": true,

  // Отключить Pylance
  "python.analysis.disabled": [],
  "jedi.enabled": false
}
```

2. **Установите pylsp и плагины** (если не установлены):
   ```powershell
   pip install python-lsp-server[all] pylsp-mypy
   ```

3. **Перезапустите Cursor**

### Решение 3: Гибридный подход (Pyright + mypy отдельно)

Используйте Pyright для автодополнения и проверки типов, а mypy запускайте отдельно:

1. **`.vscode/settings.json`**:
```json
{
  "python.languageServer": "Pylance",
  "python.analysis.typeCheckingMode": "basic",
  "jedi.enabled": false
}
```

2. **Запускайте mypy вручную или через pre-commit** (у вас уже настроено в `.pre-commit-config.yaml`)

## Быстрая диагностика конфликтов

### Команда для проверки активных процессов LSP:

```powershell
# Проверка процессов Python LSP
Get-Process | Where-Object {$_.ProcessName -like "*python*" -or $_.ProcessName -like "*node*"} | Select-Object ProcessName, Id, CPU
```

### Проверка логов LSP:

1. `Ctrl+Shift+P` → `Output: Show Output Channel`
2. Выберите канал `Python` или `Pyright`
3. Ищите ошибки типа:
   - "Multiple language servers"
   - "Language server conflict"
   - "Failed to start language server"

## Рекомендации для вашего проекта

Учитывая, что у вас:
- ✅ `pyrightconfig.json` настроен правильно
- ✅ `pyproject.toml` с настройками Pyright
- ⚠️ `pylsp-mypy.cfg` указывает на использование pylsp

**Рекомендация**: Используйте только **Pylance/Pyright** (встроенный в Cursor):

1. Создайте `.vscode/settings.json` с настройками из Решения 1
2. Переименуйте `pylsp-mypy.cfg` в `pylsp-mypy.cfg.disabled`
3. Убедитесь, что расширение "Python Language Server" отключено
4. Перезапустите Cursor

## Проверка после исправления

1. Откройте любой Python файл
2. В статус-баре должно быть только "Pylance" или "Pyright"
3. Проверьте автодополнение (`Ctrl+Space`)
4. Проверьте подсказки типов (наведите на переменную)
5. Проверьте диагностику ошибок (красные подчеркивания)

## Если проблема сохраняется

1. **Очистите кэш**:
   ```powershell
   .\clear_cursor_cache.ps1
   ```

2. **Проверьте версию Python**:
   ```powershell
   python --version
   # Должно быть 3.13
   ```

3. **Проверьте виртуальное окружение**:
   - Убедитесь, что `.venv` активирован
   - В Cursor: `Ctrl+Shift+P` → `Python: Select Interpreter` → выберите `.venv\Scripts\python.exe`

4. **Переустановите расширение Python**:
   - `Ctrl+Shift+X` → найдите "Python" (Microsoft)
   - Отключите → включите снова
   - Перезапустите Cursor

## Полезные команды

- `Ctrl+Shift+P` → `Python: Restart Language Server` - перезапуск LSP
- `Ctrl+Shift+P` → `Developer: Reload Window` - полная перезагрузка
- `Ctrl+Shift+P` → `Python: Select Interpreter` - выбор интерпретатора

