---
id: V-0056
type: verification
title: Освоенность и выбор зонда
status: approved
created: 2026-09-30
updated: 2026-10-01
kind: manual
links:
  verifies: [R-0015]
---

# Освоенность и выбор зонда

Unit, pytest: `cd learningBack && uv run pytest tests/test_mastery.py tests/test_placement.py -q`. Доказывает: приор из предпосылок, бета-обновление, зонд только на границе знаний, остановка с кодом empty/no_theory/settled, карта known/frontier/learning/locked. Пройдена, когда все тесты проходят. Состояние: есть и проходит на 2026-09-30.

## Журнал

- 2026-09-30 · заведена из docs/inbox/checks-placement.md · приложение
- 2026-10-01 · на подтверждение · architect
- 2026-10-01 · подтверждён · architect
- 2026-10-01 · возвращён в черновик · architect
- 2026-10-01 · на подтверждение · architect
- 2026-10-01 · подтверждён · architect
