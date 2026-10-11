# Выпуск приложения: dev-client, сборки, магазины, OTA

> Черновик (T-0034, R-0020, A-0006). Конфигурация в репозитории готова; шаги, требующие ваших аккаунтов,
> перечислены отдельно. Адреса API в `eas.json` — заглушки `*.example.invalid`: подставить после выбора хостинга
> (`hosting-options.md`).

## Что уже настроено

- **dev-client:** зависимость `expo-dev-client`, профиль `development` в `eas.json` (внутренняя раздача, APK).
- **Профили сборки:** `development`, `preview` (внутренняя раздача), `production` (автоувеличение номера сборки).
  У каждого свой канал обновлений (`development`, `preview`, `production`) и свой `EXPO_PUBLIC_API_BASE_URL`.
- **OTA:** зависимость `expo-updates`, `runtimeVersion` по версии приложения: обновление JS получают только сборки с
  той же версией, поэтому нативные изменения требуют новой сборки и новой версии.
- **Идентификаторы:** `ru.praxis.app` для iOS и Android (поменять до первой публикации, если нужен другой).

## Что нужно сделать вам (требует аккаунтов)

1. Аккаунт Expo и `eas login`; в `learningFront`: `eas init` (создаст проект и впишет `projectId` в `app.json`).
2. `eas update:configure` — впишет адрес обновлений в `app.json`.
3. Подставить реальные адреса API в `eas.json` (`preview`, `production`).
4. **Android:** аккаунт Google Play Console; ключ сервисного аккаунта для `eas submit`.
5. **iOS:** Apple Developer Program; `eas credentials` — сертификаты и профили.
6. Для push (T-0086): ключи FCM (Android) и APNs (iOS) загрузить в EAS (`eas credentials`).

## Команды

| Что | Команда |
|---|---|
| Сборка dev-client | `eas build --profile development --platform android` |
| Внутренняя сборка для проверки | `eas build --profile preview --platform all` |
| Сборка в магазины | `eas build --profile production --platform all` |
| Отправка в магазины | `eas submit --profile production --platform all` |
| OTA-исправление JS | `eas update --channel production --message "..."` |

## Правила выпуска

- Изменение JS и ресурсов — через `eas update` в канал; изменение нативных зависимостей, плагинов в `app.json` или
  версии SDK — новая сборка и новая версия приложения.
- SDK остаётся 54, пока публичный Expo Go его поддерживает (A-0006); при переходе на dev-client как основной способ
  проверки — отдельное решение о версии SDK.
- Перед публикацией: политика данных (`data-policy.md`) и текст для магазинов (запись голоса, push).
