---
id: A-0017
type: decision
title: Суперпроект с сабмодулями; оркестрация в корне, Dockerfile у сервиса
status: approved
created: 2026-09-30
updated: 2026-10-01
---

# Суперпроект с сабмодулями; оркестрация в корне, Dockerfile у сервиса

Принято 2026-07-04. Система состоит из клиента (Expo) и backend (FastAPI) с разными языками и циклами релиза, а документация и оркестрация относятся к обоим. Решено: корневой репозиторий learning — git-суперпроект (docs/, ROADMAP.md, docker-compose.yml, .env.example, .data/), сервисы — сабмодули learningFront и learningBack со своим main и origin, Dockerfile лежит в сабмодуле сервиса. Монорепо с workspaces отвергнуто — смешение Python- и npm-инструментов. Сквозное изменение — три коммита: по одному в каждом сабмодуле и подъём указателей в суперпроекте.

## Журнал

- 2026-09-30 · заведена из docs/inbox/decision-superproject-submodules.md · приложение
- 2026-10-01 · на подтверждение · architect
- 2026-10-01 · подтверждён · architect
