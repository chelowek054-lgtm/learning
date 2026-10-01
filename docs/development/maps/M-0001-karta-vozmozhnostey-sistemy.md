---
id: M-0001
type: map
title: Карта возможностей системы
status: approved
created: 2026-09-30
updated: 2026-09-30
---

# Карта возможностей системы

Со слов заметки system-capability-map.md: движок Activity и модули — основа для всего; от него растут аккаунт, синхронизация, AI-gateway, повторение, предметные треки (письмо, ML, речь, чтение/аудирование) и граф знаний, на графе стоят задания, плейсмент и курс; отдельно — опыт учащегося, администрирование и платформа/релиз. Разбита чуть подробнее исходного списка: предметные треки и опыт/администрирование — отдельные узлы, а не один пункт, чтобы совпадать с делением по требованиям (FR-*) в остальных заметках.

```docdd-functional
{
  "added": {
    "capabilities": [
      {
        "id": "activity-engine",
        "title": "Движок Activity и модули"
      },
      {
        "id": "account-roles",
        "title": "Аккаунт и роли",
        "parent": "activity-engine"
      },
      {
        "id": "sync-jobs",
        "title": "Синхронизация и очередь задач",
        "parent": "activity-engine"
      },
      {
        "id": "ai-gateway",
        "title": "AI-gateway, рубрики, стоимость",
        "parent": "activity-engine"
      },
      {
        "id": "srs-error-log",
        "title": "Интервальное повторение и журнал ошибок",
        "parent": "activity-engine"
      },
      {
        "id": "writing-ielts",
        "title": "Письмо IELTS",
        "parent": "activity-engine"
      },
      {
        "id": "ml-track",
        "title": "ML-трек",
        "parent": "activity-engine"
      },
      {
        "id": "speaking",
        "title": "Речь (Speaking)",
        "parent": "activity-engine"
      },
      {
        "id": "reception-drills",
        "title": "Чтение и аудирование",
        "parent": "activity-engine"
      },
      {
        "id": "knowledge-graph",
        "title": "Граф знаний",
        "parent": "activity-engine"
      },
      {
        "id": "assessment",
        "title": "Задания из теории узла",
        "parent": "knowledge-graph"
      },
      {
        "id": "placement",
        "title": "Адаптивный плейсмент",
        "parent": "knowledge-graph"
      },
      {
        "id": "course-study",
        "title": "Курс и прохождение шага",
        "parent": "knowledge-graph"
      },
      {
        "id": "learner-experience",
        "title": "Опыт учащегося",
        "parent": "activity-engine"
      },
      {
        "id": "admin-curation",
        "title": "Администрирование и курирование",
        "parent": "activity-engine"
      },
      {
        "id": "platform-release",
        "title": "Платформа и релиз",
        "parent": "activity-engine"
      }
    ]
  }
}
```

## Журнал

- 2026-09-30 · заведена из docs/inbox/system-capability-map.md · приложение
- 2026-09-30 · на подтверждение · architect
- 2026-09-30 · подтверждён · architect
