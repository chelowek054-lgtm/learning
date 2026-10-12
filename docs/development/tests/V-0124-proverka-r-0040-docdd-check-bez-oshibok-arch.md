---
id: V-0124
type: verification
title: 'Проверка R-0040: docdd check без ошибок arch_*'
status: draft
created: 2026-10-12
updated: 2026-10-12
kind: manual
links:
  verifies: [R-0040]
---

# Проверка R-0040: docdd check без ошибок arch_*

Зачем: требование R-0040 («Починить нарушения архитектуры: 50») подтверждено, но ничем не проверяется — предупреждение консоли.
Проверка: прогон `docdd check` по всему проекту не возвращает ни одной ошибки с кодом `arch_*`.

## Журнал

- 2026-10-12 · заведена из docs/inbox/ostatok-svedeniy-konsoli-posle-ochistki.md · приложение
