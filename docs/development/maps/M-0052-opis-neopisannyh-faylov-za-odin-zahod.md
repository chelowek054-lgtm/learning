---
id: M-0052
type: map
title: 'Карта по описи: описание неописанных файлов за один заход'
status: draft
created: 2026-10-20
updated: 2026-10-20
---

# Карта по описи: описание неописанных файлов за один заход

Черновик: составлен моделью по описи, не подтверждён. Охватывает 213 файлов,
которые ни одна подтверждённая карта ещё не описывала (бэкенд: утверждения и
конвейер знаний, миграции, тесты, скрипты; клиент: фичи, страницы, shared), плюс
5 файлов, которым в карте не место. Описание поверхностное: что
файл делает, на что опирается, с какими источниками данных и экранами связан.

## Кодовая база

```docdd-codemap
{
  "added": {
    "modules": [
      {
        "id": "learningBack/api/__init__.py",
        "title": "__init__.py",
        "path": "learningBack/api/__init__.py",
        "summary": "Слой API: сборка приложения и HTTP-маршруты ядра. Выше модулей и ядра в порядке слоёв (A-0023)."
      },
      {
        "id": "learningBack/api/routers/__init__.py",
        "title": "__init__.py",
        "path": "learningBack/api/routers/__init__.py",
        "summary": "Роутеры API (Ф0 — заглушки без бизнес-логики)."
      },
      {
        "id": "learningBack/api/routers/push.py",
        "title": "push.py",
        "path": "learningBack/api/routers/push.py",
        "summary": "Устройства для push-уведомлений (T-0086): регистрация, отключение, удаление. Регистрация токена — это согласие человека на push; отключить можно в настройках, не удаляя устройство."
      },
      {
        "id": "learningBack/core/embeddings.py",
        "title": "embeddings.py",
        "path": "learningBack/core/embeddings.py",
        "summary": "Эмбеддинги текста для поиска близких понятий (T-0078, A-0024). Порт: список строк на входе, список векторов фиксированной длины на выходе. Провайдер — любой сервис с совместимым `POST /embeddings` (по умолчанию `baai/bge-m3`: понимает русский и английский вместе, 1024 числа).…"
      },
      {
        "id": "learningBack/core/errors.py",
        "title": "errors.py",
        "path": "learningBack/core/errors.py",
        "summary": "Ошибки API с кодом и параметрами: текст выбирает клиент на языке человека (R-0081, T-0179). `detail` остаётся строкой (по-русски) для прежних клиентов и логов; новые клиенты берут `code` и `params`."
      },
      {
        "id": "learningBack/core/messages.py",
        "title": "messages.py",
        "path": "learningBack/core/messages.py",
        "summary": "Тексты сервера для людей: уведомления и письма на языке пользователя (R-0081, T-0179). Язык берётся из профиля (`uiLang`, затем `studyLang`), без настройки остаётся русский, как было до двух языков. Ошибки API отдают код и параметры, а не текст: выбирает текст клиент…"
      },
      {
        "id": "learningBack/core/objects.py",
        "title": "objects.py",
        "path": "learningBack/core/objects.py",
        "summary": "Объектное хранилище источников (A-0025, T-0073, R-0045). Ядро знает только контракт «ключ → байты» и временную ссылку для администратора. Реализация — любой S3-совместимый сервис (SeaweedFS в compose): код через `boto3`, адрес и ключи из окружения, поэтому замена хранилища…"
      },
      {
        "id": "learningBack/core/push.py",
        "title": "push.py",
        "path": "learningBack/core/push.py",
        "summary": "Push-уведомления вне приложения (T-0086, R-0044). Канал нужен, чтобы человек узнал о курсе при закрытом приложении. Провайдер — Expo Push: он работает с EAS-сборкой клиента и прячет за одним API FCM и APNs. Отправитель подменяем: другой провайдер — это новый класс с методом…"
      },
      {
        "id": "learningBack/migrations/versions/0025_graph_extensions.py",
        "title": "0025_graph_extensions.py",
        "path": "learningBack/migrations/versions/0025_graph_extensions.py",
        "summary": "graph_extensions: расширения Apache AGE и pgvector, схема графа знаний (T-0072) Revision ID: 0025_graph_extensions Revises: 0024_policy_consent Create Date: 2026-10-06 Существующие таблицы не меняются: concept, concept_edge, domain_edge остаются источником правды (A-0024), AGE и…"
      },
      {
        "id": "learningBack/migrations/versions/0026_provenance.py",
        "title": "0026_provenance.py",
        "path": "learningBack/migrations/versions/0026_provenance.py",
        "summary": "provenance: источники, фрагменты, связи знаний с источниками, статус связей, журнал проверки (T-0076) Revision ID: 0026_provenance Revises: 0025_graph_extensions Create Date: 2026-10-06"
      },
      {
        "id": "learningBack/migrations/versions/0027_concept_merge.py",
        "title": "0027_concept_merge.py",
        "path": "learningBack/migrations/versions/0027_concept_merge.py",
        "summary": "concept_merge: векторы понятий, решения по парам, очередь противоречий (T-0078) Revision ID: 0027_concept_merge Revises: 0026_provenance Create Date: 2026-10-06"
      },
      {
        "id": "learningBack/migrations/versions/0028_domain_specialist.py",
        "title": "0028_domain_specialist.py",
        "path": "learningBack/migrations/versions/0028_domain_specialist.py",
        "summary": "domain_specialist: специалисты по областям (T-0081) Revision ID: 0028_domain_specialist Revises: 0027_concept_merge Create Date: 2026-10-06"
      },
      {
        "id": "learningBack/migrations/versions/0029_notification.py",
        "title": "0029_notification.py",
        "path": "learningBack/migrations/versions/0029_notification.py",
        "summary": "notification: уведомления о курсе (T-0083) Revision ID: 0029_notification Revises: 0028_domain_specialist Create Date: 2026-10-06"
      },
      {
        "id": "learningBack/migrations/versions/0030_push_device.py",
        "title": "0030_push_device.py",
        "path": "learningBack/migrations/versions/0030_push_device.py",
        "summary": "push_device: устройства для push-уведомлений (T-0086) Revision ID: 0030_push_device Revises: 0029_notification Create Date: 2026-10-06"
      },
      {
        "id": "learningBack/migrations/versions/0031_concept_stage.py",
        "title": "0031_concept_stage.py",
        "path": "learningBack/migrations/versions/0031_concept_stage.py",
        "summary": "concept: этап, уровень сложности и необязательность понятия (T-0087, A-0030) Revision ID: 0031_concept_stage Revises: 0030_push_device Create Date: 2026-10-07"
      },
      {
        "id": "learningBack/migrations/versions/0032_skill_profile.py",
        "title": "0032_skill_profile.py",
        "path": "learningBack/migrations/versions/0032_skill_profile.py",
        "summary": "skill_profile: профиль навыка человека по цели (T-0088, R-0048) Revision ID: 0032_skill_profile Revises: 0031_concept_stage Create Date: 2026-10-07"
      },
      {
        "id": "learningBack/migrations/versions/0033_domain_embedding.py",
        "title": "0033_domain_embedding.py",
        "path": "learningBack/migrations/versions/0033_domain_embedding.py",
        "summary": "domain_embedding: вектор области для сопоставления по близости (T-0096, A-0031) Revision ID: 0033_domain_embedding Revises: 0032_skill_profile Create Date: 2026-10-07"
      },
      {
        "id": "learningBack/migrations/versions/0034_user_subject.py",
        "title": "0034_user_subject.py",
        "path": "learningBack/migrations/versions/0034_user_subject.py",
        "summary": "user_subject: предмет человека со статусом (T-0119) Revision ID: 0034_user_subject Revises: 0033_domain_embedding Create Date: 2026-10-11"
      },
      {
        "id": "learningBack/migrations/versions/0035_claims.py",
        "title": "0035_claims.py",
        "path": "learningBack/migrations/versions/0035_claims.py",
        "summary": "утверждения, источники утверждений, проблемы, словарь терминов, области понятий, учебные задания (T-0149) Revision ID: 0035_claims Revises: 0034_user_subject Create Date: 2026-10-12"
      },
      {
        "id": "learningBack/modules/knowledge/areas.py",
        "title": "areas.py",
        "path": "learningBack/modules/knowledge/areas.py",
        "summary": "Принадлежность понятия областям (R-0073): одно понятие может входить в несколько областей. `Concept.domain` — «домашняя» область, где понятие появилось; остальные членства — в `concept_area` вместе с этапом, уровнем и необязательностью для этой области. Курс, схема, плейсмент и…"
      },
      {
        "id": "learningBack/modules/knowledge/claims_api.py",
        "title": "claims_api.py",
        "path": "learningBack/modules/knowledge/claims_api.py",
        "summary": "API утверждений: источники для учащегося, пул проблем и жалобы «здесь ошибка» (R-0072, R-0074, R-0077). Учащийся видит у утверждения название источника, лицензию, место и ссылку на оригинал; текст цитаты — только если лицензия разрешает воспроизведение. Пул проблем и решения —…"
      },
      {
        "id": "learningBack/modules/knowledge/freshness.py",
        "title": "freshness.py",
        "path": "learningBack/modules/knowledge/freshness.py",
        "summary": "Протухание знаний и доверие к источникам по исходам споров (R-0076, R-0077, T-0163, T-0164, T-0167). Всё здесь работает без модели: находит просроченное по датам, ходит по адресам источников, считает проигранные споры. Запускается задачами очереди; расписание — внешнее (cron…"
      },
      {
        "id": "learningBack/modules/knowledge/funnel.py",
        "title": "funnel.py",
        "path": "learningBack/modules/knowledge/funnel.py",
        "summary": "Воронка отсева источников и уровень доверия (R-0072, R-0078, T-0152, T-0168, T-0169, T-0170). Дешёвые проверки первыми, модель последней: лицензия → язык → объём и качество текста → дубли → близость к области → одна проба моделью по выборке фрагментов. Отказ на любом шаге…"
      },
      {
        "id": "learningBack/modules/knowledge/gap_search.py",
        "title": "gap_search.py",
        "path": "learningBack/modules/knowledge/gap_search.py",
        "summary": "Поиск источников по областям, которых нет в графе (T-0084, R-0043). Отчёт по предварительным знаниям (prior_report) называет базовые области цели, по которым в графе нет ни одного понятия. Здесь администратор получает по каждой из них готовый запрос и одним действием запускает…"
      },
      {
        "id": "learningBack/modules/knowledge/graph_admin.py",
        "title": "graph_admin.py",
        "path": "learningBack/modules/knowledge/graph_admin.py",
        "summary": "Раздел админки «Граф знаний»: схема канона вместо трёх таблиц (T-0107…T-0110, R-0058). Страница и JSON-эндпоинты живут под тем же входом администратора, что и вся админка. Логика чтения и правок — в `graph_admin_data`; здесь только HTTP и перевод ошибок правки в понятные ответы."
      },
      {
        "id": "learningBack/modules/knowledge/graph_admin_data.py",
        "title": "graph_admin_data.py",
        "path": "learningBack/modules/knowledge/graph_admin_data.py",
        "summary": "Данные и правки схемы графа канона для админки (T-0107…T-0110, R-0058). Чтение собирает то, что раньше лежало в трёх таблицах: понятия области с этапами, связи внутри области, мосты между областями и граф самих областей. Правки идут теми же правилами, что и в остальном модуле:…"
      },
      {
        "id": "learningBack/modules/knowledge/ingest.py",
        "title": "ingest.py",
        "path": "learningBack/modules/knowledge/ingest.py",
        "summary": "Разбор документа в понятия со ссылками на фрагмент (T-0077, R-0043). Документ из хранилища режется на фрагменты (страница, заголовок главы из оглавления PDF), модель выделяет по окнам фрагментов понятия и связи, и КАЖДОЕ утверждение обязано сослаться на фрагмент и привести…"
      },
      {
        "id": "learningBack/modules/knowledge/langs.py",
        "title": "langs.py",
        "path": "learningBack/modules/knowledge/langs.py",
        "summary": "Язык текста: определение без модели и список поддерживаемых языков (R-0079, R-0080, T-0176). Основной язык графа — английский (A-0034), второй — русский. Язык документа нужен при приёме: поиск и разбор идут на обоих, текст на неподдерживаемом языке отклоняется с причиной, а не…"
      },
      {
        "id": "learningBack/modules/knowledge/localize.py",
        "title": "localize.py",
        "path": "learningBack/modules/knowledge/localize.py",
        "summary": "Язык изучения человека: теория, названия и задания узла на нём (R-0079, T-0174). Язык берётся из запроса (`lang`), затем из профиля (`studyLang`), иначе ничего не подменяется и узел отдаётся на языке по умолчанию. Тексты на других языках лежат в `content.i18n`, названия — в…"
      },
      {
        "id": "learningBack/modules/knowledge/merge.py",
        "title": "merge.py",
        "path": "learningBack/modules/knowledge/merge.py",
        "summary": "Слияние понятий из разных источников: близость по векторам и решение модели (T-0078, R-0043). Разбор нескольких книг (и нескольких окон одной) даёт одно и то же понятие под разными именами. Слияние идёт в два шага. Дёшево: эмбеддинги отбирают кандидатов — ближайших соседей…"
      },
      {
        "id": "learningBack/modules/knowledge/node_compile.py",
        "title": "node_compile.py",
        "path": "learningBack/modules/knowledge/node_compile.py",
        "summary": "Сборка узла заранее: теория из утверждений и банк заданий на каждый язык (R-0075, R-0079, T-0159, T-0160, T-0173). Один запрос к модели на понятие, когда меняется набор его принятых утверждений (хэш набора). Модель только раскладывает утверждения по разделам и сочиняет задания;…"
      },
      {
        "id": "learningBack/modules/knowledge/notifications.py",
        "title": "notifications.py",
        "path": "learningBack/modules/knowledge/notifications.py",
        "summary": "Уведомления о курсе: «готов» и «дополнен» с честной пометкой о непроверенном (T-0083, R-0044). Человек не ждёт разбора источников: курс собирается из имеющегося, а когда граф области пополняется (разобрана книга), он узнаёт, что добавлено и что это ещё черновик. Уведомления…"
      },
      {
        "id": "learningBack/modules/knowledge/notifications_api.py",
        "title": "notifications_api.py",
        "path": "learningBack/modules/knowledge/notifications_api.py",
        "summary": "API уведомлений о курсе (T-0083): список своих и отметка «прочитано»."
      },
      {
        "id": "learningBack/modules/knowledge/prior_report.py",
        "title": "prior_report.py",
        "path": "learningBack/modules/knowledge/prior_report.py",
        "summary": "Отчёт по предварительным знаниям: хватает, мало, нет (T-0075, R-0042). Тест по цепочке базовых областей (chain_placement) даёт освоенность понятий. Здесь она сверяется с графом: по каждой базовой области цели — хватает ли человеку знаний для цели, мало или нет, и есть ли эта…"
      },
      {
        "id": "learningBack/modules/knowledge/profile_api.py",
        "title": "profile_api.py",
        "path": "learningBack/modules/knowledge/profile_api.py",
        "summary": "API профиля навыка (T-0088): построить, прочитать, поправить, подтвердить."
      },
      {
        "id": "learningBack/modules/knowledge/profile_build.py",
        "title": "profile_build.py",
        "path": "learningBack/modules/knowledge/profile_build.py",
        "summary": "Скелет графа из профиля навыка (T-0090, R-0048, A-0032). Понятия профиля заводятся черновиками с этапами, уровнями и связями; области получают места в реестре областей и связи между собой, а понятия последнего этапа области-предпосылки привязываются к первым понятиям следующей.…"
      },
      {
        "id": "learningBack/modules/knowledge/profile_coverage.py",
        "title": "profile_coverage.py",
        "path": "learningBack/modules/knowledge/profile_coverage.py",
        "summary": "Отчёт полноты графа против профиля навыка (T-0099, R-0053). Профиль — «что нужно знать». Отчёт сверяет его с графом и по каждой области и понятию говорит: есть ли оно в графе и на чём стоит. Понятие находится по ключу скелета, а если скелет слит с разобранным из источника (ключ…"
      },
      {
        "id": "learningBack/modules/knowledge/profile_fill.py",
        "title": "profile_fill.py",
        "path": "learningBack/modules/knowledge/profile_fill.py",
        "summary": "Наполнение контура понятиями: все области параллельно, статус по каждой (T-0103, R-0056). Контур (области и этапы) человек уже подтвердил. Теперь по каждой области отдельным запросом приходят понятия; готовая область сразу сохраняется и «публикуется» — её скелет попадает в граф,…"
      },
      {
        "id": "learningBack/modules/knowledge/profile_match.py",
        "title": "profile_match.py",
        "path": "learningBack/modules/knowledge/profile_match.py",
        "summary": "Сопоставление профиля навыка с графом по близости векторов (T-0096, R-0050, A-0031). Для каждой области профиля решается: такая область в графе уже есть, спорный случай или новая. Сначала точное совпадение по названию и алиасам (реестр областей), затем косинусная близость…"
      },
      {
        "id": "learningBack/modules/knowledge/profile_sources.py",
        "title": "profile_sources.py",
        "path": "learningBack/modules/knowledge/profile_sources.py",
        "summary": "Автопоиск и разбор нескольких источников для новых областей профиля (T-0097, R-0051, A-0032). Скелет профиля — понятия «со слов модели». Чтобы они опирались на источники, для каждой новой области в фоне ищутся минимум `profile_min_sources` источников от разных поставщиков…"
      },
      {
        "id": "learningBack/modules/knowledge/profile_store.py",
        "title": "profile_store.py",
        "path": "learningBack/modules/knowledge/profile_store.py",
        "summary": "Хранение и фоновое построение профиля навыка (T-0088): статусы, задача, правка и подтверждение."
      },
      {
        "id": "learningBack/modules/knowledge/provenance.py",
        "title": "provenance.py",
        "path": "learningBack/modules/knowledge/provenance.py",
        "summary": "Происхождение знаний: у каждого утверждения графа есть источник и статус проверки (T-0076). Понятие и связь, внесённые автоматически из документа, помечены «черновик» (`status = draft`) и хранят ссылки на фрагменты документа, из которых выведены. Подтверждает их человек —…"
      },
      {
        "id": "learningBack/modules/knowledge/provenance_api.py",
        "title": "provenance_api.py",
        "path": "learningBack/modules/knowledge/provenance_api.py",
        "summary": "Админский API происхождения знаний (T-0076, R-0045): источники, проверка, удаление источника. Всё здесь только для администратора: учащийся не получает ни документов, ни ссылок, ни текстов фрагментов. Статус «черновик» или «проверено» он видит в курсе, но не отсюда."
      },
      {
        "id": "learningBack/modules/knowledge/reconcile.py",
        "title": "reconcile.py",
        "path": "learningBack/modules/knowledge/reconcile.py",
        "summary": "Сверка новых утверждений с узлом и пул проблем (R-0074, T-0157, T-0158, T-0165). Правило узла — в нём нет расхождений. Один запрос к модели на узел на пачку добавлений: принятые утверждения с номерами и добавляемые рядом. По каждому добавляемому — «совпадает с №», «нейтрально»…"
      },
      {
        "id": "learningBack/modules/knowledge/review.py",
        "title": "review.py",
        "path": "learningBack/modules/knowledge/review.py",
        "summary": "Специалисты по областям и очередь проверки черновиков (T-0081, R-0046). Подтверждать и править знания графа могут администраторы и специалисты. Специалист назначается администратором на конкретные области, а не на всю систему: видит очередь, источники и действует только внутри…"
      },
      {
        "id": "learningBack/modules/knowledge/review_api.py",
        "title": "review_api.py",
        "path": "learningBack/modules/knowledge/review_api.py",
        "summary": "API специалистов и очереди проверки (T-0081, R-0046). Назначать специалистов может только администратор. Очередь, источники понятий и решения доступны администратору и специалисту в его областях; учащемуся — ничего из этого."
      },
      {
        "id": "learningBack/modules/knowledge/skill_profile.py",
        "title": "skill_profile.py",
        "path": "learningBack/modules/knowledge/skill_profile.py",
        "summary": "Профиль навыка: полное описание того, что нужно знать для цели (T-0088, R-0048). Одним запросом на восемь понятий полный граф не получить. Поэтому сперва модель набрасывает контур: из каких областей состоит навык, как они зависят друг от друга и из каких этапов состоит каждая;…"
      },
      {
        "id": "learningBack/modules/knowledge/source_search.py",
        "title": "source_search.py",
        "path": "learningBack/modules/knowledge/source_search.py",
        "summary": "Поиск источников для графа: белый список каталогов и веб-поиск (T-0082, A-0027, A-0028, R-0043). Что не хватает в графе, ищется сначала в каталогах открытых источников (Wikibooks, arXiv), потом через API веб-поиска — и только среди разрешённых доменов. Решение владельца: берём,…"
      },
      {
        "id": "learningBack/modules/knowledge/stages.py",
        "title": "stages.py",
        "path": "learningBack/modules/knowledge/stages.py",
        "summary": "Этапы и уровни понятий (T-0087, A-0030): метки, которыми профиль навыка раскладывает граф. Этап — название и порядковый номер группы понятий («Определители», 4); уровень — basic, middle или advanced; «необязательное» — ветвь для знакомства, без которой цель достижима. Всё это…"
      },
      {
        "id": "learningBack/modules/knowledge/subjects_api.py",
        "title": "subjects_api.py",
        "path": "learningBack/modules/knowledge/subjects_api.py",
        "summary": "Моя библиотека: предметы человека со статусом (T-0119, R-0062)."
      },
      {
        "id": "learningBack/modules/knowledge/templates/graph.html",
        "title": "graph.html",
        "path": "learningBack/modules/knowledge/templates/graph.html",
        "summary": "Модуль graph."
      },
      {
        "id": "learningBack/modules/knowledge/theory.py",
        "title": "theory.py",
        "path": "learningBack/modules/knowledge/theory.py",
        "summary": "Теория понятия по требованию (T-0121, R-0064). Скелет графа хранит у понятия только короткое пояснение. Когда человек открывает шаг курса, а в понятии нет разделов теории, здесь строятся разделы под уровень понятия и сохраняются в `content` (версия растёт, кэш заданий по старой…"
      },
      {
        "id": "learningBack/scripts/backup_objects.py",
        "title": "backup_objects.py",
        "path": "learningBack/scripts/backup_objects.py",
        "summary": "Резервная копия объектного хранилища источников (T-0073): копия и проверка. uv run python -m scripts.backup_objects [каталог] # снять копию (по умолчанию .data/backups) uv run python -m scripts.backup_objects --verify [каталог] # сверить последнюю копию с хранилищем Копия —…"
      },
      {
        "id": "learningBack/scripts/ingest_document.py",
        "title": "ingest_document.py",
        "path": "learningBack/scripts/ingest_document.py",
        "summary": "Загрузить документ в источники и разобрать его в граф (T-0077): ручной запуск для администратора. uv run python -m scripts.ingest_document книга.pdf --domain algebra [--title \"Algebra 1\"] [--level B2] Файл сохраняется в объектное хранилище, разбирается в понятия со ссылками на…"
      },
      {
        "id": "learningBack/scripts/merge_concepts.py",
        "title": "merge_concepts.py",
        "path": "learningBack/scripts/merge_concepts.py",
        "summary": "Слить дубли понятий в области (T-0078): ручной запуск для администратора. uv run python -m scripts.merge_concepts <область> [--max-judgements 50] Эмбеддинги отбирают кандидатов, модель решает по каждой паре; решения запоминаются, повторный запуск по той же области почти ничего…"
      },
      {
        "id": "learningBack/scripts/refresh_knowledge.py",
        "title": "refresh_knowledge.py",
        "path": "learningBack/scripts/refresh_knowledge.py",
        "summary": "Плановое обслуживание графа знаний: просроченные утверждения и проверка ссылок (T-0163, T-0164). Запускать по расписанию (cron, планировщик): ставит в очередь две задачи, дальше их берёт обычный воркер. uv run python -m scripts.refresh_knowledge --user admin@example.com"
      },
      {
        "id": "learningBack/scripts/run_textbooks.py",
        "title": "run_textbooks.py",
        "path": "learningBack/scripts/run_textbooks.py",
        "summary": "Прогон нескольких учебников через весь конвейер знаний: от файла до собранных узлов. uv run python -m scripts.run_textbooks книги/ --domain probability --license cc-by --user admin@example.com Для каждого файла: приём (лицензия, язык, воронка отсева, уровень доверия) →…"
      },
      {
        "id": "learningBack/tests/kg_helpers.py",
        "title": "kg_helpers.py",
        "path": "learningBack/tests/kg_helpers.py",
        "summary": "Общие заготовки для проверок конвейера знаний V-0130…V-0139: документы, фрагменты, утверждения."
      },
      {
        "id": "learningBack/tests/test_backup_objects.py",
        "title": "test_backup_objects.py",
        "path": "learningBack/tests/test_backup_objects.py",
        "summary": "Резервная копия объектного хранилища: копия сверяется с манифестом (T-0073)."
      },
      {
        "id": "learningBack/tests/test_gap_search.py",
        "title": "test_gap_search.py",
        "path": "learningBack/tests/test_gap_search.py",
        "summary": "В мире test_chain_placement добавлена опорная область «deep» без понятий под «mid»."
      },
      {
        "id": "learningBack/tests/test_graph_admin.py",
        "title": "test_graph_admin.py",
        "path": "learningBack/tests/test_graph_admin.py",
        "summary": "Схема графа канона в админке: чтение и правки без циклов и дублей (T-0107…T-0110, R-0058)."
      },
      {
        "id": "learningBack/tests/test_graph_extensions.py",
        "title": "test_graph_extensions.py",
        "path": "learningBack/tests/test_graph_extensions.py",
        "summary": "Apache AGE и pgvector в базе (T-0072, A-0024, A-0026)."
      },
      {
        "id": "learningBack/tests/test_ingest.py",
        "title": "test_ingest.py",
        "path": "learningBack/tests/test_ingest.py",
        "summary": "Разбор документа в понятия со ссылками на фрагмент (T-0077)."
      },
      {
        "id": "learningBack/tests/test_merge.py",
        "title": "test_merge.py",
        "path": "learningBack/tests/test_merge.py",
        "summary": "Слияние понятий: близость по векторам и решение модели (T-0078)."
      },
      {
        "id": "learningBack/tests/test_migrations_match_models.py",
        "title": "test_migrations_match_models.py",
        "path": "learningBack/tests/test_migrations_match_models.py",
        "summary": "Миграции дают ту же схему, что и модели: тесты строят базу из моделей, а продакшен — из миграций. Расхождение здесь тихое: все тесты зелёные, а на настоящей базе вставка падает. Так случилось с таблицами происхождения (T-0076): у `id` в миграции не было `gen_random_uuid()`."
      },
      {
        "id": "learningBack/tests/test_notifications.py",
        "title": "test_notifications.py",
        "path": "learningBack/tests/test_notifications.py",
        "summary": "Уведомления «курс готов» и «курс дополнен» с пометкой о черновике (T-0083)."
      },
      {
        "id": "learningBack/tests/test_notifications_review.py",
        "title": "test_notifications_review.py",
        "path": "learningBack/tests/test_notifications_review.py",
        "summary": "Уведомления «понятие проверено» и «правка изменила смысл пройденного» (T-0085, R-0044)."
      },
      {
        "id": "learningBack/tests/test_objects.py",
        "title": "test_objects.py",
        "path": "learningBack/tests/test_objects.py",
        "summary": "Объектное хранилище источников: контракт и подписанные ссылки (T-0073, A-0025)."
      },
      {
        "id": "learningBack/tests/test_prior_report.py",
        "title": "test_prior_report.py",
        "path": "learningBack/tests/test_prior_report.py",
        "summary": "Отчёт по предварительным знаниям: хватает / мало / нет / не проверено / нет в графе (T-0075)."
      },
      {
        "id": "learningBack/tests/test_profile_build.py",
        "title": "test_profile_build.py",
        "path": "learningBack/tests/test_profile_build.py",
        "summary": "Скелет графа из профиля навыка и онбординг (T-0090)."
      },
      {
        "id": "learningBack/tests/test_profile_coverage.py",
        "title": "test_profile_coverage.py",
        "path": "learningBack/tests/test_profile_coverage.py",
        "summary": "Отчёт полноты графа против профиля навыка (T-0099)."
      },
      {
        "id": "learningBack/tests/test_profile_fill.py",
        "title": "test_profile_fill.py",
        "path": "learningBack/tests/test_profile_fill.py",
        "summary": "Контур отдельно от наполнения: подтверждение, «уже владею», параллель, ход по областям, подхват (T-0101…T-0104)."
      },
      {
        "id": "learningBack/tests/test_profile_match.py",
        "title": "test_profile_match.py",
        "path": "learningBack/tests/test_profile_match.py",
        "summary": "Сопоставление профиля с графом по близости векторов (T-0096, A-0031)."
      },
      {
        "id": "learningBack/tests/test_profile_sources.py",
        "title": "test_profile_sources.py",
        "path": "learningBack/tests/test_profile_sources.py",
        "summary": "Автопоиск и разбор нескольких источников для новых областей профиля (T-0097)."
      },
      {
        "id": "learningBack/tests/test_profile_start.py",
        "title": "test_profile_start.py",
        "path": "learningBack/tests/test_profile_start.py",
        "summary": "Сборка графа в фоне после подтверждения цели: профиль и скелет одной задачей, ход виден из статуса."
      },
      {
        "id": "learningBack/tests/test_provenance.py",
        "title": "test_provenance.py",
        "path": "learningBack/tests/test_provenance.py",
        "summary": "Происхождение знаний: источники, статус черновика, проверка, удаление (T-0076)."
      },
      {
        "id": "learningBack/tests/test_push.py",
        "title": "test_push.py",
        "path": "learningBack/tests/test_push.py",
        "summary": "Push-уведомления о курсе вне приложения (T-0086, R-0044)."
      },
      {
        "id": "learningBack/tests/test_review.py",
        "title": "test_review.py",
        "path": "learningBack/tests/test_review.py",
        "summary": "Специалисты по областям и очередь проверки (T-0081, R-0046)."
      },
      {
        "id": "learningBack/tests/test_skill_profile.py",
        "title": "test_skill_profile.py",
        "path": "learningBack/tests/test_skill_profile.py",
        "summary": "Профиль навыка: чистка ответа модели, размер по уровню, фоновая задача, правка (T-0088)."
      },
      {
        "id": "learningBack/tests/test_source_search.py",
        "title": "test_source_search.py",
        "path": "learningBack/tests/test_source_search.py",
        "summary": "Поиск источников: белый список, лимиты, происхождение (T-0082)."
      },
      {
        "id": "learningBack/tests/test_source_upload.py",
        "title": "test_source_upload.py",
        "path": "learningBack/tests/test_source_upload.py",
        "summary": "Загрузка учебника администратором: форма, дубли, скан, прогресс (T-0079)."
      },
      {
        "id": "learningBack/tests/test_sources_admin_only.py",
        "title": "test_sources_admin_only.py",
        "path": "learningBack/tests/test_sources_admin_only.py",
        "summary": "Источники видят только администраторы: ни одного пути утечки к учащемуся (T-0080, R-0045). Не список проверенных ответов, а обход всех GET-маршрутов приложения: если завтра в чей-то ответ попадёт документ или текст фрагмента, тест упадёт, даже если про этот маршрут никто не…"
      },
      {
        "id": "learningBack/tests/test_stage_level.py",
        "title": "test_stage_level.py",
        "path": "learningBack/tests/test_stage_level.py",
        "summary": "Этапы, уровни и необязательность понятий (T-0087, A-0030)."
      },
      {
        "id": "learningBack/tests/test_v0130_claims_extraction.py",
        "title": "test_v0130_claims_extraction.py",
        "path": "learningBack/tests/test_v0130_claims_extraction.py",
        "summary": "Утверждения и ссылки на место: извлечение (V-0130, R-0071, T-0150). Живая часть проверки (20 случайных утверждений на пересобранном графе) остаётся за человеком."
      },
      {
        "id": "learningBack/tests/test_v0131_licenses_visibility.py",
        "title": "test_v0131_licenses_visibility.py",
        "path": "learningBack/tests/test_v0131_licenses_visibility.py",
        "summary": "Лицензии и видимость источников учащемуся (V-0131, R-0072, T-0152, T-0153). Ручная часть (ссылка в приложении открывает оригинал на нужной странице) остаётся за человеком."
      },
      {
        "id": "learningBack/tests/test_v0132_concept_in_two_areas.py",
        "title": "test_v0132_concept_in_two_areas.py",
        "path": "learningBack/tests/test_v0132_concept_in_two_areas.py",
        "summary": "Одно понятие в двух областях (V-0132, R-0073, T-0155)."
      },
      {
        "id": "learningBack/tests/test_v0133_reconcile_pool.py",
        "title": "test_v0133_reconcile_pool.py",
        "path": "learningBack/tests/test_v0133_reconcile_pool.py",
        "summary": "Сверка утверждений и пул проблем (V-0133, R-0074, T-0157, T-0158)."
      },
      {
        "id": "learningBack/tests/test_v0134_node_compile_offline.py",
        "title": "test_v0134_node_compile_offline.py",
        "path": "learningBack/tests/test_v0134_node_compile_offline.py",
        "summary": "Сборка узла и обучение без модели (V-0134, R-0075, T-0159, T-0160, T-0161)."
      },
      {
        "id": "learningBack/tests/test_v0135_freshness.py",
        "title": "test_v0135_freshness.py",
        "path": "learningBack/tests/test_v0135_freshness.py",
        "summary": "Срок актуальности и замена утверждений (V-0135, R-0076, T-0162, T-0163, T-0164)."
      },
      {
        "id": "learningBack/tests/test_v0136_consensus_fix.py",
        "title": "test_v0136_consensus_fix.py",
        "path": "learningBack/tests/test_v0136_consensus_fix.py",
        "summary": "Исправление консенсуса, жалобы, доверие и отзыв источника (V-0136, R-0077, T-0165…T-0167)."
      },
      {
        "id": "learningBack/tests/test_v0137_funnel.py",
        "title": "test_v0137_funnel.py",
        "path": "learningBack/tests/test_v0137_funnel.py",
        "summary": "Воронка отсева источников (V-0137, R-0078, T-0168…T-0170)."
      },
      {
        "id": "learningBack/tests/test_v0138_v0139_languages.py",
        "title": "test_v0138_v0139_languages.py",
        "path": "learningBack/tests/test_v0138_v0139_languages.py",
        "summary": "Многоязычный граф и разбор источников на двух языках (V-0138, V-0139; R-0079, R-0080)."
      },
      {
        "id": "learningBack/tests/test_v0140_server_messages.py",
        "title": "test_v0140_server_messages.py",
        "path": "learningBack/tests/test_v0140_server_messages.py",
        "summary": "Сервер говорит на языке пользователя: коды ошибок, уведомления, письма (V-0140, R-0081, T-0179)."
      },
      {
        "id": "learningFront/src/app/(tabs)/path.tsx",
        "title": "path.tsx",
        "path": "learningFront/src/app/(tabs)/path.tsx",
        "summary": "Вкладка «Путь»: шаги курса и карта знаний — два взгляда на один путь (R-0059, T-0111)."
      },
      {
        "id": "learningFront/src/app/(tabs)/progress.tsx",
        "title": "progress.tsx",
        "path": "learningFront/src/app/(tabs)/progress.tsx",
        "summary": "Компонент интерфейса progress."
      },
      {
        "id": "learningFront/src/app/curator.tsx",
        "title": "curator.tsx",
        "path": "learningFront/src/app/curator.tsx",
        "summary": "Раздел «Куратор» (R-0060, T-0112): служебные экраны администратора, отдельно от учебных вкладок."
      },
      {
        "id": "learningFront/src/app/library.tsx",
        "title": "library.tsx",
        "path": "learningFront/src/app/library.tsx",
        "summary": "Компонент интерфейса library."
      },
      {
        "id": "learningFront/src/app/problems.tsx",
        "title": "problems.tsx",
        "path": "learningFront/src/app/problems.tsx",
        "summary": "Компонент интерфейса problems."
      },
      {
        "id": "learningFront/src/app/skill-profile.tsx",
        "title": "skill-profile.tsx",
        "path": "learningFront/src/app/skill-profile.tsx",
        "summary": "Компонент интерфейса skill-profile."
      },
      {
        "id": "learningFront/src/app/sources.tsx",
        "title": "sources.tsx",
        "path": "learningFront/src/app/sources.tsx",
        "summary": "Компонент интерфейса sources."
      },
      {
        "id": "learningFront/src/entities/concept/ui/claim-sources.tsx",
        "title": "claim-sources.tsx",
        "path": "learningFront/src/entities/concept/ui/claim-sources.tsx",
        "summary": "Источники утверждений узла и «Здесь ошибка» (T-0154, T-0166, R-0072, R-0077). Под теорией: по нажатию — утверждения с названием источника, лицензией, страницей и ссылкой на оригинал. Цитата показывается, только если сервер её прислал (лицензия позволяет воспроизводить)."
      },
      {
        "id": "learningFront/src/entities/session/subject.test.ts",
        "title": "subject.test.ts",
        "path": "learningFront/src/entities/session/subject.test.ts",
        "summary": "Модуль subject.test."
      },
      {
        "id": "learningFront/src/features/claim-problems/index.ts",
        "title": "index.ts",
        "path": "learningFront/src/features/claim-problems/index.ts",
        "summary": "Модуль index."
      },
      {
        "id": "learningFront/src/features/claim-problems/ui/problem-pool.tsx",
        "title": "problem-pool.tsx",
        "path": "learningFront/src/features/claim-problems/ui/problem-pool.tsx",
        "summary": "Пул проблем для администратора (T-0158, R-0074): противоречия между утверждениями из разных источников и жалобы учащихся «здесь ошибка». Решение пересоберёт узел при следующей сборке области."
      },
      {
        "id": "learningFront/src/features/course/model/draft.test.ts",
        "title": "draft.test.ts",
        "path": "learningFront/src/features/course/model/draft.test.ts",
        "summary": "Модуль draft.test."
      },
      {
        "id": "learningFront/src/features/course/model/draft.ts",
        "title": "draft.ts",
        "path": "learningFront/src/features/course/model/draft.ts",
        "summary": "Статус проверки шагов курса (T-0076, R-0044): курс из черновика можно начинать, но человек должен знать, что он не проверен."
      },
      {
        "id": "learningFront/src/features/course/model/group-steps.ts",
        "title": "group-steps.ts",
        "path": "learningFront/src/features/course/model/group-steps.ts",
        "summary": "Путь курса по областям и этапам (R-0065, T-0122): порядок шагов не меняется, меняется только группировка."
      },
      {
        "id": "learningFront/src/features/course/model/notices.test.ts",
        "title": "notices.test.ts",
        "path": "learningFront/src/features/course/model/notices.test.ts",
        "summary": "Модуль notices.test."
      },
      {
        "id": "learningFront/src/features/course/model/notices.ts",
        "title": "notices.ts",
        "path": "learningFront/src/features/course/model/notices.ts",
        "summary": "Уведомления на экране курса (T-0083): какие показать и как подписать."
      },
      {
        "id": "learningFront/src/features/course/ui/path-accordion.tsx",
        "title": "path-accordion.tsx",
        "path": "learningFront/src/features/course/ui/path-accordion.tsx",
        "summary": "Аккордеон «Весь путь»: область → этап → шаги; свёрнутость запоминается на устройстве (R-0065, T-0122)."
      },
      {
        "id": "learningFront/src/features/goal-intake/model/steps.test.ts",
        "title": "steps.test.ts",
        "path": "learningFront/src/features/goal-intake/model/steps.test.ts",
        "summary": "Модуль steps.test."
      },
      {
        "id": "learningFront/src/features/goal-intake/model/steps.ts",
        "title": "steps.ts",
        "path": "learningFront/src/features/goal-intake/model/steps.ts",
        "summary": "Модуль steps."
      },
      {
        "id": "learningFront/src/features/goal-intake/ui/choice-chip.tsx",
        "title": "choice-chip.tsx",
        "path": "learningFront/src/features/goal-intake/ui/choice-chip.tsx",
        "summary": "Вариант выбора из списка (уровень цели): высота не меньше 44 px, состояние не только цветом."
      },
      {
        "id": "learningFront/src/features/goal-intake/ui/step-header.tsx",
        "title": "step-header.tsx",
        "path": "learningFront/src/features/goal-intake/ui/step-header.tsx",
        "summary": "Шапка шага онбординга: пять сегментов и метка «Шаг N из 5»."
      },
      {
        "id": "learningFront/src/features/goal-reached/index.ts",
        "title": "index.ts",
        "path": "learningFront/src/features/goal-reached/index.ts",
        "summary": "Модуль index."
      },
      {
        "id": "learningFront/src/features/goal-reached/ui/goal-reached-card.tsx",
        "title": "goal-reached-card.tsx",
        "path": "learningFront/src/features/goal-reached/ui/goal-reached-card.tsx",
        "summary": "«Цель достигнута» (T-0106, R-0057): три пути дальше — выше, шире или другое."
      },
      {
        "id": "learningFront/src/features/graph-editor/model/build-progress.test.ts",
        "title": "build-progress.test.ts",
        "path": "learningFront/src/features/graph-editor/model/build-progress.test.ts",
        "summary": "Модуль build-progress.test."
      },
      {
        "id": "learningFront/src/features/graph-editor/model/build-progress.ts",
        "title": "build-progress.ts",
        "path": "learningFront/src/features/graph-editor/model/build-progress.ts",
        "summary": "Что показать, пока граф собирается в фоне: по статусу профиля, без сети и без UI. Сборка идёт в две фазы (R-0055): быстрый контур, затем наполнение по областям."
      },
      {
        "id": "learningFront/src/features/graph-editor/model/keys.ts",
        "title": "keys.ts",
        "path": "learningFront/src/features/graph-editor/model/keys.ts",
        "summary": "Переход по понятиям стрелками клавиатуры (T-0144): влево — к предпосылке, вправо — к тому, что открывает, вверх и вниз — между понятиями одной колонки. Чистая функция над раскладкой, без UI."
      },
      {
        "id": "learningFront/src/features/graph-editor/model/legend.ts",
        "title": "legend.ts",
        "path": "learningFront/src/features/graph-editor/model/legend.ts",
        "summary": "Легенда схемы (R-0069, T-0135): строки собираются из того, что реально нарисовано, и показывают число. Один набор правил на встроенную схему, полноэкранный режим и «Дерево»; образцы рисует ui/scheme-legend.tsx."
      },
      {
        "id": "learningFront/src/features/graph-editor/model/offline.ts",
        "title": "offline.ts",
        "path": "learningFront/src/features/graph-editor/model/offline.ts",
        "summary": "Офлайн-чтение схемы и очередь правок личного слоя (T-0118, R-0061). Последний загруженный граф лежит в localStorage (веб) или в памяти; правки, не дошедшие до сервера, ждут в очереди и уходят при следующей загрузке."
      },
      {
        "id": "learningFront/src/features/graph-editor/model/overview.ts",
        "title": "overview.ts",
        "path": "learningFront/src/features/graph-editor/model/overview.ts",
        "summary": "Обзор схемы по этапам (R-0070, T-0142, T-0143): на крупном графе этапы — блоки, связи между ними — одна стрелка со счётчиком, этап раскрывается на месте, у выбранного понятия рисуются только его связи, а соседи из свёрнутых этапов показаны «призраками». Чистые функции над узлами…"
      },
      {
        "id": "learningFront/src/features/graph-editor/model/remember.ts",
        "title": "remember.ts",
        "path": "learningFront/src/features/graph-editor/model/remember.ts",
        "summary": "Модуль remember."
      },
      {
        "id": "learningFront/src/features/graph-editor/model/scheme.test.ts",
        "title": "scheme.test.ts",
        "path": "learningFront/src/features/graph-editor/model/scheme.test.ts",
        "summary": "Модуль scheme.test."
      },
      {
        "id": "learningFront/src/features/graph-editor/model/scheme.ts",
        "title": "scheme.ts",
        "path": "learningFront/src/features/graph-editor/model/scheme.ts",
        "summary": "Схема графа пути (T-0113…T-0117, R-0061): раскладка, состояния освоения, подписи, фильтры, подсветка пути. Чистая логика над данными графа и карты освоенности: без сети и без UI, поэтому покрыта тестами."
      },
      {
        "id": "learningFront/src/features/graph-editor/model/stage-groups.test.ts",
        "title": "stage-groups.test.ts",
        "path": "learningFront/src/features/graph-editor/model/stage-groups.test.ts",
        "summary": "Модуль stage-groups.test."
      },
      {
        "id": "learningFront/src/features/graph-editor/model/stage-groups.ts",
        "title": "stage-groups.ts",
        "path": "learningFront/src/features/graph-editor/model/stage-groups.ts",
        "summary": "Карта по этапам (T-0093): узлы с этапом группируются в порядке этапов, остальные идут отдельно."
      },
      {
        "id": "learningFront/src/features/graph-editor/ui/course-tree.tsx",
        "title": "course-tree.tsx",
        "path": "learningFront/src/features/graph-editor/ui/course-tree.tsx",
        "summary": "«Дерево» пути: шаги курса на холсте схемы (R-0066, T-0123): пройденное, текущее и закрытое — состояния схемы."
      },
      {
        "id": "learningFront/src/features/graph-editor/ui/graph-build-panel.tsx",
        "title": "graph-build-panel.tsx",
        "path": "learningFront/src/features/graph-editor/ui/graph-build-panel.tsx",
        "summary": "Сборка карты по подтверждённой цели: запуск, видимый ход и итог (R-0049, R-0055, R-0056). Сборка идёт на сервере в фоне; экран только спрашивает статус, поэтому его можно закрыть. Две фазы: быстрый контур (человек его проверяет) и наполнение по областям (ход виден по каждой)."
      },
      {
        "id": "learningFront/src/features/graph-editor/ui/mini-map.tsx",
        "title": "mini-map.tsx",
        "path": "learningFront/src/features/graph-editor/ui/mini-map.tsx",
        "summary": "Мини-карта большого графа (T-0147): вся схема уменьшенной, рамка — то, что сейчас в окне; нажатие переносит окно."
      },
      {
        "id": "learningFront/src/features/graph-editor/ui/node-plate.tsx",
        "title": "node-plate.tsx",
        "path": "learningFront/src/features/graph-editor/ui/node-plate.tsx",
        "summary": "Плашка выбранного понятия в полноэкранной схеме (T-0133, R-0068): название, область и этап, уровень, освоение, пояснение, соседи «нужно раньше» и «открывает», «Изучать» и действия для своего понятия. На телефоне — нижняя панель с двумя положениями (компактная и раскрытая), на…"
      },
      {
        "id": "learningFront/src/features/graph-editor/ui/scheme-canvas.tsx",
        "title": "scheme-canvas.tsx",
        "path": "learningFront/src/features/graph-editor/ui/scheme-canvas.tsx",
        "summary": "Холст схемы пути: заголовки этапов, рёбра ломаными, узлы. Один компонент на встроенную схему и на полноэкранный режим (T-0132, T-0134): оба рисуют одинаково, различаются размером окна и тем, что подсвечено. Без новых зависимостей: узлы и рёбра — View, прокрутка — ScrollView,…"
      },
      {
        "id": "learningFront/src/features/graph-editor/ui/scheme-fullscreen.tsx",
        "title": "scheme-fullscreen.tsx",
        "path": "learningFront/src/features/graph-editor/ui/scheme-fullscreen.tsx",
        "summary": "Схема пути во весь экран (T-0132, R-0068): слой поверх экрана с крупным холстом, масштабом и «Вписать», плашкой выбранного понятия (снизу на телефоне, сбоку на планшете и десктопе) и подсветкой только его связей. Закрывается кнопкой и Esc; выбранный узел остаётся выбранным и…"
      },
      {
        "id": "learningFront/src/features/graph-editor/ui/scheme-legend.tsx",
        "title": "scheme-legend.tsx",
        "path": "learningFront/src/features/graph-editor/ui/scheme-legend.tsx",
        "summary": "Легенда схемы (T-0114, T-0135…T-0137): образцы нарисованы теми же приёмами, что узлы и линии на холсте; строки и числа даёт model/legend.ts, поэтому легенда не расходится с рисунком. Сворачивается, выбор запоминается."
      },
      {
        "id": "learningFront/src/features/graph-editor/ui/scheme-view.tsx",
        "title": "scheme-view.tsx",
        "path": "learningFront/src/features/graph-editor/ui/scheme-view.tsx",
        "summary": "Схема графа пути (T-0113…T-0117, R-0061): узлы по этапам слева направо, рёбра-предпосылки, легенда, состояния освоения, поиск, фильтры, подсветка пути и карточка узла — без выхода со схемы. Без новых зависимостей: узлы и рёбра — обычные View, прокрутка и масштаб — ScrollView и…"
      },
      {
        "id": "learningFront/src/features/graph-editor/ui/stage-controls.tsx",
        "title": "stage-controls.tsx",
        "path": "learningFront/src/features/graph-editor/ui/stage-controls.tsx",
        "summary": "Управление обзором по этапам (R-0070): переключатель «Этапы / Всё», путь «Все этапы › Х» со сводкой, «Вся цепочка» и плашка со списком связей между двумя этапами. Одни и те же во встроенной схеме и во весь экран."
      },
      {
        "id": "learningFront/src/features/graph-editor/ui/stage-layer.tsx",
        "title": "stage-layer.tsx",
        "path": "learningFront/src/features/graph-editor/ui/stage-layer.tsx",
        "summary": "Слой обзора по этапам поверх холста схемы (R-0070, T-0142, T-0143): блоки свёрнутых этапов, заголовки раскрытых, стрелки-счётчики между этапами и плашка «ещё N» у призраков. Лежит в координатах схемы, как узлы и рёбра."
      },
      {
        "id": "learningFront/src/features/graph-editor/ui/use-scheme-scene.tsx",
        "title": "use-scheme-scene.tsx",
        "path": "learningFront/src/features/graph-editor/ui/use-scheme-scene.tsx",
        "summary": "Что рисуется на холсте схемы: обычная раскладка по этапам или обзор по этапам (R-0070, T-0142…T-0143). Один хук на встроенную схему и на полноэкранный режим: выбор вида, раскрытые этапы, «Вся цепочка» и список связей живут здесь, поэтому оба холста показывают одно и то же."
      },
      {
        "id": "learningFront/src/features/prior-test/index.ts",
        "title": "index.ts",
        "path": "learningFront/src/features/prior-test/index.ts",
        "summary": "Модуль index."
      },
      {
        "id": "learningFront/src/features/prior-test/model/report.test.ts",
        "title": "report.test.ts",
        "path": "learningFront/src/features/prior-test/model/report.test.ts",
        "summary": "Модуль report.test."
      },
      {
        "id": "learningFront/src/features/prior-test/model/report.ts",
        "title": "report.ts",
        "path": "learningFront/src/features/prior-test/model/report.ts",
        "summary": "Как показать отчёт по предварительным знаниям (T-0075, R-0042)."
      },
      {
        "id": "learningFront/src/features/prior-test/ui/prior-test-session.tsx",
        "title": "prior-test-session.tsx",
        "path": "learningFront/src/features/prior-test/ui/prior-test-session.tsx",
        "summary": "Проверка предварительных знаний (T-0075, R-0042): короткий тест по базовым областям цели сверху вниз и отчёт «хватает / мало / нет». Тест можно пропустить — курс тогда считает, что человек этого не знает."
      },
      {
        "id": "learningFront/src/features/push-settings/index.ts",
        "title": "index.ts",
        "path": "learningFront/src/features/push-settings/index.ts",
        "summary": "Модуль index."
      },
      {
        "id": "learningFront/src/features/push-settings/model/push-model.test.ts",
        "title": "push-model.test.ts",
        "path": "learningFront/src/features/push-settings/model/push-model.test.ts",
        "summary": "Модуль push-model.test."
      },
      {
        "id": "learningFront/src/features/push-settings/model/push-model.ts",
        "title": "push-model.ts",
        "path": "learningFront/src/features/push-settings/model/push-model.ts",
        "summary": "Настройка уведомлений вне приложения (T-0086): что показать и что делает кнопка. Без сети и без UI."
      },
      {
        "id": "learningFront/src/features/push-settings/ui/push-settings.tsx",
        "title": "push-settings.tsx",
        "path": "learningFront/src/features/push-settings/ui/push-settings.tsx",
        "summary": "Карточка «Уведомления» в профиле (T-0086): включить и отключить push о курсе."
      },
      {
        "id": "learningFront/src/features/skill-profile/index.ts",
        "title": "index.ts",
        "path": "learningFront/src/features/skill-profile/index.ts",
        "summary": "Модуль index."
      },
      {
        "id": "learningFront/src/features/skill-profile/model/profile-model.test.ts",
        "title": "profile-model.test.ts",
        "path": "learningFront/src/features/skill-profile/model/profile-model.test.ts",
        "summary": "Модуль profile-model.test."
      },
      {
        "id": "learningFront/src/features/skill-profile/model/profile-model.ts",
        "title": "profile-model.ts",
        "path": "learningFront/src/features/skill-profile/model/profile-model.ts",
        "summary": "Правка профиля навыка (T-0093): что показать и как менять, без сети и без UI."
      },
      {
        "id": "learningFront/src/features/skill-profile/ui/skill-profile-editor.tsx",
        "title": "skill-profile-editor.tsx",
        "path": "learningFront/src/features/skill-profile/ui/skill-profile-editor.tsx",
        "summary": "Профиль навыка (T-0093, R-0049): человек видит, что ему нужно знать для цели, правит и строит граф."
      },
      {
        "id": "learningFront/src/features/sources/index.ts",
        "title": "index.ts",
        "path": "learningFront/src/features/sources/index.ts",
        "summary": "Модуль index."
      },
      {
        "id": "learningFront/src/features/sources/model/gaps-model.test.ts",
        "title": "gaps-model.test.ts",
        "path": "learningFront/src/features/sources/model/gaps-model.test.ts",
        "summary": "Модуль gaps-model.test."
      },
      {
        "id": "learningFront/src/features/sources/model/gaps-model.ts",
        "title": "gaps-model.ts",
        "path": "learningFront/src/features/sources/model/gaps-model.ts",
        "summary": "Пробелы в графе (T-0084): подписи и расчёты без сети и без UI."
      },
      {
        "id": "learningFront/src/features/sources/model/sources-model.test.ts",
        "title": "sources-model.test.ts",
        "path": "learningFront/src/features/sources/model/sources-model.test.ts",
        "summary": "Модуль sources-model.test."
      },
      {
        "id": "learningFront/src/features/sources/model/sources-model.ts",
        "title": "sources-model.ts",
        "path": "learningFront/src/features/sources/model/sources-model.ts",
        "summary": "Источники знаний (T-0079): подписи и расчёты хода разбора без сети и без UI."
      },
      {
        "id": "learningFront/src/features/sources/ui/gaps-card.tsx",
        "title": "gaps-card.tsx",
        "path": "learningFront/src/features/sources/ui/gaps-card.tsx",
        "summary": "Пробелы в графе под целью (T-0084): администратор видит области без понятий, правит готовый запрос и одним действием запускает поиск по белому списку и разбор."
      },
      {
        "id": "learningFront/src/features/sources/ui/sources-panel.tsx",
        "title": "sources-panel.tsx",
        "path": "learningFront/src/features/sources/ui/sources-panel.tsx",
        "summary": "Панель источников для администратора (T-0079): форма загрузки учебника и список с ходом разбора."
      },
      {
        "id": "learningFront/src/pages/home/model/tiles-model.test.ts",
        "title": "tiles-model.test.ts",
        "path": "learningFront/src/pages/home/model/tiles-model.test.ts",
        "summary": "Модуль tiles-model.test."
      },
      {
        "id": "learningFront/src/pages/home/model/tiles-model.ts",
        "title": "tiles-model.ts",
        "path": "learningFront/src/pages/home/model/tiles-model.ts",
        "summary": "Порядок плашек «Сегодня»: чистая логика без UI."
      },
      {
        "id": "learningFront/src/pages/home/ui/state-hero.tsx",
        "title": "state-hero.tsx",
        "path": "learningFront/src/pages/home/ui/state-hero.tsx",
        "summary": "Главный блок «Сегодня» (макет: Сегодня · состояния): метка, заголовок, причина и одно-два действия. Один вид на все состояния предмета — приоритет решает next-action.ts, а не вёрстка."
      },
      {
        "id": "learningFront/src/pages/home/ui/today-tiles.tsx",
        "title": "today-tiles.tsx",
        "path": "learningFront/src/pages/home/ui/today-tiles.tsx",
        "summary": "Плашки «Сегодня» (T-0120, R-0063): самостоятельные мини-виджеты под главным действием дня. Видимость и порядок плашек запоминаются на устройстве (на телефоне — до закрытия приложения)."
      },
      {
        "id": "learningFront/src/pages/library/index.ts",
        "title": "index.ts",
        "path": "learningFront/src/pages/library/index.ts",
        "summary": "Модуль index."
      },
      {
        "id": "learningFront/src/pages/library/ui/library-screen.tsx",
        "title": "library-screen.tsx",
        "path": "learningFront/src/pages/library/ui/library-screen.tsx",
        "summary": "«Моя библиотека» (T-0119, R-0062): список предметов человека; открыть, поставить на паузу, удалить, добавить."
      },
      {
        "id": "learningFront/src/pages/problems/index.ts",
        "title": "index.ts",
        "path": "learningFront/src/pages/problems/index.ts",
        "summary": "Модуль index."
      },
      {
        "id": "learningFront/src/pages/problems/ui/problems-screen.tsx",
        "title": "problems-screen.tsx",
        "path": "learningFront/src/pages/problems/ui/problems-screen.tsx",
        "summary": "Пул проблем (T-0158): экран администратора. Учащийся его не видит, сервер отвечает 403."
      },
      {
        "id": "learningFront/src/pages/skill-profile/index.ts",
        "title": "index.ts",
        "path": "learningFront/src/pages/skill-profile/index.ts",
        "summary": "Модуль index."
      },
      {
        "id": "learningFront/src/pages/skill-profile/ui/skill-profile-screen.tsx",
        "title": "skill-profile-screen.tsx",
        "path": "learningFront/src/pages/skill-profile/ui/skill-profile-screen.tsx",
        "summary": "Профиль навыка (T-0093): экран над фичей; предмет берётся из сессии."
      },
      {
        "id": "learningFront/src/pages/sources/index.ts",
        "title": "index.ts",
        "path": "learningFront/src/pages/sources/index.ts",
        "summary": "Модуль index."
      },
      {
        "id": "learningFront/src/pages/sources/ui/sources-screen.tsx",
        "title": "sources-screen.tsx",
        "path": "learningFront/src/pages/sources/ui/sources-screen.tsx",
        "summary": "Источники знаний (T-0079): экран администратора. Учащийся его не видит и API не отдаёт."
      },
      {
        "id": "learningFront/src/shared/api/claims-api.ts",
        "title": "claims-api.ts",
        "path": "learningFront/src/shared/api/claims-api.ts",
        "summary": "Утверждения узла: источники для учащегося, жалоба «здесь ошибка» и пул проблем администратора (T-0154, T-0158, T-0166). Учащийся видит название, лицензию, место и ссылку; цитата приходит, только если лицензия позволяет её воспроизводить."
      },
      {
        "id": "learningFront/src/shared/api/error-text.ts",
        "title": "error-text.ts",
        "path": "learningFront/src/shared/api/error-text.ts",
        "summary": "Текст ошибки на языке человека: сервер присылает код и параметры, клиент выбирает фразу (R-0081, T-0179)."
      },
      {
        "id": "learningFront/src/shared/api/lang-api.ts",
        "title": "lang-api.ts",
        "path": "learningFront/src/shared/api/lang-api.ts",
        "summary": "Язык человека на сервере: язык интерфейса и язык изучения (T-0174, T-0179). Сервер по ним отдаёт теорию, названия, задания, уведомления и письма на нужном языке."
      },
      {
        "id": "learningFront/src/shared/api/notification-route.test.ts",
        "title": "notification-route.test.ts",
        "path": "learningFront/src/shared/api/notification-route.test.ts",
        "summary": "Модуль notification-route.test."
      },
      {
        "id": "learningFront/src/shared/api/notification-route.ts",
        "title": "notification-route.ts",
        "path": "learningFront/src/shared/api/notification-route.ts",
        "summary": "Куда вести человека по нажатию на уведомление (T-0111): по виду уведомления, а не всегда на «Сегодня»."
      },
      {
        "id": "learningFront/src/shared/api/notifications-api.ts",
        "title": "notifications-api.ts",
        "path": "learningFront/src/shared/api/notifications-api.ts",
        "summary": "Уведомления о курсе (T-0083): «курс готов» и «курс дополнен» с пометкой о непроверенном."
      },
      {
        "id": "learningFront/src/shared/api/prior-test-api.ts",
        "title": "prior-test-api.ts",
        "path": "learningFront/src/shared/api/prior-test-api.ts",
        "summary": "Проверка предварительных знаний по базовым областям цели (T-0075, R-0042)."
      },
      {
        "id": "learningFront/src/shared/api/push-api.ts",
        "title": "push-api.ts",
        "path": "learningFront/src/shared/api/push-api.ts",
        "summary": "Push-уведомления о курсе вне приложения (T-0086, R-0044): устройства и настройка."
      },
      {
        "id": "learningFront/src/shared/api/push-device.ts",
        "title": "push-device.ts",
        "path": "learningFront/src/shared/api/push-device.ts",
        "summary": "Токен устройства для push (native): разрешение, получение токена Expo и его запоминание, чтобы при выходе из аккаунта сообщить серверу «этому телефону больше не слать». Web-вариант — push-device.web.ts."
      },
      {
        "id": "learningFront/src/shared/api/push-device.web.ts",
        "title": "push-device.web.ts",
        "path": "learningFront/src/shared/api/push-device.web.ts",
        "summary": "Web: push через Expo не поддерживается; функции-заглушки с тем же интерфейсом."
      },
      {
        "id": "learningFront/src/shared/api/skill-profile-api.ts",
        "title": "skill-profile-api.ts",
        "path": "learningFront/src/shared/api/skill-profile-api.ts",
        "summary": "Профиль навыка (T-0095, T-0090, T-0099): что нужно знать для цели, правка человеком, построение графа."
      },
      {
        "id": "learningFront/src/shared/api/sources-api.ts",
        "title": "sources-api.ts",
        "path": "learningFront/src/shared/api/sources-api.ts",
        "summary": "Источники знаний для администратора (T-0079, R-0047): загрузка учебника и ход разбора. Только для админа: учащийся ни документов, ни ссылок не получает (R-0045)."
      },
      {
        "id": "learningFront/src/shared/api/subjects-api.ts",
        "title": "subjects-api.ts",
        "path": "learningFront/src/shared/api/subjects-api.ts",
        "summary": "Моя библиотека: предметы человека со статусом (T-0119, R-0062)."
      },
      {
        "id": "learningFront/src/shared/config/design.test.ts",
        "title": "design.test.ts",
        "path": "learningFront/src/shared/config/design.test.ts",
        "summary": "Модуль design.test."
      },
      {
        "id": "learningFront/src/shared/engine/quiz/quiz.ts",
        "title": "quiz.ts",
        "path": "learningFront/src/shared/engine/quiz/quiz.ts",
        "summary": "Вопросы с проверкой ответа: общая часть дриллов чтения и аудирования (R-0022). Проверка детерминирована и считается без сети."
      },
      {
        "id": "learningFront/src/shared/i18n/core.ts",
        "title": "core.ts",
        "path": "learningFront/src/shared/i18n/core.ts",
        "summary": "Ядро интернационализации (R-0081, T-0177): языки интерфейса, выбор по языку устройства, подстановка параметров и множественное число по правилам языка. Чистая логика без react-native — проверяется тестами."
      },
      {
        "id": "learningFront/src/shared/i18n/en.ts",
        "title": "en.ts",
        "path": "learningFront/src/shared/i18n/en.ts",
        "summary": "English dictionary: main interface language. Must contain every key of ru.ts (checked by the type system)."
      },
      {
        "id": "learningFront/src/shared/i18n/i18n-context.tsx",
        "title": "i18n-context.tsx",
        "path": "learningFront/src/shared/i18n/i18n-context.tsx",
        "summary": "Язык интерфейса: провайдер и хук. Выбор человека запоминается на устройстве; пока его нет — язык устройства, иначе английский (R-0081, T-0178). Состояние для кода вне React — в translate.ts."
      },
      {
        "id": "learningFront/src/shared/i18n/i18n.test.ts",
        "title": "i18n.test.ts",
        "path": "learningFront/src/shared/i18n/i18n.test.ts",
        "summary": "Интерфейс на двух языках (V-0140, R-0081, T-0177…T-0179): словари совпадают, множественное число верно, ошибка сервера показывается фразой нужного языка по коду."
      },
      {
        "id": "learningFront/src/shared/i18n/index.ts",
        "title": "index.ts",
        "path": "learningFront/src/shared/i18n/index.ts",
        "summary": "Публичный API shared/i18n."
      },
      {
        "id": "learningFront/src/shared/i18n/lang-storage.ts",
        "title": "lang-storage.ts",
        "path": "learningFront/src/shared/i18n/lang-storage.ts",
        "summary": "Хранение выбранного языка интерфейса (native). Web-вариант — lang-storage.web.ts."
      },
      {
        "id": "learningFront/src/shared/i18n/lang-storage.web.ts",
        "title": "lang-storage.web.ts",
        "path": "learningFront/src/shared/i18n/lang-storage.web.ts",
        "summary": "Хранение выбранного языка интерфейса (web): localStorage."
      },
      {
        "id": "learningFront/src/shared/i18n/ru.ts",
        "title": "ru.ts",
        "path": "learningFront/src/shared/i18n/ru.ts",
        "summary": "Русский словарь интерфейса. Ключи этого файла — источник правды: английский словарь обязан иметь те же (en.ts типизирован по ним), поэтому незаведённый перевод ловит проверка типов."
      },
      {
        "id": "learningFront/src/shared/i18n/translate.ts",
        "title": "translate.ts",
        "path": "learningFront/src/shared/i18n/translate.ts",
        "summary": "Перевод без React: язык и словари живут здесь, чтобы чистая логика (модели) и тесты не тянули ни React, ни expo."
      },
      {
        "id": "learningFront/src/shared/lib/remember.ts",
        "title": "remember.ts",
        "path": "learningFront/src/shared/lib/remember.ts",
        "summary": "Запоминание мелких настроек вида (свёрнута ли легенда). Хранилище — localStorage на вебе; там, где его нет (телефон), настройка живёт до закрытия приложения. Любой сбой хранилища не должен ломать экран."
      },
      {
        "id": "learningFront/src/shared/ui/area-progress.tsx",
        "title": "area-progress.tsx",
        "path": "learningFront/src/shared/ui/area-progress.tsx",
        "summary": "Ход сборки по областям: у каждой свой статус «ждёт / в работе / готово / не вышло» (R-0056, S-07)."
      },
      {
        "id": "learningFront/src/shared/ui/backdrop.ts",
        "title": "backdrop.ts",
        "path": "learningFront/src/shared/ui/backdrop.ts",
        "summary": "Подложка страницы из эталона дизайна (D-0002, поверхность `backdrop.page`, T-0148): два мягких пятна поверх фона. Нативные стеки консоль эти значения не выгружает, поэтому доли и роли продублированы здесь; в макете — те же."
      },
      {
        "id": "learningFront/src/shared/ui/color.ts",
        "title": "color.ts",
        "path": "learningFront/src/shared/ui/color.ts",
        "summary": "Операции над цветом `#RRGGBB`: в React Native нет color-mix, поэтому смешиваем сами."
      },
      {
        "id": "learningFront/src/shared/ui/control-size.ts",
        "title": "control-size.ts",
        "path": "learningFront/src/shared/ui/control-size.ts",
        "summary": "Размеры контролов (D-0003, T-0139): основной «md» и малый «sm» для плотных блоков. Малый — компактный по виду, но зона нажатия остаётся не меньше 44 px за счёт hitSlop."
      },
      {
        "id": "learningFront/src/shared/ui/elevation.ts",
        "title": "elevation.ts",
        "path": "learningFront/src/shared/ui/elevation.ts",
        "summary": "Тень блока по токену elevation.card (D-0001 1.9.0): второй слой — основная мягкая тень. React Native держит одну тень на view, поэтому берём крупный слой; цвет — роль shadow темы."
      },
      {
        "id": "learningFront/src/shared/ui/nav-layout.test.ts",
        "title": "nav-layout.test.ts",
        "path": "learningFront/src/shared/ui/nav-layout.test.ts",
        "summary": "Модуль nav-layout.test."
      },
      {
        "id": "learningFront/src/shared/ui/nav-layout.ts",
        "title": "nav-layout.ts",
        "path": "learningFront/src/shared/ui/nav-layout.ts",
        "summary": "Раскладка навигации по ширине окна: чистая логика без react-native, чтобы проверяться тестами. Макет: телефон — вкладки внизу, планшет — рейка слева, десктоп — боковая панель."
      },
      {
        "id": "learningFront/src/shared/ui/theme-mode.test.ts",
        "title": "theme-mode.test.ts",
        "path": "learningFront/src/shared/ui/theme-mode.test.ts",
        "summary": "Модуль theme-mode.test."
      },
      {
        "id": "learningFront/src/shared/ui/theme-mode.ts",
        "title": "theme-mode.ts",
        "path": "learningFront/src/shared/ui/theme-mode.ts",
        "summary": "Выбор темы: чистая логика без react-native, чтобы проверяться тестами."
      },
      {
        "id": "learningFront/src/test-setup.ts",
        "title": "test-setup.ts",
        "path": "learningFront/src/test-setup.ts",
        "summary": "Тесты: test-setup."
      },
      {
        "id": "learningFront/src/widgets/app-nav/index.ts",
        "title": "index.ts",
        "path": "learningFront/src/widgets/app-nav/index.ts",
        "summary": "Модуль index."
      },
      {
        "id": "learningFront/src/widgets/app-nav/ui/app-nav.tsx",
        "title": "app-nav.tsx",
        "path": "learningFront/src/widgets/app-nav/ui/app-nav.tsx",
        "summary": "Навигация приложения: вкладки внизу (телефон), рейка (планшет), боковая панель (десктоп). Стоит в общем каркасе после входа, а не внутри вкладок: библиотека, состав навыка, повторение и служебные экраны живут вне (tabs), но навигацию терять не должны. Вход и онбординг её не…"
      },
      {
        "id": "learningFront/src/widgets/module-registry/recall-payload.test.ts",
        "title": "recall-payload.test.ts",
        "path": "learningFront/src/widgets/module-registry/recall-payload.test.ts",
        "summary": "Модуль recall-payload.test."
      },
      {
        "id": "learningFront/src/widgets/module-registry/recall-payload.ts",
        "title": "recall-payload.ts",
        "path": "learningFront/src/widgets/module-registry/recall-payload.ts",
        "summary": "Какое задание на вспоминание показывать: чистая логика без импортов, чтобы её проверял vitest."
      },
      {
        "id": "learningFront/src/widgets/module-registry/recall-renderer.tsx",
        "title": "recall-renderer.tsx",
        "path": "learningFront/src/widgets/module-registry/recall-renderer.tsx",
        "summary": "`concept_recall` показывают два разных задания: самостоятельное (вопрос в `payload.prompt`, оценка заданием `grade_concept`) и шаг курса (вопрос и критерии в `payload.item`, оценка идёт через `answerStep` и двигает освоенность и курс). Раньше шаг курса попадал на первый экран и…"
      },
      {
        "id": "learningFront/src/widgets/subject-bar/index.tsx",
        "title": "index.tsx",
        "path": "learningFront/src/widgets/subject-bar/index.tsx",
        "summary": "Шапка вкладок: какой предмет открыт и вход в «Мою библиотеку» (T-0111, R-0059, R-0062)."
      },
      {
        "id": "scripts/backup-offsite.sh",
        "title": "backup-offsite.sh",
        "path": "scripts/backup-offsite.sh",
        "summary": "Вынос свежих копий базы и объектов за пределы сервера (T-0031). Запуск на сервере из cron после backup-db.sh: OFFSITE_TARGET=user@backup-host:/srv/praxis-backups scripts/backup-offsite.sh Копирует каталог .data/backups по rsync/SSH; ничего не удаляет на стороне получателя."
      },
      {
        "id": "scripts/bootstrap-server.sh",
        "title": "bootstrap-server.sh",
        "path": "scripts/bootstrap-server.sh",
        "summary": "Первичная подготовка сервера для staging (T-0031). Запуск с вашего компьютера, один раз: scripts/bootstrap-server.sh user@host git@github.com:ORG/learning.git [каталог_на_сервере] Ставит Docker (если нет), клонирует проект с сабмодулями, создаёт .env из .env.example и…"
      },
      {
        "id": "scripts/deploy-remote.sh",
        "title": "deploy-remote.sh",
        "path": "scripts/deploy-remote.sh",
        "summary": "Деплой staging на удалённый сервер по SSH (T-0031, R-0020). Запуск с вашего компьютера: scripts/deploy-remote.sh user@host [каталог_на_сервере] Каталог по умолчанию — ~/praxis. Что делает: проверяет, что локальный main слит и отправлен, заходит на сервер и запускает там…"
      }
    ],
    "imports": [
      {
        "from": "learningBack/api/routers/push.py",
        "to": "learningBack/core/__init__.py",
        "evidence": {
          "path": "learningBack/api/routers/push.py",
          "line": 9,
          "fragment": "from core import push"
        }
      },
      {
        "from": "learningBack/api/routers/push.py",
        "to": "learningBack/core/push.py",
        "evidence": {
          "path": "learningBack/api/routers/push.py",
          "line": 9,
          "fragment": "from core import push"
        }
      },
      {
        "from": "learningBack/api/routers/push.py",
        "to": "learningBack/core/deps.py",
        "evidence": {
          "path": "learningBack/api/routers/push.py",
          "line": 10,
          "fragment": "from core.deps import CurrentUser, SessionDep"
        }
      },
      {
        "from": "learningBack/core/embeddings.py",
        "to": "learningBack/core/ai_base.py",
        "evidence": {
          "path": "learningBack/core/embeddings.py",
          "line": 19,
          "fragment": "from core.ai_base import ProviderError"
        }
      },
      {
        "from": "learningBack/core/embeddings.py",
        "to": "learningBack/core/config.py",
        "evidence": {
          "path": "learningBack/core/embeddings.py",
          "line": 20,
          "fragment": "from core.config import settings"
        }
      },
      {
        "from": "learningBack/core/objects.py",
        "to": "learningBack/core/config.py",
        "evidence": {
          "path": "learningBack/core/objects.py",
          "line": 19,
          "fragment": "from core.config import settings"
        }
      },
      {
        "from": "learningBack/core/push.py",
        "to": "learningBack/core/config.py",
        "evidence": {
          "path": "learningBack/core/push.py",
          "line": 26,
          "fragment": "from core.config import settings"
        }
      },
      {
        "from": "learningBack/core/push.py",
        "to": "learningBack/core/models.py",
        "evidence": {
          "path": "learningBack/core/push.py",
          "line": 27,
          "fragment": "from core.models import Job, PushDevice"
        }
      },
      {
        "from": "learningBack/core/push.py",
        "to": "learningBack/core/jobs.py",
        "evidence": {
          "path": "learningBack/core/push.py",
          "line": 186,
          "fragment": "from core.jobs import process_job"
        }
      },
      {
        "from": "learningBack/modules/knowledge/areas.py",
        "to": "learningBack/modules/knowledge/models.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/areas.py",
          "line": 16,
          "fragment": "from modules.knowledge.models import Concept, ConceptArea"
        }
      },
      {
        "from": "learningBack/modules/knowledge/claims_api.py",
        "to": "learningBack/core/deps.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/claims_api.py",
          "line": 15,
          "fragment": "from core.deps import CurrentSuperuser, CurrentUser, SessionDep"
        }
      },
      {
        "from": "learningBack/modules/knowledge/claims_api.py",
        "to": "learningBack/modules/knowledge/__init__.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/claims_api.py",
          "line": 16,
          "fragment": "from modules.knowledge import freshness, funnel, langs, reconcile"
        }
      },
      {
        "from": "learningBack/modules/knowledge/claims_api.py",
        "to": "learningBack/modules/knowledge/freshness.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/claims_api.py",
          "line": 16,
          "fragment": "from modules.knowledge import freshness, funnel, langs, reconcile"
        }
      },
      {
        "from": "learningBack/modules/knowledge/claims_api.py",
        "to": "learningBack/modules/knowledge/funnel.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/claims_api.py",
          "line": 16,
          "fragment": "from modules.knowledge import freshness, funnel, langs, reconcile"
        }
      },
      {
        "from": "learningBack/modules/knowledge/claims_api.py",
        "to": "learningBack/modules/knowledge/langs.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/claims_api.py",
          "line": 16,
          "fragment": "from modules.knowledge import freshness, funnel, langs, reconcile"
        }
      },
      {
        "from": "learningBack/modules/knowledge/claims_api.py",
        "to": "learningBack/modules/knowledge/reconcile.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/claims_api.py",
          "line": 16,
          "fragment": "from modules.knowledge import freshness, funnel, langs, reconcile"
        }
      },
      {
        "from": "learningBack/modules/knowledge/claims_api.py",
        "to": "learningBack/modules/knowledge/models.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/claims_api.py",
          "line": 17,
          "fragment": "from modules.knowledge.models import ("
        }
      },
      {
        "from": "learningBack/modules/knowledge/freshness.py",
        "to": "learningBack/core/models.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/freshness.py",
          "line": 19,
          "fragment": "from core.models import Job"
        }
      },
      {
        "from": "learningBack/modules/knowledge/freshness.py",
        "to": "learningBack/modules/knowledge/__init__.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/freshness.py",
          "line": 20,
          "fragment": "from modules.knowledge import provenance"
        }
      },
      {
        "from": "learningBack/modules/knowledge/freshness.py",
        "to": "learningBack/modules/knowledge/provenance.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/freshness.py",
          "line": 20,
          "fragment": "from modules.knowledge import provenance"
        }
      },
      {
        "from": "learningBack/modules/knowledge/freshness.py",
        "to": "learningBack/modules/knowledge/models.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/freshness.py",
          "line": 21,
          "fragment": "from modules.knowledge.models import ("
        }
      },
      {
        "from": "learningBack/modules/knowledge/freshness.py",
        "to": "learningBack/modules/knowledge/profile_sources.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/freshness.py",
          "line": 81,
          "fragment": "from modules.knowledge import profile_sources"
        }
      },
      {
        "from": "learningBack/modules/knowledge/funnel.py",
        "to": "learningBack/core/config.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/funnel.py",
          "line": 19,
          "fragment": "from core.config import settings"
        }
      },
      {
        "from": "learningBack/modules/knowledge/funnel.py",
        "to": "learningBack/modules/knowledge/__init__.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/funnel.py",
          "line": 20,
          "fragment": "from modules.knowledge import langs"
        }
      },
      {
        "from": "learningBack/modules/knowledge/funnel.py",
        "to": "learningBack/modules/knowledge/langs.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/funnel.py",
          "line": 20,
          "fragment": "from modules.knowledge import langs"
        }
      },
      {
        "from": "learningBack/modules/knowledge/funnel.py",
        "to": "learningBack/modules/knowledge/models.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/funnel.py",
          "line": 21,
          "fragment": "from modules.knowledge.models import ("
        }
      },
      {
        "from": "learningBack/modules/knowledge/funnel.py",
        "to": "learningBack/core/embeddings.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/funnel.py",
          "line": 154,
          "fragment": "from core.embeddings import get_embedder"
        }
      },
      {
        "from": "learningBack/modules/knowledge/gap_search.py",
        "to": "learningBack/modules/knowledge/__init__.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/gap_search.py",
          "line": 17,
          "fragment": "from modules.knowledge import ingest, prior_report, source_search"
        }
      },
      {
        "from": "learningBack/modules/knowledge/gap_search.py",
        "to": "learningBack/modules/knowledge/ingest.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/gap_search.py",
          "line": 17,
          "fragment": "from modules.knowledge import ingest, prior_report, source_search"
        }
      },
      {
        "from": "learningBack/modules/knowledge/gap_search.py",
        "to": "learningBack/modules/knowledge/prior_report.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/gap_search.py",
          "line": 17,
          "fragment": "from modules.knowledge import ingest, prior_report, source_search"
        }
      },
      {
        "from": "learningBack/modules/knowledge/gap_search.py",
        "to": "learningBack/modules/knowledge/source_search.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/gap_search.py",
          "line": 17,
          "fragment": "from modules.knowledge import ingest, prior_report, source_search"
        }
      },
      {
        "from": "learningBack/modules/knowledge/gap_search.py",
        "to": "learningBack/modules/knowledge/models.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/gap_search.py",
          "line": 18,
          "fragment": "from modules.knowledge.models import SourceDocument"
        }
      },
      {
        "from": "learningBack/modules/knowledge/graph_admin.py",
        "to": "learningBack/core/db.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/graph_admin.py",
          "line": 20,
          "fragment": "from core.db import SessionLocal"
        }
      },
      {
        "from": "learningBack/modules/knowledge/graph_admin.py",
        "to": "learningBack/modules/knowledge/__init__.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/graph_admin.py",
          "line": 21,
          "fragment": "from modules.knowledge import graph_admin_data as data"
        }
      },
      {
        "from": "learningBack/modules/knowledge/graph_admin.py",
        "to": "learningBack/modules/knowledge/graph_admin_data.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/graph_admin.py",
          "line": 21,
          "fragment": "from modules.knowledge import graph_admin_data as data"
        }
      },
      {
        "from": "learningBack/modules/knowledge/graph_admin_data.py",
        "to": "learningBack/modules/knowledge/__init__.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/graph_admin_data.py",
          "line": 17,
          "fragment": "from modules.knowledge import domains, provenance, stages"
        }
      },
      {
        "from": "learningBack/modules/knowledge/graph_admin_data.py",
        "to": "learningBack/modules/knowledge/domains.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/graph_admin_data.py",
          "line": 17,
          "fragment": "from modules.knowledge import domains, provenance, stages"
        }
      },
      {
        "from": "learningBack/modules/knowledge/graph_admin_data.py",
        "to": "learningBack/modules/knowledge/provenance.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/graph_admin_data.py",
          "line": 17,
          "fragment": "from modules.knowledge import domains, provenance, stages"
        }
      },
      {
        "from": "learningBack/modules/knowledge/graph_admin_data.py",
        "to": "learningBack/modules/knowledge/stages.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/graph_admin_data.py",
          "line": 17,
          "fragment": "from modules.knowledge import domains, provenance, stages"
        }
      },
      {
        "from": "learningBack/modules/knowledge/graph_admin_data.py",
        "to": "learningBack/modules/knowledge/content.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/graph_admin_data.py",
          "line": 18,
          "fragment": "from modules.knowledge.content import NodeContent, coerce_content"
        }
      },
      {
        "from": "learningBack/modules/knowledge/graph_admin_data.py",
        "to": "learningBack/modules/knowledge/areas.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/graph_admin_data.py",
          "line": 19,
          "fragment": "from modules.knowledge.areas import area_concepts, in_area"
        }
      },
      {
        "from": "learningBack/modules/knowledge/graph_admin_data.py",
        "to": "learningBack/modules/knowledge/models.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/graph_admin_data.py",
          "line": 20,
          "fragment": "from modules.knowledge.models import Concept, ConceptEdge, ConceptLink, ConceptSource"
        }
      },
      {
        "from": "learningBack/modules/knowledge/ingest.py",
        "to": "learningBack/core/__init__.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/ingest.py",
          "line": 27,
          "fragment": "from core import materials"
        }
      },
      {
        "from": "learningBack/modules/knowledge/ingest.py",
        "to": "learningBack/core/materials.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/ingest.py",
          "line": 27,
          "fragment": "from core import materials"
        }
      },
      {
        "from": "learningBack/modules/knowledge/ingest.py",
        "to": "learningBack/core/config.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/ingest.py",
          "line": 28,
          "fragment": "from core.config import settings"
        }
      },
      {
        "from": "learningBack/modules/knowledge/ingest.py",
        "to": "learningBack/core/models.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/ingest.py",
          "line": 29,
          "fragment": "from core.models import Job"
        }
      },
      {
        "from": "learningBack/modules/knowledge/ingest.py",
        "to": "learningBack/core/objects.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/ingest.py",
          "line": 30,
          "fragment": "from core.objects import ObjectStore, get_store"
        }
      },
      {
        "from": "learningBack/modules/knowledge/ingest.py",
        "to": "learningBack/modules/knowledge/__init__.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/ingest.py",
          "line": 31,
          "fragment": "from modules.knowledge import funnel, langs, provenance"
        }
      },
      {
        "from": "learningBack/modules/knowledge/ingest.py",
        "to": "learningBack/modules/knowledge/funnel.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/ingest.py",
          "line": 31,
          "fragment": "from modules.knowledge import funnel, langs, provenance"
        }
      },
      {
        "from": "learningBack/modules/knowledge/ingest.py",
        "to": "learningBack/modules/knowledge/langs.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/ingest.py",
          "line": 31,
          "fragment": "from modules.knowledge import funnel, langs, provenance"
        }
      },
      {
        "from": "learningBack/modules/knowledge/ingest.py",
        "to": "learningBack/modules/knowledge/provenance.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/ingest.py",
          "line": 31,
          "fragment": "from modules.knowledge import funnel, langs, provenance"
        }
      },
      {
        "from": "learningBack/modules/knowledge/ingest.py",
        "to": "learningBack/modules/knowledge/models.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/ingest.py",
          "line": 32,
          "fragment": "from modules.knowledge.models import ("
        }
      },
      {
        "from": "learningBack/modules/knowledge/ingest.py",
        "to": "learningBack/modules/knowledge/merge.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/ingest.py",
          "line": 687,
          "fragment": "from modules.knowledge import merge, notifications"
        }
      },
      {
        "from": "learningBack/modules/knowledge/ingest.py",
        "to": "learningBack/modules/knowledge/notifications.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/ingest.py",
          "line": 687,
          "fragment": "from modules.knowledge import merge, notifications"
        }
      },
      {
        "from": "learningBack/modules/knowledge/langs.py",
        "to": "learningBack/core/config.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/langs.py",
          "line": 11,
          "fragment": "from core.config import settings"
        }
      },
      {
        "from": "learningBack/modules/knowledge/localize.py",
        "to": "learningBack/core/deps.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/localize.py",
          "line": 16,
          "fragment": "from core.deps import CurrentUser"
        }
      },
      {
        "from": "learningBack/modules/knowledge/localize.py",
        "to": "learningBack/modules/knowledge/__init__.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/localize.py",
          "line": 17,
          "fragment": "from modules.knowledge import langs"
        }
      },
      {
        "from": "learningBack/modules/knowledge/localize.py",
        "to": "learningBack/modules/knowledge/langs.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/localize.py",
          "line": 17,
          "fragment": "from modules.knowledge import langs"
        }
      },
      {
        "from": "learningBack/modules/knowledge/localize.py",
        "to": "learningBack/modules/knowledge/models.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/localize.py",
          "line": 18,
          "fragment": "from modules.knowledge.models import Concept, ConceptTerm"
        }
      },
      {
        "from": "learningBack/modules/knowledge/merge.py",
        "to": "learningBack/core/config.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/merge.py",
          "line": 25,
          "fragment": "from core.config import settings"
        }
      },
      {
        "from": "learningBack/modules/knowledge/merge.py",
        "to": "learningBack/core/embeddings.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/merge.py",
          "line": 26,
          "fragment": "from core.embeddings import Embedder, get_embedder"
        }
      },
      {
        "from": "learningBack/modules/knowledge/merge.py",
        "to": "learningBack/core/models.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/merge.py",
          "line": 27,
          "fragment": "from core.models import Job"
        }
      },
      {
        "from": "learningBack/modules/knowledge/merge.py",
        "to": "learningBack/modules/knowledge/__init__.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/merge.py",
          "line": 28,
          "fragment": "from modules.knowledge import provenance"
        }
      },
      {
        "from": "learningBack/modules/knowledge/merge.py",
        "to": "learningBack/modules/knowledge/provenance.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/merge.py",
          "line": 28,
          "fragment": "from modules.knowledge import provenance"
        }
      },
      {
        "from": "learningBack/modules/knowledge/merge.py",
        "to": "learningBack/modules/knowledge/areas.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/merge.py",
          "line": 29,
          "fragment": "from modules.knowledge.areas import in_area"
        }
      },
      {
        "from": "learningBack/modules/knowledge/merge.py",
        "to": "learningBack/modules/knowledge/models.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/merge.py",
          "line": 30,
          "fragment": "from modules.knowledge.models import ("
        }
      },
      {
        "from": "learningBack/modules/knowledge/merge.py",
        "to": "learningBack/modules/knowledge/reconcile.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/merge.py",
          "line": 568,
          "fragment": "from modules.knowledge import reconcile"
        }
      },
      {
        "from": "learningBack/modules/knowledge/node_compile.py",
        "to": "learningBack/core/models.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/node_compile.py",
          "line": 21,
          "fragment": "from core.models import Job, SrsCard"
        }
      },
      {
        "from": "learningBack/modules/knowledge/node_compile.py",
        "to": "learningBack/modules/knowledge/__init__.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/node_compile.py",
          "line": 22,
          "fragment": "from modules.knowledge import funnel, langs"
        }
      },
      {
        "from": "learningBack/modules/knowledge/node_compile.py",
        "to": "learningBack/modules/knowledge/funnel.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/node_compile.py",
          "line": 22,
          "fragment": "from modules.knowledge import funnel, langs"
        }
      },
      {
        "from": "learningBack/modules/knowledge/node_compile.py",
        "to": "learningBack/modules/knowledge/langs.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/node_compile.py",
          "line": 22,
          "fragment": "from modules.knowledge import funnel, langs"
        }
      },
      {
        "from": "learningBack/modules/knowledge/node_compile.py",
        "to": "learningBack/modules/knowledge/areas.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/node_compile.py",
          "line": 23,
          "fragment": "from modules.knowledge.areas import in_area"
        }
      },
      {
        "from": "learningBack/modules/knowledge/node_compile.py",
        "to": "learningBack/modules/knowledge/models.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/node_compile.py",
          "line": 24,
          "fragment": "from modules.knowledge.models import ("
        }
      },
      {
        "from": "learningBack/modules/knowledge/notifications.py",
        "to": "learningBack/core/__init__.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/notifications.py",
          "line": 17,
          "fragment": "from core import push"
        }
      },
      {
        "from": "learningBack/modules/knowledge/notifications.py",
        "to": "learningBack/core/push.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/notifications.py",
          "line": 17,
          "fragment": "from core import push"
        }
      },
      {
        "from": "learningBack/modules/knowledge/notifications.py",
        "to": "learningBack/core/messages.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/notifications.py",
          "line": 18,
          "fragment": "from core.messages import msg, user_lang"
        }
      },
      {
        "from": "learningBack/modules/knowledge/notifications.py",
        "to": "learningBack/core/models.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/notifications.py",
          "line": 19,
          "fragment": "from core.models import Activity, Job, User"
        }
      },
      {
        "from": "learningBack/modules/knowledge/notifications.py",
        "to": "learningBack/modules/knowledge/__init__.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/notifications.py",
          "line": 21,
          "fragment": "from modules.knowledge import provenance"
        }
      },
      {
        "from": "learningBack/modules/knowledge/notifications.py",
        "to": "learningBack/modules/knowledge/provenance.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/notifications.py",
          "line": 21,
          "fragment": "from modules.knowledge import provenance"
        }
      },
      {
        "from": "learningBack/modules/knowledge/notifications.py",
        "to": "learningBack/modules/knowledge/areas.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/notifications.py",
          "line": 22,
          "fragment": "from modules.knowledge.areas import in_area"
        }
      },
      {
        "from": "learningBack/modules/knowledge/notifications.py",
        "to": "learningBack/modules/knowledge/models.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/notifications.py",
          "line": 23,
          "fragment": "from modules.knowledge.models import Concept, Course, Notification"
        }
      },
      {
        "from": "learningBack/modules/knowledge/notifications_api.py",
        "to": "learningBack/core/deps.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/notifications_api.py",
          "line": 10,
          "fragment": "from core.deps import CurrentUser, SessionDep"
        }
      },
      {
        "from": "learningBack/modules/knowledge/notifications_api.py",
        "to": "learningBack/modules/knowledge/__init__.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/notifications_api.py",
          "line": 11,
          "fragment": "from modules.knowledge import notifications"
        }
      },
      {
        "from": "learningBack/modules/knowledge/notifications_api.py",
        "to": "learningBack/modules/knowledge/notifications.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/notifications_api.py",
          "line": 11,
          "fragment": "from modules.knowledge import notifications"
        }
      },
      {
        "from": "learningBack/modules/knowledge/prior_report.py",
        "to": "learningBack/modules/knowledge/__init__.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/prior_report.py",
          "line": 17,
          "fragment": "from modules.knowledge import chain_placement, domains, provenance"
        }
      },
      {
        "from": "learningBack/modules/knowledge/prior_report.py",
        "to": "learningBack/modules/knowledge/chain_placement.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/prior_report.py",
          "line": 17,
          "fragment": "from modules.knowledge import chain_placement, domains, provenance"
        }
      },
      {
        "from": "learningBack/modules/knowledge/prior_report.py",
        "to": "learningBack/modules/knowledge/domains.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/prior_report.py",
          "line": 17,
          "fragment": "from modules.knowledge import chain_placement, domains, provenance"
        }
      },
      {
        "from": "learningBack/modules/knowledge/prior_report.py",
        "to": "learningBack/modules/knowledge/provenance.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/prior_report.py",
          "line": 17,
          "fragment": "from modules.knowledge import chain_placement, domains, provenance"
        }
      },
      {
        "from": "learningBack/modules/knowledge/prior_report.py",
        "to": "learningBack/modules/knowledge/models.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/prior_report.py",
          "line": 19,
          "fragment": "from modules.knowledge.models import Concept, Domain"
        }
      },
      {
        "from": "learningBack/modules/knowledge/profile_api.py",
        "to": "learningBack/core/ai_gateway.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/profile_api.py",
          "line": 10,
          "fragment": "from core.ai_gateway import get_ai_gateway, has_llm"
        }
      },
      {
        "from": "learningBack/modules/knowledge/profile_api.py",
        "to": "learningBack/core/deps.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/profile_api.py",
          "line": 11,
          "fragment": "from core.deps import CurrentUser, SessionDep"
        }
      },
      {
        "from": "learningBack/modules/knowledge/profile_api.py",
        "to": "learningBack/modules/knowledge/__init__.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/profile_api.py",
          "line": 12,
          "fragment": "from modules.knowledge import profile_coverage, profile_store"
        }
      },
      {
        "from": "learningBack/modules/knowledge/profile_api.py",
        "to": "learningBack/modules/knowledge/profile_coverage.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/profile_api.py",
          "line": 12,
          "fragment": "from modules.knowledge import profile_coverage, profile_store"
        }
      },
      {
        "from": "learningBack/modules/knowledge/profile_api.py",
        "to": "learningBack/modules/knowledge/profile_store.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/profile_api.py",
          "line": 12,
          "fragment": "from modules.knowledge import profile_coverage, profile_store"
        }
      },
      {
        "from": "learningBack/modules/knowledge/profile_build.py",
        "to": "learningBack/modules/knowledge/__init__.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/profile_build.py",
          "line": 16,
          "fragment": "from modules.knowledge import cross_links, domains, profile_match, skill_profile, stages"
        }
      },
      {
        "from": "learningBack/modules/knowledge/profile_build.py",
        "to": "learningBack/modules/knowledge/cross_links.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/profile_build.py",
          "line": 16,
          "fragment": "from modules.knowledge import cross_links, domains, profile_match, skill_profile, stages"
        }
      },
      {
        "from": "learningBack/modules/knowledge/profile_build.py",
        "to": "learningBack/modules/knowledge/domains.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/profile_build.py",
          "line": 16,
          "fragment": "from modules.knowledge import cross_links, domains, profile_match, skill_profile, stages"
        }
      },
      {
        "from": "learningBack/modules/knowledge/profile_build.py",
        "to": "learningBack/modules/knowledge/profile_match.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/profile_build.py",
          "line": 16,
          "fragment": "from modules.knowledge import cross_links, domains, profile_match, skill_profile, stages"
        }
      },
      {
        "from": "learningBack/modules/knowledge/profile_build.py",
        "to": "learningBack/modules/knowledge/skill_profile.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/profile_build.py",
          "line": 16,
          "fragment": "from modules.knowledge import cross_links, domains, profile_match, skill_profile, stages"
        }
      },
      {
        "from": "learningBack/modules/knowledge/profile_build.py",
        "to": "learningBack/modules/knowledge/stages.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/profile_build.py",
          "line": 16,
          "fragment": "from modules.knowledge import cross_links, domains, profile_match, skill_profile, stages"
        }
      },
      {
        "from": "learningBack/modules/knowledge/profile_build.py",
        "to": "learningBack/modules/knowledge/centrality.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/profile_build.py",
          "line": 17,
          "fragment": "from modules.knowledge.centrality import recompute_centrality"
        }
      },
      {
        "from": "learningBack/modules/knowledge/profile_build.py",
        "to": "learningBack/modules/knowledge/models.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/profile_build.py",
          "line": 18,
          "fragment": "from modules.knowledge.models import Concept, ConceptEdge, Domain"
        }
      },
      {
        "from": "learningBack/modules/knowledge/profile_coverage.py",
        "to": "learningBack/modules/knowledge/__init__.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/profile_coverage.py",
          "line": 15,
          "fragment": "from modules.knowledge import domains, profile_match, provenance, skill_profile"
        }
      },
      {
        "from": "learningBack/modules/knowledge/profile_coverage.py",
        "to": "learningBack/modules/knowledge/domains.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/profile_coverage.py",
          "line": 15,
          "fragment": "from modules.knowledge import domains, profile_match, provenance, skill_profile"
        }
      },
      {
        "from": "learningBack/modules/knowledge/profile_coverage.py",
        "to": "learningBack/modules/knowledge/profile_match.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/profile_coverage.py",
          "line": 15,
          "fragment": "from modules.knowledge import domains, profile_match, provenance, skill_profile"
        }
      },
      {
        "from": "learningBack/modules/knowledge/profile_coverage.py",
        "to": "learningBack/modules/knowledge/provenance.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/profile_coverage.py",
          "line": 15,
          "fragment": "from modules.knowledge import domains, profile_match, provenance, skill_profile"
        }
      },
      {
        "from": "learningBack/modules/knowledge/profile_coverage.py",
        "to": "learningBack/modules/knowledge/skill_profile.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/profile_coverage.py",
          "line": 15,
          "fragment": "from modules.knowledge import domains, profile_match, provenance, skill_profile"
        }
      },
      {
        "from": "learningBack/modules/knowledge/profile_coverage.py",
        "to": "learningBack/modules/knowledge/models.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/profile_coverage.py",
          "line": 16,
          "fragment": "from modules.knowledge.models import Concept, ConceptSource, Domain, SkillProfile"
        }
      },
      {
        "from": "learningBack/modules/knowledge/profile_fill.py",
        "to": "learningBack/modules/knowledge/__init__.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/profile_fill.py",
          "line": 19,
          "fragment": "from modules.knowledge import goal_intake, profile_build, profile_match, skill_profile"
        }
      },
      {
        "from": "learningBack/modules/knowledge/profile_fill.py",
        "to": "learningBack/modules/knowledge/goal_intake.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/profile_fill.py",
          "line": 19,
          "fragment": "from modules.knowledge import goal_intake, profile_build, profile_match, skill_profile"
        }
      },
      {
        "from": "learningBack/modules/knowledge/profile_fill.py",
        "to": "learningBack/modules/knowledge/profile_build.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/profile_fill.py",
          "line": 19,
          "fragment": "from modules.knowledge import goal_intake, profile_build, profile_match, skill_profile"
        }
      },
      {
        "from": "learningBack/modules/knowledge/profile_fill.py",
        "to": "learningBack/modules/knowledge/profile_match.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/profile_fill.py",
          "line": 19,
          "fragment": "from modules.knowledge import goal_intake, profile_build, profile_match, skill_profile"
        }
      },
      {
        "from": "learningBack/modules/knowledge/profile_fill.py",
        "to": "learningBack/modules/knowledge/skill_profile.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/profile_fill.py",
          "line": 19,
          "fragment": "from modules.knowledge import goal_intake, profile_build, profile_match, skill_profile"
        }
      },
      {
        "from": "learningBack/modules/knowledge/profile_fill.py",
        "to": "learningBack/modules/knowledge/models.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/profile_fill.py",
          "line": 20,
          "fragment": "from modules.knowledge.models import SkillProfile"
        }
      },
      {
        "from": "learningBack/modules/knowledge/profile_match.py",
        "to": "learningBack/core/config.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/profile_match.py",
          "line": 22,
          "fragment": "from core.config import settings"
        }
      },
      {
        "from": "learningBack/modules/knowledge/profile_match.py",
        "to": "learningBack/core/ai_base.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/profile_match.py",
          "line": 23,
          "fragment": "from core.ai_base import ProviderError"
        }
      },
      {
        "from": "learningBack/modules/knowledge/profile_match.py",
        "to": "learningBack/core/embeddings.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/profile_match.py",
          "line": 24,
          "fragment": "from core.embeddings import Embedder, get_embedder"
        }
      },
      {
        "from": "learningBack/modules/knowledge/profile_match.py",
        "to": "learningBack/modules/knowledge/__init__.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/profile_match.py",
          "line": 25,
          "fragment": "from modules.knowledge import domains, merge, provenance"
        }
      },
      {
        "from": "learningBack/modules/knowledge/profile_match.py",
        "to": "learningBack/modules/knowledge/domains.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/profile_match.py",
          "line": 25,
          "fragment": "from modules.knowledge import domains, merge, provenance"
        }
      },
      {
        "from": "learningBack/modules/knowledge/profile_match.py",
        "to": "learningBack/modules/knowledge/merge.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/profile_match.py",
          "line": 25,
          "fragment": "from modules.knowledge import domains, merge, provenance"
        }
      },
      {
        "from": "learningBack/modules/knowledge/profile_match.py",
        "to": "learningBack/modules/knowledge/provenance.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/profile_match.py",
          "line": 25,
          "fragment": "from modules.knowledge import domains, merge, provenance"
        }
      },
      {
        "from": "learningBack/modules/knowledge/profile_match.py",
        "to": "learningBack/modules/knowledge/models.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/profile_match.py",
          "line": 26,
          "fragment": "from modules.knowledge.models import Concept, Domain, DomainAlias, DomainEmbedding"
        }
      },
      {
        "from": "learningBack/modules/knowledge/profile_sources.py",
        "to": "learningBack/core/config.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/profile_sources.py",
          "line": 19,
          "fragment": "from core.config import settings"
        }
      },
      {
        "from": "learningBack/modules/knowledge/profile_sources.py",
        "to": "learningBack/core/models.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/profile_sources.py",
          "line": 20,
          "fragment": "from core.models import Job"
        }
      },
      {
        "from": "learningBack/modules/knowledge/profile_sources.py",
        "to": "learningBack/modules/knowledge/__init__.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/profile_sources.py",
          "line": 21,
          "fragment": "from modules.knowledge import gap_search, source_search"
        }
      },
      {
        "from": "learningBack/modules/knowledge/profile_sources.py",
        "to": "learningBack/modules/knowledge/gap_search.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/profile_sources.py",
          "line": 21,
          "fragment": "from modules.knowledge import gap_search, source_search"
        }
      },
      {
        "from": "learningBack/modules/knowledge/profile_sources.py",
        "to": "learningBack/modules/knowledge/source_search.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/profile_sources.py",
          "line": 21,
          "fragment": "from modules.knowledge import gap_search, source_search"
        }
      },
      {
        "from": "learningBack/modules/knowledge/profile_sources.py",
        "to": "learningBack/modules/knowledge/models.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/profile_sources.py",
          "line": 22,
          "fragment": "from modules.knowledge.models import SourceDocument"
        }
      },
      {
        "from": "learningBack/modules/knowledge/profile_sources.py",
        "to": "learningBack/modules/knowledge/langs.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/profile_sources.py",
          "line": 66,
          "fragment": "from modules.knowledge import langs"
        }
      },
      {
        "from": "learningBack/modules/knowledge/profile_sources.py",
        "to": "learningBack/modules/knowledge/ingest.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/profile_sources.py",
          "line": 108,
          "fragment": "from modules.knowledge import ingest"
        }
      },
      {
        "from": "learningBack/modules/knowledge/profile_store.py",
        "to": "learningBack/core/ai_gateway.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/profile_store.py",
          "line": 14,
          "fragment": "from core.ai_gateway import get_ai_gateway, has_llm"
        }
      },
      {
        "from": "learningBack/modules/knowledge/profile_store.py",
        "to": "learningBack/core/config.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/profile_store.py",
          "line": 15,
          "fragment": "from core.config import settings"
        }
      },
      {
        "from": "learningBack/modules/knowledge/profile_store.py",
        "to": "learningBack/core/models.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/profile_store.py",
          "line": 16,
          "fragment": "from core.models import Job"
        }
      },
      {
        "from": "learningBack/modules/knowledge/profile_store.py",
        "to": "learningBack/modules/knowledge/__init__.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/profile_store.py",
          "line": 17,
          "fragment": "from modules.knowledge import ("
        }
      },
      {
        "from": "learningBack/modules/knowledge/profile_store.py",
        "to": "learningBack/modules/knowledge/models.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/profile_store.py",
          "line": 25,
          "fragment": "from modules.knowledge.models import SkillProfile"
        }
      },
      {
        "from": "learningBack/modules/knowledge/profile_store.py",
        "to": "learningBack/core/db.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/profile_store.py",
          "line": 238,
          "fragment": "from core.db import SessionLocal"
        }
      },
      {
        "from": "learningBack/modules/knowledge/profile_store.py",
        "to": "learningBack/core/jobs.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/profile_store.py",
          "line": 239,
          "fragment": "from core.jobs import process_job"
        }
      },
      {
        "from": "learningBack/modules/knowledge/provenance.py",
        "to": "learningBack/core/objects.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/provenance.py",
          "line": 22,
          "fragment": "from core.objects import ObjectStore, get_store"
        }
      },
      {
        "from": "learningBack/modules/knowledge/provenance.py",
        "to": "learningBack/modules/knowledge/models.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/provenance.py",
          "line": 23,
          "fragment": "from modules.knowledge.models import ("
        }
      },
      {
        "from": "learningBack/modules/knowledge/provenance.py",
        "to": "learningBack/modules/knowledge/__init__.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/provenance.py",
          "line": 242,
          "fragment": "from modules.knowledge import notifications"
        }
      },
      {
        "from": "learningBack/modules/knowledge/provenance.py",
        "to": "learningBack/modules/knowledge/notifications.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/provenance.py",
          "line": 242,
          "fragment": "from modules.knowledge import notifications"
        }
      },
      {
        "from": "learningBack/modules/knowledge/provenance_api.py",
        "to": "learningBack/core/config.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/provenance_api.py",
          "line": 14,
          "fragment": "from core.config import settings"
        }
      },
      {
        "from": "learningBack/modules/knowledge/provenance_api.py",
        "to": "learningBack/core/deps.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/provenance_api.py",
          "line": 15,
          "fragment": "from core.deps import CurrentSuperuser, CurrentUser, SessionDep"
        }
      },
      {
        "from": "learningBack/modules/knowledge/provenance_api.py",
        "to": "learningBack/core/materials.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/provenance_api.py",
          "line": 16,
          "fragment": "from core.materials import NothingToExtract, UnsupportedFile"
        }
      },
      {
        "from": "learningBack/modules/knowledge/provenance_api.py",
        "to": "learningBack/modules/knowledge/__init__.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/provenance_api.py",
          "line": 17,
          "fragment": "from modules.knowledge import gap_search, ingest, provenance, review, source_search"
        }
      },
      {
        "from": "learningBack/modules/knowledge/provenance_api.py",
        "to": "learningBack/modules/knowledge/gap_search.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/provenance_api.py",
          "line": 17,
          "fragment": "from modules.knowledge import gap_search, ingest, provenance, review, source_search"
        }
      },
      {
        "from": "learningBack/modules/knowledge/provenance_api.py",
        "to": "learningBack/modules/knowledge/ingest.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/provenance_api.py",
          "line": 17,
          "fragment": "from modules.knowledge import gap_search, ingest, provenance, review, source_search"
        }
      },
      {
        "from": "learningBack/modules/knowledge/provenance_api.py",
        "to": "learningBack/modules/knowledge/provenance.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/provenance_api.py",
          "line": 17,
          "fragment": "from modules.knowledge import gap_search, ingest, provenance, review, source_search"
        }
      },
      {
        "from": "learningBack/modules/knowledge/provenance_api.py",
        "to": "learningBack/modules/knowledge/review.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/provenance_api.py",
          "line": 17,
          "fragment": "from modules.knowledge import gap_search, ingest, provenance, review, source_search"
        }
      },
      {
        "from": "learningBack/modules/knowledge/provenance_api.py",
        "to": "learningBack/modules/knowledge/source_search.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/provenance_api.py",
          "line": 17,
          "fragment": "from modules.knowledge import gap_search, ingest, provenance, review, source_search"
        }
      },
      {
        "from": "learningBack/modules/knowledge/provenance_api.py",
        "to": "learningBack/modules/knowledge/models.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/provenance_api.py",
          "line": 18,
          "fragment": "from modules.knowledge.models import Concept, ConceptEdge, SourceDocument"
        }
      },
      {
        "from": "learningBack/modules/knowledge/reconcile.py",
        "to": "learningBack/core/config.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/reconcile.py",
          "line": 20,
          "fragment": "from core.config import settings"
        }
      },
      {
        "from": "learningBack/modules/knowledge/reconcile.py",
        "to": "learningBack/core/models.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/reconcile.py",
          "line": 21,
          "fragment": "from core.models import Job"
        }
      },
      {
        "from": "learningBack/modules/knowledge/reconcile.py",
        "to": "learningBack/modules/knowledge/__init__.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/reconcile.py",
          "line": 22,
          "fragment": "from modules.knowledge import freshness, funnel, provenance"
        }
      },
      {
        "from": "learningBack/modules/knowledge/reconcile.py",
        "to": "learningBack/modules/knowledge/freshness.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/reconcile.py",
          "line": 22,
          "fragment": "from modules.knowledge import freshness, funnel, provenance"
        }
      },
      {
        "from": "learningBack/modules/knowledge/reconcile.py",
        "to": "learningBack/modules/knowledge/funnel.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/reconcile.py",
          "line": 22,
          "fragment": "from modules.knowledge import freshness, funnel, provenance"
        }
      },
      {
        "from": "learningBack/modules/knowledge/reconcile.py",
        "to": "learningBack/modules/knowledge/provenance.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/reconcile.py",
          "line": 22,
          "fragment": "from modules.knowledge import freshness, funnel, provenance"
        }
      },
      {
        "from": "learningBack/modules/knowledge/reconcile.py",
        "to": "learningBack/modules/knowledge/models.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/reconcile.py",
          "line": 23,
          "fragment": "from modules.knowledge.models import ("
        }
      },
      {
        "from": "learningBack/modules/knowledge/reconcile.py",
        "to": "learningBack/modules/knowledge/node_compile.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/reconcile.py",
          "line": 405,
          "fragment": "from modules.knowledge import node_compile"
        }
      },
      {
        "from": "learningBack/modules/knowledge/review.py",
        "to": "learningBack/core/models.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/review.py",
          "line": 17,
          "fragment": "from core.models import User"
        }
      },
      {
        "from": "learningBack/modules/knowledge/review.py",
        "to": "learningBack/modules/knowledge/__init__.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/review.py",
          "line": 18,
          "fragment": "from modules.knowledge import merge, notifications, provenance"
        }
      },
      {
        "from": "learningBack/modules/knowledge/review.py",
        "to": "learningBack/modules/knowledge/merge.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/review.py",
          "line": 18,
          "fragment": "from modules.knowledge import merge, notifications, provenance"
        }
      },
      {
        "from": "learningBack/modules/knowledge/review.py",
        "to": "learningBack/modules/knowledge/notifications.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/review.py",
          "line": 18,
          "fragment": "from modules.knowledge import merge, notifications, provenance"
        }
      },
      {
        "from": "learningBack/modules/knowledge/review.py",
        "to": "learningBack/modules/knowledge/provenance.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/review.py",
          "line": 18,
          "fragment": "from modules.knowledge import merge, notifications, provenance"
        }
      },
      {
        "from": "learningBack/modules/knowledge/review.py",
        "to": "learningBack/modules/knowledge/models.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/review.py",
          "line": 19,
          "fragment": "from modules.knowledge.models import ("
        }
      },
      {
        "from": "learningBack/modules/knowledge/review_api.py",
        "to": "learningBack/core/deps.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/review_api.py",
          "line": 14,
          "fragment": "from core.deps import CurrentSuperuser, CurrentUser, SessionDep"
        }
      },
      {
        "from": "learningBack/modules/knowledge/review_api.py",
        "to": "learningBack/modules/knowledge/__init__.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/review_api.py",
          "line": 15,
          "fragment": "from modules.knowledge import provenance, review"
        }
      },
      {
        "from": "learningBack/modules/knowledge/review_api.py",
        "to": "learningBack/modules/knowledge/provenance.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/review_api.py",
          "line": 15,
          "fragment": "from modules.knowledge import provenance, review"
        }
      },
      {
        "from": "learningBack/modules/knowledge/review_api.py",
        "to": "learningBack/modules/knowledge/review.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/review_api.py",
          "line": 15,
          "fragment": "from modules.knowledge import provenance, review"
        }
      },
      {
        "from": "learningBack/modules/knowledge/review_api.py",
        "to": "learningBack/modules/knowledge/models.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/review_api.py",
          "line": 16,
          "fragment": "from modules.knowledge.models import Concept, ConceptConflict, ConceptEdge"
        }
      },
      {
        "from": "learningBack/modules/knowledge/skill_profile.py",
        "to": "learningBack/core/ai_gateway.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/skill_profile.py",
          "line": 19,
          "fragment": "from core.ai_gateway import get_ai_gateway, has_llm"
        }
      },
      {
        "from": "learningBack/modules/knowledge/skill_profile.py",
        "to": "learningBack/modules/knowledge/__init__.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/skill_profile.py",
          "line": 20,
          "fragment": "from modules.knowledge import stages"
        }
      },
      {
        "from": "learningBack/modules/knowledge/skill_profile.py",
        "to": "learningBack/modules/knowledge/stages.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/skill_profile.py",
          "line": 20,
          "fragment": "from modules.knowledge import stages"
        }
      },
      {
        "from": "learningBack/modules/knowledge/source_search.py",
        "to": "learningBack/core/config.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/source_search.py",
          "line": 26,
          "fragment": "from core.config import settings"
        }
      },
      {
        "from": "learningBack/modules/knowledge/source_search.py",
        "to": "learningBack/modules/knowledge/__init__.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/source_search.py",
          "line": 27,
          "fragment": "from modules.knowledge import ingest, provenance"
        }
      },
      {
        "from": "learningBack/modules/knowledge/source_search.py",
        "to": "learningBack/modules/knowledge/ingest.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/source_search.py",
          "line": 27,
          "fragment": "from modules.knowledge import ingest, provenance"
        }
      },
      {
        "from": "learningBack/modules/knowledge/source_search.py",
        "to": "learningBack/modules/knowledge/provenance.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/source_search.py",
          "line": 27,
          "fragment": "from modules.knowledge import ingest, provenance"
        }
      },
      {
        "from": "learningBack/modules/knowledge/source_search.py",
        "to": "learningBack/modules/knowledge/models.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/source_search.py",
          "line": 28,
          "fragment": "from modules.knowledge.models import SourceDocument"
        }
      },
      {
        "from": "learningBack/modules/knowledge/subjects_api.py",
        "to": "learningBack/core/deps.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/subjects_api.py",
          "line": 10,
          "fragment": "from core.deps import CurrentUser, SessionDep"
        }
      },
      {
        "from": "learningBack/modules/knowledge/subjects_api.py",
        "to": "learningBack/modules/knowledge/models.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/subjects_api.py",
          "line": 11,
          "fragment": "from modules.knowledge.models import UserSubject"
        }
      },
      {
        "from": "learningBack/modules/knowledge/theory.py",
        "to": "learningBack/core/ai_gateway.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/theory.py",
          "line": 15,
          "fragment": "from core.ai_gateway import get_ai_gateway, has_llm"
        }
      },
      {
        "from": "learningBack/modules/knowledge/theory.py",
        "to": "learningBack/modules/knowledge/__init__.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/theory.py",
          "line": 16,
          "fragment": "from modules.knowledge import provenance"
        }
      },
      {
        "from": "learningBack/modules/knowledge/theory.py",
        "to": "learningBack/modules/knowledge/provenance.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/theory.py",
          "line": 16,
          "fragment": "from modules.knowledge import provenance"
        }
      },
      {
        "from": "learningBack/modules/knowledge/theory.py",
        "to": "learningBack/modules/knowledge/content.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/theory.py",
          "line": 17,
          "fragment": "from modules.knowledge.content import NodeContent, coerce_content"
        }
      },
      {
        "from": "learningBack/modules/knowledge/theory.py",
        "to": "learningBack/modules/knowledge/models.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/theory.py",
          "line": 18,
          "fragment": "from modules.knowledge.models import Concept"
        }
      },
      {
        "from": "learningBack/scripts/backup_objects.py",
        "to": "learningBack/core/config.py",
        "evidence": {
          "path": "learningBack/scripts/backup_objects.py",
          "line": 19,
          "fragment": "from core.config import settings"
        }
      },
      {
        "from": "learningBack/scripts/backup_objects.py",
        "to": "learningBack/core/objects.py",
        "evidence": {
          "path": "learningBack/scripts/backup_objects.py",
          "line": 20,
          "fragment": "from core.objects import S3ObjectStore, get_store"
        }
      },
      {
        "from": "learningBack/scripts/ingest_document.py",
        "to": "learningBack/core/ai_gateway.py",
        "evidence": {
          "path": "learningBack/scripts/ingest_document.py",
          "line": 15,
          "fragment": "from core.ai_gateway import get_ai_gateway"
        }
      },
      {
        "from": "learningBack/scripts/ingest_document.py",
        "to": "learningBack/core/db.py",
        "evidence": {
          "path": "learningBack/scripts/ingest_document.py",
          "line": 16,
          "fragment": "from core.db import SessionLocal"
        }
      },
      {
        "from": "learningBack/scripts/ingest_document.py",
        "to": "learningBack/modules/knowledge/__init__.py",
        "evidence": {
          "path": "learningBack/scripts/ingest_document.py",
          "line": 17,
          "fragment": "from modules.knowledge import ingest, provenance"
        }
      },
      {
        "from": "learningBack/scripts/ingest_document.py",
        "to": "learningBack/modules/knowledge/ingest.py",
        "evidence": {
          "path": "learningBack/scripts/ingest_document.py",
          "line": 17,
          "fragment": "from modules.knowledge import ingest, provenance"
        }
      },
      {
        "from": "learningBack/scripts/ingest_document.py",
        "to": "learningBack/modules/knowledge/provenance.py",
        "evidence": {
          "path": "learningBack/scripts/ingest_document.py",
          "line": 17,
          "fragment": "from modules.knowledge import ingest, provenance"
        }
      },
      {
        "from": "learningBack/scripts/merge_concepts.py",
        "to": "learningBack/core/ai_gateway.py",
        "evidence": {
          "path": "learningBack/scripts/merge_concepts.py",
          "line": 13,
          "fragment": "from core.ai_gateway import get_ai_gateway"
        }
      },
      {
        "from": "learningBack/scripts/merge_concepts.py",
        "to": "learningBack/core/db.py",
        "evidence": {
          "path": "learningBack/scripts/merge_concepts.py",
          "line": 14,
          "fragment": "from core.db import SessionLocal"
        }
      },
      {
        "from": "learningBack/scripts/merge_concepts.py",
        "to": "learningBack/modules/knowledge/__init__.py",
        "evidence": {
          "path": "learningBack/scripts/merge_concepts.py",
          "line": 15,
          "fragment": "from modules.knowledge import merge"
        }
      },
      {
        "from": "learningBack/scripts/merge_concepts.py",
        "to": "learningBack/modules/knowledge/merge.py",
        "evidence": {
          "path": "learningBack/scripts/merge_concepts.py",
          "line": 15,
          "fragment": "from modules.knowledge import merge"
        }
      },
      {
        "from": "learningBack/scripts/refresh_knowledge.py",
        "to": "learningBack/core/db.py",
        "evidence": {
          "path": "learningBack/scripts/refresh_knowledge.py",
          "line": 11,
          "fragment": "from core.db import SessionLocal"
        }
      },
      {
        "from": "learningBack/scripts/refresh_knowledge.py",
        "to": "learningBack/core/models.py",
        "evidence": {
          "path": "learningBack/scripts/refresh_knowledge.py",
          "line": 12,
          "fragment": "from core.models import User"
        }
      },
      {
        "from": "learningBack/scripts/refresh_knowledge.py",
        "to": "learningBack/modules/knowledge/__init__.py",
        "evidence": {
          "path": "learningBack/scripts/refresh_knowledge.py",
          "line": 13,
          "fragment": "from modules.knowledge import freshness"
        }
      },
      {
        "from": "learningBack/scripts/refresh_knowledge.py",
        "to": "learningBack/modules/knowledge/freshness.py",
        "evidence": {
          "path": "learningBack/scripts/refresh_knowledge.py",
          "line": 13,
          "fragment": "from modules.knowledge import freshness"
        }
      },
      {
        "from": "learningBack/scripts/run_textbooks.py",
        "to": "learningBack/core/ai_gateway.py",
        "evidence": {
          "path": "learningBack/scripts/run_textbooks.py",
          "line": 20,
          "fragment": "from core.ai_gateway import get_ai_gateway"
        }
      },
      {
        "from": "learningBack/scripts/run_textbooks.py",
        "to": "learningBack/core/db.py",
        "evidence": {
          "path": "learningBack/scripts/run_textbooks.py",
          "line": 21,
          "fragment": "from core.db import SessionLocal"
        }
      },
      {
        "from": "learningBack/scripts/run_textbooks.py",
        "to": "learningBack/core/models.py",
        "evidence": {
          "path": "learningBack/scripts/run_textbooks.py",
          "line": 22,
          "fragment": "from core.models import Job, User"
        }
      },
      {
        "from": "learningBack/scripts/run_textbooks.py",
        "to": "learningBack/core/worker.py",
        "evidence": {
          "path": "learningBack/scripts/run_textbooks.py",
          "line": 23,
          "fragment": "from core.worker import work_one"
        }
      },
      {
        "from": "learningBack/scripts/run_textbooks.py",
        "to": "learningBack/modules/knowledge/__init__.py",
        "evidence": {
          "path": "learningBack/scripts/run_textbooks.py",
          "line": 24,
          "fragment": "from modules.knowledge import ingest, provenance"
        }
      },
      {
        "from": "learningBack/scripts/run_textbooks.py",
        "to": "learningBack/modules/knowledge/ingest.py",
        "evidence": {
          "path": "learningBack/scripts/run_textbooks.py",
          "line": 24,
          "fragment": "from modules.knowledge import ingest, provenance"
        }
      },
      {
        "from": "learningBack/scripts/run_textbooks.py",
        "to": "learningBack/modules/knowledge/provenance.py",
        "evidence": {
          "path": "learningBack/scripts/run_textbooks.py",
          "line": 24,
          "fragment": "from modules.knowledge import ingest, provenance"
        }
      },
      {
        "from": "learningBack/scripts/run_textbooks.py",
        "to": "learningBack/modules/knowledge/models.py",
        "evidence": {
          "path": "learningBack/scripts/run_textbooks.py",
          "line": 25,
          "fragment": "from modules.knowledge.models import ("
        }
      },
      {
        "from": "learningBack/tests/kg_helpers.py",
        "to": "learningBack/core/objects.py",
        "evidence": {
          "path": "learningBack/tests/kg_helpers.py",
          "line": 7,
          "fragment": "from core.objects import MemoryObjectStore"
        }
      },
      {
        "from": "learningBack/tests/kg_helpers.py",
        "to": "learningBack/modules/knowledge/__init__.py",
        "evidence": {
          "path": "learningBack/tests/kg_helpers.py",
          "line": 8,
          "fragment": "from modules.knowledge import provenance"
        }
      },
      {
        "from": "learningBack/tests/kg_helpers.py",
        "to": "learningBack/modules/knowledge/provenance.py",
        "evidence": {
          "path": "learningBack/tests/kg_helpers.py",
          "line": 8,
          "fragment": "from modules.knowledge import provenance"
        }
      },
      {
        "from": "learningBack/tests/kg_helpers.py",
        "to": "learningBack/modules/knowledge/models.py",
        "evidence": {
          "path": "learningBack/tests/kg_helpers.py",
          "line": 9,
          "fragment": "from modules.knowledge.models import ("
        }
      },
      {
        "from": "learningBack/tests/test_backup_objects.py",
        "to": "learningBack/core/__init__.py",
        "evidence": {
          "path": "learningBack/tests/test_backup_objects.py",
          "line": 10,
          "fragment": "from core import objects"
        }
      },
      {
        "from": "learningBack/tests/test_backup_objects.py",
        "to": "learningBack/core/objects.py",
        "evidence": {
          "path": "learningBack/tests/test_backup_objects.py",
          "line": 10,
          "fragment": "from core import objects"
        }
      },
      {
        "from": "learningBack/tests/test_backup_objects.py",
        "to": "learningBack/core/config.py",
        "evidence": {
          "path": "learningBack/tests/test_backup_objects.py",
          "line": 11,
          "fragment": "from core.config import settings"
        }
      },
      {
        "from": "learningBack/tests/test_backup_objects.py",
        "to": "learningBack/scripts/__init__.py",
        "evidence": {
          "path": "learningBack/tests/test_backup_objects.py",
          "line": 13,
          "fragment": "from scripts import backup_objects"
        }
      },
      {
        "from": "learningBack/tests/test_backup_objects.py",
        "to": "learningBack/scripts/backup_objects.py",
        "evidence": {
          "path": "learningBack/tests/test_backup_objects.py",
          "line": 13,
          "fragment": "from scripts import backup_objects"
        }
      },
      {
        "from": "learningBack/tests/test_backup_objects.py",
        "to": "learningBack/tests/test_objects.py",
        "evidence": {
          "path": "learningBack/tests/test_backup_objects.py",
          "line": 14,
          "fragment": "from tests.test_objects import S3_URL, _s3_up"
        }
      },
      {
        "from": "learningBack/tests/test_gap_search.py",
        "to": "learningBack/core/__init__.py",
        "evidence": {
          "path": "learningBack/tests/test_gap_search.py",
          "line": 9,
          "fragment": "from core import objects"
        }
      },
      {
        "from": "learningBack/tests/test_gap_search.py",
        "to": "learningBack/core/objects.py",
        "evidence": {
          "path": "learningBack/tests/test_gap_search.py",
          "line": 9,
          "fragment": "from core import objects"
        }
      },
      {
        "from": "learningBack/tests/test_gap_search.py",
        "to": "learningBack/modules/knowledge/__init__.py",
        "evidence": {
          "path": "learningBack/tests/test_gap_search.py",
          "line": 11,
          "fragment": "from modules.knowledge import domains, gap_search, ingest"
        }
      },
      {
        "from": "learningBack/tests/test_gap_search.py",
        "to": "learningBack/modules/knowledge/domains.py",
        "evidence": {
          "path": "learningBack/tests/test_gap_search.py",
          "line": 11,
          "fragment": "from modules.knowledge import domains, gap_search, ingest"
        }
      },
      {
        "from": "learningBack/tests/test_gap_search.py",
        "to": "learningBack/modules/knowledge/gap_search.py",
        "evidence": {
          "path": "learningBack/tests/test_gap_search.py",
          "line": 11,
          "fragment": "from modules.knowledge import domains, gap_search, ingest"
        }
      },
      {
        "from": "learningBack/tests/test_gap_search.py",
        "to": "learningBack/modules/knowledge/ingest.py",
        "evidence": {
          "path": "learningBack/tests/test_gap_search.py",
          "line": 11,
          "fragment": "from modules.knowledge import domains, gap_search, ingest"
        }
      },
      {
        "from": "learningBack/tests/test_gap_search.py",
        "to": "learningBack/modules/knowledge/models.py",
        "evidence": {
          "path": "learningBack/tests/test_gap_search.py",
          "line": 12,
          "fragment": "from modules.knowledge.models import SourceDocument"
        }
      },
      {
        "from": "learningBack/tests/test_gap_search.py",
        "to": "learningBack/modules/knowledge/source_search.py",
        "evidence": {
          "path": "learningBack/tests/test_gap_search.py",
          "line": 13,
          "fragment": "from modules.knowledge.source_search import Candidate"
        }
      },
      {
        "from": "learningBack/tests/test_gap_search.py",
        "to": "learningBack/tests/conftest.py",
        "evidence": {
          "path": "learningBack/tests/test_gap_search.py",
          "line": 14,
          "fragment": "from tests.conftest import make_user"
        }
      },
      {
        "from": "learningBack/tests/test_gap_search.py",
        "to": "learningBack/tests/test_chain_placement.py",
        "evidence": {
          "path": "learningBack/tests/test_gap_search.py",
          "line": 15,
          "fragment": "from tests.test_chain_placement import world  # noqa: F401"
        }
      },
      {
        "from": "learningBack/tests/test_gap_search.py",
        "to": "learningBack/core/models.py",
        "evidence": {
          "path": "learningBack/tests/test_gap_search.py",
          "line": 145,
          "fragment": "from core.models import Job"
        }
      },
      {
        "from": "learningBack/tests/test_graph_admin.py",
        "to": "learningBack/modules/knowledge/__init__.py",
        "evidence": {
          "path": "learningBack/tests/test_graph_admin.py",
          "line": 7,
          "fragment": "from modules.knowledge import graph_admin_data as data"
        }
      },
      {
        "from": "learningBack/tests/test_graph_admin.py",
        "to": "learningBack/modules/knowledge/graph_admin_data.py",
        "evidence": {
          "path": "learningBack/tests/test_graph_admin.py",
          "line": 7,
          "fragment": "from modules.knowledge import graph_admin_data as data"
        }
      },
      {
        "from": "learningBack/tests/test_graph_admin.py",
        "to": "learningBack/modules/knowledge/admin.py",
        "evidence": {
          "path": "learningBack/tests/test_graph_admin.py",
          "line": 8,
          "fragment": "from modules.knowledge.admin import VIEWS"
        }
      },
      {
        "from": "learningBack/tests/test_graph_admin.py",
        "to": "learningBack/modules/knowledge/graph_admin.py",
        "evidence": {
          "path": "learningBack/tests/test_graph_admin.py",
          "line": 9,
          "fragment": "from modules.knowledge.graph_admin import GraphAdmin"
        }
      },
      {
        "from": "learningBack/tests/test_graph_admin.py",
        "to": "learningBack/modules/knowledge/models.py",
        "evidence": {
          "path": "learningBack/tests/test_graph_admin.py",
          "line": 10,
          "fragment": "from modules.knowledge.models import Concept, ConceptEdge"
        }
      },
      {
        "from": "learningBack/tests/test_graph_admin.py",
        "to": "learningBack/modules/knowledge/domains.py",
        "evidence": {
          "path": "learningBack/tests/test_graph_admin.py",
          "line": 148,
          "fragment": "from modules.knowledge import domains"
        }
      },
      {
        "from": "learningBack/tests/test_ingest.py",
        "to": "learningBack/core/config.py",
        "evidence": {
          "path": "learningBack/tests/test_ingest.py",
          "line": 10,
          "fragment": "from core.config import settings"
        }
      },
      {
        "from": "learningBack/tests/test_ingest.py",
        "to": "learningBack/core/jobs.py",
        "evidence": {
          "path": "learningBack/tests/test_ingest.py",
          "line": 11,
          "fragment": "from core.jobs import process_job"
        }
      },
      {
        "from": "learningBack/tests/test_ingest.py",
        "to": "learningBack/core/models.py",
        "evidence": {
          "path": "learningBack/tests/test_ingest.py",
          "line": 12,
          "fragment": "from core.models import Job"
        }
      },
      {
        "from": "learningBack/tests/test_ingest.py",
        "to": "learningBack/core/objects.py",
        "evidence": {
          "path": "learningBack/tests/test_ingest.py",
          "line": 13,
          "fragment": "from core.objects import MemoryObjectStore"
        }
      },
      {
        "from": "learningBack/tests/test_ingest.py",
        "to": "learningBack/modules/knowledge/__init__.py",
        "evidence": {
          "path": "learningBack/tests/test_ingest.py",
          "line": 14,
          "fragment": "from modules.knowledge import ingest, provenance"
        }
      },
      {
        "from": "learningBack/tests/test_ingest.py",
        "to": "learningBack/modules/knowledge/ingest.py",
        "evidence": {
          "path": "learningBack/tests/test_ingest.py",
          "line": 14,
          "fragment": "from modules.knowledge import ingest, provenance"
        }
      },
      {
        "from": "learningBack/tests/test_ingest.py",
        "to": "learningBack/modules/knowledge/provenance.py",
        "evidence": {
          "path": "learningBack/tests/test_ingest.py",
          "line": 14,
          "fragment": "from modules.knowledge import ingest, provenance"
        }
      },
      {
        "from": "learningBack/tests/test_ingest.py",
        "to": "learningBack/modules/knowledge/models.py",
        "evidence": {
          "path": "learningBack/tests/test_ingest.py",
          "line": 15,
          "fragment": "from modules.knowledge.models import Concept, ConceptEdge, ConceptSource, SourceDocument"
        }
      },
      {
        "from": "learningBack/tests/test_ingest.py",
        "to": "learningBack/tests/conftest.py",
        "evidence": {
          "path": "learningBack/tests/test_ingest.py",
          "line": 16,
          "fragment": "from tests.conftest import make_user"
        }
      },
      {
        "from": "learningBack/tests/test_ingest.py",
        "to": "learningBack/core/__init__.py",
        "evidence": {
          "path": "learningBack/tests/test_ingest.py",
          "line": 336,
          "fragment": "from core import objects"
        }
      },
      {
        "from": "learningBack/tests/test_merge.py",
        "to": "learningBack/core/config.py",
        "evidence": {
          "path": "learningBack/tests/test_merge.py",
          "line": 7,
          "fragment": "from core.config import settings"
        }
      },
      {
        "from": "learningBack/tests/test_merge.py",
        "to": "learningBack/core/embeddings.py",
        "evidence": {
          "path": "learningBack/tests/test_merge.py",
          "line": 8,
          "fragment": "from core.embeddings import HashEmbedder"
        }
      },
      {
        "from": "learningBack/tests/test_merge.py",
        "to": "learningBack/core/jobs.py",
        "evidence": {
          "path": "learningBack/tests/test_merge.py",
          "line": 9,
          "fragment": "from core.jobs import process_job"
        }
      },
      {
        "from": "learningBack/tests/test_merge.py",
        "to": "learningBack/core/objects.py",
        "evidence": {
          "path": "learningBack/tests/test_merge.py",
          "line": 10,
          "fragment": "from core.objects import MemoryObjectStore"
        }
      },
      {
        "from": "learningBack/tests/test_merge.py",
        "to": "learningBack/modules/knowledge/__init__.py",
        "evidence": {
          "path": "learningBack/tests/test_merge.py",
          "line": 11,
          "fragment": "from modules.knowledge import ingest, merge, provenance"
        }
      },
      {
        "from": "learningBack/tests/test_merge.py",
        "to": "learningBack/modules/knowledge/ingest.py",
        "evidence": {
          "path": "learningBack/tests/test_merge.py",
          "line": 11,
          "fragment": "from modules.knowledge import ingest, merge, provenance"
        }
      },
      {
        "from": "learningBack/tests/test_merge.py",
        "to": "learningBack/modules/knowledge/merge.py",
        "evidence": {
          "path": "learningBack/tests/test_merge.py",
          "line": 11,
          "fragment": "from modules.knowledge import ingest, merge, provenance"
        }
      },
      {
        "from": "learningBack/tests/test_merge.py",
        "to": "learningBack/modules/knowledge/provenance.py",
        "evidence": {
          "path": "learningBack/tests/test_merge.py",
          "line": 11,
          "fragment": "from modules.knowledge import ingest, merge, provenance"
        }
      },
      {
        "from": "learningBack/tests/test_merge.py",
        "to": "learningBack/modules/knowledge/models.py",
        "evidence": {
          "path": "learningBack/tests/test_merge.py",
          "line": 12,
          "fragment": "from modules.knowledge.models import ("
        }
      },
      {
        "from": "learningBack/tests/test_merge.py",
        "to": "learningBack/tests/conftest.py",
        "evidence": {
          "path": "learningBack/tests/test_merge.py",
          "line": 23,
          "fragment": "from tests.conftest import make_user"
        }
      },
      {
        "from": "learningBack/tests/test_merge.py",
        "to": "learningBack/core/__init__.py",
        "evidence": {
          "path": "learningBack/tests/test_merge.py",
          "line": 327,
          "fragment": "from core import objects"
        }
      },
      {
        "from": "learningBack/tests/test_merge.py",
        "to": "learningBack/core/models.py",
        "evidence": {
          "path": "learningBack/tests/test_merge.py",
          "line": 336,
          "fragment": "from core.models import Job"
        }
      },
      {
        "from": "learningBack/tests/test_migrations_match_models.py",
        "to": "learningBack/core/config.py",
        "evidence": {
          "path": "learningBack/tests/test_migrations_match_models.py",
          "line": 18,
          "fragment": "from core.config import settings"
        }
      },
      {
        "from": "learningBack/tests/test_migrations_match_models.py",
        "to": "learningBack/core/db.py",
        "evidence": {
          "path": "learningBack/tests/test_migrations_match_models.py",
          "line": 19,
          "fragment": "from core.db import Base"
        }
      },
      {
        "from": "learningBack/tests/test_migrations_match_models.py",
        "to": "learningBack/core/models.py",
        "evidence": {
          "path": "learningBack/tests/test_migrations_match_models.py",
          "line": 21,
          "fragment": "import core.models  # noqa: F401  # регистрация таблиц"
        }
      },
      {
        "from": "learningBack/tests/test_migrations_match_models.py",
        "to": "learningBack/modules/knowledge/models.py",
        "evidence": {
          "path": "learningBack/tests/test_migrations_match_models.py",
          "line": 22,
          "fragment": "import modules.knowledge.models  # noqa: F401"
        }
      },
      {
        "from": "learningBack/tests/test_notifications.py",
        "to": "learningBack/core/__init__.py",
        "evidence": {
          "path": "learningBack/tests/test_notifications.py",
          "line": 7,
          "fragment": "from core import objects"
        }
      },
      {
        "from": "learningBack/tests/test_notifications.py",
        "to": "learningBack/core/objects.py",
        "evidence": {
          "path": "learningBack/tests/test_notifications.py",
          "line": 7,
          "fragment": "from core import objects"
        }
      },
      {
        "from": "learningBack/tests/test_notifications.py",
        "to": "learningBack/core/jobs.py",
        "evidence": {
          "path": "learningBack/tests/test_notifications.py",
          "line": 8,
          "fragment": "from core.jobs import process_job"
        }
      },
      {
        "from": "learningBack/tests/test_notifications.py",
        "to": "learningBack/modules/knowledge/__init__.py",
        "evidence": {
          "path": "learningBack/tests/test_notifications.py",
          "line": 10,
          "fragment": "from modules.knowledge import ingest, notifications, provenance"
        }
      },
      {
        "from": "learningBack/tests/test_notifications.py",
        "to": "learningBack/modules/knowledge/ingest.py",
        "evidence": {
          "path": "learningBack/tests/test_notifications.py",
          "line": 10,
          "fragment": "from modules.knowledge import ingest, notifications, provenance"
        }
      },
      {
        "from": "learningBack/tests/test_notifications.py",
        "to": "learningBack/modules/knowledge/notifications.py",
        "evidence": {
          "path": "learningBack/tests/test_notifications.py",
          "line": 10,
          "fragment": "from modules.knowledge import ingest, notifications, provenance"
        }
      },
      {
        "from": "learningBack/tests/test_notifications.py",
        "to": "learningBack/modules/knowledge/provenance.py",
        "evidence": {
          "path": "learningBack/tests/test_notifications.py",
          "line": 10,
          "fragment": "from modules.knowledge import ingest, notifications, provenance"
        }
      },
      {
        "from": "learningBack/tests/test_notifications.py",
        "to": "learningBack/modules/knowledge/course.py",
        "evidence": {
          "path": "learningBack/tests/test_notifications.py",
          "line": 11,
          "fragment": "from modules.knowledge.course import generate_course"
        }
      },
      {
        "from": "learningBack/tests/test_notifications.py",
        "to": "learningBack/modules/knowledge/models.py",
        "evidence": {
          "path": "learningBack/tests/test_notifications.py",
          "line": 12,
          "fragment": "from modules.knowledge.models import Concept, Course, Notification"
        }
      },
      {
        "from": "learningBack/tests/test_notifications.py",
        "to": "learningBack/tests/conftest.py",
        "evidence": {
          "path": "learningBack/tests/test_notifications.py",
          "line": 13,
          "fragment": "from tests.conftest import make_user"
        }
      },
      {
        "from": "learningBack/tests/test_notifications.py",
        "to": "learningBack/core/models.py",
        "evidence": {
          "path": "learningBack/tests/test_notifications.py",
          "line": 235,
          "fragment": "from core.models import Activity"
        }
      },
      {
        "from": "learningBack/tests/test_notifications_review.py",
        "to": "learningBack/core/models.py",
        "evidence": {
          "path": "learningBack/tests/test_notifications_review.py",
          "line": 7,
          "fragment": "from core.models import Activity"
        }
      },
      {
        "from": "learningBack/tests/test_notifications_review.py",
        "to": "learningBack/modules/knowledge/__init__.py",
        "evidence": {
          "path": "learningBack/tests/test_notifications_review.py",
          "line": 8,
          "fragment": "from modules.knowledge import notifications, provenance, review"
        }
      },
      {
        "from": "learningBack/tests/test_notifications_review.py",
        "to": "learningBack/modules/knowledge/notifications.py",
        "evidence": {
          "path": "learningBack/tests/test_notifications_review.py",
          "line": 8,
          "fragment": "from modules.knowledge import notifications, provenance, review"
        }
      },
      {
        "from": "learningBack/tests/test_notifications_review.py",
        "to": "learningBack/modules/knowledge/provenance.py",
        "evidence": {
          "path": "learningBack/tests/test_notifications_review.py",
          "line": 8,
          "fragment": "from modules.knowledge import notifications, provenance, review"
        }
      },
      {
        "from": "learningBack/tests/test_notifications_review.py",
        "to": "learningBack/modules/knowledge/review.py",
        "evidence": {
          "path": "learningBack/tests/test_notifications_review.py",
          "line": 8,
          "fragment": "from modules.knowledge import notifications, provenance, review"
        }
      },
      {
        "from": "learningBack/tests/test_notifications_review.py",
        "to": "learningBack/modules/knowledge/course.py",
        "evidence": {
          "path": "learningBack/tests/test_notifications_review.py",
          "line": 9,
          "fragment": "from modules.knowledge.course import generate_course, mark_completed"
        }
      },
      {
        "from": "learningBack/tests/test_notifications_review.py",
        "to": "learningBack/modules/knowledge/models.py",
        "evidence": {
          "path": "learningBack/tests/test_notifications_review.py",
          "line": 10,
          "fragment": "from modules.knowledge.models import Concept, Notification"
        }
      },
      {
        "from": "learningBack/tests/test_notifications_review.py",
        "to": "learningBack/tests/conftest.py",
        "evidence": {
          "path": "learningBack/tests/test_notifications_review.py",
          "line": 11,
          "fragment": "from tests.conftest import make_user"
        }
      },
      {
        "from": "learningBack/tests/test_notifications_review.py",
        "to": "learningBack/tests/test_notifications.py",
        "evidence": {
          "path": "learningBack/tests/test_notifications_review.py",
          "line": 12,
          "fragment": "from tests.test_notifications import DOMAIN, As, concept"
        }
      },
      {
        "from": "learningBack/tests/test_objects.py",
        "to": "learningBack/core/__init__.py",
        "evidence": {
          "path": "learningBack/tests/test_objects.py",
          "line": 12,
          "fragment": "from core import objects"
        }
      },
      {
        "from": "learningBack/tests/test_objects.py",
        "to": "learningBack/core/objects.py",
        "evidence": {
          "path": "learningBack/tests/test_objects.py",
          "line": 12,
          "fragment": "from core import objects"
        }
      },
      {
        "from": "learningBack/tests/test_objects.py",
        "to": "learningBack/core/config.py",
        "evidence": {
          "path": "learningBack/tests/test_objects.py",
          "line": 13,
          "fragment": "from core.config import settings"
        }
      },
      {
        "from": "learningBack/tests/test_prior_report.py",
        "to": "learningBack/modules/knowledge/__init__.py",
        "evidence": {
          "path": "learningBack/tests/test_prior_report.py",
          "line": 6,
          "fragment": "from modules.knowledge import domains, prior_report"
        }
      },
      {
        "from": "learningBack/tests/test_prior_report.py",
        "to": "learningBack/modules/knowledge/domains.py",
        "evidence": {
          "path": "learningBack/tests/test_prior_report.py",
          "line": 6,
          "fragment": "from modules.knowledge import domains, prior_report"
        }
      },
      {
        "from": "learningBack/tests/test_prior_report.py",
        "to": "learningBack/modules/knowledge/prior_report.py",
        "evidence": {
          "path": "learningBack/tests/test_prior_report.py",
          "line": 6,
          "fragment": "from modules.knowledge import domains, prior_report"
        }
      },
      {
        "from": "learningBack/tests/test_prior_report.py",
        "to": "learningBack/modules/knowledge/course.py",
        "evidence": {
          "path": "learningBack/tests/test_prior_report.py",
          "line": 7,
          "fragment": "from modules.knowledge.course import build_path"
        }
      },
      {
        "from": "learningBack/tests/test_prior_report.py",
        "to": "learningBack/modules/knowledge/mastery.py",
        "evidence": {
          "path": "learningBack/tests/test_prior_report.py",
          "line": 8,
          "fragment": "from modules.knowledge.mastery import MasteryState, save_state"
        }
      },
      {
        "from": "learningBack/tests/test_prior_report.py",
        "to": "learningBack/tests/conftest.py",
        "evidence": {
          "path": "learningBack/tests/test_prior_report.py",
          "line": 9,
          "fragment": "from tests.conftest import make_user"
        }
      },
      {
        "from": "learningBack/tests/test_prior_report.py",
        "to": "learningBack/tests/test_chain_placement.py",
        "evidence": {
          "path": "learningBack/tests/test_prior_report.py",
          "line": 10,
          "fragment": "from tests.test_chain_placement import (  # noqa: F401"
        }
      },
      {
        "from": "learningBack/tests/test_prior_report.py",
        "to": "learningBack/modules/knowledge/cross_links.py",
        "evidence": {
          "path": "learningBack/tests/test_prior_report.py",
          "line": 75,
          "fragment": "from modules.knowledge import cross_links"
        }
      },
      {
        "from": "learningBack/tests/test_profile_build.py",
        "to": "learningBack/core/__init__.py",
        "evidence": {
          "path": "learningBack/tests/test_profile_build.py",
          "line": 7,
          "fragment": "from core import ai_gateway"
        }
      },
      {
        "from": "learningBack/tests/test_profile_build.py",
        "to": "learningBack/core/ai_gateway.py",
        "evidence": {
          "path": "learningBack/tests/test_profile_build.py",
          "line": 7,
          "fragment": "from core import ai_gateway"
        }
      },
      {
        "from": "learningBack/tests/test_profile_build.py",
        "to": "learningBack/modules/knowledge/__init__.py",
        "evidence": {
          "path": "learningBack/tests/test_profile_build.py",
          "line": 8,
          "fragment": "from modules.knowledge import ("
        }
      },
      {
        "from": "learningBack/tests/test_profile_build.py",
        "to": "learningBack/modules/knowledge/models.py",
        "evidence": {
          "path": "learningBack/tests/test_profile_build.py",
          "line": 17,
          "fragment": "from modules.knowledge.models import Concept, ConceptEdge, Domain"
        }
      },
      {
        "from": "learningBack/tests/test_profile_build.py",
        "to": "learningBack/tests/conftest.py",
        "evidence": {
          "path": "learningBack/tests/test_profile_build.py",
          "line": 18,
          "fragment": "from tests.conftest import make_user"
        }
      },
      {
        "from": "learningBack/tests/test_profile_coverage.py",
        "to": "learningBack/modules/knowledge/__init__.py",
        "evidence": {
          "path": "learningBack/tests/test_profile_coverage.py",
          "line": 5,
          "fragment": "from modules.knowledge import cross_links, merge, profile_build, profile_coverage, profile_store"
        }
      },
      {
        "from": "learningBack/tests/test_profile_coverage.py",
        "to": "learningBack/modules/knowledge/cross_links.py",
        "evidence": {
          "path": "learningBack/tests/test_profile_coverage.py",
          "line": 5,
          "fragment": "from modules.knowledge import cross_links, merge, profile_build, profile_coverage, profile_store"
        }
      },
      {
        "from": "learningBack/tests/test_profile_coverage.py",
        "to": "learningBack/modules/knowledge/merge.py",
        "evidence": {
          "path": "learningBack/tests/test_profile_coverage.py",
          "line": 5,
          "fragment": "from modules.knowledge import cross_links, merge, profile_build, profile_coverage, profile_store"
        }
      },
      {
        "from": "learningBack/tests/test_profile_coverage.py",
        "to": "learningBack/modules/knowledge/profile_build.py",
        "evidence": {
          "path": "learningBack/tests/test_profile_coverage.py",
          "line": 5,
          "fragment": "from modules.knowledge import cross_links, merge, profile_build, profile_coverage, profile_store"
        }
      },
      {
        "from": "learningBack/tests/test_profile_coverage.py",
        "to": "learningBack/modules/knowledge/profile_coverage.py",
        "evidence": {
          "path": "learningBack/tests/test_profile_coverage.py",
          "line": 5,
          "fragment": "from modules.knowledge import cross_links, merge, profile_build, profile_coverage, profile_store"
        }
      },
      {
        "from": "learningBack/tests/test_profile_coverage.py",
        "to": "learningBack/modules/knowledge/profile_store.py",
        "evidence": {
          "path": "learningBack/tests/test_profile_coverage.py",
          "line": 5,
          "fragment": "from modules.knowledge import cross_links, merge, profile_build, profile_coverage, profile_store"
        }
      },
      {
        "from": "learningBack/tests/test_profile_coverage.py",
        "to": "learningBack/modules/knowledge/models.py",
        "evidence": {
          "path": "learningBack/tests/test_profile_coverage.py",
          "line": 6,
          "fragment": "from modules.knowledge.models import ("
        }
      },
      {
        "from": "learningBack/tests/test_profile_coverage.py",
        "to": "learningBack/tests/conftest.py",
        "evidence": {
          "path": "learningBack/tests/test_profile_coverage.py",
          "line": 14,
          "fragment": "from tests.conftest import make_user"
        }
      },
      {
        "from": "learningBack/tests/test_profile_coverage.py",
        "to": "learningBack/tests/test_profile_build.py",
        "evidence": {
          "path": "learningBack/tests/test_profile_coverage.py",
          "line": 15,
          "fragment": "from tests.test_profile_build import profile"
        }
      },
      {
        "from": "learningBack/tests/test_profile_fill.py",
        "to": "learningBack/core/__init__.py",
        "evidence": {
          "path": "learningBack/tests/test_profile_fill.py",
          "line": 7,
          "fragment": "from core import ai_gateway"
        }
      },
      {
        "from": "learningBack/tests/test_profile_fill.py",
        "to": "learningBack/core/ai_gateway.py",
        "evidence": {
          "path": "learningBack/tests/test_profile_fill.py",
          "line": 7,
          "fragment": "from core import ai_gateway"
        }
      },
      {
        "from": "learningBack/tests/test_profile_fill.py",
        "to": "learningBack/core/jobs.py",
        "evidence": {
          "path": "learningBack/tests/test_profile_fill.py",
          "line": 8,
          "fragment": "from core.jobs import process_job"
        }
      },
      {
        "from": "learningBack/tests/test_profile_fill.py",
        "to": "learningBack/modules/knowledge/__init__.py",
        "evidence": {
          "path": "learningBack/tests/test_profile_fill.py",
          "line": 9,
          "fragment": "from modules.knowledge import goal_intake, profile_fill, profile_store, skill_profile"
        }
      },
      {
        "from": "learningBack/tests/test_profile_fill.py",
        "to": "learningBack/modules/knowledge/goal_intake.py",
        "evidence": {
          "path": "learningBack/tests/test_profile_fill.py",
          "line": 9,
          "fragment": "from modules.knowledge import goal_intake, profile_fill, profile_store, skill_profile"
        }
      },
      {
        "from": "learningBack/tests/test_profile_fill.py",
        "to": "learningBack/modules/knowledge/profile_fill.py",
        "evidence": {
          "path": "learningBack/tests/test_profile_fill.py",
          "line": 9,
          "fragment": "from modules.knowledge import goal_intake, profile_fill, profile_store, skill_profile"
        }
      },
      {
        "from": "learningBack/tests/test_profile_fill.py",
        "to": "learningBack/modules/knowledge/profile_store.py",
        "evidence": {
          "path": "learningBack/tests/test_profile_fill.py",
          "line": 9,
          "fragment": "from modules.knowledge import goal_intake, profile_fill, profile_store, skill_profile"
        }
      },
      {
        "from": "learningBack/tests/test_profile_fill.py",
        "to": "learningBack/modules/knowledge/skill_profile.py",
        "evidence": {
          "path": "learningBack/tests/test_profile_fill.py",
          "line": 9,
          "fragment": "from modules.knowledge import goal_intake, profile_fill, profile_store, skill_profile"
        }
      },
      {
        "from": "learningBack/tests/test_profile_fill.py",
        "to": "learningBack/modules/knowledge/models.py",
        "evidence": {
          "path": "learningBack/tests/test_profile_fill.py",
          "line": 10,
          "fragment": "from modules.knowledge.models import Concept"
        }
      },
      {
        "from": "learningBack/tests/test_profile_fill.py",
        "to": "learningBack/tests/conftest.py",
        "evidence": {
          "path": "learningBack/tests/test_profile_fill.py",
          "line": 11,
          "fragment": "from tests.conftest import make_user"
        }
      },
      {
        "from": "learningBack/tests/test_profile_match.py",
        "to": "learningBack/core/config.py",
        "evidence": {
          "path": "learningBack/tests/test_profile_match.py",
          "line": 9,
          "fragment": "from core.config import settings"
        }
      },
      {
        "from": "learningBack/tests/test_profile_match.py",
        "to": "learningBack/modules/knowledge/__init__.py",
        "evidence": {
          "path": "learningBack/tests/test_profile_match.py",
          "line": 10,
          "fragment": "from modules.knowledge import domains, profile_match, profile_store"
        }
      },
      {
        "from": "learningBack/tests/test_profile_match.py",
        "to": "learningBack/modules/knowledge/domains.py",
        "evidence": {
          "path": "learningBack/tests/test_profile_match.py",
          "line": 10,
          "fragment": "from modules.knowledge import domains, profile_match, profile_store"
        }
      },
      {
        "from": "learningBack/tests/test_profile_match.py",
        "to": "learningBack/modules/knowledge/profile_match.py",
        "evidence": {
          "path": "learningBack/tests/test_profile_match.py",
          "line": 10,
          "fragment": "from modules.knowledge import domains, profile_match, profile_store"
        }
      },
      {
        "from": "learningBack/tests/test_profile_match.py",
        "to": "learningBack/modules/knowledge/profile_store.py",
        "evidence": {
          "path": "learningBack/tests/test_profile_match.py",
          "line": 10,
          "fragment": "from modules.knowledge import domains, profile_match, profile_store"
        }
      },
      {
        "from": "learningBack/tests/test_profile_match.py",
        "to": "learningBack/modules/knowledge/models.py",
        "evidence": {
          "path": "learningBack/tests/test_profile_match.py",
          "line": 11,
          "fragment": "from modules.knowledge.models import Concept, SkillProfile"
        }
      },
      {
        "from": "learningBack/tests/test_profile_match.py",
        "to": "learningBack/tests/conftest.py",
        "evidence": {
          "path": "learningBack/tests/test_profile_match.py",
          "line": 12,
          "fragment": "from tests.conftest import make_user"
        }
      },
      {
        "from": "learningBack/tests/test_profile_match.py",
        "to": "learningBack/modules/knowledge/skill_profile.py",
        "evidence": {
          "path": "learningBack/tests/test_profile_match.py",
          "line": 188,
          "fragment": "from modules.knowledge import skill_profile"
        }
      },
      {
        "from": "learningBack/tests/test_profile_match.py",
        "to": "learningBack/core/ai_base.py",
        "evidence": {
          "path": "learningBack/tests/test_profile_match.py",
          "line": 212,
          "fragment": "from core.ai_base import ProviderError"
        }
      },
      {
        "from": "learningBack/tests/test_profile_sources.py",
        "to": "learningBack/core/__init__.py",
        "evidence": {
          "path": "learningBack/tests/test_profile_sources.py",
          "line": 7,
          "fragment": "from core import objects"
        }
      },
      {
        "from": "learningBack/tests/test_profile_sources.py",
        "to": "learningBack/core/objects.py",
        "evidence": {
          "path": "learningBack/tests/test_profile_sources.py",
          "line": 7,
          "fragment": "from core import objects"
        }
      },
      {
        "from": "learningBack/tests/test_profile_sources.py",
        "to": "learningBack/core/config.py",
        "evidence": {
          "path": "learningBack/tests/test_profile_sources.py",
          "line": 8,
          "fragment": "from core.config import settings"
        }
      },
      {
        "from": "learningBack/tests/test_profile_sources.py",
        "to": "learningBack/core/jobs.py",
        "evidence": {
          "path": "learningBack/tests/test_profile_sources.py",
          "line": 9,
          "fragment": "from core.jobs import process_job"
        }
      },
      {
        "from": "learningBack/tests/test_profile_sources.py",
        "to": "learningBack/core/models.py",
        "evidence": {
          "path": "learningBack/tests/test_profile_sources.py",
          "line": 10,
          "fragment": "from core.models import Job"
        }
      },
      {
        "from": "learningBack/tests/test_profile_sources.py",
        "to": "learningBack/modules/knowledge/__init__.py",
        "evidence": {
          "path": "learningBack/tests/test_profile_sources.py",
          "line": 12,
          "fragment": "from modules.knowledge import ("
        }
      },
      {
        "from": "learningBack/tests/test_profile_sources.py",
        "to": "learningBack/modules/knowledge/models.py",
        "evidence": {
          "path": "learningBack/tests/test_profile_sources.py",
          "line": 19,
          "fragment": "from modules.knowledge.models import SourceDocument"
        }
      },
      {
        "from": "learningBack/tests/test_profile_sources.py",
        "to": "learningBack/modules/knowledge/source_search.py",
        "evidence": {
          "path": "learningBack/tests/test_profile_sources.py",
          "line": 20,
          "fragment": "from modules.knowledge.source_search import Candidate"
        }
      },
      {
        "from": "learningBack/tests/test_profile_sources.py",
        "to": "learningBack/tests/conftest.py",
        "evidence": {
          "path": "learningBack/tests/test_profile_sources.py",
          "line": 21,
          "fragment": "from tests.conftest import make_user"
        }
      },
      {
        "from": "learningBack/tests/test_profile_start.py",
        "to": "learningBack/core/__init__.py",
        "evidence": {
          "path": "learningBack/tests/test_profile_start.py",
          "line": 9,
          "fragment": "from core import ai_gateway"
        }
      },
      {
        "from": "learningBack/tests/test_profile_start.py",
        "to": "learningBack/core/ai_gateway.py",
        "evidence": {
          "path": "learningBack/tests/test_profile_start.py",
          "line": 9,
          "fragment": "from core import ai_gateway"
        }
      },
      {
        "from": "learningBack/tests/test_profile_start.py",
        "to": "learningBack/core/jobs.py",
        "evidence": {
          "path": "learningBack/tests/test_profile_start.py",
          "line": 10,
          "fragment": "from core.jobs import process_job"
        }
      },
      {
        "from": "learningBack/tests/test_profile_start.py",
        "to": "learningBack/modules/knowledge/__init__.py",
        "evidence": {
          "path": "learningBack/tests/test_profile_start.py",
          "line": 11,
          "fragment": "from modules.knowledge import goal_intake, profile_store, skill_profile"
        }
      },
      {
        "from": "learningBack/tests/test_profile_start.py",
        "to": "learningBack/modules/knowledge/goal_intake.py",
        "evidence": {
          "path": "learningBack/tests/test_profile_start.py",
          "line": 11,
          "fragment": "from modules.knowledge import goal_intake, profile_store, skill_profile"
        }
      },
      {
        "from": "learningBack/tests/test_profile_start.py",
        "to": "learningBack/modules/knowledge/profile_store.py",
        "evidence": {
          "path": "learningBack/tests/test_profile_start.py",
          "line": 11,
          "fragment": "from modules.knowledge import goal_intake, profile_store, skill_profile"
        }
      },
      {
        "from": "learningBack/tests/test_profile_start.py",
        "to": "learningBack/modules/knowledge/skill_profile.py",
        "evidence": {
          "path": "learningBack/tests/test_profile_start.py",
          "line": 11,
          "fragment": "from modules.knowledge import goal_intake, profile_store, skill_profile"
        }
      },
      {
        "from": "learningBack/tests/test_profile_start.py",
        "to": "learningBack/modules/knowledge/models.py",
        "evidence": {
          "path": "learningBack/tests/test_profile_start.py",
          "line": 12,
          "fragment": "from modules.knowledge.models import Concept"
        }
      },
      {
        "from": "learningBack/tests/test_profile_start.py",
        "to": "learningBack/tests/conftest.py",
        "evidence": {
          "path": "learningBack/tests/test_profile_start.py",
          "line": 13,
          "fragment": "from tests.conftest import make_user"
        }
      },
      {
        "from": "learningBack/tests/test_provenance.py",
        "to": "learningBack/core/objects.py",
        "evidence": {
          "path": "learningBack/tests/test_provenance.py",
          "line": 10,
          "fragment": "from core.objects import MemoryObjectStore, ObjectNotFound"
        }
      },
      {
        "from": "learningBack/tests/test_provenance.py",
        "to": "learningBack/modules/knowledge/__init__.py",
        "evidence": {
          "path": "learningBack/tests/test_provenance.py",
          "line": 11,
          "fragment": "from modules.knowledge import provenance"
        }
      },
      {
        "from": "learningBack/tests/test_provenance.py",
        "to": "learningBack/modules/knowledge/provenance.py",
        "evidence": {
          "path": "learningBack/tests/test_provenance.py",
          "line": 11,
          "fragment": "from modules.knowledge import provenance"
        }
      },
      {
        "from": "learningBack/tests/test_provenance.py",
        "to": "learningBack/modules/knowledge/course.py",
        "evidence": {
          "path": "learningBack/tests/test_provenance.py",
          "line": 12,
          "fragment": "from modules.knowledge.course import generate_course"
        }
      },
      {
        "from": "learningBack/tests/test_provenance.py",
        "to": "learningBack/modules/knowledge/models.py",
        "evidence": {
          "path": "learningBack/tests/test_provenance.py",
          "line": 13,
          "fragment": "from modules.knowledge.models import ("
        }
      },
      {
        "from": "learningBack/tests/test_provenance.py",
        "to": "learningBack/tests/conftest.py",
        "evidence": {
          "path": "learningBack/tests/test_provenance.py",
          "line": 23,
          "fragment": "from tests.conftest import make_user"
        }
      },
      {
        "from": "learningBack/tests/test_provenance.py",
        "to": "learningBack/core/__init__.py",
        "evidence": {
          "path": "learningBack/tests/test_provenance.py",
          "line": 311,
          "fragment": "from core import objects"
        }
      },
      {
        "from": "learningBack/tests/test_push.py",
        "to": "learningBack/core/__init__.py",
        "evidence": {
          "path": "learningBack/tests/test_push.py",
          "line": 8,
          "fragment": "from core import push"
        }
      },
      {
        "from": "learningBack/tests/test_push.py",
        "to": "learningBack/core/push.py",
        "evidence": {
          "path": "learningBack/tests/test_push.py",
          "line": 8,
          "fragment": "from core import push"
        }
      },
      {
        "from": "learningBack/tests/test_push.py",
        "to": "learningBack/core/config.py",
        "evidence": {
          "path": "learningBack/tests/test_push.py",
          "line": 9,
          "fragment": "from core.config import settings"
        }
      },
      {
        "from": "learningBack/tests/test_push.py",
        "to": "learningBack/core/models.py",
        "evidence": {
          "path": "learningBack/tests/test_push.py",
          "line": 10,
          "fragment": "from core.models import Job, PushDevice"
        }
      },
      {
        "from": "learningBack/tests/test_push.py",
        "to": "learningBack/modules/knowledge/__init__.py",
        "evidence": {
          "path": "learningBack/tests/test_push.py",
          "line": 11,
          "fragment": "from modules.knowledge import notifications, provenance"
        }
      },
      {
        "from": "learningBack/tests/test_push.py",
        "to": "learningBack/modules/knowledge/notifications.py",
        "evidence": {
          "path": "learningBack/tests/test_push.py",
          "line": 11,
          "fragment": "from modules.knowledge import notifications, provenance"
        }
      },
      {
        "from": "learningBack/tests/test_push.py",
        "to": "learningBack/modules/knowledge/provenance.py",
        "evidence": {
          "path": "learningBack/tests/test_push.py",
          "line": 11,
          "fragment": "from modules.knowledge import notifications, provenance"
        }
      },
      {
        "from": "learningBack/tests/test_push.py",
        "to": "learningBack/modules/knowledge/models.py",
        "evidence": {
          "path": "learningBack/tests/test_push.py",
          "line": 12,
          "fragment": "from modules.knowledge.models import Notification"
        }
      },
      {
        "from": "learningBack/tests/test_push.py",
        "to": "learningBack/tests/conftest.py",
        "evidence": {
          "path": "learningBack/tests/test_push.py",
          "line": 13,
          "fragment": "from tests.conftest import make_user"
        }
      },
      {
        "from": "learningBack/tests/test_push.py",
        "to": "learningBack/tests/test_notifications.py",
        "evidence": {
          "path": "learningBack/tests/test_push.py",
          "line": 14,
          "fragment": "from tests.test_notifications import DOMAIN, As, concept, learner_with_course"
        }
      },
      {
        "from": "learningBack/tests/test_push.py",
        "to": "learningBack/core/jobs.py",
        "evidence": {
          "path": "learningBack/tests/test_push.py",
          "line": 186,
          "fragment": "from core.jobs import process_job"
        }
      },
      {
        "from": "learningBack/tests/test_push.py",
        "to": "learningBack/core/userdata.py",
        "evidence": {
          "path": "learningBack/tests/test_push.py",
          "line": 261,
          "fragment": "from core import userdata"
        }
      },
      {
        "from": "learningBack/tests/test_review.py",
        "to": "learningBack/core/objects.py",
        "evidence": {
          "path": "learningBack/tests/test_review.py",
          "line": 7,
          "fragment": "from core.objects import MemoryObjectStore"
        }
      },
      {
        "from": "learningBack/tests/test_review.py",
        "to": "learningBack/modules/knowledge/__init__.py",
        "evidence": {
          "path": "learningBack/tests/test_review.py",
          "line": 8,
          "fragment": "from modules.knowledge import merge, provenance"
        }
      },
      {
        "from": "learningBack/tests/test_review.py",
        "to": "learningBack/modules/knowledge/merge.py",
        "evidence": {
          "path": "learningBack/tests/test_review.py",
          "line": 8,
          "fragment": "from modules.knowledge import merge, provenance"
        }
      },
      {
        "from": "learningBack/tests/test_review.py",
        "to": "learningBack/modules/knowledge/provenance.py",
        "evidence": {
          "path": "learningBack/tests/test_review.py",
          "line": 8,
          "fragment": "from modules.knowledge import merge, provenance"
        }
      },
      {
        "from": "learningBack/tests/test_review.py",
        "to": "learningBack/modules/knowledge/models.py",
        "evidence": {
          "path": "learningBack/tests/test_review.py",
          "line": 9,
          "fragment": "from modules.knowledge.models import ("
        }
      },
      {
        "from": "learningBack/tests/test_review.py",
        "to": "learningBack/tests/conftest.py",
        "evidence": {
          "path": "learningBack/tests/test_review.py",
          "line": 16,
          "fragment": "from tests.conftest import make_user"
        }
      },
      {
        "from": "learningBack/tests/test_skill_profile.py",
        "to": "learningBack/core/__init__.py",
        "evidence": {
          "path": "learningBack/tests/test_skill_profile.py",
          "line": 7,
          "fragment": "from core import ai_gateway"
        }
      },
      {
        "from": "learningBack/tests/test_skill_profile.py",
        "to": "learningBack/core/ai_gateway.py",
        "evidence": {
          "path": "learningBack/tests/test_skill_profile.py",
          "line": 7,
          "fragment": "from core import ai_gateway"
        }
      },
      {
        "from": "learningBack/tests/test_skill_profile.py",
        "to": "learningBack/core/jobs.py",
        "evidence": {
          "path": "learningBack/tests/test_skill_profile.py",
          "line": 8,
          "fragment": "from core.jobs import process_job"
        }
      },
      {
        "from": "learningBack/tests/test_skill_profile.py",
        "to": "learningBack/modules/knowledge/__init__.py",
        "evidence": {
          "path": "learningBack/tests/test_skill_profile.py",
          "line": 9,
          "fragment": "from modules.knowledge import goal_intake, profile_store, skill_profile"
        }
      },
      {
        "from": "learningBack/tests/test_skill_profile.py",
        "to": "learningBack/modules/knowledge/goal_intake.py",
        "evidence": {
          "path": "learningBack/tests/test_skill_profile.py",
          "line": 9,
          "fragment": "from modules.knowledge import goal_intake, profile_store, skill_profile"
        }
      },
      {
        "from": "learningBack/tests/test_skill_profile.py",
        "to": "learningBack/modules/knowledge/profile_store.py",
        "evidence": {
          "path": "learningBack/tests/test_skill_profile.py",
          "line": 9,
          "fragment": "from modules.knowledge import goal_intake, profile_store, skill_profile"
        }
      },
      {
        "from": "learningBack/tests/test_skill_profile.py",
        "to": "learningBack/modules/knowledge/skill_profile.py",
        "evidence": {
          "path": "learningBack/tests/test_skill_profile.py",
          "line": 9,
          "fragment": "from modules.knowledge import goal_intake, profile_store, skill_profile"
        }
      },
      {
        "from": "learningBack/tests/test_skill_profile.py",
        "to": "learningBack/modules/knowledge/models.py",
        "evidence": {
          "path": "learningBack/tests/test_skill_profile.py",
          "line": 10,
          "fragment": "from modules.knowledge.models import SkillProfile"
        }
      },
      {
        "from": "learningBack/tests/test_skill_profile.py",
        "to": "learningBack/tests/conftest.py",
        "evidence": {
          "path": "learningBack/tests/test_skill_profile.py",
          "line": 11,
          "fragment": "from tests.conftest import make_user"
        }
      },
      {
        "from": "learningBack/tests/test_source_search.py",
        "to": "learningBack/core/__init__.py",
        "evidence": {
          "path": "learningBack/tests/test_source_search.py",
          "line": 10,
          "fragment": "from core import objects"
        }
      },
      {
        "from": "learningBack/tests/test_source_search.py",
        "to": "learningBack/core/objects.py",
        "evidence": {
          "path": "learningBack/tests/test_source_search.py",
          "line": 10,
          "fragment": "from core import objects"
        }
      },
      {
        "from": "learningBack/tests/test_source_search.py",
        "to": "learningBack/core/config.py",
        "evidence": {
          "path": "learningBack/tests/test_source_search.py",
          "line": 11,
          "fragment": "from core.config import settings"
        }
      },
      {
        "from": "learningBack/tests/test_source_search.py",
        "to": "learningBack/core/models.py",
        "evidence": {
          "path": "learningBack/tests/test_source_search.py",
          "line": 12,
          "fragment": "from core.models import Job"
        }
      },
      {
        "from": "learningBack/tests/test_source_search.py",
        "to": "learningBack/modules/knowledge/__init__.py",
        "evidence": {
          "path": "learningBack/tests/test_source_search.py",
          "line": 14,
          "fragment": "from modules.knowledge import provenance, source_search"
        }
      },
      {
        "from": "learningBack/tests/test_source_search.py",
        "to": "learningBack/modules/knowledge/provenance.py",
        "evidence": {
          "path": "learningBack/tests/test_source_search.py",
          "line": 14,
          "fragment": "from modules.knowledge import provenance, source_search"
        }
      },
      {
        "from": "learningBack/tests/test_source_search.py",
        "to": "learningBack/modules/knowledge/source_search.py",
        "evidence": {
          "path": "learningBack/tests/test_source_search.py",
          "line": 14,
          "fragment": "from modules.knowledge import provenance, source_search"
        }
      },
      {
        "from": "learningBack/tests/test_source_search.py",
        "to": "learningBack/modules/knowledge/models.py",
        "evidence": {
          "path": "learningBack/tests/test_source_search.py",
          "line": 15,
          "fragment": "from modules.knowledge.models import SourceDocument"
        }
      },
      {
        "from": "learningBack/tests/test_source_search.py",
        "to": "learningBack/tests/conftest.py",
        "evidence": {
          "path": "learningBack/tests/test_source_search.py",
          "line": 23,
          "fragment": "from tests.conftest import make_user"
        }
      },
      {
        "from": "learningBack/tests/test_source_upload.py",
        "to": "learningBack/core/__init__.py",
        "evidence": {
          "path": "learningBack/tests/test_source_upload.py",
          "line": 10,
          "fragment": "from core import objects"
        }
      },
      {
        "from": "learningBack/tests/test_source_upload.py",
        "to": "learningBack/core/objects.py",
        "evidence": {
          "path": "learningBack/tests/test_source_upload.py",
          "line": 10,
          "fragment": "from core import objects"
        }
      },
      {
        "from": "learningBack/tests/test_source_upload.py",
        "to": "learningBack/core/config.py",
        "evidence": {
          "path": "learningBack/tests/test_source_upload.py",
          "line": 11,
          "fragment": "from core.config import settings"
        }
      },
      {
        "from": "learningBack/tests/test_source_upload.py",
        "to": "learningBack/core/jobs.py",
        "evidence": {
          "path": "learningBack/tests/test_source_upload.py",
          "line": 12,
          "fragment": "from core.jobs import process_job"
        }
      },
      {
        "from": "learningBack/tests/test_source_upload.py",
        "to": "learningBack/core/models.py",
        "evidence": {
          "path": "learningBack/tests/test_source_upload.py",
          "line": 13,
          "fragment": "from core.models import Job"
        }
      },
      {
        "from": "learningBack/tests/test_source_upload.py",
        "to": "learningBack/modules/knowledge/__init__.py",
        "evidence": {
          "path": "learningBack/tests/test_source_upload.py",
          "line": 15,
          "fragment": "from modules.knowledge import provenance"
        }
      },
      {
        "from": "learningBack/tests/test_source_upload.py",
        "to": "learningBack/modules/knowledge/provenance.py",
        "evidence": {
          "path": "learningBack/tests/test_source_upload.py",
          "line": 15,
          "fragment": "from modules.knowledge import provenance"
        }
      },
      {
        "from": "learningBack/tests/test_source_upload.py",
        "to": "learningBack/modules/knowledge/models.py",
        "evidence": {
          "path": "learningBack/tests/test_source_upload.py",
          "line": 16,
          "fragment": "from modules.knowledge.models import Concept, SourceDocument, SourceFragment"
        }
      },
      {
        "from": "learningBack/tests/test_source_upload.py",
        "to": "learningBack/tests/conftest.py",
        "evidence": {
          "path": "learningBack/tests/test_source_upload.py",
          "line": 17,
          "fragment": "from tests.conftest import make_user"
        }
      },
      {
        "from": "learningBack/tests/test_sources_admin_only.py",
        "to": "learningBack/api/app.py",
        "evidence": {
          "path": "learningBack/tests/test_sources_admin_only.py",
          "line": 14,
          "fragment": "from api.app import app"
        }
      },
      {
        "from": "learningBack/tests/test_sources_admin_only.py",
        "to": "learningBack/core/__init__.py",
        "evidence": {
          "path": "learningBack/tests/test_sources_admin_only.py",
          "line": 15,
          "fragment": "from core import objects"
        }
      },
      {
        "from": "learningBack/tests/test_sources_admin_only.py",
        "to": "learningBack/core/objects.py",
        "evidence": {
          "path": "learningBack/tests/test_sources_admin_only.py",
          "line": 15,
          "fragment": "from core import objects"
        }
      },
      {
        "from": "learningBack/tests/test_sources_admin_only.py",
        "to": "learningBack/modules/knowledge/__init__.py",
        "evidence": {
          "path": "learningBack/tests/test_sources_admin_only.py",
          "line": 17,
          "fragment": "from modules.knowledge import provenance"
        }
      },
      {
        "from": "learningBack/tests/test_sources_admin_only.py",
        "to": "learningBack/modules/knowledge/provenance.py",
        "evidence": {
          "path": "learningBack/tests/test_sources_admin_only.py",
          "line": 17,
          "fragment": "from modules.knowledge import provenance"
        }
      },
      {
        "from": "learningBack/tests/test_sources_admin_only.py",
        "to": "learningBack/modules/knowledge/course.py",
        "evidence": {
          "path": "learningBack/tests/test_sources_admin_only.py",
          "line": 18,
          "fragment": "from modules.knowledge.course import generate_course"
        }
      },
      {
        "from": "learningBack/tests/test_sources_admin_only.py",
        "to": "learningBack/modules/knowledge/models.py",
        "evidence": {
          "path": "learningBack/tests/test_sources_admin_only.py",
          "line": 19,
          "fragment": "from modules.knowledge.models import Concept, ConceptEdge"
        }
      },
      {
        "from": "learningBack/tests/test_sources_admin_only.py",
        "to": "learningBack/tests/conftest.py",
        "evidence": {
          "path": "learningBack/tests/test_sources_admin_only.py",
          "line": 20,
          "fragment": "from tests.conftest import make_user"
        }
      },
      {
        "from": "learningBack/tests/test_stage_level.py",
        "to": "learningBack/modules/knowledge/__init__.py",
        "evidence": {
          "path": "learningBack/tests/test_stage_level.py",
          "line": 5,
          "fragment": "from modules.knowledge import merge, stages"
        }
      },
      {
        "from": "learningBack/tests/test_stage_level.py",
        "to": "learningBack/modules/knowledge/merge.py",
        "evidence": {
          "path": "learningBack/tests/test_stage_level.py",
          "line": 5,
          "fragment": "from modules.knowledge import merge, stages"
        }
      },
      {
        "from": "learningBack/tests/test_stage_level.py",
        "to": "learningBack/modules/knowledge/stages.py",
        "evidence": {
          "path": "learningBack/tests/test_stage_level.py",
          "line": 5,
          "fragment": "from modules.knowledge import merge, stages"
        }
      },
      {
        "from": "learningBack/tests/test_stage_level.py",
        "to": "learningBack/modules/knowledge/cow.py",
        "evidence": {
          "path": "learningBack/tests/test_stage_level.py",
          "line": 6,
          "fragment": "from modules.knowledge.cow import effective_graph"
        }
      },
      {
        "from": "learningBack/tests/test_stage_level.py",
        "to": "learningBack/modules/knowledge/course.py",
        "evidence": {
          "path": "learningBack/tests/test_stage_level.py",
          "line": 7,
          "fragment": "from modules.knowledge.course import build_path"
        }
      },
      {
        "from": "learningBack/tests/test_stage_level.py",
        "to": "learningBack/modules/knowledge/models.py",
        "evidence": {
          "path": "learningBack/tests/test_stage_level.py",
          "line": 8,
          "fragment": "from modules.knowledge.models import Concept"
        }
      },
      {
        "from": "learningBack/tests/test_stage_level.py",
        "to": "learningBack/modules/knowledge/router.py",
        "evidence": {
          "path": "learningBack/tests/test_stage_level.py",
          "line": 9,
          "fragment": "from modules.knowledge.router import _persist_draft"
        }
      },
      {
        "from": "learningBack/tests/test_stage_level.py",
        "to": "learningBack/tests/conftest.py",
        "evidence": {
          "path": "learningBack/tests/test_stage_level.py",
          "line": 10,
          "fragment": "from tests.conftest import make_user"
        }
      },
      {
        "from": "learningBack/tests/test_v0130_claims_extraction.py",
        "to": "learningBack/core/config.py",
        "evidence": {
          "path": "learningBack/tests/test_v0130_claims_extraction.py",
          "line": 10,
          "fragment": "from core.config import settings"
        }
      },
      {
        "from": "learningBack/tests/test_v0130_claims_extraction.py",
        "to": "learningBack/core/objects.py",
        "evidence": {
          "path": "learningBack/tests/test_v0130_claims_extraction.py",
          "line": 11,
          "fragment": "from core.objects import MemoryObjectStore"
        }
      },
      {
        "from": "learningBack/tests/test_v0130_claims_extraction.py",
        "to": "learningBack/modules/knowledge/__init__.py",
        "evidence": {
          "path": "learningBack/tests/test_v0130_claims_extraction.py",
          "line": 12,
          "fragment": "from modules.knowledge import ingest, provenance"
        }
      },
      {
        "from": "learningBack/tests/test_v0130_claims_extraction.py",
        "to": "learningBack/modules/knowledge/ingest.py",
        "evidence": {
          "path": "learningBack/tests/test_v0130_claims_extraction.py",
          "line": 12,
          "fragment": "from modules.knowledge import ingest, provenance"
        }
      },
      {
        "from": "learningBack/tests/test_v0130_claims_extraction.py",
        "to": "learningBack/modules/knowledge/provenance.py",
        "evidence": {
          "path": "learningBack/tests/test_v0130_claims_extraction.py",
          "line": 12,
          "fragment": "from modules.knowledge import ingest, provenance"
        }
      },
      {
        "from": "learningBack/tests/test_v0130_claims_extraction.py",
        "to": "learningBack/modules/knowledge/models.py",
        "evidence": {
          "path": "learningBack/tests/test_v0130_claims_extraction.py",
          "line": 13,
          "fragment": "from modules.knowledge.models import Claim, ClaimSource, ConceptArea, ConceptTerm, SourceFragment"
        }
      },
      {
        "from": "learningBack/tests/test_v0130_claims_extraction.py",
        "to": "learningBack/tests/kg_helpers.py",
        "evidence": {
          "path": "learningBack/tests/test_v0130_claims_extraction.py",
          "line": 14,
          "fragment": "from tests.kg_helpers import Gateway"
        }
      },
      {
        "from": "learningBack/tests/test_v0131_licenses_visibility.py",
        "to": "learningBack/core/config.py",
        "evidence": {
          "path": "learningBack/tests/test_v0131_licenses_visibility.py",
          "line": 10,
          "fragment": "from core.config import settings"
        }
      },
      {
        "from": "learningBack/tests/test_v0131_licenses_visibility.py",
        "to": "learningBack/modules/knowledge/__init__.py",
        "evidence": {
          "path": "learningBack/tests/test_v0131_licenses_visibility.py",
          "line": 11,
          "fragment": "from modules.knowledge import funnel"
        }
      },
      {
        "from": "learningBack/tests/test_v0131_licenses_visibility.py",
        "to": "learningBack/modules/knowledge/funnel.py",
        "evidence": {
          "path": "learningBack/tests/test_v0131_licenses_visibility.py",
          "line": 11,
          "fragment": "from modules.knowledge import funnel"
        }
      },
      {
        "from": "learningBack/tests/test_v0131_licenses_visibility.py",
        "to": "learningBack/tests/conftest.py",
        "evidence": {
          "path": "learningBack/tests/test_v0131_licenses_visibility.py",
          "line": 12,
          "fragment": "from tests.conftest import make_user"
        }
      },
      {
        "from": "learningBack/tests/test_v0131_licenses_visibility.py",
        "to": "learningBack/tests/kg_helpers.py",
        "evidence": {
          "path": "learningBack/tests/test_v0131_licenses_visibility.py",
          "line": 13,
          "fragment": "from tests.kg_helpers import Gateway, claim, concept, document"
        }
      },
      {
        "from": "learningBack/tests/test_v0132_concept_in_two_areas.py",
        "to": "learningBack/core/embeddings.py",
        "evidence": {
          "path": "learningBack/tests/test_v0132_concept_in_two_areas.py",
          "line": 5,
          "fragment": "from core.embeddings import HashEmbedder"
        }
      },
      {
        "from": "learningBack/tests/test_v0132_concept_in_two_areas.py",
        "to": "learningBack/modules/knowledge/__init__.py",
        "evidence": {
          "path": "learningBack/tests/test_v0132_concept_in_two_areas.py",
          "line": 6,
          "fragment": "from modules.knowledge import merge"
        }
      },
      {
        "from": "learningBack/tests/test_v0132_concept_in_two_areas.py",
        "to": "learningBack/modules/knowledge/merge.py",
        "evidence": {
          "path": "learningBack/tests/test_v0132_concept_in_two_areas.py",
          "line": 6,
          "fragment": "from modules.knowledge import merge"
        }
      },
      {
        "from": "learningBack/tests/test_v0132_concept_in_two_areas.py",
        "to": "learningBack/modules/knowledge/course.py",
        "evidence": {
          "path": "learningBack/tests/test_v0132_concept_in_two_areas.py",
          "line": 7,
          "fragment": "from modules.knowledge.course import build_path"
        }
      },
      {
        "from": "learningBack/tests/test_v0132_concept_in_two_areas.py",
        "to": "learningBack/modules/knowledge/cow.py",
        "evidence": {
          "path": "learningBack/tests/test_v0132_concept_in_two_areas.py",
          "line": 8,
          "fragment": "from modules.knowledge.cow import effective_graph"
        }
      },
      {
        "from": "learningBack/tests/test_v0132_concept_in_two_areas.py",
        "to": "learningBack/modules/knowledge/mastery.py",
        "evidence": {
          "path": "learningBack/tests/test_v0132_concept_in_two_areas.py",
          "line": 9,
          "fragment": "from modules.knowledge.mastery import MasteryState, load_map, save_state"
        }
      },
      {
        "from": "learningBack/tests/test_v0132_concept_in_two_areas.py",
        "to": "learningBack/modules/knowledge/models.py",
        "evidence": {
          "path": "learningBack/tests/test_v0132_concept_in_two_areas.py",
          "line": 10,
          "fragment": "from modules.knowledge.models import Concept, ConceptArea, ConceptSource"
        }
      },
      {
        "from": "learningBack/tests/test_v0132_concept_in_two_areas.py",
        "to": "learningBack/tests/conftest.py",
        "evidence": {
          "path": "learningBack/tests/test_v0132_concept_in_two_areas.py",
          "line": 11,
          "fragment": "from tests.conftest import make_user"
        }
      },
      {
        "from": "learningBack/tests/test_v0132_concept_in_two_areas.py",
        "to": "learningBack/tests/kg_helpers.py",
        "evidence": {
          "path": "learningBack/tests/test_v0132_concept_in_two_areas.py",
          "line": 12,
          "fragment": "from tests.kg_helpers import Gateway, claim, concept, document"
        }
      },
      {
        "from": "learningBack/tests/test_v0132_concept_in_two_areas.py",
        "to": "learningBack/modules/knowledge/provenance.py",
        "evidence": {
          "path": "learningBack/tests/test_v0132_concept_in_two_areas.py",
          "line": 38,
          "fragment": "from modules.knowledge import provenance"
        }
      },
      {
        "from": "learningBack/tests/test_v0133_reconcile_pool.py",
        "to": "learningBack/modules/knowledge/__init__.py",
        "evidence": {
          "path": "learningBack/tests/test_v0133_reconcile_pool.py",
          "line": 5,
          "fragment": "from modules.knowledge import node_compile, reconcile"
        }
      },
      {
        "from": "learningBack/tests/test_v0133_reconcile_pool.py",
        "to": "learningBack/modules/knowledge/node_compile.py",
        "evidence": {
          "path": "learningBack/tests/test_v0133_reconcile_pool.py",
          "line": 5,
          "fragment": "from modules.knowledge import node_compile, reconcile"
        }
      },
      {
        "from": "learningBack/tests/test_v0133_reconcile_pool.py",
        "to": "learningBack/modules/knowledge/reconcile.py",
        "evidence": {
          "path": "learningBack/tests/test_v0133_reconcile_pool.py",
          "line": 5,
          "fragment": "from modules.knowledge import node_compile, reconcile"
        }
      },
      {
        "from": "learningBack/tests/test_v0133_reconcile_pool.py",
        "to": "learningBack/modules/knowledge/models.py",
        "evidence": {
          "path": "learningBack/tests/test_v0133_reconcile_pool.py",
          "line": 6,
          "fragment": "from modules.knowledge.models import Claim, ClaimConflict, ClaimSource"
        }
      },
      {
        "from": "learningBack/tests/test_v0133_reconcile_pool.py",
        "to": "learningBack/tests/kg_helpers.py",
        "evidence": {
          "path": "learningBack/tests/test_v0133_reconcile_pool.py",
          "line": 7,
          "fragment": "from tests.kg_helpers import Gateway, claim, concept, document"
        }
      },
      {
        "from": "learningBack/tests/test_v0134_node_compile_offline.py",
        "to": "learningBack/core/config.py",
        "evidence": {
          "path": "learningBack/tests/test_v0134_node_compile_offline.py",
          "line": 7,
          "fragment": "from core.config import settings"
        }
      },
      {
        "from": "learningBack/tests/test_v0134_node_compile_offline.py",
        "to": "learningBack/modules/knowledge/__init__.py",
        "evidence": {
          "path": "learningBack/tests/test_v0134_node_compile_offline.py",
          "line": 8,
          "fragment": "from modules.knowledge import assessment_store, node_compile"
        }
      },
      {
        "from": "learningBack/tests/test_v0134_node_compile_offline.py",
        "to": "learningBack/modules/knowledge/assessment_store.py",
        "evidence": {
          "path": "learningBack/tests/test_v0134_node_compile_offline.py",
          "line": 8,
          "fragment": "from modules.knowledge import assessment_store, node_compile"
        }
      },
      {
        "from": "learningBack/tests/test_v0134_node_compile_offline.py",
        "to": "learningBack/modules/knowledge/node_compile.py",
        "evidence": {
          "path": "learningBack/tests/test_v0134_node_compile_offline.py",
          "line": 8,
          "fragment": "from modules.knowledge import assessment_store, node_compile"
        }
      },
      {
        "from": "learningBack/tests/test_v0134_node_compile_offline.py",
        "to": "learningBack/modules/knowledge/answer.py",
        "evidence": {
          "path": "learningBack/tests/test_v0134_node_compile_offline.py",
          "line": 9,
          "fragment": "from modules.knowledge.answer import score_answer"
        }
      },
      {
        "from": "learningBack/tests/test_v0134_node_compile_offline.py",
        "to": "learningBack/modules/knowledge/assessment.py",
        "evidence": {
          "path": "learningBack/tests/test_v0134_node_compile_offline.py",
          "line": 10,
          "fragment": "from modules.knowledge.assessment import AssessmentItem"
        }
      },
      {
        "from": "learningBack/tests/test_v0134_node_compile_offline.py",
        "to": "learningBack/modules/knowledge/course.py",
        "evidence": {
          "path": "learningBack/tests/test_v0134_node_compile_offline.py",
          "line": 11,
          "fragment": "from modules.knowledge.course import generate_course"
        }
      },
      {
        "from": "learningBack/tests/test_v0134_node_compile_offline.py",
        "to": "learningBack/modules/knowledge/models.py",
        "evidence": {
          "path": "learningBack/tests/test_v0134_node_compile_offline.py",
          "line": 12,
          "fragment": "from modules.knowledge.models import LearningItem"
        }
      },
      {
        "from": "learningBack/tests/test_v0134_node_compile_offline.py",
        "to": "learningBack/modules/knowledge/study.py",
        "evidence": {
          "path": "learningBack/tests/test_v0134_node_compile_offline.py",
          "line": 13,
          "fragment": "from modules.knowledge.study import start_step"
        }
      },
      {
        "from": "learningBack/tests/test_v0134_node_compile_offline.py",
        "to": "learningBack/tests/conftest.py",
        "evidence": {
          "path": "learningBack/tests/test_v0134_node_compile_offline.py",
          "line": 14,
          "fragment": "from tests.conftest import make_user"
        }
      },
      {
        "from": "learningBack/tests/test_v0134_node_compile_offline.py",
        "to": "learningBack/tests/kg_helpers.py",
        "evidence": {
          "path": "learningBack/tests/test_v0134_node_compile_offline.py",
          "line": 15,
          "fragment": "from tests.kg_helpers import Gateway, claim, concept, document"
        }
      },
      {
        "from": "learningBack/tests/test_v0135_freshness.py",
        "to": "learningBack/core/config.py",
        "evidence": {
          "path": "learningBack/tests/test_v0135_freshness.py",
          "line": 9,
          "fragment": "from core.config import settings"
        }
      },
      {
        "from": "learningBack/tests/test_v0135_freshness.py",
        "to": "learningBack/core/models.py",
        "evidence": {
          "path": "learningBack/tests/test_v0135_freshness.py",
          "line": 10,
          "fragment": "from core.models import Job, SrsCard"
        }
      },
      {
        "from": "learningBack/tests/test_v0135_freshness.py",
        "to": "learningBack/core/srs.py",
        "evidence": {
          "path": "learningBack/tests/test_v0135_freshness.py",
          "line": 11,
          "fragment": "from core.srs import initial_fsrs_state"
        }
      },
      {
        "from": "learningBack/tests/test_v0135_freshness.py",
        "to": "learningBack/modules/knowledge/__init__.py",
        "evidence": {
          "path": "learningBack/tests/test_v0135_freshness.py",
          "line": 12,
          "fragment": "from modules.knowledge import freshness, node_compile, reconcile"
        }
      },
      {
        "from": "learningBack/tests/test_v0135_freshness.py",
        "to": "learningBack/modules/knowledge/freshness.py",
        "evidence": {
          "path": "learningBack/tests/test_v0135_freshness.py",
          "line": 12,
          "fragment": "from modules.knowledge import freshness, node_compile, reconcile"
        }
      },
      {
        "from": "learningBack/tests/test_v0135_freshness.py",
        "to": "learningBack/modules/knowledge/node_compile.py",
        "evidence": {
          "path": "learningBack/tests/test_v0135_freshness.py",
          "line": 12,
          "fragment": "from modules.knowledge import freshness, node_compile, reconcile"
        }
      },
      {
        "from": "learningBack/tests/test_v0135_freshness.py",
        "to": "learningBack/modules/knowledge/reconcile.py",
        "evidence": {
          "path": "learningBack/tests/test_v0135_freshness.py",
          "line": 12,
          "fragment": "from modules.knowledge import freshness, node_compile, reconcile"
        }
      },
      {
        "from": "learningBack/tests/test_v0135_freshness.py",
        "to": "learningBack/modules/knowledge/models.py",
        "evidence": {
          "path": "learningBack/tests/test_v0135_freshness.py",
          "line": 13,
          "fragment": "from modules.knowledge.models import Claim, ClaimConflict"
        }
      },
      {
        "from": "learningBack/tests/test_v0135_freshness.py",
        "to": "learningBack/tests/conftest.py",
        "evidence": {
          "path": "learningBack/tests/test_v0135_freshness.py",
          "line": 14,
          "fragment": "from tests.conftest import make_user"
        }
      },
      {
        "from": "learningBack/tests/test_v0135_freshness.py",
        "to": "learningBack/tests/kg_helpers.py",
        "evidence": {
          "path": "learningBack/tests/test_v0135_freshness.py",
          "line": 15,
          "fragment": "from tests.kg_helpers import Gateway, claim, concept, document"
        }
      },
      {
        "from": "learningBack/tests/test_v0136_consensus_fix.py",
        "to": "learningBack/modules/knowledge/__init__.py",
        "evidence": {
          "path": "learningBack/tests/test_v0136_consensus_fix.py",
          "line": 5,
          "fragment": "from modules.knowledge import freshness, node_compile, reconcile"
        }
      },
      {
        "from": "learningBack/tests/test_v0136_consensus_fix.py",
        "to": "learningBack/modules/knowledge/freshness.py",
        "evidence": {
          "path": "learningBack/tests/test_v0136_consensus_fix.py",
          "line": 5,
          "fragment": "from modules.knowledge import freshness, node_compile, reconcile"
        }
      },
      {
        "from": "learningBack/tests/test_v0136_consensus_fix.py",
        "to": "learningBack/modules/knowledge/node_compile.py",
        "evidence": {
          "path": "learningBack/tests/test_v0136_consensus_fix.py",
          "line": 5,
          "fragment": "from modules.knowledge import freshness, node_compile, reconcile"
        }
      },
      {
        "from": "learningBack/tests/test_v0136_consensus_fix.py",
        "to": "learningBack/modules/knowledge/reconcile.py",
        "evidence": {
          "path": "learningBack/tests/test_v0136_consensus_fix.py",
          "line": 5,
          "fragment": "from modules.knowledge import freshness, node_compile, reconcile"
        }
      },
      {
        "from": "learningBack/tests/test_v0136_consensus_fix.py",
        "to": "learningBack/modules/knowledge/models.py",
        "evidence": {
          "path": "learningBack/tests/test_v0136_consensus_fix.py",
          "line": 6,
          "fragment": "from modules.knowledge.models import Claim, ClaimConflict, Concept, ReviewLog"
        }
      },
      {
        "from": "learningBack/tests/test_v0136_consensus_fix.py",
        "to": "learningBack/tests/conftest.py",
        "evidence": {
          "path": "learningBack/tests/test_v0136_consensus_fix.py",
          "line": 7,
          "fragment": "from tests.conftest import make_user"
        }
      },
      {
        "from": "learningBack/tests/test_v0136_consensus_fix.py",
        "to": "learningBack/tests/kg_helpers.py",
        "evidence": {
          "path": "learningBack/tests/test_v0136_consensus_fix.py",
          "line": 8,
          "fragment": "from tests.kg_helpers import Gateway, claim, concept, document"
        }
      },
      {
        "from": "learningBack/tests/test_v0136_consensus_fix.py",
        "to": "learningBack/modules/knowledge/provenance.py",
        "evidence": {
          "path": "learningBack/tests/test_v0136_consensus_fix.py",
          "line": 114,
          "fragment": "from modules.knowledge import provenance"
        }
      },
      {
        "from": "learningBack/tests/test_v0137_funnel.py",
        "to": "learningBack/core/config.py",
        "evidence": {
          "path": "learningBack/tests/test_v0137_funnel.py",
          "line": 7,
          "fragment": "from core.config import settings"
        }
      },
      {
        "from": "learningBack/tests/test_v0137_funnel.py",
        "to": "learningBack/modules/knowledge/__init__.py",
        "evidence": {
          "path": "learningBack/tests/test_v0137_funnel.py",
          "line": 8,
          "fragment": "from modules.knowledge import funnel, node_compile, reconcile"
        }
      },
      {
        "from": "learningBack/tests/test_v0137_funnel.py",
        "to": "learningBack/modules/knowledge/funnel.py",
        "evidence": {
          "path": "learningBack/tests/test_v0137_funnel.py",
          "line": 8,
          "fragment": "from modules.knowledge import funnel, node_compile, reconcile"
        }
      },
      {
        "from": "learningBack/tests/test_v0137_funnel.py",
        "to": "learningBack/modules/knowledge/node_compile.py",
        "evidence": {
          "path": "learningBack/tests/test_v0137_funnel.py",
          "line": 8,
          "fragment": "from modules.knowledge import funnel, node_compile, reconcile"
        }
      },
      {
        "from": "learningBack/tests/test_v0137_funnel.py",
        "to": "learningBack/modules/knowledge/reconcile.py",
        "evidence": {
          "path": "learningBack/tests/test_v0137_funnel.py",
          "line": 8,
          "fragment": "from modules.knowledge import funnel, node_compile, reconcile"
        }
      },
      {
        "from": "learningBack/tests/test_v0137_funnel.py",
        "to": "learningBack/modules/knowledge/models.py",
        "evidence": {
          "path": "learningBack/tests/test_v0137_funnel.py",
          "line": 9,
          "fragment": "from modules.knowledge.models import ClaimConflict"
        }
      },
      {
        "from": "learningBack/tests/test_v0137_funnel.py",
        "to": "learningBack/tests/kg_helpers.py",
        "evidence": {
          "path": "learningBack/tests/test_v0137_funnel.py",
          "line": 10,
          "fragment": "from tests.kg_helpers import Gateway, claim, concept, document"
        }
      },
      {
        "from": "learningBack/tests/test_v0138_v0139_languages.py",
        "to": "learningBack/core/config.py",
        "evidence": {
          "path": "learningBack/tests/test_v0138_v0139_languages.py",
          "line": 7,
          "fragment": "from core.config import settings"
        }
      },
      {
        "from": "learningBack/tests/test_v0138_v0139_languages.py",
        "to": "learningBack/modules/knowledge/__init__.py",
        "evidence": {
          "path": "learningBack/tests/test_v0138_v0139_languages.py",
          "line": 8,
          "fragment": "from modules.knowledge import funnel, langs, merge, node_compile, profile_sources, provenance"
        }
      },
      {
        "from": "learningBack/tests/test_v0138_v0139_languages.py",
        "to": "learningBack/modules/knowledge/funnel.py",
        "evidence": {
          "path": "learningBack/tests/test_v0138_v0139_languages.py",
          "line": 8,
          "fragment": "from modules.knowledge import funnel, langs, merge, node_compile, profile_sources, provenance"
        }
      },
      {
        "from": "learningBack/tests/test_v0138_v0139_languages.py",
        "to": "learningBack/modules/knowledge/langs.py",
        "evidence": {
          "path": "learningBack/tests/test_v0138_v0139_languages.py",
          "line": 8,
          "fragment": "from modules.knowledge import funnel, langs, merge, node_compile, profile_sources, provenance"
        }
      },
      {
        "from": "learningBack/tests/test_v0138_v0139_languages.py",
        "to": "learningBack/modules/knowledge/merge.py",
        "evidence": {
          "path": "learningBack/tests/test_v0138_v0139_languages.py",
          "line": 8,
          "fragment": "from modules.knowledge import funnel, langs, merge, node_compile, profile_sources, provenance"
        }
      },
      {
        "from": "learningBack/tests/test_v0138_v0139_languages.py",
        "to": "learningBack/modules/knowledge/node_compile.py",
        "evidence": {
          "path": "learningBack/tests/test_v0138_v0139_languages.py",
          "line": 8,
          "fragment": "from modules.knowledge import funnel, langs, merge, node_compile, profile_sources, provenance"
        }
      },
      {
        "from": "learningBack/tests/test_v0138_v0139_languages.py",
        "to": "learningBack/modules/knowledge/profile_sources.py",
        "evidence": {
          "path": "learningBack/tests/test_v0138_v0139_languages.py",
          "line": 8,
          "fragment": "from modules.knowledge import funnel, langs, merge, node_compile, profile_sources, provenance"
        }
      },
      {
        "from": "learningBack/tests/test_v0138_v0139_languages.py",
        "to": "learningBack/modules/knowledge/provenance.py",
        "evidence": {
          "path": "learningBack/tests/test_v0138_v0139_languages.py",
          "line": 8,
          "fragment": "from modules.knowledge import funnel, langs, merge, node_compile, profile_sources, provenance"
        }
      },
      {
        "from": "learningBack/tests/test_v0138_v0139_languages.py",
        "to": "learningBack/modules/knowledge/models.py",
        "evidence": {
          "path": "learningBack/tests/test_v0138_v0139_languages.py",
          "line": 9,
          "fragment": "from modules.knowledge.models import Concept, ConceptSource, ConceptTerm"
        }
      },
      {
        "from": "learningBack/tests/test_v0138_v0139_languages.py",
        "to": "learningBack/tests/conftest.py",
        "evidence": {
          "path": "learningBack/tests/test_v0138_v0139_languages.py",
          "line": 10,
          "fragment": "from tests.conftest import make_user"
        }
      },
      {
        "from": "learningBack/tests/test_v0138_v0139_languages.py",
        "to": "learningBack/tests/kg_helpers.py",
        "evidence": {
          "path": "learningBack/tests/test_v0138_v0139_languages.py",
          "line": 11,
          "fragment": "from tests.kg_helpers import Gateway, claim, concept, document, term"
        }
      },
      {
        "from": "learningBack/tests/test_v0140_server_messages.py",
        "to": "learningBack/core/mail.py",
        "evidence": {
          "path": "learningBack/tests/test_v0140_server_messages.py",
          "line": 5,
          "fragment": "from core.mail import reset_code_message"
        }
      },
      {
        "from": "learningBack/tests/test_v0140_server_messages.py",
        "to": "learningBack/core/messages.py",
        "evidence": {
          "path": "learningBack/tests/test_v0140_server_messages.py",
          "line": 6,
          "fragment": "from core.messages import MESSAGES, msg, user_lang"
        }
      },
      {
        "from": "learningBack/tests/test_v0140_server_messages.py",
        "to": "learningBack/modules/knowledge/__init__.py",
        "evidence": {
          "path": "learningBack/tests/test_v0140_server_messages.py",
          "line": 7,
          "fragment": "from modules.knowledge import notifications"
        }
      },
      {
        "from": "learningBack/tests/test_v0140_server_messages.py",
        "to": "learningBack/modules/knowledge/notifications.py",
        "evidence": {
          "path": "learningBack/tests/test_v0140_server_messages.py",
          "line": 7,
          "fragment": "from modules.knowledge import notifications"
        }
      },
      {
        "from": "learningBack/tests/test_v0140_server_messages.py",
        "to": "learningBack/modules/knowledge/cow.py",
        "evidence": {
          "path": "learningBack/tests/test_v0140_server_messages.py",
          "line": 8,
          "fragment": "from modules.knowledge.cow import effective_graph"
        }
      },
      {
        "from": "learningBack/tests/test_v0140_server_messages.py",
        "to": "learningBack/modules/knowledge/mastery.py",
        "evidence": {
          "path": "learningBack/tests/test_v0140_server_messages.py",
          "line": 9,
          "fragment": "from modules.knowledge.mastery import MasteryState, save_state"
        }
      },
      {
        "from": "learningBack/tests/test_v0140_server_messages.py",
        "to": "learningBack/tests/conftest.py",
        "evidence": {
          "path": "learningBack/tests/test_v0140_server_messages.py",
          "line": 10,
          "fragment": "from tests.conftest import make_user"
        }
      },
      {
        "from": "learningBack/tests/test_v0140_server_messages.py",
        "to": "learningBack/tests/kg_helpers.py",
        "evidence": {
          "path": "learningBack/tests/test_v0140_server_messages.py",
          "line": 11,
          "fragment": "from tests.kg_helpers import concept"
        }
      },
      {
        "from": "learningBack/tests/test_v0140_server_messages.py",
        "to": "learningBack/modules/knowledge/models.py",
        "evidence": {
          "path": "learningBack/tests/test_v0140_server_messages.py",
          "line": 73,
          "fragment": "from modules.knowledge.models import ConceptArea"
        }
      },
      {
        "from": "learningFront/src/app/(tabs)/path.tsx",
        "to": "learningFront/src/features/graph-editor/index.ts",
        "evidence": {
          "path": "learningFront/src/app/(tabs)/path.tsx",
          "line": 6,
          "fragment": "import { CourseTree } from '@/features/graph-editor';"
        }
      },
      {
        "from": "learningFront/src/app/(tabs)/path.tsx",
        "to": "learningFront/src/entities/session/index.ts",
        "evidence": {
          "path": "learningFront/src/app/(tabs)/path.tsx",
          "line": 7,
          "fragment": "import { useSession } from '@/entities/session';"
        }
      },
      {
        "from": "learningFront/src/app/(tabs)/path.tsx",
        "to": "learningFront/src/pages/course/index.ts",
        "evidence": {
          "path": "learningFront/src/app/(tabs)/path.tsx",
          "line": 8,
          "fragment": "import { CourseScreen } from '@/pages/course';"
        }
      },
      {
        "from": "learningFront/src/app/(tabs)/path.tsx",
        "to": "learningFront/src/pages/graph/index.ts",
        "evidence": {
          "path": "learningFront/src/app/(tabs)/path.tsx",
          "line": 9,
          "fragment": "import { GraphScreen } from '@/pages/graph';"
        }
      },
      {
        "from": "learningFront/src/app/(tabs)/path.tsx",
        "to": "learningFront/src/shared/ui/index.ts",
        "evidence": {
          "path": "learningFront/src/app/(tabs)/path.tsx",
          "line": 10,
          "fragment": "import { Button, SegmentedControl, space, useTheme } from '@/shared/ui';"
        }
      },
      {
        "from": "learningFront/src/app/(tabs)/path.tsx",
        "to": "learningFront/src/widgets/subject-bar/index.tsx",
        "evidence": {
          "path": "learningFront/src/app/(tabs)/path.tsx",
          "line": 11,
          "fragment": "import { SubjectBar } from '@/widgets/subject-bar';"
        }
      },
      {
        "from": "learningFront/src/app/(tabs)/path.tsx",
        "to": "learningFront/src/shared/i18n/index.ts",
        "evidence": {
          "path": "learningFront/src/app/(tabs)/path.tsx",
          "line": 12,
          "fragment": "import { useI18n, translate } from '@/shared/i18n';"
        }
      },
      {
        "from": "learningFront/src/app/(tabs)/progress.tsx",
        "to": "learningFront/src/pages/progress/index.ts",
        "evidence": {
          "path": "learningFront/src/app/(tabs)/progress.tsx",
          "line": 4,
          "fragment": "import { ProgressScreen } from '@/pages/progress';"
        }
      },
      {
        "from": "learningFront/src/app/(tabs)/progress.tsx",
        "to": "learningFront/src/shared/ui/index.ts",
        "evidence": {
          "path": "learningFront/src/app/(tabs)/progress.tsx",
          "line": 5,
          "fragment": "import { useTheme } from '@/shared/ui';"
        }
      },
      {
        "from": "learningFront/src/app/(tabs)/progress.tsx",
        "to": "learningFront/src/widgets/subject-bar/index.tsx",
        "evidence": {
          "path": "learningFront/src/app/(tabs)/progress.tsx",
          "line": 6,
          "fragment": "import { SubjectBar } from '@/widgets/subject-bar';"
        }
      },
      {
        "from": "learningFront/src/app/curator.tsx",
        "to": "learningFront/src/entities/session/index.ts",
        "evidence": {
          "path": "learningFront/src/app/curator.tsx",
          "line": 3,
          "fragment": "import { useSession } from '@/entities/session';"
        }
      },
      {
        "from": "learningFront/src/app/curator.tsx",
        "to": "learningFront/src/shared/ui/index.ts",
        "evidence": {
          "path": "learningFront/src/app/curator.tsx",
          "line": 4,
          "fragment": "import { Card, Empty, Label, Muted, Screen, TopBar } from '@/shared/ui';"
        }
      },
      {
        "from": "learningFront/src/app/curator.tsx",
        "to": "learningFront/src/shared/i18n/index.ts",
        "evidence": {
          "path": "learningFront/src/app/curator.tsx",
          "line": 5,
          "fragment": "import { useI18n } from '@/shared/i18n';"
        }
      },
      {
        "from": "learningFront/src/app/library.tsx",
        "to": "learningFront/src/pages/library/index.ts",
        "evidence": {
          "path": "learningFront/src/app/library.tsx",
          "line": 2,
          "fragment": "import { LibraryScreen } from '@/pages/library';"
        }
      },
      {
        "from": "learningFront/src/app/problems.tsx",
        "to": "learningFront/src/entities/session/index.ts",
        "evidence": {
          "path": "learningFront/src/app/problems.tsx",
          "line": 2,
          "fragment": "import { useSession } from '@/entities/session';"
        }
      },
      {
        "from": "learningFront/src/app/problems.tsx",
        "to": "learningFront/src/pages/problems/index.ts",
        "evidence": {
          "path": "learningFront/src/app/problems.tsx",
          "line": 3,
          "fragment": "import { ProblemsScreen } from '@/pages/problems';"
        }
      },
      {
        "from": "learningFront/src/app/problems.tsx",
        "to": "learningFront/src/shared/ui/index.ts",
        "evidence": {
          "path": "learningFront/src/app/problems.tsx",
          "line": 4,
          "fragment": "import { Muted, Screen } from '@/shared/ui';"
        }
      },
      {
        "from": "learningFront/src/app/problems.tsx",
        "to": "learningFront/src/shared/i18n/index.ts",
        "evidence": {
          "path": "learningFront/src/app/problems.tsx",
          "line": 5,
          "fragment": "import { useI18n } from '@/shared/i18n';"
        }
      },
      {
        "from": "learningFront/src/app/skill-profile.tsx",
        "to": "learningFront/src/pages/skill-profile/index.ts",
        "evidence": {
          "path": "learningFront/src/app/skill-profile.tsx",
          "line": 2,
          "fragment": "import { SkillProfileScreen } from '@/pages/skill-profile';"
        }
      },
      {
        "from": "learningFront/src/app/sources.tsx",
        "to": "learningFront/src/entities/session/index.ts",
        "evidence": {
          "path": "learningFront/src/app/sources.tsx",
          "line": 2,
          "fragment": "import { useSession } from '@/entities/session';"
        }
      },
      {
        "from": "learningFront/src/app/sources.tsx",
        "to": "learningFront/src/pages/sources/index.ts",
        "evidence": {
          "path": "learningFront/src/app/sources.tsx",
          "line": 3,
          "fragment": "import { SourcesScreen } from '@/pages/sources';"
        }
      },
      {
        "from": "learningFront/src/app/sources.tsx",
        "to": "learningFront/src/shared/ui/index.ts",
        "evidence": {
          "path": "learningFront/src/app/sources.tsx",
          "line": 4,
          "fragment": "import { Muted, Screen } from '@/shared/ui';"
        }
      },
      {
        "from": "learningFront/src/app/sources.tsx",
        "to": "learningFront/src/shared/i18n/index.ts",
        "evidence": {
          "path": "learningFront/src/app/sources.tsx",
          "line": 5,
          "fragment": "import { useI18n } from '@/shared/i18n';"
        }
      },
      {
        "from": "learningFront/src/entities/concept/ui/claim-sources.tsx",
        "to": "learningFront/src/shared/api/index.ts",
        "evidence": {
          "path": "learningFront/src/entities/concept/ui/claim-sources.tsx",
          "line": 6,
          "fragment": "import { getNodeClaims, reportClaim, type NodeClaim } from '@/shared/api';"
        }
      },
      {
        "from": "learningFront/src/entities/concept/ui/claim-sources.tsx",
        "to": "learningFront/src/shared/ui/index.ts",
        "evidence": {
          "path": "learningFront/src/entities/concept/ui/claim-sources.tsx",
          "line": 7,
          "fragment": "import { Body, Button, Card, Field, Muted, Note, space } from '@/shared/ui';"
        }
      },
      {
        "from": "learningFront/src/entities/concept/ui/claim-sources.tsx",
        "to": "learningFront/src/shared/i18n/index.ts",
        "evidence": {
          "path": "learningFront/src/entities/concept/ui/claim-sources.tsx",
          "line": 8,
          "fragment": "import { useI18n } from '@/shared/i18n';"
        }
      },
      {
        "from": "learningFront/src/entities/session/subject.test.ts",
        "to": "learningFront/src/entities/session/subject.ts",
        "evidence": {
          "path": "learningFront/src/entities/session/subject.test.ts",
          "line": 2,
          "fragment": "import { nextTarget } from './subject';"
        }
      },
      {
        "from": "learningFront/src/features/claim-problems/index.ts",
        "to": "learningFront/src/features/claim-problems/ui/problem-pool.tsx",
        "evidence": {
          "path": "learningFront/src/features/claim-problems/index.ts",
          "line": 1,
          "fragment": "export { ProblemPool } from './ui/problem-pool';"
        }
      },
      {
        "from": "learningFront/src/features/claim-problems/ui/problem-pool.tsx",
        "to": "learningFront/src/shared/api/index.ts",
        "evidence": {
          "path": "learningFront/src/features/claim-problems/ui/problem-pool.tsx",
          "line": 15,
          "fragment": "} from '@/shared/api';"
        }
      },
      {
        "from": "learningFront/src/features/claim-problems/ui/problem-pool.tsx",
        "to": "learningFront/src/shared/ui/index.ts",
        "evidence": {
          "path": "learningFront/src/features/claim-problems/ui/problem-pool.tsx",
          "line": 16,
          "fragment": "import { Body, Button, Card, Chip, Label, Muted, Note, space } from '@/shared/ui';"
        }
      },
      {
        "from": "learningFront/src/features/claim-problems/ui/problem-pool.tsx",
        "to": "learningFront/src/shared/i18n/index.ts",
        "evidence": {
          "path": "learningFront/src/features/claim-problems/ui/problem-pool.tsx",
          "line": 17,
          "fragment": "import { useI18n, type Key } from '@/shared/i18n';"
        }
      },
      {
        "from": "learningFront/src/features/course/model/draft.test.ts",
        "to": "learningFront/src/features/course/model/draft.ts",
        "evidence": {
          "path": "learningFront/src/features/course/model/draft.test.ts",
          "line": 2,
          "fragment": "import { draftNotice, isDraft } from './draft';"
        }
      },
      {
        "from": "learningFront/src/features/course/model/draft.ts",
        "to": "learningFront/src/shared/api/index.ts",
        "evidence": {
          "path": "learningFront/src/features/course/model/draft.ts",
          "line": 2,
          "fragment": "import type { Course, CourseStep } from '@/shared/api';"
        }
      },
      {
        "from": "learningFront/src/features/course/model/draft.ts",
        "to": "learningFront/src/shared/i18n/translate.ts",
        "evidence": {
          "path": "learningFront/src/features/course/model/draft.ts",
          "line": 3,
          "fragment": "import { translate } from '../../../shared/i18n/translate';"
        }
      },
      {
        "from": "learningFront/src/features/course/model/group-steps.ts",
        "to": "learningFront/src/shared/api/index.ts",
        "evidence": {
          "path": "learningFront/src/features/course/model/group-steps.ts",
          "line": 2,
          "fragment": "import type { CourseStep } from '@/shared/api';"
        }
      },
      {
        "from": "learningFront/src/features/course/model/group-steps.ts",
        "to": "learningFront/src/shared/i18n/translate.ts",
        "evidence": {
          "path": "learningFront/src/features/course/model/group-steps.ts",
          "line": 3,
          "fragment": "import { translate } from '../../../shared/i18n/translate';"
        }
      },
      {
        "from": "learningFront/src/features/course/model/notices.test.ts",
        "to": "learningFront/src/shared/api/index.ts",
        "evidence": {
          "path": "learningFront/src/features/course/model/notices.test.ts",
          "line": 2,
          "fragment": "import type { CourseNotification } from '@/shared/api';"
        }
      },
      {
        "from": "learningFront/src/features/course/model/notices.test.ts",
        "to": "learningFront/src/features/course/model/notices.ts",
        "evidence": {
          "path": "learningFront/src/features/course/model/notices.test.ts",
          "line": 3,
          "fragment": "import { hasDraftNote, noticesFor, noticeTone } from './notices';"
        }
      },
      {
        "from": "learningFront/src/features/course/model/notices.ts",
        "to": "learningFront/src/shared/api/index.ts",
        "evidence": {
          "path": "learningFront/src/features/course/model/notices.ts",
          "line": 2,
          "fragment": "import type { CourseNotification } from '@/shared/api';"
        }
      },
      {
        "from": "learningFront/src/features/course/ui/path-accordion.tsx",
        "to": "learningFront/src/shared/api/index.ts",
        "evidence": {
          "path": "learningFront/src/features/course/ui/path-accordion.tsx",
          "line": 4,
          "fragment": "import type { CourseStep } from '@/shared/api';"
        }
      },
      {
        "from": "learningFront/src/features/course/ui/path-accordion.tsx",
        "to": "learningFront/src/shared/lib/index.ts",
        "evidence": {
          "path": "learningFront/src/features/course/ui/path-accordion.tsx",
          "line": 5,
          "fragment": "import { rememberFlag, remembered } from '@/shared/lib';"
        }
      },
      {
        "from": "learningFront/src/features/course/ui/path-accordion.tsx",
        "to": "learningFront/src/shared/ui/index.ts",
        "evidence": {
          "path": "learningFront/src/features/course/ui/path-accordion.tsx",
          "line": 6,
          "fragment": "import { Card, Label, Muted, space } from '@/shared/ui';"
        }
      },
      {
        "from": "learningFront/src/features/course/ui/path-accordion.tsx",
        "to": "learningFront/src/features/course/model/group-steps.ts",
        "evidence": {
          "path": "learningFront/src/features/course/ui/path-accordion.tsx",
          "line": 7,
          "fragment": "import { groupSteps } from '../model/group-steps';"
        }
      },
      {
        "from": "learningFront/src/features/course/ui/path-accordion.tsx",
        "to": "learningFront/src/shared/i18n/index.ts",
        "evidence": {
          "path": "learningFront/src/features/course/ui/path-accordion.tsx",
          "line": 8,
          "fragment": "import { useI18n } from '@/shared/i18n';"
        }
      },
      {
        "from": "learningFront/src/features/goal-intake/model/steps.test.ts",
        "to": "learningFront/src/features/goal-intake/model/steps.ts",
        "evidence": {
          "path": "learningFront/src/features/goal-intake/model/steps.test.ts",
          "line": 2,
          "fragment": "import { failureKind, stepLabel, stepOf, STEP_COUNT } from './steps';"
        }
      },
      {
        "from": "learningFront/src/features/goal-intake/model/steps.ts",
        "to": "learningFront/src/shared/i18n/translate.ts",
        "evidence": {
          "path": "learningFront/src/features/goal-intake/model/steps.ts",
          "line": 1,
          "fragment": "import { translate } from '../../../shared/i18n/translate';"
        }
      },
      {
        "from": "learningFront/src/features/goal-intake/ui/choice-chip.tsx",
        "to": "learningFront/src/shared/ui/index.ts",
        "evidence": {
          "path": "learningFront/src/features/goal-intake/ui/choice-chip.tsx",
          "line": 3,
          "fragment": "import { font, radius, space, useTheme } from '@/shared/ui';"
        }
      },
      {
        "from": "learningFront/src/features/goal-intake/ui/step-header.tsx",
        "to": "learningFront/src/shared/ui/index.ts",
        "evidence": {
          "path": "learningFront/src/features/goal-intake/ui/step-header.tsx",
          "line": 3,
          "fragment": "import { Label, radius, space, useTheme } from '@/shared/ui';"
        }
      },
      {
        "from": "learningFront/src/features/goal-intake/ui/step-header.tsx",
        "to": "learningFront/src/features/goal-intake/model/steps.ts",
        "evidence": {
          "path": "learningFront/src/features/goal-intake/ui/step-header.tsx",
          "line": 4,
          "fragment": "import { STEP_COUNT, stepLabel } from '../model/steps';"
        }
      },
      {
        "from": "learningFront/src/features/goal-reached/index.ts",
        "to": "learningFront/src/features/goal-reached/ui/goal-reached-card.tsx",
        "evidence": {
          "path": "learningFront/src/features/goal-reached/index.ts",
          "line": 1,
          "fragment": "export { GoalReachedCard } from './ui/goal-reached-card';"
        }
      },
      {
        "from": "learningFront/src/features/goal-reached/ui/goal-reached-card.tsx",
        "to": "learningFront/src/entities/session/index.ts",
        "evidence": {
          "path": "learningFront/src/features/goal-reached/ui/goal-reached-card.tsx",
          "line": 3,
          "fragment": "import { nextTarget, useSession } from '@/entities/session';"
        }
      },
      {
        "from": "learningFront/src/features/goal-reached/ui/goal-reached-card.tsx",
        "to": "learningFront/src/shared/api/index.ts",
        "evidence": {
          "path": "learningFront/src/features/goal-reached/ui/goal-reached-card.tsx",
          "line": 4,
          "fragment": "import { buildCourse, updateProfile } from '@/shared/api';"
        }
      },
      {
        "from": "learningFront/src/features/goal-reached/ui/goal-reached-card.tsx",
        "to": "learningFront/src/shared/ui/index.ts",
        "evidence": {
          "path": "learningFront/src/features/goal-reached/ui/goal-reached-card.tsx",
          "line": 5,
          "fragment": "import { Body, Button, Card, Label, Muted, Note } from '@/shared/ui';"
        }
      },
      {
        "from": "learningFront/src/features/goal-reached/ui/goal-reached-card.tsx",
        "to": "learningFront/src/shared/i18n/index.ts",
        "evidence": {
          "path": "learningFront/src/features/goal-reached/ui/goal-reached-card.tsx",
          "line": 6,
          "fragment": "import { useI18n } from '@/shared/i18n';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/model/build-progress.test.ts",
        "to": "learningFront/src/shared/api/index.ts",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/model/build-progress.test.ts",
          "line": 2,
          "fragment": "import type { ProfileState } from '@/shared/api';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/model/build-progress.test.ts",
        "to": "learningFront/src/features/graph-editor/model/build-progress.ts",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/model/build-progress.test.ts",
          "line": 3,
          "fragment": "import { buildView, canResume, elapsedLabel, isPending } from './build-progress';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/model/build-progress.ts",
        "to": "learningFront/src/shared/api/index.ts",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/model/build-progress.ts",
          "line": 3,
          "fragment": "import type { ProfileState } from '@/shared/api';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/model/build-progress.ts",
        "to": "learningFront/src/shared/i18n/translate.ts",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/model/build-progress.ts",
          "line": 4,
          "fragment": "import { translate } from '../../../shared/i18n/translate';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/model/keys.ts",
        "to": "learningFront/src/shared/api/index.ts",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/model/keys.ts",
          "line": 3,
          "fragment": "import type { GraphEdge } from '@/shared/api';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/model/keys.ts",
        "to": "learningFront/src/features/graph-editor/model/scheme.ts",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/model/keys.ts",
          "line": 4,
          "fragment": "import type { SchemeLayout } from './scheme';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/model/legend.ts",
        "to": "learningFront/src/shared/api/index.ts",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/model/legend.ts",
          "line": 3,
          "fragment": "import type { GraphEdge, GraphNode } from '@/shared/api';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/model/legend.ts",
        "to": "learningFront/src/features/graph-editor/model/scheme.ts",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/model/legend.ts",
          "line": 4,
          "fragment": "import { scaleOf, type MasteryState } from './scheme';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/model/legend.ts",
        "to": "learningFront/src/shared/i18n/translate.ts",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/model/legend.ts",
          "line": 5,
          "fragment": "import { translate } from '../../../shared/i18n/translate';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/model/overview.ts",
        "to": "learningFront/src/shared/api/index.ts",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/model/overview.ts",
          "line": 4,
          "fragment": "import type { GraphEdge, GraphNode } from '@/shared/api';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/model/overview.ts",
        "to": "learningFront/src/features/graph-editor/model/scheme.ts",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/model/overview.ts",
          "line": 20,
          "fragment": "} from './scheme';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/model/overview.ts",
        "to": "learningFront/src/shared/i18n/translate.ts",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/model/overview.ts",
          "line": 21,
          "fragment": "import { translate } from '../../../shared/i18n/translate';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/model/remember.ts",
        "to": "learningFront/src/shared/lib/index.ts",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/model/remember.ts",
          "line": 1,
          "fragment": "export { remembered, rememberFlag } from '@/shared/lib';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/model/scheme.test.ts",
        "to": "learningFront/src/shared/api/index.ts",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/model/scheme.test.ts",
          "line": 2,
          "fragment": "import type { GraphEdge, GraphNode, MasteryMap } from '@/shared/api';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/model/scheme.test.ts",
        "to": "learningFront/src/features/graph-editor/model/scheme.ts",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/model/scheme.test.ts",
          "line": 20,
          "fragment": "} from './scheme';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/model/scheme.ts",
        "to": "learningFront/src/shared/api/index.ts",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/model/scheme.ts",
          "line": 3,
          "fragment": "import type { Course, GraphEdge, GraphNode, MasteryMap } from '@/shared/api';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/model/scheme.ts",
        "to": "learningFront/src/shared/i18n/translate.ts",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/model/scheme.ts",
          "line": 4,
          "fragment": "import { translate } from '../../../shared/i18n/translate';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/model/stage-groups.test.ts",
        "to": "learningFront/src/shared/api/index.ts",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/model/stage-groups.test.ts",
          "line": 2,
          "fragment": "import type { GraphNode } from '@/shared/api';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/model/stage-groups.test.ts",
        "to": "learningFront/src/features/graph-editor/model/stage-groups.ts",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/model/stage-groups.test.ts",
          "line": 3,
          "fragment": "import { groupByStage, hasStages } from './stage-groups';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/model/stage-groups.ts",
        "to": "learningFront/src/shared/api/index.ts",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/model/stage-groups.ts",
          "line": 2,
          "fragment": "import type { GraphNode } from '@/shared/api';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/model/stage-groups.ts",
        "to": "learningFront/src/shared/i18n/translate.ts",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/model/stage-groups.ts",
          "line": 3,
          "fragment": "import { translate } from '../../../shared/i18n/translate';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/ui/course-tree.tsx",
        "to": "learningFront/src/shared/api/index.ts",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/ui/course-tree.tsx",
          "line": 4,
          "fragment": "import { getCourse, type Course } from '@/shared/api';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/ui/course-tree.tsx",
        "to": "learningFront/src/shared/ui/index.ts",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/ui/course-tree.tsx",
          "line": 5,
          "fragment": "import { Empty, Screen, space } from '@/shared/ui';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/ui/course-tree.tsx",
        "to": "learningFront/src/features/graph-editor/model/scheme.ts",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/ui/course-tree.tsx",
          "line": 6,
          "fragment": "import { courseAsGraph } from '../model/scheme';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/ui/course-tree.tsx",
        "to": "learningFront/src/features/graph-editor/ui/scheme-view.tsx",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/ui/course-tree.tsx",
          "line": 7,
          "fragment": "import { SchemeView } from './scheme-view';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/ui/course-tree.tsx",
        "to": "learningFront/src/shared/i18n/index.ts",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/ui/course-tree.tsx",
          "line": 8,
          "fragment": "import { useI18n } from '@/shared/i18n';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/ui/graph-build-panel.tsx",
        "to": "learningFront/src/shared/api/index.ts",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/ui/graph-build-panel.tsx",
          "line": 14,
          "fragment": "} from '@/shared/api';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/ui/graph-build-panel.tsx",
        "to": "learningFront/src/shared/ui/index.ts",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/ui/graph-build-panel.tsx",
          "line": 15,
          "fragment": "import { AreaProgress, Button, Card, Label, Muted, Note, space } from '@/shared/ui';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/ui/graph-build-panel.tsx",
        "to": "learningFront/src/features/graph-editor/model/build-progress.ts",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/ui/graph-build-panel.tsx",
          "line": 16,
          "fragment": "import { buildView, canResume, elapsedLabel, isPending, POLL_MS } from '../model/build-progress';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/ui/graph-build-panel.tsx",
        "to": "learningFront/src/shared/i18n/index.ts",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/ui/graph-build-panel.tsx",
          "line": 17,
          "fragment": "import { useI18n } from '@/shared/i18n';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/ui/mini-map.tsx",
        "to": "learningFront/src/shared/ui/index.ts",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/ui/mini-map.tsx",
          "line": 3,
          "fragment": "import { radius, useTheme } from '@/shared/ui';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/ui/mini-map.tsx",
        "to": "learningFront/src/features/graph-editor/model/scheme.ts",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/ui/mini-map.tsx",
          "line": 4,
          "fragment": "import { NODE_H, NODE_W, type SchemeLayout } from '../model/scheme';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/ui/mini-map.tsx",
        "to": "learningFront/src/features/graph-editor/model/overview.ts",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/ui/mini-map.tsx",
          "line": 5,
          "fragment": "import type { StageBox } from '../model/overview';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/ui/mini-map.tsx",
        "to": "learningFront/src/shared/i18n/index.ts",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/ui/mini-map.tsx",
          "line": 6,
          "fragment": "import { useI18n } from '@/shared/i18n';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/ui/node-plate.tsx",
        "to": "learningFront/src/shared/api/index.ts",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/ui/node-plate.tsx",
          "line": 6,
          "fragment": "import type { Graph, GraphNode } from '@/shared/api';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/ui/node-plate.tsx",
        "to": "learningFront/src/shared/ui/index.ts",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/ui/node-plate.tsx",
          "line": 7,
          "fragment": "import { Body, Button, Card, Field, font, Muted, Pill, space, useTheme } from '@/shared/ui';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/ui/node-plate.tsx",
        "to": "learningFront/src/features/graph-editor/model/scheme.ts",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/ui/node-plate.tsx",
          "line": 8,
          "fragment": "import { tagsOf, type MasteryState } from '../model/scheme';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/ui/node-plate.tsx",
        "to": "learningFront/src/features/graph-editor/ui/scheme-canvas.tsx",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/ui/node-plate.tsx",
          "line": 9,
          "fragment": "import { STATE_SHORT } from './scheme-canvas';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/ui/node-plate.tsx",
        "to": "learningFront/src/shared/i18n/index.ts",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/ui/node-plate.tsx",
          "line": 10,
          "fragment": "import { useI18n } from '@/shared/i18n';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/ui/scheme-canvas.tsx",
        "to": "learningFront/src/shared/api/index.ts",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/ui/scheme-canvas.tsx",
          "line": 13,
          "fragment": "import type { Graph, GraphEdge, GraphNode } from '@/shared/api';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/ui/scheme-canvas.tsx",
        "to": "learningFront/src/shared/ui/index.ts",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/ui/scheme-canvas.tsx",
          "line": 14,
          "fragment": "import { radius, space, useTheme } from '@/shared/ui';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/ui/scheme-canvas.tsx",
        "to": "learningFront/src/features/graph-editor/model/scheme.ts",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/ui/scheme-canvas.tsx",
          "line": 30,
          "fragment": "} from '../model/scheme';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/ui/scheme-canvas.tsx",
        "to": "learningFront/src/features/graph-editor/model/overview.ts",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/ui/scheme-canvas.tsx",
          "line": 31,
          "fragment": "import { isGhost } from '../model/overview';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/ui/scheme-canvas.tsx",
        "to": "learningFront/src/shared/i18n/index.ts",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/ui/scheme-canvas.tsx",
          "line": 32,
          "fragment": "import { useI18n, translate } from '@/shared/i18n';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/ui/scheme-fullscreen.tsx",
        "to": "learningFront/src/shared/api/index.ts",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/ui/scheme-fullscreen.tsx",
          "line": 16,
          "fragment": "import type { Graph, GraphNode } from '@/shared/api';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/ui/scheme-fullscreen.tsx",
        "to": "learningFront/src/shared/ui/index.ts",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/ui/scheme-fullscreen.tsx",
          "line": 27,
          "fragment": "} from '@/shared/ui';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/ui/scheme-fullscreen.tsx",
        "to": "learningFront/src/features/graph-editor/model/keys.ts",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/ui/scheme-fullscreen.tsx",
          "line": 28,
          "fragment": "import { neighborByKey, type KeyDirection } from '../model/keys';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/ui/scheme-fullscreen.tsx",
        "to": "learningFront/src/features/graph-editor/model/scheme.ts",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/ui/scheme-fullscreen.tsx",
          "line": 40,
          "fragment": "} from '../model/scheme';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/ui/scheme-fullscreen.tsx",
        "to": "learningFront/src/features/graph-editor/model/overview.ts",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/ui/scheme-fullscreen.tsx",
          "line": 41,
          "fragment": "import { stageTitleOf } from '../model/overview';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/ui/scheme-fullscreen.tsx",
        "to": "learningFront/src/features/graph-editor/ui/mini-map.tsx",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/ui/scheme-fullscreen.tsx",
          "line": 42,
          "fragment": "import { MiniMap } from './mini-map';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/ui/scheme-fullscreen.tsx",
        "to": "learningFront/src/features/graph-editor/ui/node-plate.tsx",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/ui/scheme-fullscreen.tsx",
          "line": 43,
          "fragment": "import { NodePlate } from './node-plate';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/ui/scheme-fullscreen.tsx",
        "to": "learningFront/src/features/graph-editor/ui/scheme-legend.tsx",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/ui/scheme-fullscreen.tsx",
          "line": 44,
          "fragment": "import { LegendList } from './scheme-legend';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/ui/scheme-fullscreen.tsx",
        "to": "learningFront/src/features/graph-editor/ui/scheme-canvas.tsx",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/ui/scheme-fullscreen.tsx",
          "line": 45,
          "fragment": "import { SchemeCanvas, type CanvasMode } from './scheme-canvas';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/ui/scheme-fullscreen.tsx",
        "to": "learningFront/src/features/graph-editor/ui/stage-controls.tsx",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/ui/scheme-fullscreen.tsx",
          "line": 46,
          "fragment": "import { StageControls, StageLinksCard } from './stage-controls';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/ui/scheme-fullscreen.tsx",
        "to": "learningFront/src/features/graph-editor/ui/use-scheme-scene.tsx",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/ui/scheme-fullscreen.tsx",
          "line": 47,
          "fragment": "import type { SchemeScene } from './use-scheme-scene';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/ui/scheme-fullscreen.tsx",
        "to": "learningFront/src/shared/i18n/index.ts",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/ui/scheme-fullscreen.tsx",
          "line": 48,
          "fragment": "import { useI18n, translate } from '@/shared/i18n';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/ui/scheme-legend.tsx",
        "to": "learningFront/src/shared/ui/index.ts",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/ui/scheme-legend.tsx",
          "line": 4,
          "fragment": "import { Card, font, Label, Muted, radius, space, useTheme } from '@/shared/ui';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/ui/scheme-legend.tsx",
        "to": "learningFront/src/features/graph-editor/model/scheme.ts",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/ui/scheme-legend.tsx",
          "line": 5,
          "fragment": "import { dashBars, type Bar } from '../model/scheme';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/ui/scheme-legend.tsx",
        "to": "learningFront/src/features/graph-editor/model/legend.ts",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/ui/scheme-legend.tsx",
          "line": 6,
          "fragment": "import type { LegendItem, LegendSample } from '../model/legend';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/ui/scheme-legend.tsx",
        "to": "learningFront/src/shared/i18n/index.ts",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/ui/scheme-legend.tsx",
          "line": 7,
          "fragment": "import { translate, useI18n } from '@/shared/i18n';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/ui/scheme-view.tsx",
        "to": "learningFront/src/shared/api/index.ts",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/ui/scheme-view.tsx",
          "line": 15,
          "fragment": "} from '@/shared/api';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/ui/scheme-view.tsx",
        "to": "learningFront/src/features/graph-editor/ui/scheme-canvas.tsx",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/ui/scheme-view.tsx",
          "line": 16,
          "fragment": "import { SchemeCanvas, STATE_TEXT } from './scheme-canvas';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/ui/scheme-view.tsx",
        "to": "learningFront/src/features/graph-editor/ui/scheme-fullscreen.tsx",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/ui/scheme-view.tsx",
          "line": 17,
          "fragment": "import { SchemeFullscreen } from './scheme-fullscreen';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/ui/scheme-view.tsx",
        "to": "learningFront/src/features/graph-editor/ui/stage-controls.tsx",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/ui/scheme-view.tsx",
          "line": 18,
          "fragment": "import { StageControls, StageLinksCard } from './stage-controls';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/ui/scheme-view.tsx",
        "to": "learningFront/src/features/graph-editor/ui/use-scheme-scene.tsx",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/ui/scheme-view.tsx",
          "line": 19,
          "fragment": "import { useSchemeScene } from './use-scheme-scene';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/ui/scheme-view.tsx",
        "to": "learningFront/src/features/graph-editor/model/overview.ts",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/ui/scheme-view.tsx",
          "line": 20,
          "fragment": "import { stageTitleOf } from '../model/overview';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/ui/scheme-view.tsx",
        "to": "learningFront/src/features/graph-editor/model/legend.ts",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/ui/scheme-view.tsx",
          "line": 21,
          "fragment": "import type { LegendMode } from '../model/legend';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/ui/scheme-view.tsx",
        "to": "learningFront/src/features/graph-editor/model/offline.ts",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/ui/scheme-view.tsx",
          "line": 22,
          "fragment": "import { queueEdit } from '../model/offline';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/ui/scheme-view.tsx",
        "to": "learningFront/src/shared/ui/index.ts",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/ui/scheme-view.tsx",
          "line": 35,
          "fragment": "} from '@/shared/ui';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/ui/scheme-view.tsx",
        "to": "learningFront/src/features/graph-editor/model/scheme.ts",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/ui/scheme-view.tsx",
          "line": 46,
          "fragment": "} from '../model/scheme';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/ui/scheme-view.tsx",
        "to": "learningFront/src/features/graph-editor/model/remember.ts",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/ui/scheme-view.tsx",
          "line": 47,
          "fragment": "import { rememberFlag, remembered } from '../model/remember';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/ui/scheme-view.tsx",
        "to": "learningFront/src/features/graph-editor/ui/scheme-legend.tsx",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/ui/scheme-view.tsx",
          "line": 48,
          "fragment": "import { SchemeLegend } from './scheme-legend';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/ui/scheme-view.tsx",
        "to": "learningFront/src/shared/i18n/index.ts",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/ui/scheme-view.tsx",
          "line": 49,
          "fragment": "import { translate, useI18n } from '@/shared/i18n';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/ui/stage-controls.tsx",
        "to": "learningFront/src/shared/api/index.ts",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/ui/stage-controls.tsx",
          "line": 4,
          "fragment": "import type { GraphNode } from '@/shared/api';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/ui/stage-controls.tsx",
        "to": "learningFront/src/shared/ui/index.ts",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/ui/stage-controls.tsx",
          "line": 5,
          "fragment": "import { Button, Card, Chip, font, Label, Muted, space, useTheme } from '@/shared/ui';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/ui/stage-controls.tsx",
        "to": "learningFront/src/features/graph-editor/model/overview.ts",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/ui/stage-controls.tsx",
          "line": 6,
          "fragment": "import { stageSummary, type StageLink } from '../model/overview';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/ui/stage-controls.tsx",
        "to": "learningFront/src/features/graph-editor/ui/use-scheme-scene.tsx",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/ui/stage-controls.tsx",
          "line": 7,
          "fragment": "import type { SchemeScene, SchemeViewMode } from './use-scheme-scene';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/ui/stage-controls.tsx",
        "to": "learningFront/src/shared/i18n/index.ts",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/ui/stage-controls.tsx",
          "line": 8,
          "fragment": "import { useI18n, translate } from '@/shared/i18n';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/ui/stage-layer.tsx",
        "to": "learningFront/src/shared/ui/index.ts",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/ui/stage-layer.tsx",
          "line": 4,
          "fragment": "import { radius, useTheme } from '@/shared/ui';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/ui/stage-layer.tsx",
        "to": "learningFront/src/features/graph-editor/model/overview.ts",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/ui/stage-layer.tsx",
          "line": 5,
          "fragment": "import type { Overview, StageArrow, StageBox, StageLink } from '../model/overview';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/ui/stage-layer.tsx",
        "to": "learningFront/src/features/graph-editor/model/scheme.ts",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/ui/stage-layer.tsx",
          "line": 6,
          "fragment": "import { NODE_W } from '../model/scheme';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/ui/stage-layer.tsx",
        "to": "learningFront/src/shared/i18n/index.ts",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/ui/stage-layer.tsx",
          "line": 7,
          "fragment": "import { useI18n } from '@/shared/i18n';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/ui/use-scheme-scene.tsx",
        "to": "learningFront/src/shared/api/index.ts",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/ui/use-scheme-scene.tsx",
          "line": 5,
          "fragment": "import type { Graph, GraphNode } from '@/shared/api';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/ui/use-scheme-scene.tsx",
        "to": "learningFront/src/features/graph-editor/model/overview.ts",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/ui/use-scheme-scene.tsx",
          "line": 13,
          "fragment": "} from '../model/overview';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/ui/use-scheme-scene.tsx",
        "to": "learningFront/src/features/graph-editor/model/legend.ts",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/ui/use-scheme-scene.tsx",
          "line": 14,
          "fragment": "import { legendFor, type LegendItem, type LegendMode } from '../model/legend';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/ui/use-scheme-scene.tsx",
        "to": "learningFront/src/features/graph-editor/model/remember.ts",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/ui/use-scheme-scene.tsx",
          "line": 15,
          "fragment": "import { rememberFlag, remembered } from '../model/remember';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/ui/use-scheme-scene.tsx",
        "to": "learningFront/src/features/graph-editor/model/scheme.ts",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/ui/use-scheme-scene.tsx",
          "line": 16,
          "fragment": "import { stageKeyOf, type Highlight, type MasteryState, type SchemeLayout } from '../model/scheme';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/ui/use-scheme-scene.tsx",
        "to": "learningFront/src/features/graph-editor/ui/stage-layer.tsx",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/ui/use-scheme-scene.tsx",
          "line": 17,
          "fragment": "import { StageLayer } from './stage-layer';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/ui/use-scheme-scene.tsx",
        "to": "learningFront/src/shared/i18n/index.ts",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/ui/use-scheme-scene.tsx",
          "line": 18,
          "fragment": "import { useI18n } from '@/shared/i18n';"
        }
      },
      {
        "from": "learningFront/src/features/prior-test/index.ts",
        "to": "learningFront/src/features/prior-test/ui/prior-test-session.tsx",
        "evidence": {
          "path": "learningFront/src/features/prior-test/index.ts",
          "line": 1,
          "fragment": "export { PriorTestSession } from './ui/prior-test-session';"
        }
      },
      {
        "from": "learningFront/src/features/prior-test/model/report.test.ts",
        "to": "learningFront/src/shared/api/index.ts",
        "evidence": {
          "path": "learningFront/src/features/prior-test/model/report.test.ts",
          "line": 2,
          "fragment": "import type { PriorReport } from '@/shared/api';"
        }
      },
      {
        "from": "learningFront/src/features/prior-test/model/report.test.ts",
        "to": "learningFront/src/features/prior-test/model/report.ts",
        "evidence": {
          "path": "learningFront/src/features/prior-test/model/report.test.ts",
          "line": 3,
          "fragment": "import { areaLine, hasAreas, summaryLine, verdictTone, VERDICT_LABEL } from './report';"
        }
      },
      {
        "from": "learningFront/src/features/prior-test/model/report.ts",
        "to": "learningFront/src/shared/api/index.ts",
        "evidence": {
          "path": "learningFront/src/features/prior-test/model/report.ts",
          "line": 2,
          "fragment": "import type { AreaReport, PriorReport, Verdict } from '@/shared/api';"
        }
      },
      {
        "from": "learningFront/src/features/prior-test/model/report.ts",
        "to": "learningFront/src/shared/i18n/translate.ts",
        "evidence": {
          "path": "learningFront/src/features/prior-test/model/report.ts",
          "line": 3,
          "fragment": "import { translate } from '../../../shared/i18n/translate';"
        }
      },
      {
        "from": "learningFront/src/features/prior-test/ui/prior-test-session.tsx",
        "to": "learningFront/src/entities/session/index.ts",
        "evidence": {
          "path": "learningFront/src/features/prior-test/ui/prior-test-session.tsx",
          "line": 5,
          "fragment": "import { MASTERY_TARGETS } from '@/entities/session';"
        }
      },
      {
        "from": "learningFront/src/features/prior-test/ui/prior-test-session.tsx",
        "to": "learningFront/src/shared/ui/index.ts",
        "evidence": {
          "path": "learningFront/src/features/prior-test/ui/prior-test-session.tsx",
          "line": 15,
          "fragment": "import { Pill, useTheme, type Palette } from '@/shared/ui';"
        }
      },
      {
        "from": "learningFront/src/features/prior-test/ui/prior-test-session.tsx",
        "to": "learningFront/src/shared/api/index.ts",
        "evidence": {
          "path": "learningFront/src/features/prior-test/ui/prior-test-session.tsx",
          "line": 22,
          "fragment": "} from '@/shared/api';"
        }
      },
      {
        "from": "learningFront/src/features/prior-test/ui/prior-test-session.tsx",
        "to": "learningFront/src/features/prior-test/model/report.ts",
        "evidence": {
          "path": "learningFront/src/features/prior-test/ui/prior-test-session.tsx",
          "line": 30,
          "fragment": "} from '../model/report';"
        }
      },
      {
        "from": "learningFront/src/features/prior-test/ui/prior-test-session.tsx",
        "to": "learningFront/src/shared/i18n/index.ts",
        "evidence": {
          "path": "learningFront/src/features/prior-test/ui/prior-test-session.tsx",
          "line": 31,
          "fragment": "import { useI18n } from '@/shared/i18n';"
        }
      },
      {
        "from": "learningFront/src/features/push-settings/index.ts",
        "to": "learningFront/src/features/push-settings/ui/push-settings.tsx",
        "evidence": {
          "path": "learningFront/src/features/push-settings/index.ts",
          "line": 1,
          "fragment": "export { PushSettings } from './ui/push-settings';"
        }
      },
      {
        "from": "learningFront/src/features/push-settings/model/push-model.test.ts",
        "to": "learningFront/src/shared/api/index.ts",
        "evidence": {
          "path": "learningFront/src/features/push-settings/model/push-model.test.ts",
          "line": 2,
          "fragment": "import type { PushState } from '@/shared/api';"
        }
      },
      {
        "from": "learningFront/src/features/push-settings/model/push-model.test.ts",
        "to": "learningFront/src/features/push-settings/model/push-model.ts",
        "evidence": {
          "path": "learningFront/src/features/push-settings/model/push-model.test.ts",
          "line": 3,
          "fragment": "import { describePush } from './push-model';"
        }
      },
      {
        "from": "learningFront/src/features/push-settings/model/push-model.ts",
        "to": "learningFront/src/shared/api/index.ts",
        "evidence": {
          "path": "learningFront/src/features/push-settings/model/push-model.ts",
          "line": 2,
          "fragment": "import type { PushState } from '@/shared/api';"
        }
      },
      {
        "from": "learningFront/src/features/push-settings/model/push-model.ts",
        "to": "learningFront/src/shared/i18n/translate.ts",
        "evidence": {
          "path": "learningFront/src/features/push-settings/model/push-model.ts",
          "line": 3,
          "fragment": "import { translate } from '../../../shared/i18n/translate';"
        }
      },
      {
        "from": "learningFront/src/features/push-settings/ui/push-settings.tsx",
        "to": "learningFront/src/shared/api/index.ts",
        "evidence": {
          "path": "learningFront/src/features/push-settings/ui/push-settings.tsx",
          "line": 10,
          "fragment": "} from '@/shared/api';"
        }
      },
      {
        "from": "learningFront/src/features/push-settings/ui/push-settings.tsx",
        "to": "learningFront/src/shared/ui/index.ts",
        "evidence": {
          "path": "learningFront/src/features/push-settings/ui/push-settings.tsx",
          "line": 11,
          "fragment": "import { Button, Card, Label, Muted, Note } from '@/shared/ui';"
        }
      },
      {
        "from": "learningFront/src/features/push-settings/ui/push-settings.tsx",
        "to": "learningFront/src/features/push-settings/model/push-model.ts",
        "evidence": {
          "path": "learningFront/src/features/push-settings/ui/push-settings.tsx",
          "line": 12,
          "fragment": "import { describePush, type FailureReason } from '../model/push-model';"
        }
      },
      {
        "from": "learningFront/src/features/push-settings/ui/push-settings.tsx",
        "to": "learningFront/src/shared/i18n/index.ts",
        "evidence": {
          "path": "learningFront/src/features/push-settings/ui/push-settings.tsx",
          "line": 13,
          "fragment": "import { useI18n } from '@/shared/i18n';"
        }
      },
      {
        "from": "learningFront/src/features/skill-profile/index.ts",
        "to": "learningFront/src/features/skill-profile/ui/skill-profile-editor.tsx",
        "evidence": {
          "path": "learningFront/src/features/skill-profile/index.ts",
          "line": 1,
          "fragment": "export { SkillProfileEditor } from './ui/skill-profile-editor';"
        }
      },
      {
        "from": "learningFront/src/features/skill-profile/model/profile-model.test.ts",
        "to": "learningFront/src/shared/api/index.ts",
        "evidence": {
          "path": "learningFront/src/features/skill-profile/model/profile-model.test.ts",
          "line": 2,
          "fragment": "import type { CoverageReport, ProfileArea, ProfileConcept, SkillProfile } from '@/shared/api';"
        }
      },
      {
        "from": "learningFront/src/features/skill-profile/model/profile-model.test.ts",
        "to": "learningFront/src/features/skill-profile/model/profile-model.ts",
        "evidence": {
          "path": "learningFront/src/features/skill-profile/model/profile-model.test.ts",
          "line": 13,
          "fragment": "} from './profile-model';"
        }
      },
      {
        "from": "learningFront/src/features/skill-profile/model/profile-model.ts",
        "to": "learningFront/src/shared/api/index.ts",
        "evidence": {
          "path": "learningFront/src/features/skill-profile/model/profile-model.ts",
          "line": 8,
          "fragment": "} from '@/shared/api';"
        }
      },
      {
        "from": "learningFront/src/features/skill-profile/model/profile-model.ts",
        "to": "learningFront/src/shared/i18n/translate.ts",
        "evidence": {
          "path": "learningFront/src/features/skill-profile/model/profile-model.ts",
          "line": 9,
          "fragment": "import { translate } from '../../../shared/i18n/translate';"
        }
      },
      {
        "from": "learningFront/src/features/skill-profile/ui/skill-profile-editor.tsx",
        "to": "learningFront/src/shared/api/index.ts",
        "evidence": {
          "path": "learningFront/src/features/skill-profile/ui/skill-profile-editor.tsx",
          "line": 15,
          "fragment": "} from '@/shared/api';"
        }
      },
      {
        "from": "learningFront/src/features/skill-profile/ui/skill-profile-editor.tsx",
        "to": "learningFront/src/shared/ui/index.ts",
        "evidence": {
          "path": "learningFront/src/features/skill-profile/ui/skill-profile-editor.tsx",
          "line": 27,
          "fragment": "} from '@/shared/ui';"
        }
      },
      {
        "from": "learningFront/src/features/skill-profile/ui/skill-profile-editor.tsx",
        "to": "learningFront/src/features/skill-profile/model/profile-model.ts",
        "evidence": {
          "path": "learningFront/src/features/skill-profile/ui/skill-profile-editor.tsx",
          "line": 39,
          "fragment": "} from '../model/profile-model';"
        }
      },
      {
        "from": "learningFront/src/features/skill-profile/ui/skill-profile-editor.tsx",
        "to": "learningFront/src/shared/i18n/index.ts",
        "evidence": {
          "path": "learningFront/src/features/skill-profile/ui/skill-profile-editor.tsx",
          "line": 40,
          "fragment": "import { useI18n } from '@/shared/i18n';"
        }
      },
      {
        "from": "learningFront/src/features/sources/index.ts",
        "to": "learningFront/src/features/sources/ui/gaps-card.tsx",
        "evidence": {
          "path": "learningFront/src/features/sources/index.ts",
          "line": 1,
          "fragment": "export { GapsCard } from './ui/gaps-card';"
        }
      },
      {
        "from": "learningFront/src/features/sources/index.ts",
        "to": "learningFront/src/features/sources/ui/sources-panel.tsx",
        "evidence": {
          "path": "learningFront/src/features/sources/index.ts",
          "line": 2,
          "fragment": "export { SourcesPanel } from './ui/sources-panel';"
        }
      },
      {
        "from": "learningFront/src/features/sources/model/gaps-model.test.ts",
        "to": "learningFront/src/shared/api/index.ts",
        "evidence": {
          "path": "learningFront/src/features/sources/model/gaps-model.test.ts",
          "line": 2,
          "fragment": "import type { SourceGap } from '@/shared/api';"
        }
      },
      {
        "from": "learningFront/src/features/sources/model/gaps-model.test.ts",
        "to": "learningFront/src/features/sources/model/gaps-model.ts",
        "evidence": {
          "path": "learningFront/src/features/sources/model/gaps-model.test.ts",
          "line": 3,
          "fragment": "import { canSearch, effectiveQuery, gapsNeedPolling, resultLine } from './gaps-model';"
        }
      },
      {
        "from": "learningFront/src/features/sources/model/gaps-model.ts",
        "to": "learningFront/src/shared/api/index.ts",
        "evidence": {
          "path": "learningFront/src/features/sources/model/gaps-model.ts",
          "line": 2,
          "fragment": "import type { GapFillResult, GapFillStatus, SourceGap } from '@/shared/api';"
        }
      },
      {
        "from": "learningFront/src/features/sources/model/gaps-model.ts",
        "to": "learningFront/src/shared/i18n/translate.ts",
        "evidence": {
          "path": "learningFront/src/features/sources/model/gaps-model.ts",
          "line": 3,
          "fragment": "import { translate } from '../../../shared/i18n/translate';"
        }
      },
      {
        "from": "learningFront/src/features/sources/model/sources-model.test.ts",
        "to": "learningFront/src/shared/api/index.ts",
        "evidence": {
          "path": "learningFront/src/features/sources/model/sources-model.test.ts",
          "line": 2,
          "fragment": "import type { SourceItem, SourceProgress } from '@/shared/api';"
        }
      },
      {
        "from": "learningFront/src/features/sources/model/sources-model.test.ts",
        "to": "learningFront/src/features/sources/model/sources-model.ts",
        "evidence": {
          "path": "learningFront/src/features/sources/model/sources-model.test.ts",
          "line": 10,
          "fragment": "} from './sources-model';"
        }
      },
      {
        "from": "learningFront/src/features/sources/model/sources-model.ts",
        "to": "learningFront/src/shared/api/index.ts",
        "evidence": {
          "path": "learningFront/src/features/sources/model/sources-model.ts",
          "line": 2,
          "fragment": "import type { IngestStatus, SourceFields, SourceItem, SourceProgress } from '@/shared/api';"
        }
      },
      {
        "from": "learningFront/src/features/sources/model/sources-model.ts",
        "to": "learningFront/src/shared/i18n/translate.ts",
        "evidence": {
          "path": "learningFront/src/features/sources/model/sources-model.ts",
          "line": 3,
          "fragment": "import { translate } from '../../../shared/i18n/translate';"
        }
      },
      {
        "from": "learningFront/src/features/sources/ui/gaps-card.tsx",
        "to": "learningFront/src/shared/api/index.ts",
        "evidence": {
          "path": "learningFront/src/features/sources/ui/gaps-card.tsx",
          "line": 11,
          "fragment": "} from '@/shared/api';"
        }
      },
      {
        "from": "learningFront/src/features/sources/ui/gaps-card.tsx",
        "to": "learningFront/src/shared/ui/index.ts",
        "evidence": {
          "path": "learningFront/src/features/sources/ui/gaps-card.tsx",
          "line": 12,
          "fragment": "import { Body, Button, Card, Field, Label, Muted, Note, space } from '@/shared/ui';"
        }
      },
      {
        "from": "learningFront/src/features/sources/ui/gaps-card.tsx",
        "to": "learningFront/src/features/sources/model/gaps-model.ts",
        "evidence": {
          "path": "learningFront/src/features/sources/ui/gaps-card.tsx",
          "line": 13,
          "fragment": "import { canSearch, effectiveQuery, gapsNeedPolling, resultLine } from '../model/gaps-model';"
        }
      },
      {
        "from": "learningFront/src/features/sources/ui/gaps-card.tsx",
        "to": "learningFront/src/features/sources/model/sources-model.ts",
        "evidence": {
          "path": "learningFront/src/features/sources/ui/gaps-card.tsx",
          "line": 14,
          "fragment": "import { STATUS_LABEL } from '../model/sources-model';"
        }
      },
      {
        "from": "learningFront/src/features/sources/ui/gaps-card.tsx",
        "to": "learningFront/src/shared/i18n/index.ts",
        "evidence": {
          "path": "learningFront/src/features/sources/ui/gaps-card.tsx",
          "line": 15,
          "fragment": "import { useI18n } from '@/shared/i18n';"
        }
      },
      {
        "from": "learningFront/src/features/sources/ui/sources-panel.tsx",
        "to": "learningFront/src/shared/api/index.ts",
        "evidence": {
          "path": "learningFront/src/features/sources/ui/sources-panel.tsx",
          "line": 11,
          "fragment": "} from '@/shared/api';"
        }
      },
      {
        "from": "learningFront/src/features/sources/ui/sources-panel.tsx",
        "to": "learningFront/src/shared/ui/index.ts",
        "evidence": {
          "path": "learningFront/src/features/sources/ui/sources-panel.tsx",
          "line": 12,
          "fragment": "import { Body, Button, Card, Field, Label, Muted, Note, Progress, space } from '@/shared/ui';"
        }
      },
      {
        "from": "learningFront/src/features/sources/ui/sources-panel.tsx",
        "to": "learningFront/src/features/sources/model/sources-model.ts",
        "evidence": {
          "path": "learningFront/src/features/sources/ui/sources-panel.tsx",
          "line": 21,
          "fragment": "} from '../model/sources-model';"
        }
      },
      {
        "from": "learningFront/src/features/sources/ui/sources-panel.tsx",
        "to": "learningFront/src/shared/i18n/index.ts",
        "evidence": {
          "path": "learningFront/src/features/sources/ui/sources-panel.tsx",
          "line": 22,
          "fragment": "import { useI18n } from '@/shared/i18n';"
        }
      },
      {
        "from": "learningFront/src/pages/home/model/tiles-model.test.ts",
        "to": "learningFront/src/pages/home/model/tiles-model.ts",
        "evidence": {
          "path": "learningFront/src/pages/home/model/tiles-model.test.ts",
          "line": 2,
          "fragment": "import { moveId, orderTiles } from '../model/tiles-model';"
        }
      },
      {
        "from": "learningFront/src/pages/home/ui/state-hero.tsx",
        "to": "learningFront/src/shared/ui/index.ts",
        "evidence": {
          "path": "learningFront/src/pages/home/ui/state-hero.tsx",
          "line": 5,
          "fragment": "import { Button, Card, Display, Label, Muted, Pill, Title, space } from '@/shared/ui';"
        }
      },
      {
        "from": "learningFront/src/pages/home/ui/today-tiles.tsx",
        "to": "learningFront/src/shared/lib/index.ts",
        "evidence": {
          "path": "learningFront/src/pages/home/ui/today-tiles.tsx",
          "line": 5,
          "fragment": "import { rememberFlag, remembered, rememberedText, rememberText } from '@/shared/lib';"
        }
      },
      {
        "from": "learningFront/src/pages/home/ui/today-tiles.tsx",
        "to": "learningFront/src/shared/ui/index.ts",
        "evidence": {
          "path": "learningFront/src/pages/home/ui/today-tiles.tsx",
          "line": 6,
          "fragment": "import { Card, Label, Muted, space } from '@/shared/ui';"
        }
      },
      {
        "from": "learningFront/src/pages/home/ui/today-tiles.tsx",
        "to": "learningFront/src/pages/home/model/tiles-model.ts",
        "evidence": {
          "path": "learningFront/src/pages/home/ui/today-tiles.tsx",
          "line": 7,
          "fragment": "import { moveId, orderTiles } from '../model/tiles-model';"
        }
      },
      {
        "from": "learningFront/src/pages/home/ui/today-tiles.tsx",
        "to": "learningFront/src/shared/i18n/index.ts",
        "evidence": {
          "path": "learningFront/src/pages/home/ui/today-tiles.tsx",
          "line": 8,
          "fragment": "import { useI18n } from '@/shared/i18n';"
        }
      },
      {
        "from": "learningFront/src/pages/library/index.ts",
        "to": "learningFront/src/pages/library/ui/library-screen.tsx",
        "evidence": {
          "path": "learningFront/src/pages/library/index.ts",
          "line": 1,
          "fragment": "export { LibraryScreen } from './ui/library-screen';"
        }
      },
      {
        "from": "learningFront/src/pages/library/ui/library-screen.tsx",
        "to": "learningFront/src/entities/session/index.ts",
        "evidence": {
          "path": "learningFront/src/pages/library/ui/library-screen.tsx",
          "line": 3,
          "fragment": "import { useSession } from '@/entities/session';"
        }
      },
      {
        "from": "learningFront/src/pages/library/ui/library-screen.tsx",
        "to": "learningFront/src/shared/api/index.ts",
        "evidence": {
          "path": "learningFront/src/pages/library/ui/library-screen.tsx",
          "line": 12,
          "fragment": "} from '@/shared/api';"
        }
      },
      {
        "from": "learningFront/src/pages/library/ui/library-screen.tsx",
        "to": "learningFront/src/shared/ui/index.ts",
        "evidence": {
          "path": "learningFront/src/pages/library/ui/library-screen.tsx",
          "line": 14,
          "fragment": "import { Button, Card, Empty, Label, Muted, Note, Pill, Screen, space, TopBar } from '@/shared/ui';"
        }
      },
      {
        "from": "learningFront/src/pages/library/ui/library-screen.tsx",
        "to": "learningFront/src/shared/i18n/index.ts",
        "evidence": {
          "path": "learningFront/src/pages/library/ui/library-screen.tsx",
          "line": 15,
          "fragment": "import { useI18n, type Key } from '@/shared/i18n';"
        }
      },
      {
        "from": "learningFront/src/pages/problems/index.ts",
        "to": "learningFront/src/pages/problems/ui/problems-screen.tsx",
        "evidence": {
          "path": "learningFront/src/pages/problems/index.ts",
          "line": 1,
          "fragment": "export { ProblemsScreen } from './ui/problems-screen';"
        }
      },
      {
        "from": "learningFront/src/pages/problems/ui/problems-screen.tsx",
        "to": "learningFront/src/features/claim-problems/index.ts",
        "evidence": {
          "path": "learningFront/src/pages/problems/ui/problems-screen.tsx",
          "line": 2,
          "fragment": "import { ProblemPool } from '@/features/claim-problems';"
        }
      },
      {
        "from": "learningFront/src/pages/problems/ui/problems-screen.tsx",
        "to": "learningFront/src/shared/ui/index.ts",
        "evidence": {
          "path": "learningFront/src/pages/problems/ui/problems-screen.tsx",
          "line": 3,
          "fragment": "import { Screen, TopBar } from '@/shared/ui';"
        }
      },
      {
        "from": "learningFront/src/pages/problems/ui/problems-screen.tsx",
        "to": "learningFront/src/shared/i18n/index.ts",
        "evidence": {
          "path": "learningFront/src/pages/problems/ui/problems-screen.tsx",
          "line": 4,
          "fragment": "import { useI18n } from '@/shared/i18n';"
        }
      },
      {
        "from": "learningFront/src/pages/skill-profile/index.ts",
        "to": "learningFront/src/pages/skill-profile/ui/skill-profile-screen.tsx",
        "evidence": {
          "path": "learningFront/src/pages/skill-profile/index.ts",
          "line": 1,
          "fragment": "export { SkillProfileScreen } from './ui/skill-profile-screen';"
        }
      },
      {
        "from": "learningFront/src/pages/skill-profile/ui/skill-profile-screen.tsx",
        "to": "learningFront/src/entities/session/index.ts",
        "evidence": {
          "path": "learningFront/src/pages/skill-profile/ui/skill-profile-screen.tsx",
          "line": 2,
          "fragment": "import { useSession } from '@/entities/session';"
        }
      },
      {
        "from": "learningFront/src/pages/skill-profile/ui/skill-profile-screen.tsx",
        "to": "learningFront/src/features/skill-profile/index.ts",
        "evidence": {
          "path": "learningFront/src/pages/skill-profile/ui/skill-profile-screen.tsx",
          "line": 3,
          "fragment": "import { SkillProfileEditor } from '@/features/skill-profile';"
        }
      },
      {
        "from": "learningFront/src/pages/skill-profile/ui/skill-profile-screen.tsx",
        "to": "learningFront/src/shared/ui/index.ts",
        "evidence": {
          "path": "learningFront/src/pages/skill-profile/ui/skill-profile-screen.tsx",
          "line": 4,
          "fragment": "import { Empty, Muted, Screen, TopBar } from '@/shared/ui';"
        }
      },
      {
        "from": "learningFront/src/pages/skill-profile/ui/skill-profile-screen.tsx",
        "to": "learningFront/src/shared/i18n/index.ts",
        "evidence": {
          "path": "learningFront/src/pages/skill-profile/ui/skill-profile-screen.tsx",
          "line": 5,
          "fragment": "import { useI18n } from '@/shared/i18n';"
        }
      },
      {
        "from": "learningFront/src/pages/sources/index.ts",
        "to": "learningFront/src/pages/sources/ui/sources-screen.tsx",
        "evidence": {
          "path": "learningFront/src/pages/sources/index.ts",
          "line": 1,
          "fragment": "export { SourcesScreen } from './ui/sources-screen';"
        }
      },
      {
        "from": "learningFront/src/pages/sources/ui/sources-screen.tsx",
        "to": "learningFront/src/entities/session/index.ts",
        "evidence": {
          "path": "learningFront/src/pages/sources/ui/sources-screen.tsx",
          "line": 2,
          "fragment": "import { useSession } from '@/entities/session';"
        }
      },
      {
        "from": "learningFront/src/pages/sources/ui/sources-screen.tsx",
        "to": "learningFront/src/features/sources/index.ts",
        "evidence": {
          "path": "learningFront/src/pages/sources/ui/sources-screen.tsx",
          "line": 3,
          "fragment": "import { GapsCard, SourcesPanel } from '@/features/sources';"
        }
      },
      {
        "from": "learningFront/src/pages/sources/ui/sources-screen.tsx",
        "to": "learningFront/src/shared/ui/index.ts",
        "evidence": {
          "path": "learningFront/src/pages/sources/ui/sources-screen.tsx",
          "line": 4,
          "fragment": "import { Muted, Screen, TopBar } from '@/shared/ui';"
        }
      },
      {
        "from": "learningFront/src/pages/sources/ui/sources-screen.tsx",
        "to": "learningFront/src/shared/i18n/index.ts",
        "evidence": {
          "path": "learningFront/src/pages/sources/ui/sources-screen.tsx",
          "line": 5,
          "fragment": "import { useI18n } from '@/shared/i18n';"
        }
      },
      {
        "from": "learningFront/src/shared/api/claims-api.ts",
        "to": "learningFront/src/shared/api/http.ts",
        "evidence": {
          "path": "learningFront/src/shared/api/claims-api.ts",
          "line": 4,
          "fragment": "import { api } from './http';"
        }
      },
      {
        "from": "learningFront/src/shared/api/error-text.ts",
        "to": "learningFront/src/shared/i18n/translate.ts",
        "evidence": {
          "path": "learningFront/src/shared/api/error-text.ts",
          "line": 2,
          "fragment": "import { translate } from '../i18n/translate';"
        }
      },
      {
        "from": "learningFront/src/shared/api/error-text.ts",
        "to": "learningFront/src/shared/i18n/ru.ts",
        "evidence": {
          "path": "learningFront/src/shared/api/error-text.ts",
          "line": 3,
          "fragment": "import { ru, type Key } from '../i18n/ru';"
        }
      },
      {
        "from": "learningFront/src/shared/api/error-text.ts",
        "to": "learningFront/src/shared/api/http.ts",
        "evidence": {
          "path": "learningFront/src/shared/api/error-text.ts",
          "line": 4,
          "fragment": "import { ApiError, NetworkError } from './http';"
        }
      },
      {
        "from": "learningFront/src/shared/api/lang-api.ts",
        "to": "learningFront/src/shared/api/auth-api.ts",
        "evidence": {
          "path": "learningFront/src/shared/api/lang-api.ts",
          "line": 3,
          "fragment": "import type { AuthUser } from './auth-api';"
        }
      },
      {
        "from": "learningFront/src/shared/api/lang-api.ts",
        "to": "learningFront/src/shared/api/http.ts",
        "evidence": {
          "path": "learningFront/src/shared/api/lang-api.ts",
          "line": 4,
          "fragment": "import { api } from './http';"
        }
      },
      {
        "from": "learningFront/src/shared/api/notification-route.test.ts",
        "to": "learningFront/src/shared/api/notification-route.ts",
        "evidence": {
          "path": "learningFront/src/shared/api/notification-route.test.ts",
          "line": 2,
          "fragment": "import { targetForNotification } from './notification-route';"
        }
      },
      {
        "from": "learningFront/src/shared/api/notifications-api.ts",
        "to": "learningFront/src/shared/api/http.ts",
        "evidence": {
          "path": "learningFront/src/shared/api/notifications-api.ts",
          "line": 2,
          "fragment": "import { api } from './http';"
        }
      },
      {
        "from": "learningFront/src/shared/api/prior-test-api.ts",
        "to": "learningFront/src/shared/api/http.ts",
        "evidence": {
          "path": "learningFront/src/shared/api/prior-test-api.ts",
          "line": 2,
          "fragment": "import { api } from './http';"
        }
      },
      {
        "from": "learningFront/src/shared/api/prior-test-api.ts",
        "to": "learningFront/src/shared/api/graph-api.ts",
        "evidence": {
          "path": "learningFront/src/shared/api/prior-test-api.ts",
          "line": 3,
          "fragment": "import type { ProbeItem } from './graph-api';"
        }
      },
      {
        "from": "learningFront/src/shared/api/push-api.ts",
        "to": "learningFront/src/shared/api/http.ts",
        "evidence": {
          "path": "learningFront/src/shared/api/push-api.ts",
          "line": 2,
          "fragment": "import { api } from './http';"
        }
      },
      {
        "from": "learningFront/src/shared/api/push-device.ts",
        "to": "learningFront/src/shared/api/push-api.ts",
        "evidence": {
          "path": "learningFront/src/shared/api/push-device.ts",
          "line": 8,
          "fragment": "import { removePushDevice } from './push-api';"
        }
      },
      {
        "from": "learningFront/src/shared/api/push-device.web.ts",
        "to": "learningFront/src/shared/api/push-device.ts",
        "evidence": {
          "path": "learningFront/src/shared/api/push-device.web.ts",
          "line": 2,
          "fragment": "import type { PushTokenResult } from './push-device';"
        }
      },
      {
        "from": "learningFront/src/shared/api/skill-profile-api.ts",
        "to": "learningFront/src/shared/api/http.ts",
        "evidence": {
          "path": "learningFront/src/shared/api/skill-profile-api.ts",
          "line": 2,
          "fragment": "import { api } from './http';"
        }
      },
      {
        "from": "learningFront/src/shared/api/sources-api.ts",
        "to": "learningFront/src/shared/api/http.ts",
        "evidence": {
          "path": "learningFront/src/shared/api/sources-api.ts",
          "line": 3,
          "fragment": "import { api, ApiError, apiUrl, CLIENT_HEADERS, getBaseUrl, NetworkError } from './http';"
        }
      },
      {
        "from": "learningFront/src/shared/api/sources-api.ts",
        "to": "learningFront/src/shared/api/materials-api.ts",
        "evidence": {
          "path": "learningFront/src/shared/api/sources-api.ts",
          "line": 4,
          "fragment": "import type { PickedFile } from './materials-api';"
        }
      },
      {
        "from": "learningFront/src/shared/api/sources-api.ts",
        "to": "learningFront/src/shared/api/token.ts",
        "evidence": {
          "path": "learningFront/src/shared/api/sources-api.ts",
          "line": 5,
          "fragment": "import { getToken } from './token';"
        }
      },
      {
        "from": "learningFront/src/shared/api/sources-api.ts",
        "to": "learningFront/src/shared/i18n/translate.ts",
        "evidence": {
          "path": "learningFront/src/shared/api/sources-api.ts",
          "line": 6,
          "fragment": "import { translate } from '../i18n/translate';"
        }
      },
      {
        "from": "learningFront/src/shared/api/subjects-api.ts",
        "to": "learningFront/src/shared/api/http.ts",
        "evidence": {
          "path": "learningFront/src/shared/api/subjects-api.ts",
          "line": 2,
          "fragment": "import { api } from './http';"
        }
      },
      {
        "from": "learningFront/src/shared/config/design.test.ts",
        "to": "learningFront/src/shared/config/design.ts",
        "evidence": {
          "path": "learningFront/src/shared/config/design.test.ts",
          "line": 2,
          "fragment": "import { Themes, typography, type ThemeColors } from './design';"
        }
      },
      {
        "from": "learningFront/src/shared/i18n/en.ts",
        "to": "learningFront/src/shared/i18n/core.ts",
        "evidence": {
          "path": "learningFront/src/shared/i18n/en.ts",
          "line": 2,
          "fragment": "import type { Dictionary } from './core';"
        }
      },
      {
        "from": "learningFront/src/shared/i18n/en.ts",
        "to": "learningFront/src/shared/i18n/ru.ts",
        "evidence": {
          "path": "learningFront/src/shared/i18n/en.ts",
          "line": 3,
          "fragment": "import type { Key } from './ru';"
        }
      },
      {
        "from": "learningFront/src/shared/i18n/i18n-context.tsx",
        "to": "learningFront/src/shared/i18n/core.ts",
        "evidence": {
          "path": "learningFront/src/shared/i18n/i18n-context.tsx",
          "line": 22,
          "fragment": "} from './core';"
        }
      },
      {
        "from": "learningFront/src/shared/i18n/i18n-context.tsx",
        "to": "learningFront/src/shared/i18n/lang-storage.ts",
        "evidence": {
          "path": "learningFront/src/shared/i18n/i18n-context.tsx",
          "line": 23,
          "fragment": "import { getStoredLang, setStoredLang } from './lang-storage';"
        }
      },
      {
        "from": "learningFront/src/shared/i18n/i18n-context.tsx",
        "to": "learningFront/src/shared/i18n/translate.ts",
        "evidence": {
          "path": "learningFront/src/shared/i18n/i18n-context.tsx",
          "line": 24,
          "fragment": "import { currentLang, dictionaries, setCurrentLang } from './translate';"
        }
      },
      {
        "from": "learningFront/src/shared/i18n/i18n-context.tsx",
        "to": "learningFront/src/shared/i18n/ru.ts",
        "evidence": {
          "path": "learningFront/src/shared/i18n/i18n-context.tsx",
          "line": 25,
          "fragment": "import type { Key } from './ru';"
        }
      },
      {
        "from": "learningFront/src/shared/i18n/i18n.test.ts",
        "to": "learningFront/src/shared/api/http.ts",
        "evidence": {
          "path": "learningFront/src/shared/i18n/i18n.test.ts",
          "line": 8,
          "fragment": "import { ApiError, NetworkError } from '../api/http';"
        }
      },
      {
        "from": "learningFront/src/shared/i18n/i18n.test.ts",
        "to": "learningFront/src/shared/api/error-text.ts",
        "evidence": {
          "path": "learningFront/src/shared/i18n/i18n.test.ts",
          "line": 9,
          "fragment": "import { errorText } from '../api/error-text';"
        }
      },
      {
        "from": "learningFront/src/shared/i18n/i18n.test.ts",
        "to": "learningFront/src/shared/i18n/core.ts",
        "evidence": {
          "path": "learningFront/src/shared/i18n/i18n.test.ts",
          "line": 10,
          "fragment": "import { pluralCategory, render, type Entry } from './core';"
        }
      },
      {
        "from": "learningFront/src/shared/i18n/i18n.test.ts",
        "to": "learningFront/src/shared/i18n/en.ts",
        "evidence": {
          "path": "learningFront/src/shared/i18n/i18n.test.ts",
          "line": 11,
          "fragment": "import { en } from './en';"
        }
      },
      {
        "from": "learningFront/src/shared/i18n/i18n.test.ts",
        "to": "learningFront/src/shared/i18n/ru.ts",
        "evidence": {
          "path": "learningFront/src/shared/i18n/i18n.test.ts",
          "line": 12,
          "fragment": "import { ru } from './ru';"
        }
      },
      {
        "from": "learningFront/src/shared/i18n/i18n.test.ts",
        "to": "learningFront/src/shared/i18n/translate.ts",
        "evidence": {
          "path": "learningFront/src/shared/i18n/i18n.test.ts",
          "line": 13,
          "fragment": "import { setCurrentLang } from './translate';"
        }
      },
      {
        "from": "learningFront/src/shared/i18n/index.ts",
        "to": "learningFront/src/shared/i18n/i18n-context.tsx",
        "evidence": {
          "path": "learningFront/src/shared/i18n/index.ts",
          "line": 2,
          "fragment": "export { I18nProvider, useI18n } from './i18n-context';"
        }
      },
      {
        "from": "learningFront/src/shared/i18n/index.ts",
        "to": "learningFront/src/shared/i18n/translate.ts",
        "evidence": {
          "path": "learningFront/src/shared/i18n/index.ts",
          "line": 3,
          "fragment": "export { currentLang, setCurrentLang, translate } from './translate';"
        }
      },
      {
        "from": "learningFront/src/shared/i18n/index.ts",
        "to": "learningFront/src/shared/i18n/core.ts",
        "evidence": {
          "path": "learningFront/src/shared/i18n/index.ts",
          "line": 18,
          "fragment": "} from './core';"
        }
      },
      {
        "from": "learningFront/src/shared/i18n/index.ts",
        "to": "learningFront/src/shared/i18n/ru.ts",
        "evidence": {
          "path": "learningFront/src/shared/i18n/index.ts",
          "line": 19,
          "fragment": "export type { Key } from './ru';"
        }
      },
      {
        "from": "learningFront/src/shared/i18n/lang-storage.ts",
        "to": "learningFront/src/shared/i18n/core.ts",
        "evidence": {
          "path": "learningFront/src/shared/i18n/lang-storage.ts",
          "line": 4,
          "fragment": "import { isLang, type Lang } from './core';"
        }
      },
      {
        "from": "learningFront/src/shared/i18n/lang-storage.web.ts",
        "to": "learningFront/src/shared/i18n/core.ts",
        "evidence": {
          "path": "learningFront/src/shared/i18n/lang-storage.web.ts",
          "line": 2,
          "fragment": "import { isLang, type Lang } from './core';"
        }
      },
      {
        "from": "learningFront/src/shared/i18n/ru.ts",
        "to": "learningFront/src/shared/i18n/core.ts",
        "evidence": {
          "path": "learningFront/src/shared/i18n/ru.ts",
          "line": 3,
          "fragment": "import type { Dictionary } from './core';"
        }
      },
      {
        "from": "learningFront/src/shared/i18n/translate.ts",
        "to": "learningFront/src/shared/i18n/core.ts",
        "evidence": {
          "path": "learningFront/src/shared/i18n/translate.ts",
          "line": 2,
          "fragment": "import { deviceLocale, lookup, pickLanguage, type Lang, type Params } from './core';"
        }
      },
      {
        "from": "learningFront/src/shared/i18n/translate.ts",
        "to": "learningFront/src/shared/i18n/en.ts",
        "evidence": {
          "path": "learningFront/src/shared/i18n/translate.ts",
          "line": 3,
          "fragment": "import { en } from './en';"
        }
      },
      {
        "from": "learningFront/src/shared/i18n/translate.ts",
        "to": "learningFront/src/shared/i18n/ru.ts",
        "evidence": {
          "path": "learningFront/src/shared/i18n/translate.ts",
          "line": 4,
          "fragment": "import { ru, type Key } from './ru';"
        }
      },
      {
        "from": "learningFront/src/shared/ui/area-progress.tsx",
        "to": "learningFront/src/shared/ui/kit.tsx",
        "evidence": {
          "path": "learningFront/src/shared/ui/area-progress.tsx",
          "line": 3,
          "fragment": "import { Body, Pill } from './kit';"
        }
      },
      {
        "from": "learningFront/src/shared/ui/area-progress.tsx",
        "to": "learningFront/src/shared/ui/theme.tsx",
        "evidence": {
          "path": "learningFront/src/shared/ui/area-progress.tsx",
          "line": 4,
          "fragment": "import { space } from './theme';"
        }
      },
      {
        "from": "learningFront/src/shared/ui/area-progress.tsx",
        "to": "learningFront/src/shared/i18n/index.ts",
        "evidence": {
          "path": "learningFront/src/shared/ui/area-progress.tsx",
          "line": 5,
          "fragment": "import { translate } from '@/shared/i18n';"
        }
      },
      {
        "from": "learningFront/src/shared/ui/backdrop.ts",
        "to": "learningFront/src/shared/ui/color.ts",
        "evidence": {
          "path": "learningFront/src/shared/ui/backdrop.ts",
          "line": 5,
          "fragment": "import { withAlpha } from './color';"
        }
      },
      {
        "from": "learningFront/src/shared/ui/backdrop.ts",
        "to": "learningFront/src/shared/config/index.ts",
        "evidence": {
          "path": "learningFront/src/shared/ui/backdrop.ts",
          "line": 6,
          "fragment": "import type { ThemeName } from '@/shared/config';"
        }
      },
      {
        "from": "learningFront/src/shared/ui/nav-layout.test.ts",
        "to": "learningFront/src/shared/ui/nav-layout.ts",
        "evidence": {
          "path": "learningFront/src/shared/ui/nav-layout.test.ts",
          "line": 8,
          "fragment": "} from './nav-layout';"
        }
      },
      {
        "from": "learningFront/src/shared/ui/nav-layout.test.ts",
        "to": "learningFront/src/shared/ui/color.ts",
        "evidence": {
          "path": "learningFront/src/shared/ui/nav-layout.test.ts",
          "line": 9,
          "fragment": "import { mixColors, withAlpha } from './color';"
        }
      },
      {
        "from": "learningFront/src/shared/ui/nav-layout.ts",
        "to": "learningFront/src/shared/config/index.ts",
        "evidence": {
          "path": "learningFront/src/shared/ui/nav-layout.ts",
          "line": 3,
          "fragment": "import { grid } from '../config';"
        }
      },
      {
        "from": "learningFront/src/shared/ui/nav-layout.ts",
        "to": "learningFront/src/shared/i18n/index.ts",
        "evidence": {
          "path": "learningFront/src/shared/ui/nav-layout.ts",
          "line": 4,
          "fragment": "import type { Key } from '@/shared/i18n';"
        }
      },
      {
        "from": "learningFront/src/shared/ui/nav-layout.ts",
        "to": "learningFront/src/shared/ui/color.ts",
        "evidence": {
          "path": "learningFront/src/shared/ui/nav-layout.ts",
          "line": 6,
          "fragment": "export { withAlpha } from './color';"
        }
      },
      {
        "from": "learningFront/src/shared/ui/theme-mode.test.ts",
        "to": "learningFront/src/shared/ui/theme-mode.ts",
        "evidence": {
          "path": "learningFront/src/shared/ui/theme-mode.test.ts",
          "line": 2,
          "fragment": "import { parseThemeMode, resolveThemeName, THEME_MODES } from './theme-mode';"
        }
      },
      {
        "from": "learningFront/src/shared/ui/theme-mode.ts",
        "to": "learningFront/src/shared/config/index.ts",
        "evidence": {
          "path": "learningFront/src/shared/ui/theme-mode.ts",
          "line": 2,
          "fragment": "import type { ThemeName } from '@/shared/config';"
        }
      },
      {
        "from": "learningFront/src/shared/ui/theme-mode.ts",
        "to": "learningFront/src/shared/i18n/translate.ts",
        "evidence": {
          "path": "learningFront/src/shared/ui/theme-mode.ts",
          "line": 3,
          "fragment": "import { translate } from '../i18n/translate';"
        }
      },
      {
        "from": "learningFront/src/test-setup.ts",
        "to": "learningFront/src/shared/i18n/translate.ts",
        "evidence": {
          "path": "learningFront/src/test-setup.ts",
          "line": 1,
          "fragment": "import { setCurrentLang } from './shared/i18n/translate';"
        }
      },
      {
        "from": "learningFront/src/widgets/app-nav/index.ts",
        "to": "learningFront/src/widgets/app-nav/ui/app-nav.tsx",
        "evidence": {
          "path": "learningFront/src/widgets/app-nav/index.ts",
          "line": 1,
          "fragment": "export { AppShell } from './ui/app-nav';"
        }
      },
      {
        "from": "learningFront/src/widgets/app-nav/ui/app-nav.tsx",
        "to": "learningFront/src/entities/session/index.ts",
        "evidence": {
          "path": "learningFront/src/widgets/app-nav/ui/app-nav.tsx",
          "line": 10,
          "fragment": "import { useSession } from '@/entities/session';"
        }
      },
      {
        "from": "learningFront/src/widgets/app-nav/ui/app-nav.tsx",
        "to": "learningFront/src/shared/ui/index.ts",
        "evidence": {
          "path": "learningFront/src/widgets/app-nav/ui/app-nav.tsx",
          "line": 23,
          "fragment": "} from '@/shared/ui';"
        }
      },
      {
        "from": "learningFront/src/widgets/app-nav/ui/app-nav.tsx",
        "to": "learningFront/src/shared/i18n/index.ts",
        "evidence": {
          "path": "learningFront/src/widgets/app-nav/ui/app-nav.tsx",
          "line": 24,
          "fragment": "import { useI18n, type Key } from '@/shared/i18n';"
        }
      },
      {
        "from": "learningFront/src/widgets/module-registry/recall-payload.test.ts",
        "to": "learningFront/src/widgets/module-registry/recall-payload.ts",
        "evidence": {
          "path": "learningFront/src/widgets/module-registry/recall-payload.test.ts",
          "line": 2,
          "fragment": "import { isCourseStepPayload } from './recall-payload';"
        }
      },
      {
        "from": "learningFront/src/widgets/module-registry/recall-renderer.tsx",
        "to": "learningFront/src/shared/engine/index.ts",
        "evidence": {
          "path": "learningFront/src/widgets/module-registry/recall-renderer.tsx",
          "line": 5,
          "fragment": "import type { ActivityRendererProps } from '@/shared/engine';"
        }
      },
      {
        "from": "learningFront/src/widgets/module-registry/recall-renderer.tsx",
        "to": "learningFront/src/features/concept-recall/index.ts",
        "evidence": {
          "path": "learningFront/src/widgets/module-registry/recall-renderer.tsx",
          "line": 6,
          "fragment": "import { ConceptRecallActivity } from '@/features/concept-recall';"
        }
      },
      {
        "from": "learningFront/src/widgets/module-registry/recall-renderer.tsx",
        "to": "learningFront/src/features/concept-study/index.ts",
        "evidence": {
          "path": "learningFront/src/widgets/module-registry/recall-renderer.tsx",
          "line": 7,
          "fragment": "import { ConceptQuestionActivity } from '@/features/concept-study';"
        }
      },
      {
        "from": "learningFront/src/widgets/module-registry/recall-renderer.tsx",
        "to": "learningFront/src/widgets/module-registry/recall-payload.ts",
        "evidence": {
          "path": "learningFront/src/widgets/module-registry/recall-renderer.tsx",
          "line": 8,
          "fragment": "import { isCourseStepPayload } from './recall-payload';"
        }
      },
      {
        "from": "learningFront/src/widgets/subject-bar/index.tsx",
        "to": "learningFront/src/entities/session/index.ts",
        "evidence": {
          "path": "learningFront/src/widgets/subject-bar/index.tsx",
          "line": 3,
          "fragment": "import { useSession } from '@/entities/session';"
        }
      },
      {
        "from": "learningFront/src/widgets/subject-bar/index.tsx",
        "to": "learningFront/src/shared/ui/index.ts",
        "evidence": {
          "path": "learningFront/src/widgets/subject-bar/index.tsx",
          "line": 4,
          "fragment": "import { Muted, space } from '@/shared/ui';"
        }
      },
      {
        "from": "learningFront/src/widgets/subject-bar/index.tsx",
        "to": "learningFront/src/shared/i18n/index.ts",
        "evidence": {
          "path": "learningFront/src/widgets/subject-bar/index.tsx",
          "line": 5,
          "fragment": "import { useI18n } from '@/shared/i18n';"
        }
      }
    ]
  }
}
```

## Потоки данных

```docdd-dataflow
{
  "added": {
    "sources": [
      {
        "id": "db-postgres",
        "kind": "db",
        "where": "settings.database_url (Postgres)"
      },
      {
        "id": "env-root",
        "kind": "env",
        "where": "../.env (корень репозитория)"
      },
      {
        "id": "file-object-store",
        "kind": "file",
        "where": "settings.s3_endpoint (S3-хранилище источников, SeaweedFS)"
      },
      {
        "id": "http-backend-api",
        "kind": "http",
        "where": "EXPO_PUBLIC_API_BASE_URL (backend FastAPI, по умолчанию http://localhost:8000)"
      },
      {
        "id": "http-llm-provider",
        "kind": "http",
        "where": "settings.llm_base_url (RouterAI, OpenAI-совместимый)"
      }
    ],
    "flows": [
      {
        "from": "learningBack/core/embeddings.py",
        "to": "env-root",
        "direction": "read",
        "evidence": {
          "path": "learningBack/core/embeddings.py",
          "line": 20,
          "fragment": "from core.config import settings"
        }
      },
      {
        "from": "learningBack/core/objects.py",
        "to": "env-root",
        "direction": "read",
        "evidence": {
          "path": "learningBack/core/objects.py",
          "line": 19,
          "fragment": "from core.config import settings"
        }
      },
      {
        "from": "learningBack/core/push.py",
        "to": "env-root",
        "direction": "read",
        "evidence": {
          "path": "learningBack/core/push.py",
          "line": 26,
          "fragment": "from core.config import settings"
        }
      },
      {
        "from": "learningBack/modules/knowledge/funnel.py",
        "to": "env-root",
        "direction": "read",
        "evidence": {
          "path": "learningBack/modules/knowledge/funnel.py",
          "line": 19,
          "fragment": "from core.config import settings"
        }
      },
      {
        "from": "learningBack/modules/knowledge/graph_admin.py",
        "to": "db-postgres",
        "direction": "both",
        "evidence": {
          "path": "learningBack/modules/knowledge/graph_admin.py",
          "line": 20,
          "fragment": "from core.db import SessionLocal"
        }
      },
      {
        "from": "learningBack/modules/knowledge/ingest.py",
        "to": "env-root",
        "direction": "read",
        "evidence": {
          "path": "learningBack/modules/knowledge/ingest.py",
          "line": 28,
          "fragment": "from core.config import settings"
        }
      },
      {
        "from": "learningBack/modules/knowledge/ingest.py",
        "to": "file-object-store",
        "direction": "both",
        "evidence": {
          "path": "learningBack/modules/knowledge/ingest.py",
          "line": 30,
          "fragment": "from core.objects import ObjectStore, get_store"
        }
      },
      {
        "from": "learningBack/modules/knowledge/langs.py",
        "to": "env-root",
        "direction": "read",
        "evidence": {
          "path": "learningBack/modules/knowledge/langs.py",
          "line": 11,
          "fragment": "from core.config import settings"
        }
      },
      {
        "from": "learningBack/modules/knowledge/merge.py",
        "to": "env-root",
        "direction": "read",
        "evidence": {
          "path": "learningBack/modules/knowledge/merge.py",
          "line": 25,
          "fragment": "from core.config import settings"
        }
      },
      {
        "from": "learningBack/modules/knowledge/profile_api.py",
        "to": "http-llm-provider",
        "direction": "both",
        "evidence": {
          "path": "learningBack/modules/knowledge/profile_api.py",
          "line": 10,
          "fragment": "from core.ai_gateway import get_ai_gateway, has_llm"
        }
      },
      {
        "from": "learningBack/modules/knowledge/profile_match.py",
        "to": "env-root",
        "direction": "read",
        "evidence": {
          "path": "learningBack/modules/knowledge/profile_match.py",
          "line": 22,
          "fragment": "from core.config import settings"
        }
      },
      {
        "from": "learningBack/modules/knowledge/profile_sources.py",
        "to": "env-root",
        "direction": "read",
        "evidence": {
          "path": "learningBack/modules/knowledge/profile_sources.py",
          "line": 19,
          "fragment": "from core.config import settings"
        }
      },
      {
        "from": "learningBack/modules/knowledge/profile_store.py",
        "to": "http-llm-provider",
        "direction": "both",
        "evidence": {
          "path": "learningBack/modules/knowledge/profile_store.py",
          "line": 14,
          "fragment": "from core.ai_gateway import get_ai_gateway, has_llm"
        }
      },
      {
        "from": "learningBack/modules/knowledge/profile_store.py",
        "to": "env-root",
        "direction": "read",
        "evidence": {
          "path": "learningBack/modules/knowledge/profile_store.py",
          "line": 15,
          "fragment": "from core.config import settings"
        }
      },
      {
        "from": "learningBack/modules/knowledge/profile_store.py",
        "to": "db-postgres",
        "direction": "both",
        "evidence": {
          "path": "learningBack/modules/knowledge/profile_store.py",
          "line": 238,
          "fragment": "from core.db import SessionLocal"
        }
      },
      {
        "from": "learningBack/modules/knowledge/provenance.py",
        "to": "file-object-store",
        "direction": "both",
        "evidence": {
          "path": "learningBack/modules/knowledge/provenance.py",
          "line": 22,
          "fragment": "from core.objects import ObjectStore, get_store"
        }
      },
      {
        "from": "learningBack/modules/knowledge/provenance_api.py",
        "to": "env-root",
        "direction": "read",
        "evidence": {
          "path": "learningBack/modules/knowledge/provenance_api.py",
          "line": 14,
          "fragment": "from core.config import settings"
        }
      },
      {
        "from": "learningBack/modules/knowledge/reconcile.py",
        "to": "env-root",
        "direction": "read",
        "evidence": {
          "path": "learningBack/modules/knowledge/reconcile.py",
          "line": 20,
          "fragment": "from core.config import settings"
        }
      },
      {
        "from": "learningBack/modules/knowledge/skill_profile.py",
        "to": "http-llm-provider",
        "direction": "both",
        "evidence": {
          "path": "learningBack/modules/knowledge/skill_profile.py",
          "line": 19,
          "fragment": "from core.ai_gateway import get_ai_gateway, has_llm"
        }
      },
      {
        "from": "learningBack/modules/knowledge/source_search.py",
        "to": "env-root",
        "direction": "read",
        "evidence": {
          "path": "learningBack/modules/knowledge/source_search.py",
          "line": 26,
          "fragment": "from core.config import settings"
        }
      },
      {
        "from": "learningBack/modules/knowledge/theory.py",
        "to": "http-llm-provider",
        "direction": "both",
        "evidence": {
          "path": "learningBack/modules/knowledge/theory.py",
          "line": 15,
          "fragment": "from core.ai_gateway import get_ai_gateway, has_llm"
        }
      },
      {
        "from": "learningBack/scripts/backup_objects.py",
        "to": "env-root",
        "direction": "read",
        "evidence": {
          "path": "learningBack/scripts/backup_objects.py",
          "line": 19,
          "fragment": "from core.config import settings"
        }
      },
      {
        "from": "learningBack/scripts/backup_objects.py",
        "to": "file-object-store",
        "direction": "both",
        "evidence": {
          "path": "learningBack/scripts/backup_objects.py",
          "line": 20,
          "fragment": "from core.objects import S3ObjectStore, get_store"
        }
      },
      {
        "from": "learningBack/scripts/ingest_document.py",
        "to": "http-llm-provider",
        "direction": "both",
        "evidence": {
          "path": "learningBack/scripts/ingest_document.py",
          "line": 15,
          "fragment": "from core.ai_gateway import get_ai_gateway"
        }
      },
      {
        "from": "learningBack/scripts/ingest_document.py",
        "to": "db-postgres",
        "direction": "both",
        "evidence": {
          "path": "learningBack/scripts/ingest_document.py",
          "line": 16,
          "fragment": "from core.db import SessionLocal"
        }
      },
      {
        "from": "learningBack/scripts/merge_concepts.py",
        "to": "http-llm-provider",
        "direction": "both",
        "evidence": {
          "path": "learningBack/scripts/merge_concepts.py",
          "line": 13,
          "fragment": "from core.ai_gateway import get_ai_gateway"
        }
      },
      {
        "from": "learningBack/scripts/merge_concepts.py",
        "to": "db-postgres",
        "direction": "both",
        "evidence": {
          "path": "learningBack/scripts/merge_concepts.py",
          "line": 14,
          "fragment": "from core.db import SessionLocal"
        }
      },
      {
        "from": "learningBack/scripts/refresh_knowledge.py",
        "to": "db-postgres",
        "direction": "both",
        "evidence": {
          "path": "learningBack/scripts/refresh_knowledge.py",
          "line": 11,
          "fragment": "from core.db import SessionLocal"
        }
      },
      {
        "from": "learningBack/scripts/run_textbooks.py",
        "to": "http-llm-provider",
        "direction": "both",
        "evidence": {
          "path": "learningBack/scripts/run_textbooks.py",
          "line": 20,
          "fragment": "from core.ai_gateway import get_ai_gateway"
        }
      },
      {
        "from": "learningBack/scripts/run_textbooks.py",
        "to": "db-postgres",
        "direction": "both",
        "evidence": {
          "path": "learningBack/scripts/run_textbooks.py",
          "line": 21,
          "fragment": "from core.db import SessionLocal"
        }
      },
      {
        "from": "learningFront/src/shared/api/claims-api.ts",
        "to": "http-backend-api",
        "direction": "both",
        "evidence": {
          "path": "learningFront/src/shared/api/claims-api.ts",
          "line": 4,
          "fragment": "import { api } from './http';"
        }
      },
      {
        "from": "learningFront/src/shared/api/error-text.ts",
        "to": "http-backend-api",
        "direction": "both",
        "evidence": {
          "path": "learningFront/src/shared/api/error-text.ts",
          "line": 4,
          "fragment": "import { ApiError, NetworkError } from './http';"
        }
      },
      {
        "from": "learningFront/src/shared/api/lang-api.ts",
        "to": "http-backend-api",
        "direction": "both",
        "evidence": {
          "path": "learningFront/src/shared/api/lang-api.ts",
          "line": 4,
          "fragment": "import { api } from './http';"
        }
      },
      {
        "from": "learningFront/src/shared/api/notifications-api.ts",
        "to": "http-backend-api",
        "direction": "both",
        "evidence": {
          "path": "learningFront/src/shared/api/notifications-api.ts",
          "line": 2,
          "fragment": "import { api } from './http';"
        }
      },
      {
        "from": "learningFront/src/shared/api/prior-test-api.ts",
        "to": "http-backend-api",
        "direction": "both",
        "evidence": {
          "path": "learningFront/src/shared/api/prior-test-api.ts",
          "line": 2,
          "fragment": "import { api } from './http';"
        }
      },
      {
        "from": "learningFront/src/shared/api/push-api.ts",
        "to": "http-backend-api",
        "direction": "both",
        "evidence": {
          "path": "learningFront/src/shared/api/push-api.ts",
          "line": 2,
          "fragment": "import { api } from './http';"
        }
      },
      {
        "from": "learningFront/src/shared/api/skill-profile-api.ts",
        "to": "http-backend-api",
        "direction": "both",
        "evidence": {
          "path": "learningFront/src/shared/api/skill-profile-api.ts",
          "line": 2,
          "fragment": "import { api } from './http';"
        }
      },
      {
        "from": "learningFront/src/shared/api/sources-api.ts",
        "to": "http-backend-api",
        "direction": "both",
        "evidence": {
          "path": "learningFront/src/shared/api/sources-api.ts",
          "line": 3,
          "fragment": "import { api, ApiError, apiUrl, CLIENT_HEADERS, getBaseUrl, NetworkError } from './http';"
        }
      },
      {
        "from": "learningFront/src/shared/api/subjects-api.ts",
        "to": "http-backend-api",
        "direction": "both",
        "evidence": {
          "path": "learningFront/src/shared/api/subjects-api.ts",
          "line": 2,
          "fragment": "import { api } from './http';"
        }
      },
      {
        "from": "learningFront/src/shared/i18n/i18n.test.ts",
        "to": "http-backend-api",
        "direction": "both",
        "evidence": {
          "path": "learningFront/src/shared/i18n/i18n.test.ts",
          "line": 8,
          "fragment": "import { ApiError, NetworkError } from '../api/http';"
        }
      }
    ]
  }
}
```

## Пользовательские пути

```docdd-userflow
{
  "added": {
    "screens": [
      {
        "id": "/curator",
        "title": "curator",
        "file": "learningFront/src/app/curator.tsx"
      },
      {
        "id": "/library",
        "title": "library",
        "file": "learningFront/src/app/library.tsx"
      },
      {
        "id": "/problems",
        "title": "problems",
        "file": "learningFront/src/app/problems.tsx"
      },
      {
        "id": "/skill-profile",
        "title": "skill-profile",
        "file": "learningFront/src/app/skill-profile.tsx"
      },
      {
        "id": "/sources",
        "title": "sources",
        "file": "learningFront/src/app/sources.tsx"
      }
    ],
    "transitions": [
      {
        "from": "/curator",
        "to": "/sources",
        "trigger": "router",
        "evidence": {
          "path": "learningFront/src/app/curator.tsx",
          "line": 16,
          "fragment": "push('/sources"
        }
      },
      {
        "from": "/curator",
        "to": "/activities",
        "trigger": "router",
        "evidence": {
          "path": "learningFront/src/app/curator.tsx",
          "line": 20,
          "fragment": "push('/activities"
        }
      },
      {
        "from": "/library",
        "to": "/",
        "trigger": "router",
        "evidence": {
          "path": "learningFront/src/app/library.tsx",
          "line": 6,
          "fragment": "navigate('/"
        }
      }
    ],
    "calls": [
      {
        "from": "/curator",
        "to": "/graph/placement/{id}/chain-probe",
        "evidence": {
          "path": "learningFront/src/shared/api/prior-test-api.ts",
          "line": 53,
          "fragment": "api<ChainProbeResult>(`/graph/placement/${seg(domain)}/chain-probe"
        }
      },
      {
        "from": "/curator",
        "to": "/graph/placement/{id}/chain-answer",
        "evidence": {
          "path": "learningFront/src/shared/api/prior-test-api.ts",
          "line": 62,
          "fragment": "api<ChainAnswerResult>(`/graph/placement/${seg(domain)}/chain-answer"
        }
      },
      {
        "from": "/curator",
        "to": "/graph/placement/{id}/report",
        "evidence": {
          "path": "learningFront/src/shared/api/prior-test-api.ts",
          "line": 68,
          "fragment": "api<PriorReport>(`/graph/placement/${seg(domain)}/report"
        }
      },
      {
        "from": "/curator",
        "to": "/evidence",
        "evidence": {
          "path": "learningFront/src/shared/api/evidence-api.ts",
          "line": 27,
          "fragment": "api<{ accepted: number }>('/evidence"
        }
      },
      {
        "from": "/curator",
        "to": "/auth/me/lang",
        "evidence": {
          "path": "learningFront/src/shared/api/lang-api.ts",
          "line": 13,
          "fragment": "api<AuthUser>('/auth/me/lang"
        }
      },
      {
        "from": "/curator",
        "to": "/graph/subjects",
        "evidence": {
          "path": "learningFront/src/shared/api/subjects-api.ts",
          "line": 14,
          "fragment": "api<UserSubject[]>('/graph/subjects"
        }
      },
      {
        "from": "/curator",
        "to": "/graph/subjects/{id}",
        "evidence": {
          "path": "learningFront/src/shared/api/subjects-api.ts",
          "line": 20,
          "fragment": "api<UserSubject>(`/graph/subjects/${encodeURIComponent(id)}"
        }
      },
      {
        "from": "/curator",
        "to": "/content/materials",
        "evidence": {
          "path": "learningFront/src/shared/api/materials-api.ts",
          "line": 44,
          "fragment": "api<MaterialSummary[]>('/content/materials"
        }
      },
      {
        "from": "/curator",
        "to": "/content/materials/{id}",
        "evidence": {
          "path": "learningFront/src/shared/api/materials-api.ts",
          "line": 46,
          "fragment": "api<MaterialFull>(`/content/materials/${encodeURIComponent(id)}"
        }
      },
      {
        "from": "/curator",
        "to": "/graph/sources",
        "evidence": {
          "path": "learningFront/src/shared/api/sources-api.ts",
          "line": 51,
          "fragment": "api<SourceItem[]>('/graph/sources"
        }
      },
      {
        "from": "/curator",
        "to": "/graph/sources/{id}/progress",
        "evidence": {
          "path": "learningFront/src/shared/api/sources-api.ts",
          "line": 54,
          "fragment": "api<SourceProgress>(`/graph/sources/${encodeURIComponent(id)}/progress"
        }
      },
      {
        "from": "/curator",
        "to": "/graph/sources/gaps/{id}/fill",
        "evidence": {
          "path": "learningFront/src/shared/api/sources-api.ts",
          "line": 92,
          "fragment": "api<{ results: GapFillResult[] }>(`/graph/sources/gaps/${encodeURIComponent(goal)}/fill"
        }
      },
      {
        "from": "/curator",
        "to": "/graph/goal/clarify",
        "evidence": {
          "path": "learningFront/src/shared/api/goal-intake-api.ts",
          "line": 44,
          "fragment": "api<{ questions: GoalQuestion[] }>('/graph/goal/clarify"
        }
      },
      {
        "from": "/curator",
        "to": "/graph/goal/summarize",
        "evidence": {
          "path": "learningFront/src/shared/api/goal-intake-api.ts",
          "line": 50,
          "fragment": "api<GoalSummary>('/graph/goal/summarize"
        }
      },
      {
        "from": "/curator",
        "to": "/graph/goal/confirm",
        "evidence": {
          "path": "learningFront/src/shared/api/goal-intake-api.ts",
          "line": 57,
          "fragment": "api<GoalIntakeState>('/graph/goal/confirm"
        }
      },
      {
        "from": "/curator",
        "to": "/graph/goal/intake/{id}",
        "evidence": {
          "path": "learningFront/src/shared/api/goal-intake-api.ts",
          "line": 63,
          "fragment": "api<GoalIntakeState>(`/graph/goal/intake/${seg(domain)}"
        }
      },
      {
        "from": "/curator",
        "to": "/graph/goal/{id}/volume",
        "evidence": {
          "path": "learningFront/src/shared/api/goal-intake-api.ts",
          "line": 85,
          "fragment": "api<GoalVolume>(`/graph/goal/${seg(domain)}/volume"
        }
      },
      {
        "from": "/curator",
        "to": "/push",
        "evidence": {
          "path": "learningFront/src/shared/api/push-api.ts",
          "line": 11,
          "fragment": "api<PushState>('/push"
        }
      },
      {
        "from": "/curator",
        "to": "/push/devices",
        "evidence": {
          "path": "learningFront/src/shared/api/push-api.ts",
          "line": 14,
          "fragment": "api<PushState>('/push/devices"
        }
      },
      {
        "from": "/curator",
        "to": "/push/devices/remove",
        "evidence": {
          "path": "learningFront/src/shared/api/push-api.ts",
          "line": 17,
          "fragment": "api<{ removed: boolean }>('/push/devices/remove"
        }
      },
      {
        "from": "/curator",
        "to": "/push/enabled",
        "evidence": {
          "path": "learningFront/src/shared/api/push-api.ts",
          "line": 23,
          "fragment": "api<PushState>('/push/enabled"
        }
      },
      {
        "from": "/curator",
        "to": "/graph/notifications",
        "evidence": {
          "path": "learningFront/src/shared/api/notifications-api.ts",
          "line": 22,
          "fragment": "api<CourseNotification[]>('/graph/notifications"
        }
      },
      {
        "from": "/curator",
        "to": "/graph/notifications/read",
        "evidence": {
          "path": "learningFront/src/shared/api/notifications-api.ts",
          "line": 26,
          "fragment": "api<{ marked: number }>('/graph/notifications/read"
        }
      },
      {
        "from": "/curator",
        "to": "/graph/profile/{id}",
        "evidence": {
          "path": "learningFront/src/shared/api/skill-profile-api.ts",
          "line": 93,
          "fragment": "api<ProfileState>(`/graph/profile/${seg(domain)}"
        }
      },
      {
        "from": "/curator",
        "to": "/graph/profile/{id}/start",
        "evidence": {
          "path": "learningFront/src/shared/api/skill-profile-api.ts",
          "line": 100,
          "fragment": "api<ProfileState>(`/graph/profile/${seg(domain)}/start"
        }
      },
      {
        "from": "/curator",
        "to": "/graph/profile/{id}/fill",
        "evidence": {
          "path": "learningFront/src/shared/api/skill-profile-api.ts",
          "line": 104,
          "fragment": "api<ProfileState>(`/graph/profile/${seg(domain)}/fill"
        }
      },
      {
        "from": "/curator",
        "to": "/graph/profile/{id}/build",
        "evidence": {
          "path": "learningFront/src/shared/api/skill-profile-api.ts",
          "line": 113,
          "fragment": "api<ProfileState & { build: BuildReport }>(`/graph/profile/${seg(domain)}/build"
        }
      },
      {
        "from": "/curator",
        "to": "/graph/profile/{id}/coverage",
        "evidence": {
          "path": "learningFront/src/shared/api/skill-profile-api.ts",
          "line": 118,
          "fragment": "api<CoverageReport>(`/graph/profile/${seg(domain)}/coverage"
        }
      },
      {
        "from": "/curator",
        "to": "/graph/{id}",
        "evidence": {
          "path": "learningFront/src/shared/api/graph-api.ts",
          "line": 72,
          "fragment": "api<Graph>(`/graph/${seg(domain)}"
        }
      },
      {
        "from": "/curator",
        "to": "/graph/nodes/{id}",
        "evidence": {
          "path": "learningFront/src/shared/api/graph-api.ts",
          "line": 75,
          "fragment": "api<GraphNode>(`/graph/nodes/${seg(id)}"
        }
      },
      {
        "from": "/curator",
        "to": "/graph/canon/build",
        "evidence": {
          "path": "learningFront/src/shared/api/graph-api.ts",
          "line": 79,
          "fragment": "api<Graph>('/graph/canon/build"
        }
      },
      {
        "from": "/curator",
        "to": "/graph/goal/split",
        "evidence": {
          "path": "learningFront/src/shared/api/graph-api.ts",
          "line": 88,
          "fragment": "api<GoalSplit>('/graph/goal/split"
        }
      },
      {
        "from": "/curator",
        "to": "/graph/canon/recompute-centrality",
        "evidence": {
          "path": "learningFront/src/shared/api/graph-api.ts",
          "line": 101,
          "fragment": "api<CentralityRow[]>('/graph/canon/recompute-centrality"
        }
      },
      {
        "from": "/curator",
        "to": "/graph/canon/nodes/{id}/approve",
        "evidence": {
          "path": "learningFront/src/shared/api/graph-api.ts",
          "line": 107,
          "fragment": "api(`/graph/canon/nodes/${seg(conceptId)}/approve"
        }
      },
      {
        "from": "/curator",
        "to": "/graph/nodes/{id}/override",
        "evidence": {
          "path": "learningFront/src/shared/api/graph-api.ts",
          "line": 113,
          "fragment": "api(`/graph/nodes/${seg(baseConceptId)}/override"
        }
      },
      {
        "from": "/curator",
        "to": "/graph/user-nodes/{id}",
        "evidence": {
          "path": "learningFront/src/shared/api/graph-api.ts",
          "line": 119,
          "fragment": "api(`/graph/user-nodes/${seg(userConceptId)}"
        }
      },
      {
        "from": "/curator",
        "to": "/graph/expand",
        "evidence": {
          "path": "learningFront/src/shared/api/graph-api.ts",
          "line": 122,
          "fragment": "api<Graph>('/graph/expand"
        }
      },
      {
        "from": "/curator",
        "to": "/graph/materials/{id}/propose",
        "evidence": {
          "path": "learningFront/src/shared/api/graph-api.ts",
          "line": 148,
          "fragment": "api<MaterialProposal>(`/graph/materials/${seg(materialId)}/propose"
        }
      },
      {
        "from": "/curator",
        "to": "/graph/materials/{id}/accept",
        "evidence": {
          "path": "learningFront/src/shared/api/graph-api.ts",
          "line": 155,
          "fragment": "api<{ created: number; graph: Graph }>(`/graph/materials/${seg(materialId)}/accept"
        }
      },
      {
        "from": "/curator",
        "to": "/graph/placement/{id}/probe",
        "evidence": {
          "path": "learningFront/src/shared/api/graph-api.ts",
          "line": 225,
          "fragment": "api<ProbeResult>(`/graph/placement/${seg(domain)}/probe"
        }
      },
      {
        "from": "/curator",
        "to": "/graph/placement/answer",
        "evidence": {
          "path": "learningFront/src/shared/api/graph-api.ts",
          "line": 228,
          "fragment": "api<AnswerResult>('/graph/placement/answer"
        }
      },
      {
        "from": "/curator",
        "to": "/graph/placement/{id}/map",
        "evidence": {
          "path": "learningFront/src/shared/api/graph-api.ts",
          "line": 234,
          "fragment": "api<MasteryMap>(`/graph/placement/${seg(domain)}/map"
        }
      },
      {
        "from": "/curator",
        "to": "/graph/course/{id}",
        "evidence": {
          "path": "learningFront/src/shared/api/graph-api.ts",
          "line": 278,
          "fragment": "api<Course>(`/graph/course/${seg(domain)}"
        }
      },
      {
        "from": "/curator",
        "to": "/graph/course/{id}/complete",
        "evidence": {
          "path": "learningFront/src/shared/api/graph-api.ts",
          "line": 286,
          "fragment": "api<Course>(`/graph/course/${seg(domain)}/complete"
        }
      },
      {
        "from": "/curator",
        "to": "/graph/course/{id}/step/{id}/answer",
        "evidence": {
          "path": "learningFront/src/shared/api/graph-api.ts",
          "line": 324,
          "fragment": "api<StepResult>(`/graph/course/${seg(domain)}/step/${seg(conceptId)}/answer"
        }
      },
      {
        "from": "/curator",
        "to": "/graph/nodes",
        "evidence": {
          "path": "learningFront/src/shared/api/graph-api.ts",
          "line": 337,
          "fragment": "api<{ userConceptId: string }>('/graph/nodes"
        }
      },
      {
        "from": "/curator",
        "to": "/graph/user-edges",
        "evidence": {
          "path": "learningFront/src/shared/api/graph-api.ts",
          "line": 346,
          "fragment": "api<{ id: string }>('/graph/user-edges"
        }
      },
      {
        "from": "/curator",
        "to": "/me/study-methods",
        "evidence": {
          "path": "learningFront/src/shared/api/methods-api.ts",
          "line": 21,
          "fragment": "api<StudyMethodChoice>('/me/study-methods"
        }
      },
      {
        "from": "/curator",
        "to": "/graph/nodes/{id}/claims",
        "evidence": {
          "path": "learningFront/src/shared/api/claims-api.ts",
          "line": 33,
          "fragment": "api<NodeClaim[]>(`/graph/nodes/${seg(conceptId)}/claims"
        }
      },
      {
        "from": "/curator",
        "to": "/graph/claims/{id}/report",
        "evidence": {
          "path": "learningFront/src/shared/api/claims-api.ts",
          "line": 36,
          "fragment": "api<{ ok: boolean }>(`/graph/claims/${seg(claimId)}/report"
        }
      },
      {
        "from": "/curator",
        "to": "/graph/claims/problems",
        "evidence": {
          "path": "learningFront/src/shared/api/claims-api.ts",
          "line": 72,
          "fragment": "api<ClaimProblem[]>(`/graph/claims/problems"
        }
      },
      {
        "from": "/curator",
        "to": "/graph/claims/reports",
        "evidence": {
          "path": "learningFront/src/shared/api/claims-api.ts",
          "line": 88,
          "fragment": "api<ClaimReports[]>('/graph/claims/reports"
        }
      },
      {
        "from": "/curator",
        "to": "/graph/claims/rebuild",
        "evidence": {
          "path": "learningFront/src/shared/api/claims-api.ts",
          "line": 91,
          "fragment": "api<{ jobId: string }>(`/graph/claims/rebuild"
        }
      },
      {
        "from": "/curator",
        "to": "/auth/register",
        "evidence": {
          "path": "learningFront/src/shared/api/auth-api.ts",
          "line": 20,
          "fragment": "api<TokenResponse>('/auth/register"
        }
      },
      {
        "from": "/curator",
        "to": "/auth/login",
        "evidence": {
          "path": "learningFront/src/shared/api/auth-api.ts",
          "line": 30,
          "fragment": "api<TokenResponse>('/auth/login"
        }
      },
      {
        "from": "/curator",
        "to": "/auth/password-reset/request",
        "evidence": {
          "path": "learningFront/src/shared/api/auth-api.ts",
          "line": 46,
          "fragment": "api<ResetRequested>('/auth/password-reset/request"
        }
      },
      {
        "from": "/curator",
        "to": "/auth/password-reset/confirm",
        "evidence": {
          "path": "learningFront/src/shared/api/auth-api.ts",
          "line": 59,
          "fragment": "api<void>('/auth/password-reset/confirm"
        }
      },
      {
        "from": "/curator",
        "to": "/auth/me",
        "evidence": {
          "path": "learningFront/src/shared/api/auth-api.ts",
          "line": 73,
          "fragment": "api<AuthUser>('/auth/me"
        }
      },
      {
        "from": "/curator",
        "to": "/auth/me/profile",
        "evidence": {
          "path": "learningFront/src/shared/api/auth-api.ts",
          "line": 77,
          "fragment": "api<AuthUser>('/auth/me/profile"
        }
      },
      {
        "from": "/library",
        "to": "/graph/placement/{id}/chain-probe",
        "evidence": {
          "path": "learningFront/src/shared/api/prior-test-api.ts",
          "line": 53,
          "fragment": "api<ChainProbeResult>(`/graph/placement/${seg(domain)}/chain-probe"
        }
      },
      {
        "from": "/library",
        "to": "/graph/placement/{id}/chain-answer",
        "evidence": {
          "path": "learningFront/src/shared/api/prior-test-api.ts",
          "line": 62,
          "fragment": "api<ChainAnswerResult>(`/graph/placement/${seg(domain)}/chain-answer"
        }
      },
      {
        "from": "/library",
        "to": "/graph/placement/{id}/report",
        "evidence": {
          "path": "learningFront/src/shared/api/prior-test-api.ts",
          "line": 68,
          "fragment": "api<PriorReport>(`/graph/placement/${seg(domain)}/report"
        }
      },
      {
        "from": "/library",
        "to": "/evidence",
        "evidence": {
          "path": "learningFront/src/shared/api/evidence-api.ts",
          "line": 27,
          "fragment": "api<{ accepted: number }>('/evidence"
        }
      },
      {
        "from": "/library",
        "to": "/auth/me/lang",
        "evidence": {
          "path": "learningFront/src/shared/api/lang-api.ts",
          "line": 13,
          "fragment": "api<AuthUser>('/auth/me/lang"
        }
      },
      {
        "from": "/library",
        "to": "/graph/subjects",
        "evidence": {
          "path": "learningFront/src/shared/api/subjects-api.ts",
          "line": 14,
          "fragment": "api<UserSubject[]>('/graph/subjects"
        }
      },
      {
        "from": "/library",
        "to": "/graph/subjects/{id}",
        "evidence": {
          "path": "learningFront/src/shared/api/subjects-api.ts",
          "line": 20,
          "fragment": "api<UserSubject>(`/graph/subjects/${encodeURIComponent(id)}"
        }
      },
      {
        "from": "/library",
        "to": "/content/materials",
        "evidence": {
          "path": "learningFront/src/shared/api/materials-api.ts",
          "line": 44,
          "fragment": "api<MaterialSummary[]>('/content/materials"
        }
      },
      {
        "from": "/library",
        "to": "/content/materials/{id}",
        "evidence": {
          "path": "learningFront/src/shared/api/materials-api.ts",
          "line": 46,
          "fragment": "api<MaterialFull>(`/content/materials/${encodeURIComponent(id)}"
        }
      },
      {
        "from": "/library",
        "to": "/graph/sources",
        "evidence": {
          "path": "learningFront/src/shared/api/sources-api.ts",
          "line": 51,
          "fragment": "api<SourceItem[]>('/graph/sources"
        }
      },
      {
        "from": "/library",
        "to": "/graph/sources/{id}/progress",
        "evidence": {
          "path": "learningFront/src/shared/api/sources-api.ts",
          "line": 54,
          "fragment": "api<SourceProgress>(`/graph/sources/${encodeURIComponent(id)}/progress"
        }
      },
      {
        "from": "/library",
        "to": "/graph/sources/gaps/{id}/fill",
        "evidence": {
          "path": "learningFront/src/shared/api/sources-api.ts",
          "line": 92,
          "fragment": "api<{ results: GapFillResult[] }>(`/graph/sources/gaps/${encodeURIComponent(goal)}/fill"
        }
      },
      {
        "from": "/library",
        "to": "/graph/goal/clarify",
        "evidence": {
          "path": "learningFront/src/shared/api/goal-intake-api.ts",
          "line": 44,
          "fragment": "api<{ questions: GoalQuestion[] }>('/graph/goal/clarify"
        }
      },
      {
        "from": "/library",
        "to": "/graph/goal/summarize",
        "evidence": {
          "path": "learningFront/src/shared/api/goal-intake-api.ts",
          "line": 50,
          "fragment": "api<GoalSummary>('/graph/goal/summarize"
        }
      },
      {
        "from": "/library",
        "to": "/graph/goal/confirm",
        "evidence": {
          "path": "learningFront/src/shared/api/goal-intake-api.ts",
          "line": 57,
          "fragment": "api<GoalIntakeState>('/graph/goal/confirm"
        }
      },
      {
        "from": "/library",
        "to": "/graph/goal/intake/{id}",
        "evidence": {
          "path": "learningFront/src/shared/api/goal-intake-api.ts",
          "line": 63,
          "fragment": "api<GoalIntakeState>(`/graph/goal/intake/${seg(domain)}"
        }
      },
      {
        "from": "/library",
        "to": "/graph/goal/{id}/volume",
        "evidence": {
          "path": "learningFront/src/shared/api/goal-intake-api.ts",
          "line": 85,
          "fragment": "api<GoalVolume>(`/graph/goal/${seg(domain)}/volume"
        }
      },
      {
        "from": "/library",
        "to": "/graph/notifications",
        "evidence": {
          "path": "learningFront/src/shared/api/notifications-api.ts",
          "line": 22,
          "fragment": "api<CourseNotification[]>('/graph/notifications"
        }
      },
      {
        "from": "/library",
        "to": "/graph/notifications/read",
        "evidence": {
          "path": "learningFront/src/shared/api/notifications-api.ts",
          "line": 26,
          "fragment": "api<{ marked: number }>('/graph/notifications/read"
        }
      },
      {
        "from": "/library",
        "to": "/push",
        "evidence": {
          "path": "learningFront/src/shared/api/push-api.ts",
          "line": 11,
          "fragment": "api<PushState>('/push"
        }
      },
      {
        "from": "/library",
        "to": "/push/devices",
        "evidence": {
          "path": "learningFront/src/shared/api/push-api.ts",
          "line": 14,
          "fragment": "api<PushState>('/push/devices"
        }
      },
      {
        "from": "/library",
        "to": "/push/devices/remove",
        "evidence": {
          "path": "learningFront/src/shared/api/push-api.ts",
          "line": 17,
          "fragment": "api<{ removed: boolean }>('/push/devices/remove"
        }
      },
      {
        "from": "/library",
        "to": "/push/enabled",
        "evidence": {
          "path": "learningFront/src/shared/api/push-api.ts",
          "line": 23,
          "fragment": "api<PushState>('/push/enabled"
        }
      },
      {
        "from": "/library",
        "to": "/graph/profile/{id}",
        "evidence": {
          "path": "learningFront/src/shared/api/skill-profile-api.ts",
          "line": 93,
          "fragment": "api<ProfileState>(`/graph/profile/${seg(domain)}"
        }
      },
      {
        "from": "/library",
        "to": "/graph/profile/{id}/start",
        "evidence": {
          "path": "learningFront/src/shared/api/skill-profile-api.ts",
          "line": 100,
          "fragment": "api<ProfileState>(`/graph/profile/${seg(domain)}/start"
        }
      },
      {
        "from": "/library",
        "to": "/graph/profile/{id}/fill",
        "evidence": {
          "path": "learningFront/src/shared/api/skill-profile-api.ts",
          "line": 104,
          "fragment": "api<ProfileState>(`/graph/profile/${seg(domain)}/fill"
        }
      },
      {
        "from": "/library",
        "to": "/graph/profile/{id}/build",
        "evidence": {
          "path": "learningFront/src/shared/api/skill-profile-api.ts",
          "line": 113,
          "fragment": "api<ProfileState & { build: BuildReport }>(`/graph/profile/${seg(domain)}/build"
        }
      },
      {
        "from": "/library",
        "to": "/graph/profile/{id}/coverage",
        "evidence": {
          "path": "learningFront/src/shared/api/skill-profile-api.ts",
          "line": 118,
          "fragment": "api<CoverageReport>(`/graph/profile/${seg(domain)}/coverage"
        }
      },
      {
        "from": "/library",
        "to": "/graph/{id}",
        "evidence": {
          "path": "learningFront/src/shared/api/graph-api.ts",
          "line": 72,
          "fragment": "api<Graph>(`/graph/${seg(domain)}"
        }
      },
      {
        "from": "/library",
        "to": "/graph/nodes/{id}",
        "evidence": {
          "path": "learningFront/src/shared/api/graph-api.ts",
          "line": 75,
          "fragment": "api<GraphNode>(`/graph/nodes/${seg(id)}"
        }
      },
      {
        "from": "/library",
        "to": "/graph/canon/build",
        "evidence": {
          "path": "learningFront/src/shared/api/graph-api.ts",
          "line": 79,
          "fragment": "api<Graph>('/graph/canon/build"
        }
      },
      {
        "from": "/library",
        "to": "/graph/goal/split",
        "evidence": {
          "path": "learningFront/src/shared/api/graph-api.ts",
          "line": 88,
          "fragment": "api<GoalSplit>('/graph/goal/split"
        }
      },
      {
        "from": "/library",
        "to": "/graph/canon/recompute-centrality",
        "evidence": {
          "path": "learningFront/src/shared/api/graph-api.ts",
          "line": 101,
          "fragment": "api<CentralityRow[]>('/graph/canon/recompute-centrality"
        }
      },
      {
        "from": "/library",
        "to": "/graph/canon/nodes/{id}/approve",
        "evidence": {
          "path": "learningFront/src/shared/api/graph-api.ts",
          "line": 107,
          "fragment": "api(`/graph/canon/nodes/${seg(conceptId)}/approve"
        }
      },
      {
        "from": "/library",
        "to": "/graph/nodes/{id}/override",
        "evidence": {
          "path": "learningFront/src/shared/api/graph-api.ts",
          "line": 113,
          "fragment": "api(`/graph/nodes/${seg(baseConceptId)}/override"
        }
      },
      {
        "from": "/library",
        "to": "/graph/user-nodes/{id}",
        "evidence": {
          "path": "learningFront/src/shared/api/graph-api.ts",
          "line": 119,
          "fragment": "api(`/graph/user-nodes/${seg(userConceptId)}"
        }
      },
      {
        "from": "/library",
        "to": "/graph/expand",
        "evidence": {
          "path": "learningFront/src/shared/api/graph-api.ts",
          "line": 122,
          "fragment": "api<Graph>('/graph/expand"
        }
      },
      {
        "from": "/library",
        "to": "/graph/materials/{id}/propose",
        "evidence": {
          "path": "learningFront/src/shared/api/graph-api.ts",
          "line": 148,
          "fragment": "api<MaterialProposal>(`/graph/materials/${seg(materialId)}/propose"
        }
      },
      {
        "from": "/library",
        "to": "/graph/materials/{id}/accept",
        "evidence": {
          "path": "learningFront/src/shared/api/graph-api.ts",
          "line": 155,
          "fragment": "api<{ created: number; graph: Graph }>(`/graph/materials/${seg(materialId)}/accept"
        }
      },
      {
        "from": "/library",
        "to": "/graph/placement/{id}/probe",
        "evidence": {
          "path": "learningFront/src/shared/api/graph-api.ts",
          "line": 225,
          "fragment": "api<ProbeResult>(`/graph/placement/${seg(domain)}/probe"
        }
      },
      {
        "from": "/library",
        "to": "/graph/placement/answer",
        "evidence": {
          "path": "learningFront/src/shared/api/graph-api.ts",
          "line": 228,
          "fragment": "api<AnswerResult>('/graph/placement/answer"
        }
      },
      {
        "from": "/library",
        "to": "/graph/placement/{id}/map",
        "evidence": {
          "path": "learningFront/src/shared/api/graph-api.ts",
          "line": 234,
          "fragment": "api<MasteryMap>(`/graph/placement/${seg(domain)}/map"
        }
      },
      {
        "from": "/library",
        "to": "/graph/course/{id}",
        "evidence": {
          "path": "learningFront/src/shared/api/graph-api.ts",
          "line": 278,
          "fragment": "api<Course>(`/graph/course/${seg(domain)}"
        }
      },
      {
        "from": "/library",
        "to": "/graph/course/{id}/complete",
        "evidence": {
          "path": "learningFront/src/shared/api/graph-api.ts",
          "line": 286,
          "fragment": "api<Course>(`/graph/course/${seg(domain)}/complete"
        }
      },
      {
        "from": "/library",
        "to": "/graph/course/{id}/step/{id}/answer",
        "evidence": {
          "path": "learningFront/src/shared/api/graph-api.ts",
          "line": 324,
          "fragment": "api<StepResult>(`/graph/course/${seg(domain)}/step/${seg(conceptId)}/answer"
        }
      },
      {
        "from": "/library",
        "to": "/graph/nodes",
        "evidence": {
          "path": "learningFront/src/shared/api/graph-api.ts",
          "line": 337,
          "fragment": "api<{ userConceptId: string }>('/graph/nodes"
        }
      },
      {
        "from": "/library",
        "to": "/graph/user-edges",
        "evidence": {
          "path": "learningFront/src/shared/api/graph-api.ts",
          "line": 346,
          "fragment": "api<{ id: string }>('/graph/user-edges"
        }
      },
      {
        "from": "/library",
        "to": "/me/study-methods",
        "evidence": {
          "path": "learningFront/src/shared/api/methods-api.ts",
          "line": 21,
          "fragment": "api<StudyMethodChoice>('/me/study-methods"
        }
      },
      {
        "from": "/library",
        "to": "/graph/nodes/{id}/claims",
        "evidence": {
          "path": "learningFront/src/shared/api/claims-api.ts",
          "line": 33,
          "fragment": "api<NodeClaim[]>(`/graph/nodes/${seg(conceptId)}/claims"
        }
      },
      {
        "from": "/library",
        "to": "/graph/claims/{id}/report",
        "evidence": {
          "path": "learningFront/src/shared/api/claims-api.ts",
          "line": 36,
          "fragment": "api<{ ok: boolean }>(`/graph/claims/${seg(claimId)}/report"
        }
      },
      {
        "from": "/library",
        "to": "/graph/claims/problems",
        "evidence": {
          "path": "learningFront/src/shared/api/claims-api.ts",
          "line": 72,
          "fragment": "api<ClaimProblem[]>(`/graph/claims/problems"
        }
      },
      {
        "from": "/library",
        "to": "/graph/claims/reports",
        "evidence": {
          "path": "learningFront/src/shared/api/claims-api.ts",
          "line": 88,
          "fragment": "api<ClaimReports[]>('/graph/claims/reports"
        }
      },
      {
        "from": "/library",
        "to": "/graph/claims/rebuild",
        "evidence": {
          "path": "learningFront/src/shared/api/claims-api.ts",
          "line": 91,
          "fragment": "api<{ jobId: string }>(`/graph/claims/rebuild"
        }
      },
      {
        "from": "/library",
        "to": "/auth/register",
        "evidence": {
          "path": "learningFront/src/shared/api/auth-api.ts",
          "line": 20,
          "fragment": "api<TokenResponse>('/auth/register"
        }
      },
      {
        "from": "/library",
        "to": "/auth/login",
        "evidence": {
          "path": "learningFront/src/shared/api/auth-api.ts",
          "line": 30,
          "fragment": "api<TokenResponse>('/auth/login"
        }
      },
      {
        "from": "/library",
        "to": "/auth/password-reset/request",
        "evidence": {
          "path": "learningFront/src/shared/api/auth-api.ts",
          "line": 46,
          "fragment": "api<ResetRequested>('/auth/password-reset/request"
        }
      },
      {
        "from": "/library",
        "to": "/auth/password-reset/confirm",
        "evidence": {
          "path": "learningFront/src/shared/api/auth-api.ts",
          "line": 59,
          "fragment": "api<void>('/auth/password-reset/confirm"
        }
      },
      {
        "from": "/library",
        "to": "/auth/me",
        "evidence": {
          "path": "learningFront/src/shared/api/auth-api.ts",
          "line": 73,
          "fragment": "api<AuthUser>('/auth/me"
        }
      },
      {
        "from": "/library",
        "to": "/auth/me/profile",
        "evidence": {
          "path": "learningFront/src/shared/api/auth-api.ts",
          "line": 77,
          "fragment": "api<AuthUser>('/auth/me/profile"
        }
      },
      {
        "from": "/problems",
        "to": "/graph/placement/{id}/chain-probe",
        "evidence": {
          "path": "learningFront/src/shared/api/prior-test-api.ts",
          "line": 53,
          "fragment": "api<ChainProbeResult>(`/graph/placement/${seg(domain)}/chain-probe"
        }
      },
      {
        "from": "/problems",
        "to": "/graph/placement/{id}/chain-answer",
        "evidence": {
          "path": "learningFront/src/shared/api/prior-test-api.ts",
          "line": 62,
          "fragment": "api<ChainAnswerResult>(`/graph/placement/${seg(domain)}/chain-answer"
        }
      },
      {
        "from": "/problems",
        "to": "/graph/placement/{id}/report",
        "evidence": {
          "path": "learningFront/src/shared/api/prior-test-api.ts",
          "line": 68,
          "fragment": "api<PriorReport>(`/graph/placement/${seg(domain)}/report"
        }
      },
      {
        "from": "/problems",
        "to": "/evidence",
        "evidence": {
          "path": "learningFront/src/shared/api/evidence-api.ts",
          "line": 27,
          "fragment": "api<{ accepted: number }>('/evidence"
        }
      },
      {
        "from": "/problems",
        "to": "/auth/me/lang",
        "evidence": {
          "path": "learningFront/src/shared/api/lang-api.ts",
          "line": 13,
          "fragment": "api<AuthUser>('/auth/me/lang"
        }
      },
      {
        "from": "/problems",
        "to": "/graph/subjects",
        "evidence": {
          "path": "learningFront/src/shared/api/subjects-api.ts",
          "line": 14,
          "fragment": "api<UserSubject[]>('/graph/subjects"
        }
      },
      {
        "from": "/problems",
        "to": "/graph/subjects/{id}",
        "evidence": {
          "path": "learningFront/src/shared/api/subjects-api.ts",
          "line": 20,
          "fragment": "api<UserSubject>(`/graph/subjects/${encodeURIComponent(id)}"
        }
      },
      {
        "from": "/problems",
        "to": "/content/materials",
        "evidence": {
          "path": "learningFront/src/shared/api/materials-api.ts",
          "line": 44,
          "fragment": "api<MaterialSummary[]>('/content/materials"
        }
      },
      {
        "from": "/problems",
        "to": "/content/materials/{id}",
        "evidence": {
          "path": "learningFront/src/shared/api/materials-api.ts",
          "line": 46,
          "fragment": "api<MaterialFull>(`/content/materials/${encodeURIComponent(id)}"
        }
      },
      {
        "from": "/problems",
        "to": "/graph/sources",
        "evidence": {
          "path": "learningFront/src/shared/api/sources-api.ts",
          "line": 51,
          "fragment": "api<SourceItem[]>('/graph/sources"
        }
      },
      {
        "from": "/problems",
        "to": "/graph/sources/{id}/progress",
        "evidence": {
          "path": "learningFront/src/shared/api/sources-api.ts",
          "line": 54,
          "fragment": "api<SourceProgress>(`/graph/sources/${encodeURIComponent(id)}/progress"
        }
      },
      {
        "from": "/problems",
        "to": "/graph/sources/gaps/{id}/fill",
        "evidence": {
          "path": "learningFront/src/shared/api/sources-api.ts",
          "line": 92,
          "fragment": "api<{ results: GapFillResult[] }>(`/graph/sources/gaps/${encodeURIComponent(goal)}/fill"
        }
      },
      {
        "from": "/problems",
        "to": "/graph/goal/clarify",
        "evidence": {
          "path": "learningFront/src/shared/api/goal-intake-api.ts",
          "line": 44,
          "fragment": "api<{ questions: GoalQuestion[] }>('/graph/goal/clarify"
        }
      },
      {
        "from": "/problems",
        "to": "/graph/goal/summarize",
        "evidence": {
          "path": "learningFront/src/shared/api/goal-intake-api.ts",
          "line": 50,
          "fragment": "api<GoalSummary>('/graph/goal/summarize"
        }
      },
      {
        "from": "/problems",
        "to": "/graph/goal/confirm",
        "evidence": {
          "path": "learningFront/src/shared/api/goal-intake-api.ts",
          "line": 57,
          "fragment": "api<GoalIntakeState>('/graph/goal/confirm"
        }
      },
      {
        "from": "/problems",
        "to": "/graph/goal/intake/{id}",
        "evidence": {
          "path": "learningFront/src/shared/api/goal-intake-api.ts",
          "line": 63,
          "fragment": "api<GoalIntakeState>(`/graph/goal/intake/${seg(domain)}"
        }
      },
      {
        "from": "/problems",
        "to": "/graph/goal/{id}/volume",
        "evidence": {
          "path": "learningFront/src/shared/api/goal-intake-api.ts",
          "line": 85,
          "fragment": "api<GoalVolume>(`/graph/goal/${seg(domain)}/volume"
        }
      },
      {
        "from": "/problems",
        "to": "/graph/notifications",
        "evidence": {
          "path": "learningFront/src/shared/api/notifications-api.ts",
          "line": 22,
          "fragment": "api<CourseNotification[]>('/graph/notifications"
        }
      },
      {
        "from": "/problems",
        "to": "/graph/notifications/read",
        "evidence": {
          "path": "learningFront/src/shared/api/notifications-api.ts",
          "line": 26,
          "fragment": "api<{ marked: number }>('/graph/notifications/read"
        }
      },
      {
        "from": "/problems",
        "to": "/push",
        "evidence": {
          "path": "learningFront/src/shared/api/push-api.ts",
          "line": 11,
          "fragment": "api<PushState>('/push"
        }
      },
      {
        "from": "/problems",
        "to": "/push/devices",
        "evidence": {
          "path": "learningFront/src/shared/api/push-api.ts",
          "line": 14,
          "fragment": "api<PushState>('/push/devices"
        }
      },
      {
        "from": "/problems",
        "to": "/push/devices/remove",
        "evidence": {
          "path": "learningFront/src/shared/api/push-api.ts",
          "line": 17,
          "fragment": "api<{ removed: boolean }>('/push/devices/remove"
        }
      },
      {
        "from": "/problems",
        "to": "/push/enabled",
        "evidence": {
          "path": "learningFront/src/shared/api/push-api.ts",
          "line": 23,
          "fragment": "api<PushState>('/push/enabled"
        }
      },
      {
        "from": "/problems",
        "to": "/graph/profile/{id}",
        "evidence": {
          "path": "learningFront/src/shared/api/skill-profile-api.ts",
          "line": 93,
          "fragment": "api<ProfileState>(`/graph/profile/${seg(domain)}"
        }
      },
      {
        "from": "/problems",
        "to": "/graph/profile/{id}/start",
        "evidence": {
          "path": "learningFront/src/shared/api/skill-profile-api.ts",
          "line": 100,
          "fragment": "api<ProfileState>(`/graph/profile/${seg(domain)}/start"
        }
      },
      {
        "from": "/problems",
        "to": "/graph/profile/{id}/fill",
        "evidence": {
          "path": "learningFront/src/shared/api/skill-profile-api.ts",
          "line": 104,
          "fragment": "api<ProfileState>(`/graph/profile/${seg(domain)}/fill"
        }
      },
      {
        "from": "/problems",
        "to": "/graph/profile/{id}/build",
        "evidence": {
          "path": "learningFront/src/shared/api/skill-profile-api.ts",
          "line": 113,
          "fragment": "api<ProfileState & { build: BuildReport }>(`/graph/profile/${seg(domain)}/build"
        }
      },
      {
        "from": "/problems",
        "to": "/graph/profile/{id}/coverage",
        "evidence": {
          "path": "learningFront/src/shared/api/skill-profile-api.ts",
          "line": 118,
          "fragment": "api<CoverageReport>(`/graph/profile/${seg(domain)}/coverage"
        }
      },
      {
        "from": "/problems",
        "to": "/graph/{id}",
        "evidence": {
          "path": "learningFront/src/shared/api/graph-api.ts",
          "line": 72,
          "fragment": "api<Graph>(`/graph/${seg(domain)}"
        }
      },
      {
        "from": "/problems",
        "to": "/graph/nodes/{id}",
        "evidence": {
          "path": "learningFront/src/shared/api/graph-api.ts",
          "line": 75,
          "fragment": "api<GraphNode>(`/graph/nodes/${seg(id)}"
        }
      },
      {
        "from": "/problems",
        "to": "/graph/canon/build",
        "evidence": {
          "path": "learningFront/src/shared/api/graph-api.ts",
          "line": 79,
          "fragment": "api<Graph>('/graph/canon/build"
        }
      },
      {
        "from": "/problems",
        "to": "/graph/goal/split",
        "evidence": {
          "path": "learningFront/src/shared/api/graph-api.ts",
          "line": 88,
          "fragment": "api<GoalSplit>('/graph/goal/split"
        }
      },
      {
        "from": "/problems",
        "to": "/graph/canon/recompute-centrality",
        "evidence": {
          "path": "learningFront/src/shared/api/graph-api.ts",
          "line": 101,
          "fragment": "api<CentralityRow[]>('/graph/canon/recompute-centrality"
        }
      },
      {
        "from": "/problems",
        "to": "/graph/canon/nodes/{id}/approve",
        "evidence": {
          "path": "learningFront/src/shared/api/graph-api.ts",
          "line": 107,
          "fragment": "api(`/graph/canon/nodes/${seg(conceptId)}/approve"
        }
      },
      {
        "from": "/problems",
        "to": "/graph/nodes/{id}/override",
        "evidence": {
          "path": "learningFront/src/shared/api/graph-api.ts",
          "line": 113,
          "fragment": "api(`/graph/nodes/${seg(baseConceptId)}/override"
        }
      },
      {
        "from": "/problems",
        "to": "/graph/user-nodes/{id}",
        "evidence": {
          "path": "learningFront/src/shared/api/graph-api.ts",
          "line": 119,
          "fragment": "api(`/graph/user-nodes/${seg(userConceptId)}"
        }
      },
      {
        "from": "/problems",
        "to": "/graph/expand",
        "evidence": {
          "path": "learningFront/src/shared/api/graph-api.ts",
          "line": 122,
          "fragment": "api<Graph>('/graph/expand"
        }
      },
      {
        "from": "/problems",
        "to": "/graph/materials/{id}/propose",
        "evidence": {
          "path": "learningFront/src/shared/api/graph-api.ts",
          "line": 148,
          "fragment": "api<MaterialProposal>(`/graph/materials/${seg(materialId)}/propose"
        }
      },
      {
        "from": "/problems",
        "to": "/graph/materials/{id}/accept",
        "evidence": {
          "path": "learningFront/src/shared/api/graph-api.ts",
          "line": 155,
          "fragment": "api<{ created: number; graph: Graph }>(`/graph/materials/${seg(materialId)}/accept"
        }
      },
      {
        "from": "/problems",
        "to": "/graph/placement/{id}/probe",
        "evidence": {
          "path": "learningFront/src/shared/api/graph-api.ts",
          "line": 225,
          "fragment": "api<ProbeResult>(`/graph/placement/${seg(domain)}/probe"
        }
      },
      {
        "from": "/problems",
        "to": "/graph/placement/answer",
        "evidence": {
          "path": "learningFront/src/shared/api/graph-api.ts",
          "line": 228,
          "fragment": "api<AnswerResult>('/graph/placement/answer"
        }
      },
      {
        "from": "/problems",
        "to": "/graph/placement/{id}/map",
        "evidence": {
          "path": "learningFront/src/shared/api/graph-api.ts",
          "line": 234,
          "fragment": "api<MasteryMap>(`/graph/placement/${seg(domain)}/map"
        }
      },
      {
        "from": "/problems",
        "to": "/graph/course/{id}",
        "evidence": {
          "path": "learningFront/src/shared/api/graph-api.ts",
          "line": 278,
          "fragment": "api<Course>(`/graph/course/${seg(domain)}"
        }
      },
      {
        "from": "/problems",
        "to": "/graph/course/{id}/complete",
        "evidence": {
          "path": "learningFront/src/shared/api/graph-api.ts",
          "line": 286,
          "fragment": "api<Course>(`/graph/course/${seg(domain)}/complete"
        }
      },
      {
        "from": "/problems",
        "to": "/graph/course/{id}/step/{id}/answer",
        "evidence": {
          "path": "learningFront/src/shared/api/graph-api.ts",
          "line": 324,
          "fragment": "api<StepResult>(`/graph/course/${seg(domain)}/step/${seg(conceptId)}/answer"
        }
      },
      {
        "from": "/problems",
        "to": "/graph/nodes",
        "evidence": {
          "path": "learningFront/src/shared/api/graph-api.ts",
          "line": 337,
          "fragment": "api<{ userConceptId: string }>('/graph/nodes"
        }
      },
      {
        "from": "/problems",
        "to": "/graph/user-edges",
        "evidence": {
          "path": "learningFront/src/shared/api/graph-api.ts",
          "line": 346,
          "fragment": "api<{ id: string }>('/graph/user-edges"
        }
      },
      {
        "from": "/problems",
        "to": "/me/study-methods",
        "evidence": {
          "path": "learningFront/src/shared/api/methods-api.ts",
          "line": 21,
          "fragment": "api<StudyMethodChoice>('/me/study-methods"
        }
      },
      {
        "from": "/problems",
        "to": "/graph/nodes/{id}/claims",
        "evidence": {
          "path": "learningFront/src/shared/api/claims-api.ts",
          "line": 33,
          "fragment": "api<NodeClaim[]>(`/graph/nodes/${seg(conceptId)}/claims"
        }
      },
      {
        "from": "/problems",
        "to": "/graph/claims/{id}/report",
        "evidence": {
          "path": "learningFront/src/shared/api/claims-api.ts",
          "line": 36,
          "fragment": "api<{ ok: boolean }>(`/graph/claims/${seg(claimId)}/report"
        }
      },
      {
        "from": "/problems",
        "to": "/graph/claims/problems",
        "evidence": {
          "path": "learningFront/src/shared/api/claims-api.ts",
          "line": 72,
          "fragment": "api<ClaimProblem[]>(`/graph/claims/problems"
        }
      },
      {
        "from": "/problems",
        "to": "/graph/claims/reports",
        "evidence": {
          "path": "learningFront/src/shared/api/claims-api.ts",
          "line": 88,
          "fragment": "api<ClaimReports[]>('/graph/claims/reports"
        }
      },
      {
        "from": "/problems",
        "to": "/graph/claims/rebuild",
        "evidence": {
          "path": "learningFront/src/shared/api/claims-api.ts",
          "line": 91,
          "fragment": "api<{ jobId: string }>(`/graph/claims/rebuild"
        }
      },
      {
        "from": "/problems",
        "to": "/auth/register",
        "evidence": {
          "path": "learningFront/src/shared/api/auth-api.ts",
          "line": 20,
          "fragment": "api<TokenResponse>('/auth/register"
        }
      },
      {
        "from": "/problems",
        "to": "/auth/login",
        "evidence": {
          "path": "learningFront/src/shared/api/auth-api.ts",
          "line": 30,
          "fragment": "api<TokenResponse>('/auth/login"
        }
      },
      {
        "from": "/problems",
        "to": "/auth/password-reset/request",
        "evidence": {
          "path": "learningFront/src/shared/api/auth-api.ts",
          "line": 46,
          "fragment": "api<ResetRequested>('/auth/password-reset/request"
        }
      },
      {
        "from": "/problems",
        "to": "/auth/password-reset/confirm",
        "evidence": {
          "path": "learningFront/src/shared/api/auth-api.ts",
          "line": 59,
          "fragment": "api<void>('/auth/password-reset/confirm"
        }
      },
      {
        "from": "/problems",
        "to": "/auth/me",
        "evidence": {
          "path": "learningFront/src/shared/api/auth-api.ts",
          "line": 73,
          "fragment": "api<AuthUser>('/auth/me"
        }
      },
      {
        "from": "/problems",
        "to": "/auth/me/profile",
        "evidence": {
          "path": "learningFront/src/shared/api/auth-api.ts",
          "line": 77,
          "fragment": "api<AuthUser>('/auth/me/profile"
        }
      },
      {
        "from": "/sources",
        "to": "/graph/placement/{id}/chain-probe",
        "evidence": {
          "path": "learningFront/src/shared/api/prior-test-api.ts",
          "line": 53,
          "fragment": "api<ChainProbeResult>(`/graph/placement/${seg(domain)}/chain-probe"
        }
      },
      {
        "from": "/sources",
        "to": "/graph/placement/{id}/chain-answer",
        "evidence": {
          "path": "learningFront/src/shared/api/prior-test-api.ts",
          "line": 62,
          "fragment": "api<ChainAnswerResult>(`/graph/placement/${seg(domain)}/chain-answer"
        }
      },
      {
        "from": "/sources",
        "to": "/graph/placement/{id}/report",
        "evidence": {
          "path": "learningFront/src/shared/api/prior-test-api.ts",
          "line": 68,
          "fragment": "api<PriorReport>(`/graph/placement/${seg(domain)}/report"
        }
      },
      {
        "from": "/sources",
        "to": "/evidence",
        "evidence": {
          "path": "learningFront/src/shared/api/evidence-api.ts",
          "line": 27,
          "fragment": "api<{ accepted: number }>('/evidence"
        }
      },
      {
        "from": "/sources",
        "to": "/auth/me/lang",
        "evidence": {
          "path": "learningFront/src/shared/api/lang-api.ts",
          "line": 13,
          "fragment": "api<AuthUser>('/auth/me/lang"
        }
      },
      {
        "from": "/sources",
        "to": "/graph/subjects",
        "evidence": {
          "path": "learningFront/src/shared/api/subjects-api.ts",
          "line": 14,
          "fragment": "api<UserSubject[]>('/graph/subjects"
        }
      },
      {
        "from": "/sources",
        "to": "/graph/subjects/{id}",
        "evidence": {
          "path": "learningFront/src/shared/api/subjects-api.ts",
          "line": 20,
          "fragment": "api<UserSubject>(`/graph/subjects/${encodeURIComponent(id)}"
        }
      },
      {
        "from": "/sources",
        "to": "/content/materials",
        "evidence": {
          "path": "learningFront/src/shared/api/materials-api.ts",
          "line": 44,
          "fragment": "api<MaterialSummary[]>('/content/materials"
        }
      },
      {
        "from": "/sources",
        "to": "/content/materials/{id}",
        "evidence": {
          "path": "learningFront/src/shared/api/materials-api.ts",
          "line": 46,
          "fragment": "api<MaterialFull>(`/content/materials/${encodeURIComponent(id)}"
        }
      },
      {
        "from": "/sources",
        "to": "/graph/sources",
        "evidence": {
          "path": "learningFront/src/shared/api/sources-api.ts",
          "line": 51,
          "fragment": "api<SourceItem[]>('/graph/sources"
        }
      },
      {
        "from": "/sources",
        "to": "/graph/sources/{id}/progress",
        "evidence": {
          "path": "learningFront/src/shared/api/sources-api.ts",
          "line": 54,
          "fragment": "api<SourceProgress>(`/graph/sources/${encodeURIComponent(id)}/progress"
        }
      },
      {
        "from": "/sources",
        "to": "/graph/sources/gaps/{id}/fill",
        "evidence": {
          "path": "learningFront/src/shared/api/sources-api.ts",
          "line": 92,
          "fragment": "api<{ results: GapFillResult[] }>(`/graph/sources/gaps/${encodeURIComponent(goal)}/fill"
        }
      },
      {
        "from": "/sources",
        "to": "/graph/goal/clarify",
        "evidence": {
          "path": "learningFront/src/shared/api/goal-intake-api.ts",
          "line": 44,
          "fragment": "api<{ questions: GoalQuestion[] }>('/graph/goal/clarify"
        }
      },
      {
        "from": "/sources",
        "to": "/graph/goal/summarize",
        "evidence": {
          "path": "learningFront/src/shared/api/goal-intake-api.ts",
          "line": 50,
          "fragment": "api<GoalSummary>('/graph/goal/summarize"
        }
      },
      {
        "from": "/sources",
        "to": "/graph/goal/confirm",
        "evidence": {
          "path": "learningFront/src/shared/api/goal-intake-api.ts",
          "line": 57,
          "fragment": "api<GoalIntakeState>('/graph/goal/confirm"
        }
      },
      {
        "from": "/sources",
        "to": "/graph/goal/intake/{id}",
        "evidence": {
          "path": "learningFront/src/shared/api/goal-intake-api.ts",
          "line": 63,
          "fragment": "api<GoalIntakeState>(`/graph/goal/intake/${seg(domain)}"
        }
      },
      {
        "from": "/sources",
        "to": "/graph/goal/{id}/volume",
        "evidence": {
          "path": "learningFront/src/shared/api/goal-intake-api.ts",
          "line": 85,
          "fragment": "api<GoalVolume>(`/graph/goal/${seg(domain)}/volume"
        }
      },
      {
        "from": "/sources",
        "to": "/graph/notifications",
        "evidence": {
          "path": "learningFront/src/shared/api/notifications-api.ts",
          "line": 22,
          "fragment": "api<CourseNotification[]>('/graph/notifications"
        }
      },
      {
        "from": "/sources",
        "to": "/graph/notifications/read",
        "evidence": {
          "path": "learningFront/src/shared/api/notifications-api.ts",
          "line": 26,
          "fragment": "api<{ marked: number }>('/graph/notifications/read"
        }
      },
      {
        "from": "/sources",
        "to": "/push",
        "evidence": {
          "path": "learningFront/src/shared/api/push-api.ts",
          "line": 11,
          "fragment": "api<PushState>('/push"
        }
      },
      {
        "from": "/sources",
        "to": "/push/devices",
        "evidence": {
          "path": "learningFront/src/shared/api/push-api.ts",
          "line": 14,
          "fragment": "api<PushState>('/push/devices"
        }
      },
      {
        "from": "/sources",
        "to": "/push/devices/remove",
        "evidence": {
          "path": "learningFront/src/shared/api/push-api.ts",
          "line": 17,
          "fragment": "api<{ removed: boolean }>('/push/devices/remove"
        }
      },
      {
        "from": "/sources",
        "to": "/push/enabled",
        "evidence": {
          "path": "learningFront/src/shared/api/push-api.ts",
          "line": 23,
          "fragment": "api<PushState>('/push/enabled"
        }
      },
      {
        "from": "/sources",
        "to": "/graph/profile/{id}",
        "evidence": {
          "path": "learningFront/src/shared/api/skill-profile-api.ts",
          "line": 93,
          "fragment": "api<ProfileState>(`/graph/profile/${seg(domain)}"
        }
      },
      {
        "from": "/sources",
        "to": "/graph/profile/{id}/start",
        "evidence": {
          "path": "learningFront/src/shared/api/skill-profile-api.ts",
          "line": 100,
          "fragment": "api<ProfileState>(`/graph/profile/${seg(domain)}/start"
        }
      },
      {
        "from": "/sources",
        "to": "/graph/profile/{id}/fill",
        "evidence": {
          "path": "learningFront/src/shared/api/skill-profile-api.ts",
          "line": 104,
          "fragment": "api<ProfileState>(`/graph/profile/${seg(domain)}/fill"
        }
      },
      {
        "from": "/sources",
        "to": "/graph/profile/{id}/build",
        "evidence": {
          "path": "learningFront/src/shared/api/skill-profile-api.ts",
          "line": 113,
          "fragment": "api<ProfileState & { build: BuildReport }>(`/graph/profile/${seg(domain)}/build"
        }
      },
      {
        "from": "/sources",
        "to": "/graph/profile/{id}/coverage",
        "evidence": {
          "path": "learningFront/src/shared/api/skill-profile-api.ts",
          "line": 118,
          "fragment": "api<CoverageReport>(`/graph/profile/${seg(domain)}/coverage"
        }
      },
      {
        "from": "/sources",
        "to": "/graph/{id}",
        "evidence": {
          "path": "learningFront/src/shared/api/graph-api.ts",
          "line": 72,
          "fragment": "api<Graph>(`/graph/${seg(domain)}"
        }
      },
      {
        "from": "/sources",
        "to": "/graph/nodes/{id}",
        "evidence": {
          "path": "learningFront/src/shared/api/graph-api.ts",
          "line": 75,
          "fragment": "api<GraphNode>(`/graph/nodes/${seg(id)}"
        }
      },
      {
        "from": "/sources",
        "to": "/graph/canon/build",
        "evidence": {
          "path": "learningFront/src/shared/api/graph-api.ts",
          "line": 79,
          "fragment": "api<Graph>('/graph/canon/build"
        }
      },
      {
        "from": "/sources",
        "to": "/graph/goal/split",
        "evidence": {
          "path": "learningFront/src/shared/api/graph-api.ts",
          "line": 88,
          "fragment": "api<GoalSplit>('/graph/goal/split"
        }
      },
      {
        "from": "/sources",
        "to": "/graph/canon/recompute-centrality",
        "evidence": {
          "path": "learningFront/src/shared/api/graph-api.ts",
          "line": 101,
          "fragment": "api<CentralityRow[]>('/graph/canon/recompute-centrality"
        }
      },
      {
        "from": "/sources",
        "to": "/graph/canon/nodes/{id}/approve",
        "evidence": {
          "path": "learningFront/src/shared/api/graph-api.ts",
          "line": 107,
          "fragment": "api(`/graph/canon/nodes/${seg(conceptId)}/approve"
        }
      },
      {
        "from": "/sources",
        "to": "/graph/nodes/{id}/override",
        "evidence": {
          "path": "learningFront/src/shared/api/graph-api.ts",
          "line": 113,
          "fragment": "api(`/graph/nodes/${seg(baseConceptId)}/override"
        }
      },
      {
        "from": "/sources",
        "to": "/graph/user-nodes/{id}",
        "evidence": {
          "path": "learningFront/src/shared/api/graph-api.ts",
          "line": 119,
          "fragment": "api(`/graph/user-nodes/${seg(userConceptId)}"
        }
      },
      {
        "from": "/sources",
        "to": "/graph/expand",
        "evidence": {
          "path": "learningFront/src/shared/api/graph-api.ts",
          "line": 122,
          "fragment": "api<Graph>('/graph/expand"
        }
      },
      {
        "from": "/sources",
        "to": "/graph/materials/{id}/propose",
        "evidence": {
          "path": "learningFront/src/shared/api/graph-api.ts",
          "line": 148,
          "fragment": "api<MaterialProposal>(`/graph/materials/${seg(materialId)}/propose"
        }
      },
      {
        "from": "/sources",
        "to": "/graph/materials/{id}/accept",
        "evidence": {
          "path": "learningFront/src/shared/api/graph-api.ts",
          "line": 155,
          "fragment": "api<{ created: number; graph: Graph }>(`/graph/materials/${seg(materialId)}/accept"
        }
      },
      {
        "from": "/sources",
        "to": "/graph/placement/{id}/probe",
        "evidence": {
          "path": "learningFront/src/shared/api/graph-api.ts",
          "line": 225,
          "fragment": "api<ProbeResult>(`/graph/placement/${seg(domain)}/probe"
        }
      },
      {
        "from": "/sources",
        "to": "/graph/placement/answer",
        "evidence": {
          "path": "learningFront/src/shared/api/graph-api.ts",
          "line": 228,
          "fragment": "api<AnswerResult>('/graph/placement/answer"
        }
      },
      {
        "from": "/sources",
        "to": "/graph/placement/{id}/map",
        "evidence": {
          "path": "learningFront/src/shared/api/graph-api.ts",
          "line": 234,
          "fragment": "api<MasteryMap>(`/graph/placement/${seg(domain)}/map"
        }
      },
      {
        "from": "/sources",
        "to": "/graph/course/{id}",
        "evidence": {
          "path": "learningFront/src/shared/api/graph-api.ts",
          "line": 278,
          "fragment": "api<Course>(`/graph/course/${seg(domain)}"
        }
      },
      {
        "from": "/sources",
        "to": "/graph/course/{id}/complete",
        "evidence": {
          "path": "learningFront/src/shared/api/graph-api.ts",
          "line": 286,
          "fragment": "api<Course>(`/graph/course/${seg(domain)}/complete"
        }
      },
      {
        "from": "/sources",
        "to": "/graph/course/{id}/step/{id}/answer",
        "evidence": {
          "path": "learningFront/src/shared/api/graph-api.ts",
          "line": 324,
          "fragment": "api<StepResult>(`/graph/course/${seg(domain)}/step/${seg(conceptId)}/answer"
        }
      },
      {
        "from": "/sources",
        "to": "/graph/nodes",
        "evidence": {
          "path": "learningFront/src/shared/api/graph-api.ts",
          "line": 337,
          "fragment": "api<{ userConceptId: string }>('/graph/nodes"
        }
      },
      {
        "from": "/sources",
        "to": "/graph/user-edges",
        "evidence": {
          "path": "learningFront/src/shared/api/graph-api.ts",
          "line": 346,
          "fragment": "api<{ id: string }>('/graph/user-edges"
        }
      },
      {
        "from": "/sources",
        "to": "/me/study-methods",
        "evidence": {
          "path": "learningFront/src/shared/api/methods-api.ts",
          "line": 21,
          "fragment": "api<StudyMethodChoice>('/me/study-methods"
        }
      },
      {
        "from": "/sources",
        "to": "/graph/nodes/{id}/claims",
        "evidence": {
          "path": "learningFront/src/shared/api/claims-api.ts",
          "line": 33,
          "fragment": "api<NodeClaim[]>(`/graph/nodes/${seg(conceptId)}/claims"
        }
      },
      {
        "from": "/sources",
        "to": "/graph/claims/{id}/report",
        "evidence": {
          "path": "learningFront/src/shared/api/claims-api.ts",
          "line": 36,
          "fragment": "api<{ ok: boolean }>(`/graph/claims/${seg(claimId)}/report"
        }
      },
      {
        "from": "/sources",
        "to": "/graph/claims/problems",
        "evidence": {
          "path": "learningFront/src/shared/api/claims-api.ts",
          "line": 72,
          "fragment": "api<ClaimProblem[]>(`/graph/claims/problems"
        }
      },
      {
        "from": "/sources",
        "to": "/graph/claims/reports",
        "evidence": {
          "path": "learningFront/src/shared/api/claims-api.ts",
          "line": 88,
          "fragment": "api<ClaimReports[]>('/graph/claims/reports"
        }
      },
      {
        "from": "/sources",
        "to": "/graph/claims/rebuild",
        "evidence": {
          "path": "learningFront/src/shared/api/claims-api.ts",
          "line": 91,
          "fragment": "api<{ jobId: string }>(`/graph/claims/rebuild"
        }
      },
      {
        "from": "/sources",
        "to": "/auth/register",
        "evidence": {
          "path": "learningFront/src/shared/api/auth-api.ts",
          "line": 20,
          "fragment": "api<TokenResponse>('/auth/register"
        }
      },
      {
        "from": "/sources",
        "to": "/auth/login",
        "evidence": {
          "path": "learningFront/src/shared/api/auth-api.ts",
          "line": 30,
          "fragment": "api<TokenResponse>('/auth/login"
        }
      },
      {
        "from": "/sources",
        "to": "/auth/password-reset/request",
        "evidence": {
          "path": "learningFront/src/shared/api/auth-api.ts",
          "line": 46,
          "fragment": "api<ResetRequested>('/auth/password-reset/request"
        }
      },
      {
        "from": "/sources",
        "to": "/auth/password-reset/confirm",
        "evidence": {
          "path": "learningFront/src/shared/api/auth-api.ts",
          "line": 59,
          "fragment": "api<void>('/auth/password-reset/confirm"
        }
      },
      {
        "from": "/sources",
        "to": "/auth/me",
        "evidence": {
          "path": "learningFront/src/shared/api/auth-api.ts",
          "line": 73,
          "fragment": "api<AuthUser>('/auth/me"
        }
      },
      {
        "from": "/sources",
        "to": "/auth/me/profile",
        "evidence": {
          "path": "learningFront/src/shared/api/auth-api.ts",
          "line": 77,
          "fragment": "api<AuthUser>('/auth/me/profile"
        }
      }
    ]
  }
}
```

## Не в карте

```docdd-skipped
{
  "files": [
    {
      "path": "learningBack/.github/workflows/ci.yml",
      "why": "конфигурация CI, не модуль"
    },
    {
      "path": "learningBack/Dockerfile",
      "why": "рецепт сборки образа, не модуль"
    },
    {
      "path": "learningBack/Readme.md",
      "why": "документация, не код"
    },
    {
      "path": "learningBack/pyproject.toml",
      "why": "манифест зависимостей и настроек сборки, не модуль"
    },
    {
      "path": "learningBack/uv.lock",
      "why": "файл блокировки зависимостей, не модуль"
    }
  ]
}
```
