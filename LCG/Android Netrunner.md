# Android: Netrunner

Living Card Game (FFG, 2012–2018). После закрытия линию поддерживали **NISEI**, затем ребрендинг в **Null Signal Games (NSG)**. Правила совместимы; кардпулы и форматы различаются.

**Важно:** разделы ниже разделены. Не смешивайте FFG-эру и NISEI/NSG без понимания формата (Startup / Standard / Eternal).

Из черновика: [ДАО нетраннера 2.1 — декбилдинг (topdeck.ru)](https://topdeck.ru/forums/topic/41719-bgnetrunner-%D0%B4%D0%B0%D0%BE-%D0%BD%D0%B5%D1%82%D1%80%D0%B0%D0%BD%D0%BD%D0%B5%D1%80%D0%B0-21-%D0%B4%D0%B5%D0%BA%D0%B1%D0%B8%D0%BB%D0%B4%D0%B8%D0%BD%D0%B3/) — RU, форумная статья про колодостроение.

---

## A. Эпоха FFG (оригинальная LCG-линия)

### Правила / обучение
- [Learn to Play (PDF, FFG CDN)](https://images-cdn.fantasyflightgames.com/filer_public/e0/f1/e0f1d651-033b-41bb-8132-c2f6f97aab74/adn_learn_to_play_v2_lo.pdf) — EN, официальный буклет.
- [Rules Reference / Online Rules (PDF, FFG CDN)](https://images-cdn.fantasyflightgames.com/filer_public/25/36/25366980-ce92-4770-a9be-1e2d39f18da1/adn49_online_rules_reference_lores_11.pdf) — EN.
- [FAQ v3.12 (PDF, FFG CDN)](https://images-cdn.fantasyflightgames.com/filer_public/aa/d3/aad35e6c-afdb-4de4-b034-ec5b5b748106/adn_faq_v312.pdf) — EN, поздний FAQ FFG.
- [Rulebook mirror (1jour-1jeu PDF)](https://cdn.1j1ju.com/medias/e5/b4/42-android-netrunner-rulebook.pdf) — EN, зеркало буклета.

### Обзоры / вводные
- [Tesera: страница игры](https://tesera.ru/game/Android-Netrunner/) — RU.
- [BGG: Android Netrunner](https://boardgamegeek.com/boardgame/124742/android-netrunner) — EN (страница существует; с некоторых IP может отдавать 403 ботам).
- [Universal Head / Esoteric Order of Gamers — Rules Summary v2](https://www.orderofgamers.com/android-netrunner-v2/) — EN, классический player aid эпохи FFG (страница жива; прямой PDF на orderofgamers.com/rules/… на момент проверки отдавал 404 — брать с страницы/BGG).
- [BGG file: Universal Head Rules Summary & Reference](https://boardgamegeek.com/filepage/91272/universal-head-android-netrunner-rules-summary-and) — EN; URL подтверждён через BGG Files API, HTML-страница часто 403 ботам — открывать в браузере.

### Базы карт / колодостроение (FFG-эра)
**Главный инструмент и для FFG-кардпула — NetrunnerDB** (фильтры по старым циклам / Eternal / ban history). Ниже — что ещё полезно именно под эпоху FFG.

- [NetrunnerDB](https://netrunnerdb.com/) — EN, база карт + декбилдер; для FFG: фильтры по циклам (Core → Kitara / Reign and Reverie и т.д.), история MWL/ban, поиск по коду карты.
- [Acoo — Deck Builder](https://www.acoo.net/) — EN, исторический онлайн-декбилдер эпохи FFG; **кардпул заявлен до Core Set 2.0** (не NSG). Жив (проверено 200, сент. 2026).
- [Acoo — Cards List](https://www.acoo.net/netrunner-cards-list/) — EN, каталог/список карт на том же движке (пример вводной точки).
- [Meteor Decks (Stimhack)](https://meteor.stimhack.com/) — EN, минималистичный декбилдер; сайт жив (часть контента — draft/cube, полезен как зеркало списков).
- [Jinteki.net](https://jinteki.net/) — EN, онлайн-клиент **с собственным дек-редактором**; импорт текста/листа из NetrunnerDB (см. Export / paste в Decklist). Карты FFG и NSG.
- **CardGameDB (исторический хаб FFG)** — сайт мёртв. Календарь: [Wayback Android Netrunner](https://web.archive.org/web/*/http://www.cardgamedb.com/index.php/androidnetrunner/android-netrunner.html); форумы: [snapshot 2017-01-10](https://web.archive.org/web/20170110003503/http://www.cardgamedb.com/forums/).
- [AlwaysBeRunning](https://alwaysberunning.net/) — EN, турниры/деклисты; для чистой FFG-эры мало актуален (сцена сегодня NSG), но OAuth через NetrunnerDB и архив результатов полезны как индекс.

### Core Set ↔ Revised Core Set — различия карт (допечатка / прокси)

Источник сверки: [NetrunnerDB API](https://netrunnerdb.com/api/2.0/public/cards) (`pack_code`: **`core`** = Core Set / ADN01; **`core2`** = Revised Core Set / ADN49), плюс официальные списки FFG ([AND01](https://images-cdn.fantasyflightgames.com/filer_public/b3/62/b362982b-5648-4712-aabb-50ad368558b3/and01-card-list.pdf), [ADN49](https://images-cdn.fantasyflightgames.com/filer_public/00/9c/009c2fa5-a0c2-402a-acf3-6e051613e4ca/adn49_cardlist.pdf) — URL FFG CDN). Сопоставление по `stripped_title` (одна и та же карта, разные коды). **Новых дизайнов в Revised нет** — только репринты из Core + Genesis + Spin (заявление FFG).

**Счётчики (уникальные карты / копии в коробке):**
- Base `core`: **113** уникальных, **248** копий (коды `01xxx`).
- Revised `core2`: **132** уникальных, **247** копий (коды `20xxx`; на NRDB у части Weyland/Jinteki/NBN поле `position` расходится с суффиксом кода — в таблице ниже код NRDB).
- Только в Base (вырезаны из Revised): **40**.
- Только в Revised (из Data Packs Genesis/Spin): **59**.
- В обоих сетах: **73**; из них с другой тиражностью: **44**; с тем же qty, но другим illustrator (alt-art): **13**.

**Как читать «Что допечатать»:** сценарий «есть **1× Base**, хочу содержимое **1× Revised**» — печатать карты из табл. 2 (qty Revised) и разницу qty там, где Revised > Base (табл. 3, стол «+N к Revised»). Обратный сценарий «нужны вырезанные Base-карты» — табл. 1. Alt-art (табл. 4) для геймплея не обязателен.

Сеты на NRDB: [Core Set](https://netrunnerdb.com/en/set/core) · [Revised Core Set](https://netrunnerdb.com/en/set/core2).

#### 1. Только Base `core` (нет в Revised) — вырезаны

| Код Base | № | Название (EN) | Base | Revised | Что допечатать |
| --- | ---: | --- | ---: | --- | --- |
| `01001` | 1 | Noise: Hacker Extraordinaire | 1 | — | 1× если нужен старый Base-пул |
| `01002` | 2 | Déjà Vu | 2 | — | 2× если нужен старый Base-пул |
| `01006` | 6 | Grimoire | 1 | — | 1× если нужен старый Base-пул |
| `01007` | 7 | Corroder | 2 | — | 2× если нужен старый Base-пул |
| `01009` | 9 | Djinn | 2 | — | 2× если нужен старый Base-пул |
| `01010` | 10 | Medium | 2 | — | 2× если нужен старый Base-пул |
| `01012` | 12 | Parasite | 3 | — | 3× если нужен старый Base-пул |
| `01013` | 13 | Wyrm | 2 | — | 2× если нужен старый Base-пул |
| `01014` | 14 | Yog.0 | 2 | — | 2× если нужен старый Base-пул |
| `01016` | 16 | Wyldside | 2 | — | 2× если нужен старый Base-пул |
| `01018` | 18 | Account Siphon | 2 | — | 2× если нужен старый Base-пул |
| `01023` | 23 | Lemuria Codecracker | 2 | — | 2× если нужен старый Base-пул |
| `01024` | 24 | Desperado | 1 | — | 1× если нужен старый Base-пул |
| `01027` | 27 | Ninja | 2 | — | 2× если нужен старый Base-пул |
| `01031` | 31 | Data Dealer | 1 | — | 1× если нужен старый Base-пул |
| `01032` | 32 | Decoy | 2 | — | 2× если нужен старый Base-пул |
| `01033` | 33 | Kate "Mac" McCaffrey: Digital Tinker | 1 | — | 1× если нужен старый Base-пул |
| `01038` | 38 | Akamatsu Mem Chip | 2 | — | 2× если нужен старый Base-пул |
| `01041` | 41 | The Toolbox | 1 | — | 1× если нужен старый Base-пул |
| `01045` | 45 | Net Shield | 2 | — | 2× если нужен старый Base-пул |
| `01052` | 52 | Access to Globalsec | 3 | — | 3× если нужен старый Base-пул |
| `01054` | 54 | Haas-Bioroid: Engineering the Future | 1 | — | 1× если нужен старый Base-пул |
| `01055` | 55 | Accelerated Beta Test | 3 | — | 3× если нужен старый Base-пул |
| `01065` | 65 | Corporate Troubleshooter | 1 | — | 1× если нужен старый Base-пул |
| `01066` | 66 | Experiential Data | 2 | — | 2× если нужен старый Base-пул |
| `01071` | 71 | Zaibatsu Loyalty | 1 | — | 1× если нужен старый Base-пул |
| `01073` | 73 | Precognition | 2 | — | 2× если нужен старый Base-пул |
| `01074` | 74 | Cell Portal | 2 | — | 2× если нужен старый Base-пул |
| `01075` | 75 | Chum | 2 | — | 2× если нужен старый Base-пул |
| `01076` | 76 | Data Mine | 2 | — | 2× если нужен старый Base-пул |
| `01079` | 79 | Akitaro Watanabe | 1 | — | 1× если нужен старый Base-пул |
| `01081` | 81 | AstroScript Pilot Program | 2 | — | 2× если нужен старый Base-пул |
| `01082` | 82 | Breaking News | 2 | — | 2× если нужен старый Base-пул |
| `01089` | 89 | Matrix Analyzer | 3 | — | 3× если нужен старый Base-пул |
| `01092` | 92 | SanSan City Grid | 1 | — | 1× если нужен старый Base-пул |
| `01095` | 95 | Posted Bounty | 2 | — | 2× если нужен старый Base-пул |
| `01096` | 96 | Security Subcontract | 1 | — | 1× если нужен старый Base-пул |
| `01097` | 97 | Aggressive Negotiation | 2 | — | 2× если нужен старый Base-пул |
| `01099` | 99 | Scorched Earth | 2 | — | 2× если нужен старый Base-пул |
| `01105` | 105 | Research Station | 2 | — | 2× если нужен старый Base-пул |

*Итого: 40 карт, 72 копий в 1× Base.*

#### 2. Только Revised `core2` (нет в original Core) — репринты из Genesis/Spin

| Код Revised | № кода | Название (EN) | Base | Revised | Первый принт (pack) | Что допечатать |
| --- | ---: | --- | ---: | ---: | --- | --- |
| `20001` | 1 | Reina Roja: Freedom Fighter | — | 1 | `mt` Mala Tempora `04041` | 1× (есть только Base → допечатать) |
| `20003` | 3 | Retrieval Run | — | 2 | `fp` Future Proof `02101` | 2× (есть только Base → допечатать) |
| `20004` | 4 | Singularity | — | 1 | `dt` Double Time `04101` | 1× (есть только Base → допечатать) |
| `20007` | 7 | Spinal Modem | — | 2 | `wla` What Lies Ahead `02002` | 2× (есть только Base → допечатать) |
| `20008` | 8 | Darwin | — | 2 | `fp` Future Proof `02102` | 2× (есть только Base → допечатать) |
| `20010` | 10 | Force of Nature | — | 3 | `asis` A Study in Static `02062` | 3× (есть только Base → допечатать) |
| `20011` | 11 | Imp | — | 1 | `wla` What Lies Ahead `02003` | 1× (есть только Base → допечатать) |
| `20012` | 12 | Hemorrhage | — | 1 | `fal` Fear and Loathing `04082` | 1× (есть только Base → допечатать) |
| `20014` | 14 | Morning Star | — | 3 | `wla` What Lies Ahead `02004` | 3× (есть только Base → допечатать) |
| `20016` | 16 | Liberated Account | — | 3 | `ta` Trace Amount `02022` | 3× (есть только Base → допечатать) |
| `20017` | 17 | Scrubber | — | 2 | `asis` A Study in Static `02063` | 2× (есть только Base → допечатать) |
| `20018` | 18 | Xanadu | — | 1 | `hs` Humanity's Shadow `02082` | 1× (есть только Base → допечатать) |
| `20021` | 21 | Emergency Shutdown | — | 2 | `ce` Cyber Exodus `02043` | 2× (есть только Base → допечатать) |
| `20025` | 25 | Doppelgänger | — | 2 | `asis` A Study in Static `02064` | 2× (есть только Base → допечатать) |
| `20026` | 26 | HQ Interface | — | 1 | `hs` Humanity's Shadow `02085` | 1× (есть только Base → допечатать) |
| `20028` | 28 | Faerie | — | 3 | `fp` Future Proof `02104` | 3× (есть только Base → допечатать) |
| `20030` | 30 | Peacock | — | 3 | `wla` What Lies Ahead `02006` | 3× (есть только Base → допечатать) |
| `20031` | 31 | Pheromones | — | 1 | `hs` Humanity's Shadow `02086` | 1× (есть только Base → допечатать) |
| `20035` | 35 | Fall Guy | — | 1 | `dt` Double Time `04106` | 1× (есть только Base → допечатать) |
| `20036` | 36 | Mr. Li | — | 1 | `fp` Future Proof `02105` | 1× (есть только Base → допечатать) |
| `20037` | 37 | Chaos Theory: Wünderkind | — | 1 | `ce` Cyber Exodus `02046` | 1× (есть только Base → допечатать) |
| `20039` | 39 | Indexing | — | 2 | `fp` Future Proof `02106` | 2× (есть только Base → допечатать) |
| `20041` | 41 | Notoriety | — | 1 | `ta` Trace Amount `02026` | 1× (есть только Base → допечатать) |
| `20042` | 42 | Test Run | — | 2 | `ce` Cyber Exodus `02047` | 2× (есть только Base → допечатать) |
| `20045` | 45 | Dinosaurus | — | 2 | `ce` Cyber Exodus `02048` | 2× (есть только Base → допечатать) |
| `20053` | 53 | All-nighter | — | 1 | `asis` A Study in Static `02067` | 1× (есть только Base → допечатать) |
| `20057` | 57 | Dyson Mem Chip | — | 3 | `ta` Trace Amount `02028` | 3× (есть только Base → допечатать) |
| `20060` | 60 | Underworld Contact | — | 2 | `asis` A Study in Static `02069` | 2× (есть только Base → допечатать) |
| `20061` | 61 | Haas-Bioroid: Stronger Together | — | 1 | `wla` What Lies Ahead `02010` | 1× (есть только Base → допечатать) |
| `20062` | 62 | Project Ares | — | 2 | `om` Opening Moves `04010` | 2× (есть только Base → допечатать) |
| `20063` | 63 | Project Vitruvius | — | 3 | `ce` Cyber Exodus `02051` | 3× (есть только Base → допечатать) |
| `20067` | 67 | Hudson 1.0 | — | 1 | `mt` Mala Tempora `04051` | 1× (есть только Base → допечатать) |
| `20073` | 73 | Green Level Clearance | — | 3 | `asis` A Study in Static `02070` | 3× (есть только Base → допечатать) |
| `20075` | 75 | Ash 2X3ZB9CY | — | 1 | `wla` What Lies Ahead `02013` | 1× (есть только Base → допечатать) |
| `20076` | 76 | Strongbox | — | 1 | `fal` Fear and Loathing `04091` | 1× (есть только Base → допечатать) |
| `20079` | 79 | Project Atlas | — | 3 | `wla` What Lies Ahead `02018` | 3× (есть только Base → допечатать) |
| `20080` | 80 | The Cleaners | — | 1 | `st` Second Thoughts `04036` | 1× (есть только Base → допечатать) |
| `20081` | 81 | Dedicated Response Team | — | 1 | `fp` Future Proof `02118` | 1× (есть только Base → допечатать) |
| `20082` | 82 | Elizabeth Mills | — | 1 | `st` Second Thoughts `04037` | 1× (есть только Base → допечатать) |
| `20083` | 83 | GRNDL Refinery | — | 3 | `fal` Fear and Loathing `04099` | 3× (есть только Base → допечатать) |
| `20085` | 85 | Caduceus | — | 2 | `wla` What Lies Ahead `02019` | 2× (есть только Base → допечатать) |
| `20087` | 87 | Hive | — | 2 | `dt` Double Time `04117` | 2× (есть только Base → допечатать) |
| `20091` | 91 | Punitive Counterstrike | — | 2 | `tc` True Colors `04079` | 2× (есть только Base → допечатать) |
| `20094` | 94 | Braintrust | — | 3 | `wla` What Lies Ahead `02014` | 3× (есть только Base → допечатать) |
| `20097` | 97 | Ronin | — | 1 | `fp` Future Proof `02112` | 1× (есть только Base → допечатать) |
| `20099` | 99 | Himitsu-Bako | — | 3 | `om` Opening Moves `04013` | 3× (есть только Base → допечатать) |
| `20101` | 101 | Swordsman | — | 2 | `st` Second Thoughts `04033` | 2× (есть только Base → допечатать) |
| `20103` | 103 | Whirlpool | — | 1 | `hs` Humanity's Shadow `02094` | 1× (есть только Base → допечатать) |
| `20104` | 104 | Yagura | — | 1 | `fal` Fear and Loathing `04093` | 1× (есть только Base → допечатать) |
| `20105` | 105 | Celebrity Gift | — | 3 | `om` Opening Moves `04012` | 3× (есть только Base → допечатать) |
| `20107` | 107 | Trick of Light | — | 2 | `ta` Trace Amount `02033` | 2× (есть только Base → допечатать) |
| `20108` | 108 | Hokusai Grid | — | 1 | `hs` Humanity's Shadow `02095` | 1× (есть только Base → допечатать) |
| `20110` | 110 | Project Beale | — | 3 | `fp` Future Proof `02115` | 3× (есть только Base → допечатать) |
| `20111` | 111 | TGTBT | — | 3 | `tc` True Colors `04075` | 3× (есть только Base → допечатать) |
| `20114` | 114 | Flare | — | 1 | `fp` Future Proof `02117` | 1× (есть только Base → допечатать) |
| `20115` | 115 | Pop-up Window | — | 3 | `ce` Cyber Exodus `02056` | 3× (есть только Base → допечатать) |
| `20117` | 117 | Wraparound | — | 2 | `fal` Fear and Loathing `04096` | 2× (есть только Base → допечатать) |
| `20123` | 123 | Bernice Mai | — | 1 | `hs` Humanity's Shadow `02097` | 1× (есть только Base → допечатать) |
| `20124` | 124 | False Lead | — | 1 | `asis` A Study in Static `02080` | 1× (есть только Base → допечатать) |

*Итого: 59 карт, 108 копий в 1× Revised.*

#### 3. В обоих сетах, разная тиражность

| Код Base / Revised | Название (EN) | Base | Revised | Δ | Что допечатать |
| --- | --- | ---: | ---: | ---: | --- |
| `01003` / `20002` | Demolition Run | 3 | 2 | -1 | 1× лишние в Base / не хватает в Revised (для зеркала Base) |
| `01004` / `20005` | Stimhack · alt-art | 3 | 1 | -2 | 2× лишние в Base / не хватает в Revised (для зеркала Base) |
| `01005` / `20006` | Cyberfeeder | 3 | 2 | -1 | 1× лишние в Base / не хватает в Revised (для зеркала Base) |
| `01011` / `20013` | Mimic · alt-art | 2 | 3 | +1 | +1× к Revised (в Base меньше) |
| `01020` / `20022` | Forged Activation Orders · alt-art | 3 | 2 | -1 | 1× лишние в Base / не хватает в Revised (для зеркала Base) |
| `01021` / `20023` | Inside Job | 3 | 2 | -1 | 1× лишние в Base / не хватает в Revised (для зеркала Base) |
| `01022` / `20024` | Special Order · alt-art | 3 | 1 | -2 | 2× лишние в Base / не хватает в Revised (для зеркала Base) |
| `01025` / `20027` | Aurora | 2 | 3 | +1 | +1× к Revised (в Base меньше) |
| `01028` / `20032` | Sneakdoor Beta | 2 | 1 | -1 | 1× лишние в Base / не хватает в Revised (для зеркала Base) |
| `01034` / `20038` | Diesel | 3 | 2 | -1 | 1× лишние в Base / не хватает в Revised (для зеркала Base) |
| `01035` / `20040` | Modded · alt-art | 2 | 3 | +1 | +1× к Revised (в Base меньше) |
| `01036` / `20043` | The Maker’s Eye · alt-art | 3 | 1 | -2 | 2× лишние в Base / не хватает в Revised (для зеркала Base) |
| `01037` / `20044` | Tinkering | 3 | 2 | -1 | 1× лишние в Base / не хватает в Revised (для зеркала Base) |
| `01040` / `20047` | The Personal Touch · alt-art | 2 | 1 | -1 | 1× лишние в Base / не хватает в Revised (для зеркала Base) |
| `01042` / `20048` | Battering Ram | 2 | 3 | +1 | +1× к Revised (в Base меньше) |
| `01046` / `20051` | Pipeline · alt-art | 2 | 3 | +1 | +1× к Revised (в Base меньше) |
| `01048` / `20054` | Sacrificial Construct | 2 | 1 | -1 | 1× лишние в Base / не хватает в Revised (для зеркала Base) |
| `01049` / `20055` | Infiltration | 3 | 2 | -1 | 1× лишние в Base / не хватает в Revised (для зеркала Base) |
| `01051` / `20058` | Crypsis · alt-art | 3 | 2 | -1 | 1× лишние в Base / не хватает в Revised (для зеркала Base) |
| `01057` / `20065` | Aggressive Secretary | 2 | 1 | -1 | 1× лишние в Base / не хватает в Revised (для зеркала Base) |
| `01058` / `20071` | Archived Memories | 2 | 1 | -1 | 1× лишние в Base / не хватает в Revised (для зеркала Base) |
| `01059` / `20072` | Biotic Labor | 3 | 2 | -1 | 1× лишние в Base / не хватает в Revised (для зеркала Base) |
| `01060` / `20074` | Shipment from MirrorMorph | 2 | 1 | -1 | 1× лишние в Base / не хватает в Revised (для зеркала Base) |
| `01061` / `20066` | Heimdall 1.0 · alt-art | 2 | 1 | -1 | 1× лишние в Base / не хватает в Revised (для зеркала Base) |
| `01062` / `20068` | Ichi 1.0 · alt-art | 3 | 2 | -1 | 1× лишние в Base / не хватает в Revised (для зеркала Base) |
| `01063` / `20070` | Viktor 1.0 · alt-art | 2 | 3 | +1 | +1× к Revised (в Base меньше) |
| `01068` / `20095` | Nisei MK II | 3 | 2 | -1 | 1× лишние в Base / не хватает в Revised (для зеркала Base) |
| `01069` / `20096` | Project Junebug | 3 | 2 | -1 | 1× лишние в Base / не хватает в Revised (для зеркала Base) |
| `01070` / `20098` | Snare! | 3 | 2 | -1 | 1× лишние в Base / не хватает в Revised (для зеркала Base) |
| `01077` / `20100` | Neural Katana | 3 | 1 | -2 | 2× лишние в Base / не хватает в Revised (для зеркала Base) |
| `01078` / `20102` | Wall of Thorns | 3 | 1 | -2 | 2× лишние в Base / не хватает в Revised (для зеркала Base) |
| `01083` / `20118` | Anonymous Tip · alt-art | 2 | 1 | -1 | 1× лишние в Base / не хватает в Revised (для зеркала Base) |
| `01085` / `20120` | Psychographics · alt-art | 2 | 3 | +1 | +1× к Revised (в Base меньше) |
| `01087` / `20112` | Ghost Branch · alt-art | 3 | 1 | -2 | 2× лишние в Base / не хватает в Revised (для зеркала Base) |
| `01088` / `20113` | Data Raven · alt-art | 3 | 2 | -1 | 1× лишние в Base / не хватает в Revised (для зеркала Base) |
| `01090` / `20116` | Tollbooth | 3 | 2 | -1 | 1× лишние в Base / не хватает в Revised (для зеркала Base) |
| `01091` / `20122` | Red Herrings · alt-art | 2 | 1 | -1 | 1× лишние в Base / не хватает в Revised (для зеркала Base) |
| `01094` / `20078` | Hostile Takeover · alt-art | 3 | 1 | -2 | 2× лишние в Base / не хватает в Revised (для зеркала Base) |
| `01101` / `20084` | Archer | 2 | 1 | -1 | 1× лишние в Base / не хватает в Revised (для зеркала Base) |
| `01102` / `20086` | Hadrian's Wall · alt-art | 2 | 1 | -1 | 1× лишние в Base / не хватает в Revised (для зеркала Base) |
| `01103` / `20088` | Ice Wall | 3 | 2 | -1 | 1× лишние в Base / не хватает в Revised (для зеркала Base) |
| `01104` / `20089` | Shadow | 3 | 2 | -1 | 1× лишние в Base / не хватает в Revised (для зеркала Base) |
| `01106` / `20125` | Priority Requisition · alt-art | 3 | 2 | -1 | 1× лишние в Base / не хватает в Revised (для зеркала Base) |
| `01107` / `20126` | Private Security Force · alt-art | 3 | 2 | -1 | 1× лишние в Base / не хватает в Revised (для зеркала Base) |

*Итого: 44 карт с разным qty.* Из них Revised **больше** Base: **7** (допечатать **7** копий); Revised **меньше** Base: **37**.

#### 4. Тот же qty, другое искусство (illustrator) — опционально для прокси

| Код Base / Revised | Название (EN) | Qty | Illustrator Base → Revised |
| --- | --- | ---: | --- |
| `01008` / `20009` | Datasucker | 2 | Chelsea Conlin → Liiga Smilshkalne |
| `01015` / `20015` | Ice Carver | 1 | Mark Anthony Taduran → Adam S. Doyle |
| `01017` / `20019` | Gabriel Santiago: Consummate Professional | 1 | Ralph Beisner → Matt Zeilinger |
| `01026` / `20029` | Femme Fatale | 2 | Kate Niemczyk → Anna Christenson |
| `01029` / `20033` | Bank Job | 2 | Mauricio Herrera → Kate Laird |
| `01030` / `20034` | Crash Space | 2 | Tim Durning → Samuel Leung |
| `01043` / `20049` | Gordian Blade | 3 | Mike Nesbitt → Adam S. Doyle |
| `01053` / `20059` | Armitage Codebusting | 3 | Mauricio Herrera → Dmitry Prosvirnin, Atha Kanaani |
| `01072` / `20106` | Neural EMP | 2 | Christina Davis → Matt Zeilinger |
| `01086` / `20121` | SEA Source | 2 | Mauricio Herrera → Dmitry Prosvirnin, Atha Kanaani |
| `01108` / `20127` | Melange Mining Corp. | 2 | Henning Ludvigsen → Emilio Rodríguez |
| `01109` / `20128` | PAD Campaign | 3 | Alexandra Douglass → Kate Laird |
| `01110` / `20132` | Hedge Fund | 3 | Gong Studios → Mark Molnar |

*Итого alt-art при том же qty: 13. (Ещё часть карт из табл. 3 тоже сменили арт — помечены «alt-art».)*

**Практика допечатки из 1× Base → состав 1× Revised:** табл. 2 целиком + положительные Δ из табл. 3. Вырезанные Base-карты (табл. 1) в Revised не входят — их не печатать, если цель только Revised. Полный playset 3× многих синглтонов Revised всё равно потребует 2–3 коробки / отдельные DP / прокси.


### Сканы карт / прокси-изображения (FFG)
- [Google Drive — полный набор сканов](https://drive.google.com/drive/folders/1WwMF6danrz8qvY-yZ5R9wSiFVRESZO7a) — общая папка со сканами (от пользователя); полный набор, не только Kitara.
**Это дампы сканов FFG-картона**, не официальный PnP NSG. Ссылки — на обсуждения/индексы (Drive/Mega внутри тредов могут ротироваться — открывать глазами).

- [Reddit: Android Netrunner Cards up to Kitara @600dpi](https://www.reddit.com/r/Netrunner/comments/8pgfbj/android_netrunner_cards_up_to_kitara_600dpi/) — EN, индекс LepcisMagna: сканы ~всех печатных наборов FFG до Kitara (+ Revised Core, Reign and Reverie, championship full art); в посте — ссылка на организованную папку Drive. *(HTML Reddit с box часто 403 — открывать в браузере.)*
- [Reddit: Kitara — Council of the Crest @600dpi](https://www.reddit.com/r/Netrunner/comments/816os0/kitara_council_of_the_crest_600dpi/) — EN, ранний пост той же серии сканов.
- [Reddit: AI upscaling…600dpi](https://www.reddit.com/r/Netrunner/comments/x7ymbu/some_ai_upscaling600dpi/) — EN; в комментариях снова указывают на Drive с FFG @600dpi (перекрёстная проверка к треду Kitara).
- [Proxy Nexus](https://proxynexus.net/) — EN, генерация printable PDF / MPC ZIP из списка карт или URL деклиста NetrunnerDB; изначально завязан на сканы LepcisMagna + изображения из официальных PnP (см. [instructions](https://proxynexus.net/instructions)). Удобный «мост» скан → печать, без ручного сбора папок. Код: [axmccx/proxynexus-rs](https://github.com/axmccx/proxynexus-rs).
  - **Update 2026-08-28** ([r/Netrunner пост u/axmccx](https://www.reddit.com/r/Netrunner/comments/1w19fdm/proxy_nexus_update_20260828/)): заявлена поддержка **Netrunner Reboot** карт (`netrunner_reboot` в репо). Ранее анонсированные фичи, которые пост снова подчёркивает: **AI up-scaling** (Real-ESRGAN в браузере / WebGPU; заметный выигрыш на низком качестве вроде Midnight Sun; тяжело по GPU). FFG vs NSG: сайт по-прежнему проксирует community/FFG-сканы и извлечённые NSG PnP-изображения — для полных NSG-сетов автор/NSG рекомендуют покупать/печатать через официальные каналы (см. Purchase Guide NSG), а не только прокси.
- Справочные (не 600dpi) изображения карт: [NetrunnerDB](https://netrunnerdb.com/) (просмотр по сетам) — для учёта/декбилда, не замена hi-res сканам.

### Онлайн-игра
- [Jinteki.net](https://www.jinteki.net/) — EN, бесплатный клиент; поддерживает карты FFG и NSG.

### Комьюнити (общие хабы, где ещё помнят FFG-эру)
- [r/Netrunner](https://www.reddit.com/r/Netrunner/) — EN.
- [Android: Netrunner в Москве (VK)](https://vk.ru/netrunner_msk) — RU.
- [Stimhack: New Players](https://stimhack.com/new-players/) — EN, хаб статей для новичков (сайт жив; часть материалов — эпоха FFG, принципы экономики/консистентности всё ещё полезны).
- [Stimhack: Giving Your Deck Enough Credit](https://stimhack.com/giving-your-deck-enough-credit/) — EN, про экономику колоды.

---

## B. NISEI → Null Signal Games (NSG) — текущая поддержка
*(Также называют Null Signal / NSG; ранее — NISEI.)*

NISEI — фанатская организация после закрытия FFG; позже ребрендинг в **Null Signal Games**. Сайт nisei.net редиректит/живёт как наследие; актуальный хаб — nullsignal.games.

### Правила / обучение (актуальные)
- [Null Signal Games — главная](https://nullsignal.games/) — EN, старт: System Gateway Remastered.
- [Learn to Play (NSG)](https://nullsignal.games/players/learn-to-play/) — EN, вводный хаб под стартовые колоды System Gateway.
- [Learn to Play: Runner](https://nullsignal.games/players/learn-to-play/learn-to-play-runner/) — EN, скриптованный туториал Runner.
- [Learn to Play: Run Guide](https://nullsignal.games/players/learn-to-play/run-guide/) — EN, быстрая схема тайминга рана.
- [L2P Decks + script PDF](https://nullsignal.games/l2p-decks/) — EN, колоды и сценарий обучения; PDF сценария: [Learn-to-Play-v2.1.pdf](https://nullsignal.games/wp-content/uploads/2025/04/Learn-to-Play-v2.1.pdf) (проверено 200).
- [Teach with L2P Decks](https://nullsignal.games/l2p-decks-teacher/) — EN, страница для того, кто учит 1–2 новичков.
- [Comprehensive Rules Hub](https://nullsignal.games/rules/comp-rules/) — EN, живые comprehensive rules (совместимы с FFG-картами).
- [Major Changes](https://nullsignal.games/players/major-changes/) — EN, что изменилось в правилах/терминах с времён FFG.
- [Supported Formats](https://nullsignal.games/players/supported-formats/) — EN, Startup / Standard / ban lists (на сентябрь 2026 Startup: System Gateway + Elevation + Vantage Point).
- [FAQ (NSG)](https://nullsignal.games/about/frequently-asked-questions/) — EN.
- [Learn to Play — NISEI (наследие)](https://nisei.net/players/learn-to-play/) — EN, старый URL (закладки).

### С чего начать / покупка и PnP
- [System Gateway — Remastered](https://nullsignal.games/products/system-gateway/) — EN, рекомендуемый старт; Starter Decks + Deckbuilding Pack.
- [Elevation](https://nullsignal.games/products/elevation/) — EN, рекомендуемое первое расширение после Gateway (Core Sets = Gateway + Elevation).
- [Purchase Guide](https://nullsignal.games/players/purchase-guide/) — EN: NSG store, DriveThruCards, **MakePlayingCards**, реселлеры, бесплатные PnP PDF.
- [NSG Shop](https://shop.nullsignal.games/) — EN.
- PnP sheets System Gateway (A4, 1×): [SystemGatewayEnglish-A4-Printable-Sheets-1x.pdf](https://nullsignal.games/wp-content/uploads/2023/07/SystemGatewayEnglish-A4-Printable-Sheets-1x.pdf) — EN, проверено 200.

### Статьи / материалы NSG и комьюнити (обогащение)
Официальный блог / статьи:
- [Tag: System Gateway (архив блога)](https://nullsignal.games/blog/tag/system-gateway/) — EN, все статьи про Gateway.
- [System Gateway Full Spoiler](https://nullsignal.games/blog/system-gateway-full-spoiler/) — EN, полный спойлер набора (2021).
- [You Got Econ in My Shaper!](https://nullsignal.games/blog/you-got-econ-in-my-shaper/) — EN, про раннер-экономику в Gateway.
- [Core Sets-only Sample Decklists (блог)](https://nullsignal.games/blog/core-sets-only-sample-decklists/) — EN, анонс сэмпл-колод Gateway+Elevation (Phi / Girometics, 2025-05).
- [Getting Started: Sample Decklists (статическая страница)](https://nullsignal.games/players/getting-started-sample-decklists/) — EN, **главная точка входа**: визуальные списки колод только Gateway и Core Sets (Gateway+Elevation), с ссылками на NetrunnerDB.
- [A Love Letter To Startup](https://nullsignal.games/blog/a-love-letter-to-startup/) — EN, зачем нужен формат Startup.
- [Startup Balance Update 26.03](https://nullsignal.games/blog/startup-balance-update-26-03/) — EN, ротация Liberation / вход Vantage Point.
- [Startup Balance Update 26.09](https://nullsignal.games/blog/startup-balance-update-26-09/) — EN, актуальное на сентябрь 2026 (в т.ч. unban Reality Plus).

Комьюнити-гайды (EN):
- [A Complete(ish) Introduction to Startup (rooknetrunner)](https://rooknetrunner.wordpress.com/2022/07/22/a-completeish-introduction-to-startup/) — EN, разбор формата и «столпов» декбилдинга (экономика, брейкеры и т.п.).
- [How to Use NetrunnerDB to Build and Print a Legal Deck](https://netrunnerandroid.com/how-to-use-netrunnerdb-to-build-and-print-a-legal-deck/) — EN, пошаговый гайд по NetrunnerDB под актуальные форматы.
- [Archetype Beginner Series: Reg Runner (Supernaut)](https://supernaut26.substack.com/p/archetype-beginner-series-reg-runner/) — EN, архетип «обычного» раннера на Core Sets.
- [Deckbuilding 101 — First Corp Deck (System Gateway) — YouTube](https://www.youtube.com/watch?v=i1zoeeDJr-k) — EN, Métropole Grid: пошаговое строительство первой корп-колоды (agenda density, размер колоды 40→44).
- [AlwaysBeRunning](https://alwaysberunning.net/) — EN, турниры и деклисты (хороший источник «живых» Startup-листов после того, как освоите Core Sets).

### Базы карт / колодостроение (NSG / актуальные форматы)
**Не путать с Acoo / CardGameDB:** для Startup / Standard / NSG-only нужен NetrunnerDB (и связанные с ним ABR / Proxy Nexus / NetForge).

- [NetrunnerDB](https://netrunnerdb.com/) — EN, главная база + декбилдер; форматы **Startup / Standard / NSG-only**, банлисты, поиск `z:startup` и т.п.
- [Поиск публичных деклистов Startup](https://netrunnerdb.com/en/decklists/find?f=startup) — EN.
- [Деклисты автора Null Signal Games](https://netrunnerdb.com/en/decklists/find?author=Null%20Signal%20Games) — EN, официальные сэмплы.
- [AlwaysBeRunning](https://alwaysberunning.net/) — EN, турнирный хаб: события + деклисты; логин через NetrunnerDB OAuth; claim спота привязывает колоду NRDB.
- [Jinteki.net](https://jinteki.net/) — EN, онлайн + дек-редактор; импорт листа из NetrunnerDB (paste / export). Для тестов Startup/Standard.
- [NetForge](https://netforge.cards/) — EN, мобильный companion (iOS/Android): браузер карт, декбилдер с форматами/influence, трекер партии, sync с NetrunnerDB.
- [Meteor Decks](https://meteor.stimhack.com/) — EN, альтернативный/минималистичный билдер (жив; не замена NRDB для актуальных банлистов).
- [Acoo](https://www.acoo.net/) — **не для NSG-кардпула** (стоп на Core Set 2.0); оставлен только как FFG-исторический инструмент — см. блок A.

### Сканы карт / прокси-изображения (NSG ≠ FFG-дампы)
**Официальный PnP NSG — не то же самое, что скан-дампы FFG.** Печать System Gateway / Elevation / циклов NSG — через PDF NSG (легальный турнирный PnP). Hi-res сканы FFG — блок A выше.

- Официальный PnP NSG: [Purchase Guide](https://nullsignal.games/players/purchase-guide/) + пример sheets [SystemGatewayEnglish-A4…](https://nullsignal.games/wp-content/uploads/2023/07/SystemGatewayEnglish-A4-Printable-Sheets-1x.pdf); практический гайд: [From Zero to Netrunner PnP Hero](https://jbargu.github.io/en/post/print-and-play-netrunner/).
- [Proxy Nexus](https://proxynexus.net/) + [instructions](https://proxynexus.net/instructions) — EN; PDF/MPC из списка или URL NetrunnerDB (сканы FFG + изображения из PnP NSG-наборов, где подключены). Удобно печатать смешанные/NRDB-листы без ручной сборки.
- Русские зеркала / переводы PnP: Tesera State of Netrunner + [n1531](https://vk.ru/n1531) — см. блоки ниже.
- FFG @600dpi дампы — **только** раздел A «Сканы карт (FFG)»; не подставлять их вместо официального PnP NSG на турнирах без сверки правил/бэкинга.

### Декбилдинг для новичков / иммерсии (критично): визуальные списки и пошаговые инструкции

**Практический маршрут иммерсии (Core → Startup):**
1. Пройти скриптованный L2P (не тасовать стартовые колоды до конца скрипта) — [L2P Decks](https://nullsignal.games/l2p-decks/) + [Learn-to-Play-v2.1.pdf](https://nullsignal.games/wp-content/uploads/2025/04/Learn-to-Play-v2.1.pdf).
2. Сыграть встроенные Starter Decks из System Gateway (карты с точками/плюсами в углу — обучающий порядок).
3. Собрать / взять **сэмпл-колоду только из System Gateway** (ниже) — понять ID, влияние, agenda points.
4. Расширить до **Core Sets** (Gateway + Elevation) — сэмплы Phi на той же странице.
5. Когда комфортно — фильтр **Startup** на NetrunnerDB и актуальный банлист на [Supported Formats](https://nullsignal.games/players/supported-formats/).

**Пошагово: как собрать первую колоду в NetrunnerDB (Startup / Core):**
1. Зарегистрироваться → My Decks → New Corp/Runner deck.
2. Сначала выбрать **формат** (Startup или ограничить packs вручную: System Gateway, затем + Elevation).
3. Выбрать Identity — смотреть min deck size и influence.
4. Корп: набрать нужные agenda points (для 40–44 карт обычно 18–19; часто играют 44 карты при минимуме 40, чтобы разредить адженды).
5. Раннер: экономика + дро + suite брейкеров (Barrier / Code Gate / Sentry) + давление (multiaccess / runs).
6. Не превышать influence на out-of-faction картах; нейтральные — бесплатно.
7. Сохранить / экспортировать в Jinteki.net для тестов.

**Русские пошаговые статьи с иллюстрациями карт (Tesera / VK-источник netrunner_spb):**
- [Netrunner: как начать или вернуться (2022)](https://tesera.ru/article/faq-netrunner/) — RU, что брать, форматы, токены, протекторы, где играть.
- [Netrunner: советы для колоды Корпорации](https://tesera.ru/article/2110564/) — RU, **с иллюстрациями**: стартовая/расширенная колода Gateway, структура (Agenda / ICE / экономика / уловки), influence, размер 40→44 / 45→49, пошаговый NetrunnerDB.
- [Netrunner: советы для колоды Раннера](https://tesera.ru/article/2121958/) — RU, заключительная статья серии про основы раннер-колоды.

**Официальные визуальные сэмпл-листы (только Gateway) — Grey «CritHitD20» Tongue:**

| Колода | Сторона / ID | NetrunnerDB |
| --- | --- | --- |
| Party Hard | Anarch — René “Loup” Arcemont | [ссылка](https://netrunnerdb.com/en/decklist/4d5bc20d-5ff2-4792-bc79-226d3bb2de8f/party-hard-sg-only-) |
| Stolen Goods | Criminal — Zahya Sadeghi | [ссылка](https://netrunnerdb.com/en/decklist/e6cfb890-c28d-453b-a8aa-57cda3a7ebf8/stolen-goods-sg-only-) |
| Planning Ahead | Shaper — Tāo Salonga | [ссылка](https://netrunnerdb.com/en/decklist/d14197a6-74dd-47d0-a6e7-886d75153d8d/planning-ahead-sg-only-) |
| Discretion Advised | HB — Precision Design | [ссылка](https://netrunnerdb.com/en/decklist/2e178470-fafa-4dfd-b797-b2413b5cc613/discretion-advised-sg-only-) |
| Advanced Yomi | Jinteki — Restoring Humanity | [ссылка](https://netrunnerdb.com/en/decklist/c0122ed3-c9b7-446c-bf2b-01e207f22982/advanced-yomi-sg-only-) |
| Hyper Velocity | NBN — Reality Plus | [ссылка](https://netrunnerdb.com/en/decklist/c8f08617-26df-4deb-8fab-415c9dddd9e1/hyper-velocity-sg-only-) |
| Quick and Dirty | Weyland — Built to Last | [ссылка](https://netrunnerdb.com/en/decklist/5c7d19c1-ce7b-40ab-811e-e4481078751c/quick-and-dirty-sg-only-) |

Полные карточные списки (с количествами) — на [Getting Started: Sample Decklists](https://nullsignal.games/players/getting-started-sample-decklists/).

**Официальные сэмплы Core Sets (Gateway + Elevation) — Phi / Girometics** (подписи NSG; все проверены на NetrunnerDB):
- Runner: [Bowel Movements](https://netrunnerdb.com/en/decklist/81c60189-b0b9-429b-83a8-0cd6611fcff1/-nsg-core-bowel-movements), [Dashing Mad](https://netrunnerdb.com/en/decklist/074c32b0-6429-49ec-91c1-46dcddba9e4b/-nsg-core-dashing-mad), [Prick Thyself](https://netrunnerdb.com/en/decklist/bbcf997a-3ec6-4728-9813-82df335db2f3/-nsg-core-prick-thyself), [Tickets, please](https://netrunnerdb.com/en/decklist/96ef311d-5a55-43e3-be41-28b072994e30/-nsg-core-tickets-please), [Shootin’ ‘n’ Lootin’](https://netrunnerdb.com/en/decklist/a9c9e074-d20a-40ca-8030-f5d0d1ce677f/-nsg-core-shootin-n-lootin-), [Professional Opportunities](https://netrunnerdb.com/en/decklist/aca8a765-6c5b-4f3a-81c8-16c4dde32fdd/-nsg-core-professional-opportunities), [Flow and Ebb](https://netrunnerdb.com/en/decklist/1bf875a5-4138-40d3-87f0-de874f63135e/-nsg-core-flow-and-ebb), [Enthusiasm](https://netrunnerdb.com/en/decklist/14966eb5-a65c-4578-83bb-345e566df203/-nsg-core-enthusiasm), [Sabbatical](https://netrunnerdb.com/en/decklist/9727f883-4edd-4f1a-aabc-e1f94fd63834/-nsg-core-sabbatical).
- Corp: [Brutal Efficiency](https://netrunnerdb.com/en/decklist/b441510e-00e7-42b7-a559-a7eba52b31a4/-nsg-core-brutal-efficiency), [Agency](https://netrunnerdb.com/en/decklist/8b2c2754-48c2-4375-a124-e1eebba9a95e/-nsg-core-agency), [Fashion Lab](https://netrunnerdb.com/en/decklist/8d182470-77e1-4d5e-b55e-19f08dc44470/-nsg-core-fashion-lab), [Hidden Funds](https://netrunnerdb.com/en/decklist/fd9af10d-4c0f-4b70-ad5d-83aa51903a16/-nsg-core-hidden-funds), [Peculiarity](https://netrunnerdb.com/en/decklist/568d1eb8-340c-4bb1-bf77-54c21b514833/-nsg-core-peculiarity), [Glyph of Warding](https://netrunnerdb.com/en/decklist/da28fae5-8c7c-4354-8ed3-6ce6e5769cec/-nsg-core-glyph-of-warding), [Fine Print](https://netrunnerdb.com/en/decklist/abc6721f-4680-40fe-b189-cdf19f416bd1/-nsg-core-fine-print), [Not so subtle](https://netrunnerdb.com/en/decklist/170f1c2f-e063-415a-ab06-7ef49763da04/-nsg-core-not-so-subtle), [Gimbatul](https://netrunnerdb.com/en/decklist/19db2c28-8521-4b86-a45e-e46cb9830243/-nsg-core-gimbatul), [Brick Stack](https://netrunnerdb.com/en/decklist/51804cff-8a01-4b85-b1cc-a140935cf81c/-nsg-core-brick-stack), [Pork Chops](https://netrunnerdb.com/en/decklist/f315fb7f-798b-4b4a-b515-675590b3f258/-nsg-core-pork-chops), [Quick Returns](https://netrunnerdb.com/en/decklist/1f9d8054-4993-4a09-91ba-4fca5fff3747/-nsg-core-quick-returns).

**Заметки по «newbie / budget / first decks»:**
- Официальные сэмплы выше — лучший «first deck» визуальный источник: полные списки на сайте NSG + кликабельные NetrunnerDB.
- Исторические Startup-гайды с полным write-up (пример эпохи Ashes+Gateway): [Better Lucky (full guide)](https://netrunnerdb.com/en/decklist/b3ca3b99-327d-484c-a5e7-8b788898c998/-startup-better-lucky-with-full-guide-), [Widowmaker (full guide)](https://netrunnerdb.com/en/decklist/538aa6b3-774b-49cb-8945-31d60027522a/-startup-widowmaker-with-full-guide-) — полезны как *метод объяснения карточных выборов*, но кардпул устарел относительно Startup 2026; перед копированием сверять легальность на NetrunnerDB / Supported Formats.
- «Budget» в смысле покупки: Gateway Remastered = полный playset базовых карт; дальше Elevation; PnP легален на турнирах NSG при аккуратной печати.

### Tesera / BGG: файлы, иллюстрации, player aids

**Tesera (RU) — статьи и скачиваемые файлы (проверено HTTP 200 с box, сентябрь 2026):**
- [State of Netrunner — май 2026](https://tesera.ru/article/2591649/) — RU, актуальное состояние NSG, форматы, русские переводы; в конце статьи — ссылки на PnP.
- Черновик русских правил (Google Doc из статьи): [docs.google.com/…/15-f0SBvb5gKhDiVEiU2FPdVT5y475tbJRzOO-hDyswM](https://docs.google.com/document/d/15-f0SBvb5gKhDiVEiU2FPdVT5y475tbJRzOO-hDyswM/edit) — RU.
- Русские PnP (Яндекс.Диск, из State of Netrunner; HTTP 200 на ссылки):
  - Врата системы / System Gateway: [disk.yandex.ru/i/Yo6v1SFPOwplRQ](https://disk.yandex.ru/i/Yo6v1SFPOwplRQ)
  - Восхождение / Elevation: [disk.yandex.ru/i/_wsJjuh40O66jw](https://disk.yandex.ru/i/_wsJjuh40O66jw)
  - Цикл Освобождение / Liberation: [disk.yandex.ru/i/t5CtkcoOaZfQAQ](https://disk.yandex.ru/i/t5CtkcoOaZfQAQ)
- Зеркала английских наборов (из той же статьи; часть проверена 200):
  - System Gateway EN: [disk.yandex.ru/i/yzf4s3OSvipRMg](https://disk.yandex.ru/i/yzf4s3OSvipRMg)
  - Elevation EN: [disk.yandex.ru/i/FP51qBMjRNCzcQ](https://disk.yandex.ru/i/FP51qBMjRNCzcQ)
  - Downfall / Uprising / Midnight Sun / Parhelion / Automata / Rebellion / Vantage Point — см. конец [статьи 2591649](https://tesera.ru/article/2591649/) (ссылки вида disk.yandex.ru/i/…).
- Файлы в карточке игры Tesera (эпоха FFG / общие aids; 200):
  - [ADN_Tournament_Rules.pdf](https://tesera.ru/images/items/154643/ADN_Tournament_Rules.pdf)
  - [AndroidNetrunner_v1.0.pdf](https://tesera.ru/images/items/253099/AndroidNetrunner_v1.0.pdf) — RU-ориентированный PDF в items Tesera.
- Статьи с иллюстрациями декбилдинга: [Корп](https://tesera.ru/article/2110564/), [Раннер](https://tesera.ru/article/2121958/), [FAQ старт](https://tesera.ru/article/faq-netrunner/).

**BGG Files (thing 124742) — статус верификации:**
- Каталог файлов: [boardgamegeek.com/files/thing/124742](https://boardgamegeek.com/files/thing/124742) — HTML с box часто 403 (Cloudflare); **список подтверждён через BGG Files API** (`api.geekdo.com/api/files?objectid=124742`). Страницы filepage ниже — открывать вручную в браузере; ботам часто 403.
- Полезные player aids / refs (API подтвердил существование; HTML=403 ботам):
  - [Unofficial Rules Reference — NISEI V1.5](https://boardgamegeek.com/filepage/239356/unofficial-rules-reference-nisei-v15)
  - [Unofficial turn reference for NISEI](https://boardgamegeek.com/filepage/226717/unofficial-turn-reference-for-nisei)
  - [Android: Netrunner — one page quick reference](https://boardgamegeek.com/filepage/231602/android-netrunner-one-page-quick-reference)
  - [Printable A4 color playmats](https://boardgamegeek.com/filepage/237261/printable-a4-color-playmats) / [B&W](https://boardgamegeek.com/filepage/237260/printable-a4-black-and-white-playmats)
  - [Printable Playmats for teaching](https://boardgamegeek.com/filepage/214583/android-netrunner-printable-playmats-for-teaching)
  - [John’s Ultimate Player Aids](https://boardgamegeek.com/filepage/188727/john-s-ultimate-player-aids-for-netrunner)
  - [Universal Head Rules Summary & Reference](https://boardgamegeek.com/filepage/91272/universal-head-android-netrunner-rules-summary-and) — FFG-эра
  - [Symbol / Icon Quick Reference for teaching](https://boardgamegeek.com/filepage/100614/android-netrunner-symbol-icon-quick-reference-for)
  - [Правила игры / Rules in russian](https://boardgamegeek.com/filepage/85591/pravila-igry-rules-in-russian) — RU, эпоха FFG
- Альтернатива без BGG-логина: [Esoteric Order of Gamers — Netrunner v2](https://www.orderofgamers.com/android-netrunner-v2/) (страница 200).
- Reddit-треды про современные System Gateway reference sheets существуют (поиск: «System Gateway Player Reference Sheet»), но reddit.com с box отдавал 403 — URL не считаем верифицированными до ручной проверки.

### Онлайн-игра
- [Jinteki.net](https://www.jinteki.net/) — EN, основной клиент для NSG/Startup/Standard.

### Компаньоны / аксессуары
- [Gamefit: акриловые жетоны для Netrunner](https://gamefit.shop/ru/store/product/acrylic_tokens_for_android_netrunner) — RU/магазин.

### Комьюнити
- [Netrunner Online Events Hub (Discord invite)](https://discord.gg/EpWuadb) — EN, турниры/онлайн-события.
- [n1531 — печать нетраннера и другого PnP (VK)](https://vk.ru/n1531) — RU, самиздат/коллективная печать. *(с box HTTP 418 «I'm a teapot» / антибот; группа публичная — открывать в браузере/приложении VK.)*
- [NISEI: Что мы печатаем? (VK-статья n1531)](https://vk.com/@n1531-chto-my-pechataem) — RU; тот же антибот с box (418) — ссылка из прежних закладок/Tesera, вручную проверить.
- [Tesera: как начать или вернуться (2022)](https://tesera.ru/article/faq-netrunner/) — RU.
- [Tesera: State of Netrunner — май 2026](https://tesera.ru/article/2591649/) — RU.
- [netrunnercards.co.uk](https://netrunnercards.co.uk/) — EN, авторизованный реселлер (UK/EU shipping).

### Печать / прокси (легальный PnP от NSG)
- [From Zero to Netrunner PnP Hero (jbargu)](https://jbargu.github.io/en/post/print-and-play-netrunner/) — EN, практический гайд по печати **System Gateway** (NSG): бумага gsm, резка, скругление углов, жетоны, сравнение типографий; полезен рядом с официальными PnP PDF NSG.
- PDF PnP с сайта NSG (pay-what-you-want) — см. [Purchase Guide](https://nullsignal.games/players/purchase-guide/); карты, напечатанные так, легальны на турнирах при аккуратной нарезке и непрозрачных протекторах с «backing cards».
- Официальный пример printable sheets: [SystemGatewayEnglish-A4-Printable-Sheets-1x.pdf](https://nullsignal.games/wp-content/uploads/2023/07/SystemGatewayEnglish-A4-Printable-Sheets-1x.pdf).
- Русские зеркала / переводы: см. блок Tesera выше + группа [n1531](https://vk.ru/n1531).

---

## C. Community print / локальные тиражи (не издатель правил)

Отдельный блок, чтобы не путать с FFG и NSG как авторами карт/правил:
- **Null Signal / MPC / DriveThruCards / локальные реселлеры** — официальные каналы распространения *карт NSG* (см. Purchase Guide).
- **n1531 (VK)** — русскоязычная организация коллективной печати PnP NSG и переводов.
- **Tesera State of Netrunner (2026)** — каталог русских и EN зеркал PnP (Яндекс.Диск).


## Соло / solo

Официального соло-режима нет (ни у FFG, ни у NSG). Ниже — проверенные фан-автоматы и цифровые AI. **Разделение по эпохам** важно: часть вариантов заточена под FFG-кардпул, часть явно кросс-эра / под NSG.

### A. FFG-эра (настольные варианты)

- [RUNNING SOLO — an Android: Netrunner variant (BGG thread)](https://boardgamegeek.com/thread/922467/running-solo-an-android-netrunner-variant) — EN, классический фан-вариант Don Riddle (riddle13): играете Runner’ом против автоматизированной Corp (кубик + правила). Эпоха FFG; совместимость с поздним NSG-кардпулом **не заявлена автором** — считать FFG-ориентированным.
- [Running Solo Die Roll Reference Card (BGG PnP)](https://boardgamegeek.com/filepage/163641/running-solo-die-roll-reference-card) — EN, карманная шпаргалка по броскам кубика для Running Solo (API BGG подтвердил filepage; HTML часто 403 ботам — открывать в браузере).
- Другие ранние треды вроде «Cracking the Code» / «Stand Your Ground» встречаются на BGG как альтернативные соло-эксперименты эпохи FFG; перед игрой сверять актуальность и полноту правил на самих страницах.

### B. NSG / кросс-эра (автоматы и цифровые AI)

- [DASH — Automa for solo Android: Netrunner (BGG PnP)](https://boardgamegeek.com/filepage/287471/pnp-of-dash-an-automa-for-playing-android-netrunne) — EN, PnP-колода Dash + правила Corp-AI (Spiral Architect Games, 2024). Играете Runner’ом против любого Corp-дека. **Автор явно заявляет совместимость** с Android: Netrunner (FFG), NISEI/NSG и даже классическим Netrunner CCG — то есть подходит под оба ваших кардпула. ES-зеркало: [PnP de Dash (español)](https://boardgamegeek.com/filepage/287472/pnp-de-dash-un-automa-para-jugar-en-solitario-a-an).
- [Spiral Architect Games — Netrunner Automa](https://spiralarchitectgames.com/en/games/5/netrunner) — EN/ES, страница проекта DASH: описание механики, демо, доп. AI-паки / печать / браузерная версия.
- [Chiriboga](https://chiriboga.sifnt.net.au/) — EN, браузерный движок Android: Netrunner с AI-оппонентом ([GitHub bobtheuberfish/chiriboga](https://github.com/bobtheuberfish/chiriboga)); кардпул включает System Gateway / System Update 2021 (NSG) и туториалы.
- [Netrunner: Solo Mode (Chiriboga fork / DrBo6)](https://chiriboga.cronbach.com/) — EN, расширение Chiriboga: Quick/Custom/Gauntlet (roguelite), туториалы, precon’ы Gateway / NSG Core (+ Elevation в бете). Удобный цифровой соло под актуальный NSG-кардпул; см. также обсуждение на [r/Netrunner](https://www.reddit.com/r/Netrunner/comments/1q3w5nj/netrunner_solo_mode_versus_ai/).

**Практика:** для физического соло с вашими колодами FFG **и** NSG — начинать с **DASH**; для обучения/быстрых партий без раскладки стола — Chiriboga / Solo Mode. Running Solo — ностальгический/лёгкий FFG-вариант, если хочется «бумажного» AI без отдельной PnP-колоды автомата.

## Быстрый старт (практика 2026)

1. Правила и L2P: [NSG Learn to Play](https://nullsignal.games/players/learn-to-play/) + [L2P PDF](https://nullsignal.games/wp-content/uploads/2025/04/Learn-to-Play-v2.1.pdf) + [System Gateway](https://nullsignal.games/products/system-gateway/).
2. Первые «свои» колоды: [Sample Decklists](https://nullsignal.games/players/getting-started-sample-decklists/) (сначала Gateway-only, потом Core Sets) → копировать в [NetrunnerDB](https://netrunnerdb.com/).
3. Пошаговый декбилдинг по-русски: [Tesera Корп](https://tesera.ru/article/2110564/) + [Tesera Раннер](https://tesera.ru/article/2121958/).
4. Онлайн: [Jinteki.net](https://www.jinteki.net/).
5. RU-контекст / PnP: [Tesera FAQ](https://tesera.ru/article/faq-netrunner/) + [State of Netrunner 2026](https://tesera.ru/article/2591649/) + [VK Москва](https://vk.ru/netrunner_msk) / [n1531](https://vk.ru/n1531).
6. Если интересует именно **старый FFG-картон** — PDF Learn to Play / Rules Reference выше + Eternal/кухня на Jinteki; достать физику сложно и дорого.

### Что не удалось надёжно верифицировать с box (сентябрь 2026)
- Прямые HTML-страницы BGG filepage и часть boardgamegeek.com/boardgame/… — Cloudflare 403 ботам (каталог файлов подтверждён API).
- Wayback `web.archive.org/web/*/stimhack.com/*` — таймаут/нет ответа с box; сами stimhack.com статьи (new-players, enough-credit) открываются (200).
- VK n1531 и статья `@n1531-chto-my-pechataem` — HTTP 418 антибот; ссылки оставляем как публичные, проверять глазами.
- Reddit-треды (в т.ч. Kitara 600dpi / AI upscaling / Gateway reference sheets) — 403 ботам; URL подтверждены поисковым индексом / закладками — открывать в браузере.
- `www.jinteki.net` HEAD → 404; канон: [jinteki.net](https://jinteki.net/) (GET 200).
- Прямой PDF Universal Head на orderofgamers.com/rules/android_netrunner(_v2).pdf — 404; страница обзора жива.

