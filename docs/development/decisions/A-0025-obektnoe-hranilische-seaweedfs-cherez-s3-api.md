---
id: A-0025
type: decision
title: 'Объектное хранилище: SeaweedFS через S3 API'
status: draft
created: 2026-10-06
updated: 2026-10-06
---

# Объектное хранилище: SeaweedFS через S3 API

Решение: источники (PDF, HTML) хранятся в SeaweedFS; в коде только S3-совместимый клиент, бакеты закрытые, доступ по временным подписанным ссылкам для администраторов.
Почему: MinIO Community больше не развивается (консоль убрана в 2025, образы не публикуются, репозиторий заархивирован в феврале 2026). Garage (AGPL) и Ceph RGW рассмотрены, SeaweedFS проще для одного сервера.

## Журнал

- 2026-10-06 · заведена из docs/inbox/decision-object-storage.md, docs/inbox/decision-knowledge-pipeline-and-graph-db.md · приложение
