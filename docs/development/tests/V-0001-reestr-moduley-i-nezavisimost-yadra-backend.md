---
id: V-0001
type: verification
title: Реестр модулей и независимость ядра backend
status: approved
created: 2026-09-30
updated: 2026-10-01
kind: manual
links:
  verifies: [R-0002]
---

# Реестр модулей и независимость ядра backend

Unit, pytest: `cd learningBack && uv run pytest tests/test_modules.py -q`. Доказывает: модули грузятся из INSTALLED_MODULES, дубль модуля и дубль типа job отклоняются, роутеры смонтированы, ядро не импортирует modules.* и не называет модули. Пройдена, когда все тесты файла зелёные. Состояние: есть и проходит на 2026-09-30.

## Журнал

- 2026-09-30 · заведена из docs/inbox/checks-activity-engine.md · приложение
- 2026-10-01 · на подтверждение · architect
- 2026-10-01 · подтверждён · architect
- 2026-10-01 · возвращён в черновик · architect
- 2026-10-01 · на подтверждение · architect
- 2026-10-01 · подтверждён · architect
- 2026-10-01 · возвращён в черновик · architect
- 2026-10-01 · на подтверждение · architect
- 2026-10-01 · подтверждён · architect
