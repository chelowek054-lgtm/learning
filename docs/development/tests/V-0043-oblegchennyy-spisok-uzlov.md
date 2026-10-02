---
id: V-0043
type: verification
title: Облегчённый список узлов
status: approved
created: 2026-09-30
updated: 2026-10-02
kind: manual
command: 'cd learningBack && uv run pytest tests/test_graph_nodes.py -k "no_full_theory or node_endpoint" -q'
links:
  verifies: [R-0008, T-0006, T-0007, T-0008]
---

# Облегчённый список узлов

Unit, pytest: `будет: cd learningBack && uv run pytest tests/test_graph_light.py -q`. Доказывает: список без теории отдаёт узлы и рёбра, теория запрашивается по узлу, на графе в 200 узлов ответ заметно меньше прежнего. Пройдена, когда тест и замер размера написаны вместе с T-0008. Состояние: ещё нет — появится вместе с задачей.

## Журнал

- 2026-09-30 · заведена из docs/inbox/checks-knowledge-graph.md · приложение
- 2026-10-01 · на подтверждение · architect
- 2026-10-01 · подтверждён · architect
- 2026-10-01 · возвращён в черновик · architect
- 2026-10-01 · на подтверждение · architect
- 2026-10-01 · подтверждён · architect
- 2026-10-02 · подключена команда прогона: test_graph_nodes: лёгкий список (T-0008) · claude
