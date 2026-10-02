---
id: M-0011
type: map
title: 'Функциональная карта: отметки состояния (34)'
status: approved
created: 2026-10-02
updated: 2026-10-02
---

# Функциональная карта: отметки состояния (34)

Черновик: составлен моделью, не подтверждён. Прочитайте, поправьте руками
то, что модель не поняла, и подтвердите — до этого карта на общую картину
не влияет.

```docdd-functional
{
  "added": {
    "capabilities": [
      {
        "id": "sign-in",
        "title": "Регистрация и вход",
        "parent": "account-roles",
        "status": "partial",
        "note": "Регистрация, вход и JWT работают, но полноценных ролей пользователя нет — только флаг администратора."
      },
      {
        "id": "password-recovery",
        "title": "Восстановление пароля",
        "parent": "account-roles",
        "status": "partial",
        "note": "Код восстановления генерируется и хранится как хеш, но реально никуда не отправляется — только пишется в лог сервера."
      },
      {
        "id": "account-security",
        "title": "Безопасность аккаунта",
        "parent": "account-roles",
        "status": "partial",
        "note": "Пароль хэшируется, смена пароля отзывает старые токены. Но вход не защищён от подбора пароля, нет отдельного «выйти со всех устройств»."
      },
      {
        "id": "platform-release",
        "title": "Приложение на iOS и Android",
        "parent": "account-roles",
        "status": "implemented",
        "note": "Приложение собирается под iOS и Android: рабочий Expo-конфиг, навигация, нет пустых экранов."
      },
      {
        "id": "sync-jobs",
        "title": "Офлайн и синхронизация",
        "parent": "my-data",
        "status": "implemented",
        "note": "Локальная база на устройстве, очередь действий и синхронизация с сервером при восстановлении сети реализованы."
      },
      {
        "id": "data-permissions",
        "title": "Доступ мини-приложений по разрешению",
        "parent": "my-data",
        "status": "not_implemented",
        "note": "Модуль не запрашивает и не получает разрешения на доступ к данным пользователя — такого механизма в коде нет."
      },
      {
        "id": "data-export-delete",
        "title": "Выгрузка и удаление своих данных",
        "parent": "my-data",
        "status": "not_implemented",
        "note": "Эндпоинтов выгрузки своих данных или удаления аккаунта в коде нет."
      },
      {
        "id": "module-registry",
        "title": "Регистрация и контракт мини-приложения",
        "parent": "extensions",
        "status": "implemented",
        "note": "Реестр и контракт модуля есть и на backend, и на фронтенде — ядро не завязано на конкретные модули."
      },
      {
        "id": "isolation",
        "title": "Изоляция и защита от утечек",
        "parent": "extensions",
        "status": "not_implemented",
        "note": "Модули общаются через общий контракт, но реальной изоляции и защиты от утечек между мини-приложениями в коде нет."
      },
      {
        "id": "third-party-apps",
        "title": "Мини-приложения сторонних авторов",
        "parent": "extensions",
        "status": "not_implemented",
        "note": "Подключаются только модули, прописанные в коде backend; загрузки стороннего недоверенного мини-приложения нет."
      },
      {
        "id": "graph-moderation",
        "title": "Проверка базовых графов",
        "parent": "admin-curation",
        "status": "partial",
        "note": "Кураторские действия (одобрить узлы, помечать core/derived, промоция в канон) есть в админке, но это ручные экшены, а не процесс модерации с очередью."
      },
      {
        "id": "user-moderation",
        "title": "Модерация пользователей",
        "parent": "admin-curation",
        "status": "not_implemented",
        "note": "Жалоб, блокировок или модерации поведения пользователей в коде нет."
      },
      {
        "id": "feature-flags",
        "title": "Переключатели выкатываемых функций",
        "parent": "admin-curation",
        "status": "not_implemented",
        "note": "Механизма переключателей выкатываемых функций в коде не найдено."
      },
      {
        "id": "srs-error-log",
        "title": "Интервальное повторение и ошибки",
        "parent": "memorize",
        "status": "implemented",
        "note": "FSRS-повторение и превращение ошибок в карточки реализованы и на сервере, и на клиенте."
      },
      {
        "id": "writing-ielts",
        "title": "Письмо с оценкой по рубрике",
        "parent": "check",
        "status": "implemented",
        "note": "Письмо с оценкой по рубрике через AI Gateway работает для IELTS Task 2 и TOEFL; не хватает только экрана для IELTS Task 1."
      },
      {
        "id": "ml-track",
        "title": "Задачи на код с ревью",
        "parent": "check",
        "status": "implemented",
        "note": "Задача на код с автосохранением черновика и ревью по рубрике через AI Gateway подключена к курсу."
      },
      {
        "id": "speaking",
        "title": "Устный ответ с оценкой",
        "parent": "check",
        "status": "not_implemented",
        "note": "Тип устного ответа только объявлен — экрана, записи голоса, распознавания и оценки нет."
      },
      {
        "id": "reception-drills",
        "title": "Чтение и аудирование",
        "parent": "check",
        "status": "not_implemented",
        "note": "Типы упражнений на чтение/аудирование объявлены, но экрана и контента для них нет."
      },
      {
        "id": "assessment",
        "title": "Вопросы по теории узла",
        "parent": "check",
        "status": "implemented",
        "note": "Генерация вопросов по теории узла по ступеням Блума реализована и подключена к прохождению курса."
      },
      {
        "id": "placement",
        "title": "Что я уже знаю",
        "parent": "knowledge-graph",
        "status": "implemented",
        "note": "Адаптивное определение уже известного по графу (зонды по неопределённости и центральности) реализовано."
      },
      {
        "id": "course-study",
        "title": "Путь к цели",
        "parent": "knowledge-graph",
        "status": "implemented",
        "note": "Построение пути по графу и прохождение шагов с обновлением освоенности реализовано."
      },
      {
        "id": "learner-experience",
        "title": "Опыт учащегося",
        "parent": "activity-engine",
        "status": "implemented",
        "note": "Онбординг и единое «действие на сегодня» реализованы."
      },
      {
        "id": "goal-intake",
        "title": "Постановка цели",
        "parent": "knowledge-graph",
        "status": "partial",
        "note": "Пользователь задаёт предмет и целевой уровень, но цель не раскладывается на конкретные целевые узлы — интересы для ветвления с фронта не передаются."
      },
      {
        "id": "base-graph-build",
        "title": "Построение графа области",
        "parent": "knowledge-graph",
        "status": "implemented",
        "note": "Построение базового графа области с теорией, связями и курированием реализовано."
      },
      {
        "id": "graph-reuse",
        "title": "Переиспользование готовых областей",
        "parent": "knowledge-graph",
        "status": "partial",
        "note": "Готовая область переиспользуется автоматически при точном совпадении названия домена, но каталога и поиска существующих областей нет."
      },
      {
        "id": "graph-synthesis",
        "title": "Общий граф из нескольких областей",
        "parent": "knowledge-graph",
        "status": "not_implemented",
        "note": "Объединения нескольких областей в один общий граф в коде нет."
      },
      {
        "id": "personal-branches",
        "title": "Личные ветви",
        "parent": "knowledge-graph",
        "status": "implemented",
        "note": "Личные узлы, их рост и промоция в канон реализованы."
      },
      {
        "id": "read",
        "title": "Прочитать в удобном формате",
        "parent": "knowledge-use",
        "status": "partial",
        "note": "Теория узла читается офлайн структурированно, но без markdown-разметки и без импорта PDF/markdown-файлов."
      },
      {
        "id": "memorize-techniques",
        "title": "Другие техники запоминания",
        "parent": "memorize",
        "status": "not_implemented",
        "note": "Кроме интервального повторения других техник запоминания в коде нет."
      },
      {
        "id": "knowledge-games",
        "title": "Мини-игры на практику",
        "parent": "check",
        "status": "not_implemented",
        "note": "Мини-игр кроме карточек и вопросов в коде нет."
      },
      {
        "id": "method-switch",
        "title": "Смена способа на лету",
        "parent": "knowledge-use",
        "status": "not_implemented",
        "note": "Шаг курса проходится по жёсткой последовательности — переключить способ работы со знанием на лету нельзя."
      },
      {
        "id": "progress",
        "title": "Прогресс по области",
        "parent": "knowledge-use",
        "status": "implemented",
        "note": "Экран прогресса по области (освоенность, удержание, ошибки, регулярность) реализован."
      },
      {
        "id": "study-groups",
        "title": "Группы по области",
        "parent": "community",
        "status": "not_implemented",
        "note": "Групп пользователей по области в коде нет — ни моделей, ни экранов."
      },
      {
        "id": "topic-discussions",
        "title": "Обсуждение темы графа",
        "parent": "community",
        "status": "not_implemented",
        "note": "Обсуждений или комментариев к узлу графа в коде нет."
      }
    ]
  }
}
```

## Журнал

- 2026-10-02 · заведена черновиком · модель
- 2026-10-02 · на подтверждение
- 2026-10-02 · подтверждён
