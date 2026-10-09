# OpenCode Desktop 2.0.26 — исправление ошибки Desktop IPC handler failed в Windows

**Дата фиксации:** 9 октября 2026 года  
**Статус:** **ИСПРАВЛЕНО, проверено пользователем**  
**Платформа:** Windows 10, сборка 19045.6456; PowerShell 7.6.6  
**Приложение:** OpenCode Desktop 2.0.26  
**Сценарий:** приложение только что установлено, GUI открывается, но работа блокируется ошибкой запуска фонового сервера.

## 1. Симптомы

При запуске OpenCode Desktop появлялось сообщение:

```text
Error: Desktop IPC handler failed
...
Server process exited with code 1
Error: Managed service port 49374 on 127.0.0.1 is already in use by another process.
Configure another port with `opencode service set port <port>` and start the service again.
...
Failed to start server. Is port 49374 in use?
```

Команды `opencode service status`, `opencode service stop` и т. п. не выполнялись из CMD:

```text
"opencode" не является внутренней или внешней командой,
исполняемой программой или пакетным файлом.
```

Проверка порта не находила активных TCP-соединений:

```powershell
Get-NetTCPConnection -LocalPort 49374 -ErrorAction SilentlyContinue |
    Select-Object LocalAddress, LocalPort, State, OwningProcess
```

Команда возвращала пустой результат. Это **не доказывает**, что порт доступен для привязки: возможны исключённые/зарезервированные диапазоны и кратковременная занятость.

> **Важно для PowerShell:** `where` — псевдоним `Where-Object`, поэтому для поиска EXE используйте `where.exe opencode` или `Get-Command opencode`. В данном случае отдельный CLI не был добавлен в `PATH`.

## 2. Диагностические доказательства

Журналы OpenCode Desktop находятся в:

```text
%APPDATA%\ai.opencode.desktop\logs\<каталог запуска>\
```

Для данного инцидента:

```text
C:\Users\Ilya\AppData\Roaming\ai.opencode.desktop\logs\20261009T064030\
```

Ключевые строки `main.log`:

```text
[2026-10-09 09:40:30.396] [info] (main) app starting { version: '2.0.26', packaged: true, ... }
[2026-10-09 09:40:30.568] [info] (main) starting v2 background service
[2026-10-09 09:40:30.569] [info] (main) v2 CLI executable resolved {
  bundled: 'C:\\Users\\Ilya\\AppData\\Local\\Programs\\@opencodedesktop\\resources\\opencode-cli.exe',
  packaged: true
}
[2026-10-09 09:40:30.571] [info] (main) v2 CLI version bundled { version: '2.0.26' }
[2026-10-09 09:40:30.573] [info] (main) v2 CLI staged executable reused {
  path: 'C:\\Users\\Ilya\\AppData\\Roaming\\ai.opencode.desktop\\cli\\2.0.26\\opencode-cli.exe',
  version: '2.0.26'
}
[2026-10-09 09:40:30.852] [info] (main) v2 CLI background service starting { reason: 'missing' }
```

В `renderer.log` зафиксированы `Desktop IPC handler failed`, выход процесса сервера с кодом `1` и ошибка привязки к `127.0.0.1:49374`.

Таким образом, **доказан сбой запуска сервера на порту 49374**, но точный механизм первоначальной недоступности порта (другой процесс, резервирование Windows или иная причина) **не был установлен**.

## 3. Рабочее решение

**Что помогло:** использование встроенного `opencode-cli.exe` и перенос фоновой службы с порта **49374** на **43741**. Пользователь подтвердил: **«заработало!!»**.

Перед выполнением закройте OpenCode Desktop. В **PowerShell 7** запустите весь блок:

```powershell
# Встроенный CLI, фактический путь для OpenCode Desktop 2.0.26
$cli = Join-Path $env:APPDATA `
    'ai.opencode.desktop\cli\2.0.26\opencode-cli.exe'

if (-not (Test-Path $cli)) {
    throw "OpenCode CLI not found: $cli"
}

# Новый порт (ниже стандартного динамического диапазона 49152–65535)
$port = 43741

# Проверить возможность привязаться к 127.0.0.1:$port
$listener = [System.Net.Sockets.TcpListener]::new(
    [System.Net.IPAddress]::Loopback,
    $port
)

try {
    $listener.Start()
    Write-Host "Port $port is available" -ForegroundColor Green
}
catch {
    throw "Port $port cannot be bound: $_"
}
finally {
    $listener.Stop()
}

# Сохранить новый порт службы
& $cli service set port $port
if ($LASTEXITCODE -ne 0) {
    throw "Failed to configure OpenCode service"
}

# Запустить сервер и проверить его статус
& $cli service start
& $cli service status
```

Затем снова запустите **OpenCode Desktop**.

**Фактический результат:** после этого решения OpenCode Desktop заработал. Точный текст вывода команд `service start` и `service status` не сохранялся; подтверждён пользовательский результат, а не конкретная строка ответа CLI.

### Почему работал путь к CLI, но не команда `opencode`

В установленном Desktop был собственный исполняемый файл:

```text
%APPDATA%\ai.opencode.desktop\cli\2.0.26\opencode-cli.exe
```

Его обнаружили в журнале `main.log`. Поэтому CLI можно было вызвать по полному пути через оператор PowerShell `&`, **не устанавливая отдельный CLI** и не изменяя `PATH`.

## 4. Если ошибка повторится после обновления

При обновлении OpenCode каталог `cli\2.0.26` может измениться. Проверьте свежий `main.log` на строки `v2 CLI staged executable reused` или найдите актуальный исполняемый файл:

```powershell
Get-ChildItem "$env:APPDATA\ai.opencode.desktop\cli" `
    -Recurse -File -Filter opencode-cli.exe -ErrorAction SilentlyContinue |
    Sort-Object LastWriteTime -Descending |
    Select-Object -First 10 FullName, LastWriteTime
```

Затем подставьте найденный путь в `$cli` и повторите смену порта (при необходимости выберите другой свободный порт).

Для проверки резервирования портов и текущей занятости:

```powershell
netsh interface ipv4 show excludedportrange protocol=tcp
Get-NetTCPConnection -LocalPort 49374 -ErrorAction SilentlyContinue
Get-NetTCPConnection -LocalPort 43741 -ErrorAction SilentlyContinue
```

Проверка с `TcpListener` оценивает возможность привязки **в момент проверки**, но не гарантирует, что порт не займёт другой процесс позднее.

### Как быстро прочитать журналы нового запуска

```powershell
$logDir = Get-ChildItem "$env:APPDATA\ai.opencode.desktop\logs" -Directory |
    Sort-Object Name -Descending |
    Select-Object -First 1

foreach ($name in @('main.log', 'crash.log', 'renderer.log', 'network.log')) {
    $path = Join-Path $logDir.FullName $name
    Write-Host "`n========== $name ==========" -ForegroundColor Cyan
    if (Test-Path $path) { Get-Content $path }
}
```

При публикации журналов проверьте, не содержат ли они токены, пароли и другие секреты.

## 5. Чего делать не потребовалось

- Переустанавливать OpenCode Desktop.
- Устанавливать отдельную версию `opencode` в `PATH`.
- Удалять каталоги профиля или базу данных OpenCode.
- Принудительно завершать неизвестные процессы.
- Перезагружать Windows.

## 6. Краткая карточка инцидента

| Поле | Значение |
| --- | --- |
| Программа | OpenCode Desktop 2.0.26 |
| ОС | Windows 10 (10.0.19045.6456) |
| Оболочка | PowerShell 7.6.6 |
| Ошибка | `Desktop IPC handler failed` |
| Сбойный компонент | V2 background / managed service |
| Исходный порт | `127.0.0.1:49374` |
| Диагностика сокета | `Get-NetTCPConnection` не нашёл соединений на 49374 |
| CLI | `%APPDATA%\ai.opencode.desktop\cli\2.0.26\opencode-cli.exe` |
| Применённый порт | `43741` |
| Решение | `service set port 43741` → `service start` → `service status` |
| Результат | **Исправлено; приложение запустилось** |
| Достоверность причины | Ошибка bind подтверждена; первопричина занятости порта не доказана |

---

*Документ составлен по фактическим сообщениям, журналам и подтверждённому успешному исправлению. Не является официальной инструкцией разработчиков OpenCode.*
