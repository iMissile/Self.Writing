#Requires -Version 5.1
<#
.SYNOPSIS
  User-level env для кэшей uv / EasyOCR / torch на диске D (без TEMP/TMP).

.DESCRIPTION
  Создаёт каталоги и прописывает постоянные переменные пользователя:
    UV_CACHE_DIR        -> D:\uv-cache
    EASYOCR_MODULE_PATH -> D:\ml-cache\EasyOCR
    TORCH_HOME          -> D:\ml-cache\torch

  TEMP/TMP не трогает.
  После запуска перезапустите Cursor / VS Code / Positron / Zed и терминалы.
#>

$ErrorActionPreference = "Stop"

$vars = [ordered]@{
    UV_CACHE_DIR        = "D:\uv-cache"
    EASYOCR_MODULE_PATH = "D:\ml-cache\EasyOCR"
    TORCH_HOME          = "D:\ml-cache\torch"
}

Write-Host "Creating directories..."
foreach ($path in $vars.Values | Select-Object -Unique) {
    New-Item -ItemType Directory -Force -Path $path | Out-Null
    Write-Host "  $path"
}

Write-Host ""
Write-Host "Setting User environment variables..."
foreach ($name in $vars.Keys) {
    $value = $vars[$name]
    $prev = [Environment]::GetEnvironmentVariable($name, "User")
    [Environment]::SetEnvironmentVariable($name, $value, "User")
    # текущая сессия тоже
    Set-Item -Path "Env:$name" -Value $value
    if ($prev -and $prev -ne $value) {
        Write-Host "  $name = $value  (was: $prev)"
    }
    else {
        Write-Host "  $name = $value"
    }
}

Write-Host ""
Write-Host "Verify (User scope):"
foreach ($name in $vars.Keys) {
    $got = [Environment]::GetEnvironmentVariable($name, "User")
    Write-Host ("  {0,-22} {1}" -f $name, $got)
}

Write-Host ""
Write-Host "TEMP/TMP not changed:"
Write-Host ("  TEMP (User)  {0}" -f ([Environment]::GetEnvironmentVariable("TEMP", "User")))
Write-Host ("  TMP  (User)  {0}" -f ([Environment]::GetEnvironmentVariable("TMP", "User")))

$profilePath = Join-Path $HOME "Documents\PowerShell\Microsoft.PowerShell_profile.ps1"
if (Test-Path $profilePath) {
    $hit = Select-String -Path $profilePath -Pattern "UV_CACHE_DIR|EASYOCR_MODULE_PATH|TORCH_HOME" -SimpleMatch -ErrorAction SilentlyContinue
    if ($hit) {
        Write-Host ""
        Write-Host "Note: same vars also appear in PowerShell profile:"
        Write-Host "  $profilePath"
        Write-Host "User env covers all IDEs; you can remove duplicates from the profile if you want."
    }
}

Write-Host ""
Write-Host "Done. Restart IDEs/terminals so new processes inherit User env."
Write-Host "Then:  uv pip install -e `".[ocr-easy]`""
