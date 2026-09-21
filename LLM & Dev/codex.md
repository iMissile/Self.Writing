Да. Ниже соберу уже **нормальную инструкцию с нуля**, с учётом того, что мы реально проверили на Windows 10, какие ветки оказались тупиковыми и какая конфигурация у вас заработала.

Важная поправка к нашим ранним экспериментам: проблема `helper_sandbox_lock_failed / SetNamedSecurityInfoW ... error 5` — не особенность вашей машины. Сейчас есть несколько свежих Windows-багрепортов Codex с тем же поведением, включая Codex 0.154.x. ([GitHub][1]) Ваш `setup_error.json` подтвердил именно этот случай. 

# Установка Codex CLI на Windows

## 1. Исходная конфигурация

Эта инструкция рассчитана на такой сценарий:

```text
Windows 10/11
PowerShell 7
репозитории находятся на Windows filesystem
без WSL
Node.js 22+
npm
Python/uv — если проект Python
Claude Code / Cursor могут использовать тот же repository
```

Codex при этом запускается **самостоятельно из терминала**, а не как расширение Cursor.

Для вашего сценария это предпочтительнее, чем переносить repository в WSL.

---

# 2. Установить современный Node.js

Проверяем:

```powershell
node --version
npm --version
```

У нас первоначально было:

```text
node v22.14.0
npm 11.1.0
```

и обновление до npm 12 не проходило из-за требований npm к версии Node.

Поэтому сначала обновляем Node.

Посмотреть установленный пакет:

```powershell
winget list node
```

В нашем случае это был:

```text
OpenJS.NodeJS.22
```

Обновление:

```powershell
winget upgrade --id OpenJS.NodeJS.22
```

После перезапуска PowerShell:

```powershell
node --version
```

Рабочий результат у нас:

```text
v22.23.2
```

После этого при желании обновляем npm:

```powershell
npm install -g npm@12.0.2
```

и проверяем:

```powershell
npm --version
```

У нас получилось:

```text
12.0.2
```

---

# 3. Установить Codex CLI

```powershell
npm install -g @openai/codex
```

Проверка:

```powershell
codex --version
```

В нашей проверенной конфигурации:

```text
codex-cli 0.154.0
```

Посмотреть, какой executable запускается:

```powershell
where.exe codex
```

При npm global install ожидается что-то вроде:

```text
C:\Users\<USER>\AppData\Roaming\npm\codex
C:\Users\<USER>\AppData\Roaming\npm\codex.cmd
```

После обновления Codex полезно периодически снова делать:

```powershell
codex --version
codex doctor --all
```

---

# 4. Первый запуск

Перейти непосредственно в repository:

```powershell
cd D:\path\to\repository
codex
```

Codex выполнит авторизацию через ChatGPT.

После входа проверить:

```text
/status
```

Нас интересуют прежде всего:

```text
Directory:     D:\path\to\repository
Permissions:   ...
Agents.md:     ...
Account:       ... (Plus/Pro/etc.)
```

---

# 5. Главное: Windows sandbox

Вот здесь оказалась основная сложность.

Codex поддерживает нативный Windows sandbox. Для Windows имеется два варианта:

```toml
[windows]
sandbox = "elevated"
```

и fallback:

```toml
[windows]
sandbox = "unelevated"
```

`elevated` обеспечивает более сильную Windows-изоляцию и в исправной конфигурации был бы предпочтительным.

## Но сначала пробуем elevated

Файл:

```text
%USERPROFILE%\.codex\config.toml
```

Добавить:

```toml
[windows]
sandbox = "elevated"
```

Запустить:

```powershell
codex
```

и затем:

```powershell
codex doctor --all
```

Если всё исправно — оставляем `elevated`.

---

# 6. Известная проблема elevated sandbox

На текущих Windows-сборках Codex может появиться:

```text
sandbox provisioning failed
helper_sandbox_lock_failed
```

Более конкретная ошибка:

```text
SetNamedSecurityInfoW sandbox dir failed: 5
```

Windows error 5 означает `Access Denied`.

У вас она была зафиксирована непосредственно в:

```text
%USERPROFILE%\.codex\.sandbox\setup_error.json
```

сообщением:

```text
lock sandbox bin dir
C:\Users\<USER>\.codex\.sandbox-bin failed:
SetNamedSecurityInfoW sandbox dir failed: 5
```



Это соответствует свежим открытым Windows issues Codex. Один из багрепортов описывает именно сбой повторного применения ACL к существующему `.sandbox-bin`; другой воспроизводит ошибку на Codex 0.154.x. ([GitHub][1])

В исходниках Codex сам `helper_sandbox_lock_failed` определяется как ошибка helper'а при блокировке sandbox-каталогов через ACL. ([GitHub][2])

---

# 7. Чего НЕ надо делать при этой ошибке

В ходе диагностики мы пробовали:

```powershell
takeown ...
icacls ... /grant ... FullControl
```

Это оказалось неустойчивым workaround.

Codex может после успешной операции снова изменить ACL `.sandbox-bin`, после чего следующая sandbox initialization опять получает error 5. Такое же поведение независимо наблюдалось в свежих Windows bug reports. ([GitHub][3])

Мы также проверили вариант пересоздания `.sandbox-bin` с правильным владельцем. У вас owner действительно стал:

```text
HP-G6-ILYA\Ilya
```

а ACL выглядел вполне нормальным:

```text
SYSTEM          FullControl
Administrators  FullControl
Ilya            FullControl
CodexSandboxUsers ReadAndExecute
```

но `doctor` всё равно возвращал:

```text
helper_sandbox_lock_failed
```

Поэтому я **не рекомендую строить установку Codex вокруг ручного ремонта ACL**.

Есть более свежий отчёт, где пересоздание `.sandbox-bin` действительно позволило восстановить elevated provisioning, поэтому этот путь может работать в некоторых конфигурациях, но это скорее recovery workaround для конкретного бага, а не нормальная процедура установки. ([GitHub][4])

---

# 8. Рабочий fallback: unelevated

Если `elevated` выдаёт описанный выше баг, меняем:

```toml
[windows]
sandbox = "elevated"
```

на:

```toml
[windows]
sandbox = "unelevated"
```

Это именно тот вариант, который **реально заработал у вас**.

Запускаем:

```powershell
cd D:\path\to\repository

codex --sandbox workspace-write --ask-for-approval on-request
```

Внутри:

```text
/status
```

Нужный результат:

```text
Permissions: Workspace (Ask for approval)
```

---

# 9. Обязательно проверить sandbox реальной записью

Одного `/status` недостаточно.

Попросить Codex:

```text
Создай в корне репозитория файл codex-write-test.txt
с текстом "OK", затем прочитай его содержимое.
```

В исправной конфигурации у нас получилось:

```text
Added codex-write-test.txt
1 +OK

Explored
└ Read codex-write-test.txt

Создан файл codex-write-test.txt и прочитан: OK.
```

При этом **не было approval для выхода из sandbox**.

Это главный smoke test.

После проверки файл можно удалить.

---

# 10. Проверить выполнение процессов

Следующий тест:

```text
Запусти git status и python --version.
```

У нас Codex самостоятельно получил:

```text
git status: ...
python --version: Python 3.13.2
```

Значит в рабочей конфигурации доступны и filesystem write, и subprocess execution.

Для Python-проекта на `uv` не надо проверять:

```powershell
pytest
```

потому что это может вызвать глобальный Python.

Правильно:

```text
Запусти uv run pytest --collect-only -q.
```

И вообще проектные команды стоит выполнять как:

```powershell
uv run python ...
uv run pytest ...
uv run ruff ...
uv run mypy ...
```

а управление зависимостями:

```powershell
uv add ...
uv remove ...
```

вместо произвольного `pip install`.

---

# 11. Диагностика Codex

Главная команда:

```powershell
codex doctor --all
```

Компактно:

```powershell
codex doctor --summary
```

Для машинно-читаемой диагностики:

```powershell
codex doctor --json
```

Например, Windows sandbox можно посмотреть так:

```powershell
codex doctor --json |
    ConvertFrom-Json |
    Select-Object -ExpandProperty checks |
    Select-Object -ExpandProperty 'sandbox.helpers' |
    ConvertTo-Json -Depth 10
```

При нормальной установке там не должно быть:

```text
status: fail
helper_sandbox_lock_failed
```

Для нашего `unelevated` workaround главным критерием всё же является не косметически идеальный `doctor`, а успешное выполнение workspace операций внутри sandbox.

---

# 12. Если снова появляется error 5

Сначала смотрим:

```powershell
Get-Content "$env:USERPROFILE\.codex\.sandbox\setup_error.json" -Raw
```

Если там:

```text
helper_sandbox_lock_failed
SetNamedSecurityInfoW sandbox dir failed: 5
```

не начинаем бесконечно менять ACL.

Сначала:

```powershell
codex --version
```

Обновляем Codex:

```powershell
npm install -g @openai/codex@latest
```

и снова проверяем `elevated`.

Если актуальная версия всё ещё воспроизводит баг — возвращаемся на:

```toml
[windows]
sandbox = "unelevated"
```

до исправления Windows sandbox.

С учётом того, что issue всё ещё открыт, при будущих обновлениях Codex я бы периодически повторял тест `elevated`. ([GitHub][5])

---

# 13. Не использовать danger-full-access как решение

Не надо лечить проблемы Windows sandbox вот этим:

```powershell
codex --sandbox danger-full-access
```

и тем более:

```powershell
codex --dangerously-bypass-approvals-and-sandbox
```

Для повседневной работы с repository нам нужен:

```text
workspace-write
+
on-request
```

Это даёт Codex автономность **внутри repository**, сохраняя границу вокруг workspace.

Именно этого поведения мы добились на `unelevated`.

---

# 14. Базовый config.toml

После наших тестов я бы начинал с **минимальной** конфигурации:

```toml
[windows]
sandbox = "unelevated"

[projects.'d:\path\to\repository']
trust_level = "trusted"
```

Не стоит сразу наваливать туда десятки экспериментальных параметров.

Сначала добиваемся:

```text
/status
→ Workspace (Ask for approval)
```

и успешных:

```text
read
write
git status
uv run ...
```

Только после этого добавляем модель, reasoning, auto-review, network policy и другие удобства.

---

# 15. PowerShell

Для Codex желательно использовать современный PowerShell 7:

```powershell
$PSVersionTable.PSVersion
```

У вас сейчас PowerShell 7.6.6.

Для UTF-8 в profile разумно иметь:

```powershell
$utf8 = [System.Text.UTF8Encoding]::new($false)

$OutputEncoding = $utf8
[Console]::InputEncoding  = $utf8
[Console]::OutputEncoding = $utf8
```

У нас это исправило часть проблем с терминальным выводом: `doctor` стал видеть code page `65001` и VT processing.

Но есть ещё одна оставшаяся проблема в вашем profile:

```text
Set-PSReadLineOption:
...\Microsoft.PowerShell_profile.ps1:37
```

Codex запускает PowerShell subprocess, тот загружает profile, и эта ошибка загрязняет tool output.

Её нужно исправить отдельно.

Это **не проблема Codex sandbox**.

---

# 16. Tabby и вставка

В ходе настройки мы отдельно установили, что Tabby корректно передаёт обычный `Tab`:

```text
Key = Tab
Modifiers = None
```

и PSReadLine его получает.

Проблема была конкретно в поведении:

```powershell
MenuComplete
```

а не в Codex.

Для более традиционного completion:

```powershell
Set-PSReadLineKeyHandler -Key Tab `
    -Function TabCompleteNext

Set-PSReadLineKeyHandler -Key Shift+Tab `
    -Function TabCompletePrevious
```

А серую history suggestion можно принимать `RightArrow`.

Это тоже не относится непосредственно к установке Codex.

---

# 17. Codex + Claude Code + Cursor в одном repository

Это нормальная схема, если агенты работают **последовательно**, как у вас.

Не нужно создавать отдельную копию repository только потому, что используются разные агенты.

Но проектные инструкции должны явно запрещать агенту уничтожать изменения другого агента. Например:

```text
Before substantial changes inspect git status.

Treat existing uncommitted changes as user-owned unless clearly
established otherwise.

Do not use git reset --hard, git clean, or restore/checkout unrelated
files without explicit permission.

Do not automatically discard modifications made by another agent.
```

Для Codex основным project instruction mechanism будет `AGENTS.md`.

При этом существующие:

```text
CLAUDE.md
.claude/**
```

не надо удалять или превращать механически в Codex-конфигурацию.

---

# 18. Не просить Codex без необходимости запускать вложенный Codex

Это ещё одна находка нашего тестирования.

Когда мы попросили текущий Codex проанализировать конфигурацию проекта, он зачем-то выполнил:

```text
codex debug prompt-input "configuration inspection only"
```

В `unelevated` sandbox вложенный Codex попытался использовать временный путь:

```text
\tmp\arg0\codex-...
```

и получил:

```text
Error: Отказано в доступе. (os error 5)
```

При этом обычные операции:

```text
read/write repository
git status
python
pytest
```

работали.

Поэтому это не основание считать весь `unelevated` sandbox сломанным.

Практическое правило: при подготовке `AGENTS.md` и анализе repo **не заставлять Codex запускать `codex debug` или другой вложенный экземпляр Codex без необходимости**.

---

# 19. Итоговая рекомендуемая схема

На **сегодня, 21 сентября 2026**, для вашей Windows-машины я бы использовал:

```text
Windows filesystem
        │
        ▼
PowerShell 7
        │
        ▼
Node 22.23+
        │
        ▼
npm 12
        │
        ▼
@openai/codex
        │
        ▼
Codex CLI
        │
        ├── workspace-write
        ├── approval: on-request
        └── Windows sandbox: unelevated
                │
                ▼
        Git repository
          ├── AGENTS.md       ← Codex
          ├── CLAUDE.md       ← Claude Code
          ├── .claude/        ← Claude-specific
          ├── pyproject.toml
          └── uv.lock
```

`elevated` является более желательным Windows backend, **но не на вашей текущей комбинации Codex/Windows**, пока воспроизводится `SetNamedSecurityInfoW ... error 5`. Это известный класс свежих Windows sandbox bugs, а не повод отключать sandbox целиком. ([GitHub][1])

## Короткий installation checklist

Если завтра ставить всё заново на другую Windows-машину, мой порядок был бы таким:

```powershell
# 1. Node
winget upgrade --id OpenJS.NodeJS.22

node --version
npm --version

# 2. Codex
npm install -g @openai/codex

codex --version
where.exe codex

# 3. Repository
cd D:\path\to\repo

# 4. First launch
codex

# 5. Diagnostics
codex doctor --all
```

Сначала попробовать:

```toml
[windows]
sandbox = "elevated"
```

Если получаем подтверждённый:

```text
helper_sandbox_lock_failed
SetNamedSecurityInfoW ... failed: 5
```

не заниматься бесконечным `takeown/icacls`, а временно:

```toml
[windows]
sandbox = "unelevated"
```

и:

```powershell
codex --sandbox workspace-write --ask-for-approval on-request
```

После чего обязательные smoke tests:

```text
Создай тестовый файл в корне repo и прочитай его.

Запусти git status.

Запусти uv run python --version.

Запусти uv run pytest --collect-only -q.
```

Если всё это проходит **без выхода из sandbox**, базовая установка Codex CLI закончена.

---

Следующий этап я бы уже отделил от **установки**: сделать вам хорошую production-конфигурацию `config.toml + AGENTS.md`, которая сосуществует с вашей существующей конфигурацией Claude Code, использует `uv`, даёт Codex больше автономности и не дублирует `CLAUDE.md`. Это как раз то место, где мы остановились.

[1]: https://github.com/openai/codex/issues/36475?utm_source=chatgpt.com "Windows sandbox refresh fails with helper_sandbox_lock_failed after SetNamedSecurityInfoW(ERROR_ACCESS_DENIED) on existing .sandbox-bin · Issue #36475 · openai/codex · GitHub"
[2]: https://github.com/openai/codex/blob/main/codex-rs/windows-sandbox-rs/src/setup_error.rs?utm_source=chatgpt.com "codex/codex-rs/windows-sandbox-rs/src/setup_error.rs at main · openai/codex · GitHub"
[3]: https://github.com/openai/codex/issues/40550?utm_source=chatgpt.com "Windows app setup fails with helper_failed / Access Denied on codex-windows-sandbox-setup.exe (26.818.8289.0) · Issue #40550 · openai/codex"
[4]: https://github.com/openai/codex/issues/46380?utm_source=chatgpt.com "Windows elevated sandbox re-provisioning fails on previously locked .sandbox-bin ACL after upgrade · Issue #46380 · openai/codex · GitHub"
[5]: https://github.com/openai/codex/issues/45153?utm_source=chatgpt.com "Windows: shell commands fail with helper_sandbox_lock_failed (error 5) · Issue #45153 · openai/codex · GitHub"
