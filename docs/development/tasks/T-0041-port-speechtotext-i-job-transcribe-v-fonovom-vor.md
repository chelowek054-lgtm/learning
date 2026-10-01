---
id: T-0041
type: task
title: Порт SpeechToText и job transcribe в фоновом воркере
status: backlog
change: feature
created: 2026-09-30
updated: 2026-09-30
links:
  implements: [R-0023]
  depends_on: [T-0040]
---

# Порт SpeechToText и job transcribe в фоновом воркере

ADR: где STT (API / faster-whisper в контейнере / on-device) и формат аудио. Порт SpeechToText в core/, реализация + MockSTT. Job transcribe в фоновом воркере (синхронная обработка на /sync/push не укладывается в таймаут — нужен ADR о воркере, заменяющий d-jobs-on-push для этого job). Длинная/тихая/пустая запись → понятная ошибка, а не пустая оценка.

## Журнал

- 2026-09-30 · заведена из docs/inbox/speaking.md · приложение
