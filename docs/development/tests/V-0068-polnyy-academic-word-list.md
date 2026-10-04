---
id: V-0068
type: verification
title: Полный Academic Word List
status: approved
created: 2026-09-30
updated: 2026-10-01
kind: manual
command: 'cd learningBack && uv run pytest tests/test_awl.py -q'
links:
  verifies: [R-0024, T-0004, T-0026, T-0045]
---

# Полный Academic Word List

Unit, pytest: `будет: cd learningBack && uv run pytest tests/test_awl.py -q`. Доказывает: колода содержит полный список, а не демо-выборку из десяти слов. Пройдена, когда тест написан вместе с T-0045. Состояние: ещё нет — появится вместе с задачей.

## Журнал

- 2026-09-30 · заведена из docs/inbox/checks-srs-and-error-log.md · приложение
- 2026-10-01 · на подтверждение · architect
- 2026-10-01 · подтверждён · architect
- 2026-10-01 · возвращён в черновик · architect
- 2026-10-01 · на подтверждение · architect
- 2026-10-01 · подтверждён · architect
- 2026-10-04 · подключена команда прогона: test_awl (570 слов, 60 семейств в подсписках 1–9 и 30 в десятом, у каждой карточки пояснение и подсписок, первый подсписок к повторению сразу, остальные позже); состав слов сверен с официальным документом Coxhead · claude
