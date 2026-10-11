---
id: T-0034
type: task
title: 'Переход на EAS: dev-client, сборка, публикация в сторах, OTA'
status: in_review
change: feature
created: 2026-09-30
updated: 2026-10-11
links:
  implements: [R-0020]
  decided_by: [A-0006]
  affects: [M-0003]
---

# Переход на EAS: dev-client, сборка, публикация в сторах, OTA

Переход с Expo Go на dev-client и EAS Build (решение о версии SDK — отдельный ADR); публикация в App Store и Google Play; EAS Update для OTA-доставки JS-исправлений.

## Журнал

- 2026-09-30 · заведена из docs/inbox/platform-and-release.md · приложение
- 2026-10-01 · добавлены связи вне приложения: decided_by A-0006 · claude
- 2026-10-11 · сделано в репозитории (learningFront PR 42): профили EAS с каналами и адресами API-заглушками, expo-updates, runtimeVersion по версии приложения, идентификаторы ru.praxis.app; порядок выпуска — docs/60-operations/release.md. Не сделано, нужны ваши аккаунты: eas init и projectId, учётные записи Apple и Google, ключи FCM/APNs, реальные адреса API, сама сборка и публикация · claude
- 2026-10-11 · повторная проверка 2026-10-11: ЖДЁТ ВНЕШНЕГО: app.json/eas.json валидны, адреса API — заглушки; нужны eas init, аккаунты Apple/Google, FCM/APNs · claude
