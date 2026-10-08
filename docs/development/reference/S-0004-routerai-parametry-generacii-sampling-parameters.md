---
id: S-0004
type: reference
title: 'RouterAI: параметры генерации (sampling parameters)'
status: approved
created: 2026-10-08
updated: 2026-10-08
summary: RouterAI принимает единый набор параметров генерации (temperature, top_p, top_k, penalties, max_tokens, response_format, tools, verbosity и др.) и передаёт провайдер-специфичные как есть
kind: api
source: документация RouterAI
fetched: 2026-10-07
---

# RouterAI: параметры генерации (sampling parameters)

Таблица параметров запроса и их диапазонов/умолчаний: temperature (0–2, default 1), top_p, top_k, frequency_penalty, presence_penalty, repetition_penalty, min_p, top_a, seed, max_tokens/max_completion_tokens, logit_bias, logprobs/top_logprobs, response_format ({"type":"json_object"}), structured_outputs, stop, tools/tool_choice, parallel_tool_calls (default true), verbosity (low/medium/high/xhigh/max, у Anthropic — output_config.effort). Провайдер-специфичные параметры (safe_prompt у Mistral, raw_mode у Hyperbolic) передаются провайдеру без изменений.

## Журнал

- 2026-10-08 · заведена из docs/inbox/routerai-sampling-parameters.md · приложение
- 2026-10-08 · на подтверждение · architect
- 2026-10-08 · подтверждён · architect
