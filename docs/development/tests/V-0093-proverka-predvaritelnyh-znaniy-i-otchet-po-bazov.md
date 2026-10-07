---
id: V-0093
type: verification
title: Проверка предварительных знаний и отчёт по базовым областям
status: approved
created: 2026-10-06
updated: 2026-10-07
kind: manual
links:
  verifies: [R-0042]
---

# Проверка предварительных знаний и отчёт по базовым областям

Чем проверяется: тест идёт по цепочке сверху вниз, освоенное верхнее снимает нижнее, по итогам области получают вердикт хватает / мало / нет / не проверено / нет в графе; тест можно пропустить, курс тогда строится как для новичка.
Команда: `cd learningBack && uv run pytest tests/test_chain_placement.py tests/test_prior_report.py -q && cd ../learningFront && npx vitest run src/features/prior-test`

## Журнал

- 2026-10-06 · заведена · приложение
- 2026-10-07 · на подтверждение · architect
- 2026-10-07 · подтверждён · architect
