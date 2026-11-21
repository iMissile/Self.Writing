---
title: "Windows 11: happy path для трёх GitHub Actions Runner и единой среды разработки"
status: "Проверенный по журналам VM-326272; будущие прогоны требуют независимой приёмки"
date: 2026-11-20
revision: "1.0"
host: "VM-326272"
os: "Windows 11 Pro x64, build 22631"
service_account: "VM-326272\\Admin"
setup_script: "Setup-ThreeRunners-DevTools-v1.5.ps1"
tags: [windows, win11, github-actions, runner, rust, miktex, flowbridge, tikzarium, whereisit, qa]
---

# Windows 11 — Happy Path: три runner-а, полный инструментарий и обход всех найденных граблей

**Назначение:** воспроизвести подготовку Windows 11 Pro x64 для **Tikzarium**, **FlowBridge** и **WhereIsIt AI** без ручного повторения прежних неудачных попыток; при повторном запуске **не переустанавливать работающие компоненты**. Это инструкция для инфраструктуры сборки/QA, а не разрешение на публикацию релизов.

**Контрольная дата:** 20 ноября 2026 г. Источник фактической приёмки — терминальные журналы владельца с `VM-326272`, в том числе успешные системный `Install` и обычный `TeXUser` версии **v1.5**. Независимый GitHub `Online/Idle` и реальные сборки трёх репозиториев **не подтверждены только этими логами**.

## 0. Краткий маршрут — только необходимые действия

> На уже подготовленной машине `VM-326272` **не нужно повторять этап регистрации runner-ов**. Начните с блока **5** (проверка итоговых статусов), затем переходите к **6–8**.

| Очередность | На чистой машине | На уже подготовленной `VM-326272` | Признак успеха |
|---|---|---|---|
| 1 | Проверить хост, учётную запись, диск и время | Только контроль | Windows 11 Pro x64; точное UTC; `Admin` |
| 2 | Установить три отдельные runner-службы из проверенного GitHub Runner ZIP | **Пропустить** | Три `.runner`, три службы `Running/Auto` |
| 3 | Подтвердить **GitHub Online/Idle** | **Обязательно** | Каждое имя `online` и `busy=false` |
| 4 | Запустить DevTools **v1.5 Install** в elevated Admin | Уже **PASS**, не повторять без причин | `Exit code: 0`; `RUST_MSVC_SMOKE_PASS`; NSIS `COMPILE PASS` |
| 5 | Запустить **v1.5 TeXUser** в обычном Admin | Уже **PASS** | `AutoInstall=0`; `TEX_PDF_SMOKE_PASS` |
| 6 | При Idle контролируемо обновить окружение служб, если после установки менялся Machine PATH | Пока не подтверждено | Новые service-процессы видят Git/Rust/Node/etc. |
| 7 | Ревью + слияние диагностических workflow; только доверенный `workflow_dispatch` из `main` | Ожидается | Три независимых успешных задания на заданных runner-ах |
| 8 | Отдельные нативные сборки и GUI/QA по репозиториям | Ожидается | Доказательства каждой платформы и сценария отдельно |

**Строгая граница безопасности:** все три runner-службы выполняются от **администратора Windows**. На них **запрещены недоверенные `pull_request` / `pull_request_target` и произвольные непроверенные ветки/скрипты**. Системный установщик **не меняет** UAC, пароли, регистрацию runner-ов, службы, firewall, драйверы, WFP или файлы репозиториев.

## 1. Что подготовить и зафиксировать

### 1.1. Точный хост и файловая структура

```text
VM-326272 — Windows 11 Pro x64, build 22631
Сервисная учётная запись: VM-326272\Admin

C:\Setup\
  win11-github-runners-v1.3\
    Install-Win11Runners.ps1
    Test-Win11Runners.ps1
  Setup-ThreeRunners-DevTools-v1.5.ps1

C:\GitHubRunners\
  win11-tikzarium\
  win11-flowbridge\
  win11-whereisit\

C:\DevTools\
  Rust\cargo\
  Rust\rustup\
  Python313\
  MiKTeX\install\
  MiKTeX\config\
  MiKTeX\data\
  Poppler\
  NSIS\nsis-3.13\
  PortableCLI\
```

Три runner-а изолированы **по каталогам, регистрации, `.service`, workspace и репозиториям**. Никогда не копируйте между ними `.credentials`, `.runner`, сервисные учётные данные или SSH-ключи. Исходники, временные сборки и крупные тестовые данные не складывайте в корень `C:\Setup` или в корень репозиториев.

### 1.2. Подлинный исходник DevTools

Основной исполняемый файл: **`Setup-ThreeRunners-DevTools-v1.5.ps1`**.

Проверенный SHA-256 его байтов:

```text
499C641289DDA26096FBC7B85466FADA1448C5A3238609F51E33B75A46297776
```

Файл должен быть **UTF-8 с BOM**, переносы **CRLF**, совместимый с **Windows PowerShell 5.1**. Проверка хеша и синтаксиса перед установкой:

```powershell
$setup = 'C:\Setup\Setup-ThreeRunners-DevTools-v1.5.ps1'
if (!(Test-Path -LiteralPath $setup -PathType Leaf)) { throw "Missing $setup" }

$expected = '499C641289DDA26096FBC7B85466FADA1448C5A3238609F51E33B75A46297776'
$actual = (Get-FileHash -LiteralPath $setup -Algorithm SHA256).Hash
if ($actual -ine $expected) { throw "Wrong script SHA256: $actual" }

$bytes = [IO.File]::ReadAllBytes($setup)
if ($bytes.Length -lt 3 -or $bytes[0] -ne 0xEF -or
    $bytes[1] -ne 0xBB -or $bytes[2] -ne 0xBF) {
    throw 'UTF-8 BOM missing: PS5.1 Cyrillic parsing is unsafe'
}

$tokens = $null
$errors = $null
[void][System.Management.Automation.Language.Parser]::ParseFile(
    $setup, [ref]$tokens, [ref]$errors
)
if ($errors.Count -gt 0) {
    $errors | Format-List
    throw 'PS5.1 parse failed'
}
'BOOTSTRAP_SOURCE_PASS'
```

**Важно:** SHA-256 выше относится именно к v1.5. Если файл редактировался, **не подменяйте** ожидаемый хеш результатом собственного `Get-FileHash` без ревью изменений.

### 1.3. Проверка машины (в elevated PowerShell 5.1)

```powershell
$os = Get-CimInstance Win32_OperatingSystem
$id = [Security.Principal.WindowsIdentity]::GetCurrent()
$p = New-Object Security.Principal.WindowsPrincipal($id)
[pscustomobject]@{
    Computer  = $env:COMPUTERNAME
    User      = $id.Name
    OS        = $os.Caption
    Build     = $os.BuildNumber
    PSVersion = $PSVersionTable.PSVersion.ToString()
    Elevated  = $p.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
    FreeCGB   = [math]::Round((Get-PSDrive C).Free / 1GB, 2)
} | Format-List
```

Ожидается `VM-326272`, `VM-326272\Admin`, Windows 11 x64, `Elevated=True`, достаточно свободного диска (у v1.5 порог отказа `20 GiB`, предупреждения — ниже `40 GiB`). На другой VM **осознанно** меняют параметры `-ExpectedComputerName` и `-ExpectedAccount` и отдельно пересматривают имена runner-ов; не обходят host guard пустыми строками.

## 2. Сначала время и сеть, потом регистрация runner-ов

Ошибка **`Failed to create a session. The runner registration has been deleted from the server`** при первых стартах сопровождалась рассинхронизацией времени. Нельзя сразу считать её основанием повторно регистрировать runner или чинить ACL.

### 2.1. Независимая сверка UTC с GitHub

Открыть PowerShell под `Admin` (для этой проверки elevation не требуется):

```powershell
$ErrorActionPreference = 'Stop'
$response = Invoke-WebRequest -UseBasicParsing `
    -Uri 'https://api.github.com/' `
    -Headers @{ 'User-Agent' = 'VM-326272-ClockCheck' }

$githubUtc = [DateTimeOffset]::Parse($response.Headers['Date']).UtcDateTime
$localUtc = [DateTime]::UtcNow
$skew = [math]::Round(($localUtc - $githubUtc).TotalSeconds, 1)
[pscustomobject]@{
    WindowsUTC = $localUtc.ToString('o')
    GitHubUTC  = $githubUtc.ToString('o')
    SkewSeconds = $skew
} | Format-List
if ([math]::Abs($skew) -gt 120) { throw "CLOCK_SKEW: $skew sec" }
```

На успешной машине после синхронизации получено `SkewSeconds ≈ 4.4`. **Часовой пояс UTC сам по себе не чинит системные часы.** Для правильной работы важен именно абсолютный UTC; `tzutil /s UTC` делать необязательно. Ошибочный endpoint диагностики из раннего repair-script возвращал HTTP 404: **не использовать его как доказательство сбоя времени**.

При отклонении: проверить `w32tm /query /status` и `w32tm /query /source`; при необходимости настроить источник времени и выполнить `w32tm /resync` в повышенной консоли. Только после успешной сверки повторять старт listener-а. Не раскрывать токены регистрации в чат или в лог.

### 2.2. Доступ к GitHub

Проверка только TCP 443:

```powershell
'github.com','api.github.com','pipelines.actions.githubusercontent.com' |
    ForEach-Object {
        [pscustomobject]@{
            Host = $_
            Tcp443 = (Test-NetConnection $_ -Port 443 -InformationLevel Quiet)
        }
    } | Format-Table -AutoSize
```

**PASS TCP 443 не гарантирует** правильный HTTPS certificate chain или успешную авторизацию runner-а. Установщик v1.5 проверяет контрольные суммы скачиваемых компонентов; нельзя отключать TLS-проверку ради загрузки.

## 3. Регистрация трёх runner-ов — один раз, только на чистой VM

Если `C:\GitHubRunners\...` уже содержит `.runner` и службы установлены, **этот раздел пропустить**. Не выполняйте повторно `config.cmd` с новыми токенами на уже работающей машине.

### 3.1. Верифицированный GitHub Runner

В принятых логах использован официальный Windows runner **2.338.2**, архив:

```text
actions-runner-win-x64-2.338.2.zip
SHA256: A1F17AA987FC8158BC7521D284912267A0D01B7C2C4684B33C86783B5E8221CC
```

Используйте **существующий, уже проверенный локальный** `Install-Win11Runners.ps1` из пакета `win11-github-runners-v1.3`. Если этого пакета на новой VM нет, получите и проверьте его исходник отдельно: v1.5 DevTools **не** регистрирует runner-ы. Нельзя заменять файлы v1.3 произвольным файлом из чата или новой непроверенной ветки.

### 3.2. Happy-path команда регистрации

В **повышенном** Windows PowerShell 5.1 от имени `VM-326272\Admin`:

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass `
    -File 'C:\Setup\win11-github-runners-v1.3\Install-Win11Runners.ps1' `
    -Project all `
    -ServiceAccount CurrentAdmin `
    -ExpectedComputerName 'VM-326272'
```

Скрипт поочерёдно зарегистрирует:

| Репозиторий | Runner | Каталог |
|---|---|---|
| `i-shutov/tikzarium` | `win11-tikzarium` | `C:\GitHubRunners\win11-tikzarium` |
| `i-shutov/flowbridge` | `win11-flowbridge` | `C:\GitHubRunners\win11-flowbridge` |
| `i-shutov/whereisit-ai` | `win11-whereisit` | `C:\GitHubRunners\win11-whereisit` |

Для каждого репозитория токен брать **только** из его `Settings → Actions → Runners → New self-hosted runner` и вводить **локально в скрытое приглашение**. Не публиковать токен, `.credentials`, файлы конфигурации служб или содержимое `.ssh`.

### 3.3. Самая частая ранняя ошибка: `Отказано в доступе` для `config.cmd`

В первоначальных попытках `config.cmd` и даже `Runner.Listener.exe --version` выдавали `Access denied`. Разрешения самого пользователя `Admin` уже присутствовали — слепое повторное `icacls /grant F` **не помогло**. Установщик v1.3 учитывает прежние инциденты с ACL и проверяет прямой запуск listener-а до запроса токена.

**Если это произошло на новой машине:**

1. Проверить `Runner.Listener.exe --version`, файл и путь, а также события `Microsoft-Windows-CodeIntegrity/Operational` / AppLocker. Не менять UAC и антивирус.
2. Посмотреть наследование NTFS в **конкретном** каталоге `C:\GitHubRunners\win11-<project>`.
3. Исправлять наследование **только** в проверенной папке runner-а при подтверждённом ACL-дефекте; исторически сработал `icacls.exe 'C:\GitHubRunners\win11-tikzarium\*' /inheritance:e /T /Q`. Это не универсальная команда для всей `C:\GitHubRunners`, `C:\Windows` или профиля пользователя.
4. Повторить чтение `Runner.Listener.exe --version`; лишь после PASS переходить к регистрации.

На уже работающей `VM-326272` **ничего исправлять в ACL не нужно**.

### 3.4. Локальная проверка (после установки)

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass `
    -File 'C:\Setup\win11-github-runners-v1.3\Test-Win11Runners.ps1'
```

Ожидаем для каждого: `READY`, `Running`, `Auto`, `.\Admin`, наличие `.runner`, `.credentials` и корректного service name. `READY` **не означает** GitHub Online/Idle: нужен следующий раздел.

Если служба `Stopped` и `Service Control Manager` пишет 7023 «Неверная функция», сначала посмотреть **Application → ActionsRunnerService**. В ранних логах был текст `Failed to create a session...` — причиной оказался сдвиг времени. Не перерегистрировать и не пересоздавать службу, пока UTC не проверен и не восстановлен.

## 4. GitHub Online/Idle — отдельный обязательный gate

### 4.1. Через интерфейс GitHub

Для каждого репозитория открыть:

- <https://github.com/i-shutov/tikzarium/settings/actions/runners>
- <https://github.com/i-shutov/flowbridge/settings/actions/runners>
- <https://github.com/i-shutov/whereisit-ai/settings/actions/runners>

В списке убедиться, что runner с нужным именем **Online** и **Idle**. Состояние службы Windows `Running` само по себе этого **не доказывает**.

### 4.2. Опциональный read-only контроль через GitHub CLI

После интерактивного `gh auth login -h github.com` в **личном** профиле пользователя с правами чтения runner-ов:

```powershell
$gh = 'C:\Program Files\GitHub CLI\gh.exe'
& $gh auth status -h github.com
if ($LASTEXITCODE -ne 0) { throw 'GitHub CLI authentication required' }

$targets = @(
    @{ Repo='i-shutov/tikzarium';   Runner='win11-tikzarium'  },
    @{ Repo='i-shutov/flowbridge';  Runner='win11-flowbridge' },
    @{ Repo='i-shutov/whereisit-ai';Runner='win11-whereisit'  }
)
foreach ($t in $targets) {
    $json = (& $gh api "repos/$($t.Repo)/actions/runners?per_page=100" | Out-String)
    if ($LASTEXITCODE -ne 0) { throw "Runner API denied: $($t.Repo)" }
    $match = @((($json | ConvertFrom-Json).runners) |
        Where-Object { $_.name -eq $t.Runner })
    if ($match.Count -ne 1) { throw "Runner missing or ambiguous: $($t.Runner)" }
    $runner = $match[0]
    [pscustomobject]@{ Repo=$t.Repo; Name=$runner.name;
                       Status=$runner.status; Busy=$runner.busy } |
        Format-Table -AutoSize
    if ($runner.status -ne 'online' -or $runner.busy -ne $false) {
        throw "NOT_IDLE: $($t.Repo) $($t.Runner)"
    }
}
'ALL_THREE_GITHUB_ONLINE_IDLE_PASS'
```

GitHub API может возвращать `403` без административного разрешения к runner-ам — это **не** доказательство Offline. Тогда использовать GitHub UI. Не добавлять токены в исходник или PowerShell history.

## 5. Единая установка DevTools v1.5: порядок без граблей

### 5.1. Аудит до изменений

Закрыть активные GitHub jobs и убедиться, что нет `Runner.Worker.exe`. **При `Install`/`TeXUser` v1.5 сам остановится, если увидит такой процесс.** На production runner-е дополнительно проверить Idle в GitHub, а не ориентироваться лишь на отсутствие процесса.

```powershell
Get-Process -Name Runner.Worker -ErrorAction SilentlyContinue |
    Select-Object Id,ProcessName,Path

powershell.exe -NoProfile -ExecutionPolicy Bypass `
    -File 'C:\Setup\Setup-ThreeRunners-DevTools-v1.5.ps1' `
    -Mode Audit
```

`Audit` проверяет ОС, пользователя, службы, доступные команды; **не устанавливает** программы. На чистой Windows `WindowsApps\python.exe` является потенциальным Store-алиасом — такой `Get-Command` **не принимается** за настоящий Python.

### 5.2. Установка машинного уровня — только elevated Admin

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass `
    -File 'C:\Setup\Setup-ThreeRunners-DevTools-v1.5.ps1' `
    -Mode Install

"Exit code: $LASTEXITCODE"
```

Ожидаемый результат на проверенной VM: **`Exit code: 0`**, `RUST_MSVC_SMOKE_PASS`, `NSIS ... COMPILE PASS`. Скрипт идемпотентен в основных компонентах; уже установленный Git/MSVC/Node/и т.д. сохраняется. Он **не должен** повторно регистрировать или перезапускать runner-службы.

**Правила:**

- Не запускать системную фазу от `SYSTEM` или под другой учётной записью; она рассчитана на уже действующую сервисную `VM-326272\Admin`.
- Не запускать GUI, TeX и научные документы с повышенным токеном — только **отдельная** стадия `TeXUser`.
- Не менять `ExecutionPolicy` глобально: `-ExecutionPolicy Bypass` задаётся **только дочернему процессу** для проверенного файла.
- Не обновлять/не подменять `rust-toolchain.toml` или `Cargo.lock` автоматически при установке среды.
- Не обходить блокировку Defender, SHA-256 и Authenticode.

### 5.3. Что именно должно быть установлено

| Компонент | Принятый факт на 20.11.2026 | Нужен для |
|---|---|---|
| Git for Windows | `2.56.0.windows.1` | Все три репозитория |
| MSVC + Windows SDK | VS 2022 Build Tools, PASS | Rust MSVC, CMake, native Windows |
| Rustup/Rust stable | `rustc 1.100.0`, `cargo 1.100.0`, rustfmt, Clippy | Все три проекта |
| Python | `3.13.17` из `C:\DevTools\Python313`, не Store-алиас | CI/QA скрипты |
| Node.js/npm | `v24.22.3` / `11.19.1` | Tikzarium Tauri, UX prototype |
| CMake | установлен и найден | FlowBridge native UI |
| MiKTeX | 25.12, изолированные private roots | Tikzarium, XeLaTeX |
| Poppler | отдельный `C:\DevTools\Poppler\...\pdftotext.exe` | Независимый PDF-аудит |
| OpenSSH | Windows OpenSSH client | FlowBridge SSH |
| WebView2 | Evergreen runtime 158.0.4370.33 обнаружен | Tauri Windows UI |
| NSIS | Стандартный NSIS 3.13 Unicode, **test compile PASS** | FlowBridge installer |
| Inno Setup | 6.x, `ISCC.exe` | WhereIsIt installer |
| 7-Zip, FAR, VS Code | PASS | Подготовка/ручное QA |
| GitHub CLI, uv, SQLite | PASS | GitHub/QA/catalogs |
| Strawberry Perl, NuGet | PASS | `latexmk`, WDK package restore |
| PowerShell 7, rg, fd, fzf, zoxide, jq | PASS (дополнительные) | CLI-эргономика и диагностика |
| ChatGPT Desktop | **DEFERRED** | Интерактивное приложение; не блокирует сборки |

**`pwsh` v7.7.0 устанавливается рядом с Windows PowerShell 5.1.** Существующие PS5.1-скрипты продолжают исполняться через `powershell.exe`, не автоматически через `pwsh.exe`.

### 5.4. Rust — именно latest stable, без подмены проектных pins

Основная установка: `C:\DevTools\Rust\cargo` и `C:\DevTools\Rust\rustup`. Не создавайте параллельную вторую установку в `C:\Users\Admin\.cargo` и не теряйте `CARGO_HOME`/`RUSTUP_HOME` на повторном запуске. В v1.5 их восстанавливают до обращения к rustup.

```powershell
[Environment]::GetEnvironmentVariable('CARGO_HOME','Machine')
[Environment]::GetEnvironmentVariable('RUSTUP_HOME','Machine')
& 'C:\DevTools\Rust\cargo\bin\rustup.exe' run stable rustc --version
& 'C:\DevTools\Rust\cargo\bin\rustup.exe' run stable cargo --version
```

**Задача обновления проектов — отдельная:** в Tikzarium `rust-toolchain.toml` закрепляет `1.91.0`, в WhereIsIt — `1.100.0`, в FlowBridge используется `stable`. Установка новейшего stable **не отменяет** закрепление внутри конкретной рабочей директории. Проверить совместимость с новым Rust можно `cargo +stable ...` после доверенной фиксации кода; изменение pins и `Cargo.lock` — отдельный PR + CI.

### 5.5. Почему NSIS теперь безопасно проходит

**Действительный контракт FlowBridge:** `packaging/windows/FlowBridge.nsi` содержит `Unicode true` и использует **стандартный x86 Unicode NSIS bootstrapper для x64 payload**. Предыдущий установщик ошибочно потребовал сторонний `amd64-unicode` fork, который Defender заблокировал как потенциально опасный. v1.5 **не скачивает этот fork**.

Используется `C:\DevTools\NSIS\nsis-3.13\makensis.exe`. Если стандартный комплект неполон, применяется проверенный ZIP Tauri NSIS 3.13 с SHA-256:

```text
BA63DFFC4410EE89193E1CB5A41989991BD77C61068DA17E3156D136B7B0B3D8
```

Должен появиться лог `NSIS standard x86 Unicode bootstrapper for x64 FlowBridge payload: COMPILE PASS`. Исполняемый файл тестового установщика **создаётся, но не запускается**. Этот тест **не** означает, что реальный FlowBridge installer прошёл install/upgrade/uninstall QA.

## 6. MiKTeX — только в обычной PowerShell (medium token)

Это **самостоятельный обязательный этап**, даже если `Install` завершился кодом 0. Запускать под **тем же `VM-326272\Admin`**, но в **новом, не повышенном** PowerShell. Проверка `elevated: False` обязательна.

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass `
    -File 'C:\Setup\Setup-ThreeRunners-DevTools-v1.5.ps1' `
    -Mode TeXUser -SkipOptionalTeXPackages
```

В подтверждённых логах:

```text
Required MiKTeX packages and AutoInstall=0 verified under medium integrity
DEFERRED: Extended scientific MiKTeX packages | Skipped by -SkipOptionalTeXPackages
PASS: Private MiKTeX mandatory packages / AutoInstall=0
TEX_PDF_SMOKE_PASS: C:\Users\Admin\AppData\Local\ThreeRunnersDevTools\smoke-tex\smoke.pdf
PASS: Actual TikZ XeLaTeX -> PDF -> independent Poppler smoke
```

**Обязательные MiKTeX package IDs** из v1.5: `miktex-xetex-bin-x64-2.9`, `xetex`, `pgf`, `standalone`, `fontspec`, `unicode-math`, `lm-math`, `lm`, `dejavu`. MiKTeX не принимает установку уже присутствующего пакета как идемпотентный no-op: скрипт сначала проверяет `isInstalled` и устанавливает **только отсутствующие** пакеты. Значение `[MPM]AutoInstall=0` обязательно проверяется чтением настройки обратно.

**Расширенный научный набор пока отложен**, а не объявлен установленным: `pgfplots`, `xcolor`, `hyperref`, `babel`, `beamer`, `amsmath`, `geometry`, `booktabs`, `siunitx`, `microtype`, `latexmk`, `tikz-cd`, `tikz-3dplot`, `circuitikz`, `chemfig`, `forest`, `animate`, `fancyhdr`, `polyglossia`. Примечание: наличие `latexmk.exe` **само по себе не доказывает** статус соответствующего пакета в менеджере.

### 6.1. TLS/timeout CTAN: как действовать без снижения безопасности

В диагностике `-Mode TeXTlsAudit` наблюдалось:

```text
MiKTeX API: Windows TLS check PASS; server HTTP 400 (TLS verified)
MiKTeX official site: Windows HTTPS PASS; HTTP 200
CTAN mirror: Windows HTTPS Timeout
```

В `TeXUser` ранее встречались `SSL peer certificate or SSH remote key was not OK`, позднее `Timeout was reached` при **дополнительных** пакетах `microtype` / `latexmk`. Это **не отменяет** успешно собранный минимальный PDF и не означает, что все научные документы уже собираются.

Happy path: завершить обязательный набор с `-SkipOptionalTeXPackages`, сохранить протоколы и продолжать основную подготовку. Полный научный набор устанавливать **отдельно**, после выяснения конкретного URL CTAN mirror, сертификата, сетевого маршрута и доступного HTTPS-репозитория в официальной MiKTeX Console. **Не** выключать SSL verification, не импортировать непроверенные корневые сертификаты, не отключать Defender и не включать auto-install во время компиляции.

Read-only диагностика (обычная консоль):

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass `
    -File 'C:\Setup\Setup-ThreeRunners-DevTools-v1.5.ps1' `
    -Mode TeXTlsAudit
```

Логи пользовательской фазы: `%LOCALAPPDATA%\ThreeRunnersDevTools\`; для сетевого отказа смотреть `native-<timestamp>-miktex-optional-install-<package>-stderr.txt` и сам журнал конкретной компиляции. Сохранение `AutoInstall=0` не позволяет неожиданно ставить TeX-пакеты при QA.

### 6.2. Границы принятого TeX-smoke

Минимальный тест создаёт `standalone` + `tikz` с надписью `pass`, компилирует **реальным** `xelatex --disable-installer`, затем читает PDF через **независимый** Poppler. Он доказывает готовность базовой цепочки **только для этой фигуры**. В нём **не** проверяются весь SCI142/AI88, сложные `pgfplots`, все научные пакеты, кириллица/Arial в финальном PDF, PDF GUI preview, IME, DPI или физические жесты в Tkzarium/Studio.

## 7. После установки: обновить окружение служб и подтвердить Online/Idle

**Почему:** runner-сервисы созданы **до** установки Git, Rust, Python, Node и других каталогов в `Machine PATH`. Уже работающий `Runner.Listener` может хранить **старый снимок переменных окружения**. `TOOL_FOUND` в интерактивной Admin-консоли не гарантирует доступность того же инструмента внутри GitHub job.

Безопасная последовательность:

1. Дождаться **всех трёх GitHub Idle**; прекратить планировать новые jobs на время обслуживания. Проверить, что нет `Runner.Worker.exe`.
2. Сохранить сервисный статус и проверить, что имена соответствуют ожидаемым `.service`.
3. Лишь затем в повышенном Admin **контролируемо перезапустить** три существующие службы. Не менять их учётную запись, регистрацию или ACL.
4. Повторить локальный `Test-Win11Runners.ps1` и GitHub Online/Idle.

```powershell
# Elevated Admin. Выполнять ТОЛЬКО после независимого GitHub Idle.
$workers = @(Get-Process -Name 'Runner.Worker' -ErrorAction SilentlyContinue)
if ($workers.Count -gt 0) { throw 'Active Runner.Worker.exe: restart forbidden' }

foreach ($runner in @('win11-tikzarium','win11-flowbridge','win11-whereisit')) {
    $file = "C:\GitHubRunners\$runner\.service"
    if (!(Test-Path -LiteralPath $file -PathType Leaf)) { throw "Missing $file" }
    $name = (Get-Content -LiteralPath $file -Raw).Trim()
    if ($name -notlike 'actions.runner.*') { throw "Unexpected service: $name" }
    $svc = Get-CimInstance Win32_Service | Where-Object { $_.Name -eq $name }
    if (-not $svc -or $svc.StartName -notin @('.\Admin','VM-326272\Admin')) {
        throw "Service identity mismatch: $runner"
    }
    Restart-Service -Name $name -ErrorAction Stop
    (Get-Service -Name $name).WaitForStatus('Running',[timespan]::FromSeconds(30))
}

powershell.exe -NoProfile -ExecutionPolicy Bypass `
    -File 'C:\Setup\win11-github-runners-v1.3\Test-Win11Runners.ps1'
```

**Оговорка о race:** GitHub может назначить новое задание между проверкой Idle и рестартом. Поэтому проводить это только во время выделенного окна без новых заданий и ещё раз проверить активность непосредственно перед изменением каждой службы. Если новый job появился, рестарт **отменить**, а не принудительно останавливать задачу.

Перезагрузка всей Windows **не нужна по умолчанию**. Делать её только если установщик явно запросил reboot и все runner-ы Idle, либо если точная диагностика показала необходимость. После reboot снова проверить службы и GitHub Online/Idle.

## 8. Следующий уровень: три безопасных smoke-workflow из `main`

Ветви/PR, созданные для Win11 VPS smoke на момент проверки 20.11.2026:

| Репозиторий | Диагностический PR | Ручная цель |
|---|---|---|
| Tikzarium | [PR #192](https://github.com/i-shutov/tikzarium/pull/192) | `win11-tikzarium` |
| FlowBridge | [PR #90](https://github.com/i-shutov/flowbridge/pull/90) | `win11-flowbridge` |
| WhereIsIt AI | [PR #70](https://github.com/i-shutov/whereisit-ai/pull/70) | `win11-whereisit` |

На момент исследования PR **открыты**. Не запускать их непроверенный PR HEAD на elevated self-hosted runner. **Сначала ревью, затем слияние в `main`**, после этого запуск через GitHub UI `Actions → Windows 11 VPS runner smoke → Run workflow`, ветка `main`; вариант с `gh workflow run ... --ref main` допустим после подтверждения имени workflow и наличия его в `main`.

Сами диагностические workflows задуманы как **ручные (`workflow_dispatch`)**, с `permissions: contents: read`, проверкой конкретных имени runner-а, hostname `VM-326272`, учётной записи Admin, x64/Windows 11 и доступных инструментов. Они **не** выполняют checkout и не собирают недоверенный PR-код.

Необходимо получить по каждому проекту независимое подтверждение: `RUNNER_SMOKE_PASS`, GitHub job `Success`, runner `Online/Idle` после завершения. Инструменты `TOOL_FOUND` внутри job проверять заново — это докажет, что новый environment PATH действительно дошёл до сервисного процесса.

### 8.1. Дальнейшие реальные сборки — не смешивать с host readiness

| Продукт | Следующий build/QA gate | Что этот setup **не** доказывает |
|---|---|---|
| Tikzarium | `cargo fmt/test/clippy --locked`, Tauri `npm ci/test/lint/build`, реальный XeLaTeX/PDF, нативное GUI/RDP | Физические GUI-жесты, `Win10` W3/W4, весь SCI142/AI88, DPI/IME |
| FlowBridge | Rust FFI/CLI, CMake GUI и capture userspace, **настоящий** NSIS installer + install/upgrade/uninstall | Реальный WFP/ALE/NDISRD, драйверная подпись/установка, приватность SSH/DNS, финальный GO |
| WhereIsIt AI | Rust workspace/egui, Inno Setup, SQLite/CTF/sidecar и Windows GUI QA | Реальные каталоги владельца, полная физическая приёмка и release GO |

**Важно:** Windows 11 CI-хост **не подменяет** независимую физическую приёмку на Windows 10 Pro. Особенно для FlowBridge не присваивать этой машине без отдельного решения драйверный label `flowbridge-wfp-vm`, не устанавливать/не запускать неподписанный kernel driver и не изменять сеть/firewall/VPN ради установки инструментов.

## 9. Матрица граблей и проверенных обходов

| Инцидент / симптом | Причина или доказанное ограничение | Правильный happy path | Чего не делать |
|---|---|---|---|
| `config.cmd: Access denied` | Исполняемый listener тоже не запускался; ACL/запуск, не токен GitHub | Диагностика запуска и NTFS **только внутри runner**; v1.3 runner installer | Не выдавать бездумно `F` по всему диску, не менять UAC |
| `.runner` есть, служба `Stopped` | Реальная регистрация/session ещё не рабочая | Сверить UTC, читать `ActionsRunnerService` | Не считать `.runner` достаточным |
| `registration deleted from server` | В инциденте было несинхронное время | `Date` GitHub vs UTC Windows; `w32tm`; новый старт | Не перерегистрировать сразу |
| Recovery script завершился HTTP 404 | Неверный endpoint диагностики времени | `https://api.github.com/` + заголовок `Date` | Не объявлять часы сломанными из-за одного 404 |
| `READY Running Auto` | Это **локальная** проверка | Отдельно GitHub `Online/Idle` | Не маркировать READY как Online |
| Runner не видит Git/Cargo после установки | Старый процесс службы не получил обновлённый PATH | После Idle контролируемый рестарт сервисов | Не рестартовать активный job |
| PS5.1 некорректно читает кириллицу | `.ps1` UTF-8 без BOM в старом Win10 bootstrap | UTF-8 BOM + синтаксический preflight | Не маскировать дефекты переносом на PowerShell 7 |
| Ошибки `$build:` / `$PSScriptRoot` | Старые синтаксические/контекстные ошибки bootstrap | Сохранённый `.ps1`, Parser::ParseFile, запуск через `-File` | Не исполнять случайные куски скрипта из буфера |
| Win11-only bootstrap отказал Win10 Pro | Жёсткий OS-gate был неверен | Win10 build 19045+ или Win11 x64 проверять явно | Не подменять OS detection |
| Отсутствует `winget` или WinGet 1.2 ругается на `--disable-interactivity` | Версионная несовместимость WinGet | Критичные бинарники — vendor SHA/Authenticode; v1.5 не требует WinGet | Не считать отказ WinGet доказательством невозможности установки ПО |
| WinGet `-1073741819` | Access violation WinGet на VM | Дополнительные CLI через проверенные GitHub Releases | Не запускать один и тот же crash в цикле |
| `python.exe` указывает на `WindowsApps` | Store alias, не интерпретатор | Проверить `C:\DevTools\Python313\python.exe --version` | Не объявлять Python установленным по одному `Get-Command` |
| Node выводит десятки версий | PowerShell 5.1 некорректно обрабатывал JSON-список | Пин официального Node LTS v24.22.3, SHA256 от nodejs.org | Не брать `node` v27 alpha как «latest» |
| rustup второй раз пишет `not installed at C:\Users\Admin\.cargo` | Переменные `CARGO_HOME`/`RUSTUP_HOME` расходились с управляемой установкой | Одна пара `C:\DevTools\Rust\{cargo,rustup}`; v1.5 восстанавливает ENV | Не создавать второй Rust по умолчанию |
| Установлен Rust stable, а проект запускает старый | `rust-toolchain.toml` в repo переопределяет default | Обновление repo pin отдельным PR, сборка `+stable` как отдельный тест | Не править репозиторий скрытно при bootstrap |
| MiKTeX предупреждает `security risk: elevated` | TeX запущен с высоким административным токеном | Системная установка elevated; TeXUser — medium token | Не компилировать непроверенный TeX от администратора |
| MiKTeX `packages install` уже установленного пакета | Для MiKTeX это может быть ошибка | `packages info` → установить **только отсутствующие** → проверить again | Не устанавливать весь список вслепую |
| MiKTeX `SSL peer certificate...` | Проверка TLS сертификата не прошла | Локальный лог URL/CA/прокси; optional DEFERRED | Не отключать TLS |
| CTAN `Timeout was reached` | Маршрут/зеркало недоступно | Mandatory PASS, optional DEFERRED, no repeated requests | Не маскировать timeout как success для пакета |
| Найден `pdftotext.exe`, но из MiKTeX | Инструмент не независим и наследует MiKTeX config | Поплер из `C:\DevTools\Poppler` | Не объявлять независимый PDF-аудит по MiKTeX binary |
| NSIS download каждый раз даёт иной SHA | SourceForge возвращал другие байты/страницы | Проверенный ZIP Tauri, SHA256 | Не выключать проверку SHA |
| NSIS ZIP содержит два `makensis.exe` | Стандартная структура дистрибутива | Выбирать канонический путь, проверить MUI/Unicode через сборку | Не объявлять archive corruption |
| Потребовали `amd64-unicode` и Defender заблокировал fork | Ошибка требования: FlowBridge использует **x86 Unicode bootstrapper** | v1.5 компилирует стандартным NSIS 3.13 | Не allowlist заблокированный форк |
| VS Code download HTTP 404 | Неверный `win32-x64-system` URL | Официальный `win32-x64` + Microsoft Authenticode | Не скачивать сторонний EXE |
| ChatGPT Store `no store account` | Отсутствует интерактивная учётная запись Microsoft Store | `DEFERRED`; войти в Store и установить официальный пакет | Не скачивать «portable ChatGPT» из непроверенных источников |
| `Exit code: 0` у Install, но TeX ещё не проверен | Раздельные контексты elevation / medium | Отдельно `TeXUser` и `TEX_PDF_SMOKE_PASS` | Не принимать один exit 0 за всю систему |
| GUI прошёл в RDP на Win11 | Другие DPI, сессия и ОС | Физический Win10 QA — независимый gate | Не переносить PASS с Win11 Server/VM на Win10 Pro |

## 10. Итоговая приёмка VM-326272 по фактам на 20.11.2026

| Gate | Статус | Источник наблюдения / уточнение |
|---|---|---|
| Host OS / exact account | **PASS** | Windows 11 Pro x64 build 22631; `VM-326272\Admin` |
| Три локальные службы | **PASS_LOCAL** | `Running`, `Auto`, `.\Admin` для всех трёх |
| GitHub Online/Idle | **NOT_VERIFIED_IN_THIS_RUNBOOK** | Проверить GitHub UI/API |
| DevTools v1.5 Install | **PASS** | `2026-11-20 18:10:40`, `Exit code: 0` |
| Rust stable/MSVC smoke | **PASS** | `RUST_MSVC_SMOKE_PASS` |
| NSIS standard x86 Unicode smoke | **PASS** | `COMPILE PASS`, EXE не запускался |
| MiKTeX core/AutoInstall=0 | **PASS** | `2026-11-20 18:13:02`, medium token |
| TikZ → XeLaTeX → PDF → Poppler | **PASS** | `TEX_PDF_SMOKE_PASS`, `2026-11-20 18:13:06` |
| Расширенные научные MiKTeX пакеты | **DEFERRED_BY_CHOICE** | `-SkipOptionalTeXPackages`, не выдавать за PASS |
| ChatGPT Desktop | **DEFERRED_STORE_ACCOUNT** | официальный Microsoft Store ProductId `9PLM9XGG6VKS` |
| Рестарт runner service после обновления PATH | **NOT_VERIFIED** | Только в Idle maintenance window |
| Три workflow_dispatch на реальных runner-ах | **NOT_VERIFIED** | После ревью/слияния smoke workflow в main |
| Полные нативные сборки проектов | **NOT_VERIFIED** | Отдельные CI logs/QA artifacts |
| Release GO каждого продукта | **НЕ СЛЕДУЕТ ИЗ ЭТОЙ ПРИЁМКИ** | Иные независимые релизные критерии |

### Где брать evidence

```text
Машинный этап:
  C:\ProgramData\ThreeRunnersDevTools\report-20261120-181007.json
  C:\ProgramData\ThreeRunnersDevTools\transcript-20261120-181007.txt

Пользовательский TeX:
  C:\Users\Admin\AppData\Local\ThreeRunnersDevTools\report-20261120-181222.json
  C:\Users\Admin\AppData\Local\ThreeRunnersDevTools\smoke-tex\smoke.pdf

Дальнейший контроль:
  GitHub Actions run URLs для всех трёх workflow_dispatch,
  Service/ActionsRunnerService logs и SHA готовых артефактов.
```

Эти пути являются **адресами файлов на VM**, а не файлами, приложенными к настоящему Markdown. Источник выводов — терминальные журналы владельца; сами JSON/PDF-байты на VM в этом исследовании отдельно не выгружались и не аудировались.

## 11. Операционный режим после успешной установки

- **Не переустанавливать** базовый стек, если новый `Audit` показывает корректные инструменты, а два реальных smoke остаются PASS. Для обновлений — отдельное изменение, лог/JSON, проверка сигнатур и повторная приёмка.
- **Не републиковать релизы автоматически**: Win11 runners — средства сборки и QA, не разрешение на stable release. WFP driver, Code Signing, реальные GUI/инсталляционные тесты и Win10 приемка живут в отдельных планах.
- **Сохранять evidence и контрольные точки**, не очищая их вместе с временными установщиками. Большие тестовые датасеты держать вне Git.
- **Не изменять три runner-а одновременно при активных заданиях**. Выполнять maintenance в отдельном окне, затем проверять Online/Idle и отдельный smoke по каждому репозиторию.
- **Не считать все `TOOL_FOUND` эквивалентом `PASS`**: программа может существовать, но не запускаться или не работать в контексте service-account. Поэтому в happy path есть реальная компиляция Rust, реальная сборка NSIS, реальная TeX→PDF и ручные GitHub jobs.

## 12. Источники и привязки к проектам

**Исходники установки:** локальный `Setup-ThreeRunners-DevTools-v1.5.ps1` (SHA-256 приведён в разделе 1), исторический `Install-Win11Runners.ps1` / `Test-Win11Runners.ps1` v1.3 и реальные журналы владельца 20.11.2026. Их статус не заменяют ссылки на новые версии в Интернете.

**Репозитории и ключевые документы:**

- [Tikzarium](https://github.com/i-shutov/tikzarium), [Windows 10 workstation setup](https://github.com/i-shutov/tikzarium/tree/main/scripts/workstation/windows10), [rust-toolchain.toml](https://github.com/i-shutov/tikzarium/blob/main/rust-toolchain.toml), [Tauri frontend](https://github.com/i-shutov/tikzarium/tree/main/apps/tikzarium-studio-tauri).
- [FlowBridge](https://github.com/i-shutov/flowbridge), [NSIS installer source](https://github.com/i-shutov/flowbridge/blob/main/packaging/windows/FlowBridge.nsi), [Windows packaging build](https://github.com/i-shutov/flowbridge/blob/main/packaging/windows/BUILD.md), [CI](https://github.com/i-shutov/flowbridge/blob/main/.github/workflows/ci.yml).
- [WhereIsIt AI](https://github.com/i-shutov/whereisit-ai), [rust-toolchain.toml](https://github.com/i-shutov/whereisit-ai/blob/main/rust-toolchain.toml), [Windows installer](https://github.com/i-shutov/whereisit-ai/blob/main/installers/windows/build-installer.ps1), [Win10 egui QA handoff](https://github.com/i-shutov/whereisit-ai/tree/main/tools/qa/windows10-egui).
- [Официальная документация GitHub по self-hosted runner-ам](https://docs.github.com/en/actions/how-tos/manage-runners/self-hosted-runners/add-runners); [документация MiKTeX](https://docs.miktex.org/manual/); [официальный Rustup](https://rustup.rs/).

---

**Критерий закрытия happy path:** не «один раз смогли установить Rust», а **`Install PASS` + `TeXUser PASS` + `GitHub Online/Idle ×3` + `trusted workflow_dispatch PASS ×3`**. В рамках приведённых логов первые **два** условия выполнены; остальные нельзя объявлять пройденными без новых подтверждений.
