---
id: M-0021
type: map
title: 'Описание кода: заход 1'
status: approved
created: 2026-10-05
updated: 2026-10-05
---

# Описание кода: заход 1

Черновик: составлен моделью, не подтверждён. Прочитайте, поправьте руками
то, что модель не поняла, и подтвердите — до этого карта на общую картину
не влияет.

```docdd-codemap
{
  "added": {
    "modules": [
      {
        "id": "learningBack/core/evidence.py",
        "title": "Свидетельство об освоении",
        "layer": "ядро",
        "path": "learningBack/core/evidence.py",
        "summary": "Единый формат результата ответа независимо от способа запоминания: узел, ступень Блума, результат 0..1, источник. dispatch передаёт свидетельство всем включённым модулям, которые заявили, что его принимают — так смена способа не теряет освоенность.",
        "api": [
          {
            "name": "Evidence",
            "kind": "type",
            "summary": "Результат по ступени bloom для узла concept_id от способа source",
            "signature": "{ concept_id: UUID, bloom: str, score: float, source: str }"
          },
          {
            "name": "dispatch",
            "kind": "function",
            "summary": "Передать свидетельство модулям, которые его принимают",
            "signature": "(session, user_id, domain, evidence, modules) => int"
          }
        ]
      },
      {
        "id": "learningBack/core/mail.py",
        "title": "Отправка писем восстановления пароля",
        "layer": "ядро",
        "path": "learningBack/core/mail.py",
        "summary": "Отправитель письма с кодом восстановления пароля. Провайдер — любой SMTP через переменные окружения; без SMTP_HOST работает консольная заглушка. Сбой отправки не меняет ответ API, чтобы по нему нельзя было узнать, есть ли такой email.",
        "api": [
          {
            "name": "Mailer",
            "kind": "type",
            "summary": "Контракт отправителя письма",
            "signature": "{ send(to, subject, body) => None }"
          },
          {
            "name": "get_mailer",
            "kind": "function",
            "summary": "Выбрать отправителя: SMTP, если настроен, иначе консоль",
            "signature": "() => Mailer"
          },
          {
            "name": "send_safely",
            "kind": "function",
            "summary": "Отправить письмо, не роняя вызывающего при сбое",
            "signature": "(to, subject, body) => bool"
          },
          {
            "name": "reset_code_message",
            "kind": "function",
            "summary": "Текст письма с кодом восстановления пароля",
            "signature": "(code, ttl_minutes) => (subject, body)"
          }
        ]
      },
      {
        "id": "learningBack/core/manifest.py",
        "title": "Манифест модуля и его проверка",
        "layer": "ядро",
        "path": "learningBack/core/manifest.py",
        "summary": "Модуль описывает себя манифестом: id, версия, версия контракта ядра, что даёт и просит, зависимости, разрешённая сеть. Ядро проверяет манифест при подключении набора модулей — неизвестный запрос, несовместимый контракт, цикл зависимостей — и отказывает с понятной причиной.",
        "api": [
          {
            "name": "ModuleManifest",
            "kind": "type",
            "summary": "Манифест модуля",
            "signature": "{ id, title, version, contract, provides, requires, dependsOn, network }"
          },
          {
            "name": "ManifestError",
            "kind": "class",
            "summary": "Манифест отклонён ядром",
            "signature": "(code, module_id, message)"
          },
          {
            "name": "check_manifest",
            "kind": "function",
            "summary": "Проверить манифест одного модуля сам по себе",
            "signature": "(manifest, module_id?) => None | raises"
          },
          {
            "name": "check_set",
            "kind": "function",
            "summary": "Проверить набор модулей: занятые id, отсутствующие зависимости, циклы",
            "signature": "(manifests) => None | raises"
          },
          {
            "name": "load_order",
            "kind": "function",
            "summary": "Порядок подъёма модулей: зависимости раньше зависимых",
            "signature": "(manifests) => list[str]"
          },
          {
            "name": "contract_compatible",
            "kind": "function",
            "summary": "Совместима ли версия контракта модуля с ядром",
            "signature": "(module_contract, core_contract?) => bool"
          },
          {
            "name": "CONTRACT_VERSION",
            "kind": "const",
            "summary": "Текущая версия контракта ядра",
            "signature": "\"1.0\""
          }
        ]
      },
      {
        "id": "learningBack/core/methods.py",
        "title": "Способы изучения: контракт и реестр",
        "layer": "ядро",
        "path": "learningBack/core/methods.py",
        "summary": "Контракт способа изучения (карточки, письмо с оценкой, мини-игра): на входе узлы к проработке, на выходе активности; результат способ сообщает только как свидетельство (core.evidence). Модуль объявляет способы и шаг курса, который они исполняют; выбор человека хранится в его профиле.",
        "api": [
          {
            "name": "StudyMethod",
            "kind": "type",
            "summary": "Описание способа изучения: шаг, тип активности, офлайн",
            "signature": "{ id, title, purpose, activity_type, offline, module, in_course }"
          },
          {
            "name": "MethodError",
            "kind": "class",
            "summary": "Описание способа отклонено"
          },
          {
            "name": "check_methods",
            "kind": "function",
            "summary": "Проверить набор способов модуля: уникальность id, известный шаг",
            "signature": "(methods) => None | raises"
          },
          {
            "name": "preferences",
            "kind": "function",
            "summary": "Выбранные человеком способы по шагам из профиля",
            "signature": "(profile) => dict[str, str]"
          },
          {
            "name": "for_purpose",
            "kind": "function",
            "summary": "Способ для шага курса: предпочтительный или первый доступный",
            "signature": "(methods, purpose, preferred?) => StudyMethod | None"
          },
          {
            "name": "PURPOSES",
            "kind": "const",
            "summary": "Шаги изучения: read, recall, contrast, apply, remember",
            "signature": "(str, ...)"
          }
        ]
      },
      {
        "id": "learningBack/core/monitoring.py",
        "title": "Мониторинг здоровья системы",
        "layer": "ядро",
        "path": "learningBack/core/monitoring.py",
        "summary": "Сводка здоровья по уже накопленным данным: доля упавших задач, расход токенов, число ошибок клиента за окно — без отдельной аналитики и планировщика. Алерт — это состояние в ответе GET /v1/monitoring, которое опрашивает внешний монитор.",
        "api": [
          {
            "name": "jobs_health",
            "kind": "function",
            "summary": "Доля задач в failed среди завершённых за окно",
            "signature": "(session, now?) => dict"
          },
          {
            "name": "tokens_health",
            "kind": "function",
            "summary": "Расход токенов за окно против лимита",
            "signature": "(session, now?) => dict"
          },
          {
            "name": "client_errors_health",
            "kind": "function",
            "summary": "Число ошибок клиента за окно против лимита",
            "signature": "(session, now?) => dict"
          },
          {
            "name": "snapshot",
            "kind": "function",
            "summary": "Сводное здоровье системы и список сработавших алертов",
            "signature": "(session, now?) => dict"
          },
          {
            "name": "clip",
            "kind": "function",
            "summary": "Обрезать текст до лимита длины",
            "signature": "(text, limit) => str | None"
          }
        ]
      },
      {
        "id": "learningBack/core/routers/methods.py",
        "title": "API способов изучения и свидетельств",
        "layer": "маршруты",
        "path": "learningBack/core/routers/methods.py",
        "summary": "Эндпоинты для выбора способа изучения на шаг курса и приёма свидетельств об освоении от любого способа. Освоенность, ошибки и карточки при смене способа не трогаются.",
        "api": [
          {
            "name": "list_methods",
            "kind": "function",
            "summary": "GET /methods — способы включённых модулей",
            "signature": "(user) => list[dict]"
          },
          {
            "name": "submit_evidence",
            "kind": "function",
            "summary": "POST /evidence — принять свидетельство от способа",
            "signature": "(body, user, session) => dict"
          },
          {
            "name": "get_study_methods",
            "kind": "function",
            "summary": "GET /me/study-methods — выбранные способы и варианты",
            "signature": "(user) => dict"
          },
          {
            "name": "set_study_method",
            "kind": "function",
            "summary": "PUT /me/study-methods — выбрать способ и пересобрать курс",
            "signature": "(body, user, session) => dict"
          }
        ]
      },
      {
        "id": "learningBack/core/routers/modules_admin.py",
        "title": "API управления модулями",
        "layer": "маршруты",
        "path": "learningBack/core/routers/modules_admin.py",
        "summary": "Жизненный цикл подключённого модуля для администратора: список, включение, согласие на расширенные разрешения, отключение, необратимое удаление данных.",
        "api": [
          {
            "name": "list_modules",
            "kind": "function",
            "summary": "GET /modules — подключённые модули с манифестом и статусом",
            "signature": "(session) => list[dict]"
          },
          {
            "name": "enable_module",
            "kind": "function",
            "summary": "POST /modules/{id}/enable",
            "signature": "(module_id, session) => dict"
          },
          {
            "name": "approve_module",
            "kind": "function",
            "summary": "POST /modules/{id}/approve — согласие на запросы и сеть",
            "signature": "(module_id, session) => dict"
          },
          {
            "name": "disable_module",
            "kind": "function",
            "summary": "POST /modules/{id}/disable",
            "signature": "(module_id, session) => dict"
          },
          {
            "name": "uninstall_module",
            "kind": "function",
            "summary": "POST /modules/{id}/uninstall — удалить данные модуля с подтверждением",
            "signature": "(module_id, body, session) => dict"
          }
        ]
      },
      {
        "id": "learningBack/core/routers/monitoring.py",
        "title": "API мониторинга и ошибок клиента",
        "layer": "маршруты",
        "path": "learningBack/core/routers/monitoring.py",
        "summary": "Приём необработанных ошибок клиента (с лимитом на человека) и выдача сводки здоровья системы администратору.",
        "api": [
          {
            "name": "report_client_error",
            "kind": "function",
            "summary": "POST /client-errors — принять ошибку от вошедшего клиента",
            "signature": "(body, user, session) => dict"
          },
          {
            "name": "monitoring_snapshot",
            "kind": "function",
            "summary": "GET /monitoring — статус и сработавшие алерты",
            "signature": "(session) => dict"
          }
        ]
      },
      {
        "id": "learningBack/core/routers/userdata.py",
        "title": "API «Мои данные»",
        "layer": "маршруты",
        "path": "learningBack/core/routers/userdata.py",
        "summary": "Экран «Мои данные»: какие типы данных хранятся, разрешения модулям по типу и режиму, журнал обращений, выгрузка и удаление всех данных или аккаунта целиком. Отдельно — запуск удаления по сроку хранения.",
        "api": [
          {
            "name": "data_types",
            "kind": "function",
            "summary": "GET /me/data/types — какие данные хранятся и зачем",
            "signature": "(user) => list[dict]"
          },
          {
            "name": "data_permissions",
            "kind": "function",
            "summary": "GET /me/data/permissions",
            "signature": "(user, session) => list[dict]"
          },
          {
            "name": "set_data_permission",
            "kind": "function",
            "summary": "PUT /me/data/permissions — выдать/отозвать разрешение модулю",
            "signature": "(body, user, session) => dict"
          },
          {
            "name": "data_access_log",
            "kind": "function",
            "summary": "GET /me/data/access-log",
            "signature": "(user, session, limit?) => list[dict]"
          },
          {
            "name": "export_data",
            "kind": "function",
            "summary": "GET /me/data/export — все данные одним документом",
            "signature": "(user, session) => dict"
          },
          {
            "name": "erase_data",
            "kind": "function",
            "summary": "POST /me/data/erase — удалить все данные с подтверждением",
            "signature": "(body, user, session) => dict"
          },
          {
            "name": "delete_account",
            "kind": "function",
            "summary": "POST /me/data/delete-account — удалить аккаунт с подтверждением и паролем",
            "signature": "(body, user, session) => dict"
          },
          {
            "name": "run_retention",
            "kind": "function",
            "summary": "POST /retention/run — удалить данные с истёкшим сроком хранения",
            "signature": "(session) => dict"
          }
        ]
      },
      {
        "id": "learningBack/core/sandbox.py",
        "title": "Охраняемое исполнение модуля",
        "layer": "ядро",
        "path": "learningBack/core/sandbox.py",
        "summary": "Единственный путь модуля к данным и сети: ModuleContext проверяет разрешения и пишет журнал, сеть закрыта кроме адресов из манифеста. Вызов модуля идёт под guarded — таймаут, лимит обращений в минуту, лимит подряд идущих сбоев останавливают модуль, не ядро.",
        "api": [
          {
            "name": "SandboxError",
            "kind": "class",
            "summary": "Нарушение границы модуля"
          },
          {
            "name": "Limits",
            "kind": "type",
            "summary": "Лимиты модуля: таймаут, обращения в минуту, размер записи и ответа",
            "signature": "{ timeout_s, max_calls_per_minute, max_write_bytes, max_fetch_bytes, max_consecutive_failures }"
          },
          {
            "name": "guarded",
            "kind": "function",
            "summary": "Вызвать код модуля под охраной времени, частоты и сбоев",
            "signature": "(session, module, fn, *args, limits?, **kwargs) => Any"
          },
          {
            "name": "ModuleContext",
            "kind": "class",
            "summary": "Единственный путь модуля к данным пользователя и сети",
            "signature": "{ read(type_id, purpose), write(type_id, purpose, records), fetch(url) }"
          }
        ]
      },
      {
        "id": "learningBack/core/stt.py",
        "title": "Порт «речь в текст»",
        "layer": "ядро",
        "path": "learningBack/core/stt.py",
        "summary": "Контракт расшифровки записи ответа в текст с таймингами слов для оценки устного ответа. Провайдер — любой OpenAI-совместимый сервис; без ключа работает заглушка. Длинная, тихая или пустая запись — понятная ошибка, а не оценка из нуля слов.",
        "api": [
          {
            "name": "SpeechToText",
            "kind": "type",
            "summary": "Контракт расшифровки записи",
            "signature": "{ transcribe(audio, mime) => Transcript }"
          },
          {
            "name": "Transcript",
            "kind": "type",
            "summary": "Текст, слова с таймингами, длительность записи",
            "signature": "{ text, words, duration }"
          },
          {
            "name": "SpeechError",
            "kind": "class",
            "summary": "Запись не годится для оценки"
          },
          {
            "name": "check_transcript",
            "kind": "function",
            "summary": "Проверить длительность и число слов расшифровки",
            "signature": "(t) => Transcript | raises"
          },
          {
            "name": "get_stt",
            "kind": "function",
            "summary": "Выбрать провайдера: сервис, если настроен ключ, иначе заглушка",
            "signature": "() => SpeechToText"
          }
        ]
      },
      {
        "id": "learningBack/core/tts.py",
        "title": "Порт «текст в речь»",
        "layer": "ядро",
        "path": "learningBack/core/tts.py",
        "summary": "Контракт озвучки материалов для дрилла аудирования: текст на входе, байты аудио на выходе. Провайдер выбирается конфигурацией, как у LLM; без ключа — детерминированная заглушка без сети и расходов.",
        "api": [
          {
            "name": "TextToSpeech",
            "kind": "type",
            "summary": "Контракт озвучки текста",
            "signature": "{ mime, synthesize(text) => bytes }"
          },
          {
            "name": "MockTTS",
            "kind": "class",
            "summary": "Заглушка: детерминированные байты от текста, без воспроизведения"
          },
          {
            "name": "get_tts",
            "kind": "function",
            "summary": "Выбрать провайдера озвучки: сервис или заглушка",
            "signature": "() => TextToSpeech"
          }
        ]
      },
      {
        "id": "learningBack/core/userdata.py",
        "title": "Данные человека: хранилище с доступом по разрешениям",
        "layer": "ядро",
        "path": "learningBack/core/userdata.py",
        "summary": "Данные учащегося принадлежат платформе, а не модулям: модуль просит тип данных через этот интерфейс, ядро проверяет объявление в манифесте и разрешение человека и пишет в журнал. Отсюда же выгрузка, удаление по типу, удаление по сроку хранения и удаление аккаунта.",
        "api": [
          {
            "name": "DataType",
            "kind": "type",
            "summary": "Тип данных человека: владелец, цель, срок хранения, операции",
            "signature": "{ id, title, owner, purpose, retentionDays, read, erase, write?, expire? }"
          },
          {
            "name": "DataAccessError",
            "kind": "class",
            "summary": "Доступ модулю к данным отклонён"
          },
          {
            "name": "core_types",
            "kind": "function",
            "summary": "Типы данных, которыми владеет ядро",
            "signature": "() => list[DataType]"
          },
          {
            "name": "types",
            "kind": "function",
            "summary": "Реестр типов: ядро плюс типы включённых модулей",
            "signature": "(modules) => dict[str, DataType]"
          },
          {
            "name": "is_allowed",
            "kind": "function",
            "summary": "Разрешён ли модулю доступ к типу данных и почему",
            "signature": "(session, module, user_id, type_id, mode) => (bool, str)"
          },
          {
            "name": "read",
            "kind": "function",
            "summary": "Отдать данные модулю с проверкой разрешения и записью в журнал",
            "signature": "(session, module, user_id, type_id, purpose, registry) => Records"
          },
          {
            "name": "write",
            "kind": "function",
            "summary": "Принять данные от модуля с проверкой разрешения",
            "signature": "(session, module, user_id, type_id, purpose, records, registry) => int"
          },
          {
            "name": "set_permission",
            "kind": "function",
            "summary": "Решение человека: выдать или отозвать разрешение",
            "signature": "(session, user_id, module, type_id, mode, granted) => None"
          },
          {
            "name": "permissions",
            "kind": "function",
            "summary": "Что каждый модуль запрашивает и как это решено",
            "signature": "(session, user_id, modules) => list[dict]"
          },
          {
            "name": "access_log",
            "kind": "function",
            "summary": "Журнал обращений модулей к данным человека",
            "signature": "(session, user_id, limit?) => list[dict]"
          },
          {
            "name": "export_all",
            "kind": "function",
            "summary": "Все данные человека по реестру типов одним документом",
            "signature": "(session, user_id, registry) => dict"
          },
          {
            "name": "erase_all",
            "kind": "function",
            "summary": "Удалить данные человека по каждому типу реестра",
            "signature": "(session, user_id, registry) => dict[str, int]"
          },
          {
            "name": "purge_expired",
            "kind": "function",
            "summary": "Удалить у всех данные с истёкшим сроком хранения",
            "signature": "(session, registry, now?) => dict[str, int]"
          },
          {
            "name": "delete_account",
            "kind": "function",
            "summary": "Удалить аккаунт: данные по реестру, затем зависимые строки",
            "signature": "(session, user_id, registry) => dict"
          }
        ]
      },
      {
        "id": "learningBack/core/versioning.py",
        "title": "Версия API и совместимость клиента",
        "layer": "ядро",
        "path": "learningBack/core/versioning.py",
        "summary": "API живёт под /v1; клиент сообщает версию заголовком X-Client-Version. Устаревший клиент получает 426 с понятным кодом вместо непонятной ошибки; без заголовка запрос пропускается (web-превью, старые сборки).",
        "api": [
          {
            "name": "ClientVersionMiddleware",
            "kind": "class",
            "summary": "ASGI-мидлварь: метит ответы версией API, отсекает устаревших клиентов 426"
          },
          {
            "name": "is_outdated",
            "kind": "function",
            "summary": "Клиент старше минимально поддерживаемой версии",
            "signature": "(client_version, minimum) => bool"
          },
          {
            "name": "version_info",
            "kind": "function",
            "summary": "Версия API, сервера и минимальная версия клиента",
            "signature": "() => dict"
          },
          {
            "name": "API_VERSION",
            "kind": "const",
            "summary": "Текущая версия API",
            "signature": "\"1\""
          }
        ]
      },
      {
        "id": "learningBack/core/worker.py",
        "title": "Фоновый воркер AI-задач",
        "layer": "ядро",
        "path": "learningBack/core/worker.py",
        "summary": "В режиме jobs_mode=worker долгие задачи (распознавание речи, генерация) не обрабатываются в запросе push, а берутся отсюда: SELECT FOR UPDATE SKIP LOCKED не даёт воркерам схватить одну задачу дважды, каждая задача — своя транзакция, застрявшее в running возвращается в очередь по таймауту.",
        "api": [
          {
            "name": "claim_next",
            "kind": "function",
            "summary": "Взять следующую готовую задачу с блокировкой строки",
            "signature": "(session, now?) => Job | None"
          },
          {
            "name": "requeue_stale",
            "kind": "function",
            "summary": "Вернуть в очередь задачи, застрявшие в running",
            "signature": "(session, now?) => int"
          },
          {
            "name": "work_one",
            "kind": "function",
            "summary": "Взять и выполнить одну задачу из очереди",
            "signature": "(session, gateway, now?) => Job | None"
          },
          {
            "name": "run_loop",
            "kind": "function",
            "summary": "Работать, пока не попросят остановиться",
            "signature": "(gateway?, session_factory?, poll_seconds?, should_stop?) => int"
          }
        ]
      },
      {
        "id": "learningBack/migrations/versions/0017_client_error.py",
        "title": "Миграция: client_error",
        "layer": "миграции",
        "path": "learningBack/migrations/versions/0017_client_error.py",
        "summary": "Создаёт таблицу client_error для необработанных ошибок клиента, принимаемых POST /v1/client-errors.",
        "api": [
          {
            "name": "upgrade",
            "kind": "function",
            "summary": "Создать таблицу client_error",
            "signature": "() => None"
          },
          {
            "name": "downgrade",
            "kind": "function",
            "summary": "Откатить таблицу client_error",
            "signature": "() => None"
          }
        ]
      },
      {
        "id": "learningBack/migrations/versions/0018_module_state.py",
        "title": "Миграция: module_state",
        "layer": "миграции",
        "path": "learningBack/migrations/versions/0018_module_state.py",
        "summary": "Создаёт таблицу module_state: версия, включён, подключён — состояние модуля на работающей системе.",
        "api": [
          {
            "name": "upgrade",
            "kind": "function",
            "summary": "Создать таблицу module_state",
            "signature": "() => None"
          },
          {
            "name": "downgrade",
            "kind": "function",
            "summary": "Откатить таблицу module_state",
            "signature": "() => None"
          }
        ]
      },
      {
        "id": "learningBack/migrations/versions/0019_goal_intake.py",
        "title": "Миграция: goal_intake",
        "layer": "миграции",
        "path": "learningBack/migrations/versions/0019_goal_intake.py",
        "summary": "Создаёт таблицу goal_intake: подтверждённый итог диалога постановки цели, по одной записи на человека и область.",
        "api": [
          {
            "name": "upgrade",
            "kind": "function",
            "summary": "Создать таблицу goal_intake",
            "signature": "() => None"
          },
          {
            "name": "downgrade",
            "kind": "function",
            "summary": "Откатить таблицу goal_intake",
            "signature": "() => None"
          }
        ]
      },
      {
        "id": "learningBack/migrations/versions/0020_domain_graph.py",
        "title": "Миграция: domain_graph",
        "layer": "миграции",
        "path": "learningBack/migrations/versions/0020_domain_graph.py",
        "summary": "Создаёт таблицы domain, domain_alias, domain_edge — реестр базовых областей и связи «нужно знать до» между ними.",
        "api": [
          {
            "name": "upgrade",
            "kind": "function",
            "summary": "Создать таблицы domain, domain_alias, domain_edge",
            "signature": "() => None"
          },
          {
            "name": "downgrade",
            "kind": "function",
            "summary": "Откатить таблицы domain, domain_alias, domain_edge",
            "signature": "() => None"
          }
        ]
      },
      {
        "id": "learningBack/migrations/versions/0021_concept_link.py",
        "title": "Миграция: concept_link",
        "layer": "миграции",
        "path": "learningBack/migrations/versions/0021_concept_link.py",
        "summary": "Создаёт таблицу concept_link: предпосылки между понятиями разных областей со ступенью освоения.",
        "api": [
          {
            "name": "upgrade",
            "kind": "function",
            "summary": "Создать таблицу concept_link",
            "signature": "() => None"
          },
          {
            "name": "downgrade",
            "kind": "function",
            "summary": "Откатить таблицу concept_link",
            "signature": "() => None"
          }
        ]
      },
      {
        "id": "learningBack/migrations/versions/0022_user_data_access.py",
        "title": "Миграция: user_data_access",
        "layer": "миграции",
        "path": "learningBack/migrations/versions/0022_user_data_access.py",
        "summary": "Создаёт таблицы data_permission и data_access_log: разрешения модулей на данные человека и журнал обращений.",
        "api": [
          {
            "name": "upgrade",
            "kind": "function",
            "summary": "Создать таблицы data_permission, data_access_log",
            "signature": "() => None"
          },
          {
            "name": "downgrade",
            "kind": "function",
            "summary": "Откатить таблицы data_permission, data_access_log",
            "signature": "() => None"
          }
        ]
      },
      {
        "id": "learningBack/migrations/versions/0023_module_consent.py",
        "title": "Миграция: module_consent",
        "layer": "миграции",
        "path": "learningBack/migrations/versions/0023_module_consent.py",
        "summary": "Добавляет колонку approved в module_state: согласие на запросы и сеть модуля, нужное заново при расширении разрешений.",
        "api": [
          {
            "name": "upgrade",
            "kind": "function",
            "summary": "Добавить колонку module_state.approved",
            "signature": "() => None"
          },
          {
            "name": "downgrade",
            "kind": "function",
            "summary": "Убрать колонку module_state.approved",
            "signature": "() => None"
          }
        ]
      },
      {
        "id": "learningBack/migrations/versions/0024_policy_consent.py",
        "title": "Миграция: policy_consent",
        "layer": "миграции",
        "path": "learningBack/migrations/versions/0024_policy_consent.py",
        "summary": "Добавляет в user колонки policy_version и policy_accepted_at: версия политики данных, принятая при регистрации.",
        "api": [
          {
            "name": "upgrade",
            "kind": "function",
            "summary": "Добавить колонки user.policy_version, user.policy_accepted_at",
            "signature": "() => None"
          },
          {
            "name": "downgrade",
            "kind": "function",
            "summary": "Убрать колонки user.policy_version, user.policy_accepted_at",
            "signature": "() => None"
          }
        ]
      },
      {
        "id": "learningBack/modules/knowledge/api.py",
        "title": "Публичный интерфейс графа знаний",
        "layer": "ядро",
        "path": "learningBack/modules/knowledge/api.py",
        "summary": "Всё, что остальным модулям и ядру можно знать о графе знаний: прочитать узел и связи, найти границу знаний, получить и записать освоенность через единый формат свидетельства, подписаться на изменение узла. Внутренности графа (COW, формула освоенности) снаружи не видны.",
        "api": [
          {
            "name": "get_node",
            "kind": "function",
            "summary": "Узел с теорией: канонический с правкой пользователя или личный",
            "signature": "(session, user_id, node_id) => dict | None"
          },
          {
            "name": "get_edges",
            "kind": "function",
            "summary": "Связи узла в графе пользователя",
            "signature": "(session, user_id, domain, node_id) => list[dict]"
          },
          {
            "name": "frontier",
            "kind": "function",
            "summary": "Граница знаний: узлы, готовые к освоению",
            "signature": "(session, user_id, domain) => list[dict]"
          },
          {
            "name": "get_mastery",
            "kind": "function",
            "summary": "Освоенность по узлам области",
            "signature": "(session, user_id, domain) => dict"
          },
          {
            "name": "record_evidence",
            "kind": "function",
            "summary": "Записать свидетельство и вернуть новое состояние узла",
            "signature": "(session, user_id, domain, evidence) => MasteryState"
          }
        ]
      },
      {
        "id": "learningBack/modules/knowledge/chain_placement.py",
        "title": "Проверка по цепочке базовых областей",
        "layer": "ядро",
        "path": "learningBack/modules/knowledge/chain_placement.py",
        "summary": "Проверяет уровень по цепочке базовых областей сверху вниз: освоенное верхнее понятие снимает проверку того, что лежит под ним, поэтому взрослый и второклассник не получают одинаково длинный путь. Задания и оценка ответов те же, что у плейсмента одной области.",
        "api": [
          {
            "name": "needed_nodes",
            "kind": "function",
            "summary": "Понятия других областей, нужные для цели на ступени",
            "signature": "(session, domain, target_bloom) => dict[UUID, str]"
          },
          {
            "name": "classify",
            "kind": "function",
            "summary": "Состояние каждого нужного понятия: освоено, снято, не освоено",
            "signature": "(session, user_id, needed) => (concepts, status, states)"
          },
          {
            "name": "implied_known",
            "kind": "function",
            "summary": "Понятия, которые курсу проверять не нужно",
            "signature": "(session, user_id, needed) => set[UUID]"
          },
          {
            "name": "chain_plan",
            "kind": "function",
            "summary": "Области цепочки сверху вниз и состояние их понятий",
            "signature": "(session, user_id, domain, target_bloom) => list[dict]"
          },
          {
            "name": "next_chain_probe",
            "kind": "function",
            "summary": "Следующий зонд по цепочке: самая сложная область с непроверенным понятием",
            "signature": "(session, user_id, domain, target_bloom) => dict | raises NoProbeAvailable"
          }
        ]
      },
      {
        "id": "learningBack/modules/knowledge/cross_links.py",
        "title": "Межобластные предпосылки понятий",
        "layer": "ядро",
        "path": "learningBack/modules/knowledge/cross_links.py",
        "summary": "Связи «нужно знать, чтобы освоить» между понятиями разных областей со ступенью освоения, с которой обязательны. Курс подтягивает из базовых областей не всю область, а только нужных предков конкретных понятий на нужной ступени.",
        "api": [
          {
            "name": "LinkError",
            "kind": "class",
            "summary": "Межобластная связь отклонена"
          },
          {
            "name": "add_link",
            "kind": "function",
            "summary": "Связь «from_id нужно знать для to_id до ступени bloom»",
            "signature": "(session, from_id, to_id, bloom) => ConceptLink"
          },
          {
            "name": "links_into",
            "kind": "function",
            "summary": "Связи, ведущие в понятие",
            "signature": "(session, concept_id) => list[ConceptLink]"
          },
          {
            "name": "required_ancestors",
            "kind": "function",
            "summary": "Предки из других областей, нужные для понятий на ступени",
            "signature": "(session, concept_ids, target_bloom) => dict[UUID, str]"
          }
        ]
      },
      {
        "id": "learningBack/modules/knowledge/cross_links_api.py",
        "title": "API межобластных связей и цепочки плейсмента",
        "layer": "маршруты",
        "path": "learningBack/modules/knowledge/cross_links_api.py",
        "summary": "Эндпоинты для связей между понятиями разных областей, проверки освоенности по цепочке базовых областей и объёма пути под целью. Менять связи может куратор, читать и проверять — любой вошедший.",
        "api": [
          {
            "name": "add_concept_link",
            "kind": "function",
            "summary": "POST /concept-links — предпосылка из другой области",
            "signature": "(body, session) => dict"
          },
          {
            "name": "concept_links",
            "kind": "function",
            "summary": "GET /concept-links/{id} — что нужно знать из других областей",
            "signature": "(concept_id, session) => list[dict]"
          },
          {
            "name": "placement_chain",
            "kind": "function",
            "summary": "GET /placement/{domain}/chain — состояние базовых областей под целью",
            "signature": "(domain, user, session, target?) => list[dict]"
          },
          {
            "name": "placement_chain_probe",
            "kind": "function",
            "summary": "GET /placement/{domain}/chain-probe — следующий зонд цепочки",
            "signature": "(domain, user, session, target?) => dict"
          },
          {
            "name": "goal_volume",
            "kind": "function",
            "summary": "GET /goal/{domain}/volume — объём пути под целью",
            "signature": "(domain, session, target?) => dict"
          }
        ]
      },
      {
        "id": "learningBack/modules/knowledge/domains.py",
        "title": "Граф областей и уровни примитивности",
        "layer": "ядро",
        "path": "learningBack/modules/knowledge/domains.py",
        "summary": "Области становятся данными: реестр по устойчивому ключу с алиасами, связи «нужно знать до» без циклов, нижняя опора без предпосылок. Уровень примитивности не назначается руками — это вычисляемая глубина области в графе.",
        "api": [
          {
            "name": "DomainError",
            "kind": "class",
            "summary": "Нарушено правило графа областей"
          },
          {
            "name": "normalize",
            "kind": "function",
            "summary": "Имя области к устойчивому ключу для сравнения",
            "signature": "(name) => str"
          },
          {
            "name": "resolve",
            "kind": "function",
            "summary": "Найти область по ключу, названию или алиасу",
            "signature": "(session, name) => Domain | None"
          },
          {
            "name": "register",
            "kind": "function",
            "summary": "Завести область или вернуть существующую под алиасом",
            "signature": "(session, title, aliases?, foundation?) => (Domain, bool)"
          },
          {
            "name": "add_prereq",
            "kind": "function",
            "summary": "Связь «нужно знать до» между областями без циклов",
            "signature": "(session, domain_key, prereq_key) => DomainEdge"
          },
          {
            "name": "levels",
            "kind": "function",
            "summary": "Уровень примитивности каждой области: глубина в графе",
            "signature": "(session) => dict[str, int]"
          },
          {
            "name": "chain",
            "kind": "function",
            "summary": "Всё, что нужно знать до области, от примитивного к ближайшему",
            "signature": "(session, key) => list[dict]"
          },
          {
            "name": "listing",
            "kind": "function",
            "summary": "Все области с уровнем, предпосылками и алиасами",
            "signature": "(session) => list[dict]"
          }
        ]
      },
      {
        "id": "learningBack/modules/knowledge/domains_api.py",
        "title": "API графа областей",
        "layer": "маршруты",
        "path": "learningBack/modules/knowledge/domains_api.py",
        "summary": "Эндпоинты графа областей: читать может любой вошедший, заводить область и связи — куратор, так как канон общий.",
        "api": [
          {
            "name": "list_domains",
            "kind": "function",
            "summary": "GET /domains",
            "signature": "(session) => list[dict]"
          },
          {
            "name": "register_domain",
            "kind": "function",
            "summary": "POST /domains",
            "signature": "(body, session) => dict"
          },
          {
            "name": "add_domain_prereq",
            "kind": "function",
            "summary": "POST /domains/{key}/prereqs",
            "signature": "(key, body, session) => dict"
          },
          {
            "name": "domain_chain",
            "kind": "function",
            "summary": "GET /domains/{key}/chain",
            "signature": "(key, session) => dict"
          }
        ]
      }
    ],
    "imports": [
      {
        "from": "learningBack/core/mail.py",
        "to": "learningBack/core/config.py",
        "evidence": {
          "path": "learningBack/core/mail.py",
          "line": 17,
          "fragment": "from core.config import settings"
        }
      },
      {
        "from": "learningBack/core/monitoring.py",
        "to": "learningBack/core/config.py",
        "evidence": {
          "path": "learningBack/core/monitoring.py",
          "line": 18,
          "fragment": "from core.config import settings"
        }
      },
      {
        "from": "learningBack/core/monitoring.py",
        "to": "learningBack/core/models.py",
        "evidence": {
          "path": "learningBack/core/monitoring.py",
          "line": 19,
          "fragment": "from core.models import ClientError, Job, LlmUsage"
        }
      },
      {
        "from": "learningBack/core/routers/methods.py",
        "to": "learningBack/core/modules.py",
        "evidence": {
          "path": "learningBack/core/routers/methods.py",
          "line": 8,
          "fragment": "from core import modules"
        }
      },
      {
        "from": "learningBack/core/routers/methods.py",
        "to": "learningBack/core/deps.py",
        "evidence": {
          "path": "learningBack/core/routers/methods.py",
          "line": 9,
          "fragment": "from core.deps import CurrentUser, SessionDep"
        }
      },
      {
        "from": "learningBack/core/routers/methods.py",
        "to": "learningBack/core/evidence.py",
        "evidence": {
          "path": "learningBack/core/routers/methods.py",
          "line": 10,
          "fragment": "from core.evidence import Evidence, dispatch"
        }
      },
      {
        "from": "learningBack/core/routers/methods.py",
        "to": "learningBack/core/methods.py",
        "evidence": {
          "path": "learningBack/core/routers/methods.py",
          "line": 11,
          "fragment": "from core.methods import PREFERENCE_KEY, PURPOSES, preferences"
        }
      },
      {
        "from": "learningBack/core/routers/modules_admin.py",
        "to": "learningBack/core/modules.py",
        "evidence": {
          "path": "learningBack/core/routers/modules_admin.py",
          "line": 6,
          "fragment": "from core import modules"
        }
      },
      {
        "from": "learningBack/core/routers/modules_admin.py",
        "to": "learningBack/core/deps.py",
        "evidence": {
          "path": "learningBack/core/routers/modules_admin.py",
          "line": 7,
          "fragment": "from core.deps import CurrentSuperuser, SessionDep"
        }
      },
      {
        "from": "learningBack/core/routers/monitoring.py",
        "to": "learningBack/core/monitoring.py",
        "evidence": {
          "path": "learningBack/core/routers/monitoring.py",
          "line": 8,
          "fragment": "from core import monitoring"
        }
      },
      {
        "from": "learningBack/core/routers/monitoring.py",
        "to": "learningBack/core/deps.py",
        "evidence": {
          "path": "learningBack/core/routers/monitoring.py",
          "line": 9,
          "fragment": "from core.deps import CurrentSuperuser, CurrentUser, SessionDep"
        }
      },
      {
        "from": "learningBack/core/routers/monitoring.py",
        "to": "learningBack/core/models.py",
        "evidence": {
          "path": "learningBack/core/routers/monitoring.py",
          "line": 10,
          "fragment": "from core.models import ClientError"
        }
      },
      {
        "from": "learningBack/core/routers/monitoring.py",
        "to": "learningBack/core/ratelimit.py",
        "evidence": {
          "path": "learningBack/core/routers/monitoring.py",
          "line": 11,
          "fragment": "from core.ratelimit import SlidingWindowLimiter"
        }
      },
      {
        "from": "learningBack/core/routers/userdata.py",
        "to": "learningBack/core/modules.py",
        "evidence": {
          "path": "learningBack/core/routers/userdata.py",
          "line": 6,
          "fragment": "from core import modules, userdata"
        }
      },
      {
        "from": "learningBack/core/routers/userdata.py",
        "to": "learningBack/core/userdata.py",
        "evidence": {
          "path": "learningBack/core/routers/userdata.py",
          "line": 6,
          "fragment": "from core import modules, userdata"
        }
      },
      {
        "from": "learningBack/core/routers/userdata.py",
        "to": "learningBack/core/deps.py",
        "evidence": {
          "path": "learningBack/core/routers/userdata.py",
          "line": 7,
          "fragment": "from core.deps import CurrentSuperuser, CurrentUser, SessionDep"
        }
      },
      {
        "from": "learningBack/core/routers/userdata.py",
        "to": "learningBack/core/security.py",
        "evidence": {
          "path": "learningBack/core/routers/userdata.py",
          "line": 8,
          "fragment": "from core.security import verify_password"
        }
      },
      {
        "from": "learningBack/core/sandbox.py",
        "to": "learningBack/core/modules.py",
        "evidence": {
          "path": "learningBack/core/sandbox.py",
          "line": 28,
          "fragment": "from core import modules, userdata"
        }
      },
      {
        "from": "learningBack/core/sandbox.py",
        "to": "learningBack/core/userdata.py",
        "evidence": {
          "path": "learningBack/core/sandbox.py",
          "line": 28,
          "fragment": "from core import modules, userdata"
        }
      },
      {
        "from": "learningBack/core/stt.py",
        "to": "learningBack/core/ai_gateway/base.py",
        "evidence": {
          "path": "learningBack/core/stt.py",
          "line": 16,
          "fragment": "from core.ai_gateway.base import ProviderError"
        }
      },
      {
        "from": "learningBack/core/stt.py",
        "to": "learningBack/core/config.py",
        "evidence": {
          "path": "learningBack/core/stt.py",
          "line": 17,
          "fragment": "from core.config import settings"
        }
      },
      {
        "from": "learningBack/core/tts.py",
        "to": "learningBack/core/ai_gateway/base.py",
        "evidence": {
          "path": "learningBack/core/tts.py",
          "line": 16,
          "fragment": "from core.ai_gateway.base import ProviderError"
        }
      },
      {
        "from": "learningBack/core/tts.py",
        "to": "learningBack/core/config.py",
        "evidence": {
          "path": "learningBack/core/tts.py",
          "line": 17,
          "fragment": "from core.config import settings"
        }
      },
      {
        "from": "learningBack/core/userdata.py",
        "to": "learningBack/core/models.py",
        "evidence": {
          "path": "learningBack/core/userdata.py",
          "line": 23,
          "fragment": "from core.models import ("
        }
      },
      {
        "from": "learningBack/core/userdata.py",
        "to": "learningBack/core/db.py",
        "evidence": {
          "path": "learningBack/core/userdata.py",
          "line": 402,
          "fragment": "from core.db import Base"
        }
      },
      {
        "from": "learningBack/core/versioning.py",
        "to": "learningBack/core/config.py",
        "evidence": {
          "path": "learningBack/core/versioning.py",
          "line": 17,
          "fragment": "from core.config import settings"
        }
      },
      {
        "from": "learningBack/core/worker.py",
        "to": "learningBack/core/usage.py",
        "evidence": {
          "path": "learningBack/core/worker.py",
          "line": 22,
          "fragment": "from core import usage"
        }
      },
      {
        "from": "learningBack/core/worker.py",
        "to": "learningBack/core/ai_gateway/__init__.py",
        "evidence": {
          "path": "learningBack/core/worker.py",
          "line": 23,
          "fragment": "from core.ai_gateway import AIGateway, get_ai_gateway"
        }
      },
      {
        "from": "learningBack/core/worker.py",
        "to": "learningBack/core/config.py",
        "evidence": {
          "path": "learningBack/core/worker.py",
          "line": 24,
          "fragment": "from core.config import settings"
        }
      },
      {
        "from": "learningBack/core/worker.py",
        "to": "learningBack/core/db.py",
        "evidence": {
          "path": "learningBack/core/worker.py",
          "line": 25,
          "fragment": "from core.db import SessionLocal"
        }
      },
      {
        "from": "learningBack/core/worker.py",
        "to": "learningBack/core/jobs.py",
        "evidence": {
          "path": "learningBack/core/worker.py",
          "line": 26,
          "fragment": "from core.jobs import process_job"
        }
      },
      {
        "from": "learningBack/core/worker.py",
        "to": "learningBack/core/models.py",
        "evidence": {
          "path": "learningBack/core/worker.py",
          "line": 27,
          "fragment": "from core.models import Job"
        }
      },
      {
        "from": "learningBack/modules/knowledge/api.py",
        "to": "learningBack/core/evidence.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/api.py",
          "line": 18,
          "fragment": "from core.evidence import Evidence"
        }
      },
      {
        "from": "learningBack/modules/knowledge/api.py",
        "to": "learningBack/modules/knowledge/cow.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/api.py",
          "line": 20,
          "fragment": "from modules.knowledge.cow import effective_graph, resolve_node"
        }
      },
      {
        "from": "learningBack/modules/knowledge/api.py",
        "to": "learningBack/modules/knowledge/events.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/api.py",
          "line": 21,
          "fragment": "from modules.knowledge.events import NodeChanged, subscribe, unsubscribe"
        }
      },
      {
        "from": "learningBack/modules/knowledge/api.py",
        "to": "learningBack/modules/knowledge/mastery.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/api.py",
          "line": 22,
          "fragment": "from modules.knowledge.mastery import MasteryState, load_map"
        }
      },
      {
        "from": "learningBack/modules/knowledge/api.py",
        "to": "learningBack/modules/knowledge/models.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/api.py",
          "line": 23,
          "fragment": "from modules.knowledge.models import Concept, UserConcept"
        }
      },
      {
        "from": "learningBack/modules/knowledge/api.py",
        "to": "learningBack/modules/knowledge/placement.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/api.py",
          "line": 24,
          "fragment": "from modules.knowledge.placement import placement_map, record_answer"
        }
      },
      {
        "from": "learningBack/modules/knowledge/chain_placement.py",
        "to": "learningBack/modules/knowledge/cross_links.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/chain_placement.py",
          "line": 17,
          "fragment": "from modules.knowledge import cross_links, domains"
        }
      },
      {
        "from": "learningBack/modules/knowledge/chain_placement.py",
        "to": "learningBack/modules/knowledge/domains.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/chain_placement.py",
          "line": 17,
          "fragment": "from modules.knowledge import cross_links, domains"
        }
      },
      {
        "from": "learningBack/modules/knowledge/chain_placement.py",
        "to": "learningBack/modules/knowledge/assessment_store.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/chain_placement.py",
          "line": 18,
          "fragment": "from modules.knowledge.assessment_store import get_or_generate"
        }
      },
      {
        "from": "learningBack/modules/knowledge/chain_placement.py",
        "to": "learningBack/modules/knowledge/assessment.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/chain_placement.py",
          "line": 19,
          "fragment": "from modules.knowledge.assessment import NotGroundable"
        }
      },
      {
        "from": "learningBack/modules/knowledge/chain_placement.py",
        "to": "learningBack/modules/knowledge/mastery.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/chain_placement.py",
          "line": 20,
          "fragment": "from modules.knowledge.mastery import KNOWN_THRESHOLD, MasteryState, load_map"
        }
      },
      {
        "from": "learningBack/modules/knowledge/chain_placement.py",
        "to": "learningBack/modules/knowledge/models.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/chain_placement.py",
          "line": 21,
          "fragment": "from modules.knowledge.models import Concept"
        }
      },
      {
        "from": "learningBack/modules/knowledge/chain_placement.py",
        "to": "learningBack/modules/knowledge/placement.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/chain_placement.py",
          "line": 22,
          "fragment": "from modules.knowledge.placement import ("
        }
      },
      {
        "from": "learningBack/modules/knowledge/cross_links.py",
        "to": "learningBack/modules/knowledge/domains.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/cross_links.py",
          "line": 15,
          "fragment": "from modules.knowledge import domains"
        }
      },
      {
        "from": "learningBack/modules/knowledge/cross_links.py",
        "to": "learningBack/modules/knowledge/assessment.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/cross_links.py",
          "line": 16,
          "fragment": "from modules.knowledge.assessment import BLOOM_LEVELS"
        }
      },
      {
        "from": "learningBack/modules/knowledge/cross_links.py",
        "to": "learningBack/modules/knowledge/mastery.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/cross_links.py",
          "line": 17,
          "fragment": "from modules.knowledge.mastery import prerequisite_map"
        }
      },
      {
        "from": "learningBack/modules/knowledge/cross_links.py",
        "to": "learningBack/modules/knowledge/models.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/cross_links.py",
          "line": 18,
          "fragment": "from modules.knowledge.models import Concept, ConceptLink, Domain"
        }
      },
      {
        "from": "learningBack/modules/knowledge/cross_links_api.py",
        "to": "learningBack/core/deps.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/cross_links_api.py",
          "line": 8,
          "fragment": "from core.deps import CurrentSuperuser, CurrentUser, SessionDep"
        }
      },
      {
        "from": "learningBack/modules/knowledge/cross_links_api.py",
        "to": "learningBack/modules/knowledge/chain_placement.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/cross_links_api.py",
          "line": 9,
          "fragment": "from modules.knowledge import chain_placement, cross_links, path_volume"
        }
      },
      {
        "from": "learningBack/modules/knowledge/cross_links_api.py",
        "to": "learningBack/modules/knowledge/cross_links.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/cross_links_api.py",
          "line": 9,
          "fragment": "from modules.knowledge import chain_placement, cross_links, path_volume"
        }
      },
      {
        "from": "learningBack/modules/knowledge/cross_links_api.py",
        "to": "learningBack/modules/knowledge/path_volume.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/cross_links_api.py",
          "line": 9,
          "fragment": "from modules.knowledge import chain_placement, cross_links, path_volume"
        }
      },
      {
        "from": "learningBack/modules/knowledge/cross_links_api.py",
        "to": "learningBack/modules/knowledge/placement.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/cross_links_api.py",
          "line": 10,
          "fragment": "from modules.knowledge.placement import NoProbeAvailable"
        }
      },
      {
        "from": "learningBack/modules/knowledge/domains.py",
        "to": "learningBack/modules/knowledge/models.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/domains.py",
          "line": 21,
          "fragment": "from modules.knowledge.models import Domain, DomainAlias, DomainEdge"
        }
      },
      {
        "from": "learningBack/modules/knowledge/domains_api.py",
        "to": "learningBack/core/deps.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/domains_api.py",
          "line": 6,
          "fragment": "from core.deps import CurrentSuperuser, CurrentUser, SessionDep"
        }
      },
      {
        "from": "learningBack/modules/knowledge/domains_api.py",
        "to": "learningBack/modules/knowledge/domains.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/domains_api.py",
          "line": 7,
          "fragment": "from modules.knowledge import domains"
        }
      },
      {
        "from": "learningBack/core/app.py",
        "to": "learningBack/core/routers/methods.py",
        "evidence": {
          "path": "learningBack/core/app.py",
          "line": 18,
          "fragment": "from core.routers import methods as methods_router"
        }
      },
      {
        "from": "learningBack/core/app.py",
        "to": "learningBack/core/routers/modules_admin.py",
        "evidence": {
          "path": "learningBack/core/app.py",
          "line": 19,
          "fragment": "from core.routers import modules_admin"
        }
      },
      {
        "from": "learningBack/core/app.py",
        "to": "learningBack/core/routers/userdata.py",
        "evidence": {
          "path": "learningBack/core/app.py",
          "line": 20,
          "fragment": "from core.routers import userdata as userdata_router"
        }
      },
      {
        "from": "learningBack/core/app.py",
        "to": "learningBack/core/routers/monitoring.py",
        "evidence": {
          "path": "learningBack/core/app.py",
          "line": 21,
          "fragment": "from core.routers import monitoring as monitoring_router"
        }
      },
      {
        "from": "learningBack/core/app.py",
        "to": "learningBack/core/versioning.py",
        "evidence": {
          "path": "learningBack/core/app.py",
          "line": 16,
          "fragment": "from core.versioning import ClientVersionMiddleware, version_info"
        }
      },
      {
        "from": "learningBack/core/modules.py",
        "to": "learningBack/core/manifest.py",
        "evidence": {
          "path": "learningBack/core/modules.py",
          "line": 20,
          "fragment": "from core.manifest import ManifestError, ModuleManifest, check_manifest, check_set"
        }
      },
      {
        "from": "learningBack/core/modules.py",
        "to": "learningBack/core/methods.py",
        "evidence": {
          "path": "learningBack/core/modules.py",
          "line": 21,
          "fragment": "from core.methods import APPLY, MethodError, StudyMethod, check_methods, for_purpose"
        }
      },
      {
        "from": "learningBack/modules/knowledge/__init__.py",
        "to": "learningBack/core/manifest.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/__init__.py",
          "line": 13,
          "fragment": "from core.manifest import ModuleManifest"
        }
      },
      {
        "from": "learningBack/modules/knowledge/__init__.py",
        "to": "learningBack/core/methods.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/__init__.py",
          "line": 14,
          "fragment": "from core.methods import APPLY, CONTRAST, READ, RECALL, StudyMethod"
        }
      },
      {
        "from": "learningBack/modules/knowledge/__init__.py",
        "to": "learningBack/modules/knowledge/api.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/__init__.py",
          "line": 57,
          "fragment": "from modules.knowledge import api"
        }
      },
      {
        "from": "learningBack/modules/knowledge/__init__.py",
        "to": "learningBack/core/userdata.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/__init__.py",
          "line": 78,
          "fragment": "from core.userdata import DataType, model_type"
        }
      },
      {
        "from": "learningBack/modules/knowledge/router.py",
        "to": "learningBack/modules/knowledge/cross_links_api.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/router.py",
          "line": 16,
          "fragment": "from modules.knowledge.cross_links_api import router as _cross_links_router"
        }
      },
      {
        "from": "learningBack/modules/knowledge/router.py",
        "to": "learningBack/modules/knowledge/domains_api.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/router.py",
          "line": 17,
          "fragment": "from modules.knowledge.domains_api import router as _domains_router"
        }
      },
      {
        "from": "learningBack/core/routers/auth.py",
        "to": "learningBack/core/mail.py",
        "evidence": {
          "path": "learningBack/core/routers/auth.py",
          "line": 11,
          "fragment": "from core.mail import reset_code_message, send_safely"
        }
      }
    ],
    "groups": [
      {
        "id": "study-methods-contract",
        "title": "Контракт способа изучения",
        "summary": "Общий способ, которым модуль объявляет способ изучения шага курса и отдаёт его через API выбора и смены.",
        "modules": [
          "learningBack/core/methods.py",
          "learningBack/core/routers/methods.py"
        ],
        "capability": "method-contract"
      },
      {
        "id": "mastery-evidence-dispatch",
        "title": "Свидетельство об освоении",
        "summary": "Единый формат результата ответа, не зависящий от способа запоминания, и его доставка модулям графа.",
        "modules": [
          "learningBack/core/evidence.py"
        ],
        "capability": "mastery-evidence"
      },
      {
        "id": "module-lifecycle",
        "title": "Жизненный цикл и манифест модуля",
        "summary": "Контракт манифеста и администраторские действия над подключённым модулем: включить, согласиться на расширение, отключить, удалить данные.",
        "modules": [
          "learningBack/core/manifest.py",
          "learningBack/core/routers/modules_admin.py"
        ],
        "capability": "module-registry"
      },
      {
        "id": "module-sandbox",
        "title": "Изоляция исполнения модуля",
        "summary": "Единственный путь модуля к данным и сети с лимитами по времени, частоте и сбоям.",
        "modules": [
          "learningBack/core/sandbox.py"
        ],
        "capability": "isolation"
      },
      {
        "id": "user-data-privacy",
        "title": "«Мои данные»: доступ, выгрузка, удаление",
        "summary": "Реестр типов данных человека с разрешениями модулям, журналом доступа, выгрузкой, удалением по типу, по сроку хранения и удалением аккаунта.",
        "modules": [
          "learningBack/core/userdata.py",
          "learningBack/core/routers/userdata.py"
        ],
        "capability": "my-data"
      },
      {
        "id": "platform-ops",
        "title": "Платформа: мониторинг, версия, воркер, почта",
        "summary": "Эксплуатационные механизмы: сводка здоровья и ошибки клиента, совместимость версии клиента, фоновый воркер AI-задач, отправка писем восстановления пароля.",
        "modules": [
          "learningBack/core/monitoring.py",
          "learningBack/core/routers/monitoring.py",
          "learningBack/core/versioning.py",
          "learningBack/core/worker.py",
          "learningBack/core/mail.py"
        ],
        "capability": "platform-release"
      },
      {
        "id": "speech-to-text",
        "title": "Расшифровка устного ответа",
        "summary": "Порт распознавания речи для оценки устного ответа по таймингам слов.",
        "modules": [
          "learningBack/core/stt.py"
        ],
        "capability": "speaking"
      },
      {
        "id": "text-to-speech",
        "title": "Озвучка для аудирования",
        "summary": "Порт синтеза речи для дрилла аудирования.",
        "modules": [
          "learningBack/core/tts.py"
        ],
        "capability": "reception-drills"
      },
      {
        "id": "domain-graph-structure",
        "title": "Граф областей",
        "summary": "Реестр базовых областей, связи «нужно знать до» и вычисляемый уровень примитивности, с API для чтения и курирования.",
        "modules": [
          "learningBack/modules/knowledge/domains.py",
          "learningBack/modules/knowledge/domains_api.py"
        ],
        "capability": "domain-graph"
      },
      {
        "id": "cross-domain-prereqs",
        "title": "Межобластные предпосылки",
        "summary": "Связи между понятиями разных областей со ступенью освоения, нужные курсу, чтобы подтягивать только нужных предков.",
        "modules": [
          "learningBack/modules/knowledge/cross_links.py"
        ],
        "capability": "cross-domain-links"
      },
      {
        "id": "chain-placement",
        "title": "Проверка по цепочке базовых областей",
        "summary": "Выбор, о чём спрашивать при проверке базовых областей сверху вниз, и API плейсмента по цепочке и объёма пути.",
        "modules": [
          "learningBack/modules/knowledge/chain_placement.py",
          "learningBack/modules/knowledge/cross_links_api.py"
        ],
        "capability": "cross-domain-placement"
      }
    ]
  }
}
```

```docdd-dataflow
{
  "added": {
    "sources": [
      {
        "id": "mem-sandbox-budget",
        "kind": "memory",
        "where": "core.sandbox._calls, core.sandbox._failures",
        "title": "Счётчики вызовов и сбоев модуля (in-process)"
      }
    ],
    "flows": [
      {
        "from": "learningBack/core/monitoring.py",
        "to": "db-postgres",
        "direction": "read",
        "evidence": {
          "path": "learningBack/core/monitoring.py",
          "line": 34,
          "fragment": "session.query(Job.status, func.count())"
        }
      },
      {
        "from": "learningBack/core/userdata.py",
        "to": "db-postgres",
        "direction": "both",
        "evidence": {
          "path": "learningBack/core/userdata.py",
          "line": 102,
          "fragment": "return [row_dict(r) for r in session.query(model).filter(column == user_id)]"
        }
      },
      {
        "from": "learningBack/core/worker.py",
        "to": "db-postgres",
        "direction": "both",
        "evidence": {
          "path": "learningBack/core/worker.py",
          "line": 36,
          "fragment": "session.query(Job)"
        }
      },
      {
        "from": "learningBack/core/routers/methods.py",
        "to": "db-postgres",
        "direction": "write",
        "evidence": {
          "path": "learningBack/core/routers/methods.py",
          "line": 46,
          "fragment": "session.commit()"
        }
      },
      {
        "from": "learningBack/core/routers/monitoring.py",
        "to": "db-postgres",
        "direction": "write",
        "evidence": {
          "path": "learningBack/core/routers/monitoring.py",
          "line": 48,
          "fragment": "session.commit()"
        }
      },
      {
        "from": "learningBack/core/routers/modules_admin.py",
        "to": "db-postgres",
        "direction": "write",
        "evidence": {
          "path": "learningBack/core/routers/modules_admin.py",
          "line": 40,
          "fragment": "session.commit()"
        }
      },
      {
        "from": "learningBack/core/routers/userdata.py",
        "to": "db-postgres",
        "direction": "write",
        "evidence": {
          "path": "learningBack/core/routers/userdata.py",
          "line": 54,
          "fragment": "session.commit()"
        }
      },
      {
        "from": "learningBack/core/routers/monitoring.py",
        "to": "mem-ratelimit",
        "direction": "both",
        "evidence": {
          "path": "learningBack/core/routers/monitoring.py",
          "line": 35,
          "fragment": "_limiter.allow(str(user.id), CLIENT_ERROR_LIMIT, CLIENT_ERROR_WINDOW_SECONDS)"
        }
      },
      {
        "from": "learningBack/core/sandbox.py",
        "to": "mem-sandbox-budget",
        "direction": "both",
        "evidence": {
          "path": "learningBack/core/sandbox.py",
          "line": 71,
          "fragment": "window = _calls[module_id]"
        }
      },
      {
        "from": "learningBack/core/stt.py",
        "to": "http-llm-provider",
        "direction": "both",
        "evidence": {
          "path": "learningBack/core/stt.py",
          "line": 75,
          "fragment": "base_url=settings.llm_base_url,"
        }
      },
      {
        "from": "learningBack/core/tts.py",
        "to": "http-llm-provider",
        "direction": "both",
        "evidence": {
          "path": "learningBack/core/tts.py",
          "line": 42,
          "fragment": "base_url=settings.llm_base_url,"
        }
      },
      {
        "from": "learningBack/modules/knowledge/api.py",
        "to": "db-postgres",
        "direction": "read",
        "evidence": {
          "path": "learningBack/modules/knowledge/api.py",
          "line": 41,
          "fragment": "concept = session.get(Concept, node_id)"
        }
      },
      {
        "from": "learningBack/modules/knowledge/domains.py",
        "to": "db-postgres",
        "direction": "both",
        "evidence": {
          "path": "learningBack/modules/knowledge/domains.py",
          "line": 42,
          "fragment": "direct = session.get(Domain, norm)"
        }
      },
      {
        "from": "learningBack/modules/knowledge/cross_links.py",
        "to": "db-postgres",
        "direction": "both",
        "evidence": {
          "path": "learningBack/modules/knowledge/cross_links.py",
          "line": 48,
          "fragment": "for link in session.query(ConceptLink).all():"
        }
      },
      {
        "from": "learningBack/modules/knowledge/chain_placement.py",
        "to": "db-postgres",
        "direction": "read",
        "evidence": {
          "path": "learningBack/modules/knowledge/chain_placement.py",
          "line": 39,
          "fragment": "goal = [c.id for c in session.query(Concept).filter(Concept.domain == domain).all()]"
        }
      },
      {
        "from": "learningBack/modules/knowledge/cross_links_api.py",
        "to": "db-postgres",
        "direction": "write",
        "evidence": {
          "path": "learningBack/modules/knowledge/cross_links_api.py",
          "line": 28,
          "fragment": "session.commit()"
        }
      },
      {
        "from": "learningBack/modules/knowledge/domains_api.py",
        "to": "db-postgres",
        "direction": "write",
        "evidence": {
          "path": "learningBack/modules/knowledge/domains_api.py",
          "line": 41,
          "fragment": "session.commit()"
        }
      }
    ]
  }
}
```

```docdd-userflow
{
  "added": {
    "screens": [],
    "transitions": [],
    "calls": [
      {
        "from": "/profile",
        "to": "GET /me/study-methods",
        "evidence": {
          "path": "learningFront/src/features/study-method/ui/study-method-picker.tsx",
          "line": 17,
          "fragment": "getStudyMethods()"
        }
      },
      {
        "from": "/profile",
        "to": "PUT /me/study-methods",
        "evidence": {
          "path": "learningFront/src/features/study-method/ui/study-method-picker.tsx",
          "line": 32,
          "fragment": "setStudyMethod(REMEMBER_PURPOSE, id)"
        }
      }
    ]
  }
}
```

```docdd-skipped
{
  "files": [
    {
      "path": "learningBack/.gitignore",
      "why": "конфигурация git, не модуль"
    }
  ]
}
```

## Журнал

- 2026-10-05 · заведена черновиком · модель
- 2026-10-05 · на подтверждение · architect
- 2026-10-05 · подтверждён · architect
