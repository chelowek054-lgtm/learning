---
id: M-0016
type: map
title: Сменный способ работы со знаниями и вторая техника запоминания
status: approved
created: 2026-10-02
updated: 2026-10-02
---

# Сменный способ работы со знаниями и вторая техника запоминания

Сегодня способ работы с блоком графа один (интервальное повторение и вопросы по теории) и вшит в курс. Нужен общий контракт способа и хотя бы вторая техника, чтобы контракт был проверен не на единственном случае.

```docdd-functional
{
  "added": {
    "capabilities": [
      {
        "id": "method-switch",
        "title": "Смена способа на лету",
        "parent": "knowledge-use",
        "status": "not_implemented",
        "note": "Способ вшит в курс; сменить его сейчас нельзя"
      },
      {
        "id": "memorize-techniques",
        "title": "Другие техники запоминания",
        "parent": "memorize",
        "status": "not_implemented",
        "note": "Реализовано только интервальное повторение"
      },
      {
        "id": "method-contract",
        "title": "Единый контракт способа изучения",
        "parent": "method-switch"
      },
      {
        "id": "mastery-evidence",
        "title": "Свидетельство об освоении, не зависящее от способа",
        "parent": "method-switch"
      }
    ],
    "relations": [
      {
        "from": "method-contract",
        "to": "mastery-evidence",
        "type": "feeds",
        "summary": "способ по контракту возвращает свидетельство об освоении в общем формате"
      },
      {
        "from": "method-switch",
        "to": "memorize-techniques",
        "type": "depends",
        "summary": "смену способа нельзя проверить, пока есть только интервальное повторение"
      },
      {
        "from": "mastery-evidence",
        "to": "my-data",
        "type": "uses",
        "summary": "освоенность и ошибки хранятся в данных пользователя, а не в самом способе"
      }
    ]
  }
}
```

## Журнал

- 2026-10-02 · заведена из docs/inbox/method-switch-and-memorize-techniques.md · приложение
- 2026-10-02 · на подтверждение · architect
- 2026-10-02 · подтверждён · architect
