#!/usr/bin/env bash
# Деплой staging из main (T-0031, R-0020). Запуск на сервере из корня суперпроекта:
#
#   scripts/deploy-staging.sh
#
# Порядок: обновить код и сабмодули до main → собрать образы → поднять базу → резервная копия и
# проверка её восстановления → поднять API (миграции применяются командой запуска контейнера
# ДО старта сервера) и воркер → дождаться /health. Если /health не ответил, скрипт падает и
# печатает, как откатиться: прежние образы и копия базы остаются.
set -euo pipefail
cd "$(dirname "$0")/.."

FILES="-f docker-compose.yml -f deploy/docker-compose.staging.yml"
COMPOSE="docker compose $FILES"
export COMPOSE

echo "→ обновляю код"
git fetch origin main
git checkout main
git pull --ff-only origin main
git submodule update --init --recursive --remote --merge

echo "→ собираю образы"
$COMPOSE build

echo "→ поднимаю базу"
$COMPOSE up -d postgres
for _ in $(seq 1 30); do
  [ "$($COMPOSE ps --format '{{.Health}}' postgres)" = "healthy" ] && break
  sleep 2
done

if $COMPOSE exec -T postgres psql -U "${POSTGRES_USER:-praxis}" -d "${POSTGRES_DB:-praxis}" -Atc "select 1 from alembic_version" >/dev/null 2>&1; then
  echo "→ резервная копия перед миграциями"
  BACKUP="$(scripts/backup-db.sh)"
  scripts/restore-check.sh "$BACKUP"
else
  echo "→ база пустая, копия не нужна"
fi

echo "→ поднимаю API (миграции) и воркер"
$COMPOSE up -d api worker

for _ in $(seq 1 30); do
  if $COMPOSE exec -T api python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health', timeout=3)" >/dev/null 2>&1; then
    echo "✓ staging поднят: /health отвечает"
    exit 0
  fi
  sleep 3
done

echo "✗ /health не ответил. Откат: git checkout <прежний коммит> && $COMPOSE up -d --build;" >&2
echo "  базу вернуть из копии: ${BACKUP:-.data/backups}" >&2
exit 1
