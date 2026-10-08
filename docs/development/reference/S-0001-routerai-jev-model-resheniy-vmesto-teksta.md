---
id: S-0001
type: reference
title: 'RouterAI Jev: модель решений вместо текста'
status: approved
created: 2026-10-08
updated: 2026-10-08
summary: 'Jev — не чат-модель: получает state и questions с заранее известными вариантами и возвращает вероятности/выбор/оценку вместо текста; тарифицируются только входные токены'
kind: api
source: документация RouterAI, раздел decisions
fetched: 2026-10-07
---

# RouterAI Jev: модель решений вместо текста

Эндпоинт POST https://routerai.ru/api/v1/decisions, модель ~typesafe/jev-latest или закреплённая версия (typesafe/jev-1.13). Тело: model, state, questions — три типа вопросов: noul (да/нет → вероятность), choice (вариант из списка → победитель+probabilities+confidence), score (положение на шкале → score+probabilities+confidence+legend). Быстро (<1с), дёшево (выходные токены бесплатны, ~280 служебных токенов на запрос), ответ всегда из предложенных вариантов, без объяснений. Контекст: 32k на state+вопрос, 64k на state+все вопросы. Подходит для классификации/детекции признака/модерации/роутинга, не для многошагового анализа или генерации текста. Пороги уверенности подбираются на примерах и привязываются к зафиксированной версии модели (поле model в ответе). Есть официальные SDK (@typesafe-ai/sdk, typesafe-sdk) с base_url RouterAI.

## Журнал

- 2026-10-08 · заведена из docs/inbox/routerai-jev-decisions.md · приложение
- 2026-10-08 · на подтверждение · architect
- 2026-10-08 · подтверждён · architect
