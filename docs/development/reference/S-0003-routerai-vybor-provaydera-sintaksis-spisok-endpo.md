---
id: S-0003
type: reference
title: 'RouterAI: выбор провайдера, @-синтаксис, список endpoint-ов'
status: approved
created: 2026-10-08
updated: 2026-10-08
summary: Объект provider (order/only/ignore/allow_fallbacks/country) и @-синтаксис в строке model управляют маршрутизацией запроса к конкретному провайдеру модели; GET /models/{author}/{model}/endpoints отдаёт список провайдеров с ценами и лимитами
kind: api
source: документация RouterAI
fetched: 2026-10-07
---

# RouterAI: выбор провайдера, @-синтаксис, список endpoint-ов

По умолчанию RouterAI балансирует между провайдерами модели (без недавних сбоев → самый дешёвый → резерв). Поле provider в теле запроса: order (предпочтение), only (белый список, иначе 404), ignore (чёрный список), allow_fallbacks (для order, по умолчанию true), country (жёсткий фильтр по стране серверов). @-синтаксис в строке model (<model>@provider=...&allow_fallbacks=...) — только для /v1/chat/completions, /v1/responses, /v1/messages. GET https://routerai.ru/api/v1/models/{author}/{model}/endpoints (без авторизации) отдаёт tag, provider_name, context_length, pricing, pricing_units, status и порядок приоритета маршрутизации. Тарификация — по фактическому провайдеру, при ошибке деньги не списываются.

## Журнал

- 2026-10-08 · заведена из docs/inbox/routerai-provider-routing.md · приложение
- 2026-10-08 · на подтверждение · architect
- 2026-10-08 · подтверждён · architect
