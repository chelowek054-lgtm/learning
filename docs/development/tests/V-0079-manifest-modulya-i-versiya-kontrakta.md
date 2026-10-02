---
id: V-0079
type: verification
title: Манифест модуля и версия контракта
status: approved
created: 2026-10-01
updated: 2026-10-02
kind: manual
command: 'cd learningBack && uv run pytest tests/test_module_manifest.py -q && cd ../learningFront && npx vitest run src/shared/engine/module'
links:
  verifies: [R-0027]
---

# Манифест модуля и версия контракта

Вид: unit, запускается pytest, команда будет `cd learningBack && uv run pytest tests/test_module_manifest.py -q`.
Доказывает: ядро отклоняет модуль с несовместимой версией контракта, занятым идентификатором и неразрешённым запросом, с понятной причиной.
Пройдена, когда тест написан вместе с задачей про единый контракт и проходит. Состояние: ещё нет.

## Журнал

- 2026-10-01 · заведена из docs/inbox/platform-checks.md · приложение
- 2026-10-01 · на подтверждение · architect
- 2026-10-01 · подтверждён · architect
- 2026-10-01 · убраны связи неверного типа вне приложения: verifies [C-0001]; covers [T-0051] · claude
- 2026-10-02 · подключена команда прогона: test_module_manifest (сервер) и manifest-check.test (клиент) · claude
