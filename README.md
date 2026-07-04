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

## Документация — единый источник правды

- 📚 [`docs/`](./docs/README.md) — обзор, инварианты, глоссарий
- 🏛️ [`docs/architecture/`](./docs/architecture/README.md) — архитектурный, логический, функциональный, FSD-планы
- 🗺️ [`docs/plans/`](./docs/plans/README.md) — план разработки · текущая фаза: [Фаза 0](./docs/plans/phase-0-foundation.md)

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
docker compose up --build     # Postgres + миграции + API → http://localhost:8000/docs
```

Отдельные сервисы для разработки:

```bash
# Клиент (Expo)
cd learningFront && npm install && npx expo start

# Только backend локально (Postgres можно поднять из корня: docker compose up -d postgres)
cd learningBack && uv sync && uv run uvicorn core.app:app --reload
```

> **DevOps-раскладка:** `docker-compose.yml`, `.env.example`, `./.data` — в корне (оркестрация). `Dockerfile` каждого сервиса — в его сабмодуле (build-рецепт). Так добавление нового сервиса = новый блок в корневом compose + свой Dockerfile в его репозитории.
