---
id: M-0054
type: map
title: 'Группировка кодовой базы по приложениям, фичи — срезом'
status: approved
created: 2026-10-20
updated: 2026-10-20
---

# Группировка кодовой базы по приложениям, фичи — срезом

Черновик: составлен моделью по запросу «Сгруппировать модули», не подтверждён.
Код не меняется — только дерево групп кодовой карты.

Выделены три приложения: **Сервер** (learningBack), **Клиент** (learningFront,
FSD) и **Инфраструктура** (выкладка, бэкапы, CI, проверки процесса). Второй
уровень — слои так, как их называет проект: у сервера `api`, `modules`, `core`,
миграции, служебные команды и тесты; у клиента `app`, `pages`, `widgets`,
`features`, `entities`, `shared`. Резать по смыслу пришлось в трёх местах:
`modules/knowledge` (шесть дел в одном каталоге — граф, области, цель и профиль,
освоенность, курс, конвейер источников), `core` (доступ, данные, шлюз к модели,
реестр модулей, задания) и плоский каталог тестов сервера — он разложен по тем
же частям, что и код. Фичи и страницы клиента сгруппированы, чтобы на уровне
было не больше девяти детей.

Фича — срез: нижние группы обеих сторон ссылаются на одну возможность
функциональной карты (`capability`), например «Источники и утверждения» на
сервере и «Граф и источники» в клиенте. Служебные группы (данные ядра, UI-кит)
остаются без возможности. Прежние 108 групп (домены M-0053 и группы-фичи
прошлых разбиений) объявлены пустыми: на экране не рисуются и модули поимённо
больше не перехватывают.

## Кодовая база

```docdd-codemap
{
  "added": {
    "groups": [
      {
        "id": "server",
        "title": "Сервер",
        "summary": "Бэкенд на FastAPI: API, предметные модули, ядро, схема базы и тесты — всё, что выкладывается как сервер."
      },
      {
        "id": "client",
        "title": "Клиент",
        "summary": "Приложение на Expo (iOS, Android, веб), собранное по FSD: то, с чем работает учащийся и куратор."
      },
      {
        "id": "infra",
        "title": "Инфраструктура",
        "summary": "Выкладка, резервные копии и проверки процесса — зона девопса; с сервером связана через общие ресурсы и связи, а не вложенностью."
      },
      {
        "id": "srv-api",
        "title": "HTTP API ядра",
        "summary": "Входные точки ядра: сборка приложения и роутеры аутентификации, синхронизации, материалов, методов, мониторинга и данных пользователя.",
        "parent": "server",
        "paths": [
          "learningBack/api"
        ]
      },
      {
        "id": "srv-modules",
        "title": "Предметные модули",
        "summary": "Независимые модули предметной области, подключаемые к ядру через контракт: граф знаний, языки, ML, способы запоминания.",
        "parent": "server"
      },
      {
        "id": "srv-core",
        "title": "Ядро",
        "summary": "Общие службы, о которых модули знают только через контракты: доступ, данные, шлюз к модели, задания и реестр модулей.",
        "parent": "server"
      },
      {
        "id": "srv-migrations",
        "title": "Схема базы данных",
        "summary": "Миграции Alembic: история таблиц ядра и модулей; меняются вместе с моделью данных.",
        "parent": "server",
        "paths": [
          "learningBack/migrations"
        ]
      },
      {
        "id": "srv-scripts",
        "title": "Служебные команды сервера",
        "summary": "Команды, которые запускают рядом с API: воркер очереди, наполнение демо-данными, суперпользователь, импорт и обновление знаний, очистка просроченного.",
        "parent": "server",
        "paths": [
          "learningBack/scripts"
        ]
      },
      {
        "id": "srv-tests",
        "title": "Тесты сервера",
        "summary": "Pytest-тесты бэкенда, разложенные по тем же частям, что и код.",
        "parent": "server"
      },
      {
        "id": "srv-knowledge",
        "title": "Граф знаний",
        "summary": "Модуль knowledge: граф понятий, цель и путь, освоенность, курс и конвейер знаний из источников.",
        "parent": "srv-modules"
      },
      {
        "id": "srv-kg-graph",
        "title": "Граф и курирование",
        "summary": "Канон и личный слой поверх него, узлы и связи, редактор и панель куратора, публичный интерфейс модуля для остальных.",
        "parent": "srv-knowledge",
        "paths": [
          "learningBack/modules/knowledge/__init__.py",
          "learningBack/modules/knowledge/api.py",
          "learningBack/modules/knowledge/models.py",
          "learningBack/modules/knowledge/schemas.py",
          "learningBack/modules/knowledge/cow.py",
          "learningBack/modules/knowledge/centrality.py",
          "learningBack/modules/knowledge/events.py",
          "learningBack/modules/knowledge/content.py",
          "learningBack/modules/knowledge/admin.py",
          "learningBack/modules/knowledge/graph_admin.py",
          "learningBack/modules/knowledge/graph_admin_data.py",
          "learningBack/modules/knowledge/router.py",
          "learningBack/modules/knowledge/promotion.py",
          "learningBack/modules/knowledge/stages.py",
          "learningBack/modules/knowledge/theory.py",
          "learningBack/modules/knowledge/ai.py",
          "learningBack/modules/knowledge/templates"
        ],
        "capability": "knowledge-graph"
      },
      {
        "id": "srv-kg-domains",
        "title": "Области и межобластные связи",
        "summary": "Реестр базовых областей, связи «нужно знать до» между областями и понятиями, принадлежность понятий областям.",
        "parent": "srv-knowledge",
        "paths": [
          "learningBack/modules/knowledge/domains.py",
          "learningBack/modules/knowledge/domains_api.py",
          "learningBack/modules/knowledge/cross_links.py",
          "learningBack/modules/knowledge/cross_links_api.py",
          "learningBack/modules/knowledge/areas.py"
        ],
        "capability": "domain-graph"
      },
      {
        "id": "srv-kg-goal",
        "title": "Цель и профиль навыка",
        "summary": "Диалог постановки цели, разбиение на субдомены, объём пути и профиль навыка с отчётом полноты.",
        "parent": "srv-knowledge",
        "paths": [
          "learningBack/modules/knowledge/goal_intake.py",
          "learningBack/modules/knowledge/subdomains.py",
          "learningBack/modules/knowledge/path_volume.py",
          "learningBack/modules/knowledge/skill_profile.py",
          "learningBack/modules/knowledge/profile_api.py",
          "learningBack/modules/knowledge/profile_build.py",
          "learningBack/modules/knowledge/profile_coverage.py",
          "learningBack/modules/knowledge/profile_fill.py",
          "learningBack/modules/knowledge/profile_match.py",
          "learningBack/modules/knowledge/profile_sources.py",
          "learningBack/modules/knowledge/profile_store.py",
          "learningBack/modules/knowledge/prior_report.py",
          "learningBack/modules/knowledge/subjects_api.py"
        ],
        "capability": "goal-intake"
      },
      {
        "id": "srv-kg-placement",
        "title": "Освоенность и определение уровня",
        "summary": "Байесовская оценка освоенности, зонды на границе знаний и проверка по цепочке базовых областей.",
        "parent": "srv-knowledge",
        "paths": [
          "learningBack/modules/knowledge/mastery.py",
          "learningBack/modules/knowledge/placement.py",
          "learningBack/modules/knowledge/chain_placement.py"
        ],
        "capability": "placement"
      },
      {
        "id": "srv-kg-course",
        "title": "Курс и задания",
        "summary": "Траектория курса, развёртывание шага в активности, генерация и кэш заданий, оценка ответа, сборка узла заранее.",
        "parent": "srv-knowledge",
        "paths": [
          "learningBack/modules/knowledge/course.py",
          "learningBack/modules/knowledge/study.py",
          "learningBack/modules/knowledge/assessment.py",
          "learningBack/modules/knowledge/assessment_store.py",
          "learningBack/modules/knowledge/answer.py",
          "learningBack/modules/knowledge/node_compile.py"
        ],
        "capability": "course-study"
      },
      {
        "id": "srv-kg-sources",
        "title": "Источники и утверждения",
        "summary": "Конвейер знаний: приём и поиск источников, воронка, утверждения с цитатами, сверка и пул проблем, слияние, свежесть, языки, материалы пользователя.",
        "parent": "srv-knowledge",
        "paths": [
          "learningBack/modules/knowledge/provenance.py",
          "learningBack/modules/knowledge/provenance_api.py",
          "learningBack/modules/knowledge/ingest.py",
          "learningBack/modules/knowledge/source_search.py",
          "learningBack/modules/knowledge/gap_search.py",
          "learningBack/modules/knowledge/funnel.py",
          "learningBack/modules/knowledge/claims_api.py",
          "learningBack/modules/knowledge/reconcile.py",
          "learningBack/modules/knowledge/merge.py",
          "learningBack/modules/knowledge/freshness.py",
          "learningBack/modules/knowledge/localize.py",
          "learningBack/modules/knowledge/langs.py",
          "learningBack/modules/knowledge/material_graph.py",
          "learningBack/modules/knowledge/review.py",
          "learningBack/modules/knowledge/review_api.py",
          "learningBack/modules/knowledge/notifications.py",
          "learningBack/modules/knowledge/notifications_api.py"
        ],
        "capability": "claim-graph"
      },
      {
        "id": "srv-languages",
        "title": "Языковой модуль",
        "summary": "IELTS/TOEFL: рубрики письма, AWL, аудирование с озвучкой, дистракторы, устный ответ.",
        "parent": "srv-modules",
        "paths": [
          "learningBack/modules/languages"
        ],
        "capability": "reception-drills"
      },
      {
        "id": "srv-ml",
        "title": "ML-модуль",
        "summary": "Задачи на код и рубрики ревью решения и понимания концепции.",
        "parent": "srv-modules",
        "paths": [
          "learningBack/modules/ml"
        ],
        "capability": "ml-track"
      },
      {
        "id": "srv-memorize",
        "title": "Способы запоминания",
        "summary": "Интервальное повторение и техника «первые буквы» как способы изучения по общему контракту.",
        "parent": "srv-modules",
        "paths": [
          "learningBack/modules/srs",
          "learningBack/modules/mnemonic"
        ],
        "capability": "memorize"
      },
      {
        "id": "srv-core-access",
        "title": "Доступ и аккаунт",
        "summary": "Пароли и токены, текущий пользователь, лимит запросов, письма, версия клиента, админ-панель.",
        "parent": "srv-core",
        "paths": [
          "learningBack/core/security.py",
          "learningBack/core/deps.py",
          "learningBack/core/ratelimit.py",
          "learningBack/core/mail.py",
          "learningBack/core/versioning.py",
          "learningBack/core/admin.py"
        ],
        "capability": "account-roles"
      },
      {
        "id": "srv-core-data",
        "title": "Данные и хранилища",
        "summary": "Настройки, подключение к базе, модели и схемы ядра, объектное хранилище, данные пользователя по разрешению.",
        "parent": "srv-core",
        "paths": [
          "learningBack/core/config.py",
          "learningBack/core/db.py",
          "learningBack/core/models.py",
          "learningBack/core/schemas.py",
          "learningBack/core/objects.py",
          "learningBack/core/userdata.py",
          "learningBack/core/__init__.py"
        ]
      },
      {
        "id": "srv-core-ai",
        "title": "Шлюз к модели и речь",
        "summary": "Единый шлюз к языковой модели с заглушкой, кэш и учёт токенов, эмбеддинги, расшифровка и озвучка.",
        "parent": "srv-core",
        "paths": [
          "learningBack/core/ai_base.py",
          "learningBack/core/ai_gateway.py",
          "learningBack/core/ai_mock.py",
          "learningBack/core/ai_openai.py",
          "learningBack/core/llm_cache.py",
          "learningBack/core/usage.py",
          "learningBack/core/embeddings.py",
          "learningBack/core/stt.py",
          "learningBack/core/tts.py"
        ],
        "capability": "ai-gateway"
      },
      {
        "id": "srv-core-modules",
        "title": "Реестр модулей и способы изучения",
        "summary": "Контракт подключаемого модуля, манифест, песочница, контракт способа изучения и свидетельство освоения, SRS-хелперы.",
        "parent": "srv-core",
        "paths": [
          "learningBack/core/modules.py",
          "learningBack/core/manifest.py",
          "learningBack/core/sandbox.py",
          "learningBack/core/methods.py",
          "learningBack/core/evidence.py",
          "learningBack/core/srs.py",
          "learningBack/core/materials.py"
        ],
        "capability": "extensions"
      },
      {
        "id": "srv-core-runtime",
        "title": "Задания, мониторинг и сообщения",
        "summary": "Обработка отложенных задач и воркер, сводка здоровья, пуши, тексты и коды ошибок сервера.",
        "parent": "srv-core",
        "paths": [
          "learningBack/core/jobs.py",
          "learningBack/core/worker.py",
          "learningBack/core/monitoring.py",
          "learningBack/core/push.py",
          "learningBack/core/messages.py",
          "learningBack/core/errors.py"
        ]
      },
      {
        "id": "srv-tests-sources",
        "title": "Тесты конвейера знаний",
        "summary": "Тесты конвейера знаний: проверяют одноимённую часть кода.",
        "parent": "srv-tests",
        "paths": [
          "learningBack/tests/test_gap_search.py",
          "learningBack/tests/test_graph_admin.py",
          "learningBack/tests/test_graph_extensions.py",
          "learningBack/tests/test_ingest.py",
          "learningBack/tests/test_material_nodes.py",
          "learningBack/tests/test_materials.py",
          "learningBack/tests/test_merge.py",
          "learningBack/tests/test_notifications.py",
          "learningBack/tests/test_notifications_review.py",
          "learningBack/tests/test_provenance.py",
          "learningBack/tests/test_review.py",
          "learningBack/tests/test_source_search.py",
          "learningBack/tests/test_source_upload.py",
          "learningBack/tests/test_sources_admin_only.py",
          "learningBack/tests/test_v0130_claims_extraction.py",
          "learningBack/tests/test_v0131_licenses_visibility.py",
          "learningBack/tests/test_v0132_concept_in_two_areas.py",
          "learningBack/tests/test_v0133_reconcile_pool.py",
          "learningBack/tests/test_v0134_node_compile_offline.py",
          "learningBack/tests/test_v0135_freshness.py",
          "learningBack/tests/test_v0136_consensus_fix.py",
          "learningBack/tests/test_v0137_funnel.py",
          "learningBack/tests/test_v0138_v0139_languages.py",
          "learningBack/tests/test_v0140_server_messages.py"
        ],
        "capability": "claim-graph"
      },
      {
        "id": "srv-tests-goal",
        "title": "Тесты цели и профиля",
        "summary": "Тесты цели и профиля: проверяют одноимённую часть кода.",
        "parent": "srv-tests",
        "paths": [
          "learningBack/tests/test_goal_intake.py",
          "learningBack/tests/test_path_volume.py",
          "learningBack/tests/test_prior_report.py",
          "learningBack/tests/test_profile_build.py",
          "learningBack/tests/test_profile_coverage.py",
          "learningBack/tests/test_profile_fill.py",
          "learningBack/tests/test_profile_match.py",
          "learningBack/tests/test_profile_sources.py",
          "learningBack/tests/test_profile_start.py",
          "learningBack/tests/test_skill_profile.py",
          "learningBack/tests/test_stage_level.py",
          "learningBack/tests/test_subdomains.py"
        ],
        "capability": "goal-intake"
      },
      {
        "id": "srv-tests-graph",
        "title": "Тесты графа и курса",
        "summary": "Тесты графа и курса: проверяют одноимённую часть кода.",
        "parent": "srv-tests",
        "paths": [
          "learningBack/tests/test_assessment.py",
          "learningBack/tests/test_assessment_cache.py",
          "learningBack/tests/test_centrality.py",
          "learningBack/tests/test_chain_placement.py",
          "learningBack/tests/test_content.py",
          "learningBack/tests/test_course.py",
          "learningBack/tests/test_cow.py",
          "learningBack/tests/test_cross_links.py",
          "learningBack/tests/test_domains.py",
          "learningBack/tests/test_graph_access.py",
          "learningBack/tests/test_graph_interface.py",
          "learningBack/tests/test_graph_links_check.py",
          "learningBack/tests/test_graph_nodes.py",
          "learningBack/tests/test_graph_subject_agnostic.py",
          "learningBack/tests/test_mastery.py",
          "learningBack/tests/test_placement.py",
          "learningBack/tests/test_promotion.py",
          "learningBack/tests/test_study.py"
        ],
        "capability": "knowledge-graph"
      },
      {
        "id": "srv-tests-tracks",
        "title": "Тесты языкового и ML-трека",
        "summary": "Тесты языкового и ML-трека: проверяют одноимённую часть кода.",
        "parent": "srv-tests",
        "paths": [
          "learningBack/tests/test_awl.py",
          "learningBack/tests/test_code_review.py",
          "learningBack/tests/test_explain_distractors.py",
          "learningBack/tests/test_language_course.py",
          "learningBack/tests/test_listening_materials.py",
          "learningBack/tests/test_memorization_module.py",
          "learningBack/tests/test_reading.py",
          "learningBack/tests/test_second_technique.py",
          "learningBack/tests/test_speaking.py",
          "learningBack/tests/test_srs_merge.py",
          "learningBack/tests/test_toefl.py"
        ]
      },
      {
        "id": "srv-tests-platform",
        "title": "Тесты ядра и платформы",
        "summary": "Доступ, синхронизация, задания, шлюз к модели, модули и изоляция, данные пользователя, миграции, хранилища; общие фикстуры.",
        "parent": "srv-tests",
        "paths": [
          "learningBack/tests/__init__.py",
          "learningBack/tests/conftest.py",
          "learningBack/tests/kg_helpers.py",
          "learningBack/tests/test_account_delete.py",
          "learningBack/tests/test_auth.py",
          "learningBack/tests/test_backup_objects.py",
          "learningBack/tests/test_config_secrets.py",
          "learningBack/tests/test_job_retry.py",
          "learningBack/tests/test_llm_cache.py",
          "learningBack/tests/test_mail.py",
          "learningBack/tests/test_migrations_match_models.py",
          "learningBack/tests/test_module_manifest.py",
          "learningBack/tests/test_modules.py",
          "learningBack/tests/test_monitoring.py",
          "learningBack/tests/test_objects.py",
          "learningBack/tests/test_openai_gateway.py",
          "learningBack/tests/test_plugin_isolation.py",
          "learningBack/tests/test_provider_errors.py",
          "learningBack/tests/test_push.py",
          "learningBack/tests/test_retention.py",
          "learningBack/tests/test_sync.py",
          "learningBack/tests/test_usage.py",
          "learningBack/tests/test_user_data_access.py",
          "learningBack/tests/test_versioning.py",
          "learningBack/tests/test_worker.py"
        ]
      },
      {
        "id": "cli-app",
        "title": "Маршруты (app)",
        "summary": "Экраны expo-router: корневой макет, вкладки и отдельные маршруты.",
        "parent": "client",
        "paths": [
          "learningFront/src/app"
        ]
      },
      {
        "id": "cli-pages",
        "title": "Страницы (pages)",
        "summary": "Экраны, которые собирают фичи и виджеты.",
        "parent": "client"
      },
      {
        "id": "cli-widgets",
        "title": "Виджеты (widgets)",
        "summary": "Навигация, панель предмета, диспетчер активностей и реестр модулей с рендерерами.",
        "parent": "client",
        "paths": [
          "learningFront/src/widgets"
        ],
        "capability": "activity-engine"
      },
      {
        "id": "cli-features",
        "title": "Фичи (features)",
        "summary": "Пользовательские сценарии: каждый слайс — одно действие.",
        "parent": "client"
      },
      {
        "id": "cli-entities",
        "title": "Сущности (entities)",
        "summary": "Сессия, прогресс, модули и понятия — общие модели клиента.",
        "parent": "client",
        "paths": [
          "learningFront/src/entities"
        ]
      },
      {
        "id": "cli-shared",
        "title": "Общее (shared)",
        "summary": "Код без предметной области: клиент API и синхронизация, движок активностей, UI-кит, переводы, конфигурация.",
        "parent": "client"
      },
      {
        "id": "cli-pages-study",
        "title": "Учёба",
        "summary": "«Сегодня», повторение, прогресс, курс и определение уровня.",
        "parent": "cli-pages",
        "paths": [
          "learningFront/src/pages/home",
          "learningFront/src/pages/review",
          "learningFront/src/pages/progress",
          "learningFront/src/pages/course",
          "learningFront/src/pages/placement"
        ],
        "capability": "course-study"
      },
      {
        "id": "cli-pages-knowledge",
        "title": "Знания и цель",
        "summary": "Граф, библиотека, материалы, профиль навыка и онбординг.",
        "parent": "cli-pages",
        "paths": [
          "learningFront/src/pages/graph",
          "learningFront/src/pages/library",
          "learningFront/src/pages/materials",
          "learningFront/src/pages/skill-profile",
          "learningFront/src/pages/onboarding"
        ],
        "capability": "knowledge-graph"
      },
      {
        "id": "cli-pages-account",
        "title": "Аккаунт",
        "summary": "Вход, восстановление пароля и профиль.",
        "parent": "cli-pages",
        "paths": [
          "learningFront/src/pages/auth",
          "learningFront/src/pages/profile"
        ],
        "capability": "account-roles"
      },
      {
        "id": "cli-pages-curator",
        "title": "Куратор",
        "summary": "Источники знаний и пул проблем.",
        "parent": "cli-pages",
        "paths": [
          "learningFront/src/pages/sources",
          "learningFront/src/pages/problems"
        ],
        "capability": "admin-curation"
      },
      {
        "id": "cli-feat-goal",
        "title": "Цель и путь",
        "summary": "Постановка цели, курс, определение уровня, входной тест, достижение цели.",
        "parent": "cli-features",
        "capability": "goal-intake"
      },
      {
        "id": "cli-f-goal-intake",
        "title": "goal-intake",
        "summary": "Слайс features/goal-intake.",
        "parent": "cli-feat-goal",
        "paths": [
          "learningFront/src/features/goal-intake"
        ],
        "capability": "goal-intake"
      },
      {
        "id": "cli-f-goal-reached",
        "title": "goal-reached",
        "summary": "Слайс features/goal-reached.",
        "parent": "cli-feat-goal",
        "paths": [
          "learningFront/src/features/goal-reached"
        ],
        "capability": "goal-intake"
      },
      {
        "id": "cli-f-course",
        "title": "course",
        "summary": "Слайс features/course.",
        "parent": "cli-feat-goal",
        "paths": [
          "learningFront/src/features/course"
        ],
        "capability": "goal-intake"
      },
      {
        "id": "cli-f-placement",
        "title": "placement",
        "summary": "Слайс features/placement.",
        "parent": "cli-feat-goal",
        "paths": [
          "learningFront/src/features/placement"
        ],
        "capability": "goal-intake"
      },
      {
        "id": "cli-f-prior-test",
        "title": "prior-test",
        "summary": "Слайс features/prior-test.",
        "parent": "cli-feat-goal",
        "paths": [
          "learningFront/src/features/prior-test"
        ],
        "capability": "goal-intake"
      },
      {
        "id": "cli-feat-knowledge",
        "title": "Граф и источники",
        "summary": "Редактор графа и карта пути, источники и пул проблем, профиль навыка.",
        "parent": "cli-features",
        "capability": "knowledge-graph"
      },
      {
        "id": "cli-f-graph-editor",
        "title": "graph-editor",
        "summary": "Слайс features/graph-editor.",
        "parent": "cli-feat-knowledge",
        "paths": [
          "learningFront/src/features/graph-editor"
        ],
        "capability": "knowledge-graph"
      },
      {
        "id": "cli-f-sources",
        "title": "sources",
        "summary": "Слайс features/sources.",
        "parent": "cli-feat-knowledge",
        "paths": [
          "learningFront/src/features/sources"
        ],
        "capability": "knowledge-graph"
      },
      {
        "id": "cli-f-claim-problems",
        "title": "claim-problems",
        "summary": "Слайс features/claim-problems.",
        "parent": "cli-feat-knowledge",
        "paths": [
          "learningFront/src/features/claim-problems"
        ],
        "capability": "knowledge-graph"
      },
      {
        "id": "cli-f-skill-profile",
        "title": "skill-profile",
        "summary": "Слайс features/skill-profile.",
        "parent": "cli-feat-knowledge",
        "paths": [
          "learningFront/src/features/skill-profile"
        ],
        "capability": "knowledge-graph"
      },
      {
        "id": "cli-feat-study",
        "title": "Изучение и запоминание",
        "summary": "Теория узла, вспоминание, чтение материала, выбор способа и техника «первые буквы».",
        "parent": "cli-features",
        "capability": "knowledge-use"
      },
      {
        "id": "cli-f-concept-study",
        "title": "concept-study",
        "summary": "Слайс features/concept-study.",
        "parent": "cli-feat-study",
        "paths": [
          "learningFront/src/features/concept-study"
        ],
        "capability": "knowledge-use"
      },
      {
        "id": "cli-f-concept-recall",
        "title": "concept-recall",
        "summary": "Слайс features/concept-recall.",
        "parent": "cli-feat-study",
        "paths": [
          "learningFront/src/features/concept-recall"
        ],
        "capability": "knowledge-use"
      },
      {
        "id": "cli-f-material-read",
        "title": "material-read",
        "summary": "Слайс features/material-read.",
        "parent": "cli-feat-study",
        "paths": [
          "learningFront/src/features/material-read"
        ],
        "capability": "knowledge-use"
      },
      {
        "id": "cli-f-study-method",
        "title": "study-method",
        "summary": "Слайс features/study-method.",
        "parent": "cli-feat-study",
        "paths": [
          "learningFront/src/features/study-method"
        ],
        "capability": "knowledge-use"
      },
      {
        "id": "cli-f-mnemonic-recall",
        "title": "mnemonic-recall",
        "summary": "Слайс features/mnemonic-recall.",
        "parent": "cli-feat-study",
        "paths": [
          "learningFront/src/features/mnemonic-recall"
        ],
        "capability": "knowledge-use"
      },
      {
        "id": "cli-feat-drills",
        "title": "Тренажёры",
        "summary": "Аудирование, чтение, письмо IELTS, устный ответ и задачи на код.",
        "parent": "cli-features",
        "capability": "check"
      },
      {
        "id": "cli-f-listening-drill",
        "title": "listening-drill",
        "summary": "Слайс features/listening-drill.",
        "parent": "cli-feat-drills",
        "paths": [
          "learningFront/src/features/listening-drill"
        ],
        "capability": "check"
      },
      {
        "id": "cli-f-reading-drill",
        "title": "reading-drill",
        "summary": "Слайс features/reading-drill.",
        "parent": "cli-feat-drills",
        "paths": [
          "learningFront/src/features/reading-drill"
        ],
        "capability": "check"
      },
      {
        "id": "cli-f-ielts-writing",
        "title": "ielts-writing",
        "summary": "Слайс features/ielts-writing.",
        "parent": "cli-feat-drills",
        "paths": [
          "learningFront/src/features/ielts-writing"
        ],
        "capability": "check"
      },
      {
        "id": "cli-f-speaking",
        "title": "speaking",
        "summary": "Слайс features/speaking.",
        "parent": "cli-feat-drills",
        "paths": [
          "learningFront/src/features/speaking"
        ],
        "capability": "check"
      },
      {
        "id": "cli-f-code-task",
        "title": "code-task",
        "summary": "Слайс features/code-task.",
        "parent": "cli-feat-drills",
        "paths": [
          "learningFront/src/features/code-task"
        ],
        "capability": "check"
      },
      {
        "id": "cli-feat-push",
        "title": "Уведомления",
        "summary": "Настройки пушей.",
        "parent": "cli-features",
        "paths": [
          "learningFront/src/features/push-settings"
        ]
      },
      {
        "id": "cli-shared-api",
        "title": "Клиент API и синхронизация",
        "summary": "Запросы к серверу, токен, локальная база, очередь и синхронизация, отчёты об ошибках.",
        "parent": "cli-shared",
        "capability": "sync-jobs"
      },
      {
        "id": "cli-api-http",
        "title": "HTTP и вход",
        "summary": "Обёртка над fetch, токен, вход и ошибки с кодом.",
        "parent": "cli-shared-api",
        "paths": [
          "learningFront/src/shared/api/app-version.ts",
          "learningFront/src/shared/api/auth-api.ts",
          "learningFront/src/shared/api/current-user.ts",
          "learningFront/src/shared/api/error-text.ts",
          "learningFront/src/shared/api/http.ts",
          "learningFront/src/shared/api/index.ts",
          "learningFront/src/shared/api/token.ts",
          "learningFront/src/shared/api/token.web.ts"
        ],
        "capability": "sign-in"
      },
      {
        "id": "cli-api-sync",
        "title": "Локальная база и синхронизация",
        "summary": "SQLite-хранилище, очередь задач, push/pull и офлайн-очереди ответов.",
        "parent": "cli-shared-api",
        "paths": [
          "learningFront/src/shared/api/auto-sync.test.ts",
          "learningFront/src/shared/api/auto-sync.ts",
          "learningFront/src/shared/api/evidence-api.test.ts",
          "learningFront/src/shared/api/evidence-api.ts",
          "learningFront/src/shared/api/grading.ts",
          "learningFront/src/shared/api/job-queue.ts",
          "learningFront/src/shared/api/local-store.ts",
          "learningFront/src/shared/api/sync-client.ts",
          "learningFront/src/shared/api/sync-service.test.ts",
          "learningFront/src/shared/api/sync-service.ts",
          "learningFront/src/shared/api/voice-outbox.test.ts",
          "learningFront/src/shared/api/voice-outbox.ts",
          "learningFront/src/shared/api/db"
        ],
        "capability": "sync-jobs"
      },
      {
        "id": "cli-api-ops",
        "title": "Версия, ошибки и уведомления",
        "summary": "Проверка версии клиента, отчёты об ошибках, пуши.",
        "parent": "cli-shared-api",
        "paths": [
          "learningFront/src/shared/api/client-outdated.test.ts",
          "learningFront/src/shared/api/client-outdated.ts",
          "learningFront/src/shared/api/error-reporter.test.ts",
          "learningFront/src/shared/api/error-reporter.ts",
          "learningFront/src/shared/api/notification-route.test.ts",
          "learningFront/src/shared/api/notification-route.ts",
          "learningFront/src/shared/api/notifications-api.ts",
          "learningFront/src/shared/api/push-api.ts",
          "learningFront/src/shared/api/push-device.ts",
          "learningFront/src/shared/api/push-device.web.ts"
        ],
        "capability": "platform-release"
      },
      {
        "id": "cli-api-clients",
        "title": "Клиенты разделов API",
        "summary": "Запросы к графу, цели, источникам, утверждениям, материалам, методам и языкам.",
        "parent": "cli-shared-api",
        "paths": [
          "learningFront/src/shared/api/claims-api.ts",
          "learningFront/src/shared/api/goal-intake-api.ts",
          "learningFront/src/shared/api/graph-api.ts",
          "learningFront/src/shared/api/lang-api.ts",
          "learningFront/src/shared/api/materials-api.test.ts",
          "learningFront/src/shared/api/materials-api.ts",
          "learningFront/src/shared/api/methods-api.ts",
          "learningFront/src/shared/api/prior-test-api.ts",
          "learningFront/src/shared/api/skill-profile-api.ts",
          "learningFront/src/shared/api/sources-api.ts",
          "learningFront/src/shared/api/subjects-api.ts"
        ]
      },
      {
        "id": "cli-shared-engine",
        "title": "Движок активностей",
        "summary": "Типы активности и оценки, реестр модулей, порты хранилища и синхронизации, планировщик FSRS.",
        "parent": "cli-shared",
        "paths": [
          "learningFront/src/shared/engine"
        ],
        "capability": "activity-engine"
      },
      {
        "id": "cli-shared-ui",
        "title": "UI-кит и оформление",
        "summary": "Базовые элементы, тема, токены оформления, утилиты сети и id.",
        "parent": "cli-shared",
        "paths": [
          "learningFront/src/shared/ui",
          "learningFront/src/shared/config",
          "learningFront/src/shared/lib",
          "learningFront/src/test-setup.ts"
        ]
      },
      {
        "id": "cli-shared-i18n",
        "title": "Переводы",
        "summary": "Словари ru/en и перевод без React (i18n-core), контекст языка для экранов (i18n).",
        "parent": "cli-shared",
        "paths": [
          "learningFront/src/shared/i18n",
          "learningFront/src/shared/i18n-core"
        ],
        "capability": "ui-i18n"
      },
      {
        "id": "inf-deploy",
        "title": "Выкладка и бэкапы",
        "summary": "Подготовка сервера, развёртывание, резервные копии базы и объектов, проверка восстановления.",
        "parent": "infra",
        "paths": [
          "scripts/bootstrap-server.sh",
          "scripts/deploy-remote.sh",
          "scripts/deploy-staging.sh",
          "scripts/backup-db.sh",
          "scripts/backup-offsite.sh",
          "scripts/restore-check.sh"
        ],
        "capability": "platform-release"
      },
      {
        "id": "inf-process",
        "title": "Проверки процесса",
        "summary": "Отчёт DocDD, ссылки в документации, трассируемость, инварианты, живые проверки на настоящей модели.",
        "parent": "infra",
        "paths": [
          "scripts/docdd-report.py",
          "scripts/check-docs.py",
          "scripts/gen-traceability.py",
          "scripts/check-invariants.sh",
          "scripts/live_checks.py"
        ]
      },
      {
        "id": "platform",
        "paths": [],
        "modules": []
      },
      {
        "id": "platform-server",
        "paths": [],
        "modules": []
      },
      {
        "id": "platform-client",
        "paths": [],
        "modules": []
      },
      {
        "id": "knowledge",
        "paths": [],
        "modules": []
      },
      {
        "id": "knowledge-server",
        "paths": [],
        "modules": []
      },
      {
        "id": "knowledge-client",
        "paths": [],
        "modules": []
      },
      {
        "id": "goal",
        "paths": [],
        "modules": []
      },
      {
        "id": "goal-server",
        "paths": [],
        "modules": []
      },
      {
        "id": "goal-client",
        "paths": [],
        "modules": []
      },
      {
        "id": "study",
        "paths": [],
        "modules": []
      },
      {
        "id": "study-server",
        "paths": [],
        "modules": []
      },
      {
        "id": "study-client",
        "paths": [],
        "modules": []
      },
      {
        "id": "language",
        "paths": [],
        "modules": []
      },
      {
        "id": "language-server",
        "paths": [],
        "modules": []
      },
      {
        "id": "language-client",
        "paths": [],
        "modules": []
      },
      {
        "id": "ml",
        "paths": [],
        "modules": []
      },
      {
        "id": "ml-server",
        "paths": [],
        "modules": []
      },
      {
        "id": "ml-client",
        "paths": [],
        "modules": []
      },
      {
        "id": "checks",
        "paths": [],
        "modules": []
      },
      {
        "id": "materials",
        "paths": [],
        "modules": []
      },
      {
        "id": "study-methods-contract",
        "paths": [],
        "modules": []
      },
      {
        "id": "mastery-evidence-dispatch",
        "paths": [],
        "modules": []
      },
      {
        "id": "module-lifecycle",
        "paths": [],
        "modules": []
      },
      {
        "id": "module-sandbox",
        "paths": [],
        "modules": []
      },
      {
        "id": "user-data-privacy",
        "paths": [],
        "modules": []
      },
      {
        "id": "platform-ops",
        "paths": [],
        "modules": []
      },
      {
        "id": "speech-to-text",
        "paths": [],
        "modules": []
      },
      {
        "id": "text-to-speech",
        "paths": [],
        "modules": []
      },
      {
        "id": "domain-graph-structure",
        "paths": [],
        "modules": []
      },
      {
        "id": "cross-domain-prereqs",
        "paths": [],
        "modules": []
      },
      {
        "id": "chain-placement",
        "paths": [],
        "modules": []
      },
      {
        "id": "goal-intake-dialog-impl",
        "paths": [],
        "modules": []
      },
      {
        "id": "goal-subdomain-split-impl",
        "paths": [],
        "modules": []
      },
      {
        "id": "goal-tree-assembly-impl",
        "paths": [],
        "modules": []
      },
      {
        "id": "path-volume-preview-impl",
        "paths": [],
        "modules": []
      },
      {
        "id": "memorize-techniques-impl",
        "paths": [],
        "modules": []
      },
      {
        "id": "listening-materials-impl",
        "paths": [],
        "modules": []
      },
      {
        "id": "speaking-flow-impl",
        "paths": [],
        "modules": []
      },
      {
        "id": "goal-intake-dialog-frontend",
        "paths": [],
        "modules": []
      },
      {
        "id": "goal-confirm-gate-frontend",
        "paths": [],
        "modules": []
      },
      {
        "id": "goal-subdomain-split-frontend",
        "paths": [],
        "modules": []
      },
      {
        "id": "goal-tree-assembly-frontend",
        "paths": [],
        "modules": []
      },
      {
        "id": "memorize-techniques-frontend",
        "paths": [],
        "modules": []
      },
      {
        "id": "reception-drills-listening-frontend",
        "paths": [],
        "modules": []
      },
      {
        "id": "writing-ielts-task-data-frontend",
        "paths": [],
        "modules": []
      },
      {
        "id": "reading-drill-frontend",
        "paths": [],
        "modules": []
      },
      {
        "id": "quiz-engine-frontend",
        "paths": [],
        "modules": []
      },
      {
        "id": "speaking-response-frontend",
        "paths": [],
        "modules": []
      },
      {
        "id": "study-method-switch-frontend",
        "paths": [],
        "modules": []
      },
      {
        "id": "mnemonic-activity-frontend",
        "paths": [],
        "modules": []
      },
      {
        "id": "mastery-evidence-frontend",
        "paths": [],
        "modules": []
      },
      {
        "id": "goal-intake-api-frontend",
        "paths": [],
        "modules": []
      },
      {
        "id": "platform-release-ops",
        "paths": [],
        "modules": []
      },
      {
        "id": "client-version-gate-frontend",
        "paths": [],
        "modules": []
      },
      {
        "id": "client-error-reports-frontend",
        "paths": [],
        "modules": []
      },
      {
        "id": "module-contract-check-frontend",
        "paths": [],
        "modules": []
      },
      {
        "id": "srs-card-merge-frontend",
        "paths": [],
        "modules": []
      },
      {
        "id": "backend-foundation",
        "paths": [],
        "modules": []
      },
      {
        "id": "auth",
        "paths": [],
        "modules": []
      },
      {
        "id": "llm-gateway",
        "paths": [],
        "modules": []
      },
      {
        "id": "jobs-queue",
        "paths": [],
        "modules": []
      },
      {
        "id": "offline-sync-engine",
        "paths": [],
        "modules": []
      },
      {
        "id": "knowledge-graph-core",
        "paths": [],
        "modules": []
      },
      {
        "id": "knowledge-graph-frontend",
        "paths": [],
        "modules": []
      },
      {
        "id": "language-track-core",
        "paths": [],
        "modules": []
      },
      {
        "id": "ml-track-core",
        "paths": [],
        "modules": []
      },
      {
        "id": "ml-practice-frontend",
        "paths": [],
        "modules": []
      },
      {
        "id": "activity-engine-frontend",
        "paths": [],
        "modules": []
      },
      {
        "id": "app-shell",
        "paths": [],
        "modules": []
      },
      {
        "id": "learner-profile-frontend",
        "paths": [],
        "modules": []
      },
      {
        "id": "daily-loop-frontend",
        "paths": [],
        "modules": []
      },
      {
        "id": "progress-tracking-frontend",
        "paths": [],
        "modules": []
      },
      {
        "id": "course-plan-frontend",
        "paths": [],
        "modules": []
      },
      {
        "id": "placement-session-frontend",
        "paths": [],
        "modules": []
      },
      {
        "id": "essay-writing-frontend",
        "paths": [],
        "modules": []
      },
      {
        "id": "docdd-process-tooling",
        "paths": [],
        "modules": []
      },
      {
        "id": "server-api-routes",
        "paths": [],
        "modules": []
      },
      {
        "id": "server-core",
        "paths": [],
        "modules": []
      },
      {
        "id": "server-migrations",
        "paths": [],
        "modules": []
      },
      {
        "id": "server-scripts",
        "paths": [],
        "modules": []
      },
      {
        "id": "ops-scripts",
        "paths": [],
        "modules": []
      },
      {
        "id": "knowledge-module",
        "paths": [],
        "modules": []
      },
      {
        "id": "languages-module",
        "paths": [],
        "modules": []
      },
      {
        "id": "ml-module",
        "paths": [],
        "modules": []
      },
      {
        "id": "study-modules",
        "paths": [],
        "modules": []
      },
      {
        "id": "client-routes",
        "paths": [],
        "modules": []
      },
      {
        "id": "client-shared-api",
        "paths": [],
        "modules": []
      },
      {
        "id": "client-shared-ui",
        "paths": [],
        "modules": []
      },
      {
        "id": "client-engine",
        "paths": [],
        "modules": []
      },
      {
        "id": "client-widgets",
        "paths": [],
        "modules": []
      },
      {
        "id": "client-entities",
        "paths": [],
        "modules": []
      },
      {
        "id": "client-knowledge",
        "paths": [],
        "modules": []
      },
      {
        "id": "client-goal",
        "paths": [],
        "modules": []
      },
      {
        "id": "client-study",
        "paths": [],
        "modules": []
      },
      {
        "id": "client-language",
        "paths": [],
        "modules": []
      },
      {
        "id": "client-ml",
        "paths": [],
        "modules": []
      },
      {
        "id": "client-account",
        "paths": [],
        "modules": []
      },
      {
        "id": "checks-server",
        "paths": [],
        "modules": []
      },
      {
        "id": "checks-client",
        "paths": [],
        "modules": []
      },
      {
        "id": "tests-validation",
        "paths": [],
        "modules": []
      },
      {
        "id": "tests-knowledge",
        "paths": [],
        "modules": []
      },
      {
        "id": "tests-profile",
        "paths": [],
        "modules": []
      },
      {
        "id": "tests-platform",
        "paths": [],
        "modules": []
      },
      {
        "id": "tests-client-entities",
        "paths": [],
        "modules": []
      },
      {
        "id": "tests-client-features",
        "paths": [],
        "modules": []
      },
      {
        "id": "tests-client-pages",
        "paths": [],
        "modules": []
      },
      {
        "id": "tests-client-shared",
        "paths": [],
        "modules": []
      },
      {
        "id": "tests-client-widgets",
        "paths": [],
        "modules": []
      }
    ]
  }
}
```

## Журнал

- 2026-10-20 · на подтверждение · architect
- 2026-10-20 · подтверждён · architect
