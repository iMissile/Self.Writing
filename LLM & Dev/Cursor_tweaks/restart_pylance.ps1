# Скрипт для перезапуска Pylance и очистки кэша
Write-Host "Перезапуск Pylance..." -ForegroundColor Green

# Очистка кэша Pylance (если нужно)
$cachePath = "$env:APPDATA\Code\User\workspaceStorage"
if (Test-Path $cachePath) {
    Write-Host "Кэш находится в: $cachePath" -ForegroundColor Yellow
    Write-Host "Для полной очистки удалите папки workspaceStorage вручную" -ForegroundColor Yellow
}

Write-Host "`nДля перезапуска Pylance:" -ForegroundColor Cyan
Write-Host "1. Нажмите Ctrl+Shift+P" -ForegroundColor White
Write-Host "2. Выполните: Python: Restart Language Server" -ForegroundColor White
Write-Host "`nИли перезагрузите окно:" -ForegroundColor Cyan
Write-Host "1. Нажмите Ctrl+Shift+P" -ForegroundColor White
Write-Host "2. Выполните: Developer: Reload Window" -ForegroundColor White







