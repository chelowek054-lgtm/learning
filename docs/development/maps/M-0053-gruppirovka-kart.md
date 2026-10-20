---
id: M-0053
type: map
title: 'Группировка карт: домены, стороны и темы'
status: approved
created: 2026-10-20
updated: 2026-10-20
---

# Группировка карт: домены, стороны и темы

Черновик: составлен моделью, не подтверждён. Код не меняется — меняется только
то, как карты сложены в дерево (ADR-0027, «Бесконечная вложенность»).

- **Кодовая база.** Три уровня групп над модулями: домен (платформа, граф
  знаний, цель и путь, учебные активности, языковой трек, ML-трек, проверки) →
  сторона (сервер / клиент; у проверок — сервер / клиент) → прежние группы и
  тематические остатки каталогов. Прежние 57 групп объявлены заново с теми же
  полями и родителем; модули, которых не забирала ни одна группа, ложатся в
  остатки по каталогу, так что автоматических групп не остаётся.
- **Потоки данных.** Группы модулей берутся из кодовой карты; источники сложены
  в дерево: где лежат (сервер / устройство / внешние сервисы) → вид → источник.
- **Функциональная карта.** Над 11 корнями — четыре области: знания, учёба,
  человек и сообщество, сопровождение. Прочие поля возможностей повторены как
  есть: меняется только родитель.
- **Пользовательские пути** не трогаются: дерево там форматом не предусмотрено.

## Кодовая база

```docdd-codemap
{
  "added": {
    "groups": [
      {
        "id": "platform",
        "title": "Платформа",
        "summary": "Общее основание: доступ, данные, модель, очереди, выпуск и оболочка приложения."
      },
      {
        "id": "platform-server",
        "title": "Платформа: сервер",
        "summary": "Сервер — часть домена «Платформа».",
        "parent": "platform"
      },
      {
        "id": "platform-client",
        "title": "Платформа: клиент",
        "summary": "Клиент — часть домена «Платформа».",
        "parent": "platform"
      },
      {
        "id": "knowledge",
        "title": "Граф знаний",
        "summary": "Понятия, связи, утверждения с источниками и материалы, из которых строится граф."
      },
      {
        "id": "knowledge-server",
        "title": "Граф знаний: сервер",
        "summary": "Сервер — часть домена «Граф знаний».",
        "parent": "knowledge"
      },
      {
        "id": "knowledge-client",
        "title": "Граф знаний: клиент",
        "summary": "Клиент — часть домена «Граф знаний».",
        "parent": "knowledge"
      },
      {
        "id": "goal",
        "title": "Цель и путь",
        "summary": "Разбор цели человека, дерево цели, входная проверка и план курса."
      },
      {
        "id": "goal-server",
        "title": "Цель и путь: сервер",
        "summary": "Сервер — часть домена «Цель и путь».",
        "parent": "goal"
      },
      {
        "id": "goal-client",
        "title": "Цель и путь: клиент",
        "summary": "Клиент — часть домена «Цель и путь».",
        "parent": "goal"
      },
      {
        "id": "study",
        "title": "Учебные активности",
        "summary": "Движок активностей, повторение, свидетельства освоения, методы и ежедневный цикл."
      },
      {
        "id": "study-server",
        "title": "Учебные активности: сервер",
        "summary": "Сервер — часть домена «Учебные активности».",
        "parent": "study"
      },
      {
        "id": "study-client",
        "title": "Учебные активности: клиент",
        "summary": "Клиент — часть домена «Учебные активности».",
        "parent": "study"
      },
      {
        "id": "language",
        "title": "Языковой трек",
        "summary": "Аудирование, говорение, чтение, письмо и речь — всё про изучение языка."
      },
      {
        "id": "language-server",
        "title": "Языковой трек: сервер",
        "summary": "Сервер — часть домена «Языковой трек».",
        "parent": "language"
      },
      {
        "id": "language-client",
        "title": "Языковой трек: клиент",
        "summary": "Клиент — часть домена «Языковой трек».",
        "parent": "language"
      },
      {
        "id": "ml",
        "title": "ML-трек",
        "summary": "Практика по машинному обучению: задания с кодом и их проверка."
      },
      {
        "id": "ml-server",
        "title": "ML-трек: сервер",
        "summary": "Сервер — часть домена «ML-трек».",
        "parent": "ml"
      },
      {
        "id": "ml-client",
        "title": "ML-трек: клиент",
        "summary": "Клиент — часть домена «ML-трек».",
        "parent": "ml"
      },
      {
        "id": "checks",
        "title": "Проверки",
        "summary": "Автоматические тесты сервера и клиента."
      },
      {
        "id": "materials",
        "title": "Материалы пользователя",
        "summary": "Загрузка PDF/Markdown с разбиением на фрагменты, офлайн-чтение, и построение по материалу личных узлов графа и вопросов на вспоминание — с обязательной ссылкой на реальный фрагмент текста.",
        "paths": [
          "learningBack/core/materials.py",
          "learningBack/modules/knowledge/material_graph.py",
          "learningFront/src/app/materials.tsx",
          "learningFront/src/pages/materials",
          "learningFront/src/shared/api/materials-api.ts",
          "learningFront/src/shared/api/materials-api.test.ts"
        ],
        "parent": "knowledge-server"
      },
      {
        "id": "study-methods-contract",
        "title": "Контракт способа изучения",
        "summary": "Общий способ, которым модуль объявляет способ изучения шага курса и отдаёт его через API выбора и смены.",
        "modules": [
          "learningBack/core/methods.py",
          "learningBack/api/routers/methods.py"
        ],
        "capability": "method-contract",
        "parent": "study-server"
      },
      {
        "id": "mastery-evidence-dispatch",
        "title": "Свидетельство об освоении",
        "summary": "Единый формат результата ответа, не зависящий от способа запоминания, и его доставка модулям графа.",
        "modules": [
          "learningBack/core/evidence.py"
        ],
        "capability": "mastery-evidence",
        "parent": "study-server"
      },
      {
        "id": "module-lifecycle",
        "title": "Жизненный цикл и манифест модуля",
        "summary": "Контракт манифеста и администраторские действия над подключённым модулем: включить, согласиться на расширение, отключить, удалить данные.",
        "modules": [
          "learningBack/core/manifest.py",
          "learningBack/api/routers/modules_admin.py"
        ],
        "capability": "module-registry",
        "parent": "platform-server"
      },
      {
        "id": "module-sandbox",
        "title": "Изоляция исполнения модуля",
        "summary": "Единственный путь модуля к данным и сети с лимитами по времени, частоте и сбоям.",
        "modules": [
          "learningBack/core/sandbox.py"
        ],
        "capability": "isolation",
        "parent": "platform-server"
      },
      {
        "id": "user-data-privacy",
        "title": "«Мои данные»: доступ, выгрузка, удаление",
        "summary": "Реестр типов данных человека с разрешениями модулям, журналом доступа, выгрузкой, удалением по типу, по сроку хранения и удалением аккаунта.",
        "modules": [
          "learningBack/core/userdata.py",
          "learningBack/api/routers/userdata.py"
        ],
        "capability": "my-data",
        "parent": "platform-server"
      },
      {
        "id": "platform-ops",
        "title": "Платформа: мониторинг, версия, воркер, почта",
        "summary": "Эксплуатационные механизмы: сводка здоровья и ошибки клиента, совместимость версии клиента, фоновый воркер AI-задач, отправка писем восстановления пароля.",
        "modules": [
          "learningBack/core/monitoring.py",
          "learningBack/api/routers/monitoring.py",
          "learningBack/core/versioning.py",
          "learningBack/core/worker.py",
          "learningBack/core/mail.py"
        ],
        "capability": "platform-release",
        "parent": "platform-server"
      },
      {
        "id": "speech-to-text",
        "title": "Расшифровка устного ответа",
        "summary": "Порт распознавания речи для оценки устного ответа по таймингам слов.",
        "modules": [
          "learningBack/core/stt.py"
        ],
        "capability": "speaking",
        "parent": "language-server"
      },
      {
        "id": "text-to-speech",
        "title": "Озвучка для аудирования",
        "summary": "Порт синтеза речи для дрилла аудирования.",
        "modules": [
          "learningBack/core/tts.py"
        ],
        "capability": "reception-drills",
        "parent": "language-server"
      },
      {
        "id": "domain-graph-structure",
        "title": "Граф областей",
        "summary": "Реестр базовых областей, связи «нужно знать до» и вычисляемый уровень примитивности, с API для чтения и курирования.",
        "modules": [
          "learningBack/modules/knowledge/domains.py",
          "learningBack/modules/knowledge/domains_api.py"
        ],
        "capability": "domain-graph",
        "parent": "knowledge-server"
      },
      {
        "id": "cross-domain-prereqs",
        "title": "Межобластные предпосылки",
        "summary": "Связи между понятиями разных областей со ступенью освоения, нужные курсу, чтобы подтягивать только нужных предков.",
        "modules": [
          "learningBack/modules/knowledge/cross_links.py"
        ],
        "capability": "cross-domain-links",
        "parent": "knowledge-server"
      },
      {
        "id": "chain-placement",
        "title": "Проверка по цепочке базовых областей",
        "summary": "Выбор, о чём спрашивать при проверке базовых областей сверху вниз, и API плейсмента по цепочке и объёма пути.",
        "modules": [
          "learningBack/modules/knowledge/chain_placement.py",
          "learningBack/modules/knowledge/cross_links_api.py"
        ],
        "capability": "cross-domain-placement",
        "parent": "goal-server"
      },
      {
        "id": "goal-intake-dialog-impl",
        "title": "Диалог постановки цели",
        "summary": "Уточняющие вопросы, пересказ и подтверждение цели перед тем, как граф начнёт строиться.",
        "modules": [
          "learningBack/modules/knowledge/goal_intake.py"
        ],
        "capability": "goal-intake",
        "parent": "goal-server"
      },
      {
        "id": "goal-subdomain-split-impl",
        "title": "Разбиение цели на субдомены",
        "summary": "Крупная цель делится на части, каждая из которых строится отдельным запросом как примитивная область.",
        "modules": [
          "learningBack/modules/knowledge/subdomains.py"
        ],
        "capability": "goal-subdomain-split",
        "parent": "goal-server"
      },
      {
        "id": "goal-tree-assembly-impl",
        "title": "Сборка графа цели из субдоменов",
        "summary": "Графы субдоменов объединяются в один граф цели со связями-предпосылками через границы субдоменов.",
        "modules": [
          "learningBack/modules/knowledge/subdomains.py"
        ],
        "capability": "goal-tree-assembly",
        "parent": "goal-server"
      },
      {
        "id": "path-volume-preview-impl",
        "title": "Предпросмотр объёма пути",
        "summary": "Расчёт полного и интуитивного вариантов объёма пути до цели по графу областей, до построения графа.",
        "modules": [
          "learningBack/modules/knowledge/path_volume.py"
        ],
        "capability": "path-volume-preview",
        "parent": "goal-server"
      },
      {
        "id": "memorize-techniques-impl",
        "title": "Техники запоминания",
        "summary": "Две техники по общему контракту способа изучения: интервальное повторение и вспоминание по первым буквам.",
        "modules": [
          "learningBack/modules/srs/__init__.py",
          "learningBack/modules/mnemonic/__init__.py"
        ],
        "capability": "memorize-techniques",
        "parent": "study-server"
      },
      {
        "id": "listening-materials-impl",
        "title": "Материалы аудирования",
        "summary": "Генерация, курирование и выдача материалов аудирования, включая разбор дистракторов читательского дрилла.",
        "modules": [
          "learningBack/modules/languages/api.py",
          "learningBack/modules/languages/listening.py",
          "learningBack/modules/languages/distractors.py"
        ],
        "capability": "reception-drills",
        "parent": "language-server"
      },
      {
        "id": "speaking-flow-impl",
        "title": "Устный ответ",
        "summary": "Загрузка записи устного ответа, расшифровка и метрики темпа/пауз для оценки.",
        "modules": [
          "learningBack/modules/languages/speaking_api.py",
          "learningBack/modules/languages/speech.py"
        ],
        "capability": "speaking",
        "parent": "language-server"
      },
      {
        "id": "goal-intake-dialog-frontend",
        "title": "Диалог постановки цели (клиент)",
        "summary": "Компонент и логика диалога постановки цели: уточняющие вопросы, пересказ, подтверждение; публичная точка входа фичи.",
        "modules": [
          "learningFront/src/features/goal-intake/index.ts",
          "learningFront/src/features/goal-intake/model/dialog.ts",
          "learningFront/src/features/goal-intake/ui/goal-intake-dialog.tsx"
        ],
        "capability": "goal-intake",
        "parent": "goal-client"
      },
      {
        "id": "goal-confirm-gate-frontend",
        "title": "Заслон перед построением карты",
        "summary": "Блокирует построение графа, пока цель по области явно не подтверждена.",
        "modules": [
          "learningFront/src/features/graph-editor/ui/goal-gate.tsx"
        ],
        "capability": "goal-intake",
        "parent": "goal-client"
      },
      {
        "id": "goal-subdomain-split-frontend",
        "title": "Разбиение цели на субдомены (клиент)",
        "summary": "Правка предложенного моделью разбиения цели на части до построения: убрать, переименовать, видеть бюджет.",
        "modules": [
          "learningFront/src/features/graph-editor/model/split-edit.ts",
          "learningFront/src/features/graph-editor/ui/goal-planner.tsx"
        ],
        "capability": "goal-subdomain-split",
        "parent": "goal-client"
      },
      {
        "id": "goal-tree-assembly-frontend",
        "title": "Сборка графа цели из субдоменов (клиент)",
        "summary": "Запрос на построение графа по отредактированному человеком разбиению, по одному обращению к модели на субдомен.",
        "modules": [
          "learningFront/src/features/graph-editor/ui/goal-planner.tsx"
        ],
        "capability": "goal-tree-assembly",
        "parent": "goal-client"
      },
      {
        "id": "memorize-techniques-frontend",
        "title": "Техники запоминания (клиент)",
        "summary": "Клиентская часть техники «вспомнить по первым буквам»: метаданные модуля для реестра, самооценка вспоминания и публичный API фичи с рендерером активности.",
        "modules": [
          "learningFront/src/entities/module/mnemonic.ts",
          "learningFront/src/features/mnemonic-recall/index.ts",
          "learningFront/src/features/mnemonic-recall/model/rating.ts"
        ],
        "capability": "memorize-techniques",
        "parent": "study-client"
      },
      {
        "id": "reception-drills-listening-frontend",
        "title": "Listening-дрилл (клиент)",
        "summary": "Приём и прохождение дрилла аудирования: кэш записи на устройстве, лимит прослушиваний, проверка ответов и рендерер активности.",
        "modules": [
          "learningFront/src/features/listening-drill/index.ts",
          "learningFront/src/features/listening-drill/model/audio-cache.ts",
          "learningFront/src/features/listening-drill/model/listening-model.ts",
          "learningFront/src/features/listening-drill/model/plays-store.ts",
          "learningFront/src/features/listening-drill/model/plays-store.web.ts",
          "learningFront/src/features/listening-drill/ui/listening-drill-activity.tsx"
        ],
        "capability": "reception-drills",
        "parent": "language-client"
      },
      {
        "id": "writing-ielts-task-data-frontend",
        "title": "Данные задания Task 1 (клиент)",
        "summary": "Разбор и отрисовка числовых данных графика или таблицы задания Task 1 — читается офлайн, без картинки с сервера.",
        "modules": [
          "learningFront/src/features/ielts-writing/lib/task-data.ts",
          "learningFront/src/features/ielts-writing/ui/task-data-view.tsx"
        ],
        "capability": "writing-ielts",
        "parent": "language-client"
      },
      {
        "id": "reading-drill-frontend",
        "title": "Reading-дрилл (клиент)",
        "summary": "Разбор и прохождение reading-дрилла офлайн: текст, вопросы, таймер, мгновенная проверка и рендерер активности.",
        "modules": [
          "learningFront/src/features/reading-drill/index.ts",
          "learningFront/src/features/reading-drill/model/reading-model.ts",
          "learningFront/src/features/reading-drill/ui/reading-drill-activity.tsx"
        ],
        "capability": "reception-drills",
        "parent": "language-client"
      },
      {
        "id": "quiz-engine-frontend",
        "title": "Проверка ответов дриллов чтения и аудирования",
        "summary": "Общий разбор и детерминированная проверка вопросов (mcq/tfng/gap), используемая reading- и listening-дриллом.",
        "modules": [
          "learningFront/src/shared/lib/quiz.ts"
        ],
        "capability": "reception-drills",
        "parent": "study-client"
      },
      {
        "id": "speaking-response-frontend",
        "title": "Устный ответ (клиент)",
        "summary": "Запись устного ответа офлайн с лимитом времени, очередь на отправку записи и рендерер активности.",
        "modules": [
          "learningFront/src/features/speaking/index.ts",
          "learningFront/src/features/speaking/model/speaking-model.ts",
          "learningFront/src/features/speaking/ui/speaking-activity.tsx",
          "learningFront/src/shared/api/voice-outbox.ts"
        ],
        "capability": "speaking",
        "parent": "language-client"
      },
      {
        "id": "study-method-switch-frontend",
        "title": "Выбор способа изучения (клиент)",
        "summary": "Что можно выбрать для шага изучения и что выбрано сейчас, плюс запросы к серверу за этим выбором.",
        "modules": [
          "learningFront/src/features/study-method/index.ts",
          "learningFront/src/features/study-method/model/options.ts",
          "learningFront/src/shared/api/methods-api.ts"
        ],
        "capability": "method-switch",
        "parent": "study-client"
      },
      {
        "id": "mnemonic-activity-frontend",
        "title": "Рендерер техники «первые буквы»",
        "summary": "Экранная часть техники запоминания по первым буквам: подсказка, ответ, самооценка.",
        "modules": [
          "learningFront/src/features/mnemonic-recall/ui/mnemonic-activity.tsx"
        ],
        "capability": "memorize-techniques",
        "parent": "study-client"
      },
      {
        "id": "mastery-evidence-frontend",
        "title": "Свидетельство об освоении (клиент)",
        "summary": "Отправка результата любого способа изучения в общем формате свидетельства, с офлайн-очередью на устройстве.",
        "modules": [
          "learningFront/src/shared/api/evidence-api.ts"
        ],
        "capability": "mastery-evidence",
        "parent": "study-client"
      },
      {
        "id": "goal-intake-api-frontend",
        "title": "API постановки цели (клиент)",
        "summary": "Запросы диалога постановки цели: уточнение, пересказ, подтверждение, предпросмотр объёма пути.",
        "modules": [
          "learningFront/src/shared/api/goal-intake-api.ts"
        ],
        "capability": "goal-intake",
        "parent": "goal-client"
      },
      {
        "id": "platform-release-ops",
        "title": "Релиз и эксплуатация backend",
        "summary": "Резервная копия базы, деплой staging с проверкой здоровья и проверка восстановления копии.",
        "modules": [
          "scripts/backup-db.sh",
          "scripts/deploy-staging.sh",
          "scripts/restore-check.sh"
        ],
        "capability": "platform-release",
        "parent": "platform-client"
      },
      {
        "id": "client-version-gate-frontend",
        "title": "Проверка версии клиента",
        "summary": "Версия приложения, уходящая с запросами, и обработка отказа 426 понятным сообщением об обновлении.",
        "modules": [
          "learningFront/src/shared/api/app-version.ts",
          "learningFront/src/shared/api/client-outdated.ts"
        ],
        "capability": "platform-release",
        "parent": "platform-client"
      },
      {
        "id": "client-error-reports-frontend",
        "title": "Отчёты об ошибках клиента",
        "summary": "Необработанные ошибки устройства уходят на сервер отчётом, с дедупликацией и потолком за сессию.",
        "modules": [
          "learningFront/src/shared/api/error-reporter.ts"
        ],
        "capability": "platform-release",
        "parent": "platform-client"
      },
      {
        "id": "module-contract-check-frontend",
        "title": "Проверка манифеста модуля (клиент)",
        "summary": "Единые с сервером правила и коды отказа манифеста модуля.",
        "modules": [
          "learningFront/src/shared/engine/module/manifest-check.ts"
        ],
        "capability": "activity-engine",
        "parent": "platform-client"
      },
      {
        "id": "srs-card-merge-frontend",
        "title": "Слияние карточки повторения (клиент)",
        "summary": "Правило выбора более свежей версии карточки повторения при синхронизации с нескольких устройств.",
        "modules": [
          "learningFront/src/shared/engine/scheduler/card-merge.ts"
        ],
        "capability": "srs-error-log",
        "parent": "study-client"
      },
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
        ],
        "parent": "platform-server"
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
        ],
        "parent": "platform-server"
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
        ],
        "parent": "platform-server"
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
        ],
        "parent": "platform-server"
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
        ],
        "parent": "platform-client"
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
        ],
        "parent": "knowledge-server"
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
        ],
        "parent": "knowledge-client"
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
        ],
        "parent": "language-server"
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
        ],
        "parent": "ml-server"
      },
      {
        "id": "ml-practice-frontend",
        "title": "Практика ML-трека (клиент)",
        "summary": "Рендереры активностей ML-трека: прочитать материал, вспомнить своими словами, решить задачу на код с автосохранением черновика и отправкой на ревью.",
        "paths": [
          "learningFront/src/features/code-task",
          "learningFront/src/features/concept-recall",
          "learningFront/src/features/material-read"
        ],
        "parent": "ml-client"
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
        ],
        "parent": "study-client"
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
        ],
        "parent": "platform-client"
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
        ],
        "parent": "goal-client"
      },
      {
        "id": "daily-loop-frontend",
        "title": "Ежедневный цикл (клиент)",
        "summary": "Экран «Сегодня» решает единственное следующее действие (шаг курса, повторение или определение уровня) и очередь повторения просроченных карточек.",
        "paths": [
          "learningFront/src/pages/home",
          "learningFront/src/pages/review"
        ],
        "parent": "study-client"
      },
      {
        "id": "progress-tracking-frontend",
        "title": "Прогресс обучения (клиент)",
        "summary": "Офлайн-метрики (удержание, закрытие error-log, рост по рубрикам, серия дней) и экран прогресса, считающие их из локального event log и SRS-карточек.",
        "paths": [
          "learningFront/src/entities/progress",
          "learningFront/src/pages/progress"
        ],
        "parent": "study-client"
      },
      {
        "id": "course-plan-frontend",
        "title": "План курса (клиент)",
        "summary": "Порядок изучения графа: текущий шаг курса с причиной (укоренение/вглубь/ветка/спираль) и экран, сводящий план с исполнением шага.",
        "paths": [
          "learningFront/src/features/course",
          "learningFront/src/pages/course"
        ],
        "parent": "goal-client"
      },
      {
        "id": "placement-session-frontend",
        "title": "Определение уровня (клиент)",
        "summary": "Выбор целевой ступени и сессия адаптивных зондов на границе знаний домена с финальной картой освоенности.",
        "paths": [
          "learningFront/src/features/placement",
          "learningFront/src/pages/placement"
        ],
        "parent": "goal-client"
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
        ],
        "parent": "language-client"
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
        ],
        "parent": "platform-server"
      },
      {
        "id": "server-api-routes",
        "title": "HTTP-маршруты",
        "summary": "Входные точки API: роутеры по разделам.",
        "parent": "platform-server",
        "paths": [
          "learningBack/api"
        ]
      },
      {
        "id": "server-core",
        "title": "Ядро сервера",
        "summary": "Общие службы сервера: конфигурация, база, безопасность, модель, сообщения и ошибки.",
        "parent": "platform-server",
        "paths": [
          "learningBack/core"
        ]
      },
      {
        "id": "server-migrations",
        "title": "Схема базы данных",
        "summary": "Миграции Alembic: история изменений схемы.",
        "parent": "platform-server",
        "paths": [
          "learningBack/migrations"
        ]
      },
      {
        "id": "server-scripts",
        "title": "Служебные скрипты сервера",
        "summary": "Разовые и плановые скрипты: импорт, слияние, резервные копии, обновление знаний.",
        "parent": "platform-server",
        "paths": [
          "learningBack/scripts"
        ]
      },
      {
        "id": "ops-scripts",
        "title": "Эксплуатация",
        "summary": "Скрипты развёртывания и резервного копирования на сервере.",
        "parent": "platform-server",
        "paths": [
          "scripts"
        ]
      },
      {
        "id": "knowledge-module",
        "title": "Модуль знаний",
        "summary": "Конвейер знаний: источники, утверждения, сверка, сборка узлов, курс, свежесть, языки.",
        "parent": "knowledge-server",
        "paths": [
          "learningBack/modules/knowledge"
        ]
      },
      {
        "id": "languages-module",
        "title": "Языковой модуль",
        "summary": "Серверная часть языкового трека.",
        "parent": "language-server",
        "paths": [
          "learningBack/modules/languages"
        ]
      },
      {
        "id": "ml-module",
        "title": "ML-модуль",
        "summary": "Серверная часть ML-трека.",
        "parent": "ml-server",
        "paths": [
          "learningBack/modules/ml"
        ]
      },
      {
        "id": "study-modules",
        "title": "Повторение и мнемоника",
        "summary": "Модули интервального повторения и мнемотехник.",
        "parent": "study-server",
        "paths": [
          "learningBack/modules/srs",
          "learningBack/modules/mnemonic"
        ]
      },
      {
        "id": "client-routes",
        "title": "Маршруты приложения",
        "summary": "Экраны expo-router: вкладки и отдельные страницы.",
        "parent": "platform-client",
        "paths": [
          "learningFront/src/app"
        ]
      },
      {
        "id": "client-shared-api",
        "title": "Клиент API и синхронизация",
        "summary": "Запросы к серверу, локальное хранилище, синхронизация, токены.",
        "parent": "platform-client",
        "paths": [
          "learningFront/src/shared/api"
        ]
      },
      {
        "id": "client-shared-ui",
        "title": "Интерфейсные примитивы",
        "summary": "Общие компоненты, тема, i18n, утилиты.",
        "parent": "platform-client",
        "paths": [
          "learningFront/src/shared/ui",
          "learningFront/src/shared/i18n",
          "learningFront/src/shared/config",
          "learningFront/src/shared/lib",
          "learningFront/src/test-setup.ts"
        ]
      },
      {
        "id": "client-engine",
        "title": "Движок активностей клиента",
        "summary": "Общий движок шагов и оценивания активностей.",
        "parent": "study-client",
        "paths": [
          "learningFront/src/shared/engine"
        ]
      },
      {
        "id": "client-widgets",
        "title": "Виджеты оболочки",
        "summary": "Навигация, диспетчер активностей, реестр модулей, панель предмета.",
        "parent": "platform-client",
        "paths": [
          "learningFront/src/widgets"
        ]
      },
      {
        "id": "client-entities",
        "title": "Сущности клиента",
        "summary": "Сессия, прогресс, модуль, понятие — общие модели клиента.",
        "parent": "platform-client",
        "paths": [
          "learningFront/src/entities"
        ]
      },
      {
        "id": "client-knowledge",
        "title": "Граф, источники и проблемы",
        "summary": "Редактор графа, источники, пул проблем, профиль навыков, библиотека.",
        "parent": "knowledge-client",
        "paths": [
          "learningFront/src/features/graph-editor",
          "learningFront/src/features/sources",
          "learningFront/src/features/claim-problems",
          "learningFront/src/features/skill-profile",
          "learningFront/src/pages/graph",
          "learningFront/src/pages/sources",
          "learningFront/src/pages/problems",
          "learningFront/src/pages/skill-profile",
          "learningFront/src/pages/library",
          "learningFront/src/pages/materials",
          "learningFront/src/features/material-read"
        ]
      },
      {
        "id": "client-goal",
        "title": "Цель, вход и курс",
        "summary": "Разбор цели, входная проверка, план курса, онбординг.",
        "parent": "goal-client",
        "paths": [
          "learningFront/src/features/goal-intake",
          "learningFront/src/features/goal-reached",
          "learningFront/src/features/placement",
          "learningFront/src/features/prior-test",
          "learningFront/src/features/course",
          "learningFront/src/pages/course",
          "learningFront/src/pages/onboarding",
          "learningFront/src/pages/placement"
        ]
      },
      {
        "id": "client-study",
        "title": "Изучение и повторение",
        "summary": "Изучение понятия, вспоминание, метод изучения, обзор, прогресс, главная.",
        "parent": "study-client",
        "paths": [
          "learningFront/src/features/concept-study",
          "learningFront/src/features/concept-recall",
          "learningFront/src/features/study-method",
          "learningFront/src/features/mnemonic-recall",
          "learningFront/src/pages/review",
          "learningFront/src/pages/progress",
          "learningFront/src/pages/home"
        ]
      },
      {
        "id": "client-language",
        "title": "Языковые тренажёры",
        "summary": "Аудирование, чтение, письмо IELTS, говорение.",
        "parent": "language-client",
        "paths": [
          "learningFront/src/features/listening-drill",
          "learningFront/src/features/reading-drill",
          "learningFront/src/features/ielts-writing",
          "learningFront/src/features/speaking"
        ]
      },
      {
        "id": "client-ml",
        "title": "Задания с кодом",
        "summary": "Клиентская часть ML-практики.",
        "parent": "ml-client",
        "paths": [
          "learningFront/src/features/code-task"
        ]
      },
      {
        "id": "client-account",
        "title": "Вход, профиль и уведомления",
        "summary": "Авторизация, профиль, настройки пушей.",
        "parent": "platform-client",
        "paths": [
          "learningFront/src/pages/auth",
          "learningFront/src/pages/profile",
          "learningFront/src/features/push-settings"
        ]
      },
      {
        "id": "checks-server",
        "title": "Проверки: сервер",
        "summary": "Pytest-тесты бэкенда.",
        "parent": "checks"
      },
      {
        "id": "checks-client",
        "title": "Проверки: клиент",
        "summary": "Vitest-тесты рядом с кодом клиента.",
        "parent": "checks"
      },
      {
        "id": "tests-validation",
        "title": "Валидационные проверки V-01xx",
        "summary": "Валидационные проверки V-01xx.",
        "parent": "checks-server",
        "modules": [
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
        ]
      },
      {
        "id": "tests-knowledge",
        "title": "Тесты конвейера знаний",
        "summary": "Тесты конвейера знаний.",
        "parent": "checks-server",
        "modules": [
          "learningBack/tests/test_course.py",
          "learningBack/tests/test_graph_access.py",
          "learningBack/tests/test_graph_nodes.py",
          "learningBack/tests/test_material_nodes.py",
          "learningBack/tests/test_materials.py",
          "learningBack/tests/test_graph_interface.py",
          "learningBack/tests/test_graph_links_check.py",
          "learningBack/tests/test_graph_subject_agnostic.py",
          "learningBack/tests/test_gap_search.py",
          "learningBack/tests/test_graph_admin.py",
          "learningBack/tests/test_graph_extensions.py",
          "learningBack/tests/test_ingest.py",
          "learningBack/tests/test_merge.py",
          "learningBack/tests/test_prior_report.py",
          "learningBack/tests/test_provenance.py",
          "learningBack/tests/test_review.py",
          "learningBack/tests/test_source_search.py",
          "learningBack/tests/test_source_upload.py",
          "learningBack/tests/test_sources_admin_only.py"
        ]
      },
      {
        "id": "tests-profile",
        "title": "Тесты профиля навыков и цели",
        "summary": "Тесты профиля навыков и цели.",
        "parent": "checks-server",
        "modules": [
          "learningBack/tests/test_placement.py",
          "learningBack/tests/test_goal_intake.py",
          "learningBack/tests/test_profile_build.py",
          "learningBack/tests/test_profile_coverage.py",
          "learningBack/tests/test_profile_fill.py",
          "learningBack/tests/test_profile_match.py",
          "learningBack/tests/test_profile_sources.py",
          "learningBack/tests/test_profile_start.py",
          "learningBack/tests/test_skill_profile.py",
          "learningBack/tests/test_stage_level.py"
        ]
      },
      {
        "id": "tests-platform",
        "title": "Тесты платформы и прочее",
        "summary": "Тесты ядра, доступа, очередей, хранилищ и остального.",
        "parent": "checks-server",
        "modules": [
          "learningBack/tests/conftest.py",
          "learningBack/tests/test_assessment.py",
          "learningBack/tests/test_assessment_cache.py",
          "learningBack/tests/test_auth.py",
          "learningBack/tests/test_centrality.py",
          "learningBack/tests/test_code_review.py",
          "learningBack/tests/test_config_secrets.py",
          "learningBack/tests/test_content.py",
          "learningBack/tests/test_cow.py",
          "learningBack/tests/test_job_retry.py",
          "learningBack/tests/test_llm_cache.py",
          "learningBack/tests/test_mastery.py",
          "learningBack/tests/test_modules.py",
          "learningBack/tests/test_openai_gateway.py",
          "learningBack/tests/test_promotion.py",
          "learningBack/tests/test_study.py",
          "learningBack/tests/test_sync.py",
          "learningBack/tests/test_toefl.py",
          "learningBack/tests/test_usage.py",
          "learningBack/tests/test_account_delete.py",
          "learningBack/tests/test_awl.py",
          "learningBack/tests/test_chain_placement.py",
          "learningBack/tests/test_cross_links.py",
          "learningBack/tests/test_domains.py",
          "learningBack/tests/test_explain_distractors.py",
          "learningBack/tests/test_language_course.py",
          "learningBack/tests/test_listening_materials.py",
          "learningBack/tests/test_mail.py",
          "learningBack/tests/test_memorization_module.py",
          "learningBack/tests/test_module_manifest.py",
          "learningBack/tests/test_monitoring.py",
          "learningBack/tests/test_path_volume.py",
          "learningBack/tests/test_plugin_isolation.py",
          "learningBack/tests/test_provider_errors.py",
          "learningBack/tests/test_reading.py",
          "learningBack/tests/test_retention.py",
          "learningBack/tests/test_second_technique.py",
          "learningBack/tests/test_speaking.py",
          "learningBack/tests/test_srs_merge.py",
          "learningBack/tests/test_subdomains.py",
          "learningBack/tests/test_user_data_access.py",
          "learningBack/tests/test_versioning.py",
          "learningBack/tests/test_worker.py",
          "learningBack/tests/kg_helpers.py",
          "learningBack/tests/test_backup_objects.py",
          "learningBack/tests/test_migrations_match_models.py",
          "learningBack/tests/test_notifications.py",
          "learningBack/tests/test_notifications_review.py",
          "learningBack/tests/test_objects.py",
          "learningBack/tests/test_push.py"
        ]
      },
      {
        "id": "tests-client-entities",
        "title": "Тесты клиента: entities",
        "summary": "Тесты слоя entities.",
        "parent": "checks-client",
        "modules": [
          "learningFront/src/entities/progress/model/metrics.test.ts",
          "learningFront/src/entities/module/module.test.ts",
          "learningFront/src/entities/session/subject.test.ts"
        ]
      },
      {
        "id": "tests-client-features",
        "title": "Тесты клиента: features",
        "summary": "Тесты слоя features.",
        "parent": "checks-client",
        "modules": [
          "learningFront/src/features/code-task/model/code-draft.test.ts",
          "learningFront/src/features/ielts-writing/lib/rubric.test.ts",
          "learningFront/src/features/goal-intake/model/dialog.test.ts",
          "learningFront/src/features/graph-editor/model/split-edit.test.ts",
          "learningFront/src/features/ielts-writing/lib/task-data.test.ts",
          "learningFront/src/features/listening-drill/model/listening-model.test.ts",
          "learningFront/src/features/mnemonic-recall/model/rating.test.ts",
          "learningFront/src/features/reading-drill/model/reading-model.test.ts",
          "learningFront/src/features/speaking/model/speaking-model.test.ts",
          "learningFront/src/features/study-method/model/options.test.ts",
          "learningFront/src/features/course/model/draft.test.ts",
          "learningFront/src/features/course/model/notices.test.ts",
          "learningFront/src/features/goal-intake/model/steps.test.ts",
          "learningFront/src/features/graph-editor/model/build-progress.test.ts",
          "learningFront/src/features/graph-editor/model/scheme.test.ts",
          "learningFront/src/features/graph-editor/model/stage-groups.test.ts",
          "learningFront/src/features/prior-test/model/report.test.ts",
          "learningFront/src/features/push-settings/model/push-model.test.ts",
          "learningFront/src/features/skill-profile/model/profile-model.test.ts",
          "learningFront/src/features/sources/model/gaps-model.test.ts",
          "learningFront/src/features/sources/model/sources-model.test.ts"
        ]
      },
      {
        "id": "tests-client-pages",
        "title": "Тесты клиента: pages",
        "summary": "Тесты слоя pages.",
        "parent": "checks-client",
        "modules": [
          "learningFront/src/pages/home/model/next-action.test.ts",
          "learningFront/src/pages/home/model/tiles-model.test.ts"
        ]
      },
      {
        "id": "tests-client-shared",
        "title": "Тесты клиента: shared",
        "summary": "Тесты слоя shared.",
        "parent": "checks-client",
        "modules": [
          "learningFront/src/shared/api/auto-sync.test.ts",
          "learningFront/src/shared/api/sync-service.test.ts",
          "learningFront/src/shared/engine/module/registry.test.ts",
          "learningFront/src/shared/engine/scheduler/scheduler.test.ts",
          "learningFront/src/shared/api/materials-api.test.ts",
          "learningFront/src/shared/api/client-outdated.test.ts",
          "learningFront/src/shared/api/error-reporter.test.ts",
          "learningFront/src/shared/api/evidence-api.test.ts",
          "learningFront/src/shared/api/voice-outbox.test.ts",
          "learningFront/src/shared/engine/module/manifest-check.test.ts",
          "learningFront/src/shared/engine/scheduler/card-merge.test.ts",
          "learningFront/src/shared/api/notification-route.test.ts",
          "learningFront/src/shared/config/design.test.ts",
          "learningFront/src/shared/i18n-core/i18n.test.ts",
          "learningFront/src/shared/ui/nav-layout.test.ts",
          "learningFront/src/shared/ui/theme-mode.test.ts"
        ]
      },
      {
        "id": "tests-client-widgets",
        "title": "Тесты клиента: widgets",
        "summary": "Тесты слоя widgets.",
        "parent": "checks-client",
        "modules": [
          "learningFront/src/widgets/module-registry/recall-payload.test.ts"
        ]
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
        "id": "src-server",
        "title": "Сервер",
        "kind": "db"
      },
      {
        "id": "src-server-stores",
        "title": "Хранилища сервера",
        "kind": "db",
        "parent": "src-server"
      },
      {
        "id": "src-server-files",
        "title": "Файлы сервера",
        "kind": "file",
        "parent": "src-server"
      },
      {
        "id": "src-server-memory",
        "title": "Память процесса",
        "kind": "memory",
        "parent": "src-server"
      },
      {
        "id": "src-server-env",
        "title": "Настройки окружения",
        "kind": "env",
        "parent": "src-server"
      },
      {
        "id": "src-client",
        "title": "Устройство",
        "kind": "db"
      },
      {
        "id": "src-client-stores",
        "title": "Хранилища на устройстве",
        "kind": "db",
        "parent": "src-client"
      },
      {
        "id": "src-client-files",
        "title": "Файлы на устройстве",
        "kind": "file",
        "parent": "src-client"
      },
      {
        "id": "src-client-memory",
        "title": "Память клиента",
        "kind": "memory",
        "parent": "src-client"
      },
      {
        "id": "src-external",
        "title": "Внешние сервисы",
        "kind": "http"
      },
      {
        "id": "src-external-api",
        "title": "HTTP-интерфейсы",
        "kind": "http",
        "parent": "src-external"
      },
      {
        "id": "db-postgres",
        "kind": "db",
        "where": "settings.database_url (Postgres)",
        "parent": "src-server-stores"
      },
      {
        "id": "env-root",
        "kind": "env",
        "where": "../.env (корень репозитория)",
        "parent": "src-server-env"
      },
      {
        "id": "http-llm-provider",
        "kind": "http",
        "where": "settings.llm_base_url (RouterAI, OpenAI-совместимый)",
        "parent": "src-external-api"
      },
      {
        "id": "mem-ratelimit",
        "kind": "memory",
        "where": "core.ratelimit.reset_request_limiter",
        "title": "Счётчики лимита запросов (in-process)",
        "parent": "src-server-memory"
      },
      {
        "id": "db-sqlite-local",
        "kind": "db",
        "where": "expo-sqlite, файл praxis.db на устройстве",
        "title": "Локальная база приложения (SQLite)",
        "parent": "src-client-stores"
      },
      {
        "id": "mem-web-local-store",
        "kind": "memory",
        "where": "in-memory Map в веб-рантайме (sqlite-local-store.web.ts)",
        "title": "Веб-заглушка локального хранилища",
        "parent": "src-client-memory"
      },
      {
        "id": "http-backend-api",
        "kind": "http",
        "where": "EXPO_PUBLIC_API_BASE_URL (backend FastAPI, по умолчанию http://localhost:8000)",
        "parent": "src-external-api"
      },
      {
        "id": "file-device-storage",
        "kind": "file",
        "where": "expo-secure-store (native) / localStorage (web)",
        "title": "Защищённое хранилище токена и настроек на устройстве",
        "parent": "src-client-stores"
      },
      {
        "id": "mem-sandbox-budget",
        "kind": "memory",
        "where": "core.sandbox._calls, core.sandbox._failures",
        "title": "Счётчики вызовов и сбоев модуля (in-process)",
        "parent": "src-server-memory"
      },
      {
        "id": "mem-node-change-subscribers",
        "kind": "memory",
        "where": "modules.knowledge.events._subscribers",
        "title": "Подписчики на изменение узла (in-process)",
        "parent": "src-server-memory"
      },
      {
        "id": "file-awl-wordlist",
        "kind": "file",
        "where": "learningBack/modules/languages/data/awl.tsv",
        "title": "Список слов Academic Word List",
        "parent": "src-server-files"
      },
      {
        "id": "file-voice-recording",
        "kind": "file",
        "where": "settings.voice_dir",
        "title": "Запись устного ответа (временный файл до расшифровки)",
        "parent": "src-server-files"
      },
      {
        "id": "file-listening-audio",
        "kind": "file",
        "where": "settings.audio_dir",
        "title": "Озвучка материала аудирования",
        "parent": "src-server-files"
      },
      {
        "id": "file-listening-audio-cache",
        "kind": "file",
        "where": "expo-file-system: Paths.document/'listening' (кэш записей listening-дрилла на устройстве)",
        "title": "Кэш аудио listening-дрилла на устройстве",
        "parent": "src-client-files"
      },
      {
        "id": "mem-client-outdated-listeners",
        "kind": "memory",
        "where": "модульный Set в client-outdated.ts",
        "title": "Подписчики на «устаревшая версия приложения» (in-process)",
        "parent": "src-client-memory"
      },
      {
        "id": "file-voice-recording-device",
        "kind": "file",
        "where": "expo-audio: recorder.uri (временная запись на устройстве до отправки)",
        "title": "Запись устного ответа на устройстве до отправки",
        "parent": "src-client-files"
      },
      {
        "id": "file-backup-dir",
        "kind": "file",
        "where": ".data/backups (по умолчанию, параметр скрипта)",
        "title": "Каталог резервных копий базы",
        "parent": "src-server-files"
      },
      {
        "id": "file-object-store",
        "kind": "file",
        "where": "settings.s3_endpoint (S3-хранилище источников, SeaweedFS)",
        "parent": "src-server-stores"
      }
    ]
  }
}
```

## Функциональная карта

```docdd-functional
{
  "added": {
    "capabilities": [
      {
        "id": "area-knowledge",
        "title": "Знания",
        "summary": "Из чего строится граф знаний человека и как им пользуются: граф, библиотека, навыки.",
        "status": "partial"
      },
      {
        "id": "knowledge-graph",
        "title": "Графы знаний",
        "parent": "area-knowledge"
      },
      {
        "id": "my-library",
        "title": "Моя библиотека",
        "status": "not_implemented",
        "note": "предмет один (profile.subject), переключения и списка нет",
        "parent": "area-knowledge"
      },
      {
        "id": "skill-outline-preview",
        "title": "Контур состава навыка до сборки",
        "status": "implemented",
        "note": "Реализовано в T-0101",
        "parent": "area-knowledge"
      },
      {
        "id": "skill-area-opt-out",
        "title": "Отметка «уже владею» по области",
        "status": "implemented",
        "note": "Реализовано в T-0101",
        "parent": "area-knowledge"
      },
      {
        "id": "knowledge-use",
        "title": "Работа со знаниями",
        "parent": "area-knowledge"
      },
      {
        "id": "area-learning",
        "title": "Учёба",
        "summary": "Как знания читают, запоминают и проверяют: активности и мини-приложения.",
        "status": "partial"
      },
      {
        "id": "activity-engine",
        "title": "Движок Activity и модули",
        "parent": "area-learning"
      },
      {
        "id": "extensions",
        "title": "Подключение мини-приложений",
        "parent": "area-learning"
      },
      {
        "id": "area-people",
        "title": "Человек и сообщество",
        "summary": "Аккаунт, роли, свои данные и общение с другими.",
        "status": "partial"
      },
      {
        "id": "account-roles",
        "title": "Доступ и аккаунт",
        "parent": "area-people"
      },
      {
        "id": "my-data",
        "title": "Мои знания и данные",
        "parent": "area-people"
      },
      {
        "id": "community",
        "title": "Сообщество",
        "parent": "area-people"
      },
      {
        "id": "area-operations",
        "title": "Сопровождение",
        "summary": "Работа куратора и администратора над содержимым.",
        "status": "partial"
      },
      {
        "id": "admin-curation",
        "title": "Администрирование",
        "parent": "area-operations"
      }
    ]
  }
}
```

## Журнал

- 2026-10-20 · на подтверждение · architect
- 2026-10-20 · подтверждён · architect
