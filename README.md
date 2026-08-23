# Praxis

Персональная адаптивная обучающая платформа (iOS/Android) для изучения языков (TOEFL/IELTS) и технологий (ML/программирование).

Этот репозиторий — **git-суперпроект**: документация + два сабмодуля.

```
learning/                 ← суперпроект (docs — источник правды)
├── docs/                 архитектура, планы, (позже) business и deploy
├── learningFront/        сабмодуль: клиент (Expo/React Native, FSD)
└── learningBack/         сабмодуль: backend (FastAPI, Python, uv)
```

- **learningFront** — фронтенд по **Feature-Sliced Design**. Доменно-независимое ядро — в `src/shared/engine`. См. [docs/architecture/04-frontend-fsd.md](./docs/architecture/04-frontend-fsd.md).
- **learningBack** — backend, связан с клиентом только по HTTP. Ключ Claude — только здесь (инвариант №2).

## RoadMap — где проект сейчас

**[`ROADMAP.md`](./ROADMAP.md) — единая точка фиксации прогресса.** Отвечает на три вопроса: *где мы сейчас*, *что уже сделано (с доказательствами проверки)* и *что дальше*. Прогресс по проекту фиксируется всегда здесь — при каждом закрытом рабочем потоке.

| Фаза | Статус | Прогресс |
|---|---|---|
| [Фаза 0 — Каркас](./docs/plans/phase-0-foundation.md) | ✅ done | 34/34 задач |
| [Фаза 1 — MVP](./docs/plans/phase-1-mvp.md) | ✅ done (код) | 33/33 задач |
| [Фаза 2 — Модель знаний](./docs/plans/phase-2-knowledge-model.md) | 🟡 **в работе** | 9/21 · KG1–KG2 ✅, дальше **KG3** |
| Фаза 3 — Речь и рецепция | ⚪ ожидает | не декомпозирована |
| Фаза 4 — Продукт | ⚪ ожидает | не декомпозирована |

Что где лежит: **`ROADMAP.md`** — сводка, журнал вех, риски и реестр открытых вопросов; **[`docs/plans/`](./docs/plans/README.md)** — исполняемые чеклисты задач по фазам; **[`docs/architecture/`](./docs/architecture/README.md)** — как система устроена. Изменение архитектуры фиксируется сначала в `docs/architecture/`, затем в плане фазы, затем в роадмапе.

## Документация — единый источник правды

- 🗺️ [`ROADMAP.md`](./ROADMAP.md) — прогресс, фазы, журнал вех, риски
- 📚 [`docs/`](./docs/README.md) — обзор, инварианты, глоссарий
- 🏛️ [`docs/architecture/`](./docs/architecture/README.md) — архитектурный, логический, функциональный, FSD-планы, модель знаний
- 🗂️ [`docs/plans/`](./docs/plans/README.md) — чеклисты фаз · текущая: [Фаза 2 — Модель знаний](./docs/plans/phase-2-knowledge-model.md)

## Клонирование (с сабмодулями)

```bash
git clone --recurse-submodules <url>
# или после обычного клона:
git submodule update --init --recursive
```

## Запуск

**Весь стенд (Postgres + API) через docker-compose из корня** — оркестрация всех сервисов живёт здесь (масштабируется на будущие микросервисы/внешние сервисы). Данные контейнеров — в `./.data` (вне git).

```bash
cp .env.example .env          # параметры стенда (креды/порты)
docker compose up --build     # Postgres + миграции + API + pgAdmin
```

| Сервис | Адрес | Примечание |
|---|---|---|
| API (Swagger) | http://localhost:8000/docs | |
| Postgres | `localhost:5432` | креды из `.env` |
| pgAdmin | http://localhost:5050 | без логина; подключение «Praxis (docker)» уже прописано, пароль спросит при первом коннекте |

pgAdmin — dev-инструмент, приложение с ним не связано. Поднять стенд без него: `docker compose up postgres api`.

Отдельные сервисы для разработки:

```bash
# Клиент (Expo)
cd learningFront && npm install && npx expo start

# Только backend локально (Postgres можно поднять из корня: docker compose up -d postgres)
cd learningBack && uv sync && uv run uvicorn core.app:app --reload
```

> **DevOps-раскладка:** `docker-compose.yml`, `.env.example`, `./.data` — в корне (оркестрация). `Dockerfile` каждого сервиса — в его сабмодуле (build-рецепт). Так добавление нового сервиса = новый блок в корневом compose + свой Dockerfile в его репозитории.
