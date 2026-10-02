---
id: M-0012
type: map
title: 'Функциональная карта: связи (+17 −0)'
status: approved
created: 2026-10-02
updated: 2026-10-02
---

# Функциональная карта: связи (+17 −0)

Черновик: составлен моделью, не подтверждён. Прочитайте, поправьте руками
то, что модель не поняла, и подтвердите — до этого карта на общую картину
не влияет.

```docdd-functional
{
  "added": {
    "relations": [
      {
        "from": "srs-error-log",
        "to": "ai-gateway",
        "type": "depends",
        "summary": "карточки ошибок рождаются из оценки AI Gateway"
      },
      {
        "from": "writing-ielts",
        "to": "ai-gateway",
        "type": "depends",
        "summary": "оценка эссе по рубрике идёт через AI Gateway"
      },
      {
        "from": "ml-track",
        "to": "ai-gateway",
        "type": "depends",
        "summary": "ревью кода по рубрике идёт через AI Gateway"
      },
      {
        "from": "sync-jobs",
        "to": "ai-gateway",
        "type": "triggers",
        "summary": "push синхронизации запускает обработку отложенных AI-задач"
      },
      {
        "from": "writing-ielts",
        "to": "srs-error-log",
        "type": "feeds",
        "summary": "стартовая колода и ошибки письма становятся карточками повторения"
      },
      {
        "from": "ml-track",
        "to": "srs-error-log",
        "type": "feeds",
        "summary": "ошибки ревью кода становятся карточками error-log"
      },
      {
        "from": "assessment",
        "to": "ai-gateway",
        "type": "uses",
        "summary": "генерация заданий зовёт AI Gateway, но есть заглушка без ключа"
      },
      {
        "from": "placement",
        "to": "assessment",
        "type": "depends",
        "summary": "зонд плейсмента берётся из сгенерированных заданий по узлу"
      },
      {
        "from": "course-study",
        "to": "assessment",
        "type": "depends",
        "summary": "шаг курса разворачивается в задания по теории узла"
      },
      {
        "from": "course-study",
        "to": "placement",
        "type": "depends",
        "summary": "ответ на шаге курса обновляет освоенность через плейсмент"
      },
      {
        "from": "course-study",
        "to": "srs-error-log",
        "type": "feeds",
        "summary": "слабый узел шага курса заводит карточку удержания"
      },
      {
        "from": "placement",
        "to": "base-graph-build",
        "type": "depends",
        "summary": "зонд выбирается среди узлов уже построенного графа"
      },
      {
        "from": "personal-branches",
        "to": "graph-moderation",
        "type": "feeds",
        "summary": "личный узел становится кандидатом на промоцию, которую подтверждает администратор"
      },
      {
        "from": "ai-gateway",
        "to": "module-registry",
        "type": "depends",
        "summary": "рубрики для оценки берутся из реестра подключённых модулей"
      },
      {
        "from": "learner-experience",
        "to": "srs-error-log",
        "type": "uses",
        "summary": "экран «Сегодня» открывает повторение"
      },
      {
        "from": "learner-experience",
        "to": "course-study",
        "type": "uses",
        "summary": "экран «Сегодня» открывает курс"
      },
      {
        "from": "learner-experience",
        "to": "placement",
        "type": "uses",
        "summary": "экран «Сегодня» открывает плейсмент"
      }
    ]
  }
}
```

## Журнал

- 2026-10-02 · заведена черновиком · модель
- 2026-10-02 · на подтверждение
- 2026-10-02 · подтверждён
