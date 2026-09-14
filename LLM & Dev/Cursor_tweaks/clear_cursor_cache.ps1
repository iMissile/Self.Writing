# Скрипт для очистки кэша Cursor
# ВНИМАНИЕ: Закройте Cursor перед выполнением этого скрипта!

Write-Host "Очистка кэша Cursor..." -ForegroundColor Green
Write-Host "Убедитесь, что Cursor закрыт!" -ForegroundColor Yellow
Write-Host ""

$userProfile = $env:USERPROFILE
$localAppData = $env:LOCALAPPDATA
$roamingAppData = $env:APPDATA

# Пути к кэшу Cursor
$cachePaths = @(
    "$localAppData\Cursor",
    "$roamingAppData\Cursor",
    "$userProfile\.cursor",
    "$localAppData\Programs\Cursor\Cache",
    "$localAppData\Programs\Cursor\User\workspaceStorage"
)

$deleted = 0
$errors = 0

foreach ($path in $cachePaths) {
    if (Test-Path $path) {
        try {
            Write-Host "Удаление: $path" -ForegroundColor Cyan
            Remove-Item -Path $path -Recurse -Force -ErrorAction Stop
            $deleted++
            Write-Host "  ✓ Удалено" -ForegroundColor Green
        }
        catch {
            Write-Host "  ✗ Ошибка: $_" -ForegroundColor Red
            $errors++
        }
    }
    else {
        Write-Host "Не найдено: $path" -ForegroundColor Gray
    }
}

Write-Host ""
Write-Host "Очистка завершена!" -ForegroundColor Green
Write-Host "Удалено папок: $deleted" -ForegroundColor Cyan
if ($errors -gt 0) {
    Write-Host "Ошибок: $errors" -ForegroundColor Red
}
Write-Host ""
Write-Host "Теперь можно открыть Cursor заново." -ForegroundColor Yellow


