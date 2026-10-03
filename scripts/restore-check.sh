#!/usr/bin/env bash
# Проверка, что резервная копия восстанавливается (T-0031, R-0020):
#
#   scripts/restore-check.sh [файл.sql.gz]     # без аргумента — самый свежий дамп из .data/backups
#
# Копия накатывается во ВРЕМЕННУЮ базу `restore_check` (рабочая не трогается), затем сверяются
# версия миграций и число таблиц с рабочей базой, и временная база удаляется. Код выхода 0 —
# копия восстанавливается и совпадает по структуре.
set -euo pipefail
cd "$(dirname "$0")/.."

COMPOSE="${COMPOSE:-docker compose}"
PGUSER="${POSTGRES_USER:-praxis}"
PGDB="${POSTGRES_DB:-praxis}"
TMPDB="restore_check"
FILE="${1:-$(ls -1t .data/backups/praxis-*.sql.gz 2>/dev/null | head -n 1 || true)}"

if [ -z "$FILE" ] || [ ! -f "$FILE" ]; then
  echo "Нет файла копии (ожидался .data/backups/praxis-*.sql.gz)" >&2
  exit 1
fi

psql_in() { $COMPOSE exec -T postgres psql -U "$PGUSER" -v ON_ERROR_STOP=1 -At "$@"; }

cleanup() { psql_in -d postgres -c "DROP DATABASE IF EXISTS $TMPDB" >/dev/null 2>&1 || true; }
trap cleanup EXIT

cleanup
psql_in -d postgres -c "CREATE DATABASE $TMPDB" >/dev/null
gzip -dc "$FILE" | $COMPOSE exec -T postgres psql -U "$PGUSER" -d "$TMPDB" -v ON_ERROR_STOP=1 -q >/dev/null

version() { psql_in -d "$1" -c "select version_num from alembic_version"; }
tables() { psql_in -d "$1" -c "select count(*) from information_schema.tables where table_schema='public'"; }

LIVE_V="$(version "$PGDB")"; COPY_V="$(version "$TMPDB")"
LIVE_T="$(tables "$PGDB")";  COPY_T="$(tables "$TMPDB")"

if [ "$LIVE_V" != "$COPY_V" ] || [ "$LIVE_T" != "$COPY_T" ]; then
  echo "Копия не совпадает с рабочей базой: миграция $COPY_V vs $LIVE_V, таблиц $COPY_T vs $LIVE_T" >&2
  exit 1
fi
echo "Копия $FILE восстанавливается: миграция $COPY_V, таблиц $COPY_T"
