# CLI / TUI / GUI инструментарий (Windows)

Автономное **исследование** (13.11.2026): каталог на обзор, пробы и прореживание. Пока не смешивать с постоянными рабочими списками (`New_Windows` и др.) — отбор сюда, перенос в постоянную коллекцию только после личных тестов.

Ориентир: Windows 10/11 Pro x64, PowerShell, по возможности кроссплатформа. Не установка «всего сразу», а согласованная среда: поиск → навигация → Git → данные → sync/backup → GUI там, где визуальная проверка важнее.

**Статусы** (внутри этого файла)
- `[знакомо]` — уже встречалось / стоит где-то ещё; здесь всё равно держим карточку для сравнения
- `[кандидат]` — ещё не разбирал / не держал в постоянном наборе
- `[не OSS]` — бесплатно или freemium, но не open source; оставить осознанно

URL без трекеров. После личных проб — сокращать TOP и помечать `проверено: ДД.ММ.ГГГГ`.

---

## Принцип связок

| Сценарий | Связка |
|---|---|
| Поиск в коде/доках | `rg` (+ `rga` для PDF) → `fzf` → правки `sd` / dnGrep |
| Файлы в терминале | `fd` + `Yazi` + `zoxide` |
| Git | `lazygit` + `delta` (+ SourceGit/Gittyup GUI) |
| Данные | DuckDB / VisiData / `jq`/`yq` / Harlequin |
| Перенос | Syncthing (живое) · rclone/rsync (пакетно) · restic/Kopia (снимки) |
| Воспроизводимость машины | `chezmoi` + `just` + `uv`/`Pixi` + winget/Scoop |

Важно: **синхронизация ≠ бэкап**. `rclone sync` умеет удалять лишнее на приёмнике — сначала `--dry-run`; версии — через restic/Kopia.

---

## 1. Синхронизация, передача, бэкап

| Инструмент | UI | Статус | Заметка |
|---|---|---|---|
| [Syncthing](https://syncthing.net/) | Web GUI | `[знакомо]` | P2P sync своих машин; уже отмечен как полезный ранее |
| [rclone](https://rclone.org/) | CLI (+ эксп. GUI) | `[знакомо]` | Облака, SFTP, S3; + WinFsp для mount |
| [WinFsp](https://winfsp.dev/) | драйвер | `[знакомо]` | Нужен для `rclone mount` |
| [rsync](https://rsync.samba.org/) | CLI | `[кандидат]` | Через MSYS2; инкремент/дельта по SSH |
| [FreeFileSync](https://freefilesync.org/) | GUI | `[кандидат]` | Визуальное сравнение каталогов, зеркало |
| [restic](https://restic.net/) | CLI | `[кандидат]` | Снимки, дедуп, шифрование |
| [Kopia](https://kopia.io/) / KopiaUI | GUI+CLI | `[кандидат]` | Бэкап со снимками и расписанием |
| [WinSCP](https://winscp.net/) | GUI+CLI | `[знакомо]` | SFTP/SCP |
| [LocalSend](https://localsend.org/) | GUI | `[кандидат]` | Файлы по LAN без облака |
| [aria2](https://github.com/aria2/aria2) | CLI | `[кандидат]` | Многопоточные загрузки |

Предвыбор из обзора: `Syncthing` + `rclone` + `FreeFileSync` + `restic` (или Kopia).

---

## 2. Поиск, regex, массовые правки

| Инструмент | UI | Статус | Заметка |
|---|---|---|---|
| [ripgrep](https://github.com/BurntSushi/ripgrep) (`rg`) | CLI | `[знакомо]` | winget `BurntSushi.ripgrep.MSVC` |
| [ripgrep-all](https://github.com/phiresky/ripgrep-all) (`rga`) | CLI | `[кандидат]` | `rg` + PDF/DOCX/EPUB/ZIP/SQLite |
| [dnGrep](https://dngrep.github.io/) | GUI | `[знакомо]` | Regex, превью, Undo; сильный Windows GUI |
| [grepWin](https://github.com/stefankueng/grepWin) | GUI | `[кандидат]` | Компактный поиск/замена |
| [fd](https://github.com/sharkdp/fd) | CLI | `[кандидат]` | Поиск файлов по имени (удобнее `find`) |
| [fzf](https://github.com/junegunn/fzf) | TUI | `[кандидат]` | Fuzzy-отбор из любого списка |
| [sd](https://github.com/chmln/sd) | CLI | `[кандидат]` | Удобные regex-замены вместо `sed` |
| [ast-grep](https://github.com/ast-grep/ast-grep) | CLI | `[кандидат]` | Поиск/правка по AST кода |
| [Everything](https://www.voidtools.com/) | GUI | `[знакомо]` / `[не OSS]` | Мгновенный поиск по имени; не замена `rg` |

Примеры `rg` (PowerShell):

```powershell
rg -n 'TODO|FIXME' . -g '*.rs' -g '*.py'
rg -n 'Уравнение\s*\([0-9]+\.[0-9]+\)' . -g '*.tex'
rg -n -P '(?<=\bversion=)[0-9.]+' .   # PCRE2 lookbehind, если сборка с -P
rg --files | fzf
```

---

## 3. Современный CLI / TUI «ежедневник»

| Утилита | Зачем | Статус | ★ |
|---|---|---|---|
| [bat](https://github.com/sharkdp/bat) | `cat` с подсветкой и git-маркерами | `[кандидат]` | ★★★ |
| [eza](https://github.com/eza-community/eza) | современный `ls` / деревья / git | `[кандидат]` | ★★ |
| [delta](https://github.com/dandavison/delta) | `git diff` side-by-side | `[кандидат]` | ★★★ |
| [lazygit](https://github.com/jesseduffield/lazygit) | Git TUI | `[знакомо]` | ★★★ |
| [gitui](https://github.com/gitui-org/gitui) | Git TUI (Rust) | `[знакомо]` | ★★ |
| [Yazi](https://yazi-rs.github.io/) | файловый TUI + превью | `[знакомо]` | ★★★ |
| [zoxide](https://github.com/ajeetdsouza/zoxide) | умный `cd` | `[кандидат]` | ★★★ |
| [jq](https://jqlang.github.io/jq/) / [yq](https://mikefarah.github.io/yq/) | JSON / YAML | `[кандидат]` (jq местами в DS) | ★★★ |
| [dust](https://github.com/bootandy/dust) / [duf](https://github.com/muesli/duf) | диск: занято / свободно | `[кандидат]` | ★★ |
| [bottom](https://github.com/ClementTsang/bottom) | монитор ресурсов | `[кандидат]` | ★★ |
| [btop4win](https://github.com/aristocratos/btop4win) | монитор (знакомый монитор) | `[знакомо]` | ★★ |
| [hyperfine](https://github.com/sharkdp/hyperfine) | бенч команд | `[кандидат]` | ★★★ |
| [watchexec](https://github.com/watchexec/watchexec) | rerun при изменении файлов | `[кандидат]` | ★★★ |
| [gsudo](https://github.com/gerardog/gsudo) | `sudo` через UAC | `[кандидат]` | ★★ |
| [Difftastic](https://github.com/wilfred/difftastic) | diff по синтаксису | `[кандидат]` | ★★★ |
| [Glow](https://github.com/charmbracelet/glow) | Markdown в терминале | `[кандидат]` | ★★ |
| [Atuin](https://atuin.sh/) | история команд | `[кандидат]` | ★★ |
| [tealdeer](https://github.com/tealdeer-rs/tealdeer) | короткие примеры (tldr) | `[кандидат]` | ★★ |
| [mprocs](https://github.com/Rundfunk/mprocs) | несколько процессов в панелях | `[кандидат]` | ★★ |
| [jnv](https://github.com/ynqa/jnv) | интерактивный jq | `[кандидат]` | ★★★ |
| [Microsoft Coreutils](https://github.com/microsoft/coreutils) | preview Unix-утилит | `[кандидат]` | ★ — только эксперименты |

Связки: `lazygit + delta`; `Yazi + rg + fzf`.

---

## 4. Git GUI (отдельный ряд GUI)

| Инструмент | Статус | Заметка |
|---|---|---|
| [SourceGit](https://sourcegit-scm.github.io/) | `[знакомо]` | OSS vs SmartGit |
| [Gittyup](https://murmele.github.io/Gittyup/) | `[знакомо]` | История, line staging |
| [git-cola](https://git-cola.github.io/) | `[знакомо]` | Лёгкий staging/DAG |
| [Git Extensions](https://gitextensions.github.io/) | `[знакомо]` (упомянут) | Windows power-user |
| [TortoiseGit](https://tortoisegit.org/) | `[знакомо]` (упомянут) | Из Проводника |
| SmartGit / SourceTree / Tower | `[знакомо]` платные в чеклисте | Оставить как эталон сравнения |

---

## 5. Данные, наука, SQL

| Инструмент | Статус | Заметка |
|---|---|---|
| [DuckDB](https://duckdb.org/) | `[знакомо]` | CLI/SQL по CSV/Parquet; знакомо из DS-заметок |
| [Harlequin](https://harlequin.sh/) | `[знакомо]` | SQL IDE в терминале |
| [VisiData](https://www.visidata.org/) | `[знакомо]` | Таблицы в TUI; на Win часто WSL/MSYS Python |
| [Nushell](https://www.nushell.sh/) | `[кандидат]` | Табличный пайплайн вместо текста |
| [qsv](https://github.com/jqnatividad/qsv) | `[кандидат]` | Быстрый CSV |
| [Miller](https://miller.readthedocs.io/) (`mlr`) | `[кандидат]` | awk/sed/cut для CSV/JSON |
| [uv](https://docs.astral.sh/uv/) | `[знакомо]` | Python env; знакомый стек Python |
| [Pixi](https://prefix.dev/) | `[кандидат]` | Воспроизводимые conda-like env |
| [DB Browser for SQLite](https://sqlitebrowser.org/) | `[кандидат]` | GUI SQLite |
| [DBeaver](https://dbeaver.io/) | `[знакомо]` | в старых списках ПО |
| [lazysql](https://github.com/jorgerojas26/lazysql) | `[кандидат]` | SQL TUI; проверить телеметрию в релизах |
| [Orange](https://orangedatamining.com/) | `[кандидат]` | Visual data mining |
| [jamovi](https://www.jamovi.org/) / [JASP](https://jasp-stats.org/) | `[кандидат]` | Статистика GUI |
| [Veusz](https://veusz.github.io/) | `[кандидат]` | Научные графики |
| [Gephi](https://gephi.org/) | `[кандидат]` | Графы |
| [Protégé](https://protege.stanford.edu/) | `[кандидат]` | OWL-онтологии |
| [JabRef](https://www.jabref.org/) / [Zotero](https://www.zotero.org/) | `[кандидат]` | Библиография |
| [Euporie](https://github.com/joouha/euporie) | `[кандидат]` | Jupyter в терминале |

---

## 6. Автоматизация проекта и воспроизводимость

| Инструмент | Статус | Заметка |
|---|---|---|
| [just](https://just.systems/) | `[кандидат]` | Команды проекта в `justfile` (не Make) |
| [Task](https://taskfile.dev/) | `[кандидат]` | YAML task runner |
| [Ruff](https://github.com/astral-sh/ruff) | `[кандидат]` | Python lint/format |
| [ty](https://github.com/astral-sh/ty) | `[кандидат]` | Быстрая проверка типов Python |
| [Lefthook](https://github.com/evilmartians/lefthook) | `[кандидат]` | Git hooks |
| [git-cliff](https://github.com/orhun/git-cliff) | `[кандидат]` | Changelog из коммитов |
| [actionlint](https://github.com/rhysd/actionlint) | `[кандидат]` | Проверка GitHub Actions |
| [chezmoi](https://www.chezmoi.io/) | `[кандидат]` | Dotfiles / конфиги между машинами |
| [watchexec](https://github.com/watchexec/watchexec) | `[кандидат]` | См. §3 |

Стек «новая машина»: `chezmoi + just + uv/Pixi + winget|Scoop`.

---

## 7. Сеть, HTTP, диагностика

| Инструмент | Статус | Заметка |
|---|---|---|
| [Trippy](https://trippy.rs/) | `[кандидат]` | traceroute+ping TUI |
| [xh](https://github.com/ducaale/xh) | `[кандидат]` | Удобный HTTP CLI |
| [Posting](https://posting.sh/) | `[кандидат]` | Postman-like TUI (beta) |
| [Bruno](https://www.usebruno.com/) | `[кандидат]` | API-клиент, коллекции в Git |
| [oha](https://github.com/hatoo/oha) / [Vegeta](https://github.com/tsenart/vegeta) | `[кандидат]` | HTTP load |
| [mitmproxy](https://mitmproxy.org/) | `[знакомо]` | В знакомо из DS-заметок |
| [Nmap](https://nmap.org/) | `[кандидат]` | Только свои/разрешённые хосты |
| [Wireshark](https://www.wireshark.org/) / TShark | `[знакомо]` | знакомо; есть заметка wireshark |
| [dnslookup](https://github.com/ameshkov/dnslookup) / [q](https://github.com/natesales/q) | `[кандидат]` | DNS / DoH |
| [Angry IP Scanner](https://angryip.org/) | `[кандидат]` | Скан LAN |
| [RustDesk](https://rustdesk.com/) | `[знакомо]` | (есть отдельная заметка по self-host) |
| [HTTP Toolkit](https://httptoolkit.com/) | `[кандидат]` / open core | GUI HTTP debug |
| Proxifier | `[не OSS]` | Только если системного прокси мало |

---

## 8. Секреты, зависимости, CI security

| Инструмент | Статус | Заметка |
|---|---|---|
| [Betterleaks](https://github.com/betterleaks/betterleaks) | `[кандидат]` | Секреты в репо/истории (наследник Gitleaks) |
| [zizmor](https://github.com/zizmorcore/zizmor) | `[кандидат]` | Аудит GitHub Actions |
| [OSV-Scanner](https://google.github.io/osv-scanner/) | `[кандидат]` | CVE в зависимостях |
| [Syft](https://github.com/anchore/syft) / [Grype](https://github.com/anchore/grype) | `[кандидат]` | SBOM + уязвимости |
| [cargo-audit](https://github.com/RustSec/rustsec) | `[кандидат]` | Rust deps |
| [age](https://github.com/FiloSottile/age) | `[кандидат]` | Шифрование файлов |
| [SOPS](https://getsops.io/) | `[кандидат]` | Шифрование полей в YAML/JSON |

Перед публикацией: `betterleaks` → `osv-scanner` → `zizmor` на workflows.

---

## 9. Документы, PDF, графика, видео (CLI + GUI)

| Инструмент | Статус | Заметка |
|---|---|---|
| [Pandoc](https://pandoc.org/) | `[знакомо]` | Часто в DS/LaTeX заметках |
| [Typst](https://typst.app/) | `[кандидат]` | CLI вёрстки |
| [pdfcpu](https://pdfcpu.io/) / [qpdf](https://qpdf.readthedocs.io/) | `[кандидат]` | Validate/transform PDF |
| [D2](https://d2lang.com/) / [Graphviz](https://graphviz.org/) / [Mermaid CLI](https://github.com/mermaid-js/mermaid-cli) | `[кандидат]` | Диаграммы из текста |
| [ImageMagick](https://imagemagick.org/) | `[знакомо]` | уже в ходу |
| [FFmpeg](https://ffmpeg.org/) | `[знакомо]` | уже в ходу |
| [ExifTool](https://exiftool.org/) | `[кандидат]` | Метаданные |
| [yt-dlp](https://github.com/yt-dlp/yt-dlp) | `[знакомо]` | знакомо из DS-заметок; Tartube — GUI |
| [PDF24 Creator](https://tools.pdf24.org/en/creator) | `[кандидат]` / бесплатный | Локальные PDF-операции |
| [NAPS2](https://www.naps2.com/) | `[кандидат]` | Скан + OCR → PDF |
| [Stirling PDF](https://stirlingpdf.com/) | `[кандидат]` | Набор PDF-операций |
| [SumatraPDF](https://www.sumatrapdfreader.org/) | `[кандидат]` | Быстрый просмотр |
| [PDFsam](https://pdfsam.org/) | `[знакомо]` | знакомый OSS PDF |
| [ScreenToGif](https://www.screentogif.com/) | `[кандидат]` | Запись → GIF |
| [LosslessCut](https://losslesscut.app/) | `[кандидат]` | Нарезка без перекодирования |
| [OBS](https://obsproject.com/) / [ShareX](https://getsharex.com/) | `[знакомо]` | знакомый захват/запись |
| [digiKam](https://www.digikam.org/) / [Inkscape](https://inkscape.org/) | `[знакомо]` digiKam; Inkscape — `[кандидат]` | Фото / SVG |
| [diagrams.net](https://www.drawio.com/) Desktop | `[кандидат]` | Схемы |
| [HandBrake](https://handbrake.fr/) | `[знакомо]` | Перекодирование |

---

## 10. GUI «улучшают Windows каждый день»

| Инструмент | Статус | Заметка |
|---|---|---|
| [Flow Launcher](https://www.flowlauncher.com/) | `[знакомо]` | лаунчер |
| [PowerToys](https://learn.microsoft.com/windows/powertoys/) | `[знакомо]` | Tools; PowerRename и др. |
| [UniGetUI](https://www.marticliment.com/unigetui/) | `[кандидат]` | GUI над winget/Scoop/choco; только официальный сайт |
| [CopyQ](https://hluk.github.io/CopyQ/) | `[кандидат]` | Буфер обмена с историей |
| [QuickLook](https://github.com/QL-Win/QuickLook) | `[кандидат]` | Превью по Space |
| [AltSnap](https://github.com/RamonUnch/AltSnap) | `[кандидат]` | Окна без рамки |
| [Twinkle Tray](https://github.com/xanderfrangos/twinkle-tray) | `[кандидат]` | Яркость мониторов |
| [Auto Dark Mode](https://github.com/AutoDarkMode/Windows-Auto-Night-Mode) | `[кандидат]` | Светлая/тёмная тема |
| [PixPin](https://pixpinapp.com/) | `[кандидат]` / freemium | Скриншоты; сравнить с ShareX |
| [DevToys](https://devtoys.app/) | `[кандидат]` | JSON/regex/Base64 «швейцарский нож» |
| [ImHex](https://imhex.werwolv.net/) | `[кандидат]` | Hex + структуры |
| [WinMerge](https://winmerge.org/) | `[кандидат]` | Diff файлов/каталогов |
| [Double Commander](https://doublecmd.sourceforge.io/) | `[кандидат]` | 2-панельный FM vs Total Commander |
| [klogg](https://github.com/variar/klogg) | `[кандидат]` | Большие логи (рядом с другими log viewers) |
| [Czkawka](https://czkawka.com/) / Krokiet | `[знакомо]` | Дубликаты |
| [WizTree](https://diskanalyzer.com/) | `[не OSS]` (free personal) | Карта диска |
| [SquirrelDisk](https://github.com/adileo/squirreldisk) | `[кандидат]` | OSS анализатор диска |
| [Bulk Crap Uninstaller](https://www.bcuninstaller.com/) | `[кандидат]` | Массовое удаление |
| [OpenHashTab](https://github.com/namazso/OpenHashTab) | `[кандидат]` | Хеши в свойствах файла |
| [CrystalDiskInfo](https://crystalmark.info/en/software/crystaldiskinfo/) | `[кандидат]` (Mark рядом есть) | SMART |
| [Sandboxie Plus](https://sandboxie-plus.com/) | `[кандидат]` | Песочницы |
| [7-Zip](https://www.7-zip.org/) | `[кандидат]` / де-факто стандарт | Архивы |
| [Rufus](https://rufus.ie/) | `[знакомо]` | bootable USB |
| [Sysinternals](https://learn.microsoft.com/sysinternals/) | `[не OSS]` в целом | Procmon / Process Explorer — must для диагностики |

---

## Приоритетные короткие списки (на прореживание)

### A. Поставить / проверить первыми (инженерный минимум)

1. ripgrep, fd, fzf, bat — уже частично есть `rg`
2. dnGrep
3. lazygit + delta
4. Yazi + zoxide
5. jq + yq (+ jnv)
6. Syncthing + rclone (+ restic или Kopia)
7. FreeFileSync
8. Everything `[не OSS]` + WinMerge
9. DuckDB (+ Harlequin/VisiData — уже есть)
10. just + chezmoi
11. SourceGit / Gittyup (уже вписаны)
12. PowerToys + Flow Launcher (есть)
13. DevToys, ImHex
14. Betterleaks + osv-scanner (перед публичными репо)
15. Trippy + xh (сеть)

### B. winget «быстрый старт» (проверить `winget show` перед установкой)

```powershell
winget install -e --id BurntSushi.ripgrep.MSVC
winget install -e --id sharkdp.fd
winget install -e --id junegunn.fzf
winget install -e --id sharkdp.bat
winget install -e --id dnGrep.dnGrep
winget install -e --id Microsoft.PowerToys
```

---

## Журнал прореживания

| Дата | Что оставил / выкинул | Почему |
|---|---|---|
| 13.11.2026 | Каталог создан | Сводка из обзора CLI/TUI/GUI; файл автономный, без правок и выноса из New_Windows |
|  |  |  |

После каждой волны тестов — одна строка в таблицу и правка ★ / статусов выше.