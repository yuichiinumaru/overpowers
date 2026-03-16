---
name: growth-biz-ads-google-ads-manager
description: "Manage Google Ads campaigns. View statistics, adjust budgets, and enable/disable campaigns via the Google Ads API."
tags: ["google-ads", "marketing", "ads", "growth", "automation"]
version: 1.0.0
---

# Google Ads Manager

Инструмент для управления контекстной рекламой Google.

## Возможности
1. **Мониторинг**: Получение списка кампаний и их текущих метрик (показы, клики, CTR, затраты).
2. **Управление**: Изменение статуса кампаний (ENABLE, PAUSED) и обновление дневных бюджетов.
3. **Отчеты**: Генерация базовых отчетов за определенный период.

## Настройка
Для работы требуются учетные данные в файле `google-ads.yaml` или переменные окружения.
Файл конфигурации должен находиться по пути: `~/.google-ads.yaml` или в корне проекта.

## Использование скриптов
Основной интерфейс взаимодействия реализован через Python-скрипт `scripts/google_ads_tool.py`.

### Примеры команд
- Список кампаний: `python3 scripts/google_ads_tool.py list`
- Изменение бюджета: `python3 scripts/google_ads_tool.py update-budget --id <ID> --amount <VALUE>`
- Остановка кампании: `python3 scripts/google_ads_tool.py update-status --id <ID> --status PAUSED`

## Инструкции для агента
При получении запроса на работу с рекламой:
1. Проверьте наличие конфигурационного файла.
2. Используйте `google_ads_tool.py` для выполнения соответствующего действия.
3. Всегда подтверждайте критические изменения (изменение бюджета, остановка кампаний) перед выполнением, если пользователь не указал иное.
