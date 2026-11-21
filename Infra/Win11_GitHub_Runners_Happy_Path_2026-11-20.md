# Windows 11 Pro: единый CI-хост GitHub Actions для трёх проектов

**Happy path / runbook v1.0** · 20 ноября 2026 г.  
**Проверенный хост:** `VM-326272` (`192.177.26.134`) · **ОС:** Windows 11 Pro x64 · **оператор и учётная запись служб:** `VM-326272\Admin`  
**Проекты:** `i-shutov/tikzarium`, `i-shutov/flowbridge`, `i-shutov/whereisit-ai`.

> **Фактический результат инцидента:** после исправления системного времени расхождение Windows с HTTPS-временем GitHub составило **4,4 с**; проверка `Test-Win11Runners.ps1` показала **3 × `READY / Running / Auto`**. Это доказанная локальная приёмка. Статусы **Online/Idle** на стороне GitHub и выполнение реальных workflow проверяются **отдельно** — их не подменяет статус службы.

## 0. Архитектура и правила

На одной Windows-машине размещаются **три отдельных repository-level GitHub Actions runner'а**. Для репозиториев личной учётной записи `i-shutov` **одна регистрация runner'а не может обслуживать все три репозитория**. Для общего runner'а на уровне организации пришлось бы переносить репозитории в GitHub Organization. Здесь выбрана совместная инфраструктура с отдельными службами и рабочими каталогами.

| Репозиторий | Runner / дополнительная метка | Каталог | Windows-служба |
|---|---|---|---|
| `i-shutov/tikzarium` | `win11-tikzarium` | `C:\GitHubRunners\win11-tikzarium` | `actions.runner.i-shutov-tikzarium.win11-tikzarium` |
| `i-shutov/flowbridge` | `win11-flowbridge` | `C:\GitHubRunners\win11-flowbridge` | `actions.runner.i-shutov-flowbridge.win11-flowbridge` |
| `i-shutov/whereisit-ai` | `win11-whereisit` | `C:\GitHubRunners\win11-whereisit` | `actions.runner.i-shutov-whereisit-ai.win11-whereisit` |

Три службы автоматически стартуют после загрузки Windows; каждая независимо принимает **одну job за раз**. На одном хосте в принципе возможны три одновременные job: тяжёлые Rust/MSVC/LaTeX-сборки могут конкурировать за RAM, диск и CPU. Рабочие папки `_work` раздельны, но сам хост **не является изолированной песочницей**.

**Безопасность — обязательная граница:** все три репозитория публичные, а текущие службы работают под локальным администратором, по решению владельца VPS. **Не назначать на них `pull_request`/`pull_request_target`, внешние форки или непроверенный пользовательский код.** Использовать только вручную запускаемые workflow из защищённого `main` с минимальным `permissions`, без сторонних скриптов, секретов и checkout, где это возможно. Для обычного CI по PR оставить GitHub-hosted runner'ы. В перспективе предпочтительны отдельные непривилегированные/одноразовые VM. Для WFP/драйверных тестов FlowBridge сохранять отдельную специализированную VM, а не смешивать их с обычным CI.

**Старые метки не заменяются автоматически:** `tikzarium-winserver` и `flowbridge-wfp-vm` — другие метки. Новые runner'ы получают метки `win11-*`; существующие задания не переедут на новую VPS без осознанного изменения `runs-on`.

## 1. Самый короткий маршрут (новая чистая VPS)

1. Открыть **64-битный Windows PowerShell 5.1 от администратора** и проверить хост.
2. **До регистрации runner'ов**: настроить UTC/синхронизацию Windows Time и проверить абсолютное UTC по HTTPS-времени GitHub (допуск ±120 с).
3. В текущем окне временно разрешить PowerShell-скрипты (`ExecutionPolicy` только `Process`).
4. Распаковать **проверенный комплект `Win11-GitHub-Runners-3Projects-v1.3.zip`** в `C:\Setup\win11-github-runners-v1.3` и выполнить установщик `-Project all` под текущей административной учётной записью. По очереди ввести **локально** пароль Windows и три краткоживущих регистрационных токена GitHub.
5. Проверить `3 × READY/Running/Auto` **и повторить проверку после паузы 20–30 секунд**; затем в GitHub проверить **Online/Idle**.
6. После ревью и слияния трёх специальных PR вручную запустить три smoke workflow; получить `RUNNER_SMOKE_PASS` для каждого проекта. В конце проверить автозапуск после плановой перезагрузки.

**Если на этом хосте три службы уже `READY/Running`, пункты 3–4 не повторять!** Перейти непосредственно к проверке Online/Idle и smoke CI (разделы 5–6).

## 2. Preflight: хост, права, сеть, время

### 2.1. Кто и где выполняет команды

В открытой **повышенной** консоли (заголовок PowerShell от администратора):

```powershell
$ErrorActionPreference = 'Stop'
$env:COMPUTERNAME
whoami
Get-CimInstance Win32_OperatingSystem |
    Select-Object Caption, Version, BuildNumber, OSArchitecture

$id = [Security.Principal.WindowsIdentity]::GetCurrent()
([Security.Principal.WindowsPrincipal]$id).IsInRole(
    [Security.Principal.WindowsBuiltInRole]::Administrator)

Test-NetConnection github.com -Port 443
Test-NetConnection api.github.com -Port 443
```

Для проверенного хоста ожидаются `VM-326272`, `VM-326272\Admin`, Windows 11 x64 и `True` у проверки повышения. Для GitHub Runner требуется прежде всего **исходящий HTTPS/TCP 443**; открывать входящий порт runner'а не нужно. Доступ к RDP `3389/tcp` ограничить доверенными IP, не открывать на весь интернет без необходимости.

### 2.2. Время — самый важный preflight

На свежем VPS, физически находящемся в США, Windows показывала `05:30 +03:00`. Это выглядело как **американское локальное время, ошибочно интерпретированное в московском часовом поясе**, то есть UTC отставал примерно на **8 часов**. GitHub подключение принимал, но отказывал в создании сессии с вводящим в заблуждение `invalid_client`.

Для CI принимаем системный часовой пояс **UTC**. **Важно:** `tzutil` меняет отображение локального времени, но само по себе **не исправляет неправильные часы UTC**. Нужна реальная синхронизация через W32Time/NTP либо корректная настройка часов у VPS-провайдера/гипервизора.

```powershell
# Часовой пояс CI-сервера: UTC; выполнять только если это принято для машины.
tzutil /s 'UTC'

# Windows Time: включить и настроить исходники NTP для standalone VPS.
Set-Service W32Time -StartupType Automatic
if ((Get-Service W32Time).Status -eq 'Running') {
    Restart-Service W32Time
} else {
    Start-Service W32Time
}

w32tm /config `
    /manualpeerlist:"time.windows.com,0x8 time.cloudflare.com,0x8" `
    /syncfromflags:manual `
    /update

w32tm /resync /rediscover
Start-Sleep -Seconds 10

# Проверить выбранный источник и состояние синхронизации.
w32tm /query /source
w32tm /query /status
(Get-TimeZone).Id
```

**Независимая сверка по HTTPS** (используем рабочий URL `https://api.github.com/`, а не URL, который возвращает 404):

```powershell
[Net.ServicePointManager]::SecurityProtocol = `
    [Net.ServicePointManager]::SecurityProtocol -bor `
    [Net.SecurityProtocolType]::Tls12

$response = Invoke-WebRequest `
    -Uri 'https://api.github.com/' `
    -UseBasicParsing `
    -Headers @{ 'User-Agent' = 'GitHubRunnerClockCheck' }

if ($response.StatusCode -ne 200) {
    throw "Unexpected HTTP $($response.StatusCode): verify URL/network"
}

$githubUtc = [DateTimeOffset]::Parse(
    [string]$response.Headers['Date']
).UtcDateTime
$windowsUtc = [DateTime]::UtcNow
$skew = [Math]::Round(($windowsUtc - $githubUtc).TotalSeconds, 1)

[pscustomobject]@{
    Host        = $env:COMPUTERNAME
    Timezone    = (Get-TimeZone).Id
    WindowsUTC  = $windowsUtc.ToString('o')
    GitHubUTC   = $githubUtc.ToString('o')
    SkewSeconds = $skew
} | Format-List | Out-Host

if ([Math]::Abs($skew) -gt 120) {
    throw "CLOCK_SKEW_TOO_LARGE: $skew seconds. DO NOT register runners."
}
```

**Критерий GO:** `abs(SkewSeconds) <= 120`. В успешном проходе 20.11.2026 было **4,4 с**.

Если `w32tm /resync` не проходит: проверить **исходящий UDP/123**, DNS, выбранный NTP-сервер, `w32tm /query /status`, а на VPS — синхронизацию гостя с гипервизором. Если машина доменная, сначала проверить политику доменного времени и не перезаписывать её ручным NTP. **Нельзя** начинать очистку/перерегистрацию GitHub при недостоверном UTC.

## 3. Чистая установка трёх служб

### 3.1. Какой комплект использовать

Для данной конфигурации проверен установочный архив **`Win11-GitHub-Runners-3Projects-v1.3.zip`**. Его SHA-256:

```text
55fd2dbd36ca003ba19b09c38f4b36e4b1061b94ffddeb3b624b8f60f93f1ba3
```

Внутри закреплён официальный **GitHub Actions Runner 2.338.2** (`actions-runner-win-x64-2.338.2.zip`, SHA-256 `a1f17aa987fc8158bc7521d284912267a0d01b7c2c4684b33c86783b5e8221cc`). Проверка hash выполняется **до извлечения/регистрации**. Это зафиксированный работавший выпуск, **не утверждение о самой новой версии на будущую дату**.

**Не использовать** ранние комплекты v1.0/v1.1/v1.2: в них была ошибочная обработка наследования NTFS ACL. **Не использовать** `Repair-Win11RunnerSessions.ps1` из v1.4 для обычной установки: там некорректная проверка времени через URL, ответивший HTTP 404. При живых службах никакой повторной установки не нужно.

Разместить комплект как:

```text
C:\Setup\win11-github-runners-v1.3\
    Install-Win11Runners.ps1
    Repair-Win11RunnerAccess.ps1
    Test-Win11Runners.ps1
    README.md
    workflows\...
```

Архив можно распаковать средствами Windows или командой `Expand-Archive`. **Не** распаковывать файлы установщика поверх `C:\GitHubRunners`; там уже находятся исполняемые runner'ы и их состояние.

### 3.2. Запуск без «исчезающего окна»

В **текущем окне** PowerShell, а не через отдельный `powershell.exe -File`:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force

$setup = 'C:\Setup\win11-github-runners-v1.3'
& "$setup\Install-Win11Runners.ps1" `
    -Project all `
    -ServiceAccount CurrentAdmin `
    -ExpectedComputerName $env:COMPUTERNAME
```

Параметр `-Scope Process` не меняет системную политику навсегда. Оператор `&` запускает скрипт **в том же окне** — ошибки/таблица остаются видимыми. Если `MachinePolicy`/`UserPolicy` принудительно настроены групповой политикой, процессный `Bypass` не может их переопределить; проверить `Get-ExecutionPolicy -List`, а не отключать защиту глобально.

> **Пароли:** для Windows-службы вводится **именно пароль** локальной учётной записи `Admin`, не Windows Hello PIN. Затем последовательно вводятся отдельные **регистрационные токены GitHub**, действующие ограниченное время, **только локально и скрытым вводом**. Не отправлять их в чат, не сохранять в `.md`, Git и логи.

Страницы регистрации:

- Tikzarium — <https://github.com/i-shutov/tikzarium/settings/actions/runners/new>
- FlowBridge — <https://github.com/i-shutov/flowbridge/settings/actions/runners/new>
- WhereIsIt — <https://github.com/i-shutov/whereisit-ai/settings/actions/runners/new>

Что делает v1.3: проверяет Win11 x64/администратора, права и целостность архива, восстанавливает наследование NTFS **только у ещё не настроенных** каталогов, проверяет реальный запуск `Runner.Listener.exe --version`, затем регистрирует каждую службу под текущим Admin и валидирует локальное состояние. Установщик не переустанавливает и не сбрасывает уже зарегистрированные runner'ы при повторном вызове.

При отсутствии custom-бандла возможна штатная ручная установка из официального [GitHub Docs](https://docs.github.com/en/actions/how-tos/manage-runners/self-hosted-runners/add-runners), но важно повторить **сначала раздел 2.2**, использовать **отдельную папку и токен для каждого репозитория** и настроить запуск **как Windows-службы** на этапе регистрации. Ручное смешивание версий/учётных записей поверх существующей регистрации запрещено.

## 4. NTFS: что нужно и что категорически не нужно делать

Ранее установщик применял `/inheritance:r` рекурсивно: **файлы потеряли унаследованные разрешения**. Ситуация выглядела парадоксально: администратор имеет `F` на папке, но `config.cmd` и `Runner.Listener.exe` возвращают `Отказано в доступе`. Проверка `icacls.exe <путь-к-файлу>` показывала **имя файла без ACL-строк**. Обычное `/grant ... /T` на папке **не включает** наследование у уже защищённых файлов.

**Правило для чистой установки:** не менять NTFS ACL вручную; доверить подготовку исправленному v1.3 и проверить запуск EXE перед запросом токена. **Не применять** `icacls /inheritance:r /T` и не копировать старые исправления из v1.0–v1.2.

**Если восстанавливается только незарегистрированный каталог со сломанными правами** (нет `.runner` и `.service`, и служба не использует папку):

```powershell
Set-ExecutionPolicy -Scope Process Bypass -Force
& 'C:\Setup\win11-github-runners-v1.3\Repair-Win11RunnerAccess.ps1' `
    -Project tikzarium
```

Правильный принцип: установить наследуемые разрешения **на корне каталога**, затем включить наследование у всех его потомков (`icacls <каталог>\* /inheritance:e /T`). Скрипт дополнительно обходит дерево, не следует junction/symlink и проверяет каждую запись. **Не применять восстановление ACL к работающему/зарегистрированному runner'у** — эти каталоги скрипт намеренно отвергает.

## 5. Двухступенчатая приёмка: Windows и GitHub

### 5.1. Локальная проверка без новых токенов

```powershell
Set-ExecutionPolicy -Scope Process Bypass -Force
& 'C:\Setup\win11-github-runners-v1.3\Test-Win11Runners.ps1'

Start-Sleep -Seconds 25
& 'C:\Setup\win11-github-runners-v1.3\Test-Win11Runners.ps1'
```

Ожидаемо:

```text
Host: VM-326272 | Expected service account: VM-326272\Admin

Runner           Check State   StartMode Account
------           ----- -----   --------- -------
win11-tikzarium  READY Running Auto      .\Admin
win11-flowbridge READY Running Auto      .\Admin
win11-whereisit  READY Running Auto      .\Admin
```

`READY` проверяет `.runner`, `.credentials`, `.service`, соответствие репозитория и имени, путь службы, SID нужной учётной записи, автозапуск и **текущее** состояние `Running`. `.\Admin` и `VM-326272\Admin` обозначают одну локальную учётную запись; в проверке используются SID, а не только строки.

### 5.2. Проверка на стороне GitHub — строго обязательна

Открыть:

- <https://github.com/i-shutov/tikzarium/settings/actions/runners>
- <https://github.com/i-shutov/flowbridge/settings/actions/runners>
- <https://github.com/i-shutov/whereisit-ai/settings/actions/runners>

Убедиться в правильных **именах, метках и статусах**:

- **Idle** — подключён и готов; **Active** — выполняет задачу; **Offline** — не подключён.
- Только наличие `.runner`/`.credentials` **не доказывает** регистрацию на сервере; `StartService ReturnValue=0` **не доказывает**, что служба продолжит работать через 3–15 секунд.

Если из облака недоступен административный GitHub API списка runner'ов, проверка производится через UI владельца, а не подменяется предположением.

### 5.3. Smoke CI, затем сборки

Подготовленные **draft PR, не слитые автоматически в `main`**:

| Проект | PR | Метка |
|---|---|---|
| Tikzarium | [PR #192](https://github.com/i-shutov/tikzarium/pull/192) | `win11-tikzarium` |
| FlowBridge | [PR #90](https://github.com/i-shutov/flowbridge/pull/90) | `win11-flowbridge` |
| WhereIsIt | [PR #70](https://github.com/i-shutov/whereisit-ai/pull/70) | `win11-whereisit` |

После просмотра/слияния нужного PR в `main`: **Actions → Windows 11 VPS runner smoke → Run workflow** на `main`. Требуем `RUNNER_SMOKE_PASS`; проверка также печатает наличие `cargo/rustc`, MSVC, Python, MiKTeX/SSH/SQLite в зависимости от проекта. Отсутствие инструмента помечается `TOOL_MISSING`, а не автоматически маскируется успехом полноценной сборки.

Workflow запускается **вручную**, закреплён за именем репозитория, веткой `main` и требуемой меткой, проверяет `VM-326272`, Windows 11 x64, SID/учётную запись Admin и полный административный токен. Для smoke **нет checkout**, выполнения кода из PR и передачи секретов. Существующие GitHub-hosted workflow не меняются.

После smoke отдельно принимаются настоящие нативные сборки и инструменты:

| Проект | Что отдельно проверить |
|---|---|
| Tikzarium | Rust/Cargo, MSVC Build Tools, MiKTeX/XeLaTeX, сборку GUI/CLI; интерактивное GUI-тестирование — только в пользовательском сеансе, не в Session 0 |
| FlowBridge | Rust, CMake/MSVC, OpenSSH, сетевые тесты; реальные WFP/драйверные тесты — только на выделенной, откатываемой тестовой VM |
| WhereIsIt | Rust/egui, SQLite, headless smoke, синтетические диски и упаковку Windows; реальные CTF — по отдельному плану |

**Session 0:** служба Windows не равна интерактивному RDP-сеансу. `Running` не доказывает работоспособность кликов, ввода и визуальных скриншотов GUI. Также три одновременно тяжёлые сборки могут создавать ресурсные конфликты — при необходимости сериализовать их или использовать runner'ы последовательно.

### 5.4. Проверка после перезагрузки

В согласованное окно обслуживания (не посреди RDP-сеанса/сборки) перезагрузить VPS и заново проверить: `Get-TimeZone`, `w32tm /query /status`, HTTPS `SkewSeconds`, `3 × READY/Running`, `3 × Online/Idle`. **Если часы вновь смещаются после перезагрузки — исправлять источник времени VPS/гипервизора, а не регистрацию GitHub.**

## 6. Каталог «граблей»: симптом → первопричина → правильное действие

| Симптом | Обнаруженная причина | Правильное действие |
|---|---|---|
| Один repository-level runner не виден другим проектам | Репозиторная регистрация действует только на один repo | Три отдельные регистрации/службы либо runner на уровне организации |
| `.ps1`: «выполнение сценариев отключено» | `ExecutionPolicy` | `Set-ExecutionPolicy -Scope Process Bypass -Force`; затем `& <скрипт>` в **текущем** окне |
| Запуск через `powershell.exe -File` открыл новое окно, которое закрылось | Отдельный процесс/окно скрыли вывод для пользователя | Запускать скрипт через `& 'C:\...\Test-Win11Runners.ps1'` в текущей консоли |
| `config.cmd: Отказано в доступе` | У вложенных файлов были пустые/защищённые ACL | Исправить **наследование ACL файлов**, не повторять бесконечно `icacls /grant` только на каталоге |
| `Runner.Listener.exe --version` тоже возвращает «Отказано в доступе» | Проблема не в `.cmd`, а в доступе к EXE/блокировке запуска | Проверить `icacls` файла; v1.3 чинит ACL **до** регистрации; при корректных ACL проверить AppLocker/WDAC/Defender |
| Windows Admin, но runner регистрируется как `NETWORK SERVICE` | v1.0 использовал не ту identity для службы | В v1.3 `-ServiceAccount CurrentAdmin`; вводить пароль Windows, не PIN. Текущее `.\Admin` не ошибка |
| `Registered=True`, `.credentials=True`, `Service=YES`, но `Stopped` | Файлы и служба существуют, но сессия GitHub не держится | Сначала журналы и UTC; **не** переустанавливать вслепую |
| `StartService ReturnValue=0`, вскоре `Stopped`, SCM 7023 | Служба стартовала, listener завершился | Смотреть `ActionsRunnerService` и `_diag`, а не переустанавливать службу |
| `Connected to GitHub`, затем `invalid_client`/«registration has been deleted» | В этом инциденте — **сдвиг UTC на ~8 ч**, а не доказанное удаление регистрации | Сверить HTTPS UTC и W32Time; после синхронизации просто перезапустить службы |
| `GITHUB_TIME_UNVERIFIED: HTTP 404` от v1.4 | Ошибка URL проверочного запроса в том скрипте | Использовать `GET https://api.github.com/`, заголовок `Date`; **не** считать HTTP 404 признаком отсутствия NTP |
| После изменения часового пояса время всё ещё неверно | `tzutil` не является NTP-синхронизацией | Настроить W32Time/гипервизор, подтвердить `abs(SkewSeconds) <= 120` |
| Три службы `Running`, но job стоит `Queued` | Нет Online/Idle, метка `runs-on` не совпадает, workflow не на `main` или runner занят | Проверить GitHub UI, exact labels, ветку, ограничения workflow и загрузку VPS |
| Ранее работавшие `tikzarium-winserver` / `flowbridge-wfp-vm` workflow не попадают на новую VPS | Новые метки — **другие** | Не добавлять старые метки без анализа типа тестов; мигрировать каждую job отдельно |
| Headless-тест прошёл, GUI в RDP не проверялся | Windows-служба работает в Session 0 | GUI-приёмку проводить отдельно в интерактивном сеансе |

### 6.1. Если служба снова остановилась: только диагностировать

```powershell
# Локальное состояние трёх служб:
Get-CimInstance Win32_Service |
    Where-Object { $_.Name -like 'actions.runner.*' } |
    Select-Object Name, State, StartMode, StartName, ExitCode |
    Format-Table -AutoSize | Out-Host

# Сообщения GitHub Runner из Application Event Log:
Get-EventLog -LogName Application -Source ActionsRunnerService `
    -Newest 25 -ErrorAction SilentlyContinue |
    Select-Object TimeGenerated, EntryType, Message |
    Format-List | Out-Host

# Последние диагностические файлы каждого runner:
foreach ($name in @('win11-tikzarium','win11-flowbridge','win11-whereisit')) {
    $diag = "C:\GitHubRunners\$name\_diag"
    Get-ChildItem -LiteralPath $diag -Filter 'Runner_*.log' `
        -ErrorAction SilentlyContinue |
        Sort-Object LastWriteTime -Descending |
        Select-Object -First 2 FullName, LastWriteTime
}
```

**Не публиковать** `.credentials`, `.credentials_rsaparams`, содержимое регистрационных токенов или Windows-пароль. В диагностических журналах перед публикацией редактировать чувствительные пути/идентификаторы и потенциальные секреты.

### 6.2. Если UTC исправлен, но регистрации действительно нет на GitHub

Это **аварийная ветка**, не часть happy path:

1. Сначала подтвердить `abs(SkewSeconds) <= 120`, стабильное соединение с GitHub и точную ошибку в новом `_diag\Runner_*.log`; проверить серверный список runner'ов в GitHub Settings.
2. Только если регистрация реально отсутствует/удалена: остановить **конкретную** службу, сохранить безопасные логи, проверить точное имя службы/путь и действовать по официальной процедуре удаления/повторного добавления runner'а. **Не удалять все три регистрации массово и не удалять `_work`/системные инструменты.**
3. Повторно зарегистрировать только затронутый repo с **новым короткоживущим токеном**, выбрать существующую учётную запись Admin и service mode; проверить `Running` **спустя 20–30 секунд** и GitHub `Idle`.
4. Если проблема воспроизводится даже с правильным UTC — не повторять выдачу токенов по кругу; исследовать OAuth/proxy/TLS/логи GitHub Runner.

Команда `Runner.Listener.exe remove --local` в официальном runner удаляет локальную конфигурацию и ключи, **но сама по себе не удаляет службу Windows**; поэтому механическая очистка файлов и повторный `configure` поверх старой службы опасны. Штатная процедура предпочтительнее. Автоматическую v1.4-перерегистрацию в этом runbook **не использовать**.

## 7. Финальный acceptance checklist

- [x] Подтверждён хост `VM-326272`, Windows 11 Pro, учётная запись `Admin`.
- [x] Время приведено к корректному UTC; HTTPS-проверка показала расхождение **4,4 с** (20.11.2026).
- [x] Три runner'а настроены с отдельными именами и рабочими каталогами.
- [x] Три Windows-службы: `READY`, `Running`, `Auto`, `.\Admin`.
- [ ] Все три: **GitHub Settings → Actions → Runners → `Idle`/`Active`** (подтвердить на стороне GitHub).
- [ ] Три draft PR просмотрены и осознанно слиты в `main`.
- [ ] В каждом репозитории smoke workflow завершился с `RUNNER_SMOKE_PASS`.
- [ ] Сверены наличие и версии MSVC/Rust/MiKTeX/Python/SSH/SQLite по потребностям проектов.
- [ ] Выполнена плановая проверка перезагрузки: время сохранилось, службы стартовали, GitHub Online.
- [ ] Отдельно утверждена политика запуска **только доверенных работ** на административной VPS.

## 8. Ссылки и происхождение

**Официальные документы:**

- GitHub — [Adding self-hosted runners](https://docs.github.com/en/actions/how-tos/manage-runners/self-hosted-runners/add-runners)
- GitHub — [Configuring as a service](https://docs.github.com/en/actions/how-tos/manage-runners/self-hosted-runners/configure-the-application)
- GitHub — [Monitoring and troubleshooting](https://docs.github.com/en/actions/how-tos/manage-runners/self-hosted-runners/monitor-and-troubleshoot?platform=windows)
- GitHub — [Secure use reference](https://docs.github.com/en/actions/reference/security/secure-use)
- GitHub Runner — [исходники и релизы](https://github.com/actions/runner); [обсуждение ложного `invalid_client` при смещённом времени](https://github.com/actions/runner/issues/4648)
- Microsoft — [Windows Time service](https://learn.microsoft.com/en-us/windows-server/networking/windows-time-service/windows-time-service-tools-and-settings)
- Microsoft — [icacls](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/icacls)

**Доказательства в выполненной работе:** результат `SkewSeconds = 4,4` и таблица `3 × READY/Running/Auto`, присланные владельцем VPS 20.11.2026. Статус на стороне GitHub и успешные CI jobs в этих данных **ещё не подтверждены**.

**Решающее практическое правило:** **TIME → ACL/EXE → REGISTER → WINDOWS SERVICE → GITHUB ONLINE → SMOKE CI**. Нельзя считать какой-либо предыдущий шаг доказательством следующего.
