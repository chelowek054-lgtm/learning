---
id: V-0061
type: verification
title: Курирование сгенерированных материалов
status: approved
created: 2026-09-30
updated: 2026-10-01
kind: manual
links:
  verifies: [R-0022, T-0036, T-0037, T-0038, T-0039]
---

# Курирование сгенерированных материалов

Unit, pytest: `будет: cd learningBack && uv run pytest tests/test_material_curation.py -q`. Доказывает: материал draft не выдаётся учащемуся, approved выдаётся; повторная генерация того же входа приходит из кэша. Пройдена, когда тест написан вместе с T-0039. Состояние: ещё нет — появится вместе с задачей.

## Журнал

- 2026-09-30 · заведена из docs/inbox/checks-reception-drills.md · приложение
- 2026-10-01 · на подтверждение · architect
- 2026-10-01 · подтверждён · architect
- 2026-10-01 · возвращён в черновик · architect
- 2026-10-01 · на подтверждение · architect
- 2026-10-01 · подтверждён · architect
