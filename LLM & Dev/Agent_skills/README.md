# Agent Skills — архив

Снимок полезных скиллов и агентских практик из Codex / Cursor (задел под Claude).  
Не живой runtime: копии файлов, не symlink. Обновлять вручную при смене оригиналов.

**Дата волны:** 17.11.2026

## Полки

| Полка | Что лежит |
|---|---|
| `Generic/` | Переносимые практики агента (не привязаны к одному продукту) |
| `Codex/` | Личные + отобранные system skills Codex |
| `Cursor/` | Curated built-ins из `~/.cursor/skills-cursor` (без Hosted-only) |
| `Claude/` | Пока пусто — личных skills не найдено |

В корне каждой продуктовой полки — `SOURCE.md` с путём оригинала.

## Индекс

| Полка | Путь | Зачем |
|---|---|---|
| Generic | `Generic/complex-tasks/AGENTS.md` | Декомпозиция сложных задач, субагенты, эскалация модели, независимая проверка |
| Codex | `Codex/cloud-heavy-runs/` | Тяжёлые прогоны Tabletop / Wolfram → облако |
| Codex | `Codex/wolfram-server-compute/` | Compute через API / MCP / SDK |
| Codex | `Codex/wolfram-server-datasets/` | Типизированные Parquet / native Wolfram |
| Codex | `Codex/wolfram-server-diagnostics/` | Read-only диагностика compute / datasets |
| Codex | `Codex/system/review-agent/` | Defect-first code review |
| Codex | `Codex/system/skill-creator/` | Создание / обновление Codex skill |
| Codex | `Codex/system/skill-installer/` | Установка skills в `$CODEX_HOME/skills` |
| Codex | `Codex/system/openai-docs/` | OpenAI / Codex docs Q&A |
| Cursor | `Cursor/create-skill/` | Авторство Cursor Agent Skills |
| Cursor | `Cursor/create-rule/` | Cursor rules |
| Cursor | `Cursor/create-subagent/` | Кастомные субагенты |
| Cursor | `Cursor/create-hook/` | Cursor hooks |
| Cursor | `Cursor/review/` | Bugbot / Security Review |
| Cursor | `Cursor/review-bugbot/` | Bugbot |
| Cursor | `Cursor/review-security/` | Security Review |
| Cursor | `Cursor/split-to-prs/` | Разбиение работы на PR |
| Cursor | `Cursor/visualize/` | Инлайн-визуализации |
| Cursor | `Cursor/canvas/` | Cursor Canvas |
| Cursor | `Cursor/loop/` | Повтор промпта / skill по интервалу |

## Не вошло (намеренно)

- Codex marketplace / plugins cache (Zoom и пр.)
- Codex `imagegen`
- Cursor Hosted-only: `origin`, `onboard`, `share`, `new-repo`, `statusline`, `update-cli-config`, `update-cursor-settings`, `sdk`, `shell`, `rename-chat`, `automate`, `autopilot`, `agent-sdk-create-agent`, `migrate-to-skills`, `goal`

## Как обновлять

1. Сравнить с живыми путями из `SOURCE.md` полки.
2. Перекопировать каталог скилла целиком (`SKILL.md` + `references/` / `scripts/` / …).
3. Обновить дату в этом README и в соответствующем `SOURCE.md`.
