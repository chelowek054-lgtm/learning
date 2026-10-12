---
id: V-0122
type: verification
title: Параллельные прогоны backend-тестов не делят тестовую базу
status: approved
created: 2026-10-12
updated: 2026-10-12
kind: manual
links:
  verifies: [T-0125]
---

# Параллельные прогоны backend-тестов не делят тестовую базу

Чем проверяется: два и более параллельных запуска тестового набора backend проходят без IntegrityError и без «relation does not exist», вызванных общей тестовой базой.

## Журнал

- 2026-10-12 · заведена из docs/inbox/zhivye-proverki-model-ne-vyzyvaet-instrument.md · приложение
- 2026-10-12 · на подтверждение · architect
- 2026-10-12 · подтверждён · architect
- 2026-10-12 · проверена вручную · architect
- 2026-10-12 · отметка «проверено» снята · architect
