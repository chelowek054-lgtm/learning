---
id: M-0050
type: map
title: 'Наполнение графа знаний: утверждения, источники, сверка, сборка узла, языки'
status: approved
created: 2026-10-12
updated: 2026-10-12
---

# Наполнение графа знаний: утверждения, источники, сверка, сборка узла, языки

Со слов заметок: единица знания — утверждение со ссылкой на место в источнике; источники только с разрешённой лицензией и проходят воронку отсева; понятие одно на все области и языки; новые утверждения сверяются с узлом, противоречия — в пул администраторов; узел собирается заранее (теория и банк заданий), обучение идёт без модели; знания имеют срок актуальности; интерфейс на русском и английском.

```docdd-functional
{
  "added": {
    "capabilities": [
      {
        "id": "claim-graph",
        "title": "Утверждения со ссылкой на место в источнике",
        "parent": "knowledge-graph"
      },
      {
        "id": "global-concepts",
        "title": "Одно понятие в нескольких областях",
        "parent": "knowledge-graph"
      },
      {
        "id": "multilingual-graph",
        "title": "Многоязычный граф, основной язык английский",
        "parent": "knowledge-graph"
      },
      {
        "id": "knowledge-freshness",
        "title": "Срок актуальности знаний и обновление",
        "parent": "knowledge-graph"
      },
      {
        "id": "source-license-filter",
        "title": "Только источники с разрешённой лицензией",
        "parent": "multi-source-area-build"
      },
      {
        "id": "source-quality-funnel",
        "title": "Воронка отсева источников и уровень доверия",
        "parent": "multi-source-area-build"
      },
      {
        "id": "bilingual-ingest",
        "title": "Разбор источников на русском и английском",
        "parent": "multi-source-area-build"
      },
      {
        "id": "claim-reconciliation",
        "title": "Сверка утверждений узла и пул проблем",
        "parent": "graph-moderation"
      },
      {
        "id": "consensus-correction",
        "title": "Исправление ошибочного консенсуса и жалобы на ошибку",
        "parent": "graph-moderation"
      },
      {
        "id": "node-compile",
        "title": "Сборка узла заранее: теория из утверждений",
        "parent": "read"
      },
      {
        "id": "learner-sources",
        "title": "Источник и место в оригинале для учащегося",
        "parent": "read"
      },
      {
        "id": "learning-item-bank",
        "title": "Банк карточек и заданий с ключами без модели",
        "parent": "check"
      },
      {
        "id": "ui-i18n",
        "title": "Интерфейс на русском и английском",
        "parent": "learner-experience"
      }
    ],
    "relations": [
      {
        "from": "claim-reconciliation",
        "to": "claim-graph",
        "type": "depends",
        "summary": "сверяются утверждения, а не понятия целиком"
      },
      {
        "from": "node-compile",
        "to": "claim-graph",
        "type": "depends",
        "summary": "теория собирается только из принятых утверждений"
      },
      {
        "from": "learning-item-bank",
        "to": "node-compile",
        "type": "depends",
        "summary": "задания собираются в той же сборке узла"
      },
      {
        "from": "learner-sources",
        "to": "source-license-filter",
        "type": "depends",
        "summary": "показывать фрагменты можно только при разрешённой лицензии"
      },
      {
        "from": "learner-sources",
        "to": "claim-graph",
        "type": "uses",
        "summary": "ссылка идёт от утверждения к месту в источнике"
      },
      {
        "from": "source-quality-funnel",
        "to": "claim-graph",
        "type": "feeds",
        "summary": "в извлечение идут только прошедшие воронку источники"
      },
      {
        "from": "knowledge-freshness",
        "to": "multi-source-area-build",
        "type": "triggers",
        "summary": "просроченный узел запускает поиск более новых источников"
      },
      {
        "from": "consensus-correction",
        "to": "claim-reconciliation",
        "type": "uses",
        "summary": "решения по спорам принимаются в том же пуле"
      },
      {
        "from": "bilingual-ingest",
        "to": "multilingual-graph",
        "type": "depends",
        "summary": "источники на двух языках сливаются в один узел"
      },
      {
        "from": "multilingual-graph",
        "to": "global-concepts",
        "type": "uses",
        "summary": "одно понятие на все области и все языки"
      }
    ]
  }
}
```

## Журнал

- 2026-10-12 · заведена из docs/inbox/utverzhdenie-edinica-znaniya-grafa.md, docs/inbox/istochniki-tolko-s-licenziey-i-vidimost-uchaschemusya.md, docs/inbox/odno-ponyatie-v-neskolkih-oblastyah.md, docs/inbox/sverka-utverzhdeniy-i-pul-problem.md, docs/inbox/sborka-uzla-i-bank-zadaniy-bez-llm-pri-obuchenii.md, docs/inbox/protukhanie-znaniy-v-grafe.md, docs/inbox/oshibochnyy-konsensus-i-ispravlenie-znaniy.md, docs/inbox/otsev-nelikvidnyh-istochnikov.md, docs/inbox/mnogoyazychnyy-graf-znaniy.md, docs/inbox/razbor-istochnikov-na-dvuh-yazykah.md, docs/inbox/i18n-interfeysa-russkiy-i-angliyskiy.md · приложение
- 2026-10-12 · на подтверждение · architect
- 2026-10-12 · подтверждён · architect
