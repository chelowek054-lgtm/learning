---
id: V-0095
type: verification
title: Статус черновика, уведомления о курсе и push
status: draft
created: 2026-10-06
updated: 2026-10-06
kind: manual
links:
  verifies: [R-0044]
---

# Статус черновика, уведомления о курсе и push

Чем проверяется: у понятия и связи статус черновик / проверено / отклонено, учащийся видит его простыми словами; уведомления «курс готов», «курс дополнен», «понятие проверено», «правка изменила смысл» копятся и не дублируются; push уходит только согласившимся, с общим текстом, сбой канала не ломает курс.
Команда: `cd learningBack && uv run pytest tests/test_provenance.py tests/test_notifications.py tests/test_notifications_review.py tests/test_push.py -q && cd ../learningFront && npx vitest run src/features/course src/features/push-settings`

## Журнал

- 2026-10-06 · заведена · приложение
