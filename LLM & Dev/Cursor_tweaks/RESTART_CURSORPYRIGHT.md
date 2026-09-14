# Как перезапустить cursorpyright в Cursor

## Способ 1: Перезагрузка окна (рекомендуется)
1. Нажмите `Ctrl+Shift+P`
2. Выполните: `Developer: Reload Window`
3. Это полностью перезагрузит окно и перезапустит все языковые серверы

## Способ 2: Закрыть и открыть Cursor
- Просто закройте Cursor и откройте его снова
- Это самый надежный способ

## Способ 3: Проверка команд cursorpyright
1. Нажмите `Ctrl+Shift+P`
2. Введите `cursorpyright` или `pyright`
3. Посмотрите доступные команды

## Способ 4: Через настройки (принудительная переиндексация)
1. Временно измените в `.vscode/settings.json`:
   ```json
   "python.analysis.indexing": false
   ```
2. Сохраните файл
3. Измените обратно:
   ```json
   "python.analysis.indexing": true
   ```
4. Сохраните - это запустит переиндексацию

## Проверка работы cursorpyright
1. Откройте любой Python файл
2. В статус-баре (внизу справа) должно быть "Pyright"
3. Если видите ошибки, проверьте Output:
   - `Ctrl+Shift+P` → `Output: Show Output Channel`
   - Выберите "Python" или "Pyright"



