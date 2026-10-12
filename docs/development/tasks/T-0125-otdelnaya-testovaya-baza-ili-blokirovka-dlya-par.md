---
id: T-0125
type: task
title: Отдельная тестовая база или блокировка для параллельных прогонов backend-тестов
status: in_progress
change: fix
created: 2026-10-12
updated: 2026-10-12
links:
  implements: [R-0016]
  verified_by: [V-0122]
---

# Отдельная тестовая база или блокировка для параллельных прогонов backend-тестов

Побочное наблюдение из того же прогона: параллельные запуски тестов backend делят одну тестовую базу (см. `learningBack/tests/conftest.py`, где тестовая БД пересоздаётся на сессию) и дают ложные падения — IntegrityError, relation does not exist.

Что сделать: выделить отдельную тестовую базу на запуск или добавить блокировку в conftest, чтобы параллельные прогоны не конфликтовали.

Готово, когда: параллельные прогоны pytest backend не дают ложных IntegrityError/«relation does not exist» (см. verification).

## Журнал

- 2026-10-12 · заведена из docs/inbox/zhivye-proverki-model-ne-vyzyvaet-instrument.md · приложение
- 2026-10-12 · взята в работу и сделана в коде: learningBack#75: база, scratch-база проверки миграций и бакет бэкапа получают имя на запуск, тестовая база удаляется в конце; два одновременных pytest проходят без ложных падений (локально). PR не влит: CI learningBack красный и до этого PR (нет vector и AGE в образе postgres:16) · claude
