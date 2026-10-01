---
id: A-0002
type: decision
title: Клиент на Expo/React Native по Feature-Sliced Design; ядро в shared/engine
status: approved
created: 2026-09-30
updated: 2026-10-01
---

# Клиент на Expo/React Native по Feature-Sliced Design; ядро в shared/engine

Принято 2026-07-04. Один код на iOS/Android, команда знает TypeScript. Клиент организован по FSD (app→pages→widgets→features→entities→shared); доменно-независимое ядро (Activity, реестр модулей, порты, FSRS) живёт в src/shared/engine как нижний слой FSD. Метаданные модулей — в entities/module, сборка манифестов с рендерерами — в widgets/module-registry, рендереры — в features. Отвергнуты Flutter (другой язык) и модули как npm-пакеты (workspaces усложняют Expo). Границы слоёв пока держатся на ревью — линтер не подключён (P3-CI-04).

## Журнал

- 2026-09-30 · заведена из docs/inbox/decision-client-expo-fsd.md · приложение
- 2026-10-01 · на подтверждение · architect
- 2026-10-01 · подтверждён · architect
