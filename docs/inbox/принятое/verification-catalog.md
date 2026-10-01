# Каталог проверок

Какими средствами доказывается выполнение требований. Вид доказательства в задачах и спеках — одно из четырёх: **test**, **live**, **build**, **device** (правила).

## 1. Автоматические проверки (обязательны, NFR-13)

| Проверка | Команда | Что ловит | Где запускается |
|---|---|---|---|
| Backend: формат | `cd learningBack && uv run ruff format --check .` | Разъехавшийся формат | CI (P3-CI-01) |
| Backend: линтер | `cd learningBack && uv run ruff check .` | Ошибки и неиспользуемое | CI |
| Backend: тесты | `cd learningBack && uv run pytest` (нужен Postgres стенда; БД `<db>_test`) | Регрессии поведения (260 тестов на 2026-09-30) | CI |
| Клиент: всё сразу | `cd learningFront && npm run check` (typecheck, lint, format, tests) | Типы, стиль, регрессии | CI (P3-CI-02) |
| Инварианты | `bash scripts/check-invariants.sh` в суперпроекте | NFR-02, NFR-03, NFR-KG-1, цвета вне `design.ts` | CI (P3-CI-03) |
| Ссылки документации | `python scripts/check-docs.py` | Битые относительные ссылки в `docs/` | CI (P3-CI-03) |

## 2. Проверки инвариантов

| Требование | Проверка | Ожидание |
|---|---|---|
| NFR-02 | `grep -rniE "llm_api_key|sk-[a-z0-9]{10}" learningFront/src` | пусто |
| NFR-03 клиент | `grep -rniE "languages|ielts|toefl|concept|knowledge" learningFront/src/shared/engine --include=*.ts` (без тестов) | пусто |
| NFR-03 backend | `grep -rnE "from modules|import modules" learningBack/core` | пусто |
| NFR-KG-1 | `grep -rniE "concept_edge|UserConcept|effective_graph" learningBack/core` | пусто |
| AC-12.4 | `grep -rnE "#[0-9a-fA-F]{3,8}\b" learningFront/src` вне `shared/config/design.ts` | пусто |

## 3. Живые прогоны (live)

| Сценарий | Как | Доказывает |
|---|---|---|
| Стенд | `docker compose up -d --build`; `curl --noproxy '*' localhost:8000/health` | FR-PRD-02 (dev), миграции |
| Письмо | регистрация → эссе → sync → разбор | AC-06.1..3, AC-03.1..3 |
| Граф и курс | предмет → build → плейсмент → курс → шаг | AC-08.*, AC-10.*, AC-11.* |
| Провайдер | `LLM_API_KEY` в `.env`, сборка графа, оценка эссе | AC-04.2 |

Грабли запуска — HANDOFF §3.

## 4. Проверки на устройстве (device)

Выполняются руками, протокол — в журнале ROADMAP. Набор и порядок — задачи P3-DEV-01..05.

| Проверка | Критерий |
|---|---|
| Старт в Expo Go | Приложение открывается, SQLite мигрирует, реестр зарегистрировал модули |
| Самолётный режим | Эссе и повторения работают без сети; после включения сети sync доставляет и оценка приходит |
| Сквозной курс | предмет → граф → плейсмент → курс → шаг → ответ |
| Производительность | Планирование карточки FSRS < 16 мс |

## 5. Матрица «требование → чем проверяется»

| Группа | Автотесты | Live | Device |
|---|---|---|---|
| ENG | `registry.test.ts`, `module.test.ts` | — | AC-01.4 |
| AUTH | `test_auth.py` | AC-02.1..6 | — |
| SYNC | `test_sync.py`, `test_job_retry.py`, `sync-service.test.ts` | AC-03.1..3 | AC-03.5 (live), 03.6, 03.9 |
| AI | `test_openai_gateway.py`, `test_usage.py`, `test_llm_cache.py`, `test_modules.py` | AC-04.2, AC-04.8 | — |
| SRS | `test_study.py` (карточка узла), `scheduler.test.ts` | AC-05.3 | AC-05.7 |
| KG/ASM/PLC/CRS | `test_cow`, `test_graph_access`, `test_centrality`, `test_content`, `test_assessment*`, `test_mastery`, `test_placement`, `test_course`, `test_study` | AC-08.*…11.* | AC-11.10 |
| UX | `next-action.test.ts` | AC-12.1..6 | AC-12.8 |

**Пробелы покрытия:** нет автотестов на `modules/*/generators.py` и на клиентские экраны; клиентская логика, кроме реестра, `nextAction` и `syncNow`, проверялась только живыми прогонами.
