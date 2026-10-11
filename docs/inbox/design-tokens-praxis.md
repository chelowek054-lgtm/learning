Дизайн-токены Praxis для вкладки «Дизайн» консоли

Зачем: вкладка «Дизайн» в DocDD Console читает подтверждённую запись `design` с блоком `docdd-design` и по ней показывает токены, считает контраст, выгружает файл темы и сверяет его с кодом. Сейчас такой записи в проекте нет, поэтому вкладка пуста. Ниже блок, собранный из `learningFront/src/shared/config/design.ts` и `shared/ui/kit.tsx`. Заведите из него локальную запись `design` (общий источник практик подключён тегом `design`, это уже добавлено в project.yaml).

Что считается сделанным: запись `design` подтверждена, во вкладке «Токены» видны обе палитры и шкалы, нет предупреждений `design_block_invalid`, `design_scale_gap`, `design_contrast_low`; выгрузка для стека `expo` совпадает с файлом `learningFront/src/shared/config/design.ts` или расхождение разобрано задачей.

Откуда значения. Взято из кода как есть: палитры light и dark (12 ролей), отступы, радиусы, кегли, веса, множитель строки. Переведено в rem делением на 16. Добавлено мной как предложение, в коде этого нет: роли `accentText`, `info`, `focus`, толщины линий, размеры значков, длительности движения, шрифты, длина строки, сетка, язык интерфейса. Эти значения нужно решить человеку; роли `accentText` и `focus` равны `accent`, потому что акцент уже держит контраст 6,38:1 на светлом фоне и 8,76:1 на тёмном.

Контраст по правилам консоли считал сам, все пары проходят 4,5:1. Светлая тема: ink на bg 15,56; muted на bg 5,59, на surfaceAlt 5,08; accent на bg 6,38; onAccent на accent 6,93; onDanger на danger 7,6. Тёмная: ink на bg 15,66; muted на bg 8,15; accent на bg 8,76; onAccent на accent 9,01; onDanger на danger 7,81. Предложенный `info` (светлая #1D5F8F, тёмная #7FB6E0) держит 6,27 и 8,58.

```docdd-design
{
  "unit": "rem",
  "root": 16,
  "version": "1.0.0",
  "audience": { "markets": ["RU"], "outdoor": false },
  "principles": [
    "Телефон в первую очередь: экран начинается с 23.4375rem (375 px), веб — тем же кодом",
    "Зона нажатия не меньше 2.75rem (44 px)",
    "Контраст текста не ниже 4.5:1 в каждой теме; приглушённый текст уже даёт около 5:1, opacity поверх него не накладывать",
    "Цвет не единственный носитель смысла: рядом метка, значок или форма линии",
    "Светлая и тёмная темы обязательны на каждом экране; режим system следует за устройством",
    "Цвета и размеры берутся только из shared/config/design.ts, экраны ничего не объявляют сами",
    "core (янтарный) — смысловой цвет фундаментального ядра графа, не украшение",
    "Предложено: фокус выражается рамкой цветом focus, а не одним оттенком текста",
    "Предложено: движение выключается при системной настройке «уменьшить движение»"
  ],
  "typography": {
    "caption": { "size": 0.75,   "line": 1.05,   "weight": 600 },
    "small":   { "size": 0.8125, "line": 1.1375, "weight": 400 },
    "body":    { "size": 0.9375, "line": 1.3125, "weight": 400 },
    "lead":    { "size": 1.0625, "line": 1.4875, "weight": 500 },
    "title":   { "size": 1.375,  "line": 1.925,  "weight": 700 },
    "display": { "size": 1.75,   "line": 2.45,   "weight": 700 }
  },
  "spacing": { "xs": 0.25, "sm": 0.5, "md": 0.75, "lg": 1, "xl": 1.5, "xxl": 2 },
  "radius": { "sm": 0.5, "md": 0.75, "pill": 62.4375 },
  "border": { "thin": 0.0625, "thick": 0.09375 },
  "icon": { "sm": 1, "md": 1.25, "lg": 1.5 },
  "motion": { "fast": 120, "base": 200, "slow": 320 },
  "fonts": { "body": ["system-ui", "-apple-system", "Segoe UI", "sans-serif"] },
  "measure": 65,
  "grid": {
    "columns": 12,
    "gutter": 1,
    "breakpoints": { "xs": 0, "sm": 36, "md": 48, "lg": 62, "xl": 75, "xxl": 87.5 },
    "containers": { "sm": 33.75, "md": 45, "lg": 60, "xl": 71.25, "xxl": 82.5 }
  },
  "palette": {
    "light": {
      "bg": "#F4F6F4", "surface": "#FFFFFF", "surfaceAlt": "#E7ECE9",
      "ink": "#141F1C", "muted": "#516760", "line": "#D3DCD7",
      "accent": "#1B6552", "accentText": "#1B6552", "onAccent": "#FFFFFF",
      "core": "#835412", "ok": "#256A41", "info": "#1D5F8F", "warn": "#7B5911",
      "danger": "#973024", "onDanger": "#FFFFFF", "focus": "#1B6552"
    },
    "dark": {
      "bg": "#0E1412", "surface": "#18211F", "surfaceAlt": "#232F2C",
      "ink": "#E6EDE9", "muted": "#9CB0A8", "line": "#334340",
      "accent": "#6BC2A4", "accentText": "#6BC2A4", "onAccent": "#08110E",
      "core": "#E3AD68", "ok": "#7CC79A", "info": "#7FB6E0", "warn": "#E5BC74",
      "danger": "#EE9384", "onDanger": "#2A0F0A", "focus": "#6BC2A4"
    }
  },
  "i18n": { "default": "ru", "locales": ["ru", "en"], "fallback": "en" },
  "components": [
    { "name": "TopBar", "summary": "Заголовок вложенного экрана и «← Назад»; кнопка назад должна давать зону нажатия не меньше 2.75rem", "states": ["default", "active"], "parts": ["root", "back", "title"], "status": "stable" },
    { "name": "Card", "summary": "Поверхность; тон plain, accent (текущее действие) или core (ядро графа); нажимаемая — с откликом при нажатии", "states": ["default", "active"], "parts": ["root"], "status": "stable" },
    { "name": "Button", "summary": "primary, quiet, danger; занятое состояние busy показывает индикатор; высота не меньше 2.75rem", "states": ["default", "active", "focus", "disabled"], "parts": ["root", "label"], "status": "stable" },
    { "name": "Field", "summary": "Поле ввода; invalid подсвечивает рамку цветом danger", "states": ["default", "focus", "disabled"], "parts": ["root"], "status": "stable" },
    { "name": "Pill", "summary": "Метка-таблетка, тон muted, accent или core; не нажимаемая", "states": ["default"], "parts": ["root", "label"], "status": "stable" },
    { "name": "Progress", "summary": "Полоса прогресса высотой 0.375rem, тон accent или core", "states": ["default"], "parts": ["root", "fill"], "status": "stable" },
    { "name": "Empty", "summary": "Пустое состояние: короткая приглушённая подпись по центру", "states": ["default"], "parts": ["root"], "status": "stable" },
    { "name": "Screen", "summary": "Корень экрана: безопасная область, фон bg, прокрутка по умолчанию", "states": ["default"], "parts": ["root", "content"], "status": "stable" },
    { "name": "Note", "summary": "Строка пояснения с тоном muted, ok, warn или danger", "states": ["default"], "parts": ["root"], "status": "stable" },
    { "name": "Label", "summary": "Короткая разреженная метка заглавными, всегда приглушённая", "states": ["default"], "parts": ["root"], "status": "stable" },
    { "name": "AreaProgress", "summary": "Ход сборки по областям: ждёт, в работе, готово, сбой", "states": ["default"], "parts": ["root", "row", "dot"], "status": "stable" },
    { "name": "GradeView", "summary": "Разбор оценки ответа по критериям", "states": ["default"], "parts": ["root"], "status": "stable" }
  ],
  "overrides": []
}
```

Что найдено в коде и расходится с форматом консоли (это работа для задач, не для записи):
- Нет состояния `focus` у Button и Field: ни рамки, ни кольца при навигации с клавиатуры в вебе. Консоль требует его для обоих.
- В design.ts нет ролей `accentText`, `info`, `focus`, толщин линий, значков, движения, шрифтов, длины строки, сетки. Выгрузка для expo положит их в файл; сейчас файл их не знает, и проверка `design_theme_drift` покажет расхождение.
- Множитель строки: в design.ts записано 1,45, а в kit.tsx текст считается по 1,4. Выбрать одно число; в блоке выше стоит фактическое 1,4.
- Сетки и точек перелома в клиенте нет: веб-версия на широком экране растягивается на всю ширину. Нужен контейнер с максимальной шириной около 45rem на планшете и 60rem на десктопе, иначе проход Responsive будет находить замечания.
- Кнопка «← Назад» в TopBar: текст 15 px плюс hitSlop 8 даёт около 37 px по высоте, меньше 44.
- Интерфейс без словаря: все строки русские и зашиты в код. Для `i18n` консоль требует не меньше двух языков и английский; это отдельное решение человека — вводить словарь или осознанно держать русский единственным.
- Тёмная тема одна, без `oled` с чистым чёрным и без высококонтрастной темы. Для аудитории «не на улице» не обязательно, только отмечено.
- Нет эталонных макетов и снимков экранов: каталоги `docs/development/design/screens` и `design/mockups` пусты, вкладка «Экраны» не сможет запустить проход моделью.

Чего не делаем: не пишем файл темы вручную поверх выгрузки консоли; не вводим новые цвета вне ролей.
