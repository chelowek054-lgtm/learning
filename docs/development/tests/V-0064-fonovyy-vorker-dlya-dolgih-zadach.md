---
id: V-0064
type: verification
title: Фоновый воркер для долгих задач
status: approved
created: 2026-09-30
updated: 2026-10-01
kind: manual
links:
  verifies: [R-0023, T-0040, T-0041, T-0042, T-0043, T-0044, T-0049]
---

# Фоновый воркер для долгих задач

Integration, pytest: `будет: cd learningBack && uv run pytest tests/test_worker.py -q`. Доказывает: долгая задача исполняется вне запроса /sync/push и доходит до done. Пройдена, когда тест написан вместе с T-0049. Состояние: ещё нет — появится вместе с задачей.

## Журнал

- 2026-09-30 · заведена из docs/inbox/checks-speaking.md · приложение
- 2026-10-01 · на подтверждение · architect
- 2026-10-01 · подтверждён · architect
- 2026-10-01 · возвращён в черновик · architect
- 2026-10-01 · на подтверждение · architect
- 2026-10-01 · подтверждён · architect
