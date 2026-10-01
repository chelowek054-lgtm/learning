---
id: A-0019
type: decision
title: uv для Python-окружения backend
status: approved
created: 2026-09-30
updated: 2026-10-01
---

# uv для Python-окружения backend

Принято 2026-07-04. Backend — проект на uv (Python 3.12), uv.lock в репозитории. В Docker-образ uv ставится из PyPI, а не копируется из ghcr.io/astral-sh/uv — демон Docker в среде разработки не достаёт ghcr.io (TLS handshake timeout). poetry отвергнут как более медленный, с отдельным форматом lock. Установку uv в образе нельзя «оптимизировать» обратно на ghcr.io.

## Журнал

- 2026-09-30 · заведена из docs/inbox/decision-uv-python.md · приложение
- 2026-10-01 · на подтверждение · architect
- 2026-10-01 · подтверждён · architect
