# Быстрое исправление LSP в Cursor

## Что было исправлено

✅ Очищены дубликаты в `.vscode/settings.json`
✅ Настроен только **Pylance** (встроенный LSP для Cursor)
✅ Отключен Jedi
✅ `pylsp-mypy.cfg` уже переименован в `.disabled`

## Что нужно сделать сейчас

### Шаг 1: Перезапустите Cursor

**Вариант А (рекомендуется):**
1. Закройте Cursor полностью
2. Откройте Cursor заново
3. Откройте этот проект

**Вариант Б (быстрый):**
1. Нажмите `Ctrl+Shift+P`
2. Выполните: `Developer: Reload Window`

### Шаг 2: Проверьте работу LSP

1. Откройте любой Python файл (например, `libdocks/main.py`)
2. В **статус-баре** (внизу справа) должно быть **"Pylance"**
3. Проверьте автодополнение: начните печатать код и нажмите `Ctrl+Space`
4. Проверьте подсказки типов: наведите курсор на переменную

### Шаг 3: Если LSP не работает

1. **Проверьте интерпретатор Python:**
   - `Ctrl+Shift+P` → `Python: Select Interpreter`
   - Выберите `.venv\Scripts\python.exe`

2. **Перезапустите LSP вручную:**
   - `Ctrl+Shift+P` → `Python: Restart Language Server`

3. **Проверьте логи:**
   - `Ctrl+Shift+P` → `Output: Show Output Channel`
   - Выберите `Python` или `Pylance`
   - Ищите ошибки

4. **Очистите кэш (если ничего не помогает):**
   ```powershell
   .\clear_cursor_cache.ps1
   ```
   Затем откройте Cursor заново

## Текущие настройки

- **LSP сервер:** Pylance (встроенный в Cursor)
- **Тип проверки:** basic (соответствует `pyrightconfig.json`)
- **Индексация:** включена
- **Автодополнение:** включено
- **Подсказки типов:** включены

## Полезные команды

- `Ctrl+Shift+P` → `Python: Restart Language Server` - перезапуск LSP
- `Ctrl+Shift+P` → `Developer: Reload Window` - полная перезагрузка
- `Ctrl+Shift+P` → `Python: Select Interpreter` - выбор интерпретатора
- `Ctrl+Space` - автодополнение
- `@` - поиск по коду (индексация)

## Если проблема сохраняется

Смотрите подробную диагностику в `LSP_CONFLICTS_DIAGNOSTICS.md`











