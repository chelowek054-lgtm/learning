# Фаза 1 — MVP

**Цель фазы:** собрать первый работающий вертикальный срез, доказывающий главную гипотезу — **AI-скоринг продукции по рубрикам эффективнее изолированных карточек** — и универсальность движка (один Activity-движок тянет и язык, и ML). Всё offline-first.

**Ключевой сценарий, который должен заработать end-to-end:**
```
Новый пользователь → регистрация (свой JWT) → онбординг (цели)
 → Writing: пишет эссе ОФЛАЙН → мгновенный черновой сигнал (локальный fallback)
   → появилась сеть → sync → AI-скоринг по рубрике IELTS (4 критерия + ошибки + образец)
   → ошибки автоматически → карточки vocab_srs
 → SRS: повторяет карточки, интервалы обновляются (FSRS)
 → ML: читает материал → concept_recall (открытый ответ) → AI-проверка → слабые концепты в SRS
```

**Решения (зафиксированы перед планированием):**
- **Auth:** собственный JWT в FastAPI (закрывает открытый вопрос Ф0).
- **Охват:** оба домена — `ielts_writing_task2` + `vocab_srs` (языки) **и** `material_read`+`concept_recall` (ML).
- **Offline:** полный offline-first сразу — очередь jobs + двухфазный sync + офлайн-fallback (инвариант №1).

**Не входит в фазу:** Speaking/STT, listening/reading-дриллы, генерация passages, PDF-импорт, мульти-девайс, монетизация (Фазы 2–4).

**Предпосылки:** Фаза 0 завершена (каркас поднят и проверен). Архитектура — [docs/architecture](../architecture/README.md); контракты ядра (порты `SyncClient`/`JobQueue`/`LocalStore`, `Scheduler`, `ModuleManifest`) уже есть в `shared/engine`; схема БД и роутеры-заглушки — в `learningBack`.

> ⚠️ Требуется **CLAUDE_API_KEY** в `learningBack/.env` для реального AI-скоринга. Для разработки без ключа — `MockAIGateway` (WS3). Модели: `claude-opus-4-8` (скоринг), `claude-sonnet-4-6` (генерация) — сверять актуальность через skill `claude-api`.

---

## Definition of Done фазы

1. ✅ Регистрация/логин по своему JWT; токен в SecureStore; защищённые запросы работают.
2. ✅ Эссе пишется **офлайн**, даёт мгновенный черновой сигнал; при сети — синкается и получает AI-скоринг по рубрике IELTS Writing Task 2 (4 критерия band + ошибки + образец).
3. ✅ Ошибки из скоринга автоматически превращаются в карточки `vocab_srs`.
4. ✅ SRS-повторения работают офлайн (FSRS), очередь «на сегодня» корректна.
5. ✅ ML-трек: `material_read` → `concept_recall` → AI-проверка → слабые концепты в `concept_srs`.
6. ✅ Онбординг задаёт цели (target band, ML-темы) в профиль; Home показывает «на сегодня».
7. ✅ Инварианты Ф0 сохранены: offline-first, ключ LLM только на backend, ядро доменно-независимо, единый `response`-лог.

---

## Рабочие потоки

**Фундамент** (WS1–WS4) → **вертикальные фичи** (WS5–WS7) → **опыт** (WS8).

```
FOUNDATION
  WS1 Auth (JWT)          backend + клиент
  WS3 AI-gateway (Claude) backend  ─┐
  WS4 Рубрики+генераторы  backend  ─┴─ (WS4 после WS3)
  WS2 Sync + Job Queue    backend + клиент

FEATURES (после WS1–WS4)
  WS5 Writing (ielts_writing_task2)
  WS6 Vocab SRS (vocab_srs)
  WS7 ML-трек (material_read + concept_recall)

EXPERIENCE
  WS8 Онбординг + Home + навигация + простой адаптивный план
```

Порядок: **WS1 → (WS3 → WS4) ∥ WS2 → (WS5 ∥ WS6 ∥ WS7) → WS8**. Онбординг (WS8) частично можно начинать параллельно после WS1.

---

## WS1 — Аутентификация (собственный JWT) · ✅ done (backend live, клиент typecheck+bundle)

**Backend (learningBack):**
- [x] `P1-WS1-01` Миграция `0002`: `user.password_hash`. Хеширование (`pwdlib`/argon2). Pydantic-схемы register/login.
- [x] `P1-WS1-02` `/auth/register`, `/auth/login` → выдача access-JWT; зависимость `get_current_user` (verify JWT). Секрет JWT — из окружения.
- [x] `P1-WS1-03` Защитить роуты `sync`/`jobs`/`content` зависимостью аутентификации (per-user контекст).

**Клиент (learningFront):**
- [x] `P1-WS1-04` `expo-secure-store` для токена; `shared/api` http-клиент с `Authorization: Bearer`; auth-состояние (контекст в `shared/lib` или `entities/session`).
- [x] `P1-WS1-05` Экраны `pages/auth` (login/register), тонкие роуты; route-guard: без токена → редирект на login.

**DoD WS1:** register → login → токен сохранён → защищённый запрос проходит; без токена — редирект.

---

## WS2 — Sync + Job Queue (offline-first мост) · ✅ done (backend live, клиент typecheck+bundle)

**Backend:**
- [x] `P1-WS2-01` `POST /sync/push` (responses, jobs, srs_cards наверх) + `GET /sync/pull` (done-jobs, srs_cards вниз); per-user; LWW по времени; идемпотентность по `id`.
- [x] `P1-WS2-02` Персист jobs + переходы статусов (`pending→running→done/failed`); enqueue при push.

**Клиент:**
- [x] `P1-WS2-03` Реализация порта `SyncClient` (HTTP push/pull) и `JobQueue` (поверх SQLite-таблицы `job`) — контракты [02 §5](../architecture/02-logical.md#5-job-queue-и-синхронизация).
- [x] `P1-WS2-04` Детекция сети (`expo-network`); триггер sync (на foreground/появление сети + ручной); применение результатов pull (grade → response, новые cards → deck).

**DoD WS2:** офлайн-созданные `response`+`job` уходят наверх при сети; `done`-job и карточки приходят вниз; повторный push не двоит (идемпотентность).

---

## WS3 — AI-gateway (Claude) · ✅ done (Mock live; Claude — при ключе)

**Backend:**
- [x] `P1-WS3-01` Зависимость `anthropic`; реализация `AIGateway.grade/generate` через Claude с **structured output** (tool-use по `rubric.schema`); выбор модели per-rubric.
- [x] `P1-WS3-02` Реестр рубрик (загрузка из таблицы `rubric`); рендер промпта (шаблон рубрики + activity + ответ пользователя).
- [x] `P1-WS3-03` Валидация результата по `rubric.schema` → строгий `Grade`; логирование токенов per-user/type; кэш детерминированной генерации по хэшу входа.
- [x] `P1-WS3-04` `MockAIGateway` (детерминированная заглушка) за тем же интерфейсом — для разработки/тестов без ключа. Выбор реализации по наличию `CLAUDE_API_KEY`.

**DoD WS3:** по рубрике+ответу gateway возвращает валидный `Grade` (реальный Claude при ключе; mock — без). Ключ только из окружения (инвариант №2).

---

## WS4 — Рубрики и генераторы контента · ✅ done (live seed + скоринг)

**Backend (модули `languages`/`ml`):**
- [x] `P1-WS4-01` Рубрика `ielts_writing_task2` v1: 4 критерия band-descriptors (Task Response, Coherence & Cohesion, Lexical Resource, Grammar) — промпт + `schema` (по [Grade](../architecture/02-logical.md#7-модель-grade-результат-скоринга)); модель `claude-opus-4-8`. Seed.
- [x] `P1-WS4-02` Рубрика `concept_check` (ML `concept_recall`): критерии correctness/completeness/explanation — промпт + schema. Seed.
- [x] `P1-WS4-03` Генераторы: стартовая колода **Academic Word List** (`vocab_srs`), маппинг `grade.errors → srs_card`, `concept_recall` из `material`.
- [x] `P1-WS4-04` Seed демо-контента: выборка AWL + один ML-`material` + промпт эссе IELTS.

**DoD WS4:** рубрики грузятся реестром; генераторы дают карточки; seed наполняет демо-контент.

---

## WS5 — Writing: `ielts_writing_task2` (главная гипотеза)

**Клиент (feature-слайс `features/ielts-writing`):**
- [ ] `P1-WS5-01` Рендерер: редактор эссе (промпт задания + ввод + счётчик слов).
- [ ] `P1-WS5-02` **Офлайн-fallback** локальный грейдер (`LocalGrader`): объём, структура абзацев, покрытие AWL → мгновенный черновой сигнал.
- [ ] `P1-WS5-03` Submit → `appendResponse` + `enqueueJob(grade_writing)` (работает офлайн).
- [ ] `P1-WS5-04` Экран разбора: 4 критерия band, список ошибок, образец; обновление из pull (`response.grade`).
- [ ] `P1-WS5-05` Error-log: `grade.errors` → карточки `vocab_srs` (генерация на backend + pull).

**DoD WS5:** эссе офлайн → черновой сигнал → sync → AI-скоринг по рубрике → ошибки стали карточками.

---

## WS6 — Vocab SRS: `vocab_srs`

**Клиент (feature-слайс `features/vocab-review`):**
- [ ] `P1-WS6-01` Рендерер карточки: front/back, кнопки отзыва (again/hard/good/easy).
- [ ] `P1-WS6-02` Планировщик: отзыв → `Scheduler.review` → обновление `fsrs_state`+`due_at` в `LocalStore`; `appendResponse`.
- [ ] `P1-WS6-03` Очередь «на сегодня» из `LocalStore.listDueSrsCards`.
- [ ] `P1-WS6-04` Колода питается из error-log (WS5) + стартовый AWL (WS4).

**DoD WS6:** due-карточки повторяются, интервалы обновляются офлайн, карточки из ошибок появляются в колоде.

---

## WS7 — ML-трек: `material_read` + `concept_recall`

**Клиент (feature-слайсы `features/material-read`, `features/concept-recall`):**
- [ ] `P1-WS7-01` `material-read`: чтение закэшированного `material`.
- [ ] `P1-WS7-02` `concept-recall`: вопрос → открытый ответ → `enqueueJob(grade_concept)`.
- [ ] `P1-WS7-03` Разбор AI-проверки (верно/частично + объяснение); ошибки → `concept_srs`.

**DoD WS7:** материал прочитан → вопрос на понимание → AI-фидбек → слабые концепты в SRS. Доказывает: тот же движок тянет ML.

---

## WS8 — Онбординг + Home + навигация

**Клиент:**
- [ ] `P1-WS8-01` Онбординг: выбор целей (IELTS/TOEFL target band, ML-темы) → профиль (клиент + backend `user.profile`).
- [ ] `P1-WS8-02` Home = «на сегодня»: due-SRS + активности, через `ActivityDispatcher` (виджет `TodayQueue`).
- [ ] `P1-WS8-03` Навигация (табы Home/Review/Learn/Profile); интеграция route-guard из WS1.
- [ ] `P1-WS8-04` Простой адаптивный план: слабейший критерий из `response`-лога → предложить фокус (правило, не ML).

**DoD WS8:** онбординг задаёт цели; Home показывает работу на сегодня; приложение проходимо end-to-end.

---

## Новые зависимости

- **Backend:** `anthropic` (Claude), `pwdlib[argon2]` (хеш паролей), `pyjwt` (JWT).
- **Клиент:** `expo-secure-store` (токен), `expo-network` (детекция сети).

---

## Проверки в конце фазы (сквозной прогон)

- [ ] Регистрация→онбординг→эссе офлайн→черновой сигнал→sync→AI-grade→ошибки в SRS→повторение.
- [ ] ML: материал→recall→AI-проверка→концепт в SRS.
- [ ] Всё полезно офлайн; sync доганяет при сети; повторный sync идемпотентен.
- [ ] Инварианты: ключ LLM не в клиенте/git; ядро без доменных строк; единый `response`-лог питает FSRS и адаптацию.

---

## Открытые вопросы Фазы 1

1. **Приватность:** тексты эссе/ответов уходят в Claude для скоринга — зафиксировать политику хранения на backend (что логируем, TTL) до реального использования.
2. **Стоимость LLM:** лимиты/кэш/выбор дешёвой модели где можно — базово в WS3, тюнинг по факту расходов.
3. **Источник Academic Word List:** какой список берём (AWL Coxhead / свой) для стартовой колоды — решить в WS4.
4. **Секрет JWT и срок токена:** длительность access-токена, нужен ли refresh — уточнить в WS1 (для «для себя» достаточно долгого access).
5. **Формат офлайн-fallback для Writing:** какие именно эвристики дают полезный черновой сигнал без LLM — детализировать в WS5.
