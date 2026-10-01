---
id: A-0009
type: decision
title: Провайдер LLM задаётся конфигурацией; один OpenAI-совместимый gateway
status: approved
created: 2026-09-30
updated: 2026-10-01
---

# Провайдер LLM задаётся конфигурацией; один OpenAI-совместимый gateway

Принято 2026-08-25. Провайдер менялся трижды (Claude SDK, OpenRouter, RouterAI), и каждый раз выбор расползался по коду. Решено: любой сервис с /chat/completions и tool calling обслуживает один класс OpenAICompatibleGateway; адрес и ключ — LLM_BASE_URL/LLM_API_KEY, модели — LLM_MODEL_SCORING/LLM_MODEL_GENERATION, рубрика может задать свою model. Без ключа — MockAIGateway, модули проверяют has_llm(). max_tokens обязателен в каждом запросе; обрыв, 402 и текст вместо вызова инструмента повторяются до трёх раз. Сейчас используется RouterAI с моделью deepseek/deepseek-v4-flash-0731.

## Журнал

- 2026-09-30 · заведена из docs/inbox/decision-llm-provider-as-config.md · приложение
- 2026-10-01 · на подтверждение · architect
- 2026-10-01 · подтверждён · architect
