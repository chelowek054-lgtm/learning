---
id: M-0022
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
        "id": "learningBack/modules/knowledge/events.py",
        "title": "Подписка на изменение узла графа",
        "layer": "ядро",
        "path": "learningBack/modules/knowledge/events.py",
        "summary": "Узел графа меняется в нескольких местах (правка куратором, промоция, личная правка, перестройка модели); модуль даёт событие NodeChanged и подписку на него, чтобы держатели производных данных (кэш заданий, способы запоминания) узнавали об этом без того, чтобы граф знал о них. Обработчики вызываются синхронно в процессе API и не должны бросать: ошибка одного подписчика не отменяет правку узла и не мешает другим.",
        "api": [
          {
            "name": "NodeChanged",
            "kind": "type",
            "summary": "Событие изменения узла: кто поменял — канон или личный слой пользователя",
            "signature": "{ node_id: UUID, domain: str, version: int, user_id?: UUID }"
          },
          {
            "name": "subscribe",
            "kind": "function",
            "summary": "Подписаться на изменения узлов, вернуть функцию отписки",
            "signature": "(callback) => unsubscribe_fn"
          },
          {
            "name": "unsubscribe",
            "kind": "function",
            "summary": "Снять подписку",
            "signature": "(callback) => None"
          },
          {
            "name": "emit",
            "kind": "function",
            "summary": "Уведомить подписчиков; падение одного не мешает другим",
            "signature": "(event: NodeChanged) => None"
          }
        ]
      },
      {
        "id": "learningBack/modules/knowledge/goal_intake.py",
        "title": "Постановка цели как диалог",
        "layer": "ядро",
        "path": "learningBack/modules/knowledge/goal_intake.py",
        "summary": "Голая строка «название предмета» не даёт ни уточнить, ни проверить, что система поняла цель человека. Модуль ведёт диалог: свободный ввод → 2–4 уточняющих вопроса (не обязательных) → пересказ «область, цель, уровень, пожелания» → явное подтверждение; пока цель не подтверждена, граф не строится. Хранится только итог пересказа, а не вся переписка.",
        "api": [
          {
            "name": "GoalIntakeError",
            "kind": "class",
            "summary": "Итог диалога некорректен; код ошибки — для клиента"
          },
          {
            "name": "propose_questions",
            "kind": "function",
            "summary": "2–4 уточняющих вопроса к свободному вводу, ничего не пишет",
            "signature": "(text: str) => list[dict]"
          },
          {
            "name": "clean_questions",
            "kind": "function",
            "summary": "Привести ответ модели к уникальным вопросам, добить нехватку общими",
            "signature": "(raw) => list[dict]"
          },
          {
            "name": "summarize",
            "kind": "function",
            "summary": "Пересказ итога диалога для подтверждения",
            "signature": "(text, answers) => dict"
          },
          {
            "name": "clean_summary",
            "kind": "function",
            "summary": "Привести пересказ к безопасному виду: область, известный уровень, лимиты",
            "signature": "(raw, text) => dict"
          },
          {
            "name": "as_goal_text",
            "kind": "function",
            "summary": "Подтверждённая цель одной строкой — вход построения графа",
            "signature": "(summary) => str"
          },
          {
            "name": "confirm",
            "kind": "function",
            "summary": "Сохранить подтверждённый итог; повтор по той же области заменяет прежний",
            "signature": "(session, user_id, domain, summary) => GoalIntake"
          },
          {
            "name": "get_confirmed",
            "kind": "function",
            "summary": "Подтверждённый итог пользователя по области",
            "signature": "(session, user_id, domain) => GoalIntake | None"
          },
          {
            "name": "view",
            "kind": "function",
            "summary": "Представление итога для клиента",
            "signature": "(row) => dict"
          }
        ]
      },
      {
        "id": "learningBack/modules/knowledge/path_volume.py",
        "title": "Предпросмотр объёма пути перед построением",
        "layer": "ядро",
        "path": "learningBack/modules/knowledge/path_volume.py",
        "summary": "Человек должен видеть, во что ввязывается, до построения графа: сколько базовых областей лежит под целью и сколько в них понятий. Расчёт идёт по уже построенному графу областей и межобластным связям и ничего не строит и не тратит модель; интуитивный вариант («понять своими словами») не тянет связи, обязательные только для более высоких ступеней.",
        "api": [
          {
            "name": "volume",
            "kind": "function",
            "summary": "Объём пути до цели: полный и интуитивный варианты",
            "signature": "(session, domain, target_bloom) => dict"
          },
          {
            "name": "INTUITIVE_BLOOM",
            "kind": "const",
            "summary": "Ступень интуитивного варианта",
            "signature": "\"understand\""
          }
        ]
      },
      {
        "id": "learningBack/modules/knowledge/subdomains.py",
        "title": "Граф цели из субдоменов",
        "layer": "ядро",
        "path": "learningBack/modules/knowledge/subdomains.py",
        "summary": "Большая цель одним запросом к модели даёт плоский граф плохого качества. Модуль делит цель на субдомены (модель предлагает, человек правит), строит каждый отдельным запросом как примитивную область и объединяет итог со связями-предпосылками через границы субдоменов. Здесь только чистая логика над словарями — модель и база снаружи.",
        "api": [
          {
            "name": "propose_split",
            "kind": "function",
            "summary": "Разбиение цели на субдомены, ничего не пишет",
            "signature": "(domain, topic, limit?) => list[dict]"
          },
          {
            "name": "clean_split",
            "kind": "function",
            "summary": "Привести разбиение (модели или правку человека) к виду без дублей и циклов",
            "signature": "(raw, limit?) => list[dict]"
          },
          {
            "name": "build_subdomain",
            "kind": "function",
            "summary": "Граф одного субдомена отдельным запросом к модели",
            "signature": "(domain, goal, sub) => dict"
          },
          {
            "name": "assemble",
            "kind": "function",
            "summary": "Объединить графы субдоменов, связав хвосты предпосылки с корнями следующего",
            "signature": "(split, subgraphs) => dict"
          },
          {
            "name": "budget",
            "kind": "function",
            "summary": "Сколько запросов к модели стоит построение",
            "signature": "(split) => dict"
          },
          {
            "name": "MAX_SUBDOMAINS",
            "kind": "const",
            "summary": "Предел числа субдоменов",
            "signature": "8"
          }
        ]
      },
      {
        "id": "learningBack/modules/languages/api.py",
        "title": "API материалов аудирования и устного ответа",
        "layer": "маршруты",
        "path": "learningBack/modules/languages/api.py",
        "summary": "Эндпоинты для материалов аудирования: куратор генерирует и подтверждает, учащийся читает только подтверждённое и без текста (это аудирование — текст видит лишь куратор). Объединяет роутер listening с роутером speaking в один router модуля.",
        "api": [
          {
            "name": "generate",
            "kind": "function",
            "summary": "POST /languages/listening/generate — сгенерировать материал",
            "signature": "(body, session) => dict"
          },
          {
            "name": "list_approved",
            "kind": "function",
            "summary": "GET /languages/listening — подтверждённые материалы без текста",
            "signature": "(session) => list[dict]"
          },
          {
            "name": "list_drafts",
            "kind": "function",
            "summary": "GET /languages/listening/drafts — черновики с текстом",
            "signature": "(session) => list[dict]"
          },
          {
            "name": "approve",
            "kind": "function",
            "summary": "POST /languages/listening/{id}/approve",
            "signature": "(material_id, session) => dict"
          },
          {
            "name": "reject",
            "kind": "function",
            "summary": "POST /languages/listening/{id}/reject — вернуть в черновик",
            "signature": "(material_id, session) => dict"
          },
          {
            "name": "audio",
            "kind": "function",
            "summary": "GET /languages/listening/{id}/audio — озвучка подтверждённого материала",
            "signature": "(material_id, session) => FileResponse"
          },
          {
            "name": "router",
            "kind": "const",
            "summary": "Объединённый роутер listening + speaking"
          }
        ]
      },
      {
        "id": "learningBack/modules/languages/distractors.py",
        "title": "Разбор дистракторов",
        "layer": "ядро",
        "path": "learningBack/modules/languages/distractors.py",
        "summary": "Объясняет, почему каждый неверный вариант ответа не подходит, ссылаясь на текст. Приходит фоновой задачей при наличии сети и не блокирует дрилл: ответ проверен локально по payload, объяснение — приятное дополнение; без ключа модели берётся авторское объяснение вопроса.",
        "api": [
          {
            "name": "explain_distractors",
            "kind": "function",
            "summary": "Обработчик job: почему каждый неверный вариант не подходит",
            "signature": "(session, job, gateway) => dict"
          },
          {
            "name": "JOB_TYPE",
            "kind": "const",
            "summary": "Тип фоновой задачи",
            "signature": "\"explain_distractors\""
          }
        ]
      },
      {
        "id": "learningBack/modules/languages/listening.py",
        "title": "Материалы для аудирования",
        "layer": "ядро",
        "path": "learningBack/modules/languages/listening.py",
        "summary": "Генерация, озвучка и курирование материалов аудирования: passage и вопросы с дистракторами строит модель, озвучку — порт TTS. Материал рождается черновиком с оценкой уверенности и до подтверждения куратором учащемуся не выдаётся — сгенерированный вопрос с неверным «верным» ответом хуже его отсутствия. Состояние живёт в Material.content, материал общий (user_id = null).",
        "api": [
          {
            "name": "GenerationFailed",
            "kind": "class",
            "summary": "Модель не вернула годный материал"
          },
          {
            "name": "generate",
            "kind": "function",
            "summary": "Сгенерировать материал: passage, вопросы, озвучка",
            "signature": "(session, gateway, tts, topic, level) => Material"
          },
          {
            "name": "clean_questions",
            "kind": "function",
            "summary": "Оставить только годные вопросы: верный ответ среди вариантов",
            "signature": "(raw) => list[dict]"
          },
          {
            "name": "confidence",
            "kind": "function",
            "summary": "Уверенность, сниженная долей отброшенных вопросов",
            "signature": "(raw, kept) => float"
          },
          {
            "name": "listing",
            "kind": "function",
            "summary": "Материалы модуля, опционально по статусу",
            "signature": "(session, status?) => list[Material]"
          },
          {
            "name": "get",
            "kind": "function",
            "summary": "Материал аудирования по id",
            "signature": "(session, material_id) => Material | None"
          },
          {
            "name": "set_status",
            "kind": "function",
            "summary": "Сменить статус материала (approved/draft)",
            "signature": "(session, material_id, status) => Material | None"
          },
          {
            "name": "audio_file",
            "kind": "function",
            "summary": "Путь к файлу озвучки, если он существует",
            "signature": "(material) => Path | None"
          },
          {
            "name": "describe",
            "kind": "function",
            "summary": "Представление для клиента; текст только куратору",
            "signature": "(m, passage: bool) => dict"
          }
        ]
      },
      {
        "id": "learningBack/modules/languages/speaking_api.py",
        "title": "API загрузки устного ответа",
        "layer": "маршруты",
        "path": "learningBack/modules/languages/speaking_api.py",
        "summary": "Принимает запись устного ответа с устройства и сразу ставит job `transcribe` в очередь; файл виден только владельцу.",
        "api": [
          {
            "name": "upload",
            "kind": "function",
            "summary": "POST /languages/speaking/audio — принять запись, вернуть audioId",
            "signature": "(file, user) => dict"
          },
          {
            "name": "router",
            "kind": "const",
            "summary": "Роутер эндпоинтов speaking"
          }
        ]
      },
      {
        "id": "learningBack/modules/languages/speech.py",
        "title": "Устный ответ: запись, расшифровка, метрики",
        "layer": "ядро",
        "path": "learningBack/modules/languages/speech.py",
        "summary": "Запись приходит файлом и живёт ровно до расшифровки: голос — биометрия, поэтому после успешной расшифровки файл удаляется и дальше работает только текст с таймингами. Оценка идёт по тексту и таймингам (темп речи, длинные паузы); произношение по ним не проверить, рубрика честно помечает это ограничение.",
        "api": [
          {
            "name": "voice_path",
            "kind": "function",
            "summary": "Путь файла записи по user_id и audio_id",
            "signature": "(user_id, audio_id) => Path"
          },
          {
            "name": "store_voice",
            "kind": "function",
            "summary": "Сохранить запись, вернуть audioId",
            "signature": "(user_id, data: bytes) => str"
          },
          {
            "name": "metrics",
            "kind": "function",
            "summary": "Темп речи и паузы по таймингам слов транскрипта",
            "signature": "(transcript) => dict"
          },
          {
            "name": "as_text",
            "kind": "function",
            "summary": "Текст ответа с вкраплёнными метриками для оценки",
            "signature": "(transcript, metrics) => str"
          },
          {
            "name": "transcribe_job",
            "kind": "function",
            "summary": "Обработчик job: расшифровать, удалить запись, поставить задачу оценки",
            "signature": "(session, job, gateway) => dict"
          },
          {
            "name": "TRANSCRIBE_JOB",
            "kind": "const",
            "signature": "\"transcribe\""
          },
          {
            "name": "GRADE_JOB",
            "kind": "const",
            "signature": "\"grade_speaking\""
          }
        ]
      },
      {
        "id": "learningBack/modules/mnemonic/__init__.py",
        "title": "Backend-модуль mnemonic",
        "layer": "ядро",
        "path": "learningBack/modules/mnemonic/__init__.py",
        "summary": "Вторая техника запоминания: вспомнить формулировку узла по первым буквам слов, самому оценить, как вышло. Отличается от интервального повторения устройством, а не названием — нет расписания и карточки в очереди. Результат уходит в граф как обычное свидетельство об освоении, поэтому смена способа освоенность не стирает; модуль не знает графа — узел приходит готовым payload'ом.",
        "api": [
          {
            "name": "mask_text",
            "kind": "function",
            "summary": "Оставить первую букву слова, остальное скрыть; пунктуация цела",
            "signature": "(text) => str"
          },
          {
            "name": "MnemonicModule",
            "kind": "class",
            "summary": "Backend-модуль техники «вспомнить по первым буквам»"
          },
          {
            "name": "backend",
            "kind": "const",
            "summary": "Экземпляр MnemonicModule"
          }
        ]
      },
      {
        "id": "learningBack/modules/srs/__init__.py",
        "title": "Backend-модуль srs",
        "layer": "ядро",
        "path": "learningBack/modules/srs/__init__.py",
        "summary": "Описание способа «интервальное повторение» и перевод результата повторения в свидетельство об освоении, не зависящее от способа. Сами карточки заводят другие модули (стартовые колоды, карточки ошибок); для учащегося повторение идёт очередью карточек, а не отдельной активностью.",
        "api": [
          {
            "name": "evidence_from_review",
            "kind": "function",
            "summary": "Оценка карточки как свидетельство об освоении в общем формате",
            "signature": "(concept_id, rating, bloom?) => Evidence"
          },
          {
            "name": "SrsModule",
            "kind": "class",
            "summary": "Backend-модуль интервального повторения"
          },
          {
            "name": "backend",
            "kind": "const",
            "summary": "Экземпляр SrsModule"
          }
        ]
      },
      {
        "id": "learningBack/scripts/purge_expired.py",
        "title": "Скрипт: удалить данные с истёкшим сроком хранения",
        "layer": "скрипты",
        "path": "learningBack/scripts/purge_expired.py",
        "summary": "Запускается по расписанию (например, раз в сутки): удаляет у всех пользователей данные, срок хранения которых истёк согласно типу данных. Повторный запуск безопасен.",
        "api": [
          {
            "name": "main",
            "kind": "function",
            "summary": "Точка входа скрипта",
            "signature": "() => None"
          }
        ]
      },
      {
        "id": "learningBack/scripts/worker.py",
        "title": "Скрипт: фоновый воркер AI-задач",
        "layer": "скрипты",
        "path": "learningBack/scripts/worker.py",
        "summary": "Запускает цикл обработки очереди AI-задач (распознавание речи, генерация) до сигнала остановки; работает вместе с JOBS_MODE=worker у API, когда /sync/push только ставит задачи в очередь.",
        "api": [
          {
            "name": "main",
            "kind": "function",
            "summary": "Запустить воркер до SIGTERM/SIGINT",
            "signature": "() => None"
          }
        ]
      },
      {
        "id": "learningBack/tests/test_account_delete.py",
        "title": "Тесты: удаление аккаунта и согласие с политикой",
        "layer": "тесты",
        "path": "learningBack/tests/test_account_delete.py",
        "summary": "Проверяют T-0028/R-0018/V-0029: удаление аккаунта с подтверждением пароля стирает данные по всем типам (активности, ответы, карточки, расход токенов, журнал доступа) вместе со строками пользователя; отдельно — согласие с версией политики данных при регистрации."
      },
      {
        "id": "learningBack/tests/test_awl.py",
        "title": "Тесты: полная колода Academic Word List",
        "layer": "тесты",
        "path": "learningBack/tests/test_awl.py",
        "summary": "Проверяют T-0045/R-0024/V-0068: весь список из 570 слов AWL входит в стартовую колоду без сокращений по десяти подсписками, у каждой карточки есть слово и пояснение, а расписание выдаёт первый подсписок сразу и остальные по графику DAYS_BETWEEN_SUBLISTS, согласованному с состоянием FSRS."
      },
      {
        "id": "learningBack/tests/test_chain_placement.py",
        "title": "Тесты: проверка по цепочке базовых областей",
        "layer": "тесты",
        "path": "learningBack/tests/test_chain_placement.py",
        "summary": "Проверяют T-0066/R-0037/V-0089: уровень проверяется по цепочке базовых областей сверху вниз, освоенное верхнее понятие снимает проверку нижестоящего, а задания и оценка ответов те же, что у плейсмента одной области."
      },
      {
        "id": "learningBack/tests/test_cross_links.py",
        "title": "Тесты: межобластные предпосылки понятий",
        "layer": "тесты",
        "path": "learningBack/tests/test_cross_links.py",
        "summary": "Проверяют T-0065/R-0036/V-0088: связи «нужно знать, чтобы освоить» между понятиями разных областей и подтягивание в курс только нужных предков конкретных понятий на нужной ступени, а не всей базовой области."
      },
      {
        "id": "learningBack/tests/test_domains.py",
        "title": "Тесты: граф областей и уровень примитивности",
        "layer": "тесты",
        "path": "learningBack/tests/test_domains.py",
        "summary": "Проверяют T-0064/R-0035/V-0087: уровень области — вычисляемая глубина в графе предпосылок (самый длинный путь от опоры, а не метка), и правка связей ниже поднимает уровни областей выше."
      },
      {
        "id": "learningBack/tests/test_explain_distractors.py",
        "title": "Тесты: разбор дистракторов фоновой задачей",
        "layer": "тесты",
        "path": "learningBack/tests/test_explain_distractors.py",
        "summary": "Проверяют T-0038/V-0059: job explain_distractors через process_job с подменённым gateway объясняет, почему неверные варианты ответа читательского дрилла не подходят."
      },
      {
        "id": "learningBack/tests/test_goal_intake.py",
        "title": "Тесты: постановка цели как диалог",
        "layer": "тесты",
        "path": "learningBack/tests/test_goal_intake.py",
        "summary": "Проверяют T-0061/R-0033/V-0085: вопросы всегда 2–4, уникальны и подрезаны; пересказ собирается из ввода и ответов; подтверждение через роутер открывает построение графа субдоменов, которое без подтверждения отклоняется."
      },
      {
        "id": "learningBack/tests/test_graph_interface.py",
        "title": "Тесты: публичный интерфейс графа знаний",
        "layer": "тесты",
        "path": "learningBack/tests/test_graph_interface.py",
        "summary": "Проверяют T-0052: узел, связи, граница знаний, освоенность и запись свидетельства через modules.knowledge.api, а также подписку/отписку на изменение узла — упавший подписчик не мешает остальным."
      },
      {
        "id": "learningBack/tests/test_graph_links_check.py",
        "title": "Тесты: перезапрос графа без связей",
        "layer": "тесты",
        "path": "learningBack/tests/test_graph_links_check.py",
        "summary": "Проверяют T-0019 (находка прототипа «Английский B2»): граф без единой связи перезапрашивается у модели один раз с прямым указанием, а если повтор тоже пуст или теряет узлы — остаётся первый ответ."
      },
      {
        "id": "learningBack/tests/test_graph_subject_agnostic.py",
        "title": "Тесты: граф без привязки к предмету",
        "layer": "тесты",
        "path": "learningBack/tests/test_graph_subject_agnostic.py",
        "summary": "Проверяют T-0052/R-0028/V-0080: один и тот же код графа работает для предметов разной природы (технический, языковой и другие) без специального знания о предмете."
      },
      {
        "id": "learningBack/tests/test_language_course.py",
        "title": "Тесты: языковой предмет на общем графе",
        "layer": "тесты",
        "path": "learningBack/tests/test_language_course.py",
        "summary": "Проверяют T-0020/V-0045: шаг курса по узлу общего графа может исполняться дриллом чтения модуля languages (reading_payload) наравне с другими способами."
      },
      {
        "id": "learningBack/tests/test_listening_materials.py",
        "title": "Тесты: материалы аудирования",
        "layer": "тесты",
        "path": "learningBack/tests/test_listening_materials.py",
        "summary": "Проверяют T-0039/V-0061: генерация материала с MockTTS, цикл approve/reject и то, что учащемуся текст черновика не выдаётся — видно только подтверждённое и без passage."
      },
      {
        "id": "learningBack/tests/test_mail.py",
        "title": "Тесты: письмо восстановления пароля",
        "layer": "тесты",
        "path": "learningBack/tests/test_mail.py",
        "summary": "Проверяют T-0002/R-0006: доставка одноразового кода восстановления пароля письмом, включая лимит частоты запросов через core.ratelimit."
      },
      {
        "id": "learningBack/tests/test_memorization_module.py",
        "title": "Тесты: способы изучения как модули",
        "layer": "тесты",
        "path": "learningBack/tests/test_memorization_module.py",
        "summary": "Проверяют T-0053/V-0081: способы изучения (включая srs и mnemonic) объявляются модулями по общему контракту, курс собирается из включённых способов, отключение/включение способа не ломает граф и данные, а свидетельство об освоении от любого способа обновляет одну и ту же освоенность."
      },
      {
        "id": "learningBack/tests/test_module_manifest.py",
        "title": "Тесты: манифест и жизненный цикл модуля",
        "layer": "тесты",
        "path": "learningBack/tests/test_module_manifest.py",
        "summary": "Проверяют T-0051/C-0001/V-0079: версия контракта манифеста, совместимость с ядром и жизненный цикл подключённого модуля."
      },
      {
        "id": "learningBack/tests/test_monitoring.py",
        "title": "Тесты: мониторинг здоровья системы",
        "layer": "тесты",
        "path": "learningBack/tests/test_monitoring.py",
        "summary": "Проверяют T-0050: приём ошибок клиента, долю упавших задач и расход токенов за окно, которые отдаёт сводка здоровья системы."
      },
      {
        "id": "learningBack/tests/test_path_volume.py",
        "title": "Тесты: предпросмотр объёма пути",
        "layer": "тесты",
        "path": "learningBack/tests/test_path_volume.py",
        "summary": "Проверяют T-0067/R-0038/V-0090: точный расчёт объёма для уже построенной цели и оценку по областям, когда цели ещё нет, а также различие полного и интуитивного вариантов по ступени понимания."
      },
      {
        "id": "learningBack/tests/test_plugin_isolation.py",
        "title": "Тесты: изоляция «злого» модуля",
        "layer": "тесты",
        "path": "learningBack/tests/test_plugin_isolation.py",
        "summary": "Проверяют T-0055/R-0030/V-0082: модуль не выходит за границы данных и сети, таймаут/лимит обращений/лимит подряд идущих сбоев останавливают сам модуль, а не ядро, и действуют по согласию на расширенные разрешения."
      }
    ],
    "imports": [
      {
        "from": "learningBack/modules/knowledge/goal_intake.py",
        "to": "learningBack/core/ai_gateway.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/goal_intake.py",
          "line": 26,
          "fragment": "from core.ai_gateway import get_ai_gateway, has_llm"
        }
      },
      {
        "from": "learningBack/modules/knowledge/goal_intake.py",
        "to": "learningBack/modules/knowledge/models.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/goal_intake.py",
          "line": 27,
          "fragment": "from modules.knowledge.models import GoalIntake"
        }
      },
      {
        "from": "learningBack/modules/knowledge/path_volume.py",
        "to": "learningBack/modules/knowledge/cross_links.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/path_volume.py",
          "line": 16,
          "fragment": "from modules.knowledge import cross_links, domains"
        }
      },
      {
        "from": "learningBack/modules/knowledge/path_volume.py",
        "to": "learningBack/modules/knowledge/domains.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/path_volume.py",
          "line": 16,
          "fragment": "from modules.knowledge import cross_links, domains"
        }
      },
      {
        "from": "learningBack/modules/knowledge/path_volume.py",
        "to": "learningBack/modules/knowledge/models.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/path_volume.py",
          "line": 17,
          "fragment": "from modules.knowledge.models import Concept, Domain"
        }
      },
      {
        "from": "learningBack/modules/knowledge/subdomains.py",
        "to": "learningBack/core/ai_gateway.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/subdomains.py",
          "line": 14,
          "fragment": "from core.ai_gateway import get_ai_gateway, has_llm"
        }
      },
      {
        "from": "learningBack/modules/knowledge/subdomains.py",
        "to": "learningBack/modules/knowledge/ai.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/subdomains.py",
          "line": 178,
          "fragment": "from modules.knowledge import ai"
        }
      },
      {
        "from": "learningBack/modules/languages/api.py",
        "to": "learningBack/core/ai_gateway.py",
        "evidence": {
          "path": "learningBack/modules/languages/api.py",
          "line": 9,
          "fragment": "from core.ai_gateway import get_ai_gateway"
        }
      },
      {
        "from": "learningBack/modules/languages/api.py",
        "to": "learningBack/core/ai_base.py",
        "evidence": {
          "path": "learningBack/modules/languages/api.py",
          "line": 10,
          "fragment": "from core.ai_base import ProviderError"
        }
      },
      {
        "from": "learningBack/modules/languages/api.py",
        "to": "learningBack/core/deps.py",
        "evidence": {
          "path": "learningBack/modules/languages/api.py",
          "line": 11,
          "fragment": "from core.deps import CurrentSuperuser, CurrentUser, SessionDep"
        }
      },
      {
        "from": "learningBack/modules/languages/api.py",
        "to": "learningBack/core/tts.py",
        "evidence": {
          "path": "learningBack/modules/languages/api.py",
          "line": 12,
          "fragment": "from core.tts import get_tts"
        }
      },
      {
        "from": "learningBack/modules/languages/api.py",
        "to": "learningBack/modules/languages/listening.py",
        "evidence": {
          "path": "learningBack/modules/languages/api.py",
          "line": 13,
          "fragment": "from modules.languages import listening"
        }
      },
      {
        "from": "learningBack/modules/languages/api.py",
        "to": "learningBack/modules/languages/speaking_api.py",
        "evidence": {
          "path": "learningBack/modules/languages/api.py",
          "line": 14,
          "fragment": "from modules.languages.speaking_api import router as speaking_router"
        }
      },
      {
        "from": "learningBack/modules/languages/distractors.py",
        "to": "learningBack/core/models.py",
        "evidence": {
          "path": "learningBack/modules/languages/distractors.py",
          "line": 11,
          "fragment": "from core.models import Activity, Job"
        }
      },
      {
        "from": "learningBack/modules/languages/listening.py",
        "to": "learningBack/core/config.py",
        "evidence": {
          "path": "learningBack/modules/languages/listening.py",
          "line": 19,
          "fragment": "from core.config import settings"
        }
      },
      {
        "from": "learningBack/modules/languages/listening.py",
        "to": "learningBack/core/models.py",
        "evidence": {
          "path": "learningBack/modules/languages/listening.py",
          "line": 20,
          "fragment": "from core.models import Material"
        }
      },
      {
        "from": "learningBack/modules/languages/listening.py",
        "to": "learningBack/core/tts.py",
        "evidence": {
          "path": "learningBack/modules/languages/listening.py",
          "line": 21,
          "fragment": "from core.tts import TextToSpeech"
        }
      },
      {
        "from": "learningBack/modules/languages/speaking_api.py",
        "to": "learningBack/core/config.py",
        "evidence": {
          "path": "learningBack/modules/languages/speaking_api.py",
          "line": 5,
          "fragment": "from core.config import settings"
        }
      },
      {
        "from": "learningBack/modules/languages/speaking_api.py",
        "to": "learningBack/core/deps.py",
        "evidence": {
          "path": "learningBack/modules/languages/speaking_api.py",
          "line": 6,
          "fragment": "from core.deps import CurrentUser"
        }
      },
      {
        "from": "learningBack/modules/languages/speaking_api.py",
        "to": "learningBack/modules/languages/speech.py",
        "evidence": {
          "path": "learningBack/modules/languages/speaking_api.py",
          "line": 7,
          "fragment": "from modules.languages import speech"
        }
      },
      {
        "from": "learningBack/modules/languages/speech.py",
        "to": "learningBack/core/config.py",
        "evidence": {
          "path": "learningBack/modules/languages/speech.py",
          "line": 15,
          "fragment": "from core.config import settings"
        }
      },
      {
        "from": "learningBack/modules/languages/speech.py",
        "to": "learningBack/core/models.py",
        "evidence": {
          "path": "learningBack/modules/languages/speech.py",
          "line": 16,
          "fragment": "from core.models import Job, Response"
        }
      },
      {
        "from": "learningBack/modules/languages/speech.py",
        "to": "learningBack/core/stt.py",
        "evidence": {
          "path": "learningBack/modules/languages/speech.py",
          "line": 17,
          "fragment": "from core.stt import Transcript, get_stt"
        }
      },
      {
        "from": "learningBack/modules/mnemonic/__init__.py",
        "to": "learningBack/core/manifest.py",
        "evidence": {
          "path": "learningBack/modules/mnemonic/__init__.py",
          "line": 16,
          "fragment": "from core.manifest import ModuleManifest"
        }
      },
      {
        "from": "learningBack/modules/mnemonic/__init__.py",
        "to": "learningBack/core/methods.py",
        "evidence": {
          "path": "learningBack/modules/mnemonic/__init__.py",
          "line": 17,
          "fragment": "from core.methods import REMEMBER, StudyMethod"
        }
      },
      {
        "from": "learningBack/modules/mnemonic/__init__.py",
        "to": "learningBack/core/modules.py",
        "evidence": {
          "path": "learningBack/modules/mnemonic/__init__.py",
          "line": 18,
          "fragment": "from core.modules import BackendModule"
        }
      },
      {
        "from": "learningBack/modules/srs/__init__.py",
        "to": "learningBack/core/evidence.py",
        "evidence": {
          "path": "learningBack/modules/srs/__init__.py",
          "line": 13,
          "fragment": "from core.evidence import Evidence"
        }
      },
      {
        "from": "learningBack/modules/srs/__init__.py",
        "to": "learningBack/core/manifest.py",
        "evidence": {
          "path": "learningBack/modules/srs/__init__.py",
          "line": 14,
          "fragment": "from core.manifest import ModuleManifest"
        }
      },
      {
        "from": "learningBack/modules/srs/__init__.py",
        "to": "learningBack/core/methods.py",
        "evidence": {
          "path": "learningBack/modules/srs/__init__.py",
          "line": 15,
          "fragment": "from core.methods import REMEMBER, StudyMethod"
        }
      },
      {
        "from": "learningBack/modules/srs/__init__.py",
        "to": "learningBack/core/modules.py",
        "evidence": {
          "path": "learningBack/modules/srs/__init__.py",
          "line": 16,
          "fragment": "from core.modules import BackendModule"
        }
      },
      {
        "from": "learningBack/scripts/purge_expired.py",
        "to": "learningBack/core/modules.py",
        "evidence": {
          "path": "learningBack/scripts/purge_expired.py",
          "line": 8,
          "fragment": "from core import modules, userdata"
        }
      },
      {
        "from": "learningBack/scripts/purge_expired.py",
        "to": "learningBack/core/userdata.py",
        "evidence": {
          "path": "learningBack/scripts/purge_expired.py",
          "line": 8,
          "fragment": "from core import modules, userdata"
        }
      },
      {
        "from": "learningBack/scripts/purge_expired.py",
        "to": "learningBack/core/db.py",
        "evidence": {
          "path": "learningBack/scripts/purge_expired.py",
          "line": 9,
          "fragment": "from core.db import SessionLocal"
        }
      },
      {
        "from": "learningBack/scripts/worker.py",
        "to": "learningBack/core/worker.py",
        "evidence": {
          "path": "learningBack/scripts/worker.py",
          "line": 12,
          "fragment": "from core import worker"
        }
      },
      {
        "from": "learningBack/modules/knowledge/router.py",
        "to": "learningBack/modules/knowledge/goal_intake.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/router.py",
          "line": 42,
          "fragment": "from modules.knowledge import events, goal_intake, provenance, subdomains"
        }
      },
      {
        "from": "learningBack/modules/knowledge/router.py",
        "to": "learningBack/modules/knowledge/subdomains.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/router.py",
          "line": 42,
          "fragment": "from modules.knowledge import events, goal_intake, provenance, subdomains"
        }
      },
      {
        "from": "learningBack/modules/knowledge/router.py",
        "to": "learningBack/modules/knowledge/events.py",
        "evidence": {
          "path": "learningBack/modules/knowledge/router.py",
          "line": 43,
          "fragment": "from modules.knowledge.events import NodeChanged"
        }
      },
      {
        "from": "learningBack/modules/languages/__init__.py",
        "to": "learningBack/modules/languages/api.py",
        "evidence": {
          "path": "learningBack/modules/languages/__init__.py",
          "line": 252,
          "fragment": "from modules.languages.api import router"
        }
      },
      {
        "from": "learningBack/modules/languages/__init__.py",
        "to": "learningBack/modules/languages/listening.py",
        "evidence": {
          "path": "learningBack/modules/languages/__init__.py",
          "line": 320,
          "fragment": "from modules.languages import listening"
        }
      }
    ],
    "groups": [
      {
        "id": "goal-intake-dialog-impl",
        "title": "Диалог постановки цели",
        "summary": "Уточняющие вопросы, пересказ и подтверждение цели перед тем, как граф начнёт строиться.",
        "modules": [
          "learningBack/modules/knowledge/goal_intake.py"
        ],
        "capability": "goal-intake"
      },
      {
        "id": "goal-subdomain-split-impl",
        "title": "Разбиение цели на субдомены",
        "summary": "Крупная цель делится на части, каждая из которых строится отдельным запросом как примитивная область.",
        "modules": [
          "learningBack/modules/knowledge/subdomains.py"
        ],
        "capability": "goal-subdomain-split"
      },
      {
        "id": "goal-tree-assembly-impl",
        "title": "Сборка графа цели из субдоменов",
        "summary": "Графы субдоменов объединяются в один граф цели со связями-предпосылками через границы субдоменов.",
        "modules": [
          "learningBack/modules/knowledge/subdomains.py"
        ],
        "capability": "goal-tree-assembly"
      },
      {
        "id": "path-volume-preview-impl",
        "title": "Предпросмотр объёма пути",
        "summary": "Расчёт полного и интуитивного вариантов объёма пути до цели по графу областей, до построения графа.",
        "modules": [
          "learningBack/modules/knowledge/path_volume.py"
        ],
        "capability": "path-volume-preview"
      },
      {
        "id": "memorize-techniques-impl",
        "title": "Техники запоминания",
        "summary": "Две техники по общему контракту способа изучения: интервальное повторение и вспоминание по первым буквам.",
        "modules": [
          "learningBack/modules/srs/__init__.py",
          "learningBack/modules/mnemonic/__init__.py"
        ],
        "capability": "memorize-techniques"
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
        "capability": "reception-drills"
      },
      {
        "id": "speaking-flow-impl",
        "title": "Устный ответ",
        "summary": "Загрузка записи устного ответа, расшифровка и метрики темпа/пауз для оценки.",
        "modules": [
          "learningBack/modules/languages/speaking_api.py",
          "learningBack/modules/languages/speech.py"
        ],
        "capability": "speaking"
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
        "id": "mem-node-change-subscribers",
        "kind": "memory",
        "where": "modules.knowledge.events._subscribers",
        "title": "Подписчики на изменение узла (in-process)"
      },
      {
        "id": "file-awl-wordlist",
        "kind": "file",
        "where": "learningBack/modules/languages/data/awl.tsv",
        "title": "Список слов Academic Word List"
      },
      {
        "id": "file-voice-recording",
        "kind": "file",
        "where": "settings.voice_dir",
        "title": "Запись устного ответа (временный файл до расшифровки)"
      },
      {
        "id": "file-listening-audio",
        "kind": "file",
        "where": "settings.audio_dir",
        "title": "Озвучка материала аудирования"
      }
    ],
    "flows": [
      {
        "from": "learningBack/modules/knowledge/events.py",
        "to": "mem-node-change-subscribers",
        "direction": "write",
        "evidence": {
          "path": "learningBack/modules/knowledge/events.py",
          "line": 36,
          "fragment": "_subscribers.append(callback)"
        }
      },
      {
        "from": "learningBack/modules/knowledge/events.py",
        "to": "mem-node-change-subscribers",
        "direction": "read",
        "evidence": {
          "path": "learningBack/modules/knowledge/events.py",
          "line": 46,
          "fragment": "for callback in list(_subscribers):"
        }
      },
      {
        "from": "learningBack/modules/languages/generators.py",
        "to": "file-awl-wordlist",
        "direction": "read",
        "evidence": {
          "path": "learningBack/modules/languages/generators.py",
          "line": 21,
          "fragment": "_DATA.read_text(encoding=\"utf-8\").splitlines()"
        }
      },
      {
        "from": "learningBack/modules/languages/speech.py",
        "to": "file-voice-recording",
        "direction": "write",
        "evidence": {
          "path": "learningBack/modules/languages/speech.py",
          "line": 34,
          "fragment": "path.write_bytes(data)"
        }
      },
      {
        "from": "learningBack/modules/languages/speech.py",
        "to": "file-voice-recording",
        "direction": "read",
        "evidence": {
          "path": "learningBack/modules/languages/speech.py",
          "line": 72,
          "fragment": "t = get_stt().transcribe(path.read_bytes()"
        }
      },
      {
        "from": "learningBack/modules/languages/speech.py",
        "to": "file-voice-recording",
        "direction": "write",
        "evidence": {
          "path": "learningBack/modules/languages/speech.py",
          "line": 80,
          "fragment": "path.unlink(missing_ok=True)"
        }
      },
      {
        "from": "learningBack/modules/languages/listening.py",
        "to": "file-listening-audio",
        "direction": "write",
        "evidence": {
          "path": "learningBack/modules/languages/listening.py",
          "line": 122,
          "fragment": "path.write_bytes(tts.synthesize(passage))"
        }
      },
      {
        "from": "learningBack/modules/languages/api.py",
        "to": "file-listening-audio",
        "direction": "read",
        "evidence": {
          "path": "learningBack/modules/languages/api.py",
          "line": 80,
          "fragment": "return FileResponse(path, media_type=m.content[\"audio\"][\"mime\"])"
        }
      },
      {
        "from": "learningBack/modules/knowledge/goal_intake.py",
        "to": "db-postgres",
        "direction": "both",
        "evidence": {
          "path": "learningBack/modules/knowledge/goal_intake.py",
          "line": 284,
          "fragment": "row = session.query(GoalIntake).filter_by(user_id=user_id, domain=domain).one_or_none()"
        }
      },
      {
        "from": "learningBack/modules/knowledge/path_volume.py",
        "to": "db-postgres",
        "direction": "read",
        "evidence": {
          "path": "learningBack/modules/knowledge/path_volume.py",
          "line": 25,
          "fragment": "for name, n in session.query(Concept.domain, func.count(Concept.id))"
        }
      },
      {
        "from": "learningBack/modules/languages/distractors.py",
        "to": "db-postgres",
        "direction": "read",
        "evidence": {
          "path": "learningBack/modules/languages/distractors.py",
          "line": 47,
          "fragment": "activity = session.get(Activity, ref.get(\"activityId\"))"
        }
      },
      {
        "from": "learningBack/modules/languages/listening.py",
        "to": "db-postgres",
        "direction": "write",
        "evidence": {
          "path": "learningBack/modules/languages/listening.py",
          "line": 139,
          "fragment": "session.add(material)"
        }
      },
      {
        "from": "learningBack/modules/languages/listening.py",
        "to": "db-postgres",
        "direction": "read",
        "evidence": {
          "path": "learningBack/modules/languages/listening.py",
          "line": 146,
          "fragment": "session.query(Material)"
        }
      },
      {
        "from": "learningBack/modules/languages/speech.py",
        "to": "db-postgres",
        "direction": "read",
        "evidence": {
          "path": "learningBack/modules/languages/speech.py",
          "line": 66,
          "fragment": "response = session.get(Response, ref.get(\"responseId\"))"
        }
      },
      {
        "from": "learningBack/modules/languages/speech.py",
        "to": "db-postgres",
        "direction": "write",
        "evidence": {
          "path": "learningBack/modules/languages/speech.py",
          "line": 81,
          "fragment": "session.add("
        }
      },
      {
        "from": "learningBack/scripts/purge_expired.py",
        "to": "db-postgres",
        "direction": "write",
        "evidence": {
          "path": "learningBack/scripts/purge_expired.py",
          "line": 15,
          "fragment": "purged = userdata.purge_expired(session, userdata.types(modules.enabled_modules()))"
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
    "calls": []
  }
}
```

## Журнал

- 2026-10-05 · заведена черновиком · модель
- 2026-10-05 · на подтверждение · architect
- 2026-10-05 · подтверждён · architect
- 2026-10-03 · обновлены номера строк в свидетельствах (3): код сдвинулся, содержание карты не менялось · claude
