---
id: V-0080
type: verification
title: Граф без предметов
status: approved
created: 2026-10-01
updated: 2026-10-02
kind: manual
command: 'cd learningBack && uv run pytest tests/test_graph_subject_agnostic.py tests/test_graph_interface.py -q && cd .. && bash scripts/check-invariants.sh'
links:
  verifies: [R-0028]
---

# Граф без предметов

Вид: integration, запускается pytest, команда будет `cd learningBack && uv run pytest tests/test_graph_subject_agnostic.py -q`.
Доказывает: один и тот же код графа строит область и ведёт курс для трёх предметов разной природы (технический, языковой, произвольный), без проверок по названию предмета.
Пройдена, когда тест написан вместе с задачей про граф без предметов и проходит. Состояние: ещё нет.

## Журнал

- 2026-10-01 · заведена из docs/inbox/platform-checks.md · приложение
- 2026-10-01 · на подтверждение · architect
- 2026-10-01 · подтверждён · architect
- 2026-10-01 · убраны связи неверного типа вне приложения: covers [T-0052] · claude
- 2026-10-02 · подключена команда прогона: test_graph_subject_agnostic (три предмета, плоская языковая область, нет предметных слов в коде) и test_graph_interface · claude
