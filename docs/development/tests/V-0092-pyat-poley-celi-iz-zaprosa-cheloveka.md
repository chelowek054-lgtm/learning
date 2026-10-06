---
id: V-0092
type: verification
title: Пять полей цели из запроса человека
status: draft
created: 2026-10-06
updated: 2026-10-06
kind: manual
links:
  verifies: [R-0041]
---

# Пять полей цели из запроса человека

Чем проверяется: из свободного запроса извлекаются область, уровень, зачем, что уже знает и ограничения; пустое — явное «не указано»; подтверждённая цель хранит поля структурно; без сети работает прямая форма с теми же полями.
Команда: `cd learningBack && uv run pytest tests/test_goal_intake.py -q && cd ../learningFront && npx vitest run src/features/goal-intake`

## Журнал

- 2026-10-06 · заведена · приложение
