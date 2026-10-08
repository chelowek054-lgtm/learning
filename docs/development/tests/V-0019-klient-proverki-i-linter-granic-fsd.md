---
id: V-0019
type: verification
title: 'Клиент: проверки и линтер границ FSD'
status: approved
created: 2026-09-30
updated: 2026-10-07
kind: manual
links:
  verifies: [R-0016, T-0021, T-0022]
---

# Клиент: проверки и линтер границ FSD

Integration, npm: `cd learningFront && npm run check`. Доказывает: typecheck, lint, format и тесты проходят; после T-0022 в проверку входит линтер границ слоёв — импорт вверх даёт ошибку. Пройдена, когда команда завершается с кодом 0. Состояние: есть и проходит на 2026-09-30.

## Журнал

- 2026-09-30 · заведена из docs/inbox/checks-ci-and-branch-protection.md · приложение
- 2026-10-01 · на подтверждение · architect
- 2026-10-01 · подтверждён · architect
- 2026-10-01 · возвращён в черновик · architect
- 2026-10-01 · на подтверждение · architect
- 2026-10-01 · подтверждён · architect
- 2026-10-06 · в отчёте 2026-10-06 упала: в основном рабочем каталоге не была установлена новая зависимость expo-notifications (ошибка typecheck); после npm install полный npm run check проходит (typecheck, lint, format, 190 тестов); перепрогнать отдельно · claude
- 2026-10-07 · перепрогнана руками: `cd learningFront && npm run check` — код 0, typecheck и lint без ошибок (4 предупреждения import/no-duplicates), format без замечаний, 201 тест пройден; отчёт 2026-10-07-local.json ещё хранит старое `failed` — это снимок окружения без зависимости, автоматическим прогоном не перезаписан · claude
