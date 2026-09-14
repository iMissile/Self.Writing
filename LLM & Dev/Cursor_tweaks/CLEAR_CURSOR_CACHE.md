# Как очистить кэш Cursor

## Способ 1: Автоматическая очистка (рекомендуется)

1. **Закройте Cursor полностью** (важно!)
2. Откройте PowerShell в папке проекта
3. Выполните:
   ```powershell
   .\clear_cursor_cache.ps1
   ```
4. Откройте Cursor заново

## Способ 2: Ручная очистка через PowerShell

1. **Закройте Cursor**
2. Откройте PowerShell
3. Выполните команды:

```powershell
# Очистка кэша Cursor
$localAppData = $env:LOCALAPPDATA
$roamingAppData = $env:APPDATA
$userProfile = $env:USERPROFILE

# Удаление папок кэша
Remove-Item -Path "$localAppData\Cursor" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -Path "$roamingAppData\Cursor" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -Path "$userProfile\.cursor" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -Path "$localAppData\Programs\Cursor\Cache" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -Path "$localAppData\Programs\Cursor\User\workspaceStorage" -Recurse -Force -ErrorAction SilentlyContinue

Write-Host "Кэш очищен!" -ForegroundColor Green
```

## Способ 3: Очистка только workspaceStorage (более безопасно)

Если вы хотите очистить только кэш конкретного проекта:

1. **Закройте Cursor**
2. Выполните:
```powershell
$localAppData = $env:LOCALAPPDATA
Remove-Item -Path "$localAppData\Programs\Cursor\User\workspaceStorage\*" -Recurse -Force -ErrorAction SilentlyContinue
```

## Способ 4: Через настройки Cursor (мягкая очистка)

1. Откройте `.vscode/settings.json`
2. Временно измените:
   ```json
   "python.analysis.indexing": false
   ```
3. Сохраните файл
4. Измените обратно:
   ```json
   "python.analysis.indexing": true
   ```
5. Сохраните - это запустит переиндексацию

## Что очищается:

- **workspaceStorage** - кэш индексации проектов
- **Cache** - общий кэш приложения
- **Cursor** - настройки и кэш расширений

## ВАЖНО:

⚠️ **Закройте Cursor перед очисткой кэша!**
⚠️ Очистка кэша удалит локальные настройки workspace, но не затронет файлы проекта
⚠️ После очистки Cursor переиндексирует проект заново (может занять время)

## После очистки:

1. Откройте Cursor
2. Откройте проект
3. Дождитесь завершения индексации (в статус-баре будет "Indexing...")
4. Проверьте работу индексации через `@`


