---
id: V-0081
type: verification
title: Модуль запоминания подключается и отключается
status: approved
created: 2026-10-01
updated: 2026-10-02
kind: manual
command: 'cd learningBack && uv run pytest tests/test_memorization_module.py -q'
links:
  verifies: [R-0029]
---

# Модуль запоминания подключается и отключается

Вид: integration, запускается pytest, команда будет `cd learningBack && uv run pytest tests/test_memorization_module.py -q`.
Доказывает: повторение и письмо подключаются по контракту, отключение одного не ломает граф и данные, новый способ добавляется без правки ядра.
Пройдена, когда тест написан вместе с задачей про модули запоминания и проходит. Состояние: ещё нет.

## Журнал

- 2026-10-01 · заведена из docs/inbox/platform-checks.md · приложение
- 2026-10-01 · на подтверждение · architect
- 2026-10-01 · подтверждён · architect
- 2026-10-01 · убраны связи неверного типа вне приложения: covers [T-0053] · claude
- 2026-10-02 · подключена команда прогона: test_memorization_module (контракт способа, отключение, добавление нового способа без правки ядра, свидетельство) · claude
