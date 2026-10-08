---
id: M-0032
type: map
title: 'Состав навыка: контур до долгой сборки графа'
status: approved
created: 2026-10-07
updated: 2026-10-07
---

# Состав навыка: контур до долгой сборки графа

Со слов заметки user-flow-skill-composition.md: сейчас контур областей и наполнение понятиями идут одной фоновой задачей (`profile_store.py`, `request(with_graph=True)`), и человек узнаёт состав навыка только через 8–10 минут, не успев отметить «это я уже знаю» до того, как модель потратила на область время.

```docdd-functional
{
  "added": {
    "capabilities": [
      {
        "id": "skill-outline-preview",
        "title": "Контур состава навыка до сборки",
        "parent": "skill-profile",
        "status": "not_implemented",
        "note": "сейчас контур и наполнение — один запрос без промежуточного показа"
      },
      {
        "id": "skill-area-opt-out",
        "title": "Отметка «уже владею» по области",
        "parent": "skill-profile",
        "status": "not_implemented"
      },
      {
        "id": "area-build-progress",
        "title": "Параллельное наполнение по областям с видимым статусом",
        "parent": "multi-source-area-build",
        "status": "partial",
        "note": "фоновая сборка есть (profile_store.py: dispatch), но по 4 области разом и без статуса по каждой"
      }
    ],
    "relations": [
      {
        "from": "area-build-progress",
        "to": "skill-outline-preview",
        "type": "depends",
        "summary": "наполнение запускается только после подтверждённого человеком контура"
      }
    ]
  }
}
```

## Журнал

- 2026-10-07 · заведена из docs/inbox/user-flow-skill-composition.md, docs/inbox/graph-build-background-and-visibility.md · приложение
- 2026-10-07 · на подтверждение · architect
- 2026-10-07 · подтверждён · architect
