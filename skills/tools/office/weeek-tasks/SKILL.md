---
name: ops-pm-weeek-tasks
description: "WEEEK Task Management via Public API. Manage tasks, boards, columns, and projects programmatically."
tags:
  - weeek
  - task-management
  - api
  - pm
version: 1.0.0
---

# WEEEK задачи

## Быстрый старт

1. Установить переменные окружения:
   - `WEEEK_TOKEN` — токен авторизации
   - `WEEEK_USER_ID` — ваш ID в WEEEK (опционально)
2. Использовать `scripts/weeek_api.py` для операций.
3. Для справки по эндпоинтам читать `references/api.md`.

## Скрипт

### Получить задачи

```bash
python scripts/weeek_api.py list-tasks --day DD.MM.YYYY --board-id ID_доски --board-column-id ID_колонки
```

### Создать задачу

```bash
python scripts/weeek_api.py create-task --title \"Задача\" --day DD.MM.YYYY --no-locations
```

Если нужна привязка к проекту/доске — передать `project_id/board_id/board_column_id` или JSON:

```bash
python scripts/weeek_api.py create-task --title \"Задача\" --locations-json '[{\"boardId\":ID_доски,\"boardColumnId\":ID_колонки}]'
```

### Обновить задачу

```bash
python scripts/weeek_api.py update-task ID_задачи --title \"Новый заголовок\" --priority 2
```

### Завершить / вернуть

```bash
python scripts/weeek_api.py complete-task ID_задачи
python scripts/weeek_api.py uncomplete-task ID_задачи
```

### Переместить

```bash
python scripts/weeek_api.py move-board ID_задачи --board-id ID_доски
python scripts/weeek_api.py move-board-column ID_задачи --board-column-id ID_колонки
```

### Списки проектов/досок/колонок

```bash
python scripts/weeek_api.py list-projects
python scripts/weeek_api.py list-boards --project-id ID_проекта
python scripts/weeek_api.py list-board-columns --board-id ID_доски
```

ID можно получить через `list-projects`, `list-boards`, `list-board-columns`.

## Ограничения e вопросы

- Формат `day` в docs указан как `string`; точный формат подтвердить у пользователя.
- По умолчанию создаются «датные» задачи без привязки к проектам/доскам (`--no-locations`).
- Если задан `WEEEK_USER_ID`, он автоматически ставится в `userId` e `assignees` при создании.
