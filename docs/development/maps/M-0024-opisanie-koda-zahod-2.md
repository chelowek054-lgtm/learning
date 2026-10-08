---
id: M-0024
type: map
title: 'Описание кода: заход 2'
status: approved
created: 2026-10-05
updated: 2026-10-07
---

# Описание кода: заход 2

Черновик: составлен моделью, не подтверждён. Прочитайте, поправьте руками
то, что модель не поняла, и подтвердите — до этого карта на общую картину
не влияет.

```docdd-codemap
{
  "added": {
    "modules": [
      {
        "id": "learningFront/src/features/mnemonic-recall/ui/mnemonic-activity.tsx",
        "title": "Рендерер Activity concept_mnemonic",
        "layer": "features",
        "path": "learningFront/src/features/mnemonic-recall/ui/mnemonic-activity.tsx",
        "summary": "Показывает подсказку по первым буквам, а по запросу — сам ответ; дальше человек сам оценивает, вспомнил или нет. Самооценка переводится в результат освоения и уходит как свидетельство тем же способом, что и любая другая техника; без сети свидетельство остаётся в очереди на устройстве.",
        "api": [
          {
            "name": "MnemonicActivity",
            "kind": "component",
            "summary": "Рендерер Activity concept_mnemonic: подсказка → ответ → самооценка",
            "signature": "({ activity, onComplete }) => JSX"
          }
        ]
      },
      {
        "id": "learningFront/src/features/reading-drill/index.ts",
        "title": "Публичный API фичи reading-drill",
        "layer": "features",
        "path": "learningFront/src/features/reading-drill/index.ts",
        "summary": "Наружу виден только рендерер активности reading_drill; модель разбора и проверки задания остаётся внутренней деталью фичи.",
        "api": [
          {
            "name": "ReadingDrillActivity",
            "kind": "component",
            "summary": "Рендерер Activity reading_drill (реэкспорт)"
          }
        ]
      },
      {
        "id": "learningFront/src/features/reading-drill/model/reading-model.test.ts",
        "title": "Тесты: модель reading-дрилла",
        "layer": "тесты",
        "path": "learningFront/src/features/reading-drill/model/reading-model.test.ts",
        "summary": "Проверяют разбор payload (битые и повторяющиеся вопросы отбрасываются, таймер не задаётся при нуле или мусоре вместо числа), проверку ответов по всем трём форматам вопросов без учёта регистра и пробелов, оценку для журнала с пометкой о выходе времени, список вопросов с выбором, на которых ошиблись, и то, что остаток времени не уходит ниже нуля."
      },
      {
        "id": "learningFront/src/features/reading-drill/model/reading-model.ts",
        "title": "Модель reading-дрилла",
        "layer": "features",
        "path": "learningFront/src/features/reading-drill/model/reading-model.ts",
        "summary": "Чистый разбор payload reading-дрилла (текст, лимит времени, вопросы общего формата) и проверка ответов без сети — результат считается мгновенно и детерминированно. Таймер выводится из момента старта, а не из тикающего счётчика, поэтому не сбивается, если приложение уходило в фон; отдельно — список вопросов с выбором, на которых ошиблись, по ним при сети запрашивается разбор дистракторов.",
        "api": [
          {
            "name": "ReadingDrill",
            "kind": "type",
            "summary": "Разобранное задание reading-дрилла",
            "signature": "{ title, passage, timeLimitSec: number | null, questions: ReadingQuestion[] }"
          },
          {
            "name": "parseReadingDrill",
            "kind": "function",
            "summary": "Проверить payload и привести к ReadingDrill",
            "signature": "(raw: unknown) => ReadingDrill | null"
          },
          {
            "name": "gradeReading",
            "kind": "function",
            "summary": "Проверить ответы по вопросам задания",
            "signature": "(drill, answers) => ReadingResult"
          },
          {
            "name": "toGrade",
            "kind": "function",
            "summary": "Результат в общем виде оценки для журнала ответов",
            "signature": "(result: ReadingResult, timedOut: boolean) => Grade"
          },
          {
            "name": "secondsLeft",
            "kind": "function",
            "summary": "Остаток времени от момента старта, не уходит ниже нуля",
            "signature": "(limitSec, startedAtMs, nowMs) => number | null"
          },
          {
            "name": "formatClock",
            "kind": "function",
            "summary": "Секунды в формат мм:сс",
            "signature": "(totalSec: number) => string"
          },
          {
            "name": "answeredCount",
            "kind": "function",
            "summary": "Сколько вопросов получили ответ",
            "signature": "(drill, answers) => number"
          },
          {
            "name": "wrongChoiceIds",
            "kind": "function",
            "summary": "Вопросы с выбором, на которых ошиблись",
            "signature": "(drill, result) => string[]"
          },
          {
            "name": "isCorrect",
            "kind": "function",
            "summary": "Проверка одного ответа (реэкспорт из shared/lib/quiz)",
            "signature": "(q, given) => boolean"
          }
        ]
      },
      {
        "id": "learningFront/src/features/reading-drill/ui/reading-drill-activity.tsx",
        "title": "Рендерер Activity reading_drill",
        "layer": "features",
        "path": "learningFront/src/features/reading-drill/ui/reading-drill-activity.tsx",
        "summary": "Текст, вопросы и таймер на одном экране: до сдачи можно свободно переходить между ними, проверка идёт локально и работает офлайн. По сдаче результат уходит в общий журнал ответов, а по вопросам с выбором, на которых ошиблись, при сети фоновой задачей запрашивается разбор дистракторов — дрилл при этом не блокируется.",
        "api": [
          {
            "name": "ReadingDrillActivity",
            "kind": "component",
            "summary": "Рендерер Activity reading_drill: текст, вопросы, таймер, мгновенный результат",
            "signature": "({ activity, onComplete }) => JSX"
          }
        ]
      },
      {
        "id": "learningFront/src/features/speaking/index.ts",
        "title": "Публичный API фичи speaking",
        "layer": "features",
        "path": "learningFront/src/features/speaking/index.ts",
        "summary": "Наружу виден только рендерер активности speaking_response; модель разбора задания и правила записи остаются внутри фичи.",
        "api": [
          {
            "name": "SpeakingActivity",
            "kind": "component",
            "summary": "Рендерер Activity speaking_response (реэкспорт)"
          }
        ]
      },
      {
        "id": "learningFront/src/features/speaking/model/speaking-model.test.ts",
        "title": "Тесты: модель устного ответа",
        "layer": "тесты",
        "path": "learningFront/src/features/speaking/model/speaking-model.test.ts",
        "summary": "Проверяют разбор задания с подстановкой лимита по умолчанию и со своим лимитом, отказ разбора на пустом задании, блокировку отправки слишком короткой записи и форматирование времени записи в мм:сс."
      },
      {
        "id": "learningFront/src/features/speaking/model/speaking-model.ts",
        "title": "Модель устного ответа",
        "layer": "features",
        "path": "learningFront/src/features/speaking/model/speaking-model.ts",
        "summary": "Чистый разбор задания устного ответа (тема, лимит записи) без звука и сети: лимит по умолчанию подставляется, если задание не указало свой. Отдельно — причина, по которой слишком короткую запись нельзя отправить: в ней заведомо нет содержательного ответа.",
        "api": [
          {
            "name": "DEFAULT_MAX_SEC",
            "kind": "const",
            "summary": "Лимит записи по умолчанию, секунд",
            "signature": "120"
          },
          {
            "name": "MIN_SEC",
            "kind": "const",
            "summary": "Короче этого запись не отправляется",
            "signature": "3"
          },
          {
            "name": "SpeakingTask",
            "kind": "type",
            "summary": "Разобранное задание устного ответа",
            "signature": "{ prompt: string, maxSec: number }"
          },
          {
            "name": "parseSpeakingTask",
            "kind": "function",
            "summary": "Проверить payload и привести к SpeakingTask",
            "signature": "(raw: unknown) => SpeakingTask | null"
          },
          {
            "name": "sendBlocker",
            "kind": "function",
            "summary": "Причина, почему запись нельзя отправить; null — можно",
            "signature": "(sec: number) => string | null"
          },
          {
            "name": "formatSec",
            "kind": "function",
            "summary": "Секунды в формат мм:сс",
            "signature": "(sec: number) => string"
          }
        ]
      },
      {
        "id": "learningFront/src/features/speaking/ui/speaking-activity.tsx",
        "title": "Рендерер Activity speaking_response",
        "layer": "features",
        "path": "learningFront/src/features/speaking/ui/speaking-activity.tsx",
        "summary": "Запись устного ответа голосом полностью офлайн: лимит времени останавливает запись сам, а не обрезает её молча. Готовая запись ставится в очередь на устройстве и уходит при подключении; разбор произношения приходит позже, после синхронизации.",
        "api": [
          {
            "name": "SpeakingActivity",
            "kind": "component",
            "summary": "Рендерер Activity speaking_response: запись ответа голосом без сети",
            "signature": "({ activity, onComplete }) => JSX"
          }
        ]
      },
      {
        "id": "learningFront/src/features/study-method/index.ts",
        "title": "Публичный API фичи study-method",
        "layer": "features",
        "path": "learningFront/src/features/study-method/index.ts",
        "summary": "Наружу виден только компонент выбора способа изучения шага remember; логика, что можно выбрать и что выбрано сейчас, остаётся внутри фичи.",
        "api": [
          {
            "name": "StudyMethodPicker",
            "kind": "component",
            "summary": "Выбор способа шага remember (реэкспорт)"
          }
        ]
      },
      {
        "id": "learningFront/src/features/study-method/model/options.test.ts",
        "title": "Тесты: выбор способа шага изучения",
        "layer": "тесты",
        "path": "learningFront/src/features/study-method/model/options.test.ts",
        "summary": "Проверяют: предлагаются только способы шага, входящие в курс; без выбора действует первый способ, как решает сервер; выбор человека учитывается, а выбор отключённого модуля игнорируется в пользу способа по умолчанию; выбирать можно только тогда, когда способов больше одного."
      },
      {
        "id": "learningFront/src/features/study-method/model/options.ts",
        "title": "Выбор способа шага изучения",
        "layer": "features",
        "path": "learningFront/src/features/study-method/model/options.ts",
        "summary": "Чистая логика без сети и UI: какие способы шага предложены (только входящие в курс), какой из них действует сейчас и можно ли выбирать вовсе — выбор доступен только тогда, когда способов больше одного. Без явного выбора человека действует первый предложенный способ — то же правило, что и на сервере.",
        "api": [
          {
            "name": "REMEMBER_PURPOSE",
            "kind": "const",
            "summary": "Шаг изучения, для которого сейчас предлагается выбор",
            "signature": "\"remember\""
          },
          {
            "name": "optionsFor",
            "kind": "function",
            "summary": "Способы шага, входящие в курс",
            "signature": "(choice, purpose) => StudyMethodOption[]"
          },
          {
            "name": "activeMethod",
            "kind": "function",
            "summary": "Действующий способ шага: выбор человека или первый предложенный",
            "signature": "(choice, purpose) => string | null"
          },
          {
            "name": "canChoose",
            "kind": "function",
            "summary": "Выбирать можно, только когда способов больше одного",
            "signature": "(choice, purpose) => boolean"
          }
        ]
      },
      {
        "id": "learningFront/src/shared/api/app-version.ts",
        "title": "Версия установленного приложения",
        "layer": "shared",
        "path": "learningFront/src/shared/api/app-version.ts",
        "summary": "Версия из конфигурации сборки, доступная в рантайме через expo-constants; уходит с каждым запросом к backend, по ней сервер решает, не устарел ли клиент.",
        "api": [
          {
            "name": "APP_VERSION",
            "kind": "const",
            "summary": "Версия приложения из сборки, иначе \"0.0.0\"",
            "signature": "string"
          }
        ]
      },
      {
        "id": "learningFront/src/shared/api/client-outdated.test.ts",
        "title": "Тесты: устаревшая версия приложения",
        "layer": "тесты",
        "path": "learningFront/src/shared/api/client-outdated.test.ts",
        "summary": "Проверяют разбор минимальной версии из тела ответа 426 (тело не по форме — null, а не падение), доставку ошибки подписчикам, отсутствие уведомлений после отписки и то, что сообщение ошибки понятно человеку."
      },
      {
        "id": "learningFront/src/shared/api/client-outdated.ts",
        "title": "Устаревшая версия приложения",
        "layer": "shared",
        "path": "learningFront/src/shared/api/client-outdated.ts",
        "summary": "Сервер отвечает кодом 426 на устаревшего клиента; вместо непонятной ошибки на экране это превращается в понятную просьбу обновиться. Подписка на событие нужна потому, что запрос, вызвавший отказ, может идти с любого экрана, а показать сообщение нужно одно на всё приложение.",
        "api": [
          {
            "name": "ClientOutdatedError",
            "kind": "class",
            "summary": "Ошибка «версия устарела» с минимальной допустимой версией"
          },
          {
            "name": "parseOutdatedBody",
            "kind": "function",
            "summary": "Минимальная версия из тела ответа 426",
            "signature": "(text: string) => string | null"
          },
          {
            "name": "onClientOutdated",
            "kind": "function",
            "summary": "Подписка на событие; возвращает отписку",
            "signature": "(listener) => () => void"
          },
          {
            "name": "notifyClientOutdated",
            "kind": "function",
            "summary": "Уведомить подписчиков",
            "signature": "(e: ClientOutdatedError) => void"
          }
        ]
      },
      {
        "id": "learningFront/src/shared/api/error-reporter.test.ts",
        "title": "Тесты: отчёты об ошибках клиента",
        "layer": "тесты",
        "path": "learningFront/src/shared/api/error-reporter.test.ts",
        "summary": "Проверяют сборку отчёта из Error и из чего угодно другого (строка, объект, круговая ссылка, undefined), обрезку длинных сообщения и стека, дедупликацию одинаковой ошибки внутри окна, потолок отчётов за сессию, и то, что сбой или синхронное исключение внутри отправки не выходит наружу и не зацикливает репортёр."
      },
      {
        "id": "learningFront/src/shared/api/error-reporter.ts",
        "title": "Отчёты об ошибках клиента",
        "layer": "shared",
        "path": "learningFront/src/shared/api/error-reporter.ts",
        "summary": "Необработанная ошибка на устройстве уходит на сервер отчётом, по которому видно администратору. Репортёр дедуплицирует одинаковые ошибки, ограничивает число отчётов за сессию и никогда сам не бросает ошибок — иначе сбой отправки отчёта породил бы новый отчёт и цикл; подключается к глобальным обработчикам (ErrorUtils в React Native, события окна на web), не теряя прежний обработчик.",
        "api": [
          {
            "name": "ErrorReport",
            "kind": "type",
            "summary": "Отчёт об ошибке клиента",
            "signature": "{ message, stack?, appVersion, fatal, context }"
          },
          {
            "name": "buildReport",
            "kind": "function",
            "summary": "Собрать отчёт из чего угодно, что бросили вместо Error",
            "signature": "(error, fatal, context?, appVersion?) => ErrorReport"
          },
          {
            "name": "Reporter",
            "kind": "type",
            "summary": "Контракт репортёра",
            "signature": "{ report(error, fatal?, context?): void }"
          },
          {
            "name": "createReporter",
            "kind": "function",
            "summary": "Репортёр с дедупликацией и потолком отчётов за сессию",
            "signature": "(opts) => Reporter"
          },
          {
            "name": "installErrorReporter",
            "kind": "function",
            "summary": "Подключить отчёты к глобальным обработчикам ошибок; возвращает отписку",
            "signature": "() => () => void"
          }
        ]
      },
      {
        "id": "learningFront/src/shared/api/evidence-api.test.ts",
        "title": "Тесты: свидетельство об освоении",
        "layer": "тесты",
        "path": "learningFront/src/shared/api/evidence-api.test.ts",
        "summary": "Проверяют: при связи свидетельство уходит сразу; без связи ждёт в очереди и уходит при следующей отправке без потери остальных записей; отказ сервера по существу не маскируется под отсутствие сети; записи другого аккаунта на общем устройстве не отправляются под чужим именем."
      },
      {
        "id": "learningFront/src/shared/api/evidence-api.ts",
        "title": "Свидетельство об освоении",
        "layer": "shared",
        "path": "learningFront/src/shared/api/evidence-api.ts",
        "summary": "Любой способ изучения сообщает результат в общем формате свидетельства — освоенность считает граф знаний, а не способ. Отправка офлайн-безопасна: без сети свидетельство ждёт в очереди на устройстве, привязанной к владельцу, и уходит при следующей синхронизации; отказ сервера по существу очередь не трогает.",
        "api": [
          {
            "name": "Evidence",
            "kind": "type",
            "summary": "Свидетельство об освоении понятия",
            "signature": "{ domain, conceptId, bloom, score, source }"
          },
          {
            "name": "postEvidence",
            "kind": "const",
            "summary": "Отправить свидетельство на сервер",
            "signature": "(evidence: Evidence) => Promise<{ accepted: number }>"
          },
          {
            "name": "submitEvidence",
            "kind": "function",
            "summary": "Отправить; без сети — оставить в очереди",
            "signature": "(store, evidence) => Promise<'sent' | 'queued'>"
          },
          {
            "name": "flushEvidence",
            "kind": "function",
            "summary": "Отправить накопленную очередь текущего человека",
            "signature": "(store) => Promise<number>"
          }
        ]
      },
      {
        "id": "learningFront/src/shared/api/goal-intake-api.ts",
        "title": "Постановка цели как диалог",
        "layer": "shared",
        "path": "learningFront/src/shared/api/goal-intake-api.ts",
        "summary": "Запросы к диалогу постановки цели: уточняющие вопросы по свободному вводу, пересказ цели моделью, подтверждение пересказа человеком — граф области не строится, пока цель не подтверждена этим путём. Отдельно — предпросмотр объёма пути (сколько областей и понятий) до построения графа, полный и интуитивный вариант.",
        "api": [
          {
            "name": "GoalQuestion",
            "kind": "type",
            "summary": "Уточняющий вопрос к свободному вводу",
            "signature": "{ id, text }"
          },
          {
            "name": "GoalAnswer",
            "kind": "type",
            "summary": "Ответ на вопрос; null — пропущен",
            "signature": "{ question, answer: string | null }"
          },
          {
            "name": "GoalSummary",
            "kind": "type",
            "summary": "Пересказ цели",
            "signature": "{ area, goal, level, wishes: string[] }"
          },
          {
            "name": "GoalIntakeState",
            "kind": "type",
            "summary": "Состояние постановки цели по домену",
            "signature": "{ confirmed, summary: GoalSummary | null }"
          },
          {
            "name": "clarifyGoal",
            "kind": "function",
            "summary": "Уточняющие вопросы к свободному вводу",
            "signature": "(text: string) => Promise<{ questions: GoalQuestion[] }>"
          },
          {
            "name": "summarizeGoal",
            "kind": "function",
            "summary": "Пересказ цели по вводу и ответам",
            "signature": "(text, answers) => Promise<GoalSummary>"
          },
          {
            "name": "confirmGoal",
            "kind": "function",
            "summary": "Подтвердить пересказ по области; только после этого строится граф",
            "signature": "(domain, summary) => Promise<GoalIntakeState>"
          },
          {
            "name": "getGoalIntake",
            "kind": "function",
            "summary": "Состояние постановки цели по домену",
            "signature": "(domain: string) => Promise<GoalIntakeState>"
          },
          {
            "name": "VolumeVariant",
            "kind": "type",
            "summary": "Вариант объёма пути до цели",
            "signature": "{ bloom, precise, domainCount, conceptCount, unbuilt: string[] }"
          },
          {
            "name": "GoalVolume",
            "kind": "type",
            "summary": "Объём пути: полный и интуитивный вариант",
            "signature": "{ goal, registered, variants: { full?, intuitive? }, differs? }"
          },
          {
            "name": "getGoalVolume",
            "kind": "function",
            "summary": "Объём пути до цели по домену",
            "signature": "(domain, target) => Promise<GoalVolume>"
          }
        ]
      },
      {
        "id": "learningFront/src/shared/api/methods-api.ts",
        "title": "Способы изучения",
        "layer": "shared",
        "path": "learningFront/src/shared/api/methods-api.ts",
        "summary": "Запросы к выбору способа для шага изучения: какие способы предложены и что выбрано сейчас. Смена способа пересобирает курс на сервере, но освоенность не трогает — способ меняется, цель остаётся.",
        "api": [
          {
            "name": "StudyMethodOption",
            "kind": "type",
            "summary": "Способ, который предлагает модуль",
            "signature": "{ id, title, purpose, activityType, offline, module, inCourse }"
          },
          {
            "name": "StudyMethodChoice",
            "kind": "type",
            "summary": "Выбор человека и предложенные способы",
            "signature": "{ preferred: Record<string, string>, options: StudyMethodOption[] }"
          },
          {
            "name": "getStudyMethods",
            "kind": "function",
            "summary": "Способы и выбор человека",
            "signature": "() => Promise<StudyMethodChoice>"
          },
          {
            "name": "setStudyMethod",
            "kind": "function",
            "summary": "Выбрать способ шага; null — способ по умолчанию",
            "signature": "(purpose, method) => Promise<StudyMethodChoice>"
          }
        ]
      },
      {
        "id": "learningFront/src/shared/api/voice-outbox.test.ts",
        "title": "Тесты: очередь записей голоса",
        "layer": "тесты",
        "path": "learningFront/src/shared/api/voice-outbox.test.ts",
        "summary": "Проверяют: запись загружается, ставится job расшифровки и файл удаляется с устройства; без сети запись остаётся в очереди вместе с файлом; отказ сервера по существу снимает запись с очереди и удаляет файл; чужая запись на общем устройстве не отправляется."
      },
      {
        "id": "learningFront/src/shared/api/voice-outbox.ts",
        "title": "Очередь записей голоса",
        "layer": "shared",
        "path": "learningFront/src/shared/api/voice-outbox.ts",
        "summary": "Ответ записан без сети — файл ждёт на устройстве и уходит при синхронизации; после успешной загрузки локальный файл удаляется сразу, поскольку голос — биометрия, а на сервере дальше живёт только расшифровка. Запись, которую не отправить из-за сети, остаётся в очереди вместе с файлом; отказ сервера по существу (пустая или слишком большая запись) снимает её с очереди.",
        "api": [
          {
            "name": "VoiceEntry",
            "kind": "type",
            "summary": "Запись в очереди на отправку",
            "signature": "{ userId, responseId, uri, mime }"
          },
          {
            "name": "VoiceDeps",
            "kind": "type",
            "summary": "Загрузка и удаление файла — для подмены в тестах",
            "signature": "{ upload(entry), remove(uri) }"
          },
          {
            "name": "queueVoice",
            "kind": "function",
            "summary": "Поставить запись в очередь",
            "signature": "(store, entry) => Promise<void>"
          },
          {
            "name": "pendingVoice",
            "kind": "function",
            "summary": "Сколько записей ждёт отправки",
            "signature": "(store) => Promise<number>"
          },
          {
            "name": "defaultVoiceDeps",
            "kind": "const",
            "summary": "Настоящая загрузка на backend и удаление файла устройства",
            "signature": "VoiceDeps"
          },
          {
            "name": "flushVoice",
            "kind": "function",
            "summary": "Отправить очередь, поставить job расшифровки, вернуть число отправленных",
            "signature": "(store, deps?) => Promise<number>"
          }
        ]
      },
      {
        "id": "learningFront/src/shared/engine/module/manifest-check.test.ts",
        "title": "Тесты: проверка манифеста модуля (клиент)",
        "layer": "тесты",
        "path": "learningFront/src/shared/engine/module/manifest-check.test.ts",
        "summary": "Проверяют разбор версий и совместимость контракта (мажорная совпадает, минорная модуля не новее ядра), все коды отказа заголовка манифеста — те же, что на сервере, сообщение об отказе называет обе версии, и то, что реестр отклоняет несовместимый по контракту и повторный по идентификатору модуль."
      },
      {
        "id": "learningFront/src/shared/engine/module/manifest-check.ts",
        "title": "Проверка манифеста модуля (клиент)",
        "layer": "shared",
        "path": "learningFront/src/shared/engine/module/manifest-check.ts",
        "summary": "Те же правила и коды отказа, что на сервере (core/manifest.py): идентификатор, название, версия модуля и версия контракта, совместимость мажорной и минорной версии контракта с ядром клиента. Один контракт читается одинаково по обе стороны, поэтому несовместимый модуль не регистрируется ни там, ни там.",
        "api": [
          {
            "name": "CONTRACT_VERSION",
            "kind": "const",
            "summary": "Версия контракта клиентского ядра",
            "signature": "\"1.0\""
          },
          {
            "name": "ManifestErrorCode",
            "kind": "type",
            "summary": "Код причины отказа манифеста",
            "signature": "'bad_id' | 'bad_title' | 'bad_version' | 'bad_contract' | 'contract_incompatible' | 'duplicate_id'"
          },
          {
            "name": "ManifestError",
            "kind": "class",
            "summary": "Ошибка манифеста с кодом причины и id модуля"
          },
          {
            "name": "parseVersion",
            "kind": "function",
            "summary": "Версия \"1.2\" или \"1.2.3\" в массив чисел",
            "signature": "(text: string) => number[] | null"
          },
          {
            "name": "contractCompatible",
            "kind": "function",
            "summary": "Мажорная совпадает, минорная модуля не новее ядра",
            "signature": "(moduleContract, core?) => boolean"
          },
          {
            "name": "checkManifestHeader",
            "kind": "function",
            "summary": "Проверить заголовок манифеста; бросает ManifestError",
            "signature": "(m: ManifestHeader) => void"
          }
        ]
      },
      {
        "id": "learningFront/src/shared/engine/scheduler/card-merge.test.ts",
        "title": "Тесты: слияние карточки повторения с нескольких устройств",
        "layer": "тесты",
        "path": "learningFront/src/shared/engine/scheduler/card-merge.test.ts",
        "summary": "Проверяют: побеждает более позднее ревью независимо от числа повторов; ревьюированная карточка всегда сильнее непросмотренной; при равном времени решают число повторов, затем срывов; одинаковые состояния не заменяют друг друга; время без явной зоны читается как UTC, а мусор вместо даты проигрывает; пустое состояние не ломает сравнение."
      },
      {
        "id": "learningFront/src/shared/engine/scheduler/card-merge.ts",
        "title": "Слияние карточки повторения с нескольких устройств",
        "layer": "shared",
        "path": "learningFront/src/shared/engine/scheduler/card-merge.ts",
        "summary": "Правило слияния — то же, что на сервере (core/srs.py: review_key): побеждает более позднее ревью, а не более поздняя запись, при равном времени решают число повторов и затем срывов. Карточка без ревью или с мусором вместо даты считается старше всех, а время без явной зоны читается как UTC.",
        "api": [
          {
            "name": "compareCardStates",
            "kind": "function",
            "summary": "Сравнить два состояния карточки; >0 — первое свежее",
            "signature": "(a, b) => number"
          },
          {
            "name": "serverVersionWins",
            "kind": "const",
            "summary": "Принять серверную версию вместо локальной, только если строго свежее",
            "signature": "(local, server) => boolean"
          }
        ]
      },
      {
        "id": "learningFront/src/shared/lib/quiz.ts",
        "title": "Вопросы с проверкой ответа",
        "layer": "shared",
        "path": "learningFront/src/shared/lib/quiz.ts",
        "summary": "Общая часть reading- и listening-дриллов: разбор вопросов из payload (форма проверяется, повторы id и битые вопросы отбрасываются) и проверка ответа — для gap принимается любое из допустимых написаний без учёта регистра и лишних пробелов. Проверка детерминирована и считается без сети.",
        "api": [
          {
            "name": "QuestionType",
            "kind": "type",
            "summary": "Тип вопроса",
            "signature": "'mcq' | 'tfng' | 'gap'"
          },
          {
            "name": "QuizQuestion",
            "kind": "type",
            "summary": "Вопрос дрилла",
            "signature": "{ id, type, prompt, options?, answer: string | string[], explanation? }"
          },
          {
            "name": "parseQuestions",
            "kind": "function",
            "summary": "Вопросы из payload; форма проверяется, повторы и битые отбрасываются",
            "signature": "(raw: unknown[]) => QuizQuestion[]"
          },
          {
            "name": "isCorrect",
            "kind": "function",
            "summary": "Ответ верен без учёта регистра и пробелов, для gap — любое допустимое написание",
            "signature": "(q, given) => boolean"
          },
          {
            "name": "QuestionResult",
            "kind": "type",
            "summary": "Результат по одному вопросу",
            "signature": "{ id, correct, given, expected, explanation? }"
          },
          {
            "name": "QuizResult",
            "kind": "type",
            "summary": "Итог проверки по всем вопросам",
            "signature": "{ correct, total, fraction, details: QuestionResult[] }"
          },
          {
            "name": "gradeQuestions",
            "kind": "function",
            "summary": "Проверить ответы по всем вопросам",
            "signature": "(questions, answers) => QuizResult"
          }
        ]
      },
      {
        "id": "scripts/backup-db.sh",
        "title": "Резервная копия базы Praxis",
        "layer": "скрипты",
        "path": "scripts/backup-db.sh",
        "summary": "Снимает сжатый дамп Postgres через pg_dump в docker compose и удаляет дампы старше срока хранения; пустой дамп (сбой pg_dump) отменяет копию, а не оставляет её как рабочую. Дамп без проверки восстановления не считается бэкапом — следующим шагом запускается scripts/restore-check.sh."
      },
      {
        "id": "scripts/deploy-staging.sh",
        "title": "Деплой staging из main",
        "layer": "скрипты",
        "path": "scripts/deploy-staging.sh",
        "summary": "Обновляет код и сабмодули до main, собирает образы, поднимает базу, перед миграциями снимает резервную копию и проверяет её восстановление, поднимает API и воркер и ждёт /health. Если /health не ответил — падает с инструкцией по откату, не трогая прежние образы и копию базы.",
        "api": []
      },
      {
        "id": "scripts/live_checks.py",
        "title": "Живые проверки на реальном провайдере",
        "layer": "скрипты",
        "path": "scripts/live_checks.py",
        "summary": "Проверки V-0011/V-0075/V-0077/V-0057 на настоящем провайдере модели, не заглушке: граф по теме с расходом токенов, оценка эссе IELTS/TOEFL по рубрикам, и плейсмент по живому графу, где зонды расширяют границу освоенности. Заглушка вместо реальной модели считается провалом — признак: нулевой расход токенов в llm_usage.",
        "api": [
          {
            "name": "CHECKS",
            "kind": "const",
            "summary": "Имя проверки → функция",
            "signature": "{ llm, ielts, rubrics, placement }"
          },
          {
            "name": "run_llm",
            "kind": "function",
            "summary": "Граф по теме и расход токенов (V-0011)",
            "signature": "() => str"
          },
          {
            "name": "run_ielts",
            "kind": "function",
            "summary": "Эссе IELTS Task 2 по четырём критериям (V-0077)",
            "signature": "() => str"
          },
          {
            "name": "run_rubrics",
            "kind": "function",
            "summary": "Task 1 и TOEFL по своим рубрикам (V-0075)",
            "signature": "() => str"
          },
          {
            "name": "run_placement",
            "kind": "function",
            "summary": "Плейсмент по живому графу: зонды расширяют границу (V-0057)",
            "signature": "() => str"
          }
        ]
      },
      {
        "id": "scripts/restore-check.sh",
        "title": "Проверка восстановления резервной копии",
        "layer": "скрипты",
        "path": "scripts/restore-check.sh",
        "summary": "Накатывает копию во временную базу restore_check (рабочая база не трогается), сверяет версию миграций и число таблиц с рабочей базой и удаляет временную базу. Без аргумента берёт самый свежий дамп из .data/backups; несовпадение структуры — отказ с кодом 1."
      }
    ],
    "imports": [
      {
        "from": "learningFront/src/features/reading-drill/index.ts",
        "to": "learningFront/src/features/reading-drill/ui/reading-drill-activity.tsx",
        "evidence": {
          "path": "learningFront/src/features/reading-drill/index.ts",
          "line": 1,
          "fragment": "export { ReadingDrillActivity } from './ui/reading-drill-activity';"
        }
      },
      {
        "from": "learningFront/src/features/reading-drill/model/reading-model.ts",
        "to": "learningFront/src/shared/engine/index.ts",
        "evidence": {
          "path": "learningFront/src/features/reading-drill/model/reading-model.ts",
          "line": 4,
          "fragment": "import type { Grade } from '@/shared/engine';"
        }
      },
      {
        "from": "learningFront/src/features/reading-drill/model/reading-model.test.ts",
        "to": "learningFront/src/features/reading-drill/model/reading-model.ts",
        "evidence": {
          "path": "learningFront/src/features/reading-drill/model/reading-model.test.ts",
          "line": 11,
          "fragment": "} from './reading-model';"
        }
      },
      {
        "from": "learningFront/src/features/reading-drill/ui/reading-drill-activity.tsx",
        "to": "learningFront/src/entities/session/index.ts",
        "evidence": {
          "path": "learningFront/src/features/reading-drill/ui/reading-drill-activity.tsx",
          "line": 6,
          "fragment": "import { useSession } from '@/entities/session';"
        }
      },
      {
        "from": "learningFront/src/features/reading-drill/ui/reading-drill-activity.tsx",
        "to": "learningFront/src/shared/engine/index.ts",
        "evidence": {
          "path": "learningFront/src/features/reading-drill/ui/reading-drill-activity.tsx",
          "line": 7,
          "fragment": "import type { ActivityRendererProps } from '@/shared/engine';"
        }
      },
      {
        "from": "learningFront/src/features/reading-drill/ui/reading-drill-activity.tsx",
        "to": "learningFront/src/shared/api/index.ts",
        "evidence": {
          "path": "learningFront/src/features/reading-drill/ui/reading-drill-activity.tsx",
          "line": 8,
          "fragment": "import { createJobQueue, getLocalStore } from '@/shared/api';"
        }
      },
      {
        "from": "learningFront/src/features/reading-drill/ui/reading-drill-activity.tsx",
        "to": "learningFront/src/shared/lib/index.ts",
        "evidence": {
          "path": "learningFront/src/features/reading-drill/ui/reading-drill-activity.tsx",
          "line": 9,
          "fragment": "import { newId } from '@/shared/lib';"
        }
      },
      {
        "from": "learningFront/src/features/reading-drill/ui/reading-drill-activity.tsx",
        "to": "learningFront/src/shared/ui/index.ts",
        "evidence": {
          "path": "learningFront/src/features/reading-drill/ui/reading-drill-activity.tsx",
          "line": 22,
          "fragment": "} from '@/shared/ui';"
        }
      },
      {
        "from": "learningFront/src/features/reading-drill/ui/reading-drill-activity.tsx",
        "to": "learningFront/src/features/reading-drill/model/reading-model.ts",
        "evidence": {
          "path": "learningFront/src/features/reading-drill/ui/reading-drill-activity.tsx",
          "line": 33,
          "fragment": "} from '../model/reading-model';"
        }
      },
      {
        "from": "learningFront/src/widgets/module-registry/index.ts",
        "to": "learningFront/src/features/reading-drill/index.ts",
        "evidence": {
          "path": "learningFront/src/widgets/module-registry/index.ts",
          "line": 31,
          "fragment": "import { ReadingDrillActivity } from '@/features/reading-drill';"
        }
      },
      {
        "from": "learningFront/src/features/speaking/index.ts",
        "to": "learningFront/src/features/speaking/ui/speaking-activity.tsx",
        "evidence": {
          "path": "learningFront/src/features/speaking/index.ts",
          "line": 1,
          "fragment": "export { SpeakingActivity } from './ui/speaking-activity';"
        }
      },
      {
        "from": "learningFront/src/features/speaking/model/speaking-model.test.ts",
        "to": "learningFront/src/features/speaking/model/speaking-model.ts",
        "evidence": {
          "path": "learningFront/src/features/speaking/model/speaking-model.test.ts",
          "line": 2,
          "fragment": "import { DEFAULT_MAX_SEC, formatSec, parseSpeakingTask, sendBlocker } from './speaking-model';"
        }
      },
      {
        "from": "learningFront/src/features/speaking/ui/speaking-activity.tsx",
        "to": "learningFront/src/entities/session/index.ts",
        "evidence": {
          "path": "learningFront/src/features/speaking/ui/speaking-activity.tsx",
          "line": 12,
          "fragment": "import { useSession } from '@/entities/session';"
        }
      },
      {
        "from": "learningFront/src/features/speaking/ui/speaking-activity.tsx",
        "to": "learningFront/src/shared/api/index.ts",
        "evidence": {
          "path": "learningFront/src/features/speaking/ui/speaking-activity.tsx",
          "line": 13,
          "fragment": "import { getLocalStore, queueVoice } from '@/shared/api';"
        }
      },
      {
        "from": "learningFront/src/features/speaking/ui/speaking-activity.tsx",
        "to": "learningFront/src/shared/engine/index.ts",
        "evidence": {
          "path": "learningFront/src/features/speaking/ui/speaking-activity.tsx",
          "line": 14,
          "fragment": "import type { ActivityRendererProps } from '@/shared/engine';"
        }
      },
      {
        "from": "learningFront/src/features/speaking/ui/speaking-activity.tsx",
        "to": "learningFront/src/shared/lib/index.ts",
        "evidence": {
          "path": "learningFront/src/features/speaking/ui/speaking-activity.tsx",
          "line": 15,
          "fragment": "import { newId } from '@/shared/lib';"
        }
      },
      {
        "from": "learningFront/src/features/speaking/ui/speaking-activity.tsx",
        "to": "learningFront/src/shared/ui/index.ts",
        "evidence": {
          "path": "learningFront/src/features/speaking/ui/speaking-activity.tsx",
          "line": 16,
          "fragment": "import { Body, Button, Card, Lead, Muted, Note, space } from '@/shared/ui';"
        }
      },
      {
        "from": "learningFront/src/features/speaking/ui/speaking-activity.tsx",
        "to": "learningFront/src/features/speaking/model/speaking-model.ts",
        "evidence": {
          "path": "learningFront/src/features/speaking/ui/speaking-activity.tsx",
          "line": 17,
          "fragment": "import { formatSec, parseSpeakingTask, sendBlocker } from '../model/speaking-model';"
        }
      },
      {
        "from": "learningFront/src/widgets/module-registry/index.ts",
        "to": "learningFront/src/features/speaking/index.ts",
        "evidence": {
          "path": "learningFront/src/widgets/module-registry/index.ts",
          "line": 32,
          "fragment": "import { SpeakingActivity } from '@/features/speaking';"
        }
      },
      {
        "from": "learningFront/src/features/study-method/index.ts",
        "to": "learningFront/src/features/study-method/ui/study-method-picker.tsx",
        "evidence": {
          "path": "learningFront/src/features/study-method/index.ts",
          "line": 1,
          "fragment": "export { StudyMethodPicker } from './ui/study-method-picker';"
        }
      },
      {
        "from": "learningFront/src/features/study-method/model/options.ts",
        "to": "learningFront/src/shared/api/index.ts",
        "evidence": {
          "path": "learningFront/src/features/study-method/model/options.ts",
          "line": 2,
          "fragment": "import type { StudyMethodChoice, StudyMethodOption } from '@/shared/api';"
        }
      },
      {
        "from": "learningFront/src/features/study-method/model/options.test.ts",
        "to": "learningFront/src/features/study-method/model/options.ts",
        "evidence": {
          "path": "learningFront/src/features/study-method/model/options.test.ts",
          "line": 3,
          "fragment": "import { activeMethod, canChoose, optionsFor } from './options';"
        }
      },
      {
        "from": "learningFront/src/features/study-method/ui/study-method-picker.tsx",
        "to": "learningFront/src/features/study-method/model/options.ts",
        "evidence": {
          "path": "learningFront/src/features/study-method/ui/study-method-picker.tsx",
          "line": 8,
          "fragment": "import { activeMethod, canChoose, optionsFor, REMEMBER_PURPOSE } from '../model/options';"
        }
      },
      {
        "from": "learningFront/src/pages/profile/ui/profile-screen.tsx",
        "to": "learningFront/src/features/study-method/index.ts",
        "evidence": {
          "path": "learningFront/src/pages/profile/ui/profile-screen.tsx",
          "line": 6,
          "fragment": "import { StudyMethodPicker } from '@/features/study-method';"
        }
      },
      {
        "from": "learningFront/src/features/mnemonic-recall/ui/mnemonic-activity.tsx",
        "to": "learningFront/src/shared/api/index.ts",
        "evidence": {
          "path": "learningFront/src/features/mnemonic-recall/ui/mnemonic-activity.tsx",
          "line": 6,
          "fragment": "import { getLocalStore, submitEvidence } from '@/shared/api';"
        }
      },
      {
        "from": "learningFront/src/features/mnemonic-recall/ui/mnemonic-activity.tsx",
        "to": "learningFront/src/shared/engine/index.ts",
        "evidence": {
          "path": "learningFront/src/features/mnemonic-recall/ui/mnemonic-activity.tsx",
          "line": 7,
          "fragment": "import type { ActivityRendererProps } from '@/shared/engine';"
        }
      },
      {
        "from": "learningFront/src/features/mnemonic-recall/ui/mnemonic-activity.tsx",
        "to": "learningFront/src/shared/ui/index.ts",
        "evidence": {
          "path": "learningFront/src/features/mnemonic-recall/ui/mnemonic-activity.tsx",
          "line": 8,
          "fragment": "import { Body, Button, Lead, Muted, Note, space, Title } from '@/shared/ui';"
        }
      },
      {
        "from": "learningFront/src/features/mnemonic-recall/ui/mnemonic-activity.tsx",
        "to": "learningFront/src/features/mnemonic-recall/model/rating.ts",
        "evidence": {
          "path": "learningFront/src/features/mnemonic-recall/ui/mnemonic-activity.tsx",
          "line": 9,
          "fragment": "import { MNEMONIC_SOURCE, SELF_RATINGS, scoreOf, type SelfRating } from '../model/rating';"
        }
      },
      {
        "from": "learningFront/src/shared/api/error-reporter.ts",
        "to": "learningFront/src/shared/api/http.ts",
        "evidence": {
          "path": "learningFront/src/shared/api/error-reporter.ts",
          "line": 5,
          "fragment": "import { api } from './http';"
        }
      },
      {
        "from": "learningFront/src/shared/api/error-reporter.ts",
        "to": "learningFront/src/shared/api/app-version.ts",
        "evidence": {
          "path": "learningFront/src/shared/api/error-reporter.ts",
          "line": 6,
          "fragment": "import { APP_VERSION } from './app-version';"
        }
      },
      {
        "from": "learningFront/src/shared/api/error-reporter.test.ts",
        "to": "learningFront/src/shared/api/error-reporter.ts",
        "evidence": {
          "path": "learningFront/src/shared/api/error-reporter.test.ts",
          "line": 2,
          "fragment": "import { buildReport, createReporter } from './error-reporter';"
        }
      },
      {
        "from": "learningFront/src/shared/api/client-outdated.test.ts",
        "to": "learningFront/src/shared/api/client-outdated.ts",
        "evidence": {
          "path": "learningFront/src/shared/api/client-outdated.test.ts",
          "line": 7,
          "fragment": "} from './client-outdated';"
        }
      },
      {
        "from": "learningFront/src/shared/api/evidence-api.ts",
        "to": "learningFront/src/shared/engine/index.ts",
        "evidence": {
          "path": "learningFront/src/shared/api/evidence-api.ts",
          "line": 4,
          "fragment": "import type { LocalStore } from '@/shared/engine';"
        }
      },
      {
        "from": "learningFront/src/shared/api/evidence-api.ts",
        "to": "learningFront/src/shared/api/current-user.ts",
        "evidence": {
          "path": "learningFront/src/shared/api/evidence-api.ts",
          "line": 5,
          "fragment": "import { getCurrentUserId } from './current-user';"
        }
      },
      {
        "from": "learningFront/src/shared/api/evidence-api.ts",
        "to": "learningFront/src/shared/api/http.ts",
        "evidence": {
          "path": "learningFront/src/shared/api/evidence-api.ts",
          "line": 6,
          "fragment": "import { api, NetworkError } from './http';"
        }
      },
      {
        "from": "learningFront/src/shared/api/evidence-api.test.ts",
        "to": "learningFront/src/shared/api/evidence-api.ts",
        "evidence": {
          "path": "learningFront/src/shared/api/evidence-api.test.ts",
          "line": 3,
          "fragment": "import { flushEvidence, submitEvidence, type Evidence } from './evidence-api';"
        }
      },
      {
        "from": "learningFront/src/shared/api/evidence-api.test.ts",
        "to": "learningFront/src/shared/api/db/sqlite-local-store.web.ts",
        "evidence": {
          "path": "learningFront/src/shared/api/evidence-api.test.ts",
          "line": 2,
          "fragment": "import { SqliteLocalStore } from './db/sqlite-local-store.web';"
        }
      },
      {
        "from": "learningFront/src/shared/api/goal-intake-api.ts",
        "to": "learningFront/src/shared/api/http.ts",
        "evidence": {
          "path": "learningFront/src/shared/api/goal-intake-api.ts",
          "line": 3,
          "fragment": "import { api } from './http';"
        }
      },
      {
        "from": "learningFront/src/shared/api/methods-api.ts",
        "to": "learningFront/src/shared/api/http.ts",
        "evidence": {
          "path": "learningFront/src/shared/api/methods-api.ts",
          "line": 2,
          "fragment": "import { api } from './http';"
        }
      },
      {
        "from": "learningFront/src/shared/api/voice-outbox.ts",
        "to": "learningFront/src/shared/engine/index.ts",
        "evidence": {
          "path": "learningFront/src/shared/api/voice-outbox.ts",
          "line": 5,
          "fragment": "import type { LocalStore } from '@/shared/engine';"
        }
      },
      {
        "from": "learningFront/src/shared/api/voice-outbox.ts",
        "to": "learningFront/src/shared/api/current-user.ts",
        "evidence": {
          "path": "learningFront/src/shared/api/voice-outbox.ts",
          "line": 7,
          "fragment": "import { getCurrentUserId } from './current-user';"
        }
      },
      {
        "from": "learningFront/src/shared/api/voice-outbox.ts",
        "to": "learningFront/src/shared/api/http.ts",
        "evidence": {
          "path": "learningFront/src/shared/api/voice-outbox.ts",
          "line": 8,
          "fragment": "import { apiUrl, ApiError, CLIENT_HEADERS, NetworkError, getBaseUrl } from './http';"
        }
      },
      {
        "from": "learningFront/src/shared/api/voice-outbox.ts",
        "to": "learningFront/src/shared/api/token.ts",
        "evidence": {
          "path": "learningFront/src/shared/api/voice-outbox.ts",
          "line": 9,
          "fragment": "import { getToken } from './token';"
        }
      },
      {
        "from": "learningFront/src/shared/api/voice-outbox.test.ts",
        "to": "learningFront/src/shared/api/db/sqlite-local-store.web.ts",
        "evidence": {
          "path": "learningFront/src/shared/api/voice-outbox.test.ts",
          "line": 2,
          "fragment": "import { SqliteLocalStore } from './db/sqlite-local-store.web';"
        }
      },
      {
        "from": "learningFront/src/shared/api/voice-outbox.test.ts",
        "to": "learningFront/src/shared/api/http.ts",
        "evidence": {
          "path": "learningFront/src/shared/api/voice-outbox.test.ts",
          "line": 17,
          "fragment": "vi.mock('./http', () => {"
        }
      },
      {
        "from": "learningFront/src/shared/api/voice-outbox.test.ts",
        "to": "learningFront/src/shared/api/voice-outbox.ts",
        "evidence": {
          "path": "learningFront/src/shared/api/voice-outbox.test.ts",
          "line": 10,
          "fragment": "} from './voice-outbox';"
        }
      },
      {
        "from": "learningFront/src/shared/api/index.ts",
        "to": "learningFront/src/shared/api/app-version.ts",
        "evidence": {
          "path": "learningFront/src/shared/api/index.ts",
          "line": 42,
          "fragment": "export { APP_VERSION } from './app-version';"
        }
      },
      {
        "from": "learningFront/src/shared/api/index.ts",
        "to": "learningFront/src/shared/api/client-outdated.ts",
        "evidence": {
          "path": "learningFront/src/shared/api/index.ts",
          "line": 41,
          "fragment": "export { ClientOutdatedError, onClientOutdated } from './client-outdated';"
        }
      },
      {
        "from": "learningFront/src/shared/api/index.ts",
        "to": "learningFront/src/shared/api/error-reporter.ts",
        "evidence": {
          "path": "learningFront/src/shared/api/index.ts",
          "line": 43,
          "fragment": "export { installErrorReporter } from './error-reporter';"
        }
      },
      {
        "from": "learningFront/src/shared/api/index.ts",
        "to": "learningFront/src/shared/api/evidence-api.ts",
        "evidence": {
          "path": "learningFront/src/shared/api/index.ts",
          "line": 31,
          "fragment": "export { flushEvidence, postEvidence, submitEvidence, type Evidence } from './evidence-api';"
        }
      },
      {
        "from": "learningFront/src/shared/api/index.ts",
        "to": "learningFront/src/shared/api/goal-intake-api.ts",
        "evidence": {
          "path": "learningFront/src/shared/api/index.ts",
          "line": 30,
          "fragment": "} from './goal-intake-api';"
        }
      },
      {
        "from": "learningFront/src/shared/api/index.ts",
        "to": "learningFront/src/shared/api/methods-api.ts",
        "evidence": {
          "path": "learningFront/src/shared/api/index.ts",
          "line": 37,
          "fragment": "} from './methods-api';"
        }
      },
      {
        "from": "learningFront/src/shared/api/index.ts",
        "to": "learningFront/src/shared/api/voice-outbox.ts",
        "evidence": {
          "path": "learningFront/src/shared/api/index.ts",
          "line": 45,
          "fragment": "export { flushVoice, pendingVoice, queueVoice } from './voice-outbox';"
        }
      },
      {
        "from": "learningFront/src/shared/engine/module/registry.ts",
        "to": "learningFront/src/shared/engine/module/manifest-check.ts",
        "evidence": {
          "path": "learningFront/src/shared/engine/module/registry.ts",
          "line": 2,
          "fragment": "import { ManifestError, checkManifestHeader } from './manifest-check';"
        }
      },
      {
        "from": "learningFront/src/shared/engine/module/manifest-check.test.ts",
        "to": "learningFront/src/shared/engine/module/manifest-check.ts",
        "evidence": {
          "path": "learningFront/src/shared/engine/module/manifest-check.test.ts",
          "line": 8,
          "fragment": "} from './manifest-check';"
        }
      },
      {
        "from": "learningFront/src/shared/engine/module/manifest-check.test.ts",
        "to": "learningFront/src/shared/engine/module/registry.ts",
        "evidence": {
          "path": "learningFront/src/shared/engine/module/manifest-check.test.ts",
          "line": 9,
          "fragment": "import { createModuleRegistry } from './registry';"
        }
      },
      {
        "from": "learningFront/src/shared/engine/module/manifest-check.test.ts",
        "to": "learningFront/src/shared/engine/module/manifest.ts",
        "evidence": {
          "path": "learningFront/src/shared/engine/module/manifest-check.test.ts",
          "line": 10,
          "fragment": "import type { ModuleManifest } from './manifest';"
        }
      },
      {
        "from": "learningFront/src/shared/engine/index.ts",
        "to": "learningFront/src/shared/engine/module/manifest-check.ts",
        "evidence": {
          "path": "learningFront/src/shared/engine/index.ts",
          "line": 35,
          "fragment": "export { CONTRACT_VERSION, ManifestError } from './module/manifest-check';"
        }
      },
      {
        "from": "learningFront/src/shared/engine/index.ts",
        "to": "learningFront/src/shared/engine/scheduler/card-merge.ts",
        "evidence": {
          "path": "learningFront/src/shared/engine/index.ts",
          "line": 40,
          "fragment": "export { compareCardStates, serverVersionWins } from './scheduler/card-merge';"
        }
      },
      {
        "from": "learningFront/src/shared/engine/scheduler/card-merge.test.ts",
        "to": "learningFront/src/shared/engine/scheduler/card-merge.ts",
        "evidence": {
          "path": "learningFront/src/shared/engine/scheduler/card-merge.test.ts",
          "line": 2,
          "fragment": "import { compareCardStates, serverVersionWins } from './card-merge';"
        }
      },
      {
        "from": "scripts/deploy-staging.sh",
        "to": "scripts/backup-db.sh",
        "evidence": {
          "path": "scripts/deploy-staging.sh",
          "line": 35,
          "fragment": "BACKUP=\"$(scripts/backup-db.sh)\""
        }
      },
      {
        "from": "scripts/deploy-staging.sh",
        "to": "scripts/restore-check.sh",
        "evidence": {
          "path": "scripts/deploy-staging.sh",
          "line": 36,
          "fragment": "scripts/restore-check.sh \"$BACKUP\""
        }
      }
    ],
    "groups": [
      {
        "id": "reading-drill-frontend",
        "title": "Reading-дрилл (клиент)",
        "summary": "Разбор и прохождение reading-дрилла офлайн: текст, вопросы, таймер, мгновенная проверка и рендерер активности.",
        "modules": [
          "learningFront/src/features/reading-drill/index.ts",
          "learningFront/src/features/reading-drill/model/reading-model.ts",
          "learningFront/src/features/reading-drill/ui/reading-drill-activity.tsx"
        ],
        "capability": "reception-drills"
      },
      {
        "id": "quiz-engine-frontend",
        "title": "Проверка ответов дриллов чтения и аудирования",
        "summary": "Общий разбор и детерминированная проверка вопросов (mcq/tfng/gap), используемая reading- и listening-дриллом.",
        "modules": [
          "learningFront/src/shared/lib/quiz.ts"
        ],
        "capability": "reception-drills"
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
        "capability": "speaking"
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
        "capability": "method-switch"
      },
      {
        "id": "mnemonic-activity-frontend",
        "title": "Рендерер техники «первые буквы»",
        "summary": "Экранная часть техники запоминания по первым буквам: подсказка, ответ, самооценка.",
        "modules": [
          "learningFront/src/features/mnemonic-recall/ui/mnemonic-activity.tsx"
        ],
        "capability": "memorize-techniques"
      },
      {
        "id": "mastery-evidence-frontend",
        "title": "Свидетельство об освоении (клиент)",
        "summary": "Отправка результата любого способа изучения в общем формате свидетельства, с офлайн-очередью на устройстве.",
        "modules": [
          "learningFront/src/shared/api/evidence-api.ts"
        ],
        "capability": "mastery-evidence"
      },
      {
        "id": "goal-intake-api-frontend",
        "title": "API постановки цели (клиент)",
        "summary": "Запросы диалога постановки цели: уточнение, пересказ, подтверждение, предпросмотр объёма пути.",
        "modules": [
          "learningFront/src/shared/api/goal-intake-api.ts"
        ],
        "capability": "goal-intake"
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
        "capability": "platform-release"
      },
      {
        "id": "client-version-gate-frontend",
        "title": "Проверка версии клиента",
        "summary": "Версия приложения, уходящая с запросами, и обработка отказа 426 понятным сообщением об обновлении.",
        "modules": [
          "learningFront/src/shared/api/app-version.ts",
          "learningFront/src/shared/api/client-outdated.ts"
        ],
        "capability": "platform-release"
      },
      {
        "id": "client-error-reports-frontend",
        "title": "Отчёты об ошибках клиента",
        "summary": "Необработанные ошибки устройства уходят на сервер отчётом, с дедупликацией и потолком за сессию.",
        "modules": [
          "learningFront/src/shared/api/error-reporter.ts"
        ],
        "capability": "platform-release"
      },
      {
        "id": "module-contract-check-frontend",
        "title": "Проверка манифеста модуля (клиент)",
        "summary": "Единые с сервером правила и коды отказа манифеста модуля.",
        "modules": [
          "learningFront/src/shared/engine/module/manifest-check.ts"
        ],
        "capability": "activity-engine"
      },
      {
        "id": "srs-card-merge-frontend",
        "title": "Слияние карточки повторения (клиент)",
        "summary": "Правило выбора более свежей версии карточки повторения при синхронизации с нескольких устройств.",
        "modules": [
          "learningFront/src/shared/engine/scheduler/card-merge.ts"
        ],
        "capability": "srs-error-log"
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
        "id": "mem-client-outdated-listeners",
        "kind": "memory",
        "where": "модульный Set в client-outdated.ts",
        "title": "Подписчики на «устаревшая версия приложения» (in-process)"
      },
      {
        "id": "file-voice-recording-device",
        "kind": "file",
        "where": "expo-audio: recorder.uri (временная запись на устройстве до отправки)",
        "title": "Запись устного ответа на устройстве до отправки"
      },
      {
        "id": "file-backup-dir",
        "kind": "file",
        "where": ".data/backups (по умолчанию, параметр скрипта)",
        "title": "Каталог резервных копий базы"
      }
    ],
    "flows": [
      {
        "from": "learningFront/src/shared/api/client-outdated.ts",
        "to": "mem-client-outdated-listeners",
        "direction": "write",
        "evidence": {
          "path": "learningFront/src/shared/api/client-outdated.ts",
          "line": 27,
          "fragment": "listeners.add(listener);"
        }
      },
      {
        "from": "learningFront/src/shared/api/client-outdated.ts",
        "to": "mem-client-outdated-listeners",
        "direction": "read",
        "evidence": {
          "path": "learningFront/src/shared/api/client-outdated.ts",
          "line": 32,
          "fragment": "for (const l of listeners) l(e);"
        }
      },
      {
        "from": "learningFront/src/shared/api/voice-outbox.ts",
        "to": "http-backend-api",
        "direction": "write",
        "evidence": {
          "path": "learningFront/src/shared/api/voice-outbox.ts",
          "line": 58,
          "fragment": "res = await fetch(apiUrl('/languages/speaking/audio'), {"
        }
      },
      {
        "from": "learningFront/src/shared/api/voice-outbox.ts",
        "to": "file-voice-recording-device",
        "direction": "write",
        "evidence": {
          "path": "learningFront/src/shared/api/voice-outbox.ts",
          "line": 72,
          "fragment": "if (f.exists) f.delete();"
        }
      },
      {
        "from": "scripts/backup-db.sh",
        "to": "db-postgres",
        "direction": "read",
        "evidence": {
          "path": "scripts/backup-db.sh",
          "line": 23,
          "fragment": "pg_dump -U \"$PGUSER\" -d \"$PGDB\" --clean --if-exists --no-owner"
        }
      },
      {
        "from": "scripts/backup-db.sh",
        "to": "file-backup-dir",
        "direction": "write",
        "evidence": {
          "path": "scripts/backup-db.sh",
          "line": 23,
          "fragment": "gzip > \"$FILE\""
        }
      },
      {
        "from": "scripts/backup-db.sh",
        "to": "file-backup-dir",
        "direction": "write",
        "evidence": {
          "path": "scripts/backup-db.sh",
          "line": 31,
          "fragment": "find \"$DIR\" -name 'praxis-*.sql.gz' -mtime \"+$KEEP_DAYS\" -delete"
        }
      },
      {
        "from": "scripts/restore-check.sh",
        "to": "file-backup-dir",
        "direction": "read",
        "evidence": {
          "path": "scripts/restore-check.sh",
          "line": 30,
          "fragment": "gzip -dc \"$FILE\""
        }
      },
      {
        "from": "scripts/restore-check.sh",
        "to": "db-postgres",
        "direction": "write",
        "evidence": {
          "path": "scripts/restore-check.sh",
          "line": 29,
          "fragment": "CREATE DATABASE $TMPDB"
        }
      },
      {
        "from": "scripts/restore-check.sh",
        "to": "db-postgres",
        "direction": "read",
        "evidence": {
          "path": "scripts/restore-check.sh",
          "line": 35,
          "fragment": "LIVE_V=\"$(version \"$PGDB\")\""
        }
      },
      {
        "from": "scripts/deploy-staging.sh",
        "to": "db-postgres",
        "direction": "read",
        "evidence": {
          "path": "scripts/deploy-staging.sh",
          "line": 33,
          "fragment": "select 1 from alembic_version"
        }
      },
      {
        "from": "scripts/deploy-staging.sh",
        "to": "http-backend-api",
        "direction": "read",
        "evidence": {
          "path": "scripts/deploy-staging.sh",
          "line": 45,
          "fragment": "urllib.request.urlopen('http://localhost:8000/health'"
        }
      },
      {
        "from": "scripts/live_checks.py",
        "to": "http-backend-api",
        "direction": "both",
        "evidence": {
          "path": "scripts/live_checks.py",
          "line": 72,
          "fragment": "with OPENER.open(req, timeout=1200) as resp:"
        }
      },
      {
        "from": "scripts/live_checks.py",
        "to": "db-postgres",
        "direction": "read",
        "evidence": {
          "path": "scripts/live_checks.py",
          "line": 95,
          "fragment": "select coalesce(sum(prompt_tokens + completion_tokens), 0) from llm_usage"
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
        "from": "/course",
        "to": "POST /evidence",
        "evidence": {
          "path": "learningFront/src/shared/api/evidence-api.ts",
          "line": 27,
          "fragment": "api<{ accepted: number }>('/evidence'"
        }
      },
      {
        "from": "/activities",
        "to": "POST /evidence",
        "evidence": {
          "path": "learningFront/src/shared/api/evidence-api.ts",
          "line": 27,
          "fragment": "api<{ accepted: number }>('/evidence'"
        }
      }
    ]
  }
}
```

## Журнал

- 2026-10-05 · заведена черновиком · модель
- 2026-10-05 · на подтверждение · architect
- 2026-10-05 · подтверждён · architect
- 2026-10-03 · обновлены номера строк в свидетельствах (2): код сдвинулся, содержание карты не менялось · claude
- 2026-10-07 · обновлены номера строк и фрагмент в свидетельствах по scripts/live_checks.py (71→72, timeout 300→1200; 94→95): код сдвинулся, содержание карты не менялось · claude
