---
id: V-0006
type: verification
title: Панель /admin и createsuperuser вручную
status: approved
created: 2026-09-30
updated: 2026-10-01
kind: manual
links:
  verifies: [R-0003, T-0001]
---

# Панель /admin и createsuperuser вручную

Manual. Доказывает: не-админ не входит в /admin, снятие флага закрывает доступ той же сессии, createsuperuser создаёт, повторяет и повышает пользователя. Пройдена, когда пройдена руками по шагам и результат записан в журнал (последний раз вживую — 2026-08-23). Открытый вопрос: нужна ли автоматическая проверка входа в /admin по cookie-сессии.

## Журнал

- 2026-09-30 · заведена из docs/inbox/checks-admin-and-curation.md · приложение
- 2026-10-01 · на подтверждение · architect
- 2026-10-01 · подтверждён · architect
- 2026-10-01 · возвращён в черновик · architect
- 2026-10-01 · на подтверждение · architect
- 2026-10-01 · подтверждён · architect
