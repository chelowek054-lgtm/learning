---
id: T-0105
type: task
title: Расширить next-action.ts на состояния сборки, сбоя и карты без уровня
status: in_review
change: feature
created: 2026-10-07
updated: 2026-10-07
links:
  implements: [R-0057]
  affects: [M-0033]
---

# Расширить next-action.ts на состояния сборки, сбоя и карты без уровня

Добавить в `nextAction` ветки для «карта собирается», «сборка не удалась», «карта готова, уровень неизвестен» перед тем, как по умолчанию предлагать «Определить уровень».

## Журнал

- 2026-10-07 · заведена из docs/inbox/user-flow-as-is-problems.md, docs/inbox/user-flow-daily-loop.md · приложение
- 2026-10-07 · сделана (learningFront PR 34): nextAction знает «собирается», «сбой», «контур», «карты нет», «цель достигнута»; 8 новых тестов · claude
