#!/usr/bin/env bash
# Деплой staging на удалённый сервер по SSH (T-0031, R-0020). Запуск с вашего компьютера:
#
#   scripts/deploy-remote.sh user@host [каталог_на_сервере]
#
# Каталог по умолчанию — ~/praxis. Что делает: проверяет, что локальный main слит и отправлен, заходит на сервер
# и запускает там scripts/deploy-staging.sh (код → образы → копия базы и проверка → миграции и API → /health).
# Если на сервере нет проекта, сначала запустите scripts/bootstrap-server.sh.
set -euo pipefail

TARGET="${1:?Использование: scripts/deploy-remote.sh user@host [каталог_на_сервере]}"
DIR="${2:-~/praxis}"

cd "$(dirname "$0")/.."

# Деплоится то, что в origin/main: локальные незапушенные правки на сервер не попадут.
git fetch -q origin main
if [ "$(git rev-parse origin/main)" != "$(git rev-parse HEAD 2>/dev/null || true)" ] && [ "$(git branch --show-current)" = "main" ]; then
  echo "⚠ локальный main отличается от origin/main; на сервер уйдёт origin/main" >&2
fi
echo "→ деплою $(git rev-parse --short origin/main) на $TARGET:$DIR"

ssh -o ServerAliveInterval=30 "$TARGET" "cd $DIR && scripts/deploy-staging.sh"
echo "✓ готово: $TARGET"
