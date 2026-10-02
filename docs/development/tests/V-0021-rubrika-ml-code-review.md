---
id: V-0021
type: verification
title: Рубрика ml_code_review
status: approved
created: 2026-09-30
updated: 2026-10-02
kind: manual
command: 'cd learningBack && uv run pytest tests/test_code_review.py -k "rubric or prompt" -q'
links:
  verifies: [R-0010, T-0010, T-0011, T-0012, T-0013]
---

# Рубрика ml_code_review

Unit, pytest: `будет: cd learningBack && uv run pytest tests/test_code_review_rubric.py -q`. Доказывает: рубрика v1 есть в реестре, четыре критерия, оценка проходит схему. Пройдена, когда тест написан вместе с T-0010. Состояние: ещё нет — появится вместе с задачей.

## Журнал

- 2026-09-30 · заведена из docs/inbox/checks-code-task.md · приложение
- 2026-10-01 · на подтверждение · architect
- 2026-10-01 · подтверждён · architect
- 2026-10-01 · возвращён в черновик · architect
- 2026-10-01 · на подтверждение · architect
- 2026-10-01 · подтверждён · architect
- 2026-10-02 · подключена команда прогона: test_code_review: рубрика (T-0010) · claude
