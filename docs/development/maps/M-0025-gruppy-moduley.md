---
id: M-0025
type: map
title: Группы модулей
status: approved
created: 2026-10-05
updated: 2026-10-05
---

# Группы модулей

Черновик: составлен моделью, не подтверждён. Прочитайте, поправьте руками
то, что модель не поняла, и подтвердите — до этого карта на общую картину
не влияет.

```docdd-codemap
{
  "added": {
    "groups": [
      {
        "id": "backend-foundation",
        "title": "Каркас backend",
        "summary": "Сборка FastAPI-приложения, настройки, подключение к БД, общие зависимости запроса, ORM-модели ядра и реестр подключаемых модулей — то, чем пользуются все остальные части backend.",
        "modules": [
          "learningBack/api/app.py",
          "learningBack/core/config.py",
          "learningBack/core/db.py",
          "learningBack/core/deps.py",
          "learningBack/core/models.py",
          "learningBack/core/admin.py",
          "learningBack/core/modules.py",
          "learningBack/core/schemas.py",
          "learningBack/migrations/env.py",
          "learningBack/migrations/versions/0001_init.py",
          "learningBack/migrations/versions/0005_superuser.py",
          "learningBack/scripts/createsuperuser.py",
          "learningBack/scripts/seed.py",
          "learningBack/tests/conftest.py",
          "learningBack/tests/test_modules.py",
          "learningBack/tests/test_config_secrets.py"
        ]
      },
      {
        "id": "auth",
        "title": "Аккаунт и вход",
        "summary": "Регистрация, вход, восстановление пароля по коду, JWT-сессия и состояние аутентификации на клиенте — всё, что отвечает на вопрос «кто сейчас работает».",
        "paths": [
          "learningFront/src/pages/auth",
          "learningFront/src/entities/session"
        ],
        "modules": [
          "learningBack/core/security.py",
          "learningBack/api/routers/auth.py",
          "learningBack/core/mail.py",
          "learningBack/core/ratelimit.py",
          "learningBack/migrations/versions/0002_auth.py",
          "learningBack/migrations/versions/0004_password_reset.py",
          "learningBack/migrations/versions/0013_auth_hardening.py",
          "learningBack/tests/test_auth.py",
          "learningBack/tests/test_mail.py",
          "learningFront/src/shared/api/auth-api.ts",
          "learningFront/src/shared/api/token.ts",
          "learningFront/src/shared/api/token.web.ts"
        ]
      },
      {
        "id": "llm-gateway",
        "title": "Шлюз к языковой модели",
        "summary": "Единая точка вызова LLM-провайдера с кэшем детерминированных ответов и учётом расхода токенов — графовые и языковые модули используют её, не зная деталей провайдера.",
        "paths": [
          "learningBack/core/ai_gateway"
        ],
        "modules": [
          "learningBack/core/llm_cache.py",
          "learningBack/core/usage.py",
          "learningBack/api/routers/usage.py",
          "learningBack/migrations/versions/0008_clear_vendor_model_pins.py",
          "learningBack/migrations/versions/0009_llm_usage.py",
          "learningBack/migrations/versions/0012_llm_cache.py",
          "learningBack/tests/test_llm_cache.py",
          "learningBack/tests/test_usage.py",
          "learningBack/tests/test_openai_gateway.py",
          "learningBack/tests/test_provider_errors.py"
        ]
      },
      {
        "id": "jobs-queue",
        "title": "Очередь отложенных AI-задач",
        "summary": "Обрабатывает тяжёлые AI-задачи (оценка, расшифровка, генерация) асинхронно — в запросе или фоновым воркером, с повтором при временных сбоях провайдера.",
        "modules": [
          "learningBack/core/jobs.py",
          "learningBack/api/routers/jobs.py",
          "learningBack/core/worker.py",
          "learningBack/scripts/worker.py",
          "learningBack/migrations/versions/0010_job_retry_after.py",
          "learningBack/tests/test_job_retry.py",
          "learningBack/tests/test_worker.py"
        ]
      },
      {
        "id": "offline-sync-engine",
        "title": "Локальный движок и синхронизация",
        "summary": "Офлайн-first ядро клиента: локальное хранилище активностей/ответов/карточек, планировщик FSRS и двухфазная push/pull синхронизация с backend-эндпоинтом sync.",
        "paths": [
          "learningFront/src/shared/engine/ports",
          "learningFront/src/shared/api/db"
        ],
        "modules": [
          "learningBack/api/routers/sync.py",
          "learningBack/core/srs.py",
          "learningBack/migrations/versions/0007_srs_concept_link.py",
          "learningBack/migrations/versions/0011_srs_card_updated_at.py",
          "learningBack/migrations/versions/0016_sync_cursor.py",
          "learningBack/tests/test_sync.py",
          "learningBack/tests/test_srs_merge.py",
          "learningFront/src/shared/engine/scheduler/scheduler.ts",
          "learningFront/src/shared/engine/scheduler/scheduler.test.ts",
          "learningFront/src/shared/api/auto-sync.ts",
          "learningFront/src/shared/api/auto-sync.test.ts",
          "learningFront/src/shared/api/current-user.ts",
          "learningFront/src/shared/api/job-queue.ts",
          "learningFront/src/shared/api/local-store.ts",
          "learningFront/src/shared/api/sync-client.ts",
          "learningFront/src/shared/api/sync-service.ts",
          "learningFront/src/shared/api/sync-service.test.ts",
          "learningFront/src/shared/api/grading.ts"
        ]
      },
      {
        "id": "knowledge-graph-core",
        "title": "Граф знаний (ядро)",
        "summary": "Канонический граф понятий и персональный слой поверх него (copy-on-write): теория узла, задания, байесовская освоенность, адаптивный плейсмент, курс как траектория и промоция личных узлов в канон.",
        "modules": [
          "learningBack/modules/knowledge/__init__.py",
          "learningBack/modules/knowledge/admin.py",
          "learningBack/modules/knowledge/ai.py",
          "learningBack/modules/knowledge/answer.py",
          "learningBack/modules/knowledge/assessment.py",
          "learningBack/modules/knowledge/assessment_store.py",
          "learningBack/modules/knowledge/centrality.py",
          "learningBack/modules/knowledge/content.py",
          "learningBack/modules/knowledge/course.py",
          "learningBack/modules/knowledge/cow.py",
          "learningBack/modules/knowledge/events.py",
          "learningBack/modules/knowledge/mastery.py",
          "learningBack/modules/knowledge/models.py",
          "learningBack/modules/knowledge/placement.py",
          "learningBack/modules/knowledge/promotion.py",
          "learningBack/modules/knowledge/router.py",
          "learningBack/modules/knowledge/schemas.py",
          "learningBack/modules/knowledge/study.py",
          "learningBack/modules/knowledge/api.py",
          "learningBack/migrations/versions/0003_knowledge_model.py",
          "learningBack/migrations/versions/0006_personal_domain.py",
          "learningBack/migrations/versions/0014_concept_key.py",
          "learningBack/migrations/versions/0015_user_concept_version.py",
          "learningBack/tests/test_assessment.py",
          "learningBack/tests/test_assessment_cache.py",
          "learningBack/tests/test_centrality.py",
          "learningBack/tests/test_content.py",
          "learningBack/tests/test_course.py",
          "learningBack/tests/test_cow.py",
          "learningBack/tests/test_graph_access.py",
          "learningBack/tests/test_graph_nodes.py",
          "learningBack/tests/test_mastery.py",
          "learningBack/tests/test_placement.py",
          "learningBack/tests/test_promotion.py",
          "learningBack/tests/test_study.py",
          "learningBack/tests/test_graph_interface.py",
          "learningBack/tests/test_graph_subject_agnostic.py",
          "learningBack/tests/test_graph_links_check.py",
          "learningBack/tests/test_language_course.py"
        ]
      },
      {
        "id": "knowledge-graph-frontend",
        "title": "Граф знаний (клиент)",
        "summary": "Экран карты знаний и курирование канона: чтение эффективного графа, теория и задание узла, правка summary, построение по теме.",
        "paths": [
          "learningFront/src/features/concept-study",
          "learningFront/src/pages/graph",
          "learningFront/src/entities/concept"
        ],
        "modules": [
          "learningFront/src/features/graph-editor/index.ts",
          "learningFront/src/features/graph-editor/ui/graph-curation.tsx",
          "learningFront/src/features/graph-editor/ui/graph-map.tsx",
          "learningFront/src/shared/api/graph-api.ts"
        ]
      },
      {
        "id": "language-track-core",
        "title": "Языковой трек (ядро модуля)",
        "summary": "Типы активностей IELTS/TOEFL, выбор рубрики письма по типу эссе и предмету, провижининг стартового набора (демо-эссе, офлайн reading-дрилл) и объяснение неверных вариантов дрилла.",
        "modules": [
          "learningBack/modules/languages/__init__.py",
          "learningBack/modules/languages/generators.py",
          "learningBack/modules/languages/rubrics.py",
          "learningBack/modules/languages/distractors.py",
          "learningBack/tests/test_toefl.py",
          "learningBack/tests/test_awl.py",
          "learningBack/tests/test_reading.py",
          "learningBack/tests/test_explain_distractors.py"
        ]
      },
      {
        "id": "ml-track-core",
        "title": "Трек программирования/ML (ядро модуля)",
        "summary": "Типы активностей и рубрики модуля ML: проверка понимания концепции и ревью кода, определение ML-предмета и минимальный генератор активностей из материала.",
        "paths": [
          "learningBack/modules/ml"
        ],
        "modules": [
          "learningBack/tests/test_code_review.py"
        ]
      },
      {
        "id": "ml-practice-frontend",
        "title": "Практика ML-трека (клиент)",
        "summary": "Рендереры активностей ML-трека: прочитать материал, вспомнить своими словами, решить задачу на код с автосохранением черновика и отправкой на ревью.",
        "paths": [
          "learningFront/src/features/code-task",
          "learningFront/src/features/concept-recall",
          "learningFront/src/features/material-read"
        ]
      },
      {
        "id": "activity-engine-frontend",
        "title": "Диспетчер активностей и реестр модулей (клиент)",
        "summary": "По типу активности находит и рендерит нужный компонент среди подключённых предметных модулей — ядро клиента не знает их имён; собирает манифесты модулей воедино.",
        "paths": [
          "learningFront/src/widgets",
          "learningFront/src/entities/module"
        ],
        "modules": [
          "learningFront/src/shared/lib/module-registry-context.tsx",
          "learningFront/src/shared/engine/index.ts",
          "learningFront/src/shared/engine/module/manifest.ts",
          "learningFront/src/shared/engine/module/registry.ts",
          "learningFront/src/shared/engine/module/registry.test.ts",
          "learningFront/src/shared/engine/types/activity.ts",
          "learningFront/src/shared/engine/types/grade.ts",
          "learningFront/src/shared/engine/types/response.ts"
        ]
      },
      {
        "id": "app-shell",
        "title": "Оформление и каркас приложения",
        "summary": "Единый стиль интерфейса (палитра, отступы, темы), базовые компоненты, сетевой клиент и сборка приложения (вкладки, провайдеры), на которые опираются все экраны.",
        "paths": [
          "learningFront/src/shared/ui",
          "learningFront/src/shared/config"
        ],
        "modules": [
          "learningFront/src/app/+html.tsx",
          "learningFront/src/app/_layout.tsx",
          "learningFront/src/app/(tabs)/_layout.tsx",
          "learningFront/src/shared/lib/connectivity.ts",
          "learningFront/src/shared/lib/id.ts",
          "learningFront/src/shared/lib/index.ts",
          "learningFront/src/shared/api/http.ts",
          "learningFront/src/shared/api/index.ts",
          "learningFront/src/shared/ui/theme-storage.ts",
          "learningFront/src/shared/ui/theme-storage.web.ts"
        ]
      },
      {
        "id": "learner-profile-frontend",
        "title": "Профиль и предмет изучения (клиент)",
        "summary": "Первый экран входа (предмет, целевая ступень) и экран профиля — аккаунт, предмет, оформление, синхронизация, выход.",
        "paths": [
          "learningFront/src/pages/onboarding",
          "learningFront/src/pages/profile"
        ],
        "modules": [
          "learningFront/src/app/(tabs)/profile.tsx"
        ]
      },
      {
        "id": "daily-loop-frontend",
        "title": "Ежедневный цикл (клиент)",
        "summary": "Экран «Сегодня» решает единственное следующее действие (шаг курса, повторение или определение уровня) и очередь повторения просроченных карточек.",
        "paths": [
          "learningFront/src/pages/home",
          "learningFront/src/pages/review"
        ]
      },
      {
        "id": "progress-tracking-frontend",
        "title": "Прогресс обучения (клиент)",
        "summary": "Офлайн-метрики (удержание, закрытие error-log, рост по рубрикам, серия дней) и экран прогресса, считающие их из локального event log и SRS-карточек.",
        "paths": [
          "learningFront/src/entities/progress",
          "learningFront/src/pages/progress"
        ]
      },
      {
        "id": "course-plan-frontend",
        "title": "План курса (клиент)",
        "summary": "Порядок изучения графа: текущий шаг курса с причиной (укоренение/вглубь/ветка/спираль) и экран, сводящий план с исполнением шага.",
        "paths": [
          "learningFront/src/features/course",
          "learningFront/src/pages/course"
        ]
      },
      {
        "id": "placement-session-frontend",
        "title": "Определение уровня (клиент)",
        "summary": "Выбор целевой ступени и сессия адаптивных зондов на границе знаний домена с финальной картой освоенности.",
        "paths": [
          "learningFront/src/features/placement",
          "learningFront/src/pages/placement"
        ]
      },
      {
        "id": "essay-writing-frontend",
        "title": "Эссе IELTS/TOEFL (клиент)",
        "summary": "Мгновенный офлайн-черновой сигнал по эссе, выбор рубрики оценки по типу письма и отправка на проверку с переходом в офлайн-очередь без сети.",
        "modules": [
          "learningFront/src/features/ielts-writing/index.ts",
          "learningFront/src/features/ielts-writing/lib/local-grader.ts",
          "learningFront/src/features/ielts-writing/lib/rubric.ts",
          "learningFront/src/features/ielts-writing/lib/rubric.test.ts",
          "learningFront/src/features/ielts-writing/ui/ielts-writing-activity.tsx"
        ]
      },
      {
        "id": "docdd-process-tooling",
        "title": "Инструменты DocDD",
        "summary": "Скрипты, которыми проверяется само ведение процесса: ссылки в документации, прогон проверок верификации, матрица трассируемости требований и живые прогоны против настоящего провайдера модели.",
        "modules": [
          "scripts/check-docs.py",
          "scripts/docdd-report.py",
          "scripts/gen-traceability.py",
          "scripts/check-invariants.sh",
          "scripts/live_checks.py"
        ]
      }
    ]
  }
}
```

## Журнал

- 2026-10-05 · заведена черновиком · модель
- 2026-10-05 · на подтверждение · architect
- 2026-10-05 · подтверждён · architect
