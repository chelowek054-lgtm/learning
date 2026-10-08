---
id: S-0005
type: reference
title: 'RouterAI: режимы обработки flex и priority (service tiers)'
status: approved
created: 2026-10-08
updated: 2026-10-08
summary: 'Поле service_tier на уровне запроса меняет цену и скорость без смены модели: flex дешевле и медленнее (строгий, ошибка если недоступен), priority дороже и быстрее (мягко деградирует до default)'
kind: api
source: документация RouterAI
fetched: 2026-10-07
---

# RouterAI: режимы обработки flex и priority (service tiers)

service_tier задаётся на каждый запрос (не на ключ/аккаунт), работает в Chat Completions/Responses/Messages. default — обычная цена и скорость, резервные провайдеры при нехватке мощности. flex — обычно −50% цены, ниже скорость, строгая маршрутизация: если flex-провайдера нет — ошибка без списания денег. priority — выше стандартной цены, максимальная скорость; при нехватке мощности тихо откатывается на default без доплаты. Поддерживают: OpenAI (flex и priority), Google Vertex AI и Google AI Studio (оба), xAI (только priority); модели без поддержки режима обслуживаются стандартно. Фактический применённый режим виден в поле service_tier ответа — для контроля расходов его стоит логировать. Для одного провайдера в списке режим задаётся суффиксом, например "provider": {"order": ["openai/priority"]}.

## Журнал

- 2026-10-08 · заведена из docs/inbox/routerai-service-tiers.md · приложение
- 2026-10-08 · на подтверждение · architect
- 2026-10-08 · подтверждён · architect
