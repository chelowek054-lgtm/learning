# PostgreSQL 17 с расширениями для графа знаний (A-0024, A-0026, T-0072):
# Apache AGE (Cypher-запросы и обход графа) и pgvector (поиск кандидатов на слияние).
# Пакеты берутся из репозитория PGDG, уже подключённого в официальном образе.
FROM postgres:17
RUN apt-get update \
    && apt-get install -y --no-install-recommends postgresql-17-age postgresql-17-pgvector \
    && rm -rf /var/lib/apt/lists/*
# AGE загружается как библиотека при старте сервера: без этого `LOAD 'age'` и Cypher недоступны.
CMD ["postgres", "-c", "shared_preload_libraries=age"]
