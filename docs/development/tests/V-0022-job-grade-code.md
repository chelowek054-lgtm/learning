---
id: V-0022
type: verification
title: Job grade_code
status: approved
created: 2026-09-30
updated: 2026-10-02
kind: manual
command: 'cd learningBack && uv run pytest tests/test_code_review.py -k "grade_code or caveat or error_log" -q'
links:
  verifies: [R-0010, T-0010, T-0011, T-0012, T-0013]
---

# Job grade_code

Integration, pytest: `будет: cd learningBack && uv run pytest tests/test_grade_code_job.py -q`. Доказывает: решение оценивается по рубрике, ошибки становятся карточками, в разборе названо ограничение «код не исполнялся». Пройдена, когда тест написан вместе с T-0012. Состояние: ещё нет — появится вместе с задачей.

## Журнал

- 2026-09-30 · заведена из docs/inbox/checks-code-task.md · приложение
- 2026-10-01 · на подтверждение · architect
- 2026-10-01 · подтверждён · architect
- 2026-10-01 · возвращён в черновик · architect
- 2026-10-01 · на подтверждение · architect
- 2026-10-01 · подтверждён · architect
- 2026-10-02 · подключена команда прогона: test_code_review: job grade_code (T-0012) · claude
