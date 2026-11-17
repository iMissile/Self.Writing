# Установка клиентской платформы

Инструкция относится к переносимому `wolfram-platform-client.zip`. Она не устанавливает сервер, не запускает Wolfram kernel и не регистрирует MCP автоматически.

## macOS: проверка пакета и установка

Используйте hash, опубликованный владельцем конкретной сборки. Распаковывайте пакет только в новый versioned client root; не распаковывайте поверх старого каталога и не устанавливайте из checkout серверного репозитория.

```sh
set -eu
APP_ROOT="$HOME/Library/Application Support/WolframServer"
ZIP_PATH="/path/to/wolfram-platform-client.zip"
EXPECTED_SHA256="<owner-provided-sha256>"
CLIENT_RELEASE="$APP_ROOT/clients/client-$EXPECTED_SHA256"
KEY_DIR="$APP_ROOT/credentials/client-$EXPECTED_SHA256"
CONFIG_DIR="$APP_ROOT/config/client-$EXPECTED_SHA256"
test ! -e "$CLIENT_RELEASE"
test ! -e "$KEY_DIR"
test ! -e "$CONFIG_DIR"
printf '%s  %s\n' "$EXPECTED_SHA256" "$ZIP_PATH" | shasum -a 256 -c -
umask 077
mkdir -p "$CLIENT_RELEASE" "$KEY_DIR" "$CONFIG_DIR"
chmod -N "$KEY_DIR" "$CONFIG_DIR"
chmod 700 "$KEY_DIR" "$CONFIG_DIR"
unzip -q "$ZIP_PATH" -d "$CLIENT_RELEASE"
CLIENT_ROOT="$CLIENT_RELEASE/client"
uv sync --locked --project "$CLIENT_ROOT"
UV_PATH="$(command -v uv)"
PYTHON_PATH="$CLIENT_ROOT/.venv/bin/python"
CREDENTIAL_FILE="$KEY_DIR/research-client.json"
CONFIG_OUTPUT="$CONFIG_DIR/mcp.json"
KEY_MANAGER_FILE="/path/to/separate-admin-key-manager.json"
```

`uv sync` запускается для извлечённого каталога `client/`, который содержит собственные `pyproject.toml` и `uv.lock`; не указывайте каталог серверного checkout.

## API-ключи и права

Первый ключ на новой машине выдаёт администратор через портал: выбирает существующего владельца, назначение, scopes и срок. При наличии отдельного административного manager credential используйте CLI ниже. Для самой машины или агента не требуется создавать пользователя Linux или дополнительную роль портала.

Если секрет получен в браузере, владелец сохраняет его лично в новом закрытом UTF-8 файле `CREDENTIAL_FILE`. Формат файла содержит ровно три поля:

```json
{
  "schema_version": 1,
  "base_url": "https://<public-host>",
  "token": "<issued-token>"
}
```

Это шаблон формы, не действующий ключ. Не передавайте содержимое файла агенту или в чат. Приватный каталог и права создаются до сохранения; на POSIX файл имеет режим `0600`, на Windows наследует ACL только владельца и `SYSTEM` из отдельного нового каталога. Сам клиент проверяет эти условия при чтении. Если `configure-client.py` отказал из-за прав, исправьте права конкретного credential-файла, не отключая проверку.

Сначала выберите существующего пользователя-владельца с минимальной ролью, подходящей задаче. Роль владельца ограничивает максимальные scopes; отдельной роли `agent` нет. Scope `keys:manage` — административное полномочие: его требует отдельный bearer администратора, учётная запись должна быть активна и пароль должен быть сменён. Не добавляйте `keys:manage` в обычный MCP/compute credential; старые ключи не наследуют этот scope автоматически.

Выдайте обычный ключ с явным списком минимально необходимых scopes, меткой, сроком UTC и новым путём файла. Для ориентирования в операциях:

| Scope | Применение |
| --- | --- |
| `compute:read` | capabilities, capacity, resource stats, job list/status/card, artifacts и manifest metadata |
| `compute:download` | бинарные результаты и export trace |
| `compute:submit` | upload deployment, validate и atomic try-submit |
| `compute:control` | pause/cancel/resume собственного задания |
| `compute:control_all` | административное управление заданиями; admin only |
| `compute:approve` | утверждение deployment; admin only |
| `datasets:read` | список, metadata, schema, preview |
| `datasets:download` | бинарное скачивание Parquet и native formats |
| `datasets:write` | начало и финализация загрузки dataset |
| `keys:manage` | list/create/revoke ключей; admin only, отдельный manager bearer |

Создание token выполняется в новом файле под `KEY_DIR`; ключевой CLI печатает только публичные метаданные и путь. Ниже пути и идентификаторы — локальные значения владельца, token в команде не указывается.

```sh
OWNER_USERNAME="existing-owner"
KEY_LABEL="research-client-mac"
EXPIRES_AT_UTC="YYYY-MM-DDTHH:MM:SSZ"
uv run --offline --locked --no-sync --project "$CLIENT_ROOT" python "$CLIENT_ROOT/scripts/api-access-keys.py" \
  --credential-file "$KEY_MANAGER_FILE" --timeout-seconds 30 --max-response-bytes 1048576 \
  create --owner-username "$OWNER_USERNAME" --label "$KEY_LABEL" \
  --scope compute:read --scope compute:submit --scope datasets:read --scope datasets:write \
  --expires-at "$EXPIRES_AT_UTC" --output "$CREDENTIAL_FILE"
```

Выберите только scopes, необходимые конкретной роли и задаче; приведённый список не обязателен. Управление ключами доступно командами `list` и `revoke` и требует того же отдельного manager credential:

```sh
uv run --offline --locked --no-sync --project "$CLIENT_ROOT" python "$CLIENT_ROOT/scripts/api-access-keys.py" \
  --credential-file "$KEY_MANAGER_FILE" --timeout-seconds 30 --max-response-bytes 1048576 \
  list --limit 50 --offset 0
uv run --offline --locked --no-sync --project "$CLIENT_ROOT" python "$CLIENT_ROOT/scripts/api-access-keys.py" \
  --credential-file "$KEY_MANAGER_FILE" --timeout-seconds 30 --max-response-bytes 1048576 \
  revoke --key-id "$KEY_ID"
```

`list` показывает публичные метаданные без token; `revoke` принимает публичный `key_id`. Не копируйте manager credential в MCP. Не помещайте secret в argv, stdout/stderr, environment или контекст агента.

На macOS `chmod 600` не очищает extended ACL. Здесь `KEY_DIR` и `CONFIG_DIR` являются новыми release-specific каталогами; перед использованием очищайте ACL только у этих каталогов и новых файлов `CREDENTIAL_FILE`/`CONFIG_OUTPUT`, затем задавайте режимы `0700`/`0600`. Не применяйте `chmod -N` к `$HOME` или профилю целиком. Поведение `-N` описано в [man page `chmod(1)` от Apple](https://raw.githubusercontent.com/apple-oss-distributions/file_cmds/main/chmod/chmod.1).

```sh
chmod -N "$CREDENTIAL_FILE"
chmod 600 "$CREDENTIAL_FILE"
```

## Локальная gateway-конфигурация и ручная регистрация

`configure-client.py` читает credential только в процессе, проверяет формат, HTTPS origin и private permissions, не выполняя API-запросов. Он записывает новый gateway JSON и возвращает публичные `config_path`, `command`, `args` и безопасные Python environment values.

```sh
uv run --offline --locked --no-sync --project "$CLIENT_ROOT" python "$CLIENT_ROOT/scripts/configure-client.py" \
  --credential-file "$CREDENTIAL_FILE" --config-output "$CONFIG_OUTPUT" \
  --uv-path "$UV_PATH" --timeout-seconds 30 --max-frame-bytes 1048576 --max-inflight-calls 1
chmod -N "$CONFIG_OUTPUT"
chmod 600 "$CONFIG_OUTPUT"
```

Проверьте возвращённые `command`/`args`, затем вручную добавьте stdio server в Codex CLI. Этот скрипт не меняет глобальную конфигурацию Codex.

```sh
codex mcp add wolfram-server \
  --env PYTHONUTF8=1 --env PYTHONIOENCODING=utf-8 --env PYTHONUNBUFFERED=1 -- \
  "$UV_PATH" --no-config run --offline --no-cache --no-project \
  --python "$PYTHON_PATH" python "$CLIENT_ROOT/scripts/datasets-mcp.py" \
  --config "$CONFIG_OUTPUT"
```

## Переносимые MCP-конфигурации

В STDIO-конфигурации общие для клиентов только `command`, `args` и `env`; поля, показанные выше, не привязаны к Codex. Если клиент использует стандартный для своей платформы `mcpServers`, перенесите в него результат `configure-client.py` и замените placeholders путями именно этого компьютера:

```json
{
  "mcpServers": {
    "wolfram-server": {
      "command": "<UV_PATH>",
      "args": [
        "--no-config", "run", "--offline", "--no-cache", "--no-project",
        "--python", "<PYTHON_PATH>", "python",
        "<CLIENT_ROOT>/scripts/datasets-mcp.py", "--config", "<CONFIG_OUTPUT>"
      ],
      "env": {
        "PYTHONUTF8": "1",
        "PYTHONIOENCODING": "utf-8",
        "PYTHONUNBUFFERED": "1"
      }
    }
  }
}
```

Клиентский конфигурационный файл содержит путь к закрытому gateway JSON, а не сам bearer token. Не записывайте token в конфигурацию MCP, параметры процесса, журнал или контекст модели.

Текущий публичный Streamable HTTP endpoint: `https://wolfram-server.ru/mcp`. 27 октября 2026 г. официальный MCP 2.3.0 client успешно выполнил `initialize`, `tools/list` (26 инструментов) и read-only `compute_resources` с окнами `[30, 300]`. Это датированная проверка MCP transport/tooling, а не проверка API readiness, доступности ресурсов задания или будущей доступности endpoint. Перед работой каждого нового сеанса выполните свежую MCP read-only проверку и отдельно проверяйте актуальное состояние compute/datasets через доступные read-only API.

Клиент на другой машине может подключиться к этому endpoint. Каждый запрос передаёт `Authorization: Bearer …`. Получайте значение из защищённого хранилища секретов клиента или credential manager. Переносимый пример полей (синтаксис ссылки на секрет зависит от клиента):

```json
{
  "mcpServers": {
    "wolfram-research": {
      "url": "https://wolfram-server.ru/mcp",
      "headers": {
        "Authorization": "Bearer <runtime-injected-token>"
      }
    }
  }
}
```

Используйте только необходимые scopes существующего владельца: `compute:read` для каталога, статистики и metadata, `compute:download` для binary и trace, `compute:submit` для подачи, `compute:control` для разрешённых controls, `compute:approve` только admin; datasets используют `datasets:read`, `datasets:download` для Parquet/native binary и `datasets:write`. Административный `keys:manage` остаётся в отдельном manager credential. После подключения выполните `initialize`, `tools/list` и свежий read-only запрос; доступность и состав tools могут измениться.

После `Transport closed` или потери соединения вручную переподключите transport, повторите `initialize` и `tools/list`, затем выполните read-only probe. Не автоматизируйте UI клиента. Если ответ на `compute_try_submit` неизвестен, сначала проверьте `compute_list_jobs`/`compute_status`; не создавайте второе задание и при необходимости повторяйте исходную подачу только с тем же `request_id`. Закрытие соединения само по себе не отменяет задание.

## Linux

Используйте отдельные XDG-каталоги и те же POSIX-права. Путь credential также должен быть новым обычным файлом владельца без group/other access.

```sh
set -eu
APP_DATA_ROOT="${XDG_DATA_HOME:-$HOME/.local/share}/wolfram-server"
APP_CONFIG_ROOT="${XDG_CONFIG_HOME:-$HOME/.config}/wolfram-server"
ZIP_PATH="/path/to/wolfram-platform-client.zip"
EXPECTED_SHA256="<owner-provided-sha256>"
CLIENT_RELEASE="$APP_DATA_ROOT/clients/client-$EXPECTED_SHA256"
KEY_DIR="$APP_DATA_ROOT/credentials/client-$EXPECTED_SHA256"
CONFIG_DIR="$APP_CONFIG_ROOT/client-$EXPECTED_SHA256"
test ! -e "$CLIENT_RELEASE"
test ! -e "$KEY_DIR"
test ! -e "$CONFIG_DIR"
printf '%s  %s\n' "$EXPECTED_SHA256" "$ZIP_PATH" | sha256sum -c -
umask 077
mkdir -p "$CLIENT_RELEASE" "$KEY_DIR" "$CONFIG_DIR"
chmod 700 "$KEY_DIR" "$CONFIG_DIR"
unzip -q "$ZIP_PATH" -d "$CLIENT_RELEASE"
CLIENT_ROOT="$CLIENT_RELEASE/client"
uv sync --locked --project "$CLIENT_ROOT"
```

## Windows

Используйте отдельные новые каталоги внутри пользовательского `%LOCALAPPDATA%`. Не применяйте POSIX-режимы `0700`/`0600` и не изменяйте ACL домашнего профиля. До создания файлов ограничьте ACL только текущим SID и `SYSTEM`; `configure-client.py` проверит конечный credential/config file нативным Windows reader.

```powershell
$AppRoot = Join-Path $env:LOCALAPPDATA 'WolframServer'
$KeyDir = Join-Path $AppRoot 'credentials\client-release-id'
$ConfigDir = Join-Path $AppRoot 'config\client-release-id'
New-Item -ItemType Directory -Path $KeyDir
New-Item -ItemType Directory -Path $ConfigDir
$Sid = (whoami /user /fo csv /nh | ConvertFrom-Csv -Header User,Sid).Sid
icacls $KeyDir /inheritance:r /grant:r "*$Sid`:(OI)(CI)F" '*S-1-5-18:(OI)(CI)F'
icacls $ConfigDir /inheritance:r /grant:r "*$Sid`:(OI)(CI)F" '*S-1-5-18:(OI)(CI)F'
```

Это ACL-пример только для новых выделенных каталогов. Не применяйте его рекурсивно к существующей папке профиля или широкому общему каталогу.
