---
id: T-0039
type: task
title: Генерация passage/вопросов, озвучка и курирование материалов
status: done
change: feature
created: 2026-09-30
updated: 2026-10-04
links:
  implements: [R-0022]
  verified_by: [V-0061]
  affects: [M-0003, M-0011]
---

# Генерация passage/вопросов, озвучка и курирование материалов

Passage + вопросы с дистракторами через AIGateway.structured; озвучка через порт TextToSpeech; материал в статусе draft с confidence до подтверждения администратором; учащимся выдаются только approved.

## Журнал

- 2026-09-30 · заведена из docs/inbox/reception-drills.md · приложение
- 2026-10-04 · взята в работу, сделана: генерация passage/вопросов через structured, порт TextToSpeech с заглушкой, материал draft с confidence, выдача только approved и без текста (learningBack PR 32) · claude
- 2026-10-04 · на проверку: тесты проходят; настоящий провайдер озвучки не подключён (нужен TTS_MODEL и ключ), экрана куратора в клиенте нет — только API · claude
- 2026-10-04 · готова · проверки подтверждены и прошли в отчёте 2026-10-04 · claude
