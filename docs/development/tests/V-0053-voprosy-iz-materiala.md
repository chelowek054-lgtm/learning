---
id: V-0053
type: verification
title: Вопросы из материала
status: approved
created: 2026-09-30
updated: 2026-10-02
kind: manual
command: 'cd learningBack && uv run pytest tests/test_material_nodes.py -k "questions" -q'
links:
  verifies: [R-0014, T-0016, T-0025]
---

# Вопросы из материала

Unit, pytest: `будет: cd learningBack && uv run pytest tests/test_recall_from_material.py -q`. Доказывает: из материала порождаются вопросы concept_recall. Пройдена, когда тест написан вместе с T-0016. Состояние: ещё нет — появится вместе с задачей.

## Журнал

- 2026-09-30 · заведена из docs/inbox/checks-ml-track.md · приложение
- 2026-10-01 · на подтверждение · architect
- 2026-10-01 · подтверждён · architect
- 2026-10-01 · возвращён в черновик · architect
- 2026-10-01 · на подтверждение · architect
- 2026-10-01 · подтверждён · architect
- 2026-10-02 · подключена команда прогона: test_material_nodes: вопросы из материала (T-0016) · claude
