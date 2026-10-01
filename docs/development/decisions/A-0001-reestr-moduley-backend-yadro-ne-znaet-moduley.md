---
id: A-0001
type: decision
title: 'Реестр модулей backend: ядро не знает модулей'
status: approved
created: 2026-09-30
updated: 2026-10-01
---

# Реестр модулей backend: ядро не знает модулей

Принято 2026-09-30. Сверка нашла нарушение независимости ядра: app.py, admin.py, provisioning.py, jobs.py напрямую импортировали модуль knowledge и знали имена languages/ml. Решение: модуль экспортирует объект backend (наследник core.modules.BackendModule) с необязательным контрактом router()/rubrics()/grade_jobs()/provision()/admin_views(); подключённые модули перечислены в конфиге INSTALLED_MODULES, ядро грузит их через importlib. Рубрики сидятся insert-if-absent при старте API; стартовый контент создаётся при сохранении profile.subject, а не при регистрации. Отвергнуты прямые импорты (нарушают NFR-03) и Python entry points (избыточны для монорепо). Проверяется scripts/check-invariants.sh и test_core_does_not_know_modules.

## Журнал

- 2026-09-30 · заведена из docs/inbox/decision-backend-module-registry.md · приложение
- 2026-10-01 · на подтверждение · architect
- 2026-10-01 · подтверждён · architect
