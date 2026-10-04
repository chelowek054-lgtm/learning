---
id: T-0040
type: task
title: Запись ответа офлайн и загрузка на backend
status: in_progress
change: feature
created: 2026-09-30
updated: 2026-10-04
links:
  implements: [R-0023]
  affects: [M-0003]
---

# Запись ответа офлайн и загрузка на backend

Клиент (expo-audio): разрешения, старт/стоп, длительность, прослушивание до отправки, перезапись. POST /media/upload (multipart), таблица media, привязка к response, лимиты размера/длительности; запись на устройстве живёт до успешной загрузки, затем удаляется.

## Журнал

- 2026-09-30 · заведена из docs/inbox/speaking.md · приложение
- 2026-10-04 · взята в работу: серверная часть — приём записи POST /languages/speaking/audio (learningBack PR 34); запись на устройстве и отправка не сделаны · claude
