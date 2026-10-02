---
id: V-0042
type: verification
title: Устойчивый ключ узла
status: approved
created: 2026-09-30
updated: 2026-10-02
kind: manual
command: 'cd learningBack && uv run pytest tests/test_graph_nodes.py -k "rename or new_key or key or edges_follow or other_domain" -q'
links:
  verifies: [R-0008, T-0006, T-0007, T-0008]
---

# Устойчивый ключ узла

Unit, pytest: `будет: cd learningBack && uv run pytest tests/test_node_key.py -q`. Доказывает: перегенерация, где модель переименовала узел, не создаёт дубль. Пройдена, когда тест написан вместе с T-0007 и проходит. Состояние: ещё нет — появится вместе с задачей.

## Журнал

- 2026-09-30 · заведена из docs/inbox/checks-knowledge-graph.md · приложение
- 2026-10-01 · на подтверждение · architect
- 2026-10-01 · подтверждён · architect
- 2026-10-01 · возвращён в черновик · architect
- 2026-10-01 · на подтверждение · architect
- 2026-10-01 · подтверждён · architect
- 2026-10-02 · подключена команда прогона: test_graph_nodes: устойчивый ключ (T-0007) · claude
