"""Живые проверки на реальном провайдере (V-0011, V-0075, V-0077).

Нужны: запущенный API (по умолчанию http://localhost:8000), настоящий LLM_API_KEY в его окружении
и контейнер Postgres проекта (docker compose). Каждый запуск заводит одноразового пользователя
`livecheck-…@example.com` в локальной базе и тратит несколько запросов к модели.

    python scripts/live_checks.py llm        # граф по теме и расход токенов (V-0011)
    python scripts/live_checks.py ielts      # эссе IELTS Task 2 по четырём критериям (V-0077)
    python scripts/live_checks.py rubrics    # Task 1 и TOEFL по своим рубрикам (V-0075)
    python scripts/live_checks.py placement  # плейсмент по живому графу: зонды расширяют границу (V-0057)

Код выхода 0 — проверка пройдена, 1 — нет. Заглушка вместо реальной модели считается провалом:
признак — расход токенов у пользователя в llm_usage и комментарии оценки не «mock».
"""

from __future__ import annotations

import base64
import json
import os
import subprocess
import sys
import time
import urllib.error
import urllib.request
import uuid
from datetime import datetime, timezone

BASE = os.environ.get("PRAXIS_API", "http://localhost:8000").rstrip("/")
DB_CONTAINER = os.environ.get("PRAXIS_DB_CONTAINER", "learning-postgres-1")
OPENER = urllib.request.build_opener(urllib.request.ProxyHandler({}))  # локальный адрес — мимо прокси

ESSAY = (
    "Some people think that governments should spend money on public transport rather than on "
    "building new roads. I agree with this view for several reasons. First, public transport "
    "moves many more people per hour than cars do, so it reduces congestion in large cities. "
    "Second, it is cheaper for ordinary families, which makes cities fairer. Third, fewer cars "
    "mean cleaner air and lower noise. However, roads are still needed for goods and emergency "
    "services, so governments should not stop building them completely. In conclusion, "
    "investment in buses, trams and trains brings greater long-term benefits than new roads, "
    "provided that the existing roads are maintained properly and used efficiently by everyone."
)
TASK1_ANSWER = (
    "The chart shows the share of households with internet access in three countries between "
    "2010 and 2020. Overall, access rose in every country, with the steepest growth in the "
    "country that started lowest. In 2010 the figures were 40, 60 and 75 percent. By 2020 they "
    "had reached 78, 88 and 95 percent respectively, so the gap between the countries narrowed "
    "considerably over the decade, although the leader stayed ahead throughout the period."
)


class Failed(Exception):
    pass


def check(cond: bool, message: str) -> None:
    if not cond:
        raise Failed(message)


def call(method: str, path: str, body: dict | None = None, token: str | None = None) -> dict:
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(
        f"{BASE}/v1{path}", data=data, method=method, headers={"Content-Type": "application/json"}
    )
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    # Провайдер модели иногда недоступен (API отвечает 502): это не провал проверки, повторяем.
    for attempt in range(3):
        try:
            with OPENER.open(req, timeout=300) as resp:
                return json.loads(resp.read() or b"{}")
        except urllib.error.HTTPError as e:
            if e.code == 502 and attempt < 2:
                time.sleep(3)
                continue
            raise Failed(f"{method} {path} → {e.code}: {e.read().decode()[:300]}") from e
        except urllib.error.URLError as e:
            raise Failed(f"API недоступен ({BASE}): {e.reason}") from e
    raise Failed(f"{method} {path}: провайдер модели недоступен")


def new_user() -> tuple[str, str]:
    email = f"livecheck-{uuid.uuid4().hex[:10]}@example.com"
    token = call("POST", "/auth/register", {"email": email, "password": uuid.uuid4().hex, "acceptPolicy": True})[
        "access_token"
    ]
    payload = token.split(".")[1]
    sub = json.loads(base64.urlsafe_b64decode(payload + "=" * (-len(payload) % 4)))["sub"]
    return token, sub


def tokens_spent(user_id: str) -> int:
    sql = f"select coalesce(sum(prompt_tokens + completion_tokens), 0) from llm_usage where user_id = '{user_id}'"
    out = subprocess.run(
        ["docker", "exec", DB_CONTAINER, "psql", "-U", "praxis", "-d", "praxis", "-Atc", sql],
        capture_output=True,
        text=True,
        check=False,
    )
    check(out.returncode == 0, f"не удалось прочитать llm_usage: {out.stderr.strip()[:200]}")
    return int(out.stdout.strip() or 0)


def grade(token: str, activity_type: str, rubric_id: str, answer: str, payload: dict) -> dict:
    """Отправить эссе на оценку через sync и вернуть оценку, пришедшую обратно."""
    aid, rid, jid = (str(uuid.uuid4()) for _ in range(3))
    # Оценки кэшируются по содержимому: метка делает запрос уникальным, иначе повторный
    # прогон получил бы чужой ответ из кэша без обращения к модели.
    answer = f"{answer} (ref {uuid.uuid4().hex[:8]})"
    call(
        "POST",
        "/sync/push",
        {
            "activities": [
                {
                    "id": aid,
                    "module": "languages",
                    "type": activity_type,
                    "connectivity": "online",
                    "payload": payload,
                }
            ],
            "responses": [
                {
                    "id": rid,
                    "activityId": aid,
                    "userAnswer": answer,
                    "localCreatedAt": datetime.now(timezone.utc).isoformat(),
                }
            ],
            "jobs": [
                {
                    "id": jid,
                    "type": "grade_writing",
                    "inputRef": {"responseId": rid, "rubricId": rubric_id},
                }
            ],
        },
        token,
    )
    pulled = call("GET", "/sync/pull", token=token)
    done = [j for j in pulled.get("jobs", []) if j["id"] == jid]
    check(done and done[0]["status"] == "done", f"job оценки не завершён: {done}")
    mine = [r for r in pulled.get("responses", []) if r["id"] == rid]
    check(mine and mine[0].get("grade"), "оценка не пришла вместе с ответом")
    return mine[0]["grade"]


def real_grade(g: dict, names: list[str]) -> None:
    check([c["name"] for c in g["criteria"]] == names, f"критерии {[c['name'] for c in g['criteria']]}")
    check(all(0 <= c["score"] <= c["max"] for c in g["criteria"]), "балл вне шкалы критерия")
    check(not any(c.get("comment") == "mock" for c in g["criteria"]), "оценка выдана заглушкой")
    check(all(str(c.get("comment", "")).strip() for c in g["criteria"]), "у критерия нет разбора")


def run_llm() -> str:
    token, uid = new_user()
    domain = f"livecheck-{uuid.uuid4().hex[:6]}"
    # Граф строится только по подтверждённой цели (T-0061): сначала диалог, потом построение.
    summary = call("POST", "/graph/goal/summarize", {"text": "Основы шахматных дебютов", "answers": []}, token)
    check(call("POST", "/graph/goal/confirm", {"domain": domain, **summary}, token)["confirmed"], "цель не подтверждена")
    graph = call(
        "POST",
        "/graph/canon/build",
        {"domain": domain, "topic": "Основы шахматных дебютов", "max_nodes": 4},
        token,
    )
    check(len(graph["nodes"]) >= 2, f"граф пуст: {len(graph['nodes'])} узлов")
    check(all(n["title"].strip() for n in graph["nodes"]), "у узла пустой заголовок")
    spent = tokens_spent(uid)
    check(spent > 0, "расход токенов не записан: вызов модели не состоялся")
    return f"граф из {len(graph['nodes'])} узлов, потрачено токенов: {spent}"


def run_ielts() -> str:
    token, uid = new_user()
    g = grade(
        token,
        "ielts_writing_task2",
        "ielts_writing_task2",
        ESSAY,
        {"prompt": "Governments should invest in public transport instead of new roads. Discuss.", "rubricId": "ielts_writing_task2"},
    )
    real_grade(
        g,
        ["Task Response", "Coherence and Cohesion", "Lexical Resource", "Grammatical Range and Accuracy"],
    )
    spent = tokens_spent(uid)
    check(spent > 0, "расход токенов не записан: оценка не от реальной модели")
    return f"оценка по 4 критериям, общий балл {g.get('overall')}, токенов: {spent}"


def run_rubrics() -> str:
    token, uid = new_user()
    t1 = grade(
        token,
        "ielts_writing_task1",
        "ielts_writing_task1",
        TASK1_ANSWER,
        {"prompt": "Summarise the chart.", "rubricId": "ielts_writing_task1", "data": {"title": "Internet access, %", "series": [{"label": "A", "values": [40, 78]}]}},
    )
    real_grade(
        t1,
        ["Task Achievement", "Coherence and Cohesion", "Lexical Resource", "Grammatical Range and Accuracy"],
    )
    tf = grade(
        token,
        "toefl_writing_independent",
        "toefl_writing_independent",
        ESSAY,
        {"prompt": "Do you agree that cities should favour public transport?", "rubricId": "toefl_writing_independent"},
    )
    real_grade(tf, ["Development", "Organization", "Language Use"])
    spent = tokens_spent(uid)
    check(spent > 0, "расход токенов не записан: оценка не от реальной модели")
    return f"Task 1 и TOEFL оценены по своим рубрикам, токенов: {spent}"


def correct_answer(item: dict):
    """Верный ответ на зонд: индекс правильного варианта или эталон для открытого вопроса."""
    for i, option in enumerate(item.get("options") or []):
        if option.get("correct"):
            return i
    return item["expected"]


def run_placement() -> str:
    token, uid = new_user()
    domain = f"livecheck-{uuid.uuid4().hex[:6]}"
    call(
        "POST",
        "/graph/canon/build",
        {"domain": domain, "topic": "Основы шахматных дебютов", "max_nodes": 12},
        token,
    )
    before = call("GET", f"/graph/placement/{domain}/map", token=token)
    check(not any(n["status"] == "known" for n in before["nodes"]), "до зондов уже есть освоенные узлы")

    probe = call("GET", f"/graph/placement/{domain}/probe?target=understand", token=token)
    answered, last_estimate = 0, {}
    for _ in range(12):
        if probe.get("done") or not probe.get("conceptId"):
            break
        result = call(
            "POST",
            "/graph/placement/answer",
            {
                "domain": domain,
                "concept_id": probe["conceptId"],
                "bloom": probe["bloom"],
                "answer": correct_answer(probe["item"]),
            },
            token,
        )
        estimate = result["mastery"]["estimate"]
        previous = last_estimate.get(probe["conceptId"], 0.0)
        check(estimate > previous, f"верный ответ не поднял оценку: {previous} → {estimate}")
        last_estimate[probe["conceptId"]] = estimate
        answered += 1
        probe = result.get("next") or {"done": True}

    after = call("GET", f"/graph/placement/{domain}/map", token=token)
    known = sum(1 for n in after["nodes"] if n["status"] == "known")
    check(answered >= 6, f"зондов задано {answered}, нужно не меньше шести")
    check(known >= 2, f"после {answered} верных ответов освоенных узлов {known}: граница не расширилась")
    check(len(last_estimate) >= 2, "зонды не перешли на другие узлы по мере освоения")
    check(tokens_spent(uid) > 0, "расход токенов не записан: граф построен не реальной моделью")
    return f"зондов {answered}, освоено узлов: {known}, затронуто узлов: {len(last_estimate)}"


CHECKS = {"llm": run_llm, "ielts": run_ielts, "rubrics": run_rubrics, "placement": run_placement}

if __name__ == "__main__":
    name = sys.argv[1] if len(sys.argv) > 1 else ""
    if name not in CHECKS:
        print(f"Использование: live_checks.py {{{'|'.join(CHECKS)}}}", file=sys.stderr)
        raise SystemExit(2)
    try:
        print(f"PASS {name}: {CHECKS[name]()}")
    except Failed as e:
        print(f"FAIL {name}: {e}")
        raise SystemExit(1)
