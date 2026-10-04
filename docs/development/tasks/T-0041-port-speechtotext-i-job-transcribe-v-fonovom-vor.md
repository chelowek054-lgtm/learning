---
id: T-0041
type: task
title: Порт SpeechToText и job transcribe в фоновом воркере
status: done
change: feature
created: 2026-09-30
updated: 2026-10-04
links:
  implements: [R-0023]
  decided_by: [A-0007]
  depends_on: [T-0040]
  verified_by: [V-0062]
  affects: [M-0003, M-0011]
---

# Порт SpeechToText и job transcribe в фоновом воркере

ADR: где STT (API / faster-whisper в контейнере / on-device) и формат аудио. Порт SpeechToText в core/, реализация + MockSTT. Job transcribe в фоновом воркере (синхронная обработка на /sync/push не укладывается в таймаут — нужен ADR о воркере, заменяющий d-jobs-on-push для этого job). Длинная/тихая/пустая запись → понятная ошибка, а не пустая оценка.

## Журнал

- 2026-09-30 · заведена из docs/inbox/speaking.md · приложение
- 2026-10-01 · добавлены связи вне приложения: decided_by A-0007 · claude
- 2026-10-04 · взята в работу, сделана: порт SpeechToText с заглушкой, job transcribe через хук job_handlers, понятные ошибки; запись удаляется после расшифровки (learningBack PR 34) · claude
- 2026-10-04 · на проверку: тесты проходят; настоящий провайдер STT не подключён (нужны STT_MODEL и ключ) · claude
- 2026-10-04 · готова · проверки подтверждены и прошли в отчёте 2026-10-04 · claude
