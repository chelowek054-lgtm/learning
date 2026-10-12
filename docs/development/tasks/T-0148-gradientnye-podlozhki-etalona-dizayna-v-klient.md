---
id: T-0148
type: task
title: Градиентные подложки эталона дизайна в клиент
status: in_review
change: feature
created: 2026-10-12
updated: 2026-10-12
links:
  implements: [R-0067]
  verified_by: [V-0123]
  affects: [M-0049]
---

# Градиентные подложки эталона дизайна в клиент

Градиентные подложки из эталона дизайн-системы (эталон консоли) не перенесены в клиент — схема пути выглядит плоской против макета Claude Design.

## Журнал

- 2026-10-12 · заведена из docs/inbox/skhema-puti-nedodelki-polnoekrannogo-rezhima.md · приложение
- 2026-10-12 · на проверку: learningFront#54 — подложка страницы backdrop.page из D-0002 (два радиальных пятна ролями accent и core) в Screen; в OLED и контрастной темах её нет. На нативных платформах через experimental_backgroundImage — не проверено, что он работает. Проверки не писались и не проходились (по просьбе, сделать потом); check (tsc, eslint, prettier, 286 тестов) зелёный, на экране и устройстве не смотрели · claude
