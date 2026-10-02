---
id: V-0005
type: verification
title: Промоция персонального узла в канон
status: approved
created: 2026-09-30
updated: 2026-10-02
kind: manual
command: 'cd learningBack && uv run pytest tests/test_promotion.py -q'
links:
  verifies: [R-0003, T-0001]
---

# Промоция персонального узла в канон

Unit, pytest: `будет: cd learningBack && uv run pytest tests/test_promotion.py -q`. Доказывает: промоция создаёт канонический узел с версией, у автора снимается оверрайд, остальные видят новый канонический узел. Пройдена, когда тест написан вместе с T-0001 и проходит. Состояние: ещё нет — появится вместе с задачей.

## Журнал

- 2026-09-30 · заведена из docs/inbox/checks-admin-and-curation.md · приложение
- 2026-10-01 · на подтверждение · architect
- 2026-10-01 · подтверждён · architect
- 2026-10-01 · возвращён в черновик · architect
- 2026-10-01 · на подтверждение · architect
- 2026-10-01 · подтверждён · architect
- 2026-10-02 · подключена команда прогона: test_promotion (T-0001) · claude
