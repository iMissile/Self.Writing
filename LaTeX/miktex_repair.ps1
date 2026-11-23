<#
.SYNOPSIS
    Диагностика, восстановление пакетов и безопасная пересборка форматов MiKTeX (Windows).

.DESCRIPTION
    Решает две типовые проблемы MiKTeX:
    1) Рассинхрон базы пакетов и файлов на диске (check-update молчит, но verify находит пакеты
       "needs to be reinstalled", включая ltxbase/l3kernel).
    2) Аварийное падение `initexmf --dump` на экспериментальном формате hilatex до пересборки
       xelatex/pdflatex/lualatex — скрипт пересобирает только указанные рабочие форматы.

.EXAMPLE
    .\miktex_repair.ps1 -CheckOnly
    Только диагностика без внесения изменений.

.EXAMPLE
    .\miktex_repair.ps1
    Полный цикл: обновление пакетов, переустановка повреждённых (remove + install),
    обновление FNDB/карт шрифтов, пересборка xelatex/pdflatex/lualatex и финальная проверка.

.EXAMPLE
    .\miktex_repair.ps1 -Repair -RebuildFormats
    Переустановить пакеты из `miktex packages verify` и пересобрать рабочие форматы.

.EXAMPLE
    .\miktex_repair.ps1 -RebuildFormats -Formats @("xelatex", "pdflatex")
    Пересобрать только выбранные форматы, минуя hilatex.
#>
[CmdletBinding()]
param(
    [switch]$CheckOnly,
    [switch]$Update,
    [switch]$Repair,
    [switch]$RebuildFormats,
    [string[]]$Formats = @("xelatex", "pdflatex", "lualatex")
)

$ErrorActionPreference = "Stop"

# Если не задан ни один режим — выполняем полный безопасный цикл обслуживания
if (-not ($CheckOnly -or $Update -or $Repair -or $RebuildFormats)) {
    $Update = $true
    $Repair = $true
    $RebuildFormats = $true
}

function Get-BrokenPackages {
    $output = & miktex packages verify 2>&1
    $broken = @()
    foreach ($line in $output) {
        if ($line -match '^([^:]+): this package needs to be reinstalled\.') {
            $broken += $Matches[1]
        }
    }
    return $broken
}

function Show-Diagnostics {
    Write-Host "=== MiKTeX Setup ===" -ForegroundColor Cyan
    & miktex --version | Select-Object -First 1
    & initexmf --report | Select-String -Pattern "SharedSetup|UserInstall|UserData|CommonInstall|CommonData"

    Write-Host "`n=== Core Files on Disk ===" -ForegroundColor Cyan
    $ltx = & kpsewhich latex.ltx 2>$null
    $expl = & kpsewhich expl3.sty 2>$null
    foreach ($p in @($ltx, $expl)) {
        if ($p -and (Test-Path $p)) {
            $item = Get-Item $p
            Write-Host ("  {0,-75} {1} ({2} bytes)" -f $item.FullName, $item.LastWriteTime.ToString("yyyy-MM-dd HH:mm"), $item.Length)
        }
    }

    Write-Host "`n=== Active Format Kernel (xelatex) ===" -ForegroundColor Cyan
    $xeInfo = & xelatex -interaction=nonstopmode "\stop" 2>&1 | Select-String -Pattern "This is XeTeX|LaTeX2e|L3 programming"
    $xeInfo | ForEach-Object { Write-Host "  $_" }

    Write-Host "`n=== Target Formats Timestamps ===" -ForegroundColor Cyan
    $fmtRoot = Join-Path $env:LOCALAPPDATA "MiKTeX\miktex\data\le"
    if (Test-Path $fmtRoot) {
        $allFmts = Get-ChildItem -Path $fmtRoot -Recurse -Filter "*.fmt" -ErrorAction SilentlyContinue
        foreach ($f in $Formats) {
            $found = $allFmts | Where-Object { $_.BaseName -eq $f } | Select-Object -First 1
            if ($found) {
                Write-Host ("  {0,-16} {1}" -f $found.Name, $found.LastWriteTime.ToString("yyyy-MM-dd HH:mm:ss"))
            } else {
                Write-Host ("  {0,-16} (not built yet)" -f "$f.fmt") -ForegroundColor Yellow
            }
        }
    }

    Write-Host "`n=== Pending Package Updates ===" -ForegroundColor Cyan
    & miktex packages check-update 2>&1 | Select-Object -First 20

    Write-Host "`n=== Package Integrity (miktex packages verify) ===" -ForegroundColor Cyan
    $broken = Get-BrokenPackages
    if ($broken.Count -eq 0) {
        Write-Host "  OK: all installed packages match the database." -ForegroundColor Green
    } else {
        Write-Host ("  FOUND {0} package(s) needing reinstall:" -f $broken.Count) -ForegroundColor Yellow
        Write-Host ("  " + ($broken -join ", "))
    }
}

if ($CheckOnly) {
    Show-Diagnostics
    exit 0
}

if ($Update) {
    Write-Host "=== [1/3] Updating MiKTeX packages ===" -ForegroundColor Cyan
    & miktex packages update
    if ($LASTEXITCODE -ne 0) {
        throw "miktex packages update failed with exit code $LASTEXITCODE"
    }
}

if ($Repair) {
    Write-Host "=== [2/3] Verifying installed packages ===" -ForegroundColor Cyan
    $broken = Get-BrokenPackages
    if ($broken.Count -eq 0) {
        Write-Host "All installed packages are intact; no reinstall needed." -ForegroundColor Green
    } else {
        $listFile = Join-Path $env:TEMP "miktex-reinstall.txt"
        $broken | Set-Content -Path $listFile -Encoding ASCII
        Write-Host ("Reinstalling {0} package(s) from {1}..." -f $broken.Count, $listFile) -ForegroundColor Yellow

        & miktex packages remove --package-id-file="$listFile"
        if ($LASTEXITCODE -ne 0) {
            throw "miktex packages remove failed with exit code $LASTEXITCODE"
        }

        & miktex packages install --package-id-file="$listFile"
        if ($LASTEXITCODE -ne 0) {
            throw "miktex packages install failed with exit code $LASTEXITCODE"
        }
    }
}

if ($RebuildFormats) {
    Write-Host ("=== [3/3] Refreshing FNDB/font maps and rebuilding formats: {0} ===" -f ($Formats -join ", ")) -ForegroundColor Cyan
    $argsList = @("--update-fndb", "--mkmaps")
    foreach ($fmt in $Formats) {
        $argsList += "--dump=$fmt"
    }
    & initexmf @argsList
    if ($LASTEXITCODE -ne 0) {
        throw "initexmf failed with exit code $LASTEXITCODE (see $env:LOCALAPPDATA\MiKTeX\miktex\log\initexmf.log)"
    }
}

Write-Host "`n=== Post-repair Verification ===" -ForegroundColor Cyan
$remaining = Get-BrokenPackages
if ($remaining.Count -eq 0) {
    Write-Host "OK: miktex packages verify passed with 0 broken packages." -ForegroundColor Green
} else {
    Write-Host ("WARN: {0} package(s) still flagged: {1}" -f $remaining.Count, ($remaining -join ", ")) -ForegroundColor Yellow
}

$xeAfter = & xelatex -interaction=nonstopmode "\stop" 2>&1 | Select-String -Pattern "LaTeX2e|L3 programming"
$xeAfter | ForEach-Object { Write-Host "  $_" -ForegroundColor Green }
