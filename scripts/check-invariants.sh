#!/usr/bin/env bash
# Проверка инвариантов системы (docs/10-requirements/verification.md §2).
# Запуск из корня суперпроекта: scripts/check-invariants.sh
# Код возврата 1, если хоть один инвариант нарушен.
set -u
cd "$(dirname "$0")/.."

FRONT=learningFront/src
BACK=learningBack
fail=0

check() { # имя, ожидание-пусто: команда выводит нарушения
  local name="$1"; shift
  local out
  out=$("$@" 2>/dev/null || true)
  if [ -n "$out" ]; then
    echo "FAIL  $name"; echo "$out" | sed 's/^/        /'; fail=1
  else
    echo "ok    $name"
  fi
}

if [ ! -d "$FRONT" ] || [ ! -d "$BACK/core" ]; then
  echo "Сабмодули не инициализированы: git submodule update --init"; exit 2
fi

# NFR-02: ключей провайдера нет в клиенте
check "NFR-02 ключей LLM нет в клиенте" \
  grep -rniE "llm_api_key|sk-[a-z0-9]{10}" "$FRONT"

# NFR-03: ядро клиента без предметного кода (тесты ядра могут называть модули)
check "NFR-03 shared/engine без доменных строк" \
  bash -c "grep -rniE 'languages|ielts|toefl|concept|knowledge' '$FRONT/shared/engine' --include=*.ts --exclude=*.test.ts | grep -vE ':[0-9]+:[[:space:]]*(//|\*|/\*)'"

# NFR-03: ядро backend не импортирует модули и не знает их имён
check "NFR-03 core/ не импортирует modules" \
  grep -rnE "^\s*(from|import) modules" "$BACK/core"
check "NFR-03 core/ без имён модулей" \
  grep -rnE "[\"'](languages|ml|knowledge)[\"']" "$BACK/core" --include=*.py

# NFR-KG-1: ядро не знает про граф
check "NFR-KG-1 core/ без логики графа" \
  grep -rnE "concept_edge|UserConcept|effective_graph|ConceptEdge" "$BACK/core" --include=*.py

# NFR-KG-2 (T-0052): модуль графа не знает предметов — ни слов, ни веток по названию
check "NFR-KG-2 модуль графа без предметных слов"   grep -rniE "ielts|toefl|english|английск|машинн|нейро|backprop|softmax|трансформер|python|программир" "$BACK/modules/knowledge" --include=*.py

# AC-12.4: цвета только в design.ts
check "AC-12.4 цвета только в design.ts" \
  bash -c "grep -rnE '#[0-9a-fA-F]{3,8}\b' '$FRONT' --include=*.ts --include=*.tsx | grep -v 'shared/config/design.ts' | grep -v '\.test\.'"

[ "$fail" -eq 0 ] && echo "Инварианты соблюдены" || echo "Есть нарушения"
exit "$fail"
