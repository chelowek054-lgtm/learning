---
id: M-0023
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
        "id": "learningBack/tests/test_provider_errors.py",
        "title": "Тесты: сбой провайдера модели — 502 вместо 500",
        "layer": "тесты",
        "path": "learningBack/tests/test_provider_errors.py",
        "summary": "Проверяют качество ответов API при сбое провайдера модели: ConnectError во внешнем вызове превращается в 502 с сообщением «повторите», не протекая деталями провайдера наружу; ProviderError остаётся подклассом RuntimeError, чтобы старые обработчики её не теряли."
      },
      {
        "id": "learningBack/tests/test_reading.py",
        "title": "Тесты: reading-дрилл для языковых предметов",
        "layer": "тесты",
        "path": "learningBack/tests/test_reading.py",
        "summary": "Проверяют T-0036/R-0022: языковые предметы (IELTS, TOEFL) при provision получают один офлайн reading-дрилл с лимитом времени и текстом, повторный provision его не дублирует, предмет не из языков дрилл не получает, а у демонстрационного payload каждый вопрос (mcq/tfng/gap) имеет проверяемый ответ."
      },
      {
        "id": "learningBack/tests/test_retention.py",
        "title": "Тесты: удаление данных по срокам хранения",
        "layer": "тесты",
        "path": "learningBack/tests/test_retention.py",
        "summary": "Проверяют T-0028/R-0018/V-0028: данные с истёкшим сроком хранения удаляются по типу, а незавершённая работа (pending/failed job) не трогается вне зависимости от возраста; удаление идёт по каждому человеку отдельно, повторный запуск ничего не находит, а типы без срока хранения не чистятся вовсе; отдельно — что ручной запуск через POST /retention/run доступен только администратору."
      },
      {
        "id": "learningBack/tests/test_second_technique.py",
        "title": "Тесты: вторая техника запоминания и смена способа",
        "layer": "тесты",
        "path": "learningBack/tests/test_second_technique.py",
        "summary": "Проверяют T-0063/T-0062/V-0086: техника «вспомнить по первым буквам» — такой же способ шага remember, как и повторение, её payload строит сам модуль по данным узла; человек может выбрать способ, переключение не теряет освоенность, карточки и прогресс курса, а отключённый модуль возвращает курс к способу по умолчанию; самооценка по любой технике двигает одну и ту же освоенность."
      },
      {
        "id": "learningBack/tests/test_speaking.py",
        "title": "Тесты: устный ответ — полный цикл",
        "layer": "тесты",
        "path": "learningBack/tests/test_speaking.py",
        "summary": "Проверяют T-0040…T-0043: метрики темпа и пауз по таймингам слов, понятную ошибку на тихой/пустой/слишком длинной записи, расшифровку job'ом с удалением записи после успеха и постановкой задачи оценки, оценку по рубрике с пометкой о приблизительности и карточкой ошибки произношения, отказ на чужой записи или уязвимом пути audioId, и выдачу speaking-задания языковому предмету ровно один раз."
      },
      {
        "id": "learningBack/tests/test_srs_merge.py",
        "title": "Тесты: слияние карточек повторения с нескольких устройств",
        "layer": "тесты",
        "path": "learningBack/tests/test_srs_merge.py",
        "summary": "Проверяют T-0029/R-0019/V-0055: правило слияния карточек с нескольких устройств — побеждает более позднее ревью независимо от порядка записи, непросмотренная карточка проигрывает просмотренной, при равном времени ревью решают число повторов и срывов, повторная одинаковая запись не считается новой попыткой; на сервере два устройства сходятся без отката интервалов, проигравшая версия подтверждается (ack), но не возвращается при pull."
      },
      {
        "id": "learningBack/tests/test_subdomains.py",
        "title": "Тесты: граф цели из субдоменов",
        "layer": "тесты",
        "path": "learningBack/tests/test_subdomains.py",
        "summary": "Проверяют T-0060/R-0032/V-0084: очистку разбиения цели на субдомены от дублей, неизвестных и самоссылочных предпосылок и от циклов; сборку графа цели из графов субдоменов с префиксацией ключей и мостами между хвостом предпосылки и корнем зависимого; эндпоинты /graph/goal/split (только предлагает) и /graph/goal/build (пишет по одному запросу на субдомен, принимает правку человека, расширение существующего домена — только администратору)."
      },
      {
        "id": "learningBack/tests/test_user_data_access.py",
        "title": "Тесты: данные человека — доступ, журнал, выгрузка, удаление",
        "layer": "тесты",
        "path": "learningBack/tests/test_user_data_access.py",
        "summary": "Проверяют T-0054/R-0031/V-0083: доступ стороннего модуля к типу данных человека только по заявленному в манифесте и разрешённому человеком требованию (отказ без объявления, без разрешения, после отзыва), раздельность read/write, журнал каждого обращения по человеку, выгрузку всех данных одним документом и удаление по реестру типов вместе с разрешениями и журналом, а также то, что новый тип данных заводится модулем без правки ядра."
      },
      {
        "id": "learningBack/tests/test_versioning.py",
        "title": "Тесты: префикс /v1 и совместимость клиента",
        "layer": "тесты",
        "path": "learningBack/tests/test_versioning.py",
        "summary": "Проверяют T-0033/R-0020: разбор и числовое (не строковое) сравнение версий, обслуживание API под префиксом /v1 с устаревшими путями только для старых сборок и без них в схеме OpenAPI, версионный заголовок ответа, и отказ 426 устаревшему клиенту по X-Client-Version с читаемой причиной — при этом /version и /health остаются доступны всем."
      },
      {
        "id": "learningBack/tests/test_worker.py",
        "title": "Тесты: фоновый воркер AI-задач",
        "layer": "тесты",
        "path": "learningBack/tests/test_worker.py",
        "summary": "Проверяют T-0049/R-0023/R-0025/V-0064: в режиме jobs_mode=worker push только ставит задачу в очередь, фоновый воркер берёт задачи по порядку создания и не дважды, задача, ждущая повтора, раньше срока не берётся, временный сбой возвращает задачу в очередь с задержкой, неизвестный тип задачи помечается failed, зависшая в running задача переоткладывается по таймауту, расход токенов относится к владельцу задачи, а цикл воркера останавливается по запросу."
      },
      {
        "id": "learningFront/src/entities/module/mnemonic.ts",
        "title": "Метаданные модуля: Вспомнить по первым буквам",
        "layer": "entities",
        "path": "learningFront/src/entities/module/mnemonic.ts",
        "summary": "Клиентские метаданные второй техники запоминания — тот же набор полей, что у остальных предметных модулей (languages/ml/knowledge): только id, заголовок и единственный тип активности concept_mnemonic, офлайн, без схемы payload. Чистые данные без рендерера — рендерер (MnemonicActivity) подключается отдельно в widgets/module-registry, куда entities импортировать нельзя.",
        "api": [
          {
            "name": "MNEMONIC_MODULE_ID",
            "kind": "const",
            "summary": "Идентификатор модуля",
            "signature": "\"mnemonic\""
          },
          {
            "name": "MNEMONIC_MODULE_TITLE",
            "kind": "const",
            "summary": "Заголовок модуля для интерфейса",
            "signature": "\"Вспомнить по первым буквам\""
          },
          {
            "name": "mnemonicActivityTypes",
            "kind": "const",
            "summary": "Единственный тип активности модуля — concept_mnemonic, офлайн",
            "signature": "ActivityTypeDef[]"
          }
        ]
      },
      {
        "id": "learningFront/src/features/goal-intake/index.ts",
        "title": "Публичный API фичи goal-intake",
        "layer": "features",
        "path": "learningFront/src/features/goal-intake/index.ts",
        "summary": "Наружу видны только компонент диалога постановки цели и функция сборки предмета профиля из подтверждённого пересказа; модель диалога и сам компонент остаются внутренними деталями фичи.",
        "api": [
          {
            "name": "GoalIntakeDialog",
            "kind": "component",
            "summary": "Диалог постановки цели: уточнение → пересказ → подтверждение"
          },
          {
            "name": "subjectOf",
            "kind": "function",
            "summary": "Предмет профиля из подтверждённого пересказа",
            "signature": "(summary, toId) => { id, title, target }"
          }
        ]
      },
      {
        "id": "learningFront/src/features/goal-intake/model/dialog.ts",
        "title": "Логика диалога постановки цели",
        "layer": "features",
        "path": "learningFront/src/features/goal-intake/model/dialog.ts",
        "summary": "Чистая логика диалога постановки цели без сети и UI: сбор ответов на уточняющие вопросы (пустое поле — пропуск, а не пустой ответ), проверка готовности к пересказу и подтверждению, правка пересказа человеком, строка пересказа, сборка предмета профиля и решение о показе выбора между полным и интуитивным путём с человекочитаемым объёмом пути.",
        "api": [
          {
            "name": "canAsk",
            "kind": "function",
            "summary": "Достаточно ли содержателен ввод, чтобы задавать по нему вопросы",
            "signature": "(text: string) => boolean"
          },
          {
            "name": "collectAnswers",
            "kind": "function",
            "summary": "Ответы по вопросам; пустое поле — пропуск",
            "signature": "(questions, values) => GoalAnswer[]"
          },
          {
            "name": "answeredCount",
            "kind": "function",
            "summary": "Сколько вопросов реально получили ответ",
            "signature": "(answers: GoalAnswer[]) => number"
          },
          {
            "name": "canConfirm",
            "kind": "function",
            "summary": "Область и цель названы — можно подтверждать",
            "signature": "(summary: GoalSummary) => boolean"
          },
          {
            "name": "editSummary",
            "kind": "function",
            "summary": "Правка пересказа человеком: чистит пожелания, подставляет область в пустую цель",
            "signature": "(summary, patch) => GoalSummary"
          },
          {
            "name": "recapLine",
            "kind": "function",
            "summary": "Строка пересказа для подтверждения",
            "signature": "(summary: GoalSummary) => string"
          },
          {
            "name": "subjectOf",
            "kind": "function",
            "summary": "Предмет профиля из подтверждённого пересказа",
            "signature": "(summary, toId) => { id, title, target }"
          },
          {
            "name": "needsChoice",
            "kind": "function",
            "summary": "Нужен ли выбор между полным и интуитивным путём",
            "signature": "(volume: GoalVolume | null) => boolean"
          },
          {
            "name": "volumeLine",
            "kind": "function",
            "summary": "Строка объёма пути с верным склонением и пометкой оценки",
            "signature": "(v: VolumeVariant) => string"
          }
        ]
      },
      {
        "id": "learningFront/src/features/goal-intake/model/dialog.test.ts",
        "title": "Тесты: логика диалога постановки цели",
        "layer": "тесты",
        "path": "learningFront/src/features/goal-intake/model/dialog.test.ts",
        "summary": "Проверяют чистую логику диалога: пустое поле — пропуск, а не пустой ответ; вопросы задаются только при содержательном вводе; подтверждение требует названной области; правка пересказа чистит пожелания и подставляет область в пустую цель; строка пересказа не повторяет одинаковые область и цель; предмет профиля собирается из пересказа; выбор пути предлагается только при различающихся вариантах; объём пути называется с верным склонением и пометкой оценки."
      },
      {
        "id": "learningFront/src/features/goal-intake/ui/goal-intake-dialog.tsx",
        "title": "Диалог постановки цели",
        "layer": "features",
        "path": "learningFront/src/features/goal-intake/ui/goal-intake-dialog.tsx",
        "summary": "Компонент диалога постановки цели: свободный ввод → необязательные уточняющие вопросы → пересказ с правкой → подтверждение, и отдельно — выбор между полным и интуитивным путём, если под целью есть различающиеся по объёму базовые области. Без сети или без модели уточнение падает молча, и вызывающий получает onFallback — экран должен показать прямую форму ввода.",
        "api": [
          {
            "name": "GoalIntakeDialog",
            "kind": "component",
            "summary": "Диалог постановки цели от свободного ввода до подтверждения",
            "signature": "({ initialText?, onConfirmed, onFallback }) => JSX"
          }
        ]
      },
      {
        "id": "learningFront/src/features/graph-editor/model/split-edit.ts",
        "title": "Правка разбиения цели на субдомены",
        "layer": "features",
        "path": "learningFront/src/features/graph-editor/model/split-edit.ts",
        "summary": "Чистая логика правки предложенного моделью разбиения цели на субдомены до построения графа: убрать субдомен вместе со ссылками на него (иначе сервер бы отбросил их молча), переименовать, посчитать бюджет запросов по оставшимся частям и упорядочить их для показа от основ к зависимым, не вешая экран на цикле.",
        "api": [
          {
            "name": "Subdomain",
            "kind": "type",
            "summary": "Субдомен разбиения цели",
            "signature": "{ key, title, summary, prereqs: string[] }"
          },
          {
            "name": "BuildBudget",
            "kind": "type",
            "summary": "Цена построения в запросах к модели",
            "signature": "{ requests, subdomains, limit }"
          },
          {
            "name": "removeSubdomain",
            "kind": "function",
            "summary": "Убрать субдомен вместе со ссылками на него",
            "signature": "(list, key) => Subdomain[]"
          },
          {
            "name": "renameSubdomain",
            "kind": "function",
            "summary": "Переименовать субдомен",
            "signature": "(list, key, title) => Subdomain[]"
          },
          {
            "name": "canBuild",
            "kind": "function",
            "summary": "Строить можно, пока остался хоть один названный субдомен",
            "signature": "(list: Subdomain[]) => boolean"
          },
          {
            "name": "toPayload",
            "kind": "function",
            "summary": "Что уйдёт на сервер: пустые названия и ссылки на них отсекаются",
            "signature": "(list: Subdomain[]) => Subdomain[]"
          },
          {
            "name": "budgetFor",
            "kind": "function",
            "summary": "Бюджет после правки по числу оставшихся субдоменов",
            "signature": "(list, limit) => BuildBudget"
          },
          {
            "name": "orderByPrereqs",
            "kind": "function",
            "summary": "Порядок показа: от основ к зависимым, без зависания на цикле",
            "signature": "(list: Subdomain[]) => Subdomain[]"
          }
        ]
      },
      {
        "id": "learningFront/src/features/graph-editor/model/split-edit.test.ts",
        "title": "Тесты: правка разбиения цели на субдомены",
        "layer": "тесты",
        "path": "learningFront/src/features/graph-editor/model/split-edit.test.ts",
        "summary": "Проверяют чистую логику правки: удаление субдомена подчищает ссылки на него у остальных и не мутирует исходный список; переименование меняет только название; на сервер уходят только названные субдомены со ссылками, обрезанными до оставшихся; построить можно, пока есть хоть один названный субдомен; бюджет считается по числу оставшихся; порядок показа ставит предпосылки раньше зависимых и не виснет на цикле или ссылке на несуществующий субдомен."
      },
      {
        "id": "learningFront/src/features/graph-editor/ui/goal-gate.tsx",
        "title": "Заслон перед построением карты",
        "layer": "features",
        "path": "learningFront/src/features/graph-editor/ui/goal-gate.tsx",
        "summary": "Пока цель по области не подтверждена явно, построение карты знаний недоступно. Для целей, уже заданных прямой формой или до появления диалога постановки цели, подтверждение — одна кнопка по уже введённым области и уровню.",
        "api": [
          {
            "name": "GoalGate",
            "kind": "component",
            "summary": "Блокирует детей, пока цель по домену не подтверждена",
            "signature": "({ domain, children }) => JSX"
          }
        ]
      },
      {
        "id": "learningFront/src/features/graph-editor/ui/goal-planner.tsx",
        "title": "Построение карты из субдоменов в два шага",
        "layer": "features",
        "path": "learningFront/src/features/graph-editor/ui/goal-planner.tsx",
        "summary": "Построение графа цели в два шага: сперва модель предлагает разбиение на субдомены с ценой в запросах, человек может убрать или переименовать части, и только после этого — отдельный запрос на сборку, по одному обращению к модели на субдомен.",
        "api": [
          {
            "name": "GoalPlanner",
            "kind": "component",
            "summary": "Разбиение цели на части с правкой и последующая сборка графа",
            "signature": "({ domain, topic, onBuilt }) => JSX"
          }
        ]
      },
      {
        "id": "learningFront/src/features/ielts-writing/lib/task-data.ts",
        "title": "Данные задания Task 1",
        "layer": "features",
        "path": "learningFront/src/features/ielts-writing/lib/task-data.ts",
        "summary": "Данные графика или таблицы задания Task 1 приходят как числа в payload.data, а не картинкой — поэтому их можно отрисовать и прочитать офлайн. Модуль проверяет форму пришедших данных, не доверяя им, готовит строки для столбчатой диаграммы и считает нехватку слов до минимума эссе.",
        "api": [
          {
            "name": "TaskData",
            "kind": "type",
            "summary": "Разобранные данные задания",
            "signature": "{ kind?, title?, unit?, categories: string[], series: {name, values: number[]}[] }"
          },
          {
            "name": "parseTaskData",
            "kind": "function",
            "summary": "Проверить форму payload и привести к TaskData",
            "signature": "(raw: unknown) => TaskData | null"
          },
          {
            "name": "BarRow",
            "kind": "type",
            "summary": "Строка столбчатой диаграммы",
            "signature": "{ category, bars: {series, value, fraction}[] }"
          },
          {
            "name": "barRows",
            "kind": "function",
            "summary": "Строки диаграммы: длина полосы — доля от наибольшего значения",
            "signature": "(data: TaskData) => BarRow[]"
          },
          {
            "name": "countWords",
            "kind": "function",
            "summary": "Число слов по пробельным разделителям, как на экзамене",
            "signature": "(text: string) => number"
          },
          {
            "name": "wordsShort",
            "kind": "function",
            "summary": "Не хватает до минимума слов; 0 — норма выполнена",
            "signature": "(text, minWords: unknown) => number"
          }
        ]
      },
      {
        "id": "learningFront/src/features/ielts-writing/lib/task-data.test.ts",
        "title": "Тесты: данные задания Task 1",
        "layer": "тесты",
        "path": "learningFront/src/features/ielts-writing/lib/task-data.test.ts",
        "summary": "Проверяют разбор и подготовку данных: форма входных данных проверяется, а не считается данной — мусор и пустые данные дают null; нечисловые значения становятся нулём и битые ряды отбрасываются; длина полосы диаграммы — доля от наибольшего значения по всем рядам без деления на ноль; короткий ряд дополняется нулём; слова считаются по пробельным разделителям, нехватка до минимума — включая случай без заданного минимума."
      },
      {
        "id": "learningFront/src/features/ielts-writing/ui/task-data-view.tsx",
        "title": "Отрисовка данных задания Task 1",
        "layer": "features",
        "path": "learningFront/src/features/ielts-writing/ui/task-data-view.tsx",
        "summary": "Отрисовывает данные задания Task 1 столбчатой диаграммой и теми же цифрами текстом рядом — цифры нужны всегда: по ним пишут описание и по ним же проверяют точность написанного.",
        "api": [
          {
            "name": "TaskDataView",
            "kind": "component",
            "summary": "Столбчатая диаграмма и цифры данных задания Task 1",
            "signature": "({ data: TaskData }) => JSX"
          }
        ]
      },
      {
        "id": "learningFront/src/features/listening-drill/index.ts",
        "title": "Публичный API фичи listening-drill",
        "layer": "features",
        "path": "learningFront/src/features/listening-drill/index.ts",
        "summary": "Наружу виден только рендерер активности; кэш аудио и модель прослушиваний остаются внутренними деталями фичи.",
        "api": [
          {
            "name": "ListeningDrillActivity",
            "kind": "component",
            "summary": "Рендерер Activity listening_drill"
          }
        ]
      },
      {
        "id": "learningFront/src/features/listening-drill/model/audio-cache.ts",
        "title": "Кэш аудио listening-дрилла на устройстве",
        "layer": "features",
        "path": "learningFront/src/features/listening-drill/model/audio-cache.ts",
        "summary": "Запись дрилла аудирования скачивается один раз при наличии сети и дальше воспроизводится без неё. Без сети и без записи в кэше возвращает null, а не бросает ошибку — вызывающий сам решает, как показать отсутствие записи.",
        "api": [
          {
            "name": "cachedUri",
            "kind": "function",
            "summary": "URI уже закэшированной записи или null",
            "signature": "(key: string) => string | null"
          },
          {
            "name": "ensureCached",
            "kind": "function",
            "summary": "Скачать запись, если её ещё нет; без сети вернёт null",
            "signature": "(key, audioPath) => Promise<string | null>"
          }
        ]
      },
      {
        "id": "learningFront/src/features/listening-drill/model/listening-model.ts",
        "title": "Модель listening-дрилла",
        "layer": "features",
        "path": "learningFront/src/features/listening-drill/model/listening-model.ts",
        "summary": "Чистый разбор payload listening-дрилла и производные от него: лимит прослушиваний по умолчанию как на экзамене (один раз), сколько прослушиваний осталось и человекочитаемая причина, почему слушать сейчас нельзя. Проверка ответов на вопросы общая с reading-дриллом — тот же формат вопросов.",
        "api": [
          {
            "name": "DEFAULT_MAX_PLAYS",
            "kind": "const",
            "summary": "Прослушиваний по умолчанию, если задание не указало иначе",
            "signature": "1"
          },
          {
            "name": "ListeningDrill",
            "kind": "type",
            "summary": "Разобранное задание аудирования",
            "signature": "{ title, audioPath, maxPlays, questions: QuizQuestion[] }"
          },
          {
            "name": "parseListeningDrill",
            "kind": "function",
            "summary": "Проверить payload и привести к ListeningDrill",
            "signature": "(raw: unknown) => ListeningDrill | null"
          },
          {
            "name": "playsLeft",
            "kind": "function",
            "summary": "Сколько прослушиваний осталось, не уходя ниже нуля",
            "signature": "(maxPlays, used) => number"
          },
          {
            "name": "AudioState",
            "kind": "type",
            "summary": "Состояние кэша аудио на устройстве",
            "signature": "'cached' | 'missing' | 'checking'"
          },
          {
            "name": "listenBlocker",
            "kind": "function",
            "summary": "Причина, почему слушать нельзя сейчас; null — можно",
            "signature": "(state, maxPlays, used) => string | null"
          }
        ]
      },
      {
        "id": "learningFront/src/features/listening-drill/model/listening-model.test.ts",
        "title": "Тесты: модель listening-дрилла",
        "layer": "тесты",
        "path": "learningFront/src/features/listening-drill/model/listening-model.test.ts",
        "summary": "Проверяют: по умолчанию прослушивание разрешено один раз, если задание не указало иначе; повреждённое задание (без audioPath или вопросов) не разбирается; оставшиеся прослушивания не уходят ниже нуля; причина, по которой слушать нельзя, объясняется словами для каждого из состояний — проверка кэша, отсутствие записи на устройстве, исчерпанный лимит."
      },
      {
        "id": "learningFront/src/features/listening-drill/model/plays-store.ts",
        "title": "Счётчик прослушиваний (устройство)",
        "layer": "features",
        "path": "learningFront/src/features/listening-drill/model/plays-store.ts",
        "summary": "Сколько раз уже прослушана запись конкретной активности — хранится в защищённом хранилище устройства, а не в памяти экрана, иначе лимит обходится простым выходом с экрана и возвратом.",
        "api": [
          {
            "name": "getPlays",
            "kind": "function",
            "summary": "Сколько прослушиваний уже потрачено на активность",
            "signature": "(activityId: string) => Promise<number>"
          },
          {
            "name": "addPlay",
            "kind": "function",
            "summary": "Зафиксировать ещё одно прослушивание",
            "signature": "(activityId: string) => Promise<number>"
          }
        ]
      },
      {
        "id": "learningFront/src/features/listening-drill/model/plays-store.web.ts",
        "title": "Счётчик прослушиваний (веб)",
        "layer": "features",
        "path": "learningFront/src/features/listening-drill/model/plays-store.web.ts",
        "summary": "Тот же контракт счётчика прослушиваний, что у нативного plays-store.ts, но на localStorage — на вебе SecureStore недоступен. При недоступном хранилище запись тихо не сохраняется, и лимит в этом случае действует только в пределах одного открытого экрана.",
        "api": [
          {
            "name": "getPlays",
            "kind": "function",
            "summary": "Сколько прослушиваний уже потрачено на активность",
            "signature": "(activityId: string) => Promise<number>"
          },
          {
            "name": "addPlay",
            "kind": "function",
            "summary": "Зафиксировать ещё одно прослушивание",
            "signature": "(activityId: string) => Promise<number>"
          }
        ]
      },
      {
        "id": "learningFront/src/features/listening-drill/ui/listening-drill-activity.tsx",
        "title": "Рендерер Activity listening_drill",
        "layer": "features",
        "path": "learningFront/src/features/listening-drill/ui/listening-drill-activity.tsx",
        "summary": "Скачивает и кэширует запись при сети, фиксирует потраченное прослушивание до начала воспроизведения (чтобы выход с экрана не возвращал попытку), и проверяет ответы на вопросы по тому же формату, что reading-дрилл. Текст того, что произносится, учащемуся не показывается — цель упражнения в восприятии на слух.",
        "api": [
          {
            "name": "ListeningDrillActivity",
            "kind": "component",
            "summary": "Рендерер Activity listening_drill",
            "signature": "({ activity, onComplete }) => JSX"
          }
        ]
      },
      {
        "id": "learningFront/src/features/mnemonic-recall/index.ts",
        "title": "Публичный API фичи mnemonic-recall",
        "layer": "features",
        "path": "learningFront/src/features/mnemonic-recall/index.ts",
        "summary": "Наружу виден только рендерер активности concept_mnemonic.",
        "api": [
          {
            "name": "MnemonicActivity",
            "kind": "component",
            "summary": "Рендерер Activity concept_mnemonic (реэкспорт)"
          }
        ]
      },
      {
        "id": "learningFront/src/features/mnemonic-recall/model/rating.ts",
        "title": "Самооценка вспоминания",
        "layer": "features",
        "path": "learningFront/src/features/mnemonic-recall/model/rating.ts",
        "summary": "Самооценка вспоминания по технике «первые буквы» переводится в результат 0..1 той же шкалой ступеней (не вспомнил/с трудом/хорошо/легко), что и оценка карточки интервального повторения — освоенность в графе знаний общая независимо от техники.",
        "api": [
          {
            "name": "SelfRating",
            "kind": "type",
            "summary": "Ступень самооценки",
            "signature": "'again' | 'hard' | 'good' | 'easy'"
          },
          {
            "name": "SELF_RATINGS",
            "kind": "const",
            "summary": "Шкала ступеней с результатом каждой",
            "signature": "{ key: SelfRating, label, score }[]"
          },
          {
            "name": "scoreOf",
            "kind": "function",
            "summary": "Результат 0..1 по ступени; неизвестная ступень — ошибка",
            "signature": "(rating: SelfRating) => number"
          },
          {
            "name": "MNEMONIC_SOURCE",
            "kind": "const",
            "summary": "Идентификатор способа в свидетельстве об освоении",
            "signature": "\"first_letters\""
          }
        ]
      },
      {
        "id": "learningFront/src/features/mnemonic-recall/model/rating.test.ts",
        "title": "Тесты: самооценка вспоминания",
        "layer": "тесты",
        "path": "learningFront/src/features/mnemonic-recall/model/rating.test.ts",
        "summary": "Проверяют шкалу самооценки: оценки идут по возрастанию без разрывов от 0 (провал) до 1 (полное владение); каждый результат лежит в границах, которые принимает сервер; неизвестная самооценка отвергается явной ошибкой, а не тихо превращается в ноль."
      }
    ],
    "imports": [
      {
        "from": "learningFront/src/entities/module/mnemonic.ts",
        "to": "learningFront/src/shared/engine/index.ts",
        "evidence": {
          "path": "learningFront/src/entities/module/mnemonic.ts",
          "line": 3,
          "fragment": "import type { ActivityTypeDef } from '@/shared/engine';"
        }
      },
      {
        "from": "learningFront/src/entities/module/index.ts",
        "to": "learningFront/src/entities/module/mnemonic.ts",
        "evidence": {
          "path": "learningFront/src/entities/module/index.ts",
          "line": 6,
          "fragment": "export { MNEMONIC_MODULE_ID, MNEMONIC_MODULE_TITLE, mnemonicActivityTypes } from './mnemonic';"
        }
      },
      {
        "from": "learningFront/src/widgets/module-registry/index.ts",
        "to": "learningFront/src/features/mnemonic-recall/index.ts",
        "evidence": {
          "path": "learningFront/src/widgets/module-registry/index.ts",
          "line": 34,
          "fragment": "import { MnemonicActivity } from '@/features/mnemonic-recall';"
        }
      },
      {
        "from": "learningFront/src/widgets/module-registry/index.ts",
        "to": "learningFront/src/features/listening-drill/index.ts",
        "evidence": {
          "path": "learningFront/src/widgets/module-registry/index.ts",
          "line": 30,
          "fragment": "import { ListeningDrillActivity } from '@/features/listening-drill';"
        }
      },
      {
        "from": "learningFront/src/features/goal-intake/index.ts",
        "to": "learningFront/src/features/goal-intake/ui/goal-intake-dialog.tsx",
        "evidence": {
          "path": "learningFront/src/features/goal-intake/index.ts",
          "line": 1,
          "fragment": "export { GoalIntakeDialog } from './ui/goal-intake-dialog';"
        }
      },
      {
        "from": "learningFront/src/features/goal-intake/index.ts",
        "to": "learningFront/src/features/goal-intake/model/dialog.ts",
        "evidence": {
          "path": "learningFront/src/features/goal-intake/index.ts",
          "line": 2,
          "fragment": "export { directIntake, subjectOf } from './model/dialog';"
        }
      },
      {
        "from": "learningFront/src/pages/onboarding/ui/onboarding-screen.tsx",
        "to": "learningFront/src/features/goal-intake/index.ts",
        "evidence": {
          "path": "learningFront/src/pages/onboarding/ui/onboarding-screen.tsx",
          "line": 11,
          "fragment": "import { directIntake, GoalIntakeDialog, subjectOf } from '@/features/goal-intake';"
        }
      },
      {
        "from": "learningFront/src/features/goal-intake/ui/goal-intake-dialog.tsx",
        "to": "learningFront/src/entities/session/index.ts",
        "evidence": {
          "path": "learningFront/src/features/goal-intake/ui/goal-intake-dialog.tsx",
          "line": 7,
          "fragment": "import { MASTERY_TARGETS, toSubjectId } from '@/entities/session';"
        }
      },
      {
        "from": "learningFront/src/features/goal-intake/ui/goal-intake-dialog.tsx",
        "to": "learningFront/src/shared/api/index.ts",
        "evidence": {
          "path": "learningFront/src/features/goal-intake/ui/goal-intake-dialog.tsx",
          "line": 16,
          "fragment": "} from '@/shared/api';"
        }
      },
      {
        "from": "learningFront/src/features/goal-intake/ui/goal-intake-dialog.tsx",
        "to": "learningFront/src/shared/ui/index.ts",
        "evidence": {
          "path": "learningFront/src/features/goal-intake/ui/goal-intake-dialog.tsx",
          "line": 28,
          "fragment": "} from '@/shared/ui';"
        }
      },
      {
        "from": "learningFront/src/features/goal-intake/ui/goal-intake-dialog.tsx",
        "to": "learningFront/src/features/goal-intake/model/dialog.ts",
        "evidence": {
          "path": "learningFront/src/features/goal-intake/ui/goal-intake-dialog.tsx",
          "line": 38,
          "fragment": "} from '../model/dialog';"
        }
      },
      {
        "from": "learningFront/src/features/goal-intake/model/dialog.ts",
        "to": "learningFront/src/shared/api/index.ts",
        "evidence": {
          "path": "learningFront/src/features/goal-intake/model/dialog.ts",
          "line": 8,
          "fragment": "} from '@/shared/api';"
        }
      },
      {
        "from": "learningFront/src/features/goal-intake/model/dialog.test.ts",
        "to": "learningFront/src/features/goal-intake/model/dialog.ts",
        "evidence": {
          "path": "learningFront/src/features/goal-intake/model/dialog.test.ts",
          "line": 17,
          "fragment": "} from './dialog';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/ui/goal-gate.tsx",
        "to": "learningFront/src/entities/session/index.ts",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/ui/goal-gate.tsx",
          "line": 6,
          "fragment": "import { targetLabel, useSession } from '@/entities/session';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/ui/goal-gate.tsx",
        "to": "learningFront/src/shared/api/index.ts",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/ui/goal-gate.tsx",
          "line": 7,
          "fragment": "import { confirmGoal, getGoalIntake } from '@/shared/api';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/ui/goal-gate.tsx",
        "to": "learningFront/src/shared/ui/index.ts",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/ui/goal-gate.tsx",
          "line": 8,
          "fragment": "import { Button, Card, Label, Muted, Note, space } from '@/shared/ui';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/ui/graph-map.tsx",
        "to": "learningFront/src/features/graph-editor/ui/goal-gate.tsx",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/ui/graph-map.tsx",
          "line": 11,
          "fragment": "import { GoalGate } from './goal-gate';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/ui/graph-map.tsx",
        "to": "learningFront/src/features/graph-editor/ui/goal-planner.tsx",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/ui/graph-map.tsx",
          "line": 12,
          "fragment": "import { GoalPlanner } from './goal-planner';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/ui/goal-planner.tsx",
        "to": "learningFront/src/shared/api/index.ts",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/ui/goal-planner.tsx",
          "line": 6,
          "fragment": "import { buildGoal, splitGoal, type Graph } from '@/shared/api';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/ui/goal-planner.tsx",
        "to": "learningFront/src/shared/ui/index.ts",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/ui/goal-planner.tsx",
          "line": 7,
          "fragment": "import { Body, Button, Card, Field, Label, Muted, Note, space } from '@/shared/ui';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/ui/goal-planner.tsx",
        "to": "learningFront/src/features/graph-editor/model/split-edit.ts",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/ui/goal-planner.tsx",
          "line": 17,
          "fragment": "} from '../model/split-edit';"
        }
      },
      {
        "from": "learningFront/src/features/graph-editor/model/split-edit.test.ts",
        "to": "learningFront/src/features/graph-editor/model/split-edit.ts",
        "evidence": {
          "path": "learningFront/src/features/graph-editor/model/split-edit.test.ts",
          "line": 10,
          "fragment": "} from './split-edit';"
        }
      },
      {
        "from": "learningFront/src/features/ielts-writing/ui/ielts-writing-activity.tsx",
        "to": "learningFront/src/features/ielts-writing/lib/task-data.ts",
        "evidence": {
          "path": "learningFront/src/features/ielts-writing/ui/ielts-writing-activity.tsx",
          "line": 11,
          "fragment": "import { countWords, parseTaskData, wordsShort } from '../lib/task-data';"
        }
      },
      {
        "from": "learningFront/src/features/ielts-writing/ui/ielts-writing-activity.tsx",
        "to": "learningFront/src/features/ielts-writing/ui/task-data-view.tsx",
        "evidence": {
          "path": "learningFront/src/features/ielts-writing/ui/ielts-writing-activity.tsx",
          "line": 12,
          "fragment": "import { TaskDataView } from './task-data-view';"
        }
      },
      {
        "from": "learningFront/src/features/ielts-writing/ui/task-data-view.tsx",
        "to": "learningFront/src/features/ielts-writing/lib/task-data.ts",
        "evidence": {
          "path": "learningFront/src/features/ielts-writing/ui/task-data-view.tsx",
          "line": 5,
          "fragment": "import { barRows, type TaskData } from '../lib/task-data';"
        }
      },
      {
        "from": "learningFront/src/features/ielts-writing/ui/task-data-view.tsx",
        "to": "learningFront/src/shared/ui/index.ts",
        "evidence": {
          "path": "learningFront/src/features/ielts-writing/ui/task-data-view.tsx",
          "line": 4,
          "fragment": "import { Card, Label, Muted, radius, space, useTheme } from '@/shared/ui';"
        }
      },
      {
        "from": "learningFront/src/features/ielts-writing/lib/task-data.test.ts",
        "to": "learningFront/src/features/ielts-writing/lib/task-data.ts",
        "evidence": {
          "path": "learningFront/src/features/ielts-writing/lib/task-data.test.ts",
          "line": 2,
          "fragment": "import { barRows, countWords, parseTaskData, wordsShort } from './task-data';"
        }
      },
      {
        "from": "learningFront/src/features/listening-drill/index.ts",
        "to": "learningFront/src/features/listening-drill/ui/listening-drill-activity.tsx",
        "evidence": {
          "path": "learningFront/src/features/listening-drill/index.ts",
          "line": 1,
          "fragment": "export { ListeningDrillActivity } from './ui/listening-drill-activity';"
        }
      },
      {
        "from": "learningFront/src/features/listening-drill/model/audio-cache.ts",
        "to": "learningFront/src/shared/api/index.ts",
        "evidence": {
          "path": "learningFront/src/features/listening-drill/model/audio-cache.ts",
          "line": 3,
          "fragment": "import { apiUrl, CLIENT_HEADERS, getToken } from '@/shared/api';"
        }
      },
      {
        "from": "learningFront/src/features/listening-drill/model/listening-model.test.ts",
        "to": "learningFront/src/features/listening-drill/model/listening-model.ts",
        "evidence": {
          "path": "learningFront/src/features/listening-drill/model/listening-model.test.ts",
          "line": 7,
          "fragment": "} from './listening-model';"
        }
      },
      {
        "from": "learningFront/src/features/listening-drill/ui/listening-drill-activity.tsx",
        "to": "learningFront/src/entities/session/index.ts",
        "evidence": {
          "path": "learningFront/src/features/listening-drill/ui/listening-drill-activity.tsx",
          "line": 6,
          "fragment": "import { useSession } from '@/entities/session';"
        }
      },
      {
        "from": "learningFront/src/features/listening-drill/ui/listening-drill-activity.tsx",
        "to": "learningFront/src/shared/api/index.ts",
        "evidence": {
          "path": "learningFront/src/features/listening-drill/ui/listening-drill-activity.tsx",
          "line": 7,
          "fragment": "import { getLocalStore } from '@/shared/api';"
        }
      },
      {
        "from": "learningFront/src/features/listening-drill/ui/listening-drill-activity.tsx",
        "to": "learningFront/src/shared/engine/index.ts",
        "evidence": {
          "path": "learningFront/src/features/listening-drill/ui/listening-drill-activity.tsx",
          "line": 8,
          "fragment": "import type { ActivityRendererProps } from '@/shared/engine';"
        }
      },
      {
        "from": "learningFront/src/features/listening-drill/ui/listening-drill-activity.tsx",
        "to": "learningFront/src/shared/engine/index.ts",
        "evidence": {
          "path": "learningFront/src/features/listening-drill/ui/listening-drill-activity.tsx",
          "line": 9,
          "fragment": "import { gradeQuestions, type QuizQuestion, type QuizResult } from '@/shared/engine';"
        }
      },
      {
        "from": "learningFront/src/features/listening-drill/ui/listening-drill-activity.tsx",
        "to": "learningFront/src/shared/ui/index.ts",
        "evidence": {
          "path": "learningFront/src/features/listening-drill/ui/listening-drill-activity.tsx",
          "line": 22,
          "fragment": "} from '@/shared/ui';"
        }
      },
      {
        "from": "learningFront/src/features/listening-drill/ui/listening-drill-activity.tsx",
        "to": "learningFront/src/features/listening-drill/model/audio-cache.ts",
        "evidence": {
          "path": "learningFront/src/features/listening-drill/ui/listening-drill-activity.tsx",
          "line": 23,
          "fragment": "import { cachedUri, ensureCached } from '../model/audio-cache';"
        }
      },
      {
        "from": "learningFront/src/features/listening-drill/ui/listening-drill-activity.tsx",
        "to": "learningFront/src/features/listening-drill/model/listening-model.ts",
        "evidence": {
          "path": "learningFront/src/features/listening-drill/ui/listening-drill-activity.tsx",
          "line": 29,
          "fragment": "} from '../model/listening-model';"
        }
      },
      {
        "from": "learningFront/src/features/listening-drill/ui/listening-drill-activity.tsx",
        "to": "learningFront/src/features/listening-drill/model/plays-store.ts",
        "evidence": {
          "path": "learningFront/src/features/listening-drill/ui/listening-drill-activity.tsx",
          "line": 30,
          "fragment": "import { addPlay, getPlays } from '../model/plays-store';"
        }
      },
      {
        "from": "learningFront/src/features/mnemonic-recall/index.ts",
        "to": "learningFront/src/features/mnemonic-recall/ui/mnemonic-activity.tsx",
        "evidence": {
          "path": "learningFront/src/features/mnemonic-recall/index.ts",
          "line": 1,
          "fragment": "export { MnemonicActivity } from './ui/mnemonic-activity';"
        }
      },
      {
        "from": "learningFront/src/features/mnemonic-recall/model/rating.test.ts",
        "to": "learningFront/src/features/mnemonic-recall/model/rating.ts",
        "evidence": {
          "path": "learningFront/src/features/mnemonic-recall/model/rating.test.ts",
          "line": 2,
          "fragment": "import { SELF_RATINGS, scoreOf } from './rating';"
        }
      }
    ],
    "groups": [
      {
        "id": "goal-intake-dialog-frontend",
        "title": "Диалог постановки цели (клиент)",
        "summary": "Компонент и логика диалога постановки цели: уточняющие вопросы, пересказ, подтверждение; публичная точка входа фичи.",
        "modules": [
          "learningFront/src/features/goal-intake/index.ts",
          "learningFront/src/features/goal-intake/model/dialog.ts",
          "learningFront/src/features/goal-intake/ui/goal-intake-dialog.tsx"
        ],
        "capability": "goal-intake"
      },
      {
        "id": "goal-confirm-gate-frontend",
        "title": "Заслон перед построением карты",
        "summary": "Блокирует построение графа, пока цель по области явно не подтверждена.",
        "modules": [
          "learningFront/src/features/graph-editor/ui/goal-gate.tsx"
        ],
        "capability": "goal-intake"
      },
      {
        "id": "goal-subdomain-split-frontend",
        "title": "Разбиение цели на субдомены (клиент)",
        "summary": "Правка предложенного моделью разбиения цели на части до построения: убрать, переименовать, видеть бюджет.",
        "modules": [
          "learningFront/src/features/graph-editor/model/split-edit.ts",
          "learningFront/src/features/graph-editor/ui/goal-planner.tsx"
        ],
        "capability": "goal-subdomain-split"
      },
      {
        "id": "goal-tree-assembly-frontend",
        "title": "Сборка графа цели из субдоменов (клиент)",
        "summary": "Запрос на построение графа по отредактированному человеком разбиению, по одному обращению к модели на субдомен.",
        "modules": [
          "learningFront/src/features/graph-editor/ui/goal-planner.tsx"
        ],
        "capability": "goal-tree-assembly"
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
        "capability": "memorize-techniques"
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
        "capability": "reception-drills"
      },
      {
        "id": "writing-ielts-task-data-frontend",
        "title": "Данные задания Task 1 (клиент)",
        "summary": "Разбор и отрисовка числовых данных графика или таблицы задания Task 1 — читается офлайн, без картинки с сервера.",
        "modules": [
          "learningFront/src/features/ielts-writing/lib/task-data.ts",
          "learningFront/src/features/ielts-writing/ui/task-data-view.tsx"
        ],
        "capability": "writing-ielts"
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
        "id": "file-listening-audio-cache",
        "kind": "file",
        "where": "expo-file-system: Paths.document/'listening' (кэш записей listening-дрилла на устройстве)",
        "title": "Кэш аудио listening-дрилла на устройстве"
      }
    ],
    "flows": [
      {
        "from": "learningFront/src/features/listening-drill/model/audio-cache.ts",
        "to": "file-listening-audio-cache",
        "direction": "read",
        "evidence": {
          "path": "learningFront/src/features/listening-drill/model/audio-cache.ts",
          "line": 10,
          "fragment": "return f.exists ? f.uri : null;"
        }
      },
      {
        "from": "learningFront/src/features/listening-drill/model/audio-cache.ts",
        "to": "file-listening-audio-cache",
        "direction": "write",
        "evidence": {
          "path": "learningFront/src/features/listening-drill/model/audio-cache.ts",
          "line": 20,
          "fragment": "File.downloadFileAsync(apiUrl(audioPath), fileFor(key)"
        }
      },
      {
        "from": "learningFront/src/features/listening-drill/model/audio-cache.ts",
        "to": "http-backend-api",
        "direction": "read",
        "evidence": {
          "path": "learningFront/src/features/listening-drill/model/audio-cache.ts",
          "line": 20,
          "fragment": "apiUrl(audioPath)"
        }
      },
      {
        "from": "learningFront/src/features/listening-drill/model/plays-store.ts",
        "to": "file-device-storage",
        "direction": "read",
        "evidence": {
          "path": "learningFront/src/features/listening-drill/model/plays-store.ts",
          "line": 7,
          "fragment": "const n = Number(await SecureStore.getItemAsync(key(activityId)));"
        }
      },
      {
        "from": "learningFront/src/features/listening-drill/model/plays-store.ts",
        "to": "file-device-storage",
        "direction": "write",
        "evidence": {
          "path": "learningFront/src/features/listening-drill/model/plays-store.ts",
          "line": 13,
          "fragment": "await SecureStore.setItemAsync(key(activityId), String(next));"
        }
      },
      {
        "from": "learningFront/src/features/listening-drill/model/plays-store.web.ts",
        "to": "file-device-storage",
        "direction": "read",
        "evidence": {
          "path": "learningFront/src/features/listening-drill/model/plays-store.web.ts",
          "line": 6,
          "fragment": "const n = Number(globalThis.localStorage?.getItem(key(activityId)));"
        }
      },
      {
        "from": "learningFront/src/features/listening-drill/model/plays-store.web.ts",
        "to": "file-device-storage",
        "direction": "write",
        "evidence": {
          "path": "learningFront/src/features/listening-drill/model/plays-store.web.ts",
          "line": 16,
          "fragment": "globalThis.localStorage?.setItem(key(activityId), String(next));"
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
- 2026-10-03 · обновлены номера строк в свидетельствах (1): код сдвинулся, содержание карты не менялось · claude
