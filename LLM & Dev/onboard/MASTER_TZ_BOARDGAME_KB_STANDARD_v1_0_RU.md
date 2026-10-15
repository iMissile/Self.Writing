# МАСТЕР-ТЕХНИЧЕСКОЕ ЗАДАНИЕ
## Глубокое исследование настольных игр и создание доказательной базы знаний

**Версия:** 1.0  
**Дата:** 2026-10-09  
**Статус:** нормативный универсальный шаблон для подготовки игровых, предметно-ориентированных ЧТЗ  
**Адресаты:** старший аналитик / исследователь (этап предварительной разведки), студент-первокурсник / оператор данных (этап исполнения), QA-проверяющий, локальный исследовательский агент  
**Формат поставки настоящего документа:** один Markdown-файл; приложения, упоминаемые ниже, являются *будущими выходными артефактами при анализе конкретной игры*, а не файлами, включёнными в текущий универсальный шаблон.  
**Область применения:** карточные, экономические, асимметричные, приключенческие, кооперативные и гибридные настольные игры, их дополнения, локализации, промоматериалы, версии правил, цифровые реализации и содержательный архив обсуждений.

> **Основное требование.** Старший аналитик сначала проводит собственное глубокое расследование и по возможности закрывает discovery и verification. Студенту выдаётся **исполняемое, предзаполненное ТЗ**, а не задание «найти информацию об игре». В любой записи должно быть понятно: что известно, откуда известно, что осталось проверить, чем проверять и когда считать задачу завершённой.

> **Политика тяжёлых медиа первого прохода.** Сканы отдельных карт размером **от 10 МБ на карту**, PDF **со сканами карт** размером **от 50 МБ**, видео размером **от 30 МБ** не скачивать в первом проходе. Сохранять точные URL, метаданные, признаки качества, размер или оценку размера, ценность, статус доступности и прогноз общего объёма отложенной загрузки. Порог трактуется включительно: `>=`. Для единообразного машинного контроля **1 МБ = 1 000 000 байт**. При неизвестном размере сначала делать только безопасную метаинвентаризацию, а не слепую полную загрузку.

---

# 1. Назначение и результат

## 1.1. Задача

Для указанной заказчиком игры `[GAME]` и всех *релевантных* официальных дополнений, переизданий, промоматериалов и локализаций сформировать долговременный, воспроизводимый, пригодный для машинного поиска и человеческой проверки корпус. В результате база знаний (БЗ) должна отвечать не просто «что написано на карте», а:

1. какая **логическая игровая сущность** описывается;
2. в каком продукте и физическом тираже она встречается;
3. какой текст, символ, рисунок и оформление имела конкретная печать;
4. какое правило действовало для неё в выбранном временном и игровом контексте;
5. какие FAQ, официальные rulings, errata, replacement и локализации меняли понимание;
6. как сущность взаимодействует с другими картами, действиями, ресурсами, состояниями и дополнениями;
7. какие стратегии, комбинации и противодействия обсуждаются, при каких условиях они применимы и какими доказательствами подкреплены;
8. где лежит исходный материал, какова его доказательная сила и почему ему можно или нельзя доверять;
9. что найдено, что не найдено, что нельзя проверить без физической коробки и что сознательно отложено из-за объёма.

## 1.2. Цепочка обработки

```text
DISCOVER → VERIFY → REGISTER → ACQUIRE_WHEN_ALLOWED → HASH
→ PROVENANCE → AUTHORITY → VERSION / EDITION / FORMAT
→ LOSSLESS_TRANSCRIBE → SEMANTIC_NORMALIZE → CROSS-CHECK
→ RULES / COMPONENT / STRATEGY GRAPH → QA
→ MACHINE-READABLE CORPUS → OBSIDIAN / FULL-TEXT / RAG
→ AUDIT REPORT → HANDOFF / CHECKPOINT
```

Если найден исчезающий небольшой источник, который разрешено сохранять, его надо зарегистрировать и заархивировать до разработки идеального парсера. Если найден тяжёлый носитель выше порога — зарегистрировать и **отложить** согласно §8.

## 1.3. Не является достаточным результатом

- один PDF с правилами или набор ссылок;
- таблица названий без печатных текстов, номеров, символов и версий;
- выгрузка чужой wiki без origin и lineage;
- OCR без визуальной проверки;
- галерея изображений без соответствия `entity_id ↔ printing_id ↔ image_asset_id`;
- пересказ BGG или произвольный tier list, выданный за подтверждённую мету;
- переписывание старого текста карты современной эрратой без хранения старой версии;
- архив с десятками гигабайт файлов без каталога, контрольных сумм и статусов;
- заявление «исследование завершено» при незакрытых критических проверках.

---

# 2. Роли, границы ответственности и порядок выполнения

| Роль | Зона ответственности | Что запрещено перекладывать |
|---|---|---|
| **Старший аналитик** | Предварительный веб- и архивный поиск, установление состава, поиск исходных URL, разбор конфликтов, формальная модель игры, первичные карточные/компонентные реестры, критические rulings, стратегические гипотезы, рабочие таблицы и схемы | Не отправлять студента заново искать очевидные официальные источники, состав дополнений, основные редкие материалы и принципиальные трактовки |
| **Студент-первокурсник** | Структурированное сохранение, сверка, разметка, транскрипция, заполнение предопределённых схем, фиксация исключений, запуск готовых QA-проверок | Не изобретать онтологию и не выносить самостоятельно окончательный вердикт о спорном ruling / переводе |
| **QA / старший ревьюер** | Независимая сверка существенных сведений, проверка состава, текстов и статусов доказательности, решение о допуске записей в `ACCEPTED` | Не допускать автоматического повышения доверия по одной копии или реконструкции |
| **Владелец** | Уточнение приоритета имеющейся коробки, выбор локализации, передача собственных сканов при необходимости, утверждение специально помеченных исключений | Не обязан повторно собирать открытые интернет-сведения, доступные аналитику |

**Два этапа обязательны.**

- **Этап S — Senior Research.** Выпускается предметно-ориентированный ЧТЗ с `VERIFIED_BASELINE`, `SOURCE_SEEDS`, `CANONICAL_SEEDS`, `OPEN_QUESTIONS`, `RESEARCH_DISPOSITIONS`, конкретными URL, именами файлов, версиями, исходными таблицами и очередями. Состояния указываются честно: `VERIFIED / PARTIAL / OPEN / BLOCKED / BOUNDED_NEGATIVE`.
- **Этап J — Junior Execution.** Студент выполняет заранее расписанные work packages и исправляет их до приёмки. Если появляется новое сложное противоречие, оно эскалируется старшему аналитику, а не «решается на глаз».

При подготовке задания по конкретной игре старший аналитик обязан явно указать **«Что студенту не надо исследовать заново»**, со ссылкой на сохранённые доказательства или старшие аналитические таблицы. Гипотезы из senior-таблиц не превращаются в факты только потому, что они там уже записаны.

---

# 3. Обязательная предметная предварительная разведка

Для каждой новой игры до выдачи студенту ЧТЗ выполнить следующие исследования. Если класс данных неприменим (например, в игре нет кубиков), поставить `NOT_APPLICABLE` с основанием, а не молча исключить его.

| Направление | Что старший аналитик устанавливает заранее | Минимальный предметный результат |
|---|---|---|
| Продуктовая генеалогия | База, самостоятельные коробки, expansion, reprint, deluxe, update/replacement, promos, crowdfunding, print-and-play, fan content | `products`, `editions`, `product_relationships` и сверка составов |
| Физические компоненты | Карты, обороты, планшеты, маркеры, тайлы, жетоны, фишки, кубики/грани, справочники, численность и вариантность | Предзаполненный `component_manifest`, ожидаемое число сущностей и физических копий |
| Правила | Официальные PDF, редакции, FAQ, errata, designer/publisher rulings, reference sheets, спорные окна timing | `rules_versions`, `rulings`, `rules_conflicts`, тестовые кейсы |
| Карты и надписи | Номера, названия, цвета, типы, состав наборов, все доступные стороны и издания, канонические и переведённые тексты | `card_identities`, `card_printings`, `card_text_versions`; максимальный разумный seed |
| Ключевые символы | Значки, нестандартная типографика, плашки, конвенции значений, пиктограммы, различия между изданиями | `symbol_dictionary` и source-backed смысл каждого знака |
| Локализации | Официальные русские и другие значимые версии, издатели, сроки, терминологические расхождения, исправления, дефекты перевода | `localizations`, `entity_aliases`, `translation_issues` |
| Сообщества и история | BGG Files/Forums/Images/GeekLists, Tesera, Reddit, специальные сайты, печатные guides, архивы умерших сайтов | `source_manifest`, приоритетный topic/thread ledger |
| Цифровые реализации | Steam/TTS, VASSAL, BGA, приложения, Lackey/OCTGN, официальные цифровые игры, открытые репозитории | Реестр версий, asset URLs, состав, ограничения авторитета |
| Стратегия и мета | Публикации, обучающие материалы, обсуждения «после N партий», турниры, комбо, counters, ситуации, число игроков, эволюция взглядов | Доказательный `strategy_claims`, стартовый combo/counter graph |
| Неизвестное и трудное | Конфликт арифметики тиражей, пропавшая карта, спорный символ, неточные сканы, старые FAQ, missing pages | Адресная очередь `OPEN_*` с конкретными маршрутами проверки |
| Медиа | Ссылки на сканы, PDF с картами, видео, мастер-архивы и TTS texture sheets | Размерный inventory и `deferred_large_assets` без скачивания больших payload |

**Запрет общего повторного поиска:** если проблема уже имеет disposition с evidence trail, студент не начинает её с Google/BGG заново. Повтор разрешён только при новом прямом lead, документированном конфликте, смене версии или обоснованном истечении актуальности.

## 3.1. Выбор режима для конкретной игры

Старший аналитик дописывает один раздел `GAME_ONTOLOGY.md` (в составе предметного пакета, но не отдельный файл настоящего универсального ТЗ), который выбирает игровые оси:

- **Карточная / LCG:** identity, copies, products, expansions, factions, costs, keywords, timing, errata, deck legality, restrictions, counters, decks, archetypes.
- **Экономическая:** состояние ресурсов, конверсии, action economy, trade, production chains, market/demand, очередность, owner access, доход, scoring, игроки/форматы.
- **Драфт / engine building:** колода/пул, очередность выбора, открытая/закрытая информация, situational value, combo timing, drafting signals.
- **Кубики / символические грани:** конкретный физический die, семейство, каждая face, символ, эффект, модификации, distribution, setup-dependent probability.
- **Приключенческая / кампания:** encounters, персонажи, enemies/bosses, level/progression, variant, persistence, party, difficulty, scenario setup, campaign state.
- **Асимметричная / модульная:** фракционные/персонажные исключения, перекрывающие правила, совместимость модулей, различные game-state схемы.

Смешанная игра использует несколько моделей сразу. Не нужно искусственно сводить всё к `cards.csv`.

---

# 4. Классы источников, приоритет и степень доверия

## 4.1. Authority не равно уверенности

**Authority class** указывает, кто выпустил материал; **confidence** — насколько полно доказано конкретное утверждение. Отдельно хранить `evidence_status` и `acquisition_status`.

| `authority_class` | Описание | Условия использования |
|---|---|---|
| `OFFICIAL_RULES_PRIMARY` | Издательские правила/справочники соответствующей редакции | Приоритет внутри применимого `ruleset_id` |
| `OFFICIAL_ERRATA_PRIMARY` | Официальные поправки и replacement | Применимость определяется effective date/version |
| `OFFICIAL_PRODUCT_PRIMARY` | Издательский состав, продуктовая страница, каталог | Истина для заявленного состава, но не гарантия, что конкретная коробка идентична |
| `OFFICIAL_STAFF_RULING` | Прямой ответ подтверждённого автора/представителя | Хранить автора, дату, тему, scope, последующие изменения |
| `OFFICIAL_LOCALIZATION_PRIMARY` | Выпущенные локализатором компоненты/правила | Первичный источник **для своей печати**, не замена иностранному оригиналу |
| `OFFICIAL_HISTORICAL` | Старые издательские страницы, crowdfunding, archived news | Исторические обещания отделять от фактического retail |
| `IMPLEMENTATION_PRIMARY` | Код/поведение цифровой реализации | Доказательство поведения **реализации**, не автоматическая норма tabletop |
| `COMMUNITY_DATABASE` | BGG, фанатские базы, card indexes | Вторичный источник, полезный для cross-check |
| `COMMUNITY_RULES_AGGREGATOR` | FAQ-компиляции, тематические справочники | Нужна атрибуция исходного rulings |
| `COMMUNITY_ANALYTICAL` | Стратегические статьи, BGG/Reddit-дискуссии | Контекстные claims, не официальные факты |
| `COMMUNITY_TRANSLATION` | Неофициальные переводы | Отдельный переводческий слой |
| `FAN_CONTENT` | Фанатские сценарии, карты, варианты | Не смешивать с официальным пулом |
| `LEAD_ONLY` | Сниппет, мёртвая ссылка, вторичная ссылка на неизвестный документ | Разрешён только статус зацепки |
| `UNVERIFIED` | Непроверенное утверждение | Не включать в фактические ответы без предупреждения |

## 4.2. Confidence

| Код | Критерий |
|---|---|
| `A` | Сохранённый, корректно атрибутированный первичный документ/изображение, доказывающий именно это поле |
| `B` | Два или более **независимых по происхождению** согласованных источника |
| `C` | Один доброкачественный производный/общественный источник |
| `D` | Реконструкция по косвенным фактам, ясно перечислены предположения |
| `E` | Lead без содержательного доказательства |

Нельзя считать копию документа на трёх сайтах тремя независимыми подтверждениями. `A` не означает «применимо ко всем изданиям». Для спорных записей обязательно поле `confidence_notes`.

## 4.3. Статусы утверждения и поиска

```text
VERIFIED_PRIMARY          — проверен по подлинному применимому первичному источнику
VERIFIED_DERIVATIVE       — проверен как производный материал (с lineage)
CORROBORATED              — подтверждён независимыми источниками
PROVISIONAL               — рабочая реконструкция; требуется проверка
PARTIAL                   — часть вопроса подтверждена
OPEN_FORENSIC             — нужны конкретные дополнительные доказательства
BOUNDED_NEGATIVE          — ограниченный и протоколированный поиск не дал результата
BLOCKED_INPUT             — требуется недоступный сегодня файл, скан или owner input
NOT_APPLICABLE            — направление не имеет отношения к игре
ACCEPTED                  — запись прошла применимые QA gates
REJECTED                  — противоречие/ошибка, причиной служит отдельный issue
```

`BOUNDED_NEGATIVE` **не доказывает несуществование** объекта. Записать область поиска, варианты написания, просмотренные URL, даты, ограничение доступа, evidence, критерий остановки. `BLOCKED_INPUT` не переводить в `ACCEPTED` обещанием когда-нибудь получить файл.

---

# 5. Структура продуктового, печатного и локализационного корпуса

## 5.1. Разные идентичности

```text
product_id                       продукт / набор / expansion
  └─ edition_id                  язык, регион, издатель, тираж/выпуск
      └─ edition_component_id    конкретное включение + физическое число копий

logical_entity_id                карта / персонаж / объект / тайл / жетон / правило
  └─ printing_id                 напечатанный вариант (обороты, art, номер, текст)
      └─ text_version_id         точная версия текста / исправление / перевод
          └─ text_block_id       самостоятельная зона надписи
              └─ text_run_id     фрагмент с типографикой, значками и координатами

image_asset_id                   изображение или его представление
  ↔ printing_id / component_face_id / text_block_id

ruleset_id + game_format_id      условия применения / состав правил / пул компонентов
```

**Не считать:** `new art = new logical card`, `two identical copies = two identities`, `errata = overwrote printed text`, `translated title = new entity`.

## 5.2. Базовые продуктовые таблицы

| Таблица / PK | Обязательные поля | Главные связи |
|---|---|---|
| `products` / `product_id` | `title`, `publisher`, `first_release_date`, `product_role`, `namespace`, `official_url`, `source_ids`, `confidence` | 1:N `editions`; N:N `product_relationships` |
| `editions` / `edition_id` | `product_id`, `language`, `region`, `local_publisher`, `printing_label`, `release_date`, `sku/ean_if_known`, `ruleset_id`, `source_ids` | 1:N `edition_components` |
| `product_relationships` / `relationship_id` | `from_product_id`, `to_product_id`, `relation`, `source_ids`, `confidence` | `EXPANSION_OF`, `REPRINT_OF`, `REQUIRES`, `LOCALIZATION_OF`, `REPLACES`, `PROMO_FOR`, `CROSSOVER` |
| `component_types` / `type_id` | `name`, `faces_expected`, `is_language_dependent`, `rules_bearing` | Справочник |
| `components` / `component_id` | `component_type_id`, `logical_entity_id`, `name`, `faces`, `physical_properties`, `source_ids` | 1:N `component_faces` |
| `edition_components` / `edition_component_id` | `edition_id`, `component_id`, `printing_id`, `quantity`, `manifest_source_id`, `status` | Сверка содержимого коробок |
| `component_faces` / `face_id` | `component_id`, `side/face_index`, `text_version_id`, `image_asset_id`, `role`, `source_ids` | Лицевая/обратная/каждая грань |
| `entity_aliases` / `alias_id` | `logical_entity_id`, `language`, `alias`, `context`, `edition_id`, `source_id` | Многоязычные / исторические названия |
| `localizations` / `localization_id` | `original_entity_id`, `localized_printing_id`, `language`, `publisher`, `source_id`, `version_basis` | Локализационный crosswalk |
| `translation_issues` / `issue_id` | `printing_id`, `original_span_id`, `translated_span_id`, `issue_type`, `impact`, `evidence`, `resolution_status` | Ошибки/терминология/пропуски |
| `game_formats` / `format_id` | `ruleset_id`, `legal_products`, `card_pool`, `module_set`, `player_count_range`, `banned/replaced_entities`, `source_ids` | Основа strategy/rules QA |

**Physical conservation check:** число физических карт/жетонов в указанном издании должно совпадать с опубликованным составом либо конфликт должен быть сохранён явно. Например, `50 distinct × 2 copies` нельзя превращать в `100 distinct`. При наличии promo/replacement/blank отдельно объявлять, входит ли предмет в заявленное издателем число.

---

# 6. Точная транскрипция карт, табличек, кубиков и любых игровых надписей

## 6.1. Обязательные уровни текста

Каждый источник текста сохранять в *четырёх независимых представлениях*:

1. **Original printed (lossless):** точно видимый на печати текст с орфографией, регистром, знаками препинания, переносами, начертаниями, особенными символами и расположением.
2. **Structured rich text:** тот же текст, сегментированный по зонам и фрагментам (`runs`), с точными стилями и ссылками на символы/изображения; позволяет восстановить печатное оформление без догадок.
3. **Normalized semantic:** разметка trigger / condition / cost / target / effect / numbers / choices / timing и нормализованные значения, отдельно от фактической надписи.
4. **Effective text:** применимый к версии правил текст с учетом errata/replacement/rulings; должен храниться как отдельная версия или слой вычисления, с ссылкой на источник изменения.

`plain_text` является **дополнительным** удобным поисковым полем, но никогда единственным хранилищем печатного текста.

## 6.2. Требуемые таблицы и ограничения

| Таблица | Поля (минимум) | Контроль |
|---|---|---|
| `card_identities` | `card_id`, `canonical_name`, `entity_type`, `first_product_id`, `canonical_set_id`, `source_ids` | Не дублировать alt art и переводы как новые identity |
| `card_printings` | `printing_id`, `card_id`, `edition_id`, `set_code`, `collector_number`, `rarity/type/color/faction_if_any`, `language`, `artist`, `copyright_line`, `art_variant`, `face_count`, `source_ids`, `verification_status` | Ключ `(edition, collector_no, variant)` предметно уточнить |
| `card_text_versions` | `text_version_id`, `printing_id`, `version_kind`, `language`, `printed_raw`, `plain_text`, `effective_from`, `effective_to`, `rule_source_ids`, `replaces_text_version_id`, `status` | Для `PRINTED` нельзя незаметно менять текст |
| `card_text_blocks` | `block_id`, `text_version_id`, `block_order`, `block_kind`, `side`, `bbox_normalized`, `rotation`, `reading_order`, `source_region_id` | Название / цена / тип / способности / footer отдельно |
| `card_text_runs` | `run_id`, `block_id`, `run_order`, `literal_text`, `format_marks`, `semantic_tags`, `font_case`, `line_index`, `bbox_normalized`, `symbol_id_nullable`, `source_region_id`, `confidence`, `manual_verified` | Воссоздать последовательность и оформление |
| `symbols` | `symbol_id`, `canonical_label`, `printed_glyph`, `icon_family`, `visual_description`, `semantic_meaning`, `scope_ruleset_id`, `source_ids` | Не допускать многозначного `?` без контекста |
| `symbol_occurrences` | `occurrence_id`, `symbol_id`, `text_run_id`, `printing_id`, `face_id`, `bbox`, `orientation`, `render_variant`, `source_id` | Каждый видимый значок привязан к изображению |
| `effect_atoms` | `effect_id`, `text_version_id`, `source_span_ids`, `trigger`, `condition`, `cost`, `target`, `operation`, `amount_expression`, `duration`, `optional/mandatory`, `timing_window`, `game_state_dependencies` | Эффект обязан ссылаться на исходный текст |
| `text_comparisons` | `comparison_id`, `from_text_version_id`, `to_text_version_id`, `diff_type`, `exact_diff`, `semantic_impact`, `source_ids`, `reviewer_status` | Изменение слов vs изменение правил разделять |

`format_marks` хранить **массивом**, допускаются одновременно `BOLD` и `ITALIC`. Рекомендуемые значения:

```text
BOLD, ITALIC, BOLD_ITALIC, SMALL_CAPS, ALL_CAPS, UNDERLINE,
SUPERSCRIPT, SUBSCRIPT, OUTLINED, COLORED, INVERTED,
BOXED, STAMPED, SYMBOL, CUSTOM_FONT, RUBRIC, UNDETERMINED
```

`semantic_tags`: `KEYWORD`, `CARD_NAME`, `RESOURCE`, `COST`, `TRIGGER`, `CONDITION`, `TARGET`, `RULE_REFERENCE`, `ABILITY_NAME`, `FLAVOR`, `NUMBER`, `UNIT`, `REMINDER`, `COPYRIGHT`, `ARTIST_CREDIT`, `OTHER`. Классы `format_marks` и `semantic_tags` не взаимозаменяемы: жирный текст *может* быть keyword, но это требуется доказать; не каждый keyword напечатан жирным.

Разметка должна явно поддерживать:

- латинские/кириллические и другие письменности; диакритику, лигатуры, редкие символы;
- жирный, курсив, подчёркивание, капитель, нестандартный цвет/обводку, выворотку;
- пиктограммы с несколькими числами/деталями, повёрнутые или инвертированные изображения;
- разделители, списки, пустые строки, заголовки, колонки, рамки, подсказки и flavour text;
- значимость типографики в правилах (особенно `bold` / `italic` / капитализация);
- нелинейный `reading_order` для сложной верстки;
- переднюю/заднюю сторону, разные зоны планшета, поле жетона, грань кубика;
- OCR-сомнения, нечитаемые места, вариантные чтения (`transcription_issue`), review.

Координаты `bbox_normalized` хранить относительно полной стороны изображения как четыре числа `[x0,y0,x1,y1]` в диапазоне `0..1`; источник размеров изображения обязателен. Если точные координаты неизвестны, использовать `null` и оставить задачу на дополнительную разметку, **не выдумывать** их.

## 6.3. Соглашение о текстовой записи значков

В `printed_raw` обозначать нечитаемые как текст значки явными вставками `⟦icon:SYMBOL_ID⟧`, а не случайными emoji или произвольными словами. Конкретное начертание хранится в `symbols` и `image_assets`. В человекочитаемом рендере можно показывать SVG/PNG с `alt`, не теряя машинной ссылки.

**Пример только для демонстрации схемы; вымышленная карта, не результат исследования реальной игры:**

```json
{
  "printing_id": "EXAMPLE_PRINT_001",
  "text_version_id": "EXAMPLE_PRINT_001_PRINTED_EN",
  "block_kind": "ABILITY",
  "printed_raw": "⟦icon:EX_COST_RED⟧ Pay 2.\nDraw 1 card.",
  "runs": [
    {"order": 1, "literal_text": "", "symbol_id": "EX_COST_RED", "format_marks": ["SYMBOL"], "semantic_tags": ["COST"]},
    {"order": 2, "literal_text": " Pay ", "symbol_id": null, "format_marks": [], "semantic_tags": ["COST"]},
    {"order": 3, "literal_text": "2", "symbol_id": null, "format_marks": ["BOLD"], "semantic_tags": ["NUMBER", "COST"]},
    {"order": 4, "literal_text": ".\n", "symbol_id": null, "format_marks": [], "semantic_tags": []},
    {"order": 5, "literal_text": "Draw", "symbol_id": null, "format_marks": ["ITALIC"], "semantic_tags": ["KEYWORD"]},
    {"order": 6, "literal_text": " 1 card.", "symbol_id": null, "format_marks": [], "semantic_tags": ["EFFECT"]}
  ]
}
```

В этом примере важен алгоритм, а не стили: настоящие `BOLD`/`ITALIC` устанавливаются **только** по конкретному оттиску/изображению. Проверка `render(runs) == printed_raw` должна быть определена так, чтобы вставка `symbol_id` восстанавливалась в `⟦icon:...⟧` и сохранились `\n`.

## 6.4. OCR и двойной контроль

1. Сначала получить пригодный source image/PDF и записать `source_id + page + bbox + printing_id`.
2. Если PDF имеет оригинальный text layer — извлечь его **как кандидат**; он тоже может нарушать reading order или терять иконки.
3. OCR/vision transcription выполняется отдельной производной стадией. Оригинальный файл не изменять.
4. Сверить каждую букву, число, `+/-`, стоимость, условие, punctuation, `bold/italic`, line breaks и символ вручную или независимым вторым просмотром; ошибки записать.
5. Для главных rule-bearing значков обязательна визуальная проверка даже при идеальном OCR текста.
6. Отдельно сверить artist/credit, set icon, legal/copyright microtext, collector number.
7. Текст допускается к `ACCEPTED` только при `manual_verified=true` и доказательной привязке к **конкретной печати**. Неясное место остается `PARTIAL` с точным bbox.
8. Независимую сверку особо опасных числовых эффектов, изменений после errata и локализаций выполнять вторым проверяющим.

**Критическая ошибка:** заполнение печатного текста нормализованным эффектом из другого источника без подтверждения его точного написания на данной печати. В этом случае `normalized_effect` может быть seed, но `printed_raw` остаётся `UNKNOWN`.

---

# 7. Правила, rulings, errata, временные и формальные модели

## 7.1. Набор таблиц

| Таблица | Обязательные поля |
|---|---|
| `rules_versions` | `ruleset_id`, `product_id`, `language`, `version_label`, `internal_date`, `publication_date`, `effective_from`, `effective_to`, `source_id`, `sha256` |
| `rules_sections` | `section_id`, `ruleset_id`, `heading`, `page`, `section_order`, `source_span`, `printed_text`, `normalized_rule` |
| `rule_terms` | `term_id`, `term_original`, `term_ru`, `definition`, `scope`, `formatting_requirement`, `source_ids` |
| `rulings` | `ruling_id`, `question`, `answer`, `author`, `authority_class`, `published_at`, `source_post_id`, `rule_topic_ids`, `scope_ruleset_id`, `confidence`, `supersedes`, `superseded_by` |
| `rule_conflicts` | `conflict_id`, `claim_a_id`, `claim_b_id`, `difference`, `possible_causes`, `resolution`, `status`, `evidence_ids` |
| `rule_cases` | `case_id`, `ruleset_id`, `format_id`, `initial_state_json`, `action_sequence_json`, `expected_state_json`, `source_ids`, `status` |
| `effect_atoms` | Как в §6; связь текста и исполняемой семантики |
| `rules_overrides` | `override_id`, `base_rule_id`, `module/variant_id`, `condition`, `replacement`, `priority`, `source_id` |

Различать **printed rule**, **clarification**, **erratum**, **replacement**, **community interpretation**, **implementation behavior**. Указать, что именно является нормой для выбранной печати/партии. Если два официальных источника противоречат, сначала проверить дату, scope, языковую редакцию, product и официальную замену; при неустранимом конфликте хранить оба, не «исправлять» их арифметикой или мнением.

## 7.2. Формализация

Для каждой нетривиальной механики зафиксировать:

```text
trigger | precondition | payer | action_cost | event_sequence |
mandatory_or_optional | target | affected_objects | timing_window |
state_change | duration | precedence | player_count_scope |
format_scope | source_text_span_ids | version_source_ids
```

И составить хотя бы один позитивный и один граничный тест. Для disputed rulings особенно важны: порядок фаз, before/after, одновременные эффекты, early discard, replacement effects, незаконные альтернативы, конечное действие, лимит единиц/символов, максимумы/минимумы и неявная скрытая информация.

## 7.3. Контроль печатного и действующего текста

```text
PRINTED_V1 --errata_event--> EFFECTIVE_V2
            \--replacement_printing--> PRINTED_V2
PRINTED_LOCALIZED_RU --translation_issue--> ORIGINAL_PRINTED_V1
DIGITAL_IMPLEMENTATION --behavior_diff--> PRINTED_OR_EFFECTIVE_CONTEXT
```

У каждого перехода должен быть `event_id`, дата/редакция, source evidence, описание точной разницы, scope. Запрещено подменять printed text effective text в исходной таблице.

---

# 8. Политика скачивания, сохранения и отложенных крупных файлов

## 8.1. Жёсткие пороги **первого прохода**

| Объект | Условие отложения | Что делаем | Чего не делаем |
|---|---:|---|---|
| Скан/фото **одной карты** | `size_bytes >= 10 000 000` | Сохраняем URL, размер, разрешение из метаданных/страницы, выпуск, стороны, качество, альтернативы | Не скачиваем оригинальный тяжёлый image payload |
| PDF **со сканами карт** | `size_bytes >= 50 000 000` | Сохраняем PDF URL, страницу-источник, размер, ожидаемое число карт/страниц, доступные превью/оглавление | Не скачиваем весь PDF |
| Видео | `size_bytes >= 30 000 000` | Сохраняем страницу, ID, длительность, описание, таймкоды, chapters, captions/transcript если публично доступны без большого видео | Не скачиваем видеопоток |
| ZIP/мод/архив с большими текстурами | При существенном неизвестном общем объёме или тяжёлых вложениях | Сначала descriptor/manifest, список URL/файлов/типов и объёмов; решение о скачивании — после инвентаризации | Не тянем полный комплект TTS atlas/texture sheets/сканов вслепую |
| Обычные HTML, CSV, JSON, небольшие иллюстрации, rulebook/FAQ | Нет специального запрета по таблице выше | Сохраняем при релевантности с SHA-256 и provenance | Не объявляем *любой* PDF «PDF со сканами карт» |

**Порог относится к размеру файла**, а для отдельного card scan — к одному файлу изображения одной карты. Если общий PDF или ZIP содержит много карт, не применять лимит «10 МБ на карту» вместо общего порога для PDF/архива. Для иных крупных носителей в предразведке требуется отдельное решение с учётом общего бюджета и запрета «огромные файлы сразу не тащить».

## 8.2. Протокол проверки размера без полного скачивания

1. Из страницы-источника получить landing page, **direct asset URL**, MIME и заявленный размер (если указан).
2. Допустимы HEAD или корректно поддерживаемый сервером запрос `Range: bytes=0-0` для `Content-Length`/`Content-Range`. Не допускать автоматической полной загрузки при игнорировании Range; прерывать после безопасного лимита.
3. Проверить `Content-Encoding`, redirect chain, query, срок действия подписанной ссылки, необходимость авторизации. Не сохранять приватные токены в публичном source manifest.
4. При отсутствии достоверного размера записать `size_status=UNKNOWN`, `size_bytes=null`, `estimation_method` и диапазон при наличии обоснованного метода. Не выдавать экстраполяцию за измерение.
5. Если неизвестный размер и это потенциально крупное медиа, **отложить**; не доказывать размер полной загрузкой.
6. Если файл маленький и разрешён к сохранению — скачать, сверить фактические байты, рассчитать SHA-256; если оказался большим, прекратить/не регистрировать его как полностью приобретённый и описать частичную загрузку.
7. Для TTS workshop/save JSON инвентаризовать URL внешних asset и Deck IDs, включая раскладки и листы текстур. Сначала metadata, потом разрешённые небольшие media.
8. Для одинаковых зеркал не суммировать объём дважды, если известна одинаковая идентичность; **совпадение URL** не всегда означает совпадение файлов во времени — сохранять дату, ETag/Last-Modified и hash где доступен.

## 8.3. `deferred_large_assets` — обязательный реестр

```text
asset_id                    STRING PRIMARY KEY
asset_kind                  ENUM(CARD_SCAN, SCAN_PDF, VIDEO, TTS_TEXTURE,
                                 VASSAL_MEDIA, ARCHIVE, OTHER)
logical_entity_id           STRING NULL
printing_id                 STRING NULL
source_id                   STRING NOT NULL
landing_url                 STRING
original_direct_url         STRING NULL
archive_url                 STRING NULL
url_requires_auth           BOOLEAN
http_status                 STRING NULL
mime_type                   STRING NULL
format                      STRING NULL
size_bytes                  INT64 NULL
size_status                 ENUM(EXACT_HEADER, PUBLISHER_STATED,
                                 CONTAINER_METADATA, ESTIMATED, UNKNOWN)
size_estimate_low_bytes     INT64 NULL
size_estimate_high_bytes    INT64 NULL
size_probe_method           STRING
width_px                    INT32 NULL
height_px                   INT32 NULL
page_count                  INT32 NULL
duration_seconds            FLOAT NULL
card_faces_expected         INT32 NULL
language                    STRING NULL
edition_id                  STRING NULL
quality_note                STRING NULL
rights_status               STRING
priority                    ENUM(P0, P1, P2, P3)
value_for_kb                STRING
alternative_light_source    STRING NULL
dedup_group_id              STRING NULL
status                      ENUM(DEFERRED_SIZE, DEFERRED_UNKNOWN_SIZE,
                                 ACCESS_DENIED, METADATA_ONLY, LATER_APPROVED)
reason_not_downloaded       STRING
observed_at                 DATETIME
next_action                 STRING
```

`LATER_APPROVED` означает только отдельное разрешение на дальнейший проход, не `DOWNLOADED`. Файлы с неизвестным размером не подмешивать в точный итог байтов.

## 8.4. Финальный отчёт Heavy Media

Обязательный файл предметного проекта: `reports/HEAVY_MEDIA_DEFERRED_REPORT.md`.

Отчёт должен показывать:

- счётчики по типам файлов (`CARD_SCAN`, `SCAN_PDF`, `VIDEO`, `TTS_TEXTURE`, `ARCHIVE`);
- **измеренный** объём, **оценочный** объём и отдельно число/долю файлов **без данных о размере**;
- итоги до и после дедупликации, метод дедупликации, степень неопределённости;
- примерные размеры каждого будущего acquisition batch и необходимые носители хранения;
- покрытие наборов/изданий/сторон по доступным лёгким источникам и то, что осталось только в отложенных носителях;
- ранжирование `P0..P3` по уникальности, качеству, полноте, доказательной ценности, редкости и риску утраты;
- таблицу **конкретных прямых URL**, а не формулировку «где-то на BGG»;
- список редких, но очень тяжёлых материалов, для которых нужен отдельный санкционированный этап.

**Счёт объёма:**

```text
known_bytes = SUM(size_bytes WHERE size_status in EXACT_HEADER,
                                           PUBLISHER_STATED,
                                           CONTAINER_METADATA)
min_estimate = known_bytes + SUM(size_estimate_low_bytes for estimated only)
max_estimate = known_bytes + SUM(size_estimate_high_bytes for estimated only)
unknown_count = COUNT(size_status == UNKNOWN)
unique_estimated_total = same after dedup grouping of reliable equivalents
```

Если источники заявляют размер без прямого запроса, обозначать его как `publisher_stated`, а не как проверенный сервером. Для неизвестных размеров не ставить `0`. Отчёт отдельно предупреждает, что суммарный объём **неполон**, пока есть `UNKNOWN`.

**Шаблон таблицы Heavy Media:**

| ID | Тип | Игра/издание | URL | Размер/метод | Покрытие | Приоритет | Почему отложено | Альтернатива |
|---|---|---|---|---|---|---|---|---|
| `EXAMPLE-MEDIA-001` | CARD_SCAN | `[GAME]/[EDITION]` | `[DIRECT_URL]` | 12.3 МБ / HEAD | 1 лицевая сторона | P1 | `>=10 МБ` | небольшой preview |
| `EXAMPLE-MEDIA-002` | SCAN_PDF | `[GAME]/[EDITION]` | `[DIRECT_URL]` | неизвестно | предполагаемые N листов | P0 | `DEFERRED_UNKNOWN_SIZE` | отдельно текстовые правила |

*В этой демонстрационной таблице URL и размеры вымышленные, фактические данные появятся только в предметном исследовании.*

---
# 9. Каталог источников, сохранение и происхождение данных

## 9.1. `sources` — обязательная схема

```text
source_id                     STRING PRIMARY KEY
source_title                  STRING NOT NULL
source_family                 STRING
source_kind                   STRING      # RULEBOOK, FAQ, CARD_IMAGE, ARTICLE, ...
author                        STRING NULL
publisher                     STRING NULL
published_at                  DATE/DATETIME NULL
modified_at                   DATE/DATETIME NULL
retrieved_at                  DATETIME NOT NULL
original_public_url           STRING NULL
canonical_url                 STRING NULL
landing_url                   STRING NULL
archive_url                   STRING NULL
source_host                   STRING
content_origin                STRING
language                      STRING NULL
namespace                     STRING
ruleset_id                    STRING NULL
edition_id                    STRING NULL
authority_class               ENUM(see §4.1)
confidence                    ENUM(A, B, C, D, E)
evidence_status               ENUM(see §4.3)
acquisition_status            ENUM(DISCOVERED, DEFERRED, ACQUIRED,
                                   ACCESS_DENIED, LOST, FAILED, BLOCKED)
local_raw_path                STRING NULL
content_mime                  STRING NULL
size_bytes                    INT64 NULL
sha256                        STRING NULL
http_status                   INT NULL
capture_method                STRING
raw_preserved                 BOOLEAN
ocr_used                      BOOLEAN
data_lineage_parent_ids       ARRAY[STRING]
independent_evidence_group    STRING NULL
rights_status                 STRING
safe_for_rag                  BOOLEAN
notes                         STRING
```

Разрешается хранить зеркало первоисточника, но `source_host` и `content_origin` должны различаться: например, пользовательский PDF с копией официальных правил имеет hosting в сообществе и происхождение у издателя. При отсутствии доказанной версии нельзя выдумывать release date или авторитет.

## 9.2. Файлы, скачивания, повторные попытки

Для каждого фактически сохранённого объекта:

```text
raw_file_id
source_id
exact_path
original_filename
bytes_on_disk
sha256
retrieved_at
capture_command_or_method
mime_claimed
mime_sniffed
conversion_applied = false
security_review
```

- **Raw immutable:** сохранённый источник не перезаписывать нормализованной или очищенной версией.
- **Derived separated:** извлечение DOCX images, PDF text, OCR, thumbnail, color correction, транскрипция, граф — отдельные производные результаты, связанные с raw SHA-256.
- **Dedup:** одинаковый SHA-256 — байтовая идентичность, но обе URL/истории происхождения остаются; pHash/визуальное сходство — подсказка, а не доказательство идентичного текста/версии.
- **Logging:** записывать начало/конец, HTTP status, redirect, retries, quota/rate limiting и причину ошибок. Не молчать при недоступном URL.
- **Архивы:** сохранять member path, original filename, manifest, иногда внутренний SHA-256 каждого файла, не путать ZIP bytes с отдельными card faces.
- **HTML:** отдельно raw HTML, parsed text и сохранённые URL; для форумов — post/page ID и quote relation.
- **Файлы старых сайтов:** исходный публичный URL и archive/replay URL хранить вместе; archived wrapper не всегда равен историческому payload.

## 9.3. Линия происхождения (`data_lineage`)

```text
lineage_id
child_entity_or_asset_id
parent_entity_or_asset_id
relation              # EXTRACTED_FROM, OCR_OF, TRANSLATED_FROM,
                      # MIRROR_OF, RECONSTRUCTED_FROM, NORMALIZED_FROM,
                      # IMPLEMENTED_FROM, QUOTES, CORRECTS
method
transformation_version
reviewer
verified_at
source_ids
independent_evidence_group
```

Пример: отсканированная карта → производное выпрямленное изображение → OCR → ручная расшифровка → `card_text_runs` → `effect_atoms` → Obsidian. Все переходы прослеживаются назад до файла и URL. Семантическое преобразование не должно стирать оригинал.

## 9.4. Архивирование веб-форумов

При наличии BGG, Reddit, Tesera, Discord export или аналогичного общедоступного корпуса хранить минимум:

```text
forum_topic_id | platform | game_id | forum_category | title | topic_url
created_at | last_post_at | declared_post_count | observed_post_count
pages_seen | pages_expected | completeness_status | source_ids

post_id | topic_id | author_handle | posted_at | edited_at | page_no
body_raw_html | body_text | quote_targets[] | parent_post_id
source_id | moderation_or_missing_status
```

Счётчики сайта и количество реально доступных объектов проверять отдельно. При расхождении `44 total / 43 returned`, например, статус `COUNTER_LIST_DIVERGENCE` фиксирует **факт расхождения**, но не приписывает «удалённую запись» без доказательств.

---

# 10. Полнота карточного и компонентного корпуса

## 10.1. Conservation/reconciliation matrix

Для каждого продукта/тиража подготовить таблицу:

| `edition_id` | Тип компонентов | Expected physical | Observed physical | Distinct logical | Replacement | Promo extra | Blank | Diff | Evidence | Status |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| `[EDITION]` | Cards | `[N]` | `[N]` | `[M]` | `[R]` | `[P]` | `[B]` | `[computed]` | `[source_ids]` | `[status]` |

Если ожидаемых физических 160, а логических 115, это может быть корректно: требуется разложить на дубликаты, замены, отдельные печати и blank cards. Нельзя просто увеличить число logical identities до 160.

## 10.2. Дополнительные схемы для компонентов

| Класс | Что нельзя потерять | Рекомендуемая модель |
|---|---|---|
| Карты | Название, номер, тип, color/faction, оборот, значки, printed text, art/credits | `card_identities`, `card_printings`, `card_text_runs`, `image_assets` |
| Кубики | Конкретный die, каждая грань, ориентация, число и визуальные значки, условия броска/выбора | `dice`, `die_faces`, `face_text_versions`, `symbol_occurrences` |
| Жетоны / чипы | Front/back и их функция, quantity, совместимость, иллюстрация, версия | `components`, `component_faces`, `component_update_events` |
| Двусторонние тайлы | Тип, front/back связка, события/эффекты на каждой стороне | `tile_faces`, `setup_roles` |
| Персонажи / фракции | Собственные правила, начальная колода/набор, уникальные подсистемы, исключения | `playable_entities`, `character_modules`, `rule_overrides` |
| Сценарии / encounters | Setup, варианты выбора, противники, outcomes, награды, campaign dependencies | `scenarios`, `encounter_options`, `scenario_requirements` |
| Кампании | Persistent state, обновления, межпартийные переходы | `campaigns`, `campaign_state_elements` |
| Объекты поля | Области, значения, последовательность ходов, значки, ограничения доступа | `board_regions`, `board_states`, `rules_sections` |
| Другие справочники | Правила/способности на карточках-памятках | `reference_sheet_versions`, `text_blocks`, `ruleset_scope` |

У электронных реализаций сбор сторон и листов изображений должен точно соответствовать `DeckID`, atlas region или другому механизму адресации; карту нельзя считать верифицированной по одному названию texture sheet.

---

# 11. Стратегии, мета, комбинации и противодействия

## 11.1. Не отделять стратегию от её условий

**Универсальное поле `card_strength = 9.5` запрещено как канонический факт** без измерительной модели и контекста. Аналитика строится для `V(entity | ruleset, format, card_pool, players, phase, setup, resources, known_information, opponents, modules)`.

У каждого strategic claim должны быть:

```text
claim_id | claim_type | subject_entity_ids[] | author | date | source_id
claim_text_verbatim_or_located | claim_summary | citation_location
ruleset_id | game_format_id | player_count | phase | module_set
assumptions | prerequisites | quantification_method | evidence_class
supporting_sources[] | contradicting_sources[] | confidence
reconciliation_status | update_history
```

Возможные `claim_type`:

```text
BEGINNER_ADVICE, PIVOTAL_TURN, OPENING, DRAFT_PICK, YEAR_ALLOCATION,
BUILD_PATH, TIER, ACTION_ECONOMY, RESOURCE_CONVERSION,
CARD_EVALUATION, COMBO, COUNTER, MATCHUP, TEMPO, ENDGAME,
PLAYER_COUNT_DEPENDENCY, FORMAT_OPINION, VARIANT_ANALYSIS,
HISTORICAL_META_EVOLUTION
```

Стратегические тексты об эволюции отношения к игре после десятков/сотен/тысяч партий сохранять вместе с датой и уровнем опыта автора, **не приписывая** субъективному взгляду универсальный статус.

## 11.2. Граф отношений и hypergraph

Тривиальный граф `A ↔ B` недостаточен, если комбинация требует третьей карты, особой очередности или состояния. Хранить **две связанные структуры**:

- `graph_edges` — атомарные отношения между сущностями;
- `combo_definitions` + `combo_members` + `combo_conditions` — комбинации как гиперрёбра с контекстом.

**`graph_edges`**:

```text
edge_id | from_id | to_id | relation_type | directed | ruleset_id
format_id | condition_id | evidence_ids[] | confidence | derived_by
```

Начальные типы рёбер (предметно адаптировать):

```text
PRODUCES, CONSUMES, CONVERTS_TO, REQUIRES, ALLOWS, PROHIBITS,
TRIGGERS, ENABLES, ACCELERATES, PAYS_OFF, SCORES, TAXES,
COUNTERS, SOFT_COUNTERS, HARD_COUNTERS, DENIES, DELAYS,
REPLACES, COMPATIBLE_WITH, INCOMPATIBLE_WITH, AVAILABLE_IN,
PRINTED_AS, TRANSLATED_AS, SUPERSEDED_BY, RULED_BY, QUOTED_BY
```

**`combo_definitions`**:

```text
combo_id | title | minimal_core_entity_ids[] | optional_entity_ids[]
required_state_json | required_sequence_json | forbidden_state_json
ruleset_ids[] | format_ids[] | player_count_scope | phase_window
resource_cost | opportunity_cost | expected_payoff_model
failure_modes | fragility | counter_ids[] | evidence_ids[]
confidence | analysis_status
```

**`combo_members`**: `combo_id | entity_id | role | mandatory | sequence_order` (`ENABLER`, `PAYOFF`, `ACCELERATOR`, `RESOURCE`, `COUNTER`, `OPTIONAL`).

**`combo_conditions`**: `condition_id | combo_id | variable | operator | expected_value | source_ids`.

**`counters`**: `counter_id | target_entity_or_combo_id | kind | counter_entities[] | required_timing | tradeoff | hardness | format_id | source_ids | confidence`.

Если комбо не работает при другом количестве игроков или card pool — не удалять его: сохранить applicability. Если claim из BGG ошибается по правилам, вносить как спорную историческую точку зрения с объяснением, почему её нельзя рекомендовать как legal play.

## 11.3. Аналитические модели по жанрам

- **Деньги/производство:** ценность действия, yield, food/energy opportunity cost, стоимость доступа, stockpiles, converted resource shadow values, способы ускорения двигателей, условия окупаемости.
- **Драфт:** сила первого выбора vs late pick, pool dilution, подсмотренная информация, случайный набор карт, P1P1, намеренное отрицание карт оппоненту, подготовка года/раунда.
- **LCG/колоды:** legality по формату, основные archetypes, faction restrictions, tutor, synergy/counter, restricted/banned lists, порядок активации.
- **Кооператив:** character-party-scenario-boss matchups, сложности, варианты героев, источники gear/skill.
- **Случайные компоненты:** точное вероятностное дерево после верификации физических граней, а затем simulation с фиксированными seeds и unit tests.

Не заявлять статистику побед, если не существует реального корпуса матчей. Симуляционные оценки отдельно маркировать `MODEL_DERIVED` с перечнем assumptions, исходных состояний и доверительных интервалов при наличии.

## 11.4. Корпус учебных материалов

Искать и сохранять ссылки/малые доступные транскрипты на:

- официальные tutorials, playthrough, rules explanations;
- статьи «как начать», «10 первых ошибок», руководства по освоению;
- продвинутые стратегии и обсуждения после большого числа партий;
- карточные разборы, matchup guides, tournament reports;
- длинные дискуссии с изменением мнения авторов — как отдельный `HISTORICAL_META_EVOLUTION`;
- видеоматериалы: **индекс/таймкоды/chapters/transcripts** даже если видео больше 30 МБ и его поток отложен.

Обязателен контекст публикации и отличение реальной цитаты от реферативного пересказа. Не выдавать за просмотренное видео, у которого удалось получить только заголовок и описание.

---

# 12. Медиа, сканы, цифровые реализации и локализации

## 12.1. `image_assets`

```text
image_asset_id | logical_entity_id | printing_id | component_face_id
source_id | original_url | container_archive | archive_member_path
language | side_or_face | file_format | width_px | height_px
claimed_dpi | actual_pixel_density_if_derived | size_bytes | sha256
perceptual_hash | color_profile | alpha | crop_status | border_status
rotation | watermark | cleaned_or_edited | is_thumbnail | derived_from_id
image_rights_status | quality_rank | confidence | acquired_or_deferred
```

Файл высокого разрешения с другим текстом или исторической печатью не является дубликатом новой карты низкого разрешения. `pHash` используется для поиска похожих изображений, а **не** для слияния разных печатей. Для печати PnP/прокси при необходимости иметь отдельно физические размеры, DPI и параметры кадрирования; исходный кадр сохранять неизменным. Модель сканов **не требует** скачивания тяжёлых оригиналов в первом проходе.

## 12.2. Цифровые реализации

| Система | Что исследовать | Главное ограничение |
|---|---|---|
| Tabletop Simulator / Steam Workshop | Mod ID, дата/версия, save/descriptor JSON, Deck IDs, FaceURL/BackURL, atlas layout, script features, список asset, доступность | Не скачивать массивы texture sheets без размерной инвентаризации; скрипт не определяет издательский ruling |
| VASSAL | `.vmod` версия, список компонентов и ресурсов, origin, publisher permission | Изображения и поведение не обязательно соответствуют актуальной печати |
| BGA / приложения / Steam | Релизная хронология, реализованные modules, card pools, правила интерфейса, public user guides | Implementation ≠ нормативные tabletop правила |
| Lackey / OCTGN / сторонние репозитории | Plugin IDs, версии, card definitions, symbols, raw resources, SHA/commit | Secondary / implementation evidence; лицензии и полнота обязательны |
| Boardgame-specific fan tools | Калькуляторы, player aids, генераторы, базы карт, odds models | Верифицировать источники механики; не наследовать молча чужие ошибки |

При правомерно доступном descriptor `assets.json` хранить `referenced_urls`, expected size, deck/atlas mapping, `is_available`, HTTP status, `downloaded`, `hash_if_downloaded`, locale, component mapping. Заблокированный / удалённый workshop item допускает статус `LOST/LEAD_ONLY`, а не обещание полного corpus.

## 12.3. Локализации

- Сохранить исходный язык, оригинальное имя и *точное локализованное печатное* имя.
- Разнести официальную издательскую локализацию, неофициальный перевод и исправление локализатора.
- Сверить колоду/количество физических копий, сетовые символы, коллекторские номера, текст и layout с оригиналом.
- Не переписывать локализованный текст английским effective text; заводить `translation_issue` и `effective_localized_interpretation`, если подтверждены.
- Отдельно фиксировать утраты строк, неверную жирность/курсив, отсутствующий icon, переставленный heading, неочевидные терминологические и timing-конфликты.
- Для приоритетного издания владельца построить edition-specific acceptance queries: «что находится именно в моей коробке?».

## 12.4. Правовой и защитный режим

Сохранение источника для личного исследования **не означает** автоматическое право открыто публиковать сканы, игровое оформление, полные тексты карт или защищённые медиа. Отдельно хранить `rights_status`, `redistribution_status`, publisher/creator permission, условия использования. Не обходить paywall, auth или антибот-защиту несанкционированным методом и не массово извлекать чужие закрытые сведения.

Если используются авторизованные снимки веб-страниц, пользовательские сессионные cookies, CSRF, OAuth и Authorization headers **не должны попасть** в публичный каталог/Obsidian/RAG/отчёт. `USER_SESSION` — очищать в safe derivative, `SOURCE_CONTENT` — не повреждать, `UNKNOWN` — карантин и ручная проверка. Не хранить пароль в репозитории и логах.

---

# 13. Архитектура локальной БЗ

## 13.1. Структура каталогов

При отсутствии особого указания владельца использовать **OneDrive-папку без Git в корне БЗ**, Obsidian для заметок, Parquet как канонические таблицы, DuckDB как пересоздаваемый аналитический build artifact. Небольшие исходные и производные материалы хранятся по отдельности. Исходные Git-репозитории цифровых модов при необходимости клонировать **вне** синхронизируемого корня, в БЗ сохранять immutable revision snapshots/commit metadata.

```text
[GAME]-Arch/
├── README.md
├── PROJECT_POLICY.md
├── RIGHTS_NOTES.md
├── 00_catalog/
│   ├── sources.parquet / sources.csv
│   ├── acquisition_log.parquet
│   ├── checksums.sha256
│   ├── URL_aliases.csv
│   ├── conflicts.csv
│   ├── research_dispositions.csv
│   ├── research_leads.csv
│   └── deferred_large_assets.csv
├── 01_raw_official/       # current + historical official, small/allowed
├── 02_raw_archives/       # Wayback/mirrors, source origin preserved
├── 03_raw_community/      # BGG, Tesera, Reddit, guides, forums
├── 04_raw_localizations/  # official + unofficial separated
├── 05_raw_digital/        # TTS/VASSAL/BGA descriptors, repos/snapshots
├── 06_raw_strategy/       # guides, articles, lightweight transcript data
├── 07_images/             # acquired light assets and previews
├── 08_machine_readable/
│   ├── parquet/
│   ├── jsonl/
│   ├── schemas/
│   └── exports/
├── 09_database/           # disposable DB + build manifest
├── 10_obsidian/
│   ├── 00_MOC/
│   ├── Products/  Editions/  Cards/  Printings/  Components/
│   ├── Symbols/  Rules/  Rulings/  Combos/  Counters/
│   ├── Strategy/  Sources/  Localizations/  Digital/
│   └── Open_Questions/
├── 11_agents/             # ontology, retrieval/authority policy
├── 12_reports/
│   ├── corpus_status.md
│   ├── source_coverage.md
│   ├── cards_and_printings_coverage.md
│   ├── rules_and_rulings_coverage.md
│   ├── symbols_and_typography_coverage.md
│   ├── strategy_and_combo_coverage.md
│   ├── HEAVY_MEDIA_DEFERRED_REPORT.md
│   ├── qa_report.md
│   ├── residual_questions.md
│   └── checkpoint.md
├── 13_tools/              # reproducible scripts/config/tests
├── 99_quarantine/         # failed/ambiguous/security/rights
└── _private_acquisition/  # not published/indexed/synced if secrets present
```

Каталоги и точные имена могут уточняться под конкретную игру. Правила:

1. `raw` immutable после регистрации; изменения через derivatives.
2. Любой полученный файл имеет SHA-256, source_id и путь.
3. Markdown/Obsidian **не является** единственным источником фактов; заметки регенерируются из таблиц.
4. Manual notes, которых нет в таблицах, хранятся в отдельном устойчивом пространстве, генерация их не затирает.
5. DuckDB закрывается до синхронизации; использовать одного writer, атомарные замены файлов и резервные копии.
6. Секреты/персональные auth-профили не класть в синхронизируемые и индексируемые общие каталоги.
7. `data_dictionary.md`, схемы и связь ключей — обязательны; формат csv/parquet можно обменивать без потери типов.

## 13.2. Обязательные связи и граф

```text
SOURCE --supports--> CLAIM/RULING/TEXT_VERSION/PRINTING/IMAGE
SOURCE --derived_from--> SOURCE
PRODUCT --includes--> EDITION --includes_copy--> COMPONENT/PRINTING
ENTITY --printed_as--> PRINTING --has_text--> TEXT_VERSION
TEXT_VERSION --contains--> BLOCK --contains--> RUN --uses--> SYMBOL
PRINTING --depicted_by--> IMAGE_ASSET
RULE --superseded_by--> RULE
RULING --clarifies--> RULE/ENTITY/MECHANIC
ENTITY --member_of--> COMBO --countered_by--> COUNTER
STRATEGY_CLAIM --valid_in--> FORMAT/RULESET/PHASE/PLAYER_COUNT
TRANSLATION --corresponds_to--> PRINTING/TEXT_VERSION
DIGITAL_ASSET --represents--> COMPONENT/PRINTING
```

Вся связь N:N реализуется через link tables, не хранить огромные разделённые запятыми списки как единственный канонический тип. Для экспорта может быть `ids[]` при наличии отдельной schema-aware связи.

## 13.3. Agent/RAG retrieval policy

Агент при ответах:

1. сначала определяет игру, edition, `ruleset_id`, format, язык и временную версию;
2. ищет entity/aliases, печати и source-backed claims;
3. сортирует по **применимости и authority**, а не только по свежести или популярности;
4. различает `PRINTED`, `EFFECTIVE`, `COMMUNITY`, `IMPLEMENTATION`;
5. в спорном случае выводит разные формулировки и статус конфликта;
6. даёт ссылку на source, raw path, страницу/пост/region, confidence;
7. явно говорит `UNKNOWN/NOT_VERIFIED`, если отсутствует доказательство;
8. не пересказывает непроверенную стратегию как факт и не выдумывает отсутствующий текст/числа.

---

# 14. Work Packages: исполняемая инструкция для первокурсника

Каждый WP получает уникальный ID, owner, priority, status, **входные файлы**, детальные шаги, команду/инструмент (если технический), выходные файлы, validation script/check и acceptance. Если студент не программист, ему даются готовые скрипты/примеры вывода; не требуется самостоятельно придумывать SQL, регулярки или импортеры.

## 14.1. Рекомендуемая очередь работ

| WP | Приоритет | Предусловие | Действия студента | Обязательный выход | Приёмка |
|---|---|---|---|---|---|
| `WP00` Bootstrap | P0 | Папка, предметное ЧТЗ | Создать структуру БЗ, README, схемы, шаблон логов, убедиться в правах и путях | `PROJECT_POLICY`, `data_dictionary`, `status` | Структура соответствует манифесту, пути валидны |
| `WP01` Security | P0 | WP00 | Убрать user credentials из safe exports, оставить источник целым, карантин сомнительного | `security_selftest.md`, журнал cleanup | Секреты не попадают в Obsidian/exports |
| `WP02` Source imports | P0 | Senior source seeds | Загрузить/проверить разрешённые небольшие официальные sources, записать redirects/hash/status | `sources`, `acquisition_log`, `checksums` | Каждый seed обработан; ни один не исчез без статуса |
| `WP03` Versions/products | P0 | WP02 | Привести продукты, издания, локализации, замены к IDs и relations | `products`, `editions`, `relationships` | Состав согласован; различия печатей сохранены |
| `WP04` Component reconciliation | P0 | WP03 | Сопоставить expected/observed copies и стороны; зафиксировать расхождения | `components`, `edition_components`, matrix | Все known counts объяснены либо `OPEN` |
| `WP05` Card canonicalization | P0 | WP02–04 | Дозаполнить логические карты, номера, языки и печати по seed | `card_identities`, `card_printings` | Нет дублей alt art, обязательные FK/numbering |
| `WP06` Rich text | P0 | WP05, малые изображения/PDF | Разбить текст на блоки/runs, начертания, значки, layout; визуально сверить | `card_text_versions`, `blocks`, `runs`, `symbols` | 100% принятых печатей выдерживают fidelity-gates |
| `WP07` Rules/rulings | P0 | WP02,05–06 | Версионировать rules/FAQ, разметить rule claims и ответственные authority | `rules_*`, `rulings`, `conflicts` | Нет overwriting printed, ссылки до raw |
| `WP08` Symbols/faces | P0 | WP04,06 | Проверить каждый set icon, glyph, die face, front/back, ориентацию | `symbol_occurrences`, `component_faces`, `die_faces` | Непрочитанные face/runes отмечены явно |
| `WP09` Localizations | P1 | WP05–08 | Связать exact оригинальные и локальные печати, сверить отличия | `entity_aliases`, `translation_issues` | Нет подмены и необъяснённых ключевых разночтений |
| `WP10` Community corpus | P1 | WP02 | Зафиксировать BGG/Tesera topics/files, скачать разрешённое/сохранить недоступное | `threads`, `posts`, source inventory | Все целевые P0/P1 темы имеют статус |
| `WP11` Strategy claims | P1 | WP07,10 | Размечать статьи и треды по тезисам, player count, format, evidence | `strategy_claims` | Нет контекстно голых tier scores |
| `WP12` Combo/counter | P1 | WP06–07,11 | Нормализовать связи и комбо; указать ограничения/контрпримеры | `graph_edges`, `combo_definitions`, `counters` | Каждая комбинация валидна в заданном контексте |
| `WP13` Digital implementations | P1 | WP02–05 | Зарегистрировать релизы, manifests, small descriptors, maps; тяжелые textures отложить | `digital_versions`, `digital_assets`, `deferred_large_assets` | Нет ложного authoritative layer и слепой загрузки |
| `WP14` Heavy media inventory | P0 | WP02 и все workstreams | Отложить файлы по размеру, сохранить URLs и size method, dedup/оценить volume | `deferred_large_assets`, Heavy Media report | Все target media classified; три порога соблюдены |
| `WP15` DB/Obsidian | P1 | WP03–14 | Сгенерировать Parquet/DuckDB/MOC/note links, search index | БЗ, индексы, build log | Регистрация работает и ссылки разрешаются |
| `WP16` QA/rules test cases | P0 | WP05–15 | Выполнить схемные, числовые, типографические и контекстные тесты | `qa_report`, issues, fixture results | Все blocking checks PASS либо documented blocker |
| `WP17` Reports/checkpoint | P0 | WP16 | Подготовить сверку источников, остаточные вопросы, что senior уже закрыл, handoff | Итоговые отчёты и checkpoint | Проверяемая стадия, без ложного COMPLETE |

**Принцип приоритета:** в предметном ТЗ старший аналитик заменяет/добавляет WP по механике игры, но оставляет обязательные классы: sources, versions, text fidelity, rules, strategy, deferred media, QA и handoff.

## 14.2. Шаблон одного WP — использовать без изменений структуры

```yaml
wp_id: WPXX
name: "[Название]"
priority: P0
owner_role: JUNIOR
scope: "[Продукты, версии, языки, номера]"
preconditions:
  - "[Названия seed-файлов и уже выполненных WP]"
inputs:
  - "[Exact path / source IDs, а не 'найдите сами']"
known_truths_not_to_rediscover:
  - "[Конкретные доказанные положения и их source IDs]"
procedure:
  - step: 1
    action: "[Одна наблюдаемая операция]"
    method: "[Готовый скрипт/кнопки/формат]"
  - step: 2
    action: "[Проверка результата операции 1]"
expected_outputs:
  - "[Пути/таблицы/названия колонок]"
qa_checks:
  - "[Точный автоматический тест или ручная процедура]"
acceptance:
  - "[Условие, допускающее PASS/FAIL без трактовки]"
failure_handling:
  - "[Где фиксировать 403, 404, спорную печать, OCR ambiguity]"
escalation:
  - "[Какой вопрос вернуть senior при конфликте]"
stop_conditions:
  - "[Ограничение повторного поиска]"
```

## 14.3. Что делать студенту при типовых проблемах

| Ситуация | Правильное действие | Нельзя |
|---|---|---|
| PDF не открывается или сайт 403 | Записать URL, статус, дату, проверить разрешённый прямой/архивный маршрут, передать `BLOCKED` | Писать «этого PDF не существует» |
| OCR не читает слово | Указать страницу, bbox, кандидаты и confidence; отправить на визуальную сверку | Придумывать подходящее по смыслу слово |
| На двух картах один номер | Проверить set/edition/printing/side/version, открыть конфликт | Перезаписывать запись новым вариантом |
| Wiki противоречит официальным правилам | Сохранить оба statement, указать authority и scope | Усреднять и выдавать компромиссную «редакцию» |
| BGG counter говорит 44, получено 43 | Протоколировать разные наблюдения, проверить точные маршруты с stop rule | Дополнять вымышленным 44-м тредом |
| Недоступен большой архив | Сохранить descriptor/URL/размерный estimate и причины deferred | Запускать массовую загрузку наудачу |
| Два источника повторяют один FAQ | Отметить `MIRROR_OF`/общий origin | Считать это независимым двойным подтверждением |
| Вторая печать меняет типографику | Создать printing/text diff, оценить семантическое влияние | Подменять `BOLD`/`ITALIC` старой печати новой |
| Источник стёрся | Сохранить dead-link ledger, архивные зацепки, bounded negative | Выдавать поиск за полную реконструкцию |

---

# 15. Обязательные шаблоны записей

Примеры ниже — **структура**, не факт об исследуемой игре. Пустые значения не заполнять домыслами.

## 15.1. Запись источника (`sources.csv` / JSONL)

```yaml
source_id: SRC-0001
title: "[Исходный заголовок]"
authority_class: OFFICIAL_RULES_PRIMARY
content_origin: "[Издатель]"
source_host: "[Домен, где найден]"
original_public_url: "[Публичный адрес]"
archive_url: null
published_at: null
retrieved_at: "[ISO-8601 с timezone]"
language: "en"
local_raw_path: "01_raw_official/[file]"
size_bytes: null
sha256: null           # ставить только после сохранения точных bytes
acquisition_status: DISCOVERED
confidence: E
rights_status: UNKNOWN
lineage_parent_ids: []
notes: "[Предметная роль документа]"
```

## 15.2. Карточная запись с печатью и проверкой

```yaml
card_id: "[Stable ID]"
canonical_name: "[Original logical title]"
printings:
  - printing_id: "[Stable printing ID]"
    edition_id: "[Product edition]"
    language: "en"
    collector_number: "[literal exactly]"
    set_symbol_ids: []
    image_asset_ids: []
    printed_title: "[as printed]"
    printed_text_version_id: "[id]"
    effective_text_version_id: null
    art_variant: "[identifier or null]"
    source_ids: []
    transcription_status: PARTIAL
    typography_verified: false
    verification_notes: "[What remains missing]"
```

## 15.3. Символ

```yaml
symbol_id: "[stable glyph id]"
printed_glyph: null           # Unicode только если действительно соответствует
visual_description: "[shape, fill, strokes, orientation, microletters]"
icon_family: "[resource/faction/phase/set/other]"
semantic_meaning: "[only verified meaning]"
ruleset_id: "[scope]"
variants:
  - "[asset id / change reason / printing]"
source_ids: []
manual_verified: false
```

## 15.4. Ruling / конфликт

```yaml
ruling_id: "R-0001"
question: "[Точное правило, которое требуется объяснить]"
answer: null
authority_class: UNVERIFIED
ruleset_id: "[exact version]"
format_id: "[if applicable]"
source_ids: []
source_location: "[page or post ID]"
printed_rule_ids: []
supersedes: []
superseded_by: []
confidence: E
status: OPEN_FORENSIC
escalation: "[What source would settle it]"
```

## 15.5. Стратегический claim

```yaml
claim_id: "STR-0001"
claim_type: COMBO
claim_summary: "[Описать тезис, не выдавая за общую истину]"
author: "[source author]"
published_at: null
source_id: "[id]"
source_location: "[thread/post/section/timestamp]"
entity_ids: []
format_id: null
player_count: null
phase: null
assumptions: []
supporting_evidence_ids: []
contradicting_evidence_ids: []
confidence: E
status: LEAD_ONLY
```

## 15.6. Обсидиан-заметка (регулируемый generated view)

```markdown
---
id: "[logical_entity_id]"
type: card
namespace: "[official / promo / fan / localized]"
printing_ids: []
ruleset_ids: []
source_ids: []
confidence: "[A-E]"
---

# [Имя карты]

## Идентичность и издания
[Стабильный ID; товары; варианты искусства; языки; копии]

## Дословный печатный текст
[Структурированный рендер конкретной printing, не normalized paraphrase]

## Effective / errata / rulings
[Версии и доказательства с точными ссылками]

## Механики и эффекты
[Ключевые triggers/conditions/targets, links на исходные spans]

## Связанные комбинации и counters
[Контекстные claims, не универсальная сила]

## Источники и неопределённость
[Raw path/URL, страницы, статус, нерешённые проблемы]
```

## 15.7. Протокол отрицательного результата

```yaml
question_id: "RQ-0001"
object: "[What was looked for]"
status: BOUNDED_NEGATIVE
search_window: "[dates]"
checked_sources: []
exact_queries: []
archive_routes: []
methods: []
observed_results: []
unchecked_or_inaccessible: []
stop_reason: "[Scope exhausted / no new lead]"
new_lead_trigger: "[What would justify revisiting]"
conclusion: "Не обнаружено в ограниченном поиске; не утверждать несуществование."
```

---

# 16. QA: автоматические и ручные проверки

## 16.1. Машинные инварианты

1. Primary keys уникальны и не пусты; внешние ссылки разрешаются, `UNKNOWN` не маскируется выдуманным ID.
2. Для записей `ACQUIRED`, если raw действительно сохранён, существует файл и совпадает SHA-256/размер.
3. Каждая `PRINTED` текстовая запись относится к конкретной печати, каждая печать — к сущности и изданию.
4. Каждый принятый `text_run` имеет порядок, принадлежит блоку, и полный рендер возвращает `printed_raw` без потери символов/переносов.
5. `BOLD/ITALIC` не восстанавливаются из смысловых предположений; для `ACCEPTED` `manual_verified=true`, `source_region_id` или источниковая страница подтверждена.
6. `symbol_occurrences.symbol_id` существует в словаре; каждый непрочитанный знак имеет issue, а не случайную замену emoji.
7. Каждый `effect_atom` ссылается на реальные `source_span_ids` и текстовую версию.
8. `PRINTED` не изменяется errata; `EFFECTIVE` имеет исходное событие изменения с датой/scope.
9. Конфликты тиражей и published/observed counts не прячутся: conservation matrix даёт ноль по закрытым строкам либо ссылку на конкретную issue.
10. Claim `community` и tier нельзя экспортировать как official fact; у него есть источник и контекст формата.
11. У каждого combo/hyperedge валидные member IDs, states, applicability, evidence; нет несуществующих карт и условий.
12. Большие объекты размера `>=` порогов помечены deferred и отсутствуют среди автоматически скачанных heavy media первого прохода.
13. Если `size_status=UNKNOWN`, размер не равно `0` и не включается в сумму точных измерений.
14. Финальные ссылки Obsidian/source notes корректны, пропавшие raw файлы подсвечены.
15. `ACCEPTED` записи не содержат критических unresolved fields для соответствующего gate.

## 16.2. Примеры SQL-проверок (адаптировать к фактическим именам колонок)

```sql
-- 1. Неожиданные дубли печатей в рамках edition/number/variant:
SELECT edition_id, collector_number, COALESCE(art_variant, '') AS variant,
       COUNT(*) AS n
FROM card_printings
GROUP BY 1, 2, 3
HAVING COUNT(*) > 1;

-- 2. Каждая печать с accepted printed text должна иметь source:
SELECT t.text_version_id
FROM card_text_versions AS t
JOIN card_printings AS p ON t.printing_id = p.printing_id
WHERE t.version_kind = 'PRINTED'
  AND t.status = 'ACCEPTED'
  AND (t.printed_raw IS NULL OR p.source_ids IS NULL);

-- 3. Нет ли text runs со ссылкой на отсутствующий symbol:
SELECT r.run_id, r.symbol_id
FROM card_text_runs AS r
LEFT JOIN symbols AS s ON r.symbol_id = s.symbol_id
WHERE r.symbol_id IS NOT NULL AND s.symbol_id IS NULL;

-- 4. Размерный порог: скан карты 10 MB+ не должен быть acquired в проходе 1:
SELECT asset_id, size_bytes, status
FROM deferred_large_assets
WHERE asset_kind = 'CARD_SCAN'
  AND size_bytes >= 10000000 AND status NOT IN
      ('DEFERRED_SIZE', 'ACCESS_DENIED', 'METADATA_ONLY', 'LATER_APPROVED');

-- 5. Подозрительные стратегические записи без контекста:
SELECT claim_id
FROM strategy_claims
WHERE claim_type IN ('TIER', 'PICK_PRIORITY', 'MATCHUP')
  AND (source_id IS NULL OR format_id IS NULL);
```

Для разных игр допустимо `format_id=NULL` у аналитической публикации, если контекст действительно не назван; тогда запись **не проходит** строгий gate для контекстно применимых рекомендаций, а помечается `CONTEXT_UNKNOWN` — не надо придумывать формат только ради прохождения теста.

SQL-примеры — шаблон; запускать только после подгонки имён схем к данным предметной игры. Для проверки `render(runs)==printed_raw` нужна отдельная программа или тест, поскольку SQL без функции рендера не подтверждает fidelity.

## 16.3. Обязательная выборочная независимая сверка

Старший ревьюер повторно проверяет **100%**:

- конфликтных/replacement/errata текстов, перевода с игровым эффектом;
- нетривиальных cost/timing/target/number и эффектов с `BOLD/ITALIC`-значением;
- редких set/faction/symbol signs, у которых разночтение меняет механику;
- тех записей, на которых строится критическая стратегия, комбо или ответ о legality;
- мест, где OCR дал низкую уверенность либо art скрывает glyph.

Для большого остального корпуса предметный ЧТЗ фиксирует случайную/стратифицированную выборку с размером и seed генератора. Ошибка в выборке вызывает расширение проверки группы с похожим источником/типом оформления. `ACCEPTED` не означает «мы визуально проверили только три любые карты».

## 16.4. Acceptance gates

| Gate | Условие PASS | Причина FAIL/OPEN |
|---|---|---|
| `G0_SCOPE` | Описаны base + дополнения + издания + явные границы, для всех категорий есть status | Непонятен фактический corpus |
| `G1_SOURCES` | У каждого high-priority seed имеются URL/source_id и acquisition/deferred/blocked result | Missing primary without explanation |
| `G2_PRODUCTS` | Закрыта арифметика составов или сохранён полный documented conflict | Missing card or duplicate identity without disposition |
| `G3_PRINTINGS` | Принятые карты связаны с правильными physical printings и странами/языками | Неразличимы historical/effective |
| `G4_TEXT_FIDELITY` | Проверенные исходные тексты и оформление восстановимы; icons mapped | Потеря bold/italic/symbol/line breaks |
| `G5_RULES` | Правила версионированы, critical rulings снабжены authority, cases проходят | Непроверенное правило выдаётся за официальный ruling |
| `G6_STRATEGY` | Комбо и стратегические тезисы контекстны и имеют evidence/counters | Tier list без формата и происхождения |
| `G7_MEDIA_POLICY` | Все выявленные большие assets deferred, есть размеры/диапазоны/UNKNOWN и суммарный отчёт | Слепая загрузка, неполный инвентарь |
| `G8_STORAGE` | Raw/derived разнесены, hash/DB/Obsidian/links работают | Broken provenance, потеря original |
| `G9_HANDOFF` | Есть checkpoint, логи, unresolved и точные следующие шаги | Нельзя возобновить без устных объяснений |

Итоговый статус проекта не может быть `FULLY_ACCEPTED`, если какой-либо применимый блокирующий gate имеет `FAIL/OPEN`. Допускается `ACCEPTED_WITH_DOCUMENTED_EXCEPTIONS`, если ответственный ревьюер **явно** утвердил ограниченный scope и перечень unresolved, а не если студент просто исключил трудные записи.

---

# 17. Приёмочные вопросы: БЗ обязана отвечать с доказательствами

Для конкретной игры senior подставляет реальные сущности и источники в следующие классы вопросов; IDs вопросов стабильно сохраняются:

| ID | Проверочный запрос | Ожидаемое содержание |
|---|---|---|
| `AQ01` | Какие официальные продукты/дополнения существуют и чем различаются? | Product tree, edition, time, source |
| `AQ02` | Что точно входит в выбранную коробку/локализацию? | Physical counts, copy count, cards, printed backs, sources |
| `AQ03` | Сколько логических карт и сколько физических копий? | Conservation matrix, alt art/replacement exclusions |
| `AQ04` | Где печаталась выбранная карта и какие её версии? | All printings, titles, art, set/no., dates |
| `AQ05` | Что **точно** написано на карте в конкретной печати? | Rich formatted text: bold/italic/symbols/line breaks, image/page provenance |
| `AQ06` | Что изменилось в errata и применяется ли к моему тиражу? | Printed/effective diff, scope, authority |
| `AQ07` | Почему одно и то же правило трактуют по-разному? | Rule text, FAQ, staff answers, chronological conflicts |
| `AQ08` | Какие последствия имеет конкретный символ/знак? | Source-backed symbol semantics and occurrence links |
| `AQ09` | Чем английский текст отличается от русской локализации? | Crosswalk, rich text diff, translation issue |
| `AQ10` | Какие игровые эффекты / действия существуют и где legal timing? | Trigger/condition/target/effect formalization and cases |
| `AQ11` | Как работает указанное комбо в указанном формате и сколько ему нужно действий? | Hypergraph, requirements, payoff, cost, fragility, source |
| `AQ12` | Что мешает этому комбо и при каком числе игроков? | Counters, timing, player count and format context |
| `AQ13` | Что советуют новичку и в чём расходятся эксперты? | Attributed beginner guides, claims, contradictory evidence |
| `AQ14` | Как меняются стратегии после разных тиражей/дополнений? | Historical meta, format shifts, source dates |
| `AQ15` | Что в BGA/Steam/TTS отличается от настольных правил? | Implementation version/scope and ruling context |
| `AQ16` | Есть ли доказательство существования потерянного promo/FAQ? | Raw/archive path or honest bounded-negative status |
| `AQ17` | Какие изображения доступны в приемлемом размере, и какие heavy files отложены? | Source/asset manifest, quality, bytes and estimates |
| `AQ18` | Какой объём потребуется для полной загрузки отложенных сканов/видео? | Per-type/unique totals and unknown count; no fake precision |
| `AQ19` | Откуда взято конкретное утверждение и можно ли проверить оригинал? | Chain entity → source → raw → URL/date/hash/authority/confidence |
| `AQ20` | Какие вопросы остаются открытыми и почему? | Gap/disposition ledger, bounded negative, blocker and next action |

Отдельные вопросы по конкретной игре обязательны: для экономической — price/action calculations; для драфта — pool-dependent pick; для кубиков — face-level probability; для LCG — deck legality; для кампании — compatibility/character/environment/variant. Точные ожидаемые ответы в предметном ЧТЗ должны содержать числа или ссылки **только** после подтверждённого исследования.

---

# 18. Отчётность, статусы, checkpoint и передача

## 18.1. Статусный отчёт

Каждый завершённый сеанс работы должен оставлять проверяемый `WORK_REPORT_YYYY-MM-DD.md`:

```text
Дата / версия проекта / состав исследованных изданий
Выполненные WP и их gates
Новое подтверждено: [ID, значение, evidence path]
Новые / исправленные записи и количество по таблицам
Какие URL/файлы сохранены: count, bytes, sha256 manifest
Какие URL не доступны и почему
Ошибки OCR / typography / symbols и исправления
Новые rule conflicts / strategy contradictions
Изменение accepted / provisional / blocked coverage
Deferred Large Media: новые asset IDs и объём
Остаточные вопросы: ID / root cause / конкретный next step
Следующая очередь WP, входные данные и критерий завершения
```

Статусы `IN_PROGRESS`, `PARTIAL`, `BOUNDED_NEGATIVE`, `BLOCKED_INPUT` показывать предметно; нельзя маскировать сложный пробел словами «почти всё готово».

## 18.2. Исследовательская disposition matrix

| RQ ID | Вопрос | Что проверено | Evidence IDs/paths | Статус | Что **не повторять** | Оставшаяся проверка / стоп-условие |
|---|---|---|---|---|---|---|
| `RQ-001` | `[вопрос]` | `[факт или отсутствие]` | `[source IDs]` | `[VERIFIED/PARTIAL/...]` | `[поиск уже выполнен]` | `[конкретный следующий шаг]` |

Для сложного вопроса сохранять отдельные атомарные subclaims: один аспект может быть `VERIFIED`, а другой `OPEN`. Закрывать целый GAP только если все входящие условия закрыты.

## 18.3. Накопительный checkpoint

При передаче между ревизиями или аналитиками:

```yaml
checkpoint_schema_version: "1.0"
game_slug: "[game]"
revision: "R[n]"
created_at: "[ISO-8601]"
source_manifest_path: "00_catalog/sources.parquet"
checksum_manifest_path: "00_catalog/checksums.sha256"
completed_work_packages: []
partial_work_packages: []
blocked_work_packages: []
accepted_entity_counts: {}
provisional_entity_counts: {}
open_conflict_ids: []
source_acquisition_stats: {}
heavy_media_stats:
  deferred_count: 0
  known_bytes: 0
  estimated_min_bytes: null
  estimated_max_bytes: null
  unknown_size_count: 0
next_steps:
  - "[P0 first next action]"
inputs_needed_from_owner: []
things_junior_must_not_rediscover: []
qa_result: "[PASS/PARTIAL/FAIL]"
```

Каждый checkpoint — **точка возобновления**, а не краткий эмоциональный итог. `R[n+1]` должен знать, что сделано, где байты и логи, чем подтверждены решения и какие задачи нельзя повторять.

## 18.4. Передача студенту — минимальный состав предметного пакета

Хотя универсальное мастер-ТЗ находится **в одном файле**, выполненное исследование конкретной игры обычно должно экспортировать **проверяемые данные**:

- предметный `MASTER_TZ_[GAME]_RESEARCHED.md`;
- `START_HERE.md` с 5–10 первыми действиями и объяснением «что уже сделано старшим»;
- `source_manifest.csv` + source notes и конкретные URL;
- `products/editions/components/cards` seed CSV/Parquet, schema/data dictionary;
- правила/rulings, стратегия, combos/counters, graph edges и реестры конфликтов;
- `deferred_large_assets.csv` + `HEAVY_MEDIA_DEFERRED_REPORT.md`;
- acceptance queries/gates, README для agent, текущий checkpoint;
- небольшие raw-файлы, если они уже реально получены, с SHA-256 и допустимым режимом хранения.

**Не требовать** скачивания крупных media ради формирования этого пакета. Сохранить точные URL и отчёт об оценочном объёме достаточно для первого прохода.

---

# 19. Стандарт качества и требования к старшему аналитику

Предметное ТЗ должно быть содержательным, а не преимущественно методическим. Перед выдачей первокурснику старший аналитик обязан:

1. **Провести адресную проверку источников** по официальным документам, BGG/Tesera/архивам, цифровым версиям и ключевым стратегиям.
2. **Предзаполнить** столько реестров, сколько реально позволяют доступные сведения, особенно products, editions, cards, sources, rules and high-value combos. Пустой шаблон без исследованных данных не считается полным предметным ЧТЗ.
3. **Разобрать конфликты сам** там, где доказательства доступны: арифметика карточных наборов, вопросы новых карт vs replacements, различия печатного и effective text, переводческие дефекты, forum counters, старые правила.
4. **Не производить видимость проверки:** source discovered ≠ bytes acquired; reviewed image ≠ OCR completed; article metadata ≠ article body read; caption missing ≠ video watched; exact size unknown ≠ zero bytes.
5. Внести точные **URL, названия файлов, ID тредов/страниц/Workshop items**, известные даты, размеры, прямые архивные маршруты и методы проверки.
6. Указать **схему и типы** каждой новой предметной таблицы, идентификаторы, связи, примеры строк и правила обновления.
7. Разобрать **символы, типографику, language-specific terms** на конкретных материалах; богатый текст не сводить к переводам или `normalized_effect`.
8. Создать seed combo/counter graph и starter strategy claims с исходными ссылками, не только обещать будущую аналитику.
9. Для незакрытого пункта привести **не общую фразу**, а воспроизводимую форензическую очередь: что искали, где, что обнаружено, какой файл нужен, как он закроет вопрос и когда поиск надо остановить.
10. Перед выпуском выполнить QA собственного handoff: ни одна существенная таблица не пустая без объяснения, все упомянутые файлы доступны, все source IDs разрешаются, отсутствуют вымышленные hashes и скачанные assets, большие файлы не попали в первый проход.

**Принцип границы ответственности:** если старший аналитик может самостоятельно найти, прочитать, сравнить, подсчитать или формализовать открытое доказательство, он делает это **до** выдачи студенту ТЗ. Студент обслуживает доказательный pipeline и выполняет ограниченную сверку; не должен заново проделывать экспертный discovery.

---

# 20. Справочник типовых ошибок, которые предотвращает стандарт

| Ошибка | Последствие | Защита |
|---|---|---|
| Нормализованный перевод принят за оригинальный текст | Потеря printed fidelity и неверная локализация | Отдельные `PRINTED` / `NORMALIZED` / `EFFECTIVE` |
| Игнорирование жирного/курсивного/пиктограммы | Меняется юридически значимый эффект карты | `card_text_runs`, `symbol_occurrences`, visual gate |
| Слияние альт-арта с новой логической картой | Неверный размер card pool | `identity != printing != copy` |
| Размытие версий правил | Старые печати получают новые ограничения без основания | Temporal rules/rulings graph |
| Использование TTS как официального reference | Цифровая ошибка превращается в «правило» | Authority classes + implementation diff |
| Слепое чтение чужой wiki как authoritative | Производная ошибка наследуется БЗ | `data_lineage`, independent evidence groups |
| «Карточный реестр = все карточки» при наличии замен/blank | Неверный физический состав | Conservation matrix, replacement/promo role |
| Tier list без player count/pool | Вредные универсальные рекомендации | Contextual strategy claims |
| Два сайта с одним PDF считаются независимыми | Искусственно высокий confidence | Content origin + mirror relations |
| Скачивание ZIP/TTS с гигабайтами текстур | Перегрузка OneDrive, архив трудно аудировать | Deferred manifest + per-class thresholds |
| Непроверенное количество «не найдено» | Ложная полнота или фиктивная пропажа | Bounded negative, declared-vs-observed counts |
| Граф рёбер без условий | Неработающие комбо и советы | Hyperedges + explicit state/timing |
| Один сырой текст в Obsidian без таблиц | Невозможно надёжно сравнить печати и правила | Canonical Parquet + regenerative views |
| Создание hash из ссылки вместо bytes | Неверная доказательная цепочка | SHA only after successful byte capture |

---

# 21. Формат команды на новое исследование

После команды владельца вида:

```text
Проведи исследование по [GAME], включая [EXPANSIONS] и [LOCALIZATION].
```

старший аналитик **не просит вновь пересказывать настоящее ТЗ**, а:

1. определяет scope, издателя, дату и существенные версии/расширения;
2. применяет правила §§3–13 и подбирает игровую онтологию;
3. выполняет discovery, retrieval и самостоятельную проверку;
4. строит verified baseline, source manifest, canonical counts, tables и graph seeds;
5. помечает тяжёлые носители по §8 без скачивания выше порогов;
6. формирует адресные WP, residual questions, QA и acceptance по §§14–18;
7. выдаёт **предметное мастер-ТЗ и проверяемые лёгкие доказательства**; позволяет первокурснику начать работу без устной передачи знаний.

Если заказчик предпочитает одиночный выходной файл, допускается единый **игровой master `.md`**, в котором схемы, ссылки, маленькие таблицы и примеры присутствуют inline; при больших объёмах фактические CSV/Parquet следует предоставлять отдельно, поскольку Markdown-документ не заменяет машину данных. Настоящее ТЗ задаёт правила, а не сообщает, будто специфическое исследование уже выполнено.

---

# 22. Основание стандарта и отличие от исходных образцов

Стандарт составлен по предоставленным заказчиком исследовательским материалам (источники **не переисследовались в сети** при создании именно этого обобщающего документа):

| Пример | Включённая практика |
|---|---|
| `MASTER_TZ_SEASONS_LIBELLUD_KB_v1_2_RESEARCHED.md` | Исторические печати и эффективный текст, authority/lineage, format-aware strategy, combo hypergraph, Obsidian/Parquet/DuckDB, acceptance queries |
| `MASTER_TZ_TOO_MANY_BONES_KB_v2_EXECUTABLE_RESEARCHED(1).md` | Предметная онтология компонентов/граней, temporal FAQ, игровые модули, подробные WP и gates, цифровые реализации, legal/security policy |
| `LE_HAVRE_KB_ANALYST_HANDOFF_v1_1.zip` | Product manifests, локализационные и визуальные сверки, реконструкция карточных наборов |
| `LE_HAVRE_EXPERT_ANALYST_HANDOFF_v1_2.zip` | Сильный экспертный handoff: предзаполненные 115 canonical building identities, CSV/XLSX, rules findings, graph/GraphML, DuckDB starter, strategy corpus; задачи, которые студент **не** должен исследовать заново |
| `RUNE_AGE_SENIOR_CLOSEOUT_ASSIST_2026-10-06(1).md` | GAP ledger, честные `PARTIAL / BOUNDED_NEGATIVE / BLOCKED_INPUT`, точные поисковые маршруты, stop rules, запрет ложной приёмки |

**Новые обязательные требования, добавленные в этот единый нормативный стандарт:**

- полноценная **lossless rich-text** модель `card_text_runs`, `symbol_occurrences`, координатных зон и независимых типографических отметок;
- явная таблица **heavy-media порогов** `10/50/30 МБ`, метаданные вместо больших загрузок и оценка совокупного будущего трафика;
- одинаковый набор минимальных QA-gates для типографики, числовых составов, rulings, стратегий и восстановления доказательного пути;
- единый WP/negative result/checkpoint handoff для студента-первокурсника;
- специальное требование, чтобы **старший аналитик закрывал доступные сложные вопросы самостоятельно**, а не выдавал студенту только направления поиска.

---

# 23. Definition of Done данного универсального ТЗ

Этот **универсальный** документ считается готовым к применению, если он содержит: роли и порядок расследования, реестр исследовательских направлений, source/authority/confidence statuses, product/edition/printing/identity модели, lossless текст/символы/разметку, printed/effective rules, формальные rulings, стратегические claims и combo/counter hypergraph, ограничения по правам, OneDrive/Obsidian архитектуру, heavy media без немедленного скачивания, исполнимые WP, шаблоны, QA/acceptance, checkpoint и стартовый протокол для новой игры.

**Не путать этот результат с фактическим завершением исследования конкретной настольной игры.** Для него нужен отдельный проход с реальными URL, проверенными файлами, таблицами карточного корпуса, найденными стратегическими источниками, конкретными нумерациями, числовой сверкой состава, оценкой объёма тяжёлых файлов и результатами тестов.

**Нормативная формула:**

> Сначала экспертное расследование и формализация фактов; затем структурированная исполнительская работа студента; и только после неё — воспроизводимая приёмка базы знаний. Тексты, визуальные символы, версии и происхождение — данные первого класса. Тяжёлые медиа первого прохода — в реестре и отчёте, а не в скачанном архиве.
