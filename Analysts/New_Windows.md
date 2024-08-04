# Установка Windows с диска
- COOL! Лучшее решение. [Rufus](https://rufus.ie/ru_RU.html). Простое создание загрузочных USB-дисков

# Package manager
- COOL! [Chocolatery. The Package Manager for Windows](https://chocolatey.org/). Modern Software Automation
- [How to upgrade Chocolatey on Windows](https://www.opentechguides.com/how-to/article/windows/212/chocolatey-upgrade.html)
`c:\> choco upgrade chocolatey`
- [List All Installed Packages with Chocolatey](https://mangolassi.it/topic/18334/list-all-installed-packages-with-chocolatey)
`choco list --local-only`. Там же примеры команд на апгрейд.
- [How to Use Chocolatey to Easily Install and Update Windows Programs](https://www.maketecheasier.com/use-chocolatey-to-install-update-windows-programs/). Тут упоминается про Chocolatey GUI. `choco install chocolateygui`

# Бесплатные лицензии
- [COMSS1](https://www.comss.ru/list.php?c=club)

# МТС, раздача интернета
- [КАК ОБОЙТИ ОГРАНИЧЕНИЕ МТС БЕЗЛИМИТИЩЕ НА ПЛАТНУЮ РАЗДАЧУ ИНТЕРНЕТА. КАК ИЗМЕНИТЬ TTL. +ВИДЕО](http://compblog.ru/kak-obojti-ogranichenie-mts-bezlimitishhe-na-platnuyu-razdachu-interneta-kak-izmenit-ttl.html)

# Ubuntu on Windows10
- [Everything You Can Do With Windows 10’s New Bash Shell](http://www.howtogeek.com/265900/everything-you-can-do-with-windows-10s-new-bash-shell/)
- Так не заработало. Ни прямая инсталляция, ни апдейты. [How to Update the Windows Bash Shell to Ubuntu 16.04](http://www.howtogeek.com/278152/how-to-update-the-windows-bash-shell/). 
- [How to Upgrade Bash on Windows 10 to Ubuntu 16.04 LTS](http://www.omgubuntu.co.uk/2016/08/upgrade-bash-windows-10-ubuntu-16-04-lts). Пробуем таким образом:
	- `sudo do-release-upgrade -f DistUpgradeViewNonInteractive -d`
	- `sudo -S dpkg --configure -a`
	- `sudo -S apt-get update`
	- `sudo -S apt-get dist-upgrade`
	- `sudo -S apt-get autoremove`

# Скачивание произвольного образа Windows
- [](https://tb.rg-adguard.net/public.php)

# Переключение между мониторами в Windows 10
- [Переключение между мониторами в Windows 10](https://realadmin.ru/admining/pereklyuchenie-mezhdu-monitorami.html).
Быстро переключиться между основным и дополнительным монитором позволяют горячие клавиши Win + P. В Windows 10 эта комбинация вызывает меню «Проецировать», где можно выбрать режим отображения экранов.
- [Перемещение окон между мониторами](https://realadmin.ru/admining/pereklyuchenie-mezhdu-monitorami.html). Перемещение программ и окон на другой монитор может осуществляться обычным перетаскиванием мыши, но есть и более удобный способ. В Windows 10 для этого существуют горячие клавиши: Win + Shift + стрелка вправо/влево. Например, если одновременно нажать Win + Shift и левую стрелку, то окно с активной программой перенесется на левый дисплей.

# Настройка приложений Windows 10
- [Как включить всем привычный Просмотр Фотографий в Windows 10](http://g-ek.com/prosmotr-fotografij-v-windows-10)
- [iPhone или iPad не синхронизируется с компьютером?](http://appleinsider.ru/iphone/iphone-ili-ipad-ne-sinxroniziruetsya-s-kompyuterom-est-reshenie.html) Есть решение. Если вы столкнулись с подобной проблемой, может помочь сброс папки Lockdown на Mac или Windows
- [Невозможность создания резервной копии данных iPhone, iPad или восстановления из резервной копии в iTunes](http://app-s.ru/publ/rezervnaja_kopija_v_itunes_ne_udaetsja_vypolnit_rezervnoe_kopirovanie_ili_vosstanovlenie_iz_rezervnoj_kopii_v_itunes/1-1-0-215)
- Решение найдено в YouTube:
Диспетчер устройств -> Переносные устройства -> Apple iPad -> Обновить драйверы -> Manual -> "C:\Program Files\Common Files\Apple\Mobile Device Support\Drivers"
- [Как настроить автоматический вход при загрузке Windows 10 TP](https://lifehacker.ru/avtomaticheskij-vhod-windows-10-tp/)
В том распространённом случае, когда вы доверяете своему домашнему и/или офисному окружению и не пытаетесь ограничить доступ к Windows, предлагаем при помощи нескольких простых шагов настроить автоматический вход в аккаунт:
	- Сделайте правый клик на кнопке «Пуск» в левом нижнем углу экрана. Щёлкните по пункту «Выполнить».
	- Введите команду `netplwiz` и запустите её выполнение.
	- В открывшемся окне «Учётные записи пользователей» снимите галочку напротив пункта «Требовать ввод имени пользователя и пароля».
	- Укажите свой пароль и повторите его ввод.

# Как определить ключ установки Windows
- [Почему нельзя выполнять чистую установку Windows 10 обладателям Windows 7 и 8](https://lifehacker.ru/2015/08/04/tonkosti-ustanovki-windows-10/)
- [5 простых способов как узнать ключ продукта ОС Windows 10](http://geek-nose.com/5-prostyx-sposobov-kak-uznat-klyuch-produkta-os-windows-10/)
- [Как узнать ключ продукта Windows 10](http://remontka.pro/windows-10-key/)
- Выбираем средства с GUI:
	- [Как узнать OEM ключ из UEFI](http://remontka.pro/windows-10-key/)
	- [ProduKey от NirSoft](http://www.nirsoft.net/utils/product_cd_key_viewer.html) для определения ключа Windows 10 и не только. “ProduKey” от NirSoft умеет определять ключи других копий Windows, установленных на локальном и удаленных компьютерах, в том числе на всех машинах в домене. Также он может вытащить ключ из реестра незагруженной системы. Последнее бывает необходимо при переустановке ОС, чтобы повторно активировать Windows 10, когда она потребует ключ продукта.
	- !! [ShowKeyPlus](https://github.com/Superfly-Inc/ShowKeyPlus/releases/). “ShowKeyPlus” – единственный продукт, который смог определить ключ установленной ОС Windows 10 и ее предшественницы Windows 7 (“семерка” в нашем примере была обновлена до “десятки”). Как и “ProduKey” от NirSoft, она не требует инсталляции и не распространяет рекламу, ее достаточно скачать и запустить. Ключи продуктов отображаются в основном окне. Нажатием “Save” их можно скопировать и сохранить в текстовом файле.
Кроме того, “ShowKeyPlus” умеет извлекать product key из реестра незагруженной ОС. Кликните для этого “Retrieve key from backup” и укажите путь к источнику – файлу Software, который находится в каталоге Буква_раздела\Windows\system32\config.
- [How To Get Windows 10 For Free If You’re Running Windows Vista or XP](http://bgr.com/2015/06/20/windows-10-free-upgrade-xp-vista/)

# Перевод Win 32 на Win 64
Это возможно!
- [How to upgrade from a 32-bit to 64-bit version of Windows 10](https://www.windowscentral.com/how-upgrade-32-bit-64-bit-version-windows-10)

# RAM
- [Single Rank vs Dual Rank RAM: Differences & Performance Impact](https://www.cgdirector.com/single-rank-vs-dual-rank-ram/). Sigle Rank рулит.
- [SINGLE RANK MEMORY VS. DUAL RANK MEMORY (VS QUAD RANK MEMORY)](https://www.oempcworld.com/support/singlevsdualram.html). Generally Single Rank Memory is faster than Dual Rank Memory, in layman’s terms when a computer accesses Single Rank Memory it only has to go around the track once, where are Dual Rank it would have to go around the track twice.

# Hardware
- [USBefuddled: Untangling the Rat’s Nest of USB-C Standards and Cables](https://tidbits.com/2021/12/03/usbefuddled-untangling-the-rats-nest-of-usb-c-standards-and-cables/)

# Command Line
- [Split long commands in multiple lines through Windows batch file](https://stackoverflow.com/questions/69068/split-long-commands-in-multiple-lines-through-windows-batch-file)
```
Example:
copy file1.txt file2.txt
would be written as:
copy file1.txt^
 file2.txt
```
- [Windows Command Prompt: How to pass multi-line string parameters](https://stackoverflow.com/questions/11948025/windows-command-prompt-how-to-pass-multi-line-string-parameters)
- [Change working directory to network share](https://superuser.com/questions/1014248/change-working-directory-to-network-share)
	Solution: Use `pushd` or use PowerShell where `cd \\Server\path`.
	Alternate Solution: Map the UNC path to a drive letter. `net use Y: \\myServer\myShare`
- [How to recursively list files (and only files) in Windows Command Prompt?](https://superuser.com/questions/1010287/how-to-recursively-list-files-and-only-files-in-windows-command-prompt) `dir /A-D /S /B`
- [Is it possible to get a recursive directory listing with details in Windows?](https://superuser.com/questions/1631829/is-it-possible-to-get-a-recursive-directory-listing-with-details-in-windows)
`for /f %F in ('dir /s /r /b /a-d *.*') do @echo %~zF %F`
`for /f %F in ('dir /s /b /a-d') do @echo %~zF %F`


# Переход на SSD
- [Рейтинг SSD дисков, выбираем лучший SSD 2021, тест скорости SSD дисков](https://www.nix.ru/hardware-review/ssd-benchmark-performance.html)
- [Пpoдвинутый тecт cкopocти жecткиx диcкoв - IOmeter](https://servak.com.ua/blog/rukovodstva/prodvinutyj-test-skorosti-zhestkih-diskov-iometer/)
- [CrystalDiskMark](https://crystalmark.info/en/software/crystaldiskmark/)
- [Samsung SSD 850 EVO 250GB – Problems And Their Solutions](http://webfrst.com/samsung-ssd-850-evo-250gb-problems-solutions/)
- [Программа SSD Ready](https://www.ssdready.com/ssdready-ru/). Узнайте как долго у вас будет работать SSD диск
- [Как создать RAM диск в Windows 11 и Windows 10](https://remontka.pro/create-ram-disk-windows/)
- [RAMDisk, или что делать если у вас в компьютере 128 гигабайт оперативной памяти](https://geektimes.ru/company/kingston_technology/blog/277610/)
- RAMDisks:
	- [SoftPerfect RAM Disk](http://forum.ru-board.com/topic.cgi?forum=35&topic=47817&start=40#lt)
	- Остановился на этом. [DataRAM RAMDisk](http://memory.dataram.com/products-and-services/software/ramdisk)
	- [Primo Ramdisk (VSuite Ramdisk II) - Powerful RAM Disk Emulator for Windows](http://www.romexsoftware.com/en-us/primo-ramdisk/)
- [Отучиваем Google Chrome убивать ресурс SSD винчестера](https://habrahabr.ru/sandbox/59573/)
Следующий вариант по-моему скромному мнению, решил все мои проблемы. Я решил использовать RAM Drive — т.е. держать все в оперативной памяти, и только лишь при выключении писать на винчестер. Учитывая что ноутбук у меня либо включен, либо в ждущем режиме, то писаться при выключении будет очень редко. Из понравившихся программ остановил выбор на Qsoft RAMDisk. Ставится как драйвер. В свойствах выбрал размер диска, файловую систему, куда писать при выключении. Под диск выделил 512 МБ (думаю разумный минимум 128 МБ).
Можно было перенести просто папку кеша [`C:\Users\%USER%\AppData\Local\Google\Chrome\User Data\Default\Cache`], можно было и добавить к ней папку Media Cache, но я решил полностью избавиться от всяческих записей, и перенести полностью всю папку User Data. 
Можно было опять же указать в параметрах ярлыка --user-data-dir=«путь к рам-диску» для перенаправления хранения профиля, можно было прописать в реестре, но при запуске без ярлыка либо обновлении, все это не работало бы. Начал думать как бы так сделать чтобы ничего не меняя перенаправить. И тут я вспомнил про символические ссылки!
Была скачана утилита Link Shell Extension, при помощи которой я фактически на месте папки User Data создал «ярлык», ссылку которая вела на мой рам-диск. Т.е. на диске ничего не лежало, заходя в папку User Data мы сразу же перенаправлялись на рам-диск. Причем в чем плюс такого решения — ни система, ни Хром никакого подвоха не видели.
Хром стал работать еще быстрее чем он был на SSD. Очень быстро. Я теперь наверное даже всем порекомендую хотя-бы кеш хрома вынести на небольшой рам-диск. Лично для меня загадка почему инженеры не придают внимания проблеме того что хром очень много и часто пишет. Надежность информации это хорошо, но не ценой же убийства винчестера!
- [Оптимизация настроек Windows 10 для работы SSD диска](http://windowsten.ru/optimizaciya-nastroek-windows-10-dlya-raboty-ssd-diska/)
	- `fsutil behavior query DisableDeleteNotify` . Должно быть поставлено в 0 (TRIM)
- [SSD-твикинг: мифы и реальность](http://www.thg.ru/storage/ssd_tweaks/onepage.html). Тут есть про настройку схем энергопитания.
- [Новые технологии. Обзор Samsung 850 Pro 31.08.2014](http://allssd.ru/obzor-samsung-850-pro/)
- [SSD Mini Tweaker](http://spb-chas.ucoz.ru/). Программа для изменения настроек и параметров системы под твердотельный накопитель. Цель программы - это снизить обращение системы к SSD для более продолжительной его работы. Распространяется бесплатно и предназначена для тех, у кого система установлена на SSD-диске.
- [Lenovo v580 (20147) и mSATA SSD как загрузочный диск!](https://forums.lenovo.com/t5/%D0%A1%D0%B5%D1%80%D0%B8%D0%B8-U-%D0%B8-V/Lenovo-v580-20147-%D0%B8-mSATA-SSD-%D0%BA%D0%B0%D0%BA-%D0%B7%D0%B0%D0%B3%D1%80%D1%83%D0%B7%D0%BE%D1%87%D0%BD%D1%8B%D0%B9-%D0%B4%D0%B8%D1%81%D0%BA/td-p/2149052)
- [Lenovo V580c установка Windows 10 на SSD](https://forums.lenovo.com/t5/%D0%A1%D0%B5%D1%80%D0%B8%D0%B8-U-%D0%B8-V/Lenovo-V580c-%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B0-Windows-10-%D0%BD%D0%B0-SSD/m-p/3354438)
- [Для SSD диска в V580c (20160) - незадействованный слот miniPCIe или mSATA?](http://lenovo-forums.ru/topic/5670-%D0%B4%D0%BB%D1%8F-ssd-%D0%B4%D0%B8%D1%81%D0%BA%D0%B0-%D0%B2-v580c-20160-%D0%BD%D0%B5%D0%B7%D0%B0%D0%B4%D0%B5%D0%B9%D1%81%D1%82%D0%B2%D0%BE%D0%B2%D0%B0%D0%BD%D0%BD%D1%8B%D0%B9-%D1%81%D0%BB%D0%BE%D1%82-minipcie-%D0%B8%D0%BB%D0%B8-msata/)
Вчера купил твердотельный накопитель (SSD) Plextor 128Gb mSATA (PX-128M5M). Всё встало отлично. Сразу определилось.
Возникли некоторые проблемы с переносом Windows 7 на SSD. Это потому, что пробовал делать средствами Acronis True Image. Делать это лучше, как оказалось,  AOMEI Partition Assistant Home Edition – бесплатной программкой с большим функционалом. Вот здесь инструкция, как пользоваться:
- [AOMEI Partition Assistant 6.0](http://www.aomeitech.com/aomei-partition-assistant.html). Professional and complete disk partition solution for Windows OS
	- [The easiest OS migration to new hard drive or SSD](http://www.disk-partition.com/features/migrate-os-to-ssd.html)
	- [Learn How to Migrate OS to SSD or HDD](http://www.disk-partition.com/features/migrate-os-to-ssd.html)

http://it-like.ru/kak-perenesti-windows-7-na-ssd-disk/

Далее, можно обновить прошивку. Вот инструкция как делать и где взять: http://pk-help.com/workstation/upgrade-plextor-m5s/
- [жесткий диск SSD 500ГБ, mSATA, SATA III, Samsung 850 EVO Series, MZ-M5E500BW](https://www.ulmart.ru/goods/3498218#tab-properties)
- [Технология Over-Provisioning в SSD](http://www.nix.ru/computer_hardware_news/hardware_news_viewer.html?id=178629)

# Изменение типа дисков MBR/GPT
Телевизор вот не видит разделы диска GPT если их несколько. Ищем решение. Либо конвертировать в MBR, либо оставить только один GPT раздел
- [How Can You Convert GPT to MBR without Data Loss Using Command Prompt?](https://www.diskpart.com/gpt-mbr/convert-gpt-to-mbr-without-data-loss-using-command-prompt.html)
- [Изменение схемы разделов диска с GPT на MBR](https://learn.microsoft.com/ru-ru/windows-server/storage/disk-management/change-a-gpt-disk-into-an-mbr-disk)
- [MBR2GPT.EXE](https://learn.microsoft.com/ru-ru/windows/deployment/mbr-to-gpt?source=recommendations)

# Работа с партициями
- [Viewing Partition Information on a Windows System](https://support.moonpoint.com/os/windows/commands/partitions/)
`diskpart`, `wmic`
- [Get Windows NTFS Block Size](https://www.bytesizedalex.com/get-windows-ntfs-block-size/)
`fsutil fsinfo ntfsinfo f:`
- [Advanced Format (AF) Technology](https://idema.org/initiatives/advanced-format/). Ключевая фраза "512 byte emulation (AF 512e)"
- [512-byte Emulation (512e) Disk Compatibility Update](https://learn.microsoft.com/en-us/windows/win32/win7appqual/512-byte-emulation--512e--disk-compatibility-update)
- [Диски, контроллеры, ОС и Advanced Format](https://habr.com/ru/articles/245085/)
- [How to 'fix' disk with 512-byte sectors, formatted using an enclosure that translated to 4k sectors](https://superuser.com/questions/1562160/how-to-fix-disk-with-512-byte-sectors-formatted-using-an-enclosure-that-trans)
- [How to reformat HDD & SSD to 512B Sector Size](https://forums.servethehome.com/index.php?threads/how-to-reformat-hdd-ssd-to-512b-sector-size.4968/page-20). Идет очень длинный диалог.
- [An update that improves the compatibility of Windows 7 and Windows Server 2008 R2 with Advanced Format Disks is available](https://support.microsoft.com/en-us/topic/an-update-that-improves-the-compatibility-of-windows-7-and-windows-server-2008-r2-with-advanced-format-disks-is-available-004a02e4-7812-e14f-9dd7-d5e61c3ee20e)

# Локализация bad sector у АВ
- [Bad Block Copy for Windows](http://alter.org.ua/en/soft/win/bb_recover/)
- [DMDE - DM Disk Editor and Data Recovery Software](https://dmde.com/)
- [Finding out which file is affected by a bad sector](https://www.disktuna.com/finding-out-which-file-is-affected-by-a-bad-sector/).
The [Microsoft support tool NFI.exe](https://support.microsoft.com/en-us/help/253066/oem-support-tools-phase-3-service-release-2-availability) can be used to convert a LBA sector address to a file path. This way you can determine which files need to be restored from backup after sector reallocation.
- `NFI.exe` потерял следы, есть альтернатива:
	- [findLBAf](ftp://www.terabyteunlimited.com/findlbaf.zip)  от TerabyteUnlimited
- [Бесплатная лицензия Hard Disk Sentinel Standard Edition](https://www.comss.ru/page.php?id=4446)
```
Для получения бесплатной лицензии Hard Disk Sentinel выполните следующие действия:

1. Скачайте и установите программу по ссылке ниже. Программа устанавливается уже активированной.
Поддерживаемые ОС Windows: Windows 95, 98, 98SE, ME, NT4, 2000, XP, 2003, 2008, Vista, Windows 7, Windows Home Server, Windows 2012, Windows 8, Windows 8.1, Windows 10 версий 32-bit и 64-bit (где применимо)

Примечание: Чтобы включить русский язык, выберите его при установке или перейдите в меню Configuration -> Preferences и в выпадающем меню Language выберите Russian. Затем нажмите ОК.
Условия предложения
•Это пожизненная лицензия только для версии 5.20.
•Нет бесплатных обновлений до будущих версий. При обновлении вы потеряете активацию.
•Нет бесплатной технической поддержки.
•Только для некоммерческого использования
```
- [Ошибка 0xC0000225, 0xC00000E, Missing Winload.efi после копирования или миграции ОС](https://kb.paragon-software.com/ru/article/423)
- [Ошибка chkdsk : проверка диска не работает](https://computer76.ru/2017/10/20/chkdsk-errors/)
	- `sfc /scannow` -- проверка целостности файловой системы, починка файлов.

# WebDAV
- [Как в Windows подключить облачное хранилище в качестве сетевого диска по протоколу WebDav](https://remontcompa.ru/windows/funkcional-windows/1832-kak-v-windows-podklyuchit-oblachnoe-hranilische-v-kachestve-setevogo-diska-po-protokolu-webdav.html)
- [OneDrive — подключение по протоколу WebDav](https://vellisa.ru/onedrive-webdav)
- [OneDrive WebDAV](https://webdav.io/webdav/webdav-integrations/onedrive-webdav/)

# Проблемы Lenovo с видеодрайвером
1. Удалить Nvidia Update & UpdatusUser (через netplwiz)
2. Удалить Norton и прочую фигню
3. Office 365 со скидкой 50%. [Хак](http://news.microsoft.com/ru-ru/office-2016-for-windows-10/)

# Windows 7 и выше. Проблемы с принтером HP Laserjet 1300
- Начал решение отсюда: [Помогите найти драйвер способный печатать на HP Lasejet 1300 в Windows 7/Vista в родном для принтера разрешении 1200 dpi](http://forum.ixbt.com/topic.cgi?id=58:14)
- Нашел решение здесь: [Установка драйвера HP LaserJet 1320 в Windows 10. Решено!!!](https://dyrik.ru/windows/ustanovka-drajvera-hp-laserjet-1320-v-windows-7-windows-8-i-windows-10-resheno.html)

# Полезные твики по настройке Windows

- [Windows: Как изменить язык при входе в систему?]
Бывает, что необходимо изменить язык ввода при вводе пароля/логина. По-умолчанию язык ввода пароля задается в соответствии с выбранной локализацией операционной системы Windows. Можно изменить это двумя способа. Дедовским через реестр и если у Вас виндоус старше седьмой версии - через менюшку управления языками.

Способ первый:
Заходим меню: "Панель управления" -> "Часы, языки и регион" -> "Смена раскладки клавиатуры и других способов ввода". После чего переходим на вкладку "Дополнительно" и ставим галочку "Копировать параметры" (Помните, что у вас по умолчанию в самой Windows) должен стоять нужная раскладка).
Перезагружаемся и все.

Способ второй:
Для этого нужно перейти в реестр Windows (запускаем через сочетание клавиш Windows + R, там прописываем regedit и жмём Enter).
Заходим в раздел

HKEY_USERS\.Default\Keyboard Layout\Preload
Там два ключа, 1 и 2.
В ключе 1 надо задать значение 409 (англ) в ключе 2 значение 419 (рус).
Т.е. просто поменять местами, т.к. для русской локализации они заданы наоборот.

- [Компьютер уходит в сон через 2 минуты](https://fandorka.by/2018/02/pcsleep/). Проблема кроется в новом режиме «System unattended sleep timeout», который по умолчанию включен, но не виден в настройках. Чтобы его деактивировать, необходимо проделать несколько несложных шагов.
	1. Запускаем редактор реестра: кликайте левой кнопкой мышки по кнопке пуск и набирайте «Regedit», по появившейся иконке приложения жмите правой кнопкой мыши и выбирайте «Запуск от имени администратора»
	2. В открывшемся редакторе необходимо перейти по адресу: HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Power\PowerSettings\238C9FA8-0AAD-41ED-83F4-97BE242C8F20\7bc4a2f9-d8fc-4469-b07b-33eb785aaca0
	3. Измените значение параметра «Attributes» на 2 (два раза щелкните левой кнопкой мыши по нему) и жмите «ОК»
	4. Правой кнопкой мыши кликайте по кнопке Пуск и выбирайте пункт «Управление электропитанием»
	5. В открывшемся окне выбирайте «дополнительные параметры питания»
	6. Там жмем «настройка схемы электропитания»
	7. «Изменить дополнительные параметры питания»
	8. И вот наконец мы на финальном шаге. Идите в секцию сон и измените значения для параметра «Время ожидания автоматического перехода …» на желаемое время, например 20 мин

- Как отключить в ярлыках Рабочего стола тени шрифта. Взял с копии статьи ["Обживаем Windows 10"](https://ishutov.blogspot.com/2015/12/windows-10.html) в моем блоге.
Как Вы знаете, шрифт, который используется в иконках Рабочего стола, по умолчанию, отбрасывает тень. Бывает, что по этой причине, при наложении текста на однотонное фоновое изображение, его невозможно прочитать. Остаётся один выход – отключить тень.
Для отмены отображения, отбрасываемых шрифтом, теней, есть несколько вариантов. Один из них внести изменения в реестр Windows. Делается это так: меню «Пуск», потом набираем в строке поиска команду «Regedit» и нажимаем кнопку «Enter». Следующим действием подтверждаем запрос в появившемся окне системы контроля учетных записей. После этого открываем окно редактора реестра и переходим к ключу `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced`. Смотрим в правую часть окна и находим параметр `DWORD`, который называется `ListviewShadow`.
Двойным кликом мыши открываем его, и ставим там значение «О», нажав на кнопку «ОК» соглашаемся с изменениями. Всё, осталось закрыть реестр и перезагрузить компьютер, после чего ваши изменения вступят в силу. Параметр, который мы только что отредактировали как раз и регулирует прозрачность шрифта.
Такого же результата можно было добиться и без перезагрузки компьютера, просто изменив настройку графического интерфейса системы. Возможно, кому то это решение покажется более простым. Делается это так: в Панели управления выбираем пункт «Система и безопасность» , кликаем по значку «Система», потом в открывшемся окне — по значку «Дополнительные параметры системы». Далее в разделе «Быстродействие», нажимаем кнопку «Параметры» и просто снимаем галочку на пункте «Отбрасывание теней значками на рабочем столе». Соглашаемся с изменениями, щелкнув по кнопке «ОК», и всё, тени больше отображаться не будут.

- Win+R - вызов окна "выполнить"
	- control - вызов панели управления
	- netplwiz - управление учетными записями пользователей
	- control userpasswords2 - управление учетными записями пользователей
	- dcomcnfg - настройка компонент (в частности, DCOM)
	- "RunDll32.exe shell32.dll,Control_RunDLL hotplug.dll" - восстановление иконки безопасного извлечения устройства в Windows
	- mmc devmgmt.msc - запуск диспетчера устройств

- Запуск центра обновления Windows:
   Пуск -> Параметры -> Обновления и безопасность
- Убираем флажок с объектов в explorer. [Как убрать флажки в проводнике на Windows 10](https://guidepc.ru/windows/kak-ubrat-flazhki-v-provodnike-na-windows-10/). Эта функция впервые появилась в Windows Vista и обычно включалась по умолчанию в Windows 8 на устройствах с сенсорным экраном. На панели ленты в верхней части окна проводника перейдите на вкладку «Вид». Найдите «Флажки элементов» на панели инструментов Вид и щелкните по нему.
Альтернативный метод: используйте окно параметров папки. Нажмите кнопку «Параметры», и Вы увидите окно «Параметры папки». Перейдите на вкладку «Вид». Прокручивайте список вниз, пока не увидите «Использовать флажки для выбора элементов». Снимите флажок, затем нажмите Применить.
- [Что делать, если пропало безопасное извлечение устройства в Windows](http://remontka.pro/propalo-bezopasnoe-izvlechenie/) или [здесь](http://pomogaemkompu.temaretik.com/741888136915716896/chto-delat-esli-propalo-bezopasnoe-izvlechenie-ustrojstva-v-windows/) 
- [«Безопасное извлечение устройства» использовать или нет?](http://nn-lab.ru/windows/bezopasnoe-izvlechenie-ustrojstva-ispolzovat-ili-net.php)
А [тут вот] детальные изыскания по поводу пропавшей закладки "Политика"

Win 10 ставится на Win 8.1
SP1 можно получить через web: [Service Pack and Update Center](http://windows.microsoft.com/en-us/windows/service-packs-download)

- [Как получить Windows 10 без очереди](http://lifehacker.ru/2015/07/30/kak-poluchit-windows-10/)
	- Task Manager + запустить новый процесс как администратор Powershell -> wuauclt.exe/updatenow
- [Обновление KB 3081436 для Windows 10 приводит к бесконечной перезагрузке, как и KB 3081424, выпущенное ранее](http://gamesqa.ru/news/obnovlenie-kb-3081436-dlya-windows-10-privodit-k-beskonechnoj-perezagruzke-kak-i-kb-3081424-vypushhennoe-ranee-1538/)

- [Как отключить или включить экран блокировки Windows 10](http://www.oszone.net/27774/Lock_Screen_-_Enable_or_Disable_in_Windows_10)
- [Как включить полноэкранный «Пуск» в Window 10](http://www.softrew.ru/instructions/1410-kak-vklyuchit-polnoekrannyy-pusk-v-window-10.html)

Как показывает практика, проблема с установкой заключается в наличии некорректного профиля Nvidia под названием UpdatusUser.
- [What is “UpdatusUser” Folder and How to Remove it from Windows Explorer?](http://www.askvg.com/tip-what-is-updatususer-folder-and-how-to-remove-it-from-windows-explorer/)

- [Microsoft тайком загружает файлы Windows 10 пользователям Windows 7 и 8. Как с этим бороться](http://lifehacker.ru/2015/09/11/how-to-block-windows-10-upgrade-downloads/)

- [How to install or uninstall Windows Store Apps in Windows 10](https://www.thewindowsclub.com/uninstall-windows-10-apps)
- [Как очистить файлы и папки быстрого доступа в проводнике?](https://tunecom.ru/windows/143-kak-ochistit-chasto-ispolzuemye-papki-i-fajly-v-windows-10.html)
- [Отображение значков на рабочем столе в Windows](https://support.microsoft.com/ru-ru/windows/%D0%BE%D1%82%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5-%D0%B7%D0%BD%D0%B0%D1%87%D0%BA%D0%BE%D0%B2-%D0%BD%D0%B0-%D1%80%D0%B0%D0%B1%D0%BE%D1%87%D0%B5%D0%BC-%D1%81%D1%82%D0%BE%D0%BB%D0%B5-%D0%B2-windows-c13270f0-3812-c71d-f27e-29aa32588b20#:~:text=%D0%92%D1%8B%D0%B1%D0%B5%D1%80%D0%B8%D1%82%D0%B5%20%D0%9F%D1%83%D1%81%D0%BA%20%2C%20%D0%BE%D1%82%D0%BA%D1%80%D0%BE%D0%B9%D1%82%D0%B5%20%D0%9F%D0%B0%D1%80%D0%B0%D0%BC%D0%B5%D1%82%D1%80%D1%8B%20%2C%20%D0%B7%D0%B0%D1%82%D0%B5%D0%BC,%D0%BD%D0%B0%D0%B6%D0%BC%D0%B8%D1%82%D0%B5%20%D0%BA%D0%BD%D0%BE%D0%BF%D0%BA%D0%B8%20%D0%9F%D1%80%D0%B8%D0%BC%D0%B5%D0%BD%D0%B8%D1%82%D1%8C%20%D0%B8%20%D0%9E%D0%9A.)

## Проблемы с реестром
- [Event ID 10016 - The application-specific permission settings do not grant Local Activation permission for the COM Server application with CLSID](http://answers.microsoft.com/en-us/windows/forum/windows_8-performance/event-id-10016-the-application-specific-permission/9ff8796f-c352-4da2-9322-5fdf8a11c81e?auth=1) и [здесь](http://blog.ronnypot.nl/?p=843)
- [Параметры разрешений для конкретного приложения не дают разрешения Локально Активация для приложения COM-сервера с CLSID {D63B10C5-BB46-4990-A94F-E40B9D520160} и APPID {9CA88EE3-ACB7-47C8-AFC4-AB702511C276}](http://admsoft.ru/parametry-razreshenij-dlya-konkretnogo-prilozheniya-ne-dayut-razresheniya-lokalno-aktivaciya-dlya-prilozheniya-com-servera-s-clsid-d63b10c5-bb46-4990-a94f-e40b9d520160-i-appid-9ca88ee3-acb7-47c8)

В инете есть решение, точно сейчас не напишу, у себя поправил, суть в том что рантаймброкер не может нормально запуститься. В реестре надо на пару веток дать разрешения для Администраторы, далее через *dcomcnfg* - службы и компоненты - компьютеры - мой компьютер - настройка DCOM - для runtimebroker в разрешениях на запуск и активацию добавить network service и local service и system.
конкретнее тут:
Скрытый текст
http://answers.microsoft.com/en-us/windows/forum/windows_10-security/event-id-10016-runtime-broker/18c291c6-f2a1-4f3c-b4ad-2b7ff59fd9f9?auth=1
Закрыть

# Интернет
## Проблемы с Wi-Fi
- [Пропадает интернет (Wi-Fi) в Windows 10 после выхода из спящего режима](https://help-wifi.com/reshenie-problem-i-oshibok/propadaet-internet-wi-fi-v-windows-10-posle-vyxoda-iz-spyashhego-rezhima/).
Это происходит потому, что для экономии, система отключает Wi-Fi адаптер. А после включения, он уже не может нормально работать, поэтому и пропадает интернет. Эта проблема очень часто возникает только при работе от батареи. Все что нужно сделать, это запретить "десятке" отключать беспроводной сетевой адаптер.

## Проблемы с провалами в ping в wi-fi
- [Regular Ping Spikes with Realtek RTL8821CE 802.11ac PCIe Adapter](https://h30434.www3.hp.com/t5/Notebook-Wireless-and-Networking/Regular-Ping-Spikes-with-Realtek-RTL8821CE-802-11ac-PCIe/td-p/7563964)
И так вот починилось (This will definitely stop your wireless card from searching for nearby networks and updating your signal quality when you're not asking it to- which is what is causing the spikes.):
```
C:\Users\Ilya>netsh wlan show settings
Параметры беспроводной локальной сети
---------------------
    Отображать заблокированные сети в списке видимых сетей: Нет
    Использовать профили групповой политики только в сетях, настраиваемых групповой политикой: Нет
    Режим размещенной сети разрешен в службе беспроводной сети: да.
    Разрешить использование общих учетных данных пользователя для проверки подлинности сети: Да
    Период блокировки: не задан.
    Логика автоматической конфигурации включена для интерфейса "Беспроводная сеть"
    Случайный выбор MAC-адресов недоступен на интерфейсе Беспроводная сеть
C:\Users\Ilya>netsh wlan set autoconfig enabled=no interface="Wireless Network Connection"
Данный беспроводной интерфейс в системе отсутствует.
C:\Users\Ilya>netsh wlan set autoconfig enabled=no interface="Беспроводная сеть"
Состояние автонастройки для интерфейса "Беспроводная сеть": запрещен.
```
Но так он потом сам не подключается, надо передергивать...
- [How can I disable network search only when a specific program is running?](https://superuser.com/questions/1147878/how-can-i-disable-network-search-only-when-a-specific-program-is-running)
- [How to Perform a Clean Boot in Windows 10 to Troubleshoot Software Conflicts](https://www.tenforums.com/tutorials/41804-perform-clean-boot-windows-10-troubleshoot-software-conflicts.html)
- [Internet lag spikes and updating wifi driver from realtek](https://answers.microsoft.com/en-us/windows/forum/all/internet-lag-spikes-and-updating-wifi-driver-from/f3b271d6-04a3-4fcc-9371-3b310ed9a2d8)
- [Виртуальный WiFi в Windows 7](https://sekrasoft.livejournal.com/42591.html)
- [How to Fix Ping Spikes in Windows 11/10](https://thegeekpage.com/ping-spikes-in-windows-11-10/#Fix_9_-_Disable_Location_Tracking_Feature)

## Проблемы с интернетом
- [Неопознанная сеть без доступа к Интернету - причины и решение](https://ocomp.info/neopoznannaya-set-bez-interneta.html)
- [Интернет есть, но пишет "Без доступа к интернету" (Windows 10, 8, 7): чем грозит и как исправить](https://vladimirbelev.ru/internet-est-no-pishet-bez-dostupa-k-internetu-windows-10)
- [Исправляем ошибку «msftconnecttest redirect» в Windows 10](https://tehnichka.pro/error-msftconnecttest-redirect-windows-10/)
`HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\NlaSvc\Parameters\Internet` ставим в 0
- [Windows 10 показывает, что интернета нет, но по факту интернет есть](https://answers.microsoft.com/ru-ru/windows/forum/all/windows-10/889c8fb0-db37-47c0-99f6-1ca86a4e5e78).
Похоже у Вас возникает проблема с доступом к серверам DNS, из-за чего система не находит сервисы Microsoft, которые она использует для контроля подключения к сети Интернет.

Пожалуйста попробуйте в свойства сетевого подключения, которое Вы используете для доступа к сети Интернет добавить публичные DNS-сервера Google 8.8.8.8 и 4.4.4.4, либо публичные сервера например Яндекса.

Если это не поможет, Пожалуйста попробуйте перезапустить сетевое соединение, выполнив поочерёдно в командной строке, запущенной с правами администратора команды:
```
netsh winsock reset  и нажмите Enter.
netsh int ip reset  и нажмите Enter.
ipconfig /release  и нажмите Enter.
ipconfig /renew  и нажмите Enter.
ipconfig /flushdns  и нажмите Enter.
```

## Word
- [Reduce the file size of a picture in Microsoft Office](https://support.microsoft.com/en-us/office/reduce-the-file-size-of-a-picture-in-microsoft-office-8db7211c-d958-457c-babd-194109eb9535)

## Outlook
- [Папки в Outlook отображаются на английском языке](https://www.dmosk.ru/polezno.php?review=outlook-en). 
`C:\Program Files\Microsoft Office\root\Office16\outlook.exe /resetfoldernames` переименовают папки на русский (под русской локалью) и теперь их надо синхронизировать по IMAP с русскими папками на сервере.
- [Переименование папок почты в Outlook 2016](https://answers.microsoft.com/ru-ru/msoffice/forum/msoffice_outlook-mso_win10-mso_365hp/%D0%BF%D0%B5%D1%80%D0%B5%D0%B8%D0%BC%D0%B5%D0%BD/09bb0f12-8dda-4a5c-bd3d-657efde45595)

## Tools
- [7 best tabbed command line tools for Windows 10](https://windowsreport.com/tabbed-command-line-windows-10/)
	- Console2
	- PowerCmd
	- ColorConsole
	- MobaExtrem
	- Terminal Wings
	- ConEmu
	- PowerShell ISE
- [Windows Command Line Tools For Developers. Tabbed Console starts here](https://blogs.msdn.microsoft.com/commandline/2018/04/13/tabbed-console-starts-here/)
- COOL! [Windows Terminal 1.0](https://devblogs.microsoft.com/commandline/windows-terminal-1-0/)
- [MSIX Tutorial: A comprehensive 24-chapter guide](https://www.advancedinstaller.com/msix-introduction.html)
- [Direct Folders — экономим клики при работе с файлами в Windows](https://lifehacker.ru/direct-folders-ekonomim-kliki-pri-rabote-s-fajlami-v-windows/)
- [Listary](https://www.listary.com/) is a revolutionary search utility for Windows that makes finding your files and launching applications blazing fast, for casual and power users alike!
- [Clover 3](http://en.ejie.me/). Wings for your Windows Explorer! Clover is an extension of the Windows Explorer, to add multi-tab functionality similar to Google Chrome browser. After install Clover, you will be able to open multiple folders within the same window, and you can also add folder bookmarks.

- [6 Best Free Video Metadata Editor Software For Windows](https://listoffreeware.com/free-video-metadata-editor-software-windows/)

- [GUIformat: FAT32 format](http://www.ridgecrop.demon.co.uk/index.htm?guiformat.htm) I finally got round to doing a Windows GUI version of fat32format.
- [Hard disk information from command prompt](https://social.technet.microsoft.com/Forums/windowsserver/en-US/a2f8e48e-38fc-4bc6-9e0e-e7cedea83d66/hard-disk-information-from-command-prompt?forum=winservergen)
```
Using fsutil volume diskfree c:   or  dir command we can get info on one particular drive, but how to get this on all drives in the system using a single command?
```
- [DriveLetterView v1.46](https://www.nirsoft.net/utils/drive_letter_view.html)
- [Перенос настроек Far Manager с другого компьютера](https://qastack.ru/superuser/169763/migrating-far-manager-settings-from-another-machine) или [здесь](https://poweruser.guru/questions/169763/%D0%BF%D0%B5%D1%80%D0%B5%D0%BD%D0%BE%D1%81-%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B5%D0%BA-far-manager-%D1%81-%D0%B4%D1%80%D1%83%D0%B3%D0%BE%D0%B3%D0%BE-%D0%BA%D0%BE%D0%BC%D0%BF%D1%8C%D1%8E%D1%82%D0%B5%D1%80%D0%B0)
Для Far Manager ver. 3,0:
Настройки экспорта:
Far.exe /export settings.cfg
Настройки импорта:
Far.exe /import settings.cfg

Элементы «F2 User Menu» не были экспортированы.
Меню F2 здесь:"%APPDATA%\Far Manager\Profile\FarMenu.ini"
- [Упрощаем себе работу в ОС Windows с Microsoft PowerToys](https://dtf.ru/howto/1124539-uproshchaem-sebe-rabotu-v-os-windows-s-microsoft-powertoys)
- [Equivalent to the htop command on Windows](https://serverfault.com/questions/815207/equivalent-to-the-htop-command-on-windows)
	- [btop++ for windows](https://github.com/aristocratos/btop4win)
- [RunAsDate v1.41 - Run a program with the specified date/time](https://www.nirsoft.net/utils/run_as_date.html). Copyright (c) 2007 - 2022 Nir Sofer
- Emulate keystroke
	- [KeyTyperSimulator](https://github.com/mszeu/KeyTyperSimulator)
	- [AutoIt v3](https://www.autoitscript.com/site/autoit/) is a freeware BASIC-like scripting language designed for automating the Windows GUI and general scripting. It uses a combination of simulated keystrokes, mouse movement and window/control manipulation in order to automate tasks in a way not possible or reliable with other languages (e.g. VBScript and SendKeys). AutoIt is also very small, self-contained and will run on all versions of Windows out-of-the-box with no annoying “runtimes” required!
	- [AutoTyper](https://github.com/mathlon26/AutoTyper). This is a Python program that simulates keystrokes based on the contents of a text file. The program uses the pyautogui library to send keystrokes to the active window. You can use this program for various purposes, such as automating text input or testing applications that rely on keyboard input.



## Tips
- [Бесплатно продлеваем Kiwi for Gmail](https://dailysoftwaredeal.com/seller/giveaway-kiwi-for-gmail-windows-mac-1-year-license/). Тут идет покупка, если из приложения не доступно пока. https://www.kiwiforgmail.com/. Code: KiwiForFree
- [Как создать локальную учетную запись в Windows 10](http://windowstips.ru/notes/18570)
- [4 Ways To Boot Into Safe Mode In Windows 10](http://www.digitalcitizen.life/4-ways-boot-safe-mode-windows-10)

- [ms-setting:display and ms-personalization-background problem](http://www.windows10forums.com/threads/ms-setting-display-and-ms-personalization-background-problem.1247/)
Hey Guyz. I found a solution for settings and updates. Download this update [3081424](https://support.microsoft.com/kb/3081424). And download the utility Microsoft Troubleshooter and fix it. Download it from here http://aka.ms/diag_settings
- [Settings doesn’t launch, or launches the Store instead](http://answers.microsoft.com/en-us/windows/forum/windows_10-other_settings/settings-doesnt-launch-or-launches-the-store/ec439819-7ee4-4b4d-abdd-35d82e04c55f)
- [How do I find out which programs have registered global hotkeys in Windows 10?](https://superuser.com/questions/1091942/how-do-i-find-out-which-programs-have-registered-global-hotkeys-in-windows-10)

## Удаления мэпинга сетевой папки
- [How to delete mapped network drives on Windows 10 {QUICK GUIDE}](https://windowsreport.com/delete-mapped-network-drive/). Type: `net use drive letter/delete`
 (for example, if you have a drive mapping using letter G, type net use G:/delete)
- [unmap a drive letter from a folder in Windows 10](https://answers.microsoft.com/en-us/windows/forum/all/unmap-a-drive-letter-from-a-folder-in-windows-10/efa0b5c6-7d15-4451-aa27-4432b822600a)
- Resolved: [Unable to Open/Disconnect a Mapped Drive in Windows 10](https://answers.microsoft.com/en-us/windows/forum/windows_10-files/unable-to-opendisconnect-a-mapped-drive-in-windows/0289115c-0998-45ee-aacb-728d1bd31c01?auth=1):
```

To resolve this issue, please follow the steps on how to disconnect a Mapped drive below:

Right click on Start button > select Command Prompt (Admin).
Type " mountvol /r "
Reboot your computer.
```

## Folder ownership
- COOL! [List all files with certain extensions in Windows folder in a single call](https://stackoverflow.com/questions/17618271/list-all-files-with-certain-extensions-in-windows-folder-in-a-single-call).
`dir /b *.csv *.xsl *.txt > results.txt`
	- [Dir](https://www.microsoft.com/resources/documentation/windows/xp/all/proddocs/en-us/dir.mspx?mfr=true). Displays a list of a directory's files and subdirectories.
- Утилиты командной строки для работы с ACL: `takeown.exe` & `icacl.exe`
Пример использования `icacls` и `takeown` для получения доступа ко всем файлам несистемного диска.
`takeown /f H: /r /d y`
`/r` - нужен для обработки всех вложенных папок
`/d y` - положительно отвечает на стандартный запрос да/нет, который появляется в том случае, если у пользователя нет прав для доступа к подпапкам.
`icacls.exe H:\* /reset /T`
Запускать из под администратора

Став владельцем папок, вы получите доступ к их содержимому, но, скорее всего, не сможете осуществлять запись в них. В этом случае можно взять полный контроль над папками таким образом

`icacls H:\* /grant:r Администратор:F /t`
Вместо имя подставьте имя вашей учетной записи или группы, которой вы хотите дать полный контроль над папками.
`grant:r` - заменяет все текущие права, что имеет смысл в том конкретном случае когда (учетная запись, имевшая права, уже не существует), но далеко не всегда....
- [Windows 7 и сброс прав доступа и владельца файлов](http://tt.erinome.net/2012/07/265)
```
Оказывается, есть другой способ с использованием встроенной в систему утилиты icacls. Она позволяет рекурсивно сбросить права доступа на стандартные для указанного каталога и всего его содержимого. Для этого необходимо запустить командную строку cmd.exe с правами администратора и воспользоваться следующей командой:

icacls.exe "E:\Inaccessible Folder" /reset /T
Вместо E:\Inaccessible Folder следует указать путь к каталогу, где необходимо сбросить старые разрешения.

В отдельных случаях перед запуском icacls может потребоваться утилита takeown:

takeown.exe /f "E:\" /r /d y
icacls.exe "E:\" /reset /T
После завершения работы утилиты все содержимое указанного каталога будет иметь стандартные права доступа вашей системы, он станет доступен для всех пользователей.
```


## Настройка VPN и браузеров
- [How to disable images in firefox](https://support.mozilla.org/en-US/questions/981640)
- [How to turn off images in Firefox](https://www.ghacks.net/2015/03/24/how-to-turn-off-images-in-firefox/)
- [Image Block add-on](https://addons.mozilla.org/en-US/firefox/addon/image-block/)
- COOL! Поднимаем свой собственный VPN.
	- [Как создать свой собственный VPN-сервер прямо на iPhone за 5 минут](https://www.iphones.ru/iNotes/kak-na-iphone-nastroit-svoy-vpn-i-avtomaticheskoe-podklyuchenie-servisa-09-06-2022)
`pivpn` --  вывести список доступных команд для настройки сервера.
`pivpn -a` -- создание нового пользователя.
`pivpn -qr` -- отображение QR-кода конфигурации.
	- [PiVPN](https://pivpn.io/) The simplest way to setup and manage a VPN, designed for Raspberry Pi™.
	- [WireGuard](https://www.wireguard.com/): fast, modern, secure VPN tunnel
WireGuard® is an extremely simple yet fast and modern VPN that utilizes state-of-the-art cryptography.


## RDP
- [Как нажать Ctrl+Alt+Del работая удаленно через RDP ?](https://sysadmin.ru/articles/kak-nazhat-ctrlaltdel-rabotaya-udalenno-cherez-rdp). На помощь нам придет другая комбинация клавиш. Чтобы добиться аналогичного эффекта на удаленном компьютере, нужно нажать комбинацию клавиш `Control+Alt+End` (сокр. `Ctrl+Alt+End`).

## Password Manager
- [Достаём мастер-пароль из заблокированного менеджера паролей 1Password 4](https://habr.com/ru/post/441166/)
- [Bitwarden](https://bitwarden.com/). Solve your password management problems. The easiest and safest way for individuals, teams, and business organizations to store, share, and sync sensitive data.
	- [Family vs Premium?](https://www.reddit.com/r/Bitwarden/comments/7o7vjs/family_vs_premium/)
	- [What are organizations?](https://help.bitwarden.com/article/what-is-an-organization/)
- [Backing Up My Bitwarden Database](https://blog.patshead.com/2019/09/backing-up-my-bitwarden-database.html)
- [Offline management of (writeable) vault items](https://community.bitwarden.com/t/offline-management-of-writeable-vault-items/107)
- [Password Managers: Under the Hood of Secrets Management](https://www.securityevaluators.com/casestudies/password-manager-hacking/). February 19, 2019
- [Альтернативы LastPass. Сравнительная оценка шести парольных менеджеров](https://habr.com/ru/post/434314/)
- [You were not born to remember passwords](https://www.enpass.io/)

## VPN
Замена CiscoAnyConnect
http://macappstore.org/openconnect/
http://www.infradead.org/openconnect/download.html
https://openconnect.github.io/openconnect-gui/ (edited)
https://chocolatey.org/packages/openconnect-gui

## Web camera
- [3 Ways to Fix Camera App Not Working in Windows 10](https://www.top-password.com/blog/fix-camera-app-not-working-in-windows-10/)
- [Как исправить ошибку веб-камеры в Windows 10](https://siniy-ekran.ru/poleznoe/kak-ispravit-oshibku-veb-kamery-v-windows-10/)
!!! Посмотрел по фото на ваш ноутбук: там на клавише Esc случайно не значок перечеркнутой камеры? Если он, то попробуйте либо просто клавишу Esc, либо Fn+эту_клавишу.

## Мышка Logitech
- [Привязка мыши(клавиатуры) logitech (не unifying) к не родному донглу](https://www.cyberforum.ru/mouses/thread2600706.html)

## Photoshop
- COOL! [20 Free Spray Paint Photoshop Brushes with Splatters & Drips](https://blog.spoongraphics.co.uk/freebies/20-free-spray-paint-photoshop-brushes-with-splatters-drips)
- Descreen/Remove pattern [Pattern Suppressor v2.7](http://ft.rognemedia.no/) Free tool for easily removing repeating patterns using Photoshop. Based on FFT
- [ImageJ. FFT filter](https://imagej.net/)
- Manual Descreen step-by-step:
Please follow the below steps that might help you:
1.    The first thing you want to do is scan the newspaper in at a very high resolution.(600dpi). Sometimes you will want to scan the image at an angle to help avoid as much of a moire pattern as possible.
2.    In Photoshop, duplicate the layer and make it a Smart Object – not necessary to do both.
3.    Add a Gaussian Blur of 3.7 pixels to essentially merge the dots and create smoother gradients. This amount may vary depending on the size of the dots and the resolution at which you scanned.
4.    Then apply the Unsharp Mask filter with settings:
	o Amount: 120%
	o Radius: 5px
	o Threshold: 1 level
         Applying too much sharpening will introduce halos around the edges which will take away from the impact of the image and will look very unprofessional.
5.    Resample the image to your end resolution. The resampling will help remove some of the apparent blurriness of the image as well.
6.    At the end, just add a simple Curves Adjustment Layer to add some contrast.

## Steam
- [How to move Single or Multiple Steam Games to another Drive or Folder](https://www.thewindowsclub.com/move-steam-games-another-drive-folder)
- [How to Move a Steam Game to Another Drive, The Easy Way](https://www.howtogeek.com/269515/how-to-move-a-steam-game-to-another-drive-without-re-downloading-it/)
- [Как вернуть деньги за игры, купленные в Steam](http://kanobu.ru/articles/kak-vernut-dengi-za-igryi-kuplennyie-v-steam-369053/)
- [Backup, Restore, Move Steam games with Steam Library Manager](https://www.thewindowsclub.com/steam-library-manager)
- Вручную в explorer. [Moving a Library](https://www.cloudwards.net/how-to-move-steam-games/)
```
Step 1: Create a Steam library folder following the instructions above, then close the Steam client.
Step 2: Browse to the Steam installation folder to be moved. Once there, delete all files and folders except for “Steamapps” and “userdata.”
Step 3: Cut and paste the Steam folder into the new path you created. For instance, it could be called E:\SteamLibrary
Step 4: Reopen Steam and log in, then point Steam to your new directory and verify game files if necessary. If you encounter issues, try uninstalling and reinstalling Steam. The Steam support page can also be helpful.
```
- [Steam Console](https://steamcommunity.com/sharedfiles/filedetails/?id=873543244). Добавить к ярлыку `-console`
- Как создать ярлыки по установленным Steam играм
	- В библиотеке Steam выбрать игры и в меню на правом клике выбрать "Создать ярлыки"
	- [Steam Shortcut Generator - Automatically generate shortcuts for all installed Steam games!](https://www.reddit.com/r/Steam/comments/g26g0g/steam_shortcut_generator_automatically_generate/). Python [source](https://github.com/JeeZeh/steam-shortcut-generator)
	- [How do I add start menu items to a Steam game after the installation?](https://gaming.stackexchange.com/questions/52485/how-do-i-add-start-menu-items-to-a-steam-game-after-the-installation)
	- [bernstein82/SteamShortcutCreator.ps1](https://gist.github.com/bernstein82/f0e14a3d38ed1c3ba36b)
- [Need for Speed Most Wanted PC Fullscreen](https://answers.ea.com/t5/Need-for-Speed-Most-Wanted/Need-for-Speed-Most-Wanted-PC-Fullscreen/td-p/5375272)
```
Slight correction to a previous answer. And if you tab out of this one and lose full screen, hit alt enter and you're back in full screen
1. Open up the launcher
2. Click on NFS:MW but do not launch the game
3. Click on Settings [The Gear Icon]
4. Go to "Game Properties"
5. Click on "Advance Launch Settings"
6. Copy and Paste into the bar " -fullscreen "
```


# Нужные утилиты
- [1Password]()
- [ABBYY FineReader 11]()
- [Acrobat Reader DC]()
- [Advanced PDF Password Recovery]()
- [AIMP]()
- [AOMEI Backupper Professional]()
- [AOMEI Partition Assistant Pro Edition 6.0]()
- [Archivarius 3000]()
- [Arduino]()
- [Arq]()
- [AstroGrep]()
- [Atom]()
- [Aurora HDR 2018]()
- [Balsamiq Mockups 3]()
- [Bash на Ubuntu]()
- [Bitvise SSH Client]()
- [Bitwarden]()
- [Brackets]()
- [Bulk Rename Utility]()
- [Camtasia 9]()
- [Cisco AnyConnect Secure Mobility Client]()
- [Codec Tweak Tool]()
- [ConEmu (x64)]()
- [CorelDRAW X7 (64-Bit)]()
- [CPUID CPU-Z]()
- [DBeaver]()
- [DeepGit]()
- [dnGREP]()
- [Dropbox]()
- [Duplicate Cleaner Pro]()
- [EmEditor]()
- [Evernote]()
- [Everything]()
- [EXIF ReName]()
- [Falcon SQL Client]()
- [Far]()
- [Firefox]()
- [Foxit PDF Editor]()
- [Git Shell]()
- [Google Chrome NO SANDBOX]()
- [Google Web Designer]()
- [Google Диск]()
- [Grammarly]()
- [Hard Disk Sentinel]()
- [HDD Regenerator]()
- [HFS+ for Windows]()
- [Inkscape 0.91]()
- [Instant Eyedropper]()
- [Intel(R) Driver Update Utility 2.4]()
- [Intel(R) HD Graphics Control Panel]()
- [Internet Explorer]()
- [iTunes]()
- [IZArc]()
- [JetBrains DataGrip 2019.1.4 x64]()
- [JetBrains PyCharm 2017.1.3 x64]()
- [Kaspersky Internet Security]()
- [Kaspersky Passwords]()
- [KeepVid Pro]()
- [Kid3]()
- [Kiwi for Gmail]()
- [LameXP]()
- [LEGO MINDSTORMS Education EV3]()
- [Lenovo Solution Center]()
- [Listary]()
- [LogExpert]()
- [LSEConfig]()
- [Luminar 2018]()
- [MarkdownPad 2]()
- [MediaInfo]()
- [MEGAsync]()
- [Melloware PlacesBar Editor]()
- [Microsoft Edge]()
- [MobileBalance]()
- [MTC TB]()
- [mTail]()
- [mTorrent]()
- [NCH Suite]()
- [Nokia PC Suite]()
- [OpenConnect-GUI VPN client]()
- [OpenVPN GUI]()
- [ORPALIS PDF Reducer Pro 3]()
- [Outlook 2016]()
- [Paragon HFS+ for Windows]()
- [Passware Kit Forensic 2017 v1]()
- [Password Agent]()
- [PDFsam Basic](https://pdfsam.org/pdfsam-basic/) - a free, open source, multi-platform software designed to split, merge, extract pages, mix and rotate PDF files.
- [Photoshop 2015]()
- [Plex Media Server]()
- [Postman]()
- [PowerGREP 4]()
- [PowerGREP 5]()
- [PowerPoint 2016]()
- [PowerShell-6.0.0-beta.2]()
- [Process Hacker 2]()
- [Project 2016]()
- [PuTTY]()
- [R i386 3.6.1]()
- [R x64 3.6.1]()
- [RAMDisk Configuration Utility]()
- [Recuva]()
- [Rename-It!]()
- [Resilio Sync]()
- [RStudio]()
- [Samsung Magician]()
- [Search Everything]()
- [Similarity]()
- [Skype]()
- [Slack]()
- [Smart Switch]()
- [SmartDown]()
- [SmartGit]()
- [Snagit 13]()
- [SoftorinoYoutubeConverter2]()
- [SourceTree]()
- [Steam]()
- [SyncToy 2.1(x64)]()
- [Tag&Rename]()
- [TeamViewer 14]()
- [Telegram]()
- [TextPipe Pro Evaluation]()
- [TigoTago]()
- [Tower]()
- [TreeSize (Administrator)]()
- [TripMode]()
- [Typora]()
- [UltraISO]()
- [Uplay]()
- [ViceVersa PRO]()
- [VidCoder Beta]()
- [VideoPad Video Editor]()
- [VideoProc]()
- [Visio 2016]()
- [WALTR2]()
- [WebSite-Watcher]()
- [WhatsApp]()
- [WhereIsIt]()
- [WinDjView]()
- [Windows Hotkey Explorer]()
- [Windscribe]()
- [WinEdt 10]()
- [Wing IDE 6.0]()
- [WinSCP]()
- [Wireshark]()
- [Wolfram Mathematica 11.3]()
- [Word 2016]()
- [XmlPad]()
- [XnView]()
- [Xshell 5]()
- [Xshell 6]()

## Video
- [19 команд ffmpeg для любых нужд](https://habr.com/ru/post/171213/)
- [Windows `.bat` script that checks video file integrity using `ffmpeg.exe`](https://github.com/describe19/check-video)



## Руководство по установке подсистемы Windows для Linux в Windows 10
- [Install WSL with a single command now available in Windows 10 version 2004 and higher](https://devblogs.microsoft.com/commandline/install-wsl-with-a-single-command-now-available-in-windows-10-version-2004-and-higher/). In the latest Windows Insider Preview builds, you can install everything you need to run WSL just by running `wsl.exe --install`
- [Возможны два варианта установки подсистемы Windows для Linux (WSL)](https://docs.microsoft.com/ru-ru/windows/wsl/install-win10)
- [Upgrading from WSL1 to WSL2](https://dev.to/adityakanekar/upgrading-from-wsl1-to-wsl2-1fl9)
- Сравнительная таблица [How to Update from WSL to WSL 2 in Windows 10](https://www.tenforums.com/tutorials/164301-how-update-wsl-wsl-2-windows-10-a.html)
- [Enable the Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10#step-4---download-the-linux-kernel-update-package)
- WSL2, информация от Микрософт. 
    - Для получения сведений о ключевых различиях с WSL 2 перейдите на страницу https://aka.ms/wsl2
    - WSL 2 требуется обновление компонента ядра. Дополнительные сведения см. на странице https://aka.ms/wsl2kernel
Please make sure that virtualization is enabled inside of your computer's BIOS. The instructions on how to do this will vary from computer to computer, and will most likely be under CPU related options.
- [Install Windows Subsystem for Linux 2 in Windows 10](https://winaero.com/install-windows-subsystem-for-linux-2-in-windows-10/)
- [Automatically Configuring WSL](https://devblogs.microsoft.com/commandline/automatically-configuring-wsl/)
- Доставляем утилиты(https://onstartup.ru/obrabotka-teksta/xsltproc/):
```
sudo apt update
sudo apt install xsltproc
sudo apt install zip
```

### сжимаем диск, занятый WSL
- [How do I get back unused disk space from Ubuntu on WSL2?](https://superuser.com/questions/1606213/how-do-i-get-back-unused-disk-space-from-ubuntu-on-wsl2)
	- [wslcompact](https://github.com/okibcn/wslcompact)
- WSL data partition. `docker-desktop-data.vhdx`
- [How to reduce size of docker data volume in Docker Desktop for Windows v2](https://dev.to/marzelin/how-to-reduce-size-of-docker-data-volume-in-docker-desktop-for-windows-v2-5d38)
- [Docker Desktop WSL ext4.vhdx too large](https://stackoverflow.com/questions/70946140/docker-desktop-wsl-ext4-vhdx-too-large).
If you're willing to wipe all of your docker data, open the Docker Desktop client, click the bug icon in the top bar, and then click Clean/Purge data:
- Рабочее решение! [Docker Desktop WSL ext4.vhdx too large](https://stackoverflow.com/questions/70946140/docker-desktop-wsl-ext4-vhdx-too-large)
```
I am putting the gist of the instructions below for reference but the guide above is more complete.
First make sure all WSL instances are shut down by opening an administrator command window, and typing:
>> wsl --shutdown 
Verify everything is stopped by:
>> wsl.exe --list --verbose
Then start diskpart:
>> diskpart
and inside diskpart type:
DISKPART> select vdisk file="<path to vhdx file>"
For example:
DISKPART> select vdisk file="C:\Users\user\AppData\Local\Packages\CanonicalGroupLimited.Ubuntu22.04LTS_12rqwer1sdgsda\LocalState\ext4.vhdx"
it should respond by saying DiskPart successfully selected the virtual disk file.
Then to shrink
DISKPART> compact vdisk
```
- REM Чистка кэша (3ий сигнал, самая глубокая очистка)
REM https://unix.stackexchange.com/questions/87908/how-do-you-empty-the-buffers-and-cache-on-a-linux-system
```
echo (Echo) Clean cache
%WINDOWS_INK%\_ubuntu.exe run "sudo sh -c 'sync && echo 3 > /proc/sys/vm/drop_caches'"
```

### Переносим WSL на другой диск
- [Basic commands for WSL](https://learn.microsoft.com/en-us/windows/wsl/basic-commands)
- [Move WSL to Another Drive](https://blog.iany.me/2020/06/move-wsl-to-another-drive/)
- Рабочий вариант с подробными объяснениями !!! [Move WSL File System to another Drive](https://dev.to/equiman/move-wsl-file-system-to-another-drive-2a3d)
```
wsl --list --verbose
wsl --shutdown
wsl --export Ubuntu D:\backup\ubuntu.tar
wsl --unregister Ubuntu
wsl --import Ubuntu D:\WSL\Ubuntu D:\backup\ubuntu.tar
```
Точно также перетаскиваем образы Docker Desktop (не работает, не запускается потом докер !!!)
```
wsl --export docker-desktop-data d:\backup\docker-desktop-data.tar
wsl --unregister docker-desktop-data
wsl --import docker-desktop-data D:\WSL\DockerDesktopWSL D:\backup\docker-desktop-data.tar
```
овторно импортировать можно выполнив в директории `%USERPROFILE%\AppData\Local\Docker\wsl\data`
```
wsl --import-in-place docker-desktop-data ext4.vhdx
```
Но можно перетащить в интерфейсе Docker Desktop: `Settings/Resources/Disk Image Location`. Он сам создаст директорию и перетащит образ диска.
И я понял почему не перетаскивался. Он поместил образ в подпапку `D:/WSL/DockerDesktopWSL/data` !!!
На эту тему есть отдельная статейка [Move docker-desktop-data distro out of System Drive](https://dev.to/kim-ch/move-docker-desktop-data-distro-out-of-system-drive-4cg2)
НЕОБХОДИМА ПЕРЕЗАГРУЗКА WINDOWS!!!
Есть масса подводных камней, читаем [Disk image location is not changing #13345 {Open}](https://github.com/docker/for-win/issues/13345)

### Переносим docker образы с системного диска
- [How To Change Docker Data Path On Windows 10](https://devops.tutorials24x7.com/blog/how-to-change-docker-data-path-on-windows-10)
- [On Windows 10, what is the proper way to install docker on another drive (not C:\)?](https://forums.docker.com/t/on-windows-10-what-is-the-proper-way-to-install-docker-on-another-drive-not-c/120428)
- [Docker Engine on Windows](https://learn.microsoft.com/en-us/virtualization/windowscontainers/manage-docker/configure-docker-daemon)
- [Change Docker Desktop settings on Windows](https://docs.docker.com/desktop/settings/windows/#features-in-development)

## Ubuntu в WSL
- [WSL mount external and network drives](https://www.scivision.dev/mount-usb-drives-windows-subsystem-for-linux/).
Для внешнего диска такая команда отрабатывает: `mount -t drvfs s: /mnt/s`
- [Is there a way to mount an external drive when it becomes available in WSL?](https://superuser.com/questions/1734353/is-there-a-way-to-mount-an-external-drive-when-it-becomes-available-in-wsl)

## BitLocker
- [Изучаем и вскрываем BitLocker. Как устроена защита дисков Windows и как ее взломать](https://xakep.ru/2017/02/23/bitlocker-hacking/)
- Вот ведь, прямо мой случай.  [Bitlocker is off but C drive shows Bitlocker encrypted Wondows 10](https://social.technet.microsoft.com/Forums/en-US/a6c735ab-62d2-47a2-bb0c-aff9a3db1523/bitlocker-is-off-but-c-drive-shows-bitlocker-encrypted-wondows-10?forum=win10itprosecurity)
Смотрим статус командой `manage-bde -status c:`
Видим, что 
```
Том C: [Windows ]
[Том с операционной системой]

    Размер:                           237,46 ГБ
    Версия BitLocker:                 2.0
    Состояние преобразования:         Зашифровано только занятое место
    Зашифровано (процентов):          100,0%
    Метод шифрования:                 XTS-AES 128
    Состояние защиты:                 Защита отключена
    Состояние блокировки:             Разблокировка
    Поле идентификации:               Неизвестный
    Предохранители ключа:              не обнаружены


C:\windows\system32>manage-bde -status d:
Шифрование дисков BitLocker: версия средства настройки: 10.0.19041
(C) Корпорация Майкрософт (Microsoft Corporation), 2013. Все права защищены.

Том D: [Data]
[Том данных]

    Размер:                           931,51 ГБ
    Версия BitLocker:                 2.0
    Состояние преобразования:         Выполняется шифрование
    Зашифровано (процентов):          13,3%
    Метод шифрования:                 XTS-AES 128
    Состояние защиты:                 Защита отключена
    Состояние блокировки:             Разблокировка
    Поле идентификации:               Неизвестный
    Автоматическая разблокировка:     Отключен
    Предохранители ключа:              не обнаружены
```
- [Solved for Dell](https://www.dell.com/community/Windows-10/BitLocker-need-a-key-but-I-never-installed-it/m-p/7427359#M14749)
* Restart the system
* At the Dell Logo keep tapping F2
* You will enter the BIOS screen
* Go to Secure Boot header, expand and select Expert Key Management
* Click the Restore Settings button
* Select Factory Settings
* Press OK
* Exit the BIOS and restart

Windows should now launch as it did before, even my last browser session appeared and lost nothing from c:\ drive!
- [BitLocker](https://en.wikipedia.org/wiki/BitLocker)
- [Secure Boot: как отключить защиту или настроить правильно в UEFI](https://gamesqa.ru/kompyutery/secure-boot-kak-otklyuchit-zashhitu-ili-nastroit-pravilno-v-uefi-12565/)
- !!! [HP PCs - BitLocker Encryption Is Enabled by Default](https://support.hp.com/in-en/document/c06458046). CAUTION: If you cannot find your BitLocker recovery key when needed, you will lose access to data on encrypted drives.
- [HP PCs - Using BitLocker or Finding the Recovery Key (Windows 10)](https://support.hp.com/in-en/document/c06432394)
- РЕШЕНИЕ: частичное шифрование включается в WinPro при связке ее с MS аккаунтом. Отключить можно в параметрах учетной записи в win -- откатается все назад.
`Параметры > Обновление и безопасность > Шифрование устройства`

# Настройка рабочего Windows10 с нуля
- Отключаем в ярлыках Рабочего стола тени шрифта (описано выше, "Как отключить в ярлыках Рабочего стола тени шрифта").
- Ставим английский язык по умолчанию и при входе в систему (описано выше, "Windows: Как изменить язык при входе в систему?").
- Отключаем автосон (описано выше, "Компьютер уходит в сон через 2 минуты")
- Настроим значки на рабочем столе (описано выше, "Отображение значков на рабочем столе в Windows"). `Пуск > Параметры  > Персонализация > Темы > Связанные параметры > Параметры значков рабочего стола.` 
- Ставим Steam / Start10, Fences
- Устанавливаем Ubuntu под Windows [WSL 2](https://docs.microsoft.com/ru-ru/windows/wsl/install-win10)
	- ОБЯЗАТЕЛЬНО делаем root-пользователя дефолтным. Зайти в командную строку cmd и написать: `ubuntu2004 config --default-user root`
	- Назначить wsl2 сетевой диск (например, `W`): Найти `\\wsl$\` в проводнике и перейти в папку `Ubuntu-хх.хх` Правой кнопкой нажать на название и выбрать в выпадающем меню – Подключить сетевой диск.
	- Корневая папка проектов: `/opt`. Для удобства ее стоит сделать доступной всем пользователям: `sudo chmod -R 777 /opt`
- Ставим Package Manager [Chocolatey](https://chocolatey.org/)
   or/and 
- [Scoop](https://scoop.sh/) A command-line installer for Windows
- Ставим FarManager [`choco install far`](https://community.chocolatey.org/packages/Far)
- Устанавливаем FiraCode для RStudio. [`choco install firacode`](https://community.chocolatey.org/packages/FiraCode)
- Устанавливаем [Windows Terminal]() и для него шрифт `Cascadia Code`.
	- [Update code font from Consolas to Cascadia Code with ligature](https://weblogs.asp.net/dixin/update-code-font-from-consolas-to-cascadia-code-with-ligature)
	- [microsoft/cascadia-code](https://github.com/microsoft/cascadia-code)
	- [Install with chocolatey](https://community.chocolatey.org/packages/cascadiacode). `choco install cascadiacode`
	- [Cascadia Mono Font 2108.26](https://community.chocolatey.org/packages/cascadiamono). `choco install cascadiamono`
	- [Конфигурируем меню Windows Termial](https://codeandkeep.com/Tmux-on-Windows/). If you want to set this as your default shell in the Windows Terminal, you can update the settings `Ctrl + ,` to do so. Replace the GUID in defaultProfile with the one for your Linux app. You can find the GUID in the list section under profiles. Set this GUID as the defaultProfile, and this will be the shell that opens by default.
- Ставим `Link Shell Extension` с [официальной страницы](https://schinagl.priv.at/nt/hardlinkshellext/hardlinkshellext.html)
- Ставим [DataRAM RAMDisk](http://memory.dataram.com/products-and-services/software/ramdisk) и спасаем SSD от Chrome (см выше по тексту).
RAM Disk на `Y:`, выделяем под кэш Хрома 512 Мб, делаем Junction кэша хрома.
- Ставим [OpenVPN Community edition](https://openvpn.net/community-downloads/)
- Ставим SSH клиент [Bitvise SSH Client/xShell]
- Ставим Zentimo xStorage Manager
- Ставим SnagIt, блокируем его в файерволе (wf.msc) или касперском. [Best practices for configuring Защитник Windows firewall](https://docs.microsoft.com/ru-ru/windows/security/threat-protection/windows-firewall/best-practices-configuring).
Переносим базы SnagIt
	- [Snagit (Windows): Move Unsaved Captures to a Different Computer](https://support.techsmith.com/hc/en-us/articles/203731768-Snagit-Windows-Move-Unsaved-Captures-to-a-Different-Computer)
	- [Snagit (Windows): Manually Restore a Datastore](https://support.techsmith.com/hc/en-us/articles/203732148-Snagit-Windows-Manually-Restore-a-Datastore)
- Мигрируем конфигурацию Anydesk. [Backup & Restore Settings and ID](https://support.anydesk.com/AnyDesk_ID_and_Alias)
[Export saved connections (on Mac) is it possible?](https://www.reddit.com/r/AnyDesk/comments/jwlboc/export_saved_connections_on_mac_is_it_possible/). If you have a business licence then you can export them as csv files otherwise no you can't.
Но список последних подключений можно найти в конф файле: [`C:\Users\'UserName'\AppData\Roaming\AnyDesk\user.conf`](https://gist.github.com/oropesa/a058c813ffb25ee696104d660cca6e5a)
```
(In both Windows)
1. Go to C:\Users\{USER}\AppData\Roaming\AnyDesk
2. Copy & Paste 'thumbnails'
3. Open 'user.conf'
4. Replace the line 'ad.roster.items='
5. Done.
```
- Ставим EmEditor (19.9.4 проверен), отключаем в Касперском доступ в инет на `EMURASOFT`. Сетевой экран/Настройки программ.
	- Ставим проверку русского языка [Spellcheck](https://www.emeditor.com/text-editor-features/more-features/spellcheck/). На момент установки словари жили [здесь](https://extensions.openoffice.org/en/project/slovari-dlya-russkogo-yazyka-dictionaries-russian). After download a dictionary, change the file extension from .oxt to .zip, extract the Zip file, and then copy *.dic and *.aff files into the Dictionaries sub folder of the EmEditor install folder (usually C:\Program Files\EmEditor\Dictionaries).
	- Ставим для *.R подсветку синтаксиса [EmEditor Syntax ](https://www.emeditor.com/wpfb_file_category/syntax-files/), а именно, [R syntax file](https://www.emeditor.com/files/r-esy/). Инструкция по установке [How can I install an EmEditor syntax file?](http://www.emeditor.org/en/faq_setup_setup_syntax.html).
	- Включаем отображение номеров строк. [EmEditor How to: To Display Line Numbers and or the Ruler](http://www.emeditor.org/en/howto_customize_usage_ruler.html) To Display Line Numbers and or the Ruler
1.Click Properties for Current Configuration (if you want to change only the current configuration) or Properties for All Configuration (if you want to change all configurations) to display the General tab.

2.Click Show Line Numbers to display line numbers, or click Show Ruler to display the ruler.
	- Включаем отображение специсимволов: [Show Marks (Space Tabs EOL) in Selection only](https://www.emeditor.com/forums/topic/show-marks-space-tabs-eol-in-selection-only/)
I just realized that we can do that already at our own:

        1.) Enable all (or the wanted) whitespace marks from menu “View > Marks”
        2.) Go to menu “Tools > Properties for xxx Configuration”
        3.) Click the [Display] tab and select “Returns, tabs, EOL”
        4.) choose Text Color > Custom and set it to white
        (or to your chosen background color, if not default), (of course you could also set the color to a light grey for example)
        5.) close the dialog with the [OK] button
        Done.

Now the marks are invisible on normal work, but visible on selection only.
- В AstroGrep настраиваем открытие файлов в emeditor: `"*" "C:\Program Files\EmEditor\EmEditor.exe" "/l %2 %1"`
- Ставим SmartGit, переносим настройки из `%appdata%\syntevo\SmartGit\<version>\`. Читаем [How to import old settings/repositories](https://stackoverflow.com/questions/45837545/how-to-import-old-settings-repositories) `*.yml` files
- Настраиваем Касперского для разрешения доступа Edge в инет. [Cannot open websites in Google Chrome and Edge Chromium when working with Kaspersky Security 10 for Windows Server](https://support.kaspersky.com/15392)
- После установки Касперского в режиме администратора отключаем штатный брандмауэр Windows `netsh advfirewall set allprofiles state off`
- В Google Chrome включаем режим чтения. Делается это через экспериментальные настройки. `chrome://flags/#enable-reader-mode`
- Отключаем встроенный Windows Defender. Связано это с подобными фокусами: [Штатный антивирус в Windows 10 стал помечать клиент uTorrent как вредоносное ПО, автоматически удалять его и препятствовать его повторной установке.](https://www.cnews.ru/news/top/2021-06-16_microsoft_voznenavidela_samyj)
- [Keyboard shortcuts in Windows](https://support.microsoft.com/en-us/windows/keyboard-shortcuts-in-windows-dcc61a57-8ff0-cffe-9796-cb9706c75eec)
- TODO: инкорпорировать частично настройки Богдана.
- Настраиваем Docker
	- Ставим **Docker Desktop** по инструкции [Начало работы с удаленными контейнерами Docker в WSL 2](https://docs.microsoft.com/ru-ru/windows/wsl/tutorials/wsl-containers)
	- Docker может жрать немало памяти (гигабайты), поэтому есть инструкции по его тушению в случае ненужности. [Stopping Vmmem from using RAM](https://stackoverflow.com/questions/64165192/stopping-vmmem-from-using-ram). just `wsl --shutdown` in PowerShell or cmd.
	- Собираем минимальный докер в концепции `renv` по репозиторию Богдана, запускаем изнутри wsl: `docker build -f rstudio-server.Dockerfile .` Можно добавить `-t rstudio-server.v1:4.1.2` - будет тэг к образу. Можно добавить `-v /opt:/opt` - будет зеркало папки из WSL в контейнер.
	- Тэг надо вешать, иначе потом проблемы с запуском. [How to run the docker image with <none> tag](https://stackoverflow.com/questions/55115622/how-to-run-the-docker-image-with-none-tag). Команды по переименование тэгов можно посмотреть здесь: [docker tag](https://docs.docker.com/engine/reference/commandline/tag/), в частности `docker tag 0e5574283393 fedora/httpd:version1.0`
	- Запускаем R командой `docker run -ti rstudio-server:4.1.2 /usr/local/bin/R` (или `/bin/bash` для консоли).
	- [Изучаем Docker, часть 5: команды](https://habr.com/ru/company/ruvds/blog/440660/). Нашел проблемку с `with-contenv` [run script when dockercontainer starts?](https://askubuntu.com/questions/1054664/run-script-when-dockercontainer-starts)
	- [WSL2 (docker) ports are not openend on host](https://stackoverflow.com/questions/69838995/wsl2-docker-ports-are-not-openend-on-host)
	- [Using Docker Desktop and Docker Hub Together – Part 1](https://www.docker.com/blog/using-docker-desktop-and-docker-hub-together-part-1/)
- Настраиваем Outlook (опционально):
	- [Создание подписи в Outlook и ее добавление в сообщения](https://support.microsoft.com/ru-ru/office/%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5-%D0%BF%D0%BE%D0%B4%D0%BF%D0%B8%D1%81%D0%B8-%D0%B2-outlook-%D0%B8-%D0%B5%D0%B5-%D0%B4%D0%BE%D0%B1%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5-%D0%B2-%D1%81%D0%BE%D0%BE%D0%B1%D1%89%D0%B5%D0%BD%D0%B8%D1%8F-8ee5d4f4-68fd-464a-a1c1-0e1c80bb27f2). Откройте новое сообщение. Меню Сообщение, выберите пункт Подписи> подписи.
	- [Импорт и экспорт контактов из Outlook](https://office-apps.net/faq-office/249-import-i-eksport-kontaktov-v-outlook.html). Проводится через Экспорт/Импорт.
- Ставим FineReader. У меня пашет 11.0.101.583 Corporate Edition (CE)
- [Удаленное управление Kaspersky Free](https://forum.kasperskyclub.ru/topic/80660-udalennoe-upravlenie-kaspersky-free/). Важно для возможности настройки с помощью AnyDesk и др.
Разрешение на удаленное управление антивирусом включила (галочку поставили) - квадратик стал зеленый ... )))
добавить программу в список Доверенных программ https://support.kaspersky.com/KFA/21.3/ru-RU/201385.htm и включить исключение Разрешить взаимодействие с интерфейсом Kaspersky Free. 

## Поиск дубликатов изображений в Windows
- [Find visually similar images for a given image file (on Windows)](https://softwarerecs.stackexchange.com/questions/17046/find-visually-similar-images-for-a-given-image-file-on-windows)
- [Top 5 Best Duplicate Photo Cleaners For Windows 10](https://yourstory.com/mystory/top-5-duplicate-photo-cleaners-for-windows-10/amp)
- [TinEye Reverse Image Search](https://tineye.com/)
TinEye browser extensions are the fastest way to search for images online.

# Утилиты для синхронизации и частное облако
- [Syncthing](https://syncthing.net/)
	- [Создаём личное облачное хранилище. Syncthing](https://hacker-basement.ru/2019/05/26/private-cloud-syncthing/)
	- [Nextcloud](https://nextcloud.com/). The self-hosted productivity platform that keeps you in control
- [Resilio Sync](https://www.resilio.com/). Universal File Delivery for the Enterprise.
Unify, control, and accelerate global file data, securely
- copy
	- [robocopy](https://learn.microsoft.com/ru-ru/windows-server/administration/windows-commands/robocopy) Копирует данные файла из одного расположения в другое.
	- [Robocopy](https://ru.wikipedia.org/wiki/Robocopy) (от англ. Robust File Copy) — утилита командной строки для репликации (не просто копирования) каталогов (папок). Она была доступна как часть Windows Resource Kit и представлена как стандартный компонент Windows Vista, Windows 7 и Windows Server 2008. Robocopy функционально заменяет Xcopy, с большим количеством опций.
	- [Использование Robocopy для синхронизации и резервного копирования файлов, примеры](https://winitpro.ru/index.php/2020/05/13/robocopy-sinxronizaciya-i-rezervnoe-kopirovanie-fajlov/)


# Миграция с gmail на yandex.mail
- [Для выноса данных из Google: https://takeout.google.com]
- [How to Import MBOX to Yandex.Mail – 2 Easy Methods](https://www.adviksoft.com/blog/import-mbox-to-yandex-mail/)
- [Настройка почтовых программ на компьютере
Mozilla Thunderbird](https://yandex.ru/support/mail/mail-clients/mozilla-thunderbird.html)
- [Как лучше перенести доменную почту с gmail на yandex?](https://qna.habr.com/q/303103)

# Win timing
- [Calculate time difference in Windows batch file](https://stackoverflow.com/questions/9922498/calculate-time-difference-in-windows-batch-file)
- [7 Ways to Measure Time Taken to Complete a Batch File or Command Line Execution](https://www.raymond.cc/blog/measure-time-taken-to-complete-a-batch-file-or-command-line-execution/). Рулит доп. утилита `ptime` весом в 20 кб.
- [How-to: Calculate a time difference with tdiff.cmd](https://ss64.com/nt/syntax-tdiff.html)
- [7 способов измерить время, необходимое для выполнения командного файла или выполнения командной строки](https://culhu.ru/archives/31596):
	- [ptime.exe](http://www.pc-tools.net/win32/ptime/) - Accurately measure program execution time
	- TimeThis.exe -- официальный инструмент Microsoft из комплекта ресурсов Windows 2000

# Настройка приложений из MS Store
- [Как создать ярлык приложения из Microsoft Store на рабочем столе](https://comp-security.net/%D0%BA%D0%B0%D0%BA-%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D1%82%D1%8C-%D1%8F%D1%80%D0%BB%D1%8B%D0%BA-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F-%D0%B8%D0%B7-microsoft-store/)
После установки такого приложения из Microsoft Store оно появляется в списке приложений в меню «Пуск». Оттуда приложение можно закрепить на начальном экране или на панели задач. Но, из меню «Пуск» нельзя создавать ярлык на рабочем столе, что создает неудобства для пользователей, которые привыкли запускать программы именно с помощью ярлыков.
	1. `Win-R` и в открывшемся окне выполнить команду `shell:AppsFolder`
	2. Чтобы создать ярлык на рабочем столе нужно найти здесь нужную программу, кликнуть по ней правой кнопкой мышки и выбрать пункт «Создать ярлык».
	
# curl
- [curl](https://curl.se/) command line tool and library for transferring data with URLs (since 1998)
- [Windows 10](https://everything.curl.dev/get/windows) comes with the curl tool bundled with the operating system since version 1804. If you have an older Windows version or just want to upgrade to the latest version shipped by the curl project, download the latest official curl release for Windows from curl.se/windows and install that.
  Скачал последнюю версию `curl` и просто всунул ее в `Windows/System32`. Но все равно не заработало, пошла ошибка `0x60`. Не находил сертификат.
  [По инструкции](https://curl.se/docs/sslcerts.html) засунул из этого же дистрибутива свежий сертификат туда же.
  If you are using the curl command line tool, you can specify your own CA cert file by setting the environment variable CURL_CA_BUNDLE to the path of your choice.
If you are using the curl command line tool on Windows, curl will search for a CA cert file named "curl-ca-bundle.crt" in these directories and in this order:
	- application's directory
	- current working directory
	- Windows System directory (e.g. C:\windows\system32)
	- Windows Directory (e.g. C:\windows)
	- all directories along %PATH%

# image magick
- [Install ImageMagick @ Ubuntu] `sudo apt install imagemagick`
- [Image Resizer Утилита](https://learn.microsoft.com/ru-ru/windows/powertoys/image-resizer)
- [Mogrify subfolders and keep original directory structure](https://stackoverflow.com/questions/27518256/mogrify-subfolders-and-keep-original-directory-structure)
- [Resize multiple images with imagemagick from a folder to other (and keep the name) with a command](https://askubuntu.com/questions/1068850/resize-multiple-images-with-imagemagick-from-a-folder-to-other-and-keep-the-nam)
- [Mogrify subfolders and keep original directory structure](https://stackoverflow.com/questions/27518256/mogrify-subfolders-and-keep-original-directory-structure)
- [Inline Image Modification](https://imagemagick.org/script/mogrify.php)
- [Resize all images in subdirectories](https://www.davd.io/resize-all-images-in-subdirectories/) `find . -name "*.jpg" -print0 | xargs -0 mogrify -resize 2200x2200`
- [Batch resize images and output images to new folder with ImageMagick](https://stackoverflow.com/questions/14304480/batch-resize-images-and-output-images-to-new-folder-with-imagemagick)
- [How do I batch-resize images in ImageMagick while maintaining aspect ratio and a max width and height?](https://stackoverflow.com/questions/56305138/how-do-i-batch-resize-images-in-imagemagick-while-maintaining-aspect-ratio-and-a)
- [Command-line Basics: Resizing Images with ImageMagick](https://www.digitalocean.com/community/tutorials/workflow-resizing-images-with-imagemagick)

# эмулятор Android на Windows
- [BlueStack](https://www.bluestacks.com/)

# wake-up
- [How To Automatically Turn On Computer and/or Wake Computer Up](https://learn.microsoft.com/en-us/answers/questions/422921/how-to-automatically-turn-on-computer-and-or-wake)
- [How to Schedule Windows 10 Wake from Sleep](https://www.ubackup.com/windows-10/windows-10-schedule-sleep-and-wake.html)

# log viewer
- [Tailviewer](https://kittyfisto.github.io/Tailviewer/). A fast, free and open source log viewer for Windows
- [LogExpert](https://github.com/zarunbal/LogExpert). Windows tail program and log file analyzer.
- Платный [LogViewPlus](https://www.logviewplus.com/tail-for-windows.html)

# захват и запись экрана
- [LightShot](https://app.prntscr.com/ru/). Самый быстрый и удобный способ сделать скриншот.
- [OBS Studio](https://obsproject.com/ru). Бесплатная программа с открытым исходным кодом для записи видео и потокового вещания.

# Работа с облачными хранилищами
- [RaiDrive](https://www.raidrive.com/)
- [Air Explorer](https://www.airexplorer.net/ru/pro/)

# пропал Alt-Tab
- [How to Fix Alt-Tab Shortcut Not Working on Windows 10](https://softwarekeep.com/help-center/how-to-fix-alt-tab-shortcut-not-working-on-windows-10)