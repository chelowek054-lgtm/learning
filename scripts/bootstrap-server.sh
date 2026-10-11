#!/usr/bin/env bash
# Первичная подготовка сервера для staging (T-0031). Запуск с вашего компьютера, один раз:
#
#   scripts/bootstrap-server.sh user@host git@github.com:ORG/learning.git [каталог_на_сервере]
#
# Ставит Docker (если нет), клонирует проект с сабмодулями, создаёт .env из .env.example и останавливается:
# секреты (POSTGRES_PASSWORD, JWT_SECRET, ADMIN_SESSION_SECRET, LLM_API_KEY, S3_*) вписываете вы на сервере.
# TLS-прокси (Caddy или nginx) перед портом API ставится отдельно, см. docs/60-operations/environments.md.
set -euo pipefail

TARGET="${1:?Использование: scripts/bootstrap-server.sh user@host repo-url [каталог]}"
REPO="${2:?Нужен адрес репозитория}"
DIR="${3:-praxis}"

ssh "$TARGET" bash -s -- "$REPO" "$DIR" <<'REMOTE'
set -euo pipefail
REPO="$1"; DIR="$2"
if ! command -v docker >/dev/null 2>&1; then
  echo "→ ставлю Docker"
  curl -fsSL https://get.docker.com | sh
fi
docker compose version >/dev/null
if [ ! -d "$DIR/.git" ]; then
  git clone --recurse-submodules "$REPO" "$DIR"
fi
cd "$DIR"
[ -f .env ] || cp .env.example .env
echo "✓ проект в ~/$DIR. Впишите секреты: nano ~/$DIR/.env"
echo "  затем поставьте TLS-прокси и запустите с компьютера: scripts/deploy-remote.sh <user@host> ~/$DIR"
REMOTE
