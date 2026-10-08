---
id: M-0031
type: map
title: 'Функциональная карта: отметки состояния (8, задачи закрыты)'
status: approved
created: 2026-10-07
updated: 2026-10-07
---

# Функциональная карта: отметки состояния (8, задачи закрыты)

Черновик: составлен моделью, не подтверждён. Прочитайте, поправьте руками
то, что модель не поняла, и подтвердите — до этого карта на общую картину
не влияет.

Повод: сверка (`docdd-report`/валидатор) показала `capability_behind` для
восьми возможностей — все задачи под ними закрыты, а возможность всё ещё
«Не оценено»/«Не реализовано». Статусы ниже поставлены по коду, не по
журналу задач: для каждой указан файл и символ, где смотреть.

```docdd-functional
{
  "added": {
    "capabilities": [
      {
        "id": "ai-gateway",
        "title": "Контроль расходов на AI",
        "parent": "admin-curation",
        "status": "partial",
        "note": "Единая точка вызова модели с переключением на заглушку без ключа (core/ai_gateway.py: get_ai_gateway). Расход токенов пишется и виден администратору: core/usage.py (record, summary), эндпоинт GET /usage/summary в api/routers/usage.py (только для суперпользователя, FR-AI-05). Явного потолка/лимита расходов в коде нет — есть только видимость, не контроль в смысле ограничения."
      },
      {
        "id": "goal-subdomain-split",
        "title": "Разбиение цели на субдомены",
        "parent": "base-graph-build",
        "status": "implemented",
        "note": "modules/knowledge/subdomains.py: propose_split предлагает разбиение с ограничением MAX_SUBDOMAINS и разрывом циклов (_break_cycles); clean_split позволяет человеку поправить разбиение до сборки."
      },
      {
        "id": "goal-tree-assembly",
        "title": "Сборка графа цели из субдоменов",
        "parent": "base-graph-build",
        "status": "implemented",
        "note": "modules/knowledge/subdomains.py: build_subdomain строит каждый субдомен отдельным запросом, assemble собирает итоговый граф из поддеревьев, budget считает расход токенов/запросов на построение."
      },
      {
        "id": "goal-clarify",
        "title": "Уточняющие вопросы к цели",
        "parent": "goal-intake",
        "status": "implemented",
        "note": "modules/knowledge/router.py: POST /goal/clarify (clarify_goal) задаёт уточняющие вопросы; клиент — learningFront/src/features/goal-intake/ui/goal-intake-dialog.tsx. Модель спрашивает только о пяти полях, которых не хватает (T-0074)."
      },
      {
        "id": "goal-confirm",
        "title": "Подтверждение понятой области перед построением",
        "parent": "goal-intake",
        "status": "implemented",
        "note": "modules/knowledge/router.py: POST /goal/summarize (пересказ) и POST /goal/confirm (confirm_goal) сохраняют итог; _require_confirmed_goal блокирует построение графа, пока цель не подтверждена. Для офлайна остаётся прямая форма без диалога."
      },
      {
        "id": "domain-registry",
        "title": "Реестр базовых областей с устойчивыми ключами",
        "parent": "graph-reuse",
        "status": "implemented",
        "note": "modules/knowledge/models.py: Domain (устойчивый key, foundation — нижняя опора), DomainAlias (другое название → тот же key), DomainEdge («нужно знать до»); API modules/knowledge/domains_api.py (GET/POST /domains)."
      },
      {
        "id": "cross-domain-links",
        "title": "Предпосылки между понятиями разных областей по ступени освоения",
        "parent": "domain-graph",
        "status": "implemented",
        "note": "modules/knowledge/models.py: ConceptLink — предпосылка между понятиями разных областей с полем bloom (ступень освоения, с которой предпосылка обязательна)."
      },
      {
        "id": "cross-domain-placement",
        "title": "Проверка освоенности сверху вниз по цепочке базовых областей",
        "parent": "placement",
        "status": "implemented",
        "note": "modules/knowledge/chain_placement.py: chain_plan и next_chain_probe; API GET /graph/placement/{domain}/chain и /chain-probe в modules/knowledge/cross_links_api.py. Снятие нижестоящей области по освоенности верхней подключено к курсу (T-0066); клиентский экран объёма пути — отдельная возможность (T-0067, см. также M-0017/M-0019)."
      }
    ]
  }
}
```

## Журнал

- 2026-10-07 · заведена черновиком по находке валидатора (`capability_behind`): T-0003…T-0055 (ai-gateway), T-0060 (субдомены), T-0061/T-0074 (диалог цели), T-0064…T-0067 (граф областей) закрыты, а возможности не оценены · модель
- 2026-10-07 · на подтверждение · architect
- 2026-10-07 · подтверждён · architect
