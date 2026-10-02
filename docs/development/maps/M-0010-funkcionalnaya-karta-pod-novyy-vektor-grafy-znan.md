---
id: M-0010
type: map
title: 'Функциональная карта под новый вектор: графы знаний и мини-приложения'
status: approved
created: 2026-10-02
updated: 2026-10-02
---

# Функциональная карта под новый вектор: графы знаний и мини-приложения

Карта перестраивается от технического «Движка Activity» к тому, что делает человек: строит граф знаний под цель, работает со знаниями через мини-приложения (прочитать, запомнить, проверить), владеет своими данными, общается с изучающими то же. Предметы (IELTS, TOEFL, ML) уходят внутрь мини-приложений проверки и перестают быть целью продукта. Возможности, которые остаются по смыслу, объявлены заново под новыми родителями с прежним id (placement, course-study, srs-error-log, assessment, writing-ielts, ml-track, speaking, reception-drills, sync-jobs, ai-gateway, admin-curation, account-roles, platform-release); технические верхние уровни activity-engine и learner-experience убраны — первый описывает устройство кода, второй растворён в «Прогрессе» и «Прочитать».

```docdd-functional
{
  "added": {
    "vision": {
      "problem": "Человек учит что-то из разных источников, и знания у него разрознены: не видно, как темы связаны между собой, что уже известно, чего не хватает до цели и в каком порядке идти. Выученное забывается, а проверить себя по всей области, а не по отдельным фактам, нечем. Курсы дают поток материала без учёта уже известного; карточки — запоминание без структуры; тесты — проверку без пути к цели.",
      "audience": "Тот, кто сам изучает или повторяет область под свою цель — экзамен, работа, увлечение; область любая: язык, технология, наука, игра. Вокруг — кураторы, следящие за качеством базовых графов, и авторы мини-приложений для новых способов читать, запоминать и проверять знания.",
      "outcome": "На вопрос «что хочешь изучить» человек получает граф знаний под свою цель: базовый граф области, отмеченное уже известное, свои личные ветви. Видит, сколько освоено и что осталось, читает/запоминает/проверяет знания удобными способами и меняет способ, не теряя накопленного. Доходит до цели по своему графу; освоенное удерживается; новая область строится быстрее, опираясь на уже готовые графы других областей.",
      "not": "Не учебник и не курс одного предмета — предметы это данные графа, а не рамка продукта. Не отдаёт данные мини-приложениям напрямую, только через платформу и по разрешению человека. Не выдаёт сгенерированное моделью за проверенное — граф без проверки куратором помечен как черновик. Не выдаёт официальных сертификатов — проверка это тренировочный сигнал. Не превращается в ленту ради времени в приложении."
    },
    "capabilities": [
      {
        "id": "knowledge-graph",
        "title": "Графы знаний"
      },
      {
        "id": "goal-intake",
        "title": "Постановка цели",
        "parent": "knowledge-graph"
      },
      {
        "id": "base-graph-build",
        "title": "Построение графа области",
        "parent": "knowledge-graph"
      },
      {
        "id": "graph-reuse",
        "title": "Переиспользование готовых областей",
        "parent": "knowledge-graph"
      },
      {
        "id": "graph-synthesis",
        "title": "Общий граф из нескольких областей",
        "parent": "knowledge-graph"
      },
      {
        "id": "placement",
        "title": "Что я уже знаю",
        "parent": "knowledge-graph"
      },
      {
        "id": "course-study",
        "title": "Путь к цели",
        "parent": "knowledge-graph"
      },
      {
        "id": "personal-branches",
        "title": "Личные ветви",
        "parent": "knowledge-graph"
      },
      {
        "id": "knowledge-use",
        "title": "Работа со знаниями"
      },
      {
        "id": "read",
        "title": "Прочитать в удобном формате",
        "parent": "knowledge-use"
      },
      {
        "id": "memorize",
        "title": "Запомнить",
        "parent": "knowledge-use"
      },
      {
        "id": "srs-error-log",
        "title": "Интервальное повторение и ошибки",
        "parent": "memorize"
      },
      {
        "id": "memorize-techniques",
        "title": "Другие техники запоминания",
        "parent": "memorize"
      },
      {
        "id": "check",
        "title": "Проверить себя",
        "parent": "knowledge-use"
      },
      {
        "id": "assessment",
        "title": "Вопросы по теории узла",
        "parent": "check"
      },
      {
        "id": "writing-ielts",
        "title": "Письмо с оценкой по рубрике",
        "parent": "check"
      },
      {
        "id": "ml-track",
        "title": "Задачи на код с ревью",
        "parent": "check"
      },
      {
        "id": "speaking",
        "title": "Устный ответ с оценкой",
        "parent": "check"
      },
      {
        "id": "reception-drills",
        "title": "Чтение и аудирование",
        "parent": "check"
      },
      {
        "id": "knowledge-games",
        "title": "Мини-игры на практику",
        "parent": "check"
      },
      {
        "id": "method-switch",
        "title": "Смена способа на лету",
        "parent": "knowledge-use"
      },
      {
        "id": "progress",
        "title": "Прогресс по области",
        "parent": "knowledge-use"
      },
      {
        "id": "my-data",
        "title": "Мои знания и данные"
      },
      {
        "id": "sync-jobs",
        "title": "Офлайн и синхронизация",
        "parent": "my-data"
      },
      {
        "id": "data-permissions",
        "title": "Доступ мини-приложений по разрешению",
        "parent": "my-data"
      },
      {
        "id": "data-export-delete",
        "title": "Выгрузка и удаление своих данных",
        "parent": "my-data"
      },
      {
        "id": "extensions",
        "title": "Подключение мини-приложений"
      },
      {
        "id": "module-registry",
        "title": "Регистрация и контракт мини-приложения",
        "parent": "extensions"
      },
      {
        "id": "isolation",
        "title": "Изоляция и защита от утечек",
        "parent": "extensions"
      },
      {
        "id": "third-party-apps",
        "title": "Мини-приложения сторонних авторов",
        "parent": "extensions"
      },
      {
        "id": "admin-curation",
        "title": "Администрирование"
      },
      {
        "id": "graph-moderation",
        "title": "Проверка базовых графов",
        "parent": "admin-curation"
      },
      {
        "id": "user-moderation",
        "title": "Модерация пользователей",
        "parent": "admin-curation"
      },
      {
        "id": "feature-flags",
        "title": "Переключатели выкатываемых функций",
        "parent": "admin-curation"
      },
      {
        "id": "ai-gateway",
        "title": "Контроль расходов на AI",
        "parent": "admin-curation"
      },
      {
        "id": "community",
        "title": "Сообщество"
      },
      {
        "id": "study-groups",
        "title": "Группы по области",
        "parent": "community"
      },
      {
        "id": "topic-discussions",
        "title": "Обсуждение темы графа",
        "parent": "community"
      },
      {
        "id": "account-roles",
        "title": "Доступ и аккаунт"
      },
      {
        "id": "sign-in",
        "title": "Регистрация и вход",
        "parent": "account-roles"
      },
      {
        "id": "password-recovery",
        "title": "Восстановление пароля",
        "parent": "account-roles"
      },
      {
        "id": "account-security",
        "title": "Безопасность аккаунта",
        "parent": "account-roles"
      },
      {
        "id": "platform-release",
        "title": "Приложение на iOS и Android",
        "parent": "account-roles"
      }
    ]
  }
}
```

## Журнал

- 2026-10-02 · заведена из docs/inbox/functional-map-knowledge-platform.md, docs/inbox/product-vector.md · приложение
- 2026-10-02 · на подтверждение · architect
- 2026-10-02 · подтверждён · architect
