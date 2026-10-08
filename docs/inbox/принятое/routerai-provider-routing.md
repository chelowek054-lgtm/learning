# RouterAI: выбор провайдера, @-синтаксис, список endpoint-ов (справка провайдера)

Источник: документация RouterAI (получена от человека 2026-10-07).

## Балансировка по умолчанию

RouterAI распределяет нагрузку между провайдерами модели: сперва те, у кого не было значительных сбоев за
последние 30 секунд; среди них — самые дешёвые; остальные — резерв (fallbacks).

## Объект `provider` в теле запроса

| Поле | Тип | По умолчанию | Смысл |
|---|---|---|---|
| `order` | `string[]` | — | Предпочтение: первый из списка, кто обслуживает модель и не отсеян `only`/`ignore` |
| `only` | `string[]` | — | Белый список; если никого нет — ошибка `404` |
| `ignore` | `string[]` | — | Чёрный список; если исключены все — `404` |
| `allow_fallbacks` | `bool` | `true` | Относится только к `order`: если из списка никого нет, `true` — другой допустимый провайдер, `false` — `404` |
| `country` | `string` | — | Код страны серверов (`"ru"`); жёсткий фильтр, соблюдается и при резервных попытках |

Идентификаторы провайдеров — в нижнем регистре (`openai`, `anthropic`, `google`, `deepseek`, ...); значение —
поле `tag` в списке endpoint-ов. Порядок применения: `only`/`ignore` отсеивают → `order` выбирает → при отсутствии
`order`-кандидатов решает `allow_fallbacks`. Пример: `{"order":["amazon-bedrock"],"only":["google-vertex"]}` уйдёт
в `google-vertex`. Важно: `order/only/ignore` определяют выбор, но при резервной попытке после сбоя запрос может
уйти провайдеру вне списка; жёстко — только `country`.

## @-синтаксис в строке `model`

`<model>@<key>=<value>&<key>=<value>`; параметры: `provider` (эквивалент `provider.only` с одним значением),
`allow_fallbacks` (`true`/`false`). Примеры: `anthropic/claude-opus-5@provider=amazon-bedrock`,
`deepseek/deepseek-v4-pro-0813@provider=deepinfra&allow_fallbacks=false`. Работает только на `/v1/chat/completions`,
`/v1/responses`, `/v1/messages` (не embeddings, audio, media). Тот же параметр одновременно в строке и в теле —
ошибка `400`; неизвестный или повторяющийся параметр — `400`. Сложные случаи (`order`, `ignore`, `country`) — только
объектом `provider`.

## Список endpoint-ов модели

`GET https://routerai.ru/api/v1/models/{author}/{model}/endpoints` (без авторизации). Для каждого endpoint-а:
`tag`, `provider_name`, `name`, `countries` (и `country` для совместимости), `context_length`,
`max_completion_tokens`, `max_prompt_tokens`, `quantization`, `supported_parameters`, `supported_apis`
(`chat`, `messages`, `responses`, `embeddings`, ...), `status` (0 — штатно, отрицательное — временно
деприоритизирован), `pricing` (в рублях, у конкретного провайдера), `pricing_units` (`token`, `request`, `image`,
`megapixel`, `second`, `search_unit`), `variable_pricings` (пороги по токенам промпта). Единицы одного и того же
ключа цены у разных моделей могут отличаться — сверяться с `pricing_units`. Порядок endpoint-ов — приоритет
маршрутизации (первый выбирается по умолчанию).

## Тарификация и ошибки

Стоимость считается по фактическому провайдеру; один запрос через разных провайдеров стоит по-разному; при
ошибке средства не списываются. Ошибки: `404` (`only`/`ignore` отсеяли всех или нет провайдера из `order` при
`allow_fallbacks:false`), `503` (нет доступного провайдера), `402` (недостаточно средств), `500/502/503` (сбой
провайдера после исчерпания резерва).
