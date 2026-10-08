---
id: S-0002
type: reference
title: 'RouterAI: плагины (web, file-parser) и мультимодальные входы'
status: approved
created: 2026-10-08
updated: 2026-10-08
summary: Плагины web/file-parser включаются массивом plugins без предварительной настройки; мультимодальные входы (изображения, PDF, аудио, видео) идут через /chat/completions типами контента в messages[].content
kind: api
source: документация RouterAI
fetched: 2026-10-07
---

# RouterAI: плагины (web, file-parser) и мультимодальные входы

Плагины передаются массивом plugins в теле запроса: web (id "web") — дополняет ответ свежими результатами поиска, суффикс модели :online — то же самое; file-parser (id "file-parser") — разбор содержимого загруженных PDF. Мультимодальность — всё на /api/v1/chat/completions: image_url, file (PDF), input_audio, video_url внутри messages[].content, можно смешивать модальности в одном запросе; RouterAI сам отфильтровывает модели без нужной модальности. Подача: URL (для публичного контента) или base64 (для локальных файлов). Отдельные эндпоинты: /api/v1/audio/transcriptions (распознавание речи) и /api/v1/audio/speech (синтез речи, совместим с OpenAI Audio Speech).

## Журнал

- 2026-10-08 · заведена из docs/inbox/routerai-plugins-and-multimodal.md · приложение
- 2026-10-08 · на подтверждение · architect
- 2026-10-08 · подтверждён · architect
