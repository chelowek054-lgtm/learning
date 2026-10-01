---
id: T-0032
type: task
title: Сервер не стартует с dev-секретами в staging/prod
status: done
change: feature
created: 2026-09-30
updated: 2026-10-01
links:
  implements: [R-0020]
  decided_by: [A-0015]
  affects: [M-0003]
---

# Сервер не стартует с dev-секретами в staging/prod

Проверка при старте: dev-значения вида dev-insecure-change-me запрещены в staging/prod — сервер отказывается стартовать.

## Журнал

- 2026-09-30 · заведена из docs/inbox/platform-and-release.md · приложение
- 2026-10-01 · добавлены связи вне приложения: decided_by A-0015 · claude
- 2026-10-01 · готова к работе · claude
- 2026-10-01 · взята в работу · claude
- 2026-10-01 · на проверку · claude
- 2026-10-01 · выполнена · тесты test_config_secrets · claude
