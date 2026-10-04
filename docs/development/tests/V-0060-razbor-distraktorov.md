---
id: V-0060
type: verification
title: Разбор дистракторов
status: approved
created: 2026-09-30
updated: 2026-10-01
kind: manual
command: 'cd learningBack && uv run pytest tests/test_explain_distractors.py -q && cd ../learningFront && npx vitest run src/features/reading-drill'
links:
  verifies: [R-0022, T-0036, T-0037, T-0038, T-0039]
---

# Разбор дистракторов

Integration, pytest: `будет: cd learningBack && uv run pytest tests/test_explain_distractors.py -q`. Доказывает: job explain_distractors приходит при сети и не блокирует прохождение. Пройдена, когда тест написан вместе с T-0038. Состояние: ещё нет — появится вместе с задачей.

## Журнал

- 2026-09-30 · заведена из docs/inbox/checks-reception-drills.md · приложение
- 2026-10-01 · на подтверждение · architect
- 2026-10-01 · подтверждён · architect
- 2026-10-01 · возвращён в черновик · architect
- 2026-10-01 · на подтверждение · architect
- 2026-10-01 · подтверждён · architect
- 2026-10-04 · подключена команда прогона: test_explain_distractors (разбор по неверным вариантам, запасной разбор без модели, чужой вход отклонён) и reading-model.test (job ставится только на ошибки с выбором) · claude
