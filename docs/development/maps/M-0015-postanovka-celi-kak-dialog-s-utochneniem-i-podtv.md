---
id: M-0015
type: map
title: Постановка цели как диалог с уточнением и подтверждением
status: draft
created: 2026-10-02
updated: 2026-10-02
---

# Постановка цели как диалог с уточнением и подтверждением

Сейчас постановка цели — голая форма (название предмета и уровень), и граф строится прямо по ней. Нужен диалог: свободный ввод → уточняющие вопросы модели → пересказ и подтверждение понятой области → только после этого доступно построение.

```docdd-functional
{
  "added": {
    "capabilities": [
      {
        "id": "goal-intake",
        "title": "Постановка цели",
        "parent": "knowledge-graph",
        "status": "partial",
        "note": "Сейчас форма: название предмета и целевой уровень, без уточнения и подтверждения"
      },
      {
        "id": "goal-clarify",
        "title": "Уточняющие вопросы к цели",
        "parent": "goal-intake",
        "status": "not_implemented"
      },
      {
        "id": "goal-confirm",
        "title": "Подтверждение понятой области перед построением",
        "parent": "goal-intake",
        "status": "not_implemented"
      }
    ],
    "relations": [
      {
        "from": "goal-clarify",
        "to": "goal-confirm",
        "type": "feeds",
        "summary": "ответы на уточняющие вопросы формируют пересказ для подтверждения"
      },
      {
        "from": "goal-confirm",
        "to": "base-graph-build",
        "type": "triggers",
        "summary": "подтверждение области открывает построение графа; без него граф не строится"
      }
    ]
  }
}
```

## Журнал

- 2026-10-02 · заведена из docs/inbox/goal-intake-dialog.md · приложение
