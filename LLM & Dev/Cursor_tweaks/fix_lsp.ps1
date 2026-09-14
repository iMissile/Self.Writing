# Скрипт для исправления проблем с LSP в Cursor
Write-Host "Исправление настроек LSP для Python в Cursor..." -ForegroundColor Green
Write-Host ""

# Проверка наличия .vscode/settings.json
$settingsPath = ".vscode\settings.json"
if (-not (Test-Path $settingsPath)) {
    Write-Host "ОШИБКА: Файл $settingsPath не найден!" -ForegroundColor Red
    exit 1
}

Write-Host "✓ Настройки найдены: $settingsPath" -ForegroundColor Green

# Проверка pylsp-mypy.cfg
if (Test-Path "pylsp-mypy.cfg") {
    Write-Host "⚠ Найден pylsp-mypy.cfg - переименовываю в .disabled..." -ForegroundColor Yellow
    Rename-Item -Path "pylsp-mypy.cfg" -NewName "pylsp-mypy.cfg.disabled" -Force
    Write-Host "✓ Файл переименован" -ForegroundColor Green
} else {
    Write-Host "✓ pylsp-mypy.cfg уже отключен или не найден" -ForegroundColor Green
}

Write-Host ""
Write-Host "Настройки LSP исправлены!" -ForegroundColor Green
Write-Host ""
Write-Host "Следующие шаги:" -ForegroundColor Cyan
Write-Host "1. Закройте Cursor полностью (если открыт)" -ForegroundColor White
Write-Host "2. Откройте Cursor заново" -ForegroundColor White
Write-Host "3. Нажмите Ctrl+Shift+P и выполните: 'Developer: Reload Window'" -ForegroundColor White
Write-Host "4. Проверьте статус-бар (внизу справа) - должно быть 'Pylance'" -ForegroundColor White
Write-Host ""
Write-Host "Или выполните перезапуск LSP:" -ForegroundColor Cyan
Write-Host "   Ctrl+Shift+P → 'Python: Restart Language Server'" -ForegroundColor White
Write-Host ""











