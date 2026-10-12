---
id: T-0139
type: task
title: size="sm" у Button и Chip с зоной нажатия 44px
status: in_review
change: feature
created: 2026-10-12
updated: 2026-10-12
links:
  implements: [R-0068]
  depends_on: [D-0003]
  verified_by: [V-0127, V-0123]
  affects: [M-0049]
---

# size="sm" у Button и Chip с зоной нажатия 44px

Клиент получает у Button и Chip параметр size="sm" по спецификации malaya-knopka-design, заменяет локальный NeighborButton в плашке узла схемы пути. Reuse: none — размера sm в общем реестре компонентов пока нет, добавляется этой задачей и D-записью вместе.

## Журнал

- 2026-10-12 · заведена из docs/inbox/malaya-knopka-kompaktnyy-razmer-kontrola.md, docs/inbox/skhema-puti-nedodelki-polnoekrannogo-rezhima.md · приложение
- 2026-10-12 · на проверку: learningFront#54 — size="sm" у Button и Chip с зоной нажатия 44 px (hitSlop), роль цвета tone, NeighborButton переведён на него. НЕ СДЕЛАНО: размер не добавлен в общий реестр компонентов эталона консоли (D-0003 просит добавить сначала туда). Проверки не писались и не проходились (по просьбе, сделать потом); check (tsc, eslint, prettier, 286 тестов) зелёный, на экране и устройстве не смотрели · claude
