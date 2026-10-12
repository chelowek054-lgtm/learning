---
id: T-0021
type: task
title: Защита ветки main во всех трёх репозиториях
status: done
change: feature
reuse: none
created: 2026-09-30
updated: 2026-10-11
links:
  implements: [R-0016]
  decided_by: [A-0017]
  affects: [M-0003, M-0011]
---

# Защита ветки main во всех трёх репозиториях

Настройка GitHub (не код): merge только при зелёном CI, во всех трёх репозиториях (learning, learningFront, learningBack).

## Журнал

- 2026-09-30 · заведена из docs/inbox/platform-and-release.md · приложение
- 2026-10-01 · добавлены связи вне приложения: decided_by A-0017 · claude
- 2026-10-03 · на проверку: защита main включена в learning, learningBack, learningFront (обязательная проверка CI «check», принудительный push и удаление ветки запрещены; администратор не ограничен — прямые коммиты документов в суперпроект возможны); проба — PR с красным тестом в learningBack получил состояние BLOCKED и закрыт без слияния; V-0020 не подтверждена человеком · claude
- 2026-10-04 · связь с картой M-0011: она объявляет возможность, которую меняет задача (сверка map_capability_missing) · claude
- 2026-10-11 · повторная проверка 2026-10-11: ПРОШЛА: защита main во всех трёх репозиториях (check обязателен, force-push и удаление запрещены); красный PR пробовали только в learningBack · claude
