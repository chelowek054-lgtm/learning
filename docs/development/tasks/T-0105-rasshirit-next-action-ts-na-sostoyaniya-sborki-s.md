---
id: T-0105
type: task
title: Расширить next-action.ts на состояния сборки, сбоя и карты без уровня
status: in_progress
change: feature
created: 2026-10-07
updated: 2026-10-11
links:
  implements: [R-0057]
  affects: [M-0033]
---

# Расширить next-action.ts на состояния сборки, сбоя и карты без уровня

Добавить в `nextAction` ветки для «карта собирается», «сборка не удалась», «карта готова, уровень неизвестен» перед тем, как по умолчанию предлагать «Определить уровень».

## Журнал

- 2026-10-07 · заведена из docs/inbox/user-flow-as-is-problems.md, docs/inbox/user-flow-daily-loop.md · приложение
- 2026-10-07 · сделана (learningFront PR 34): nextAction знает «собирается», «сбой», «контур», «карты нет», «цель достигнута»; 8 новых тестов · claude
- 2026-10-11 · ВОЗВРАЩЕНА по проверке 2026-10-11 (vitest 13 тестов зелёные): (1) нет состояний «цель ставится» и «пауза» ни в nextAction, ни в тестах, хотя R-0057 и V-0108 требуют кейс на каждое; в журнале об этом не сказано. (2) вход {hasSubject:true, course:null, dueCount:0, build:null, graphSize:null} → placement (next-action.ts:99); ожидалось не «Определить уровень» при неизвестном состоянии (так будет при ошибке getGraph/getProfile). (3) вход {build:{status:'failed'}, course:{current:шаг}, dueCount:5, graphSize:32} → failed, курс и повторение скрыты (next-action.ts:70); то же для outline (:77); приоритет не обоснован. (4) вход {graphSize:0, course:{current:шаг}} → build, а не course (:81). (5) updatedAt с мусорной строкой → minutes NaN (:63-66). tsc: 6 ошибок типов маршрутов /path,/library,/curator — нужно перегенерировать типы · claude
