# Обслуживание и диагностика MiKTeX (Windows)

Практическая памятка по типовым проблемам обновления MiKTeX, пересборки форматов и работы современных пакетов (`koma-script`, `marginnote`, `l3kernel`, `ltxbase`) на Windows.

Связанный скрипт автоматизации в этом каталоге: [miktex_repair.ps1](miktex_repair.ps1).

---

## 1. Симптом: «Обновлений нет», но компилятор работает на старом ядре LaTeX2e

### Как проявляется
- `miktex packages check-update` отвечает: `There are currently no updates available.`
- При компиляции свежих пакетов возникают ошибки несовместимости с ядром:
  - `koma-script` v3.49+ (`scrartcl`, `scrreprt`, `scrbook`):
    ```text
    ! Undefined control sequence.
    l.6936 \IfDocumentMetadataT
    ```
  - `marginnote` (2026+):
    ```text
    ! You can't use `\relax' after \the.
    <recently read> ...pport/marginpar/begin_args_int
    ```
- В заголовке лога `xelatex` / `pdflatex` печатается старая дата ядра (например, `LaTeX2e <2024-11-01>`), хотя сам MiKTeX обновлён (например, `MiKTeX 26.5`).

### Причина
Произошёл **рассинхрон между базой метаданных MiKTeX и файлами на диске**:
- в локальной базе пакетов MiKTeX уже записаны свежие метки упаковки (`timePackaged`) для `ltxbase`, `l3kernel` и др., поэтому `check-update` считает их актуальными;
- при прерванном обновлении, блокировке файлов или частичном копировании реальные файлы (`tex\latex\base\latex.ltx`, `tex\latex\l3kernel\expl3.sty` и десятки других пакетов) на диске остались от старой версии.

### Диагностика
```powershell
# 1. Проверить целостность всех установленных пакетов по контрольным суммам базы
miktex packages verify

# 2. Сравнить дату упаковки ltxbase/l3kernel в базе с реальным файлом на диске
miktex packages list --template "{id}`t{isInstalled}`t{timePackaged}" |
  Select-String -Pattern "^(ltxbase|l3kernel|koma-script)\b"

Get-Item (kpsewhich latex.ltx), (kpsewhich expl3.sty) |
  Select-Object FullName, LastWriteTime, Length
```
Если `miktex packages verify` выводит строки вида:
```text
ltxbase: this package needs to be reinstalled.
l3kernel: this package needs to be reinstalled.
```
значит файлы на диске не соответствуют базе и пакеты нужно переустановить.

---

## 2. Нюансы CLI `miktex packages` при переустановке

1. **Команда удаления называется `remove`, а не `uninstall`.**
   `miktex packages uninstall` выдаст `Incorrect usage: uninstall: unknown command`.
2. **`miktex packages install` не перезаписывает уже установленный пакет.**
   Он остановится с ошибкой `Sorry, but: <pkg>: package is already installed`. Для переустановки нужно сначала выполнить `remove`, затем `install`.
3. **Массовая переустановка по списку из `verify`:**
   Закройте MiKTeX Console и редакторы, держащие файлы TeX, затем выполните:
   ```powershell
   $broken = (miktex packages verify 2>&1) |
     ForEach-Object { if ($_ -match '^([^:]+): this package needs to be reinstalled\.') { $Matches[1] } }

   if ($broken) {
       $listFile = Join-Path $env:TEMP "miktex-reinstall.txt"
       $broken | Set-Content -Path $listFile -Encoding ASCII
       miktex packages remove  --package-id-file="$listFile"
       miktex packages install --package-id-file="$listFile"
   }
   ```

---

## 3. Почему падает `initexmf --dump` без аргументов (`hilatex.fmt`)

### Как проявляется
Запуск `initexmf --update-fndb --mkmaps --dump` (без указания конкретных форматов) завершается с кодом `1`, а в `%LOCALAPPDATA%\MiKTeX\miktex\log\initexmf.log` появляется ошибка:
```text
ERROR initexmf - sub-process error output has been saved to '...\miktex_YYYY-MM-DD-HHMMSS.out'
FATAL initexmf - Windows API error 2: Не удается найти указанный файл.
FATAL initexmf - Info: existing="...\Temp\mikXXXXX\hilatex.fmt", path="...\MiKTeX\miktex/data/le/hitex\hilatex.fmt"
```

### Причина и последствия
Голый флаг `--dump` вызывает `miktex --enable-installer formats build` для **всех** зарегистрированных форматов подряд (`amstex`, `bagpipe`, `lollipop`, `cslatex`, `hilatex` и т.д.). Экспериментальный формат **`hilatex`** (движок `hitex`) часто падает при сборке, и **`initexmf` аварийно прерывается, не доходя до пересборки `xelatex.fmt` и `pdflatex.fmt`** — в итоге они остаются старыми!

### Правильное решение
Всегда пересобирайте только нужные рабочие форматы явно:
```powershell
initexmf --update-fndb --mkmaps --dump=xelatex --dump=pdflatex --dump=lualatex
```

Проверить даты реально пересобранных `.fmt`-файлов:
```powershell
Get-ChildItem "$env:LOCALAPPDATA\MiKTeX\miktex\data\le" -Recurse -Filter "*.fmt" |
  Select-Object Name, LastWriteTime | Sort-Object Name
```

---

## 4. Полезные пути и проверки в MiKTeX (Windows)

- **Проверить режим установки (User vs Admin):**
  ```powershell
  initexmf --report
  ```
  Строка `SharedSetup: no` означает частную пользовательскую установку (`UserInstall` в `%LOCALAPPDATA%\Programs\MiKTeX`, кэш и форматы `UserData` в `%LOCALAPPDATA%\MiKTeX`). Если `SharedSetup: yes`, следите, чтобы обновления не делались вразнобой в User и Admin режимах.
- **Логи диагностики:**
  - `%LOCALAPPDATA%\MiKTeX\miktex\log\initexmf.log` — сборка форматов, FNDB, карт шрифтов;
  - `%LOCALAPPDATA%\MiKTeX\miktex\log\miktex_*.out` — вывод дочерних процессов `miktex formats build`;
  - `%LOCALAPPDATA%\MiKTeX\miktex\log\mpmcli.log` / `miktex-console.log` — установка/удаление пакетов.
- **Проверить, какое ядро реально зашито в текущий `xelatex.fmt`:**
  ```powershell
  xelatex -interaction=nonstopmode "\stop" | Select-String "LaTeX2e|L3 programming"
  ```

---

## 5. Автоматический скрипт `miktex_repair.ps1`

Скрипт [miktex_repair.ps1](miktex_repair.ps1) автоматизирует весь цикл диагностики, починки и безопасной пересборки форматов (в обход `hilatex`).

### Примеры запуска
```powershell
# Только диагностика (ничего не меняет): проверяет обновления, verify, даты ядра и форматов
.\miktex_repair.ps1 -CheckOnly

# Полный цикл (по умолчанию): update -> переустановка битых пакетов -> пересборка xelatex/pdflatex/lualatex -> финальный verify
.\miktex_repair.ps1

# Только починить пакеты из verify и пересобрать форматы (без скачивания новых обновлений)
.\miktex_repair.ps1 -Repair -RebuildFormats

# Только пересобрать рабочие форматы (минуя hilatex)
.\miktex_repair.ps1 -RebuildFormats

# Указать свой набор форматов
.\miktex_repair.ps1 -RebuildFormats -Formats @("xelatex", "pdflatex")
```

---

## 6. Защита переносимых KOMA-Script проектов от старого ядра

Если `.tex`-шаблон на `KOMA-Script` v3.49+ должен компилироваться и на машинах, где ядро LaTeX2e ещё `2024-11-01`, можно поставить в самую первую строку документа (до `\documentclass`):

```latex
\providecommand\IfDocumentMetadataT[1]{}\providecommand\IfDocumentMetadataTF[2]{#2}
\documentclass[11pt,a4paper]{scrartcl}
```

На актуальном LaTeX2e (2025/2026+) `\providecommand` ничего не переопределяет и оставляет нативную реализацию нетронутой.
