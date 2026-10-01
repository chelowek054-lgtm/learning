---
id: A-0018
type: decision
title: Словари интерфейса — единые источники в реестре и entities, не в экранах
status: approved
created: 2026-09-30
updated: 2026-10-01
---

# Словари интерфейса — единые источники в реестре и entities, не в экранах

Принято 2026-08-25. Названия типов, уровней и причин шагов жили в двух-трёх экранах и разошлись; домен 'ml' был зашит в четырёх экранах. Решено: у каждого словаря один источник — название типа в ActivityTypeDef.title/hint через registry.getActivityTitle, уровни в MASTERY_TARGETS, причины шагов в STEP_REASON, предмет через profile.subject/useSession().subject, оформление только в shared/config/design.ts. Проверяется grep по hex-цветам вне design.ts и ревью; новый экран не заводит свою карту названий.

## Журнал

- 2026-09-30 · заведена из docs/inbox/decision-ui-vocabularies-single-source.md · приложение
- 2026-10-01 · на подтверждение · architect
- 2026-10-01 · подтверждён · architect
