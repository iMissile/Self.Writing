# Warhammer 40,000: Conquest

Дуэльный LCG (FFG + Games Workshop license). Линия официально закрыта; сообщество поддерживает игру, есть **Apoka Team** (фан-дополнения), современные декбилдеры и онлайн.

Черновик был пустым. Закладка: [ConquestDB](https://conquestdb.com/).

---

## Правила / обучение
- [Rulebook (PDF, 1jour-1jeu mirror)](https://cdn.1j1ju.com/medias/6f/8c/76-warhammer-40-000-conquest-rulebook.pdf) — EN.
- [FAQ / Rules Reference (PDF, FFG CDN)](https://images-cdn.fantasyflightgames.com/filer_public/ff/a9/ffa9a7d3-5dd0-4ad0-932f-ead08fa360ba/whk_faq_20.pdf) — EN.
- На [ConquestDB](https://conquestdb.com/) и [Iridial](https://www.iridial.net/) есть ссылки на FFG Rules Reference и видео-туториалы (Hive Tyrant и др.).
- [Apoka + expansions rules collection](https://apoka40k.weebly.com/) — EN, правила фан-сетов Apoka (ссылка с ConquestDB).

## Обзоры
- [Noble Knight: Warhammer Conquest overview](https://play.nobleknight.com/warhammer-conquest-and-the-best-complete-living-card-games/) — EN.
- [BGG: Warhammer 40,000: Conquest](https://boardgamegeek.com/boardgame/156858/warhammer-40000-conquest) — EN.
- [r/warhammerconquest](https://www.reddit.com/r/warhammerconquest/) — EN, главный Reddit-хаб.

## Базы карт / колодостроение
- [ConquestDB](https://conquestdb.com/) — EN, **актуальный** декбилдер/база (FFG + Apoka); публичные деклисты, поиск, card printout; экспорт в **TTS** и **Iridial** (API import с v1.9.5); импорт из CardGameDB / сырого текста (из закладок). Проверено 200.
- [ConquestDB — Decks](https://conquestdb.com/decks/) — EN, create / import / published decks.
- [ConquestDB GitHub (site)](https://github.com/C-C-Coalback/Conquest-LCG-Site) / [Deckbuilder repo](https://github.com/C-C-Coalback/Conquest-LCG-Deckbuilder) — исходники.
- [Iridial](https://www.iridial.net/) — EN, браузерный клиент (игра); колоды удобно тянуть из ConquestDB. Проверено 200.
- [CardPlace.ru: Warhammer Conquest](https://www.cardplace.ru/directory/new_search/Warhammer%20Conquest/all/1) — RU, каталог/поиск карт (из закладок; проверено 200) — справочник, не полноценный декбилдер.
- [rgmc4/warhammer_40K_conquest_card_data](https://github.com/rgmc4/warhammer_40K_conquest_card_data) — EN, **card data** (OCTGN→JSON/CSV + Apoka/Black Crusade); **не** image-сканы. Источник каталога для Proxy Nexus `whconquest`.
- Исторический **CardGameDB** — мёртв; [Wayback calendar](https://web.archive.org/web/*/http://www.cardgamedb.com/); форумы: [snapshot 2017-01-10](https://web.archive.org/web/20170110003503/http://www.cardgamedb.com/forums/). ConquestDB умеет импортировать старые листы оттуда.

## Онлайн-игра
- [Iridial](https://www.iridial.net/) — EN, браузерный клиент; поддержка FFG и Apoka; Discord упоминается на сайте без публичной ссылки.
- [TTS mod (Steam Workshop)](https://steamcommunity.com/sharedfiles/filedetails/?id=2471847304) — EN, Tabletop Simulator, hi-res FFG + Apoka (из Reddit-треда сообщества).
- [TTS Complete Edition HQ (vanilla FFG, final)](https://steamcommunity.com/sharedfiles/filedetails/?id=2345148868) — EN, near-4k сканы FFG без Apoka; автор указывает наследника `2471847304` выше. Проверено 200.
- **Как пользоваться (TTS):** подписаться на [RELOADED / Scripted](https://steamcommunity.com/sharedfiles/filedetails/?id=2471847304) (рекомендуется; HQ-сканы из Complete Edition уже внутри + Apoka + скрипты) или на [Complete Edition HQ](https://steamcommunity.com/sharedfiles/filedetails/?id=2345148868) (vanilla FFG, final, без скриптов). Перезапустить TTS → **Games → Workshop** → открыть мод → **Host** (или Join по приглашению). Колоды: стартеры на столе; книги-контейнеры по краям стола (поиск карты → вытащить → собрать колоду → ПКМ Save Object); либо Deck Key с [ConquestDB](https://conquestdb.com/) в поле импорта мода. **Скрипты RELOADED:** варлорд+колода в зоны HQ → кубик на Initiative → выбрать Sector → кнопка Red/Blue цвета игрока с Initiative → **Warlord Setup** → в Command Phase кнопки у планет (только если выиграли struggle) → **End Round**. Gotchas: Scripting ON у хоста; гости тоже подписаны на тот же мод; импортированный варлорд — заменить настольной копией или в Description `{ "Resource":X, "Card":X }`; dials в HQ Complete — цифрами 1–0 на тайлах; Traxis Sector мёртв → ConquestDB; 2v2 отдельный мод [2886614434](https://steamcommunity.com/sharedfiles/filedetails/?id=2886614434). Discord: [gGX4WmPwVu](https://discord.gg/gGX4WmPwVu) / [Warlords zvUe4HG](https://discord.com/invite/zvUe4HG).

## Сканы карт / прокси-изображения

### Google Drive — полный pack-архив (найдено пользователем)
- **[Google Drive — Warhammer 40k Conquest (COMPLETE)](https://drive.google.com/drive/folders/1So4TqKTDvaIJV3rtn6pYuHSHvk2VtOh9)** — публичная папка сканов FFG (title страницы Drive: «Warhammer 40k Conquest (COMPLETE)»). **Нашёл пользователь после Discord-охоты** (сервер WH40K Conquest / pinned Drive); tracking-параметры (`usp=…`) сняты. Проверено: listing открывается без логина (HTTP 200, сент. 2026 MSK).
- По описанию в [Proxy Nexus whconquest renamer README](https://github.com/axmccx/proxynexus-rs/blob/master/utils/image_file_renamers/whconquest/README.md) это **pack-архив**: bleed-cut под MPC, ~**300 dpi**, раскладка «папка на пак» (иногда cycle → pack → Warlords/Planets). В корне — `bleed_40k Back.png`.
- **Не путать с «faction archive»** (SortedConquestImages из TTS, ~575 dpi по фракциям) — тот по README всё ещё **shared на Conquest Discord**, публичного folder ID в том README нет.
- Несмотря на имя COMPLETE, **pack-архив неполный**: README Nexus прямо пишет, что **семь карт отсутствуют** в нём (все есть в faction archive). Список имён ниже — из отчёта в Reddit-треде Proxy Nexus / комментариев к обновлению (см. Proxy Nexus); **метаданные** этих семи карт в data-репо **есть**.

**Заявленные MISSING scans в COMPLETE pack-архиве (данные карт ≠ сканы):**

| Сет | Карта | # |
|---|---|---|
| Core Set | Raid | 118 |
| Core Set | Altar of Torment | 121 |
| Core Set | Twisted Laboratory | 122 |
| Core Set | Doom | 141 |
| Core Set | Experimental Devilfish | 161 |
| Searching For Truth | Shrieking Exarch | 81 |
| The Great Devourer | Dark Cunning | 38 |

Проверка **card data** (не изображений): все 7 есть в [rgmc4/warhammer_40K_conquest_card_data `all_cards.csv`](https://github.com/rgmc4/warhammer_40K_conquest_card_data) и в встроенном каталоге Nexus `whc_cards.json`. Поштучный listing файлов внутри Drive API с box **не удался** (first-party key / 400) — наличие/отсутствие JPEG именно в этой папке глазами не перечислено; опора на README Nexus («seven cards are missing») + список из Reddit/пользователя.

### Proxy Nexus (теперь с Conquest)
- [Proxy Nexus](https://proxynexus.net/) — EN, printable PDF / MPC ZIP из списка карт / сета / (где есть) decklist URL. **Warhammer 40k Conquest поддержан** (`game_id`: `whconquest`; адаптер в [proxynexus-rs](https://github.com/axmccx/proxynexus-rs), коммит «add support for warhammer 40k conquest», 2026-08-31).
- Каталог карт **не API FFG**, а JSON из [rgmc4/warhammer_40K_conquest_card_data](https://github.com/rgmc4/warhammer_40K_conquest_card_data) (OCTGN XML → JSON + ручные дополнения; **официальные FFG + фан Black Crusade / Apoka**). Это **card data / OCTGN**, **не** репозиторий image-сканов. Renamer README Nexus явно строит `whc_cards.json` / `whc_packs.json` из этого репо — практический «trust» источника данных автором Nexus (axmccx).
- Обновление / контекст: [r/Netrunner — Proxy Nexus Update 2026-08-28](https://www.reddit.com/r/Netrunner/comments/1w19fdm/proxy_nexus_update_20260828/) (автор **u/axmccx**); параллельный пост с LOTR-нотами: [r/lotrlcg — Proxy Nexus Update](https://www.reddit.com/r/lotrlcg/comments/1w19hx2/proxy_nexus_update/). HTML Reddit с box часто 403 — открывать в браузере. В треде пользовательский интерес к Conquest; поддержка Conquest в коде появилась сразу после (см. коммит выше).
- Поддерживаемые игры в `proxynexus-core/src/games/` (на момент проверки master): Netrunner, Netrunner Reboot, L5R, AGOT (+1st), LotR LCG, Arkham Horror LCG, Call of Cthulhu LCG, Marvel Champions, **WH Conquest**, WH Invasion. Decklist URL — не у всех (у Conquest в `get_decklist_adapter` **нет** провайдера → только card list / set).
- Сканы для web-коллекции Nexus собираются из архивов выше через CLI renamer; web app **не** подтягивает картинки с ConquestDB.

### Discord (по-прежнему вход к faction/hi-rez архиву)
- **Живой инвайт (проверен Discord API 2026-09-29):** [discord.gg/gGX4WmPwVu](https://discord.gg/gGX4WmPwVu) — сервер **«WH40K Conquest»** (guild 343342901176041472, ~814 members), инвайтер **cornholio1992** (автор TTS HQ Complete Edition). Не истекает. Faction archive / hi-rez pinned Drive historically жили здесь; публичный COMPLETE pack Drive выше — отдельная находка пользователя.
- **Мёртвые инвайты:** discord.gg/rSTGkarT (из [11xr6fp](https://www.reddit.com/r/warhammerconquest/comments/11xr6fp/discord_link_and_hirez_scans_for_printing/) / [1118asl](https://www.reddit.com/r/warhammerconquest/comments/1118asl/looking_for_high_quality_scans/)) — API Unknown Invite; discord.gg/mfvCzD8X (Steam comments) — тоже Unknown Invite.

### Индексы / указатели
- [Reddit: Looking for High Quality Scans](https://www.reddit.com/r/warhammerconquest/comments/1118asl/looking_for_high_quality_scans/) — EN: TTS assets + Discord pinned Drive.
- [Reddit: Discord link and hi-rez scans for printing](https://www.reddit.com/r/warhammerconquest/comments/11xr6fp/discord_link_and_hirez_scans_for_printing/) — EN; старый инвайт мёртв → gGX4WmPwVu.
- [Reddit: Proxy of original sets](https://www.reddit.com/r/warhammerconquest/comments/nkhk8l/proxy_of_original_sets/) — EN; LepcisMagna **не** публиковал Conquest Drive.
- [Winter 2014 Promos @600dpi](https://www.reddit.com/r/warhammerconquest/comments/2kii52/winter_2014_promos_at_600dpi/) — точечный imgur промо.

### Практика печати / альтернативы
- [TTS Complete Edition HQ (vanilla FFG)](https://steamcommunity.com/sharedfiles/filedetails/?id=2345148868) / наследник [2471847304](https://steamcommunity.com/sharedfiles/filedetails/?id=2471847304) — near-4k сканы в файлах мода; источник faction-архива по README Nexus.
- [ConquestDB](https://conquestdb.com/) — **card printout** (точечная печать / справочные изображения сайта, не bulk 600dpi-архив). Ajax-поиск карт с box без CSRF не разобран — статус картинок именно семи missing **не верифицирован** через ConquestDB API.
- [Apoka HQ (weebly)](https://apoka40k.weebly.com/) — Print / Buy / Proxies фан-сетов.
- [Apoka — Release Plan / hi-res pics](https://apoka.mozello.com/) — hi-res под печать **фан-паков** Apoka.
- [Apoka — Proxy](https://apoka.mozello.com/cards/proxy/) / [Print & Play how-to](https://apoka.mozello.com/cards/print--play).
- [CardPlace.ru: Warhammer Conquest](https://www.cardplace.ru/directory/new_search/Warhammer%20Conquest/all/1) — RU каталог (справочно).
- [Flickr: Conquest Cards DB](https://www.flickr.com/photos/conquest40k/collections) — просмотр карт, не 600dpi bulk download.

### Архив deep-pass 2026-09-29 (до находки Drive)
До пользовательской находки публичный folder ID в открытом вебе **не находился** (Discord-only). Таблица авеню того прогона сохранена в git-истории / предыдущем `.bak`; вывод «публичного Drive нет» **снят** — актуальный URL выше.


## Комьюнити
- [r/warhammerconquest](https://www.reddit.com/r/warhammerconquest/) — EN; оттуда же ищут Discord («Warlords of Conquest» и др. — инвайты ротируются).
- [Apoka HQ](https://apoka40k.weebly.com/) — EN.


## Соло / solo

Официального соло у FFG не было (дуэльный LCG). **Пробела в сообществе нет** — на BGG лежит несколько рабочих фан-автоматов / solo rules (подтверждены через BGG Files API; HTML filepage часто 403 ботам — открывать в браузере).

- [Easy solo rules (BGG PnP)](https://boardgamegeek.com/filepage/148350/easy-solo-rules) — EN, лёгкий вариант (структурированные правила Andy Dunks + правки): мало оверхеда, без лишних компонентов; часто рекомендуют в [треде «Best solo mode???»](https://boardgamegeek.com/thread/2926672/best-solo-mode).
- [SOLO RULES v2.0 (BGG PnP)](https://boardgamegeek.com/filepage/108986/solo-rules-v20-02-10-15) — EN (Painted Goblin / Chris Alton и эволюция): более «умный» AI для теста колод; берите **верхний** файл v2.0, ранние версии помечены outdated.
- [The Quest-o-matic — solitaire variant (BGG PnP)](https://boardgamegeek.com/filepage/149189/the-quest-o-matic-a-solitaire-variant-for-warhamme) — EN, попытка ближе имитировать человека; чуть больше учёта (удобны наборы d10).
- [IA Warhammer Conquest pour partie solo (BGG)](https://boardgamegeek.com/filepage/113252/ia-warhammer-conquest-pour-partie-solo) — FR, большой пакет Thierry (много версий, учёт расширений / Apoka); DE-перевод: [Solo Bot (Deutsche Übersetzung)](https://boardgamegeek.com/filepage/235861/solo-bot-deutsche-ubersetzung).

**Итог:** для быстрого старта — **Easy solo rules**; если нужен жёстче/богаче AI — SOLO RULES v2.0 или французский пакет Thierry. Онлайн-дуэль по-прежнему через Iridial / TTS (см. выше).

## Непроверено
- Постоянный Discord-invite «Warlords of Conquest» / Apoka (инвайты в старых Reddit-постах часто истекают) — брать свежую ссылку с r/warhammerconquest / Iridial / Apoka HQ.
- Faction archive (SortedConquestImages / ~575 dpi) — публичный folder ID по-прежнему **не извлечён**; вход через Discord gGX4WmPwVu. Pack COMPLETE Drive выше — ~300 dpi и с 7 missing scans (см. таблицу).
- Поштучная проверка JPEG семи missing внутри Drive 1So4… с box не сделана (Drive API first-party); сверять глазами / faction archive.
- Полный текст комментария u/axmccx в Reddit 1w19fdm про «trust» rgmc4 — HTML Reddit с box 403; доверие подтверждено кодом/README Nexus (каталог из того репо), не дословной цитатой комментария.
- Статус второго онлайн-клиента, если упоминается рядом с Iridial — уточнять на Reddit.
