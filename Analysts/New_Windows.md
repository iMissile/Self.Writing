# Установка Windows с диска
- COOL! Лучшее решение. [Rufus](https://rufus.ie/ru_RU.html). Простое создание загрузочных USB-дисков

# Package manager
- COOL! [Chocolatery. The Package Manager for Windows](https://chocolatey.org/). Modern Software Automation

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

# Переход на SSD
- [Samsung SSD 850 EVO 250GB – Problems And Their Solutions](http://webfrst.com/samsung-ssd-850-evo-250gb-problems-solutions/)
- [Программа SSD Ready](https://www.ssdready.com/ssdready-ru/). Узнайте как долго у вас будет работать SSD диск
- [RAMDisk, или что делать если у вас в компьютере 128 гигабайт оперативной памяти](https://geektimes.ru/company/kingston_technology/blog/277610/)
- RAMDisks:
	- [SoftPerfect RAM Disk](http://forum.ru-board.com/topic.cgi?forum=35&topic=47817&start=40#lt)
	- Остановился на этом. [DataRAM RAMDisk](http://memory.dataram.com/products-and-services/software/ramdisk)
	- [Primo Ramdisk (VSuite Ramdisk II) - Powerful RAM Disk Emulator for Windows](http://www.romexsoftware.com/en-us/primo-ramdisk/)
- [Отучиваем Google Chrome убивать ресурс SSD винчестера](https://habrahabr.ru/sandbox/59573/)
Следующий вариант по-моему скромному мнению, решил все мои проблемы. Я решил использовать RAM Drive — т.е. держать все в оперативной памяти, и только лишь при выключении писать на винчестер. Учитывая что ноутбук у меня либо включен, либо в ждущем режиме, то писаться при выключении будет очень редко. Из понравившихся программ остановил выбор на Qsoft RAMDisk. Ставится как драйвер. В свойствах выбрал размер диска, файловую систему, куда писать при выключении. Под диск выделил 512 МБ (думаю разумный минимум 128 МБ).
Можно было перенести просто папку кеша, можно было и добавить к ней папку Media Cache, но я решил полностью избавиться от всяческих записей, и перенести полносью всю папку User Data. 
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

## Проблемы с реестром
- [Event ID 10016 - The application-specific permission settings do not grant Local Activation permission for the COM Server application with CLSID](http://answers.microsoft.com/en-us/windows/forum/windows_8-performance/event-id-10016-the-application-specific-permission/9ff8796f-c352-4da2-9322-5fdf8a11c81e?auth=1) и [здесь](http://blog.ronnypot.nl/?p=843)
- [Параметры разрешений для конкретного приложения не дают разрешения Локально Активация для приложения COM-сервера с CLSID {D63B10C5-BB46-4990-A94F-E40B9D520160} и APPID {9CA88EE3-ACB7-47C8-AFC4-AB702511C276}](http://admsoft.ru/parametry-razreshenij-dlya-konkretnogo-prilozheniya-ne-dayut-razresheniya-lokalno-aktivaciya-dlya-prilozheniya-com-servera-s-clsid-d63b10c5-bb46-4990-a94f-e40b9d520160-i-appid-9ca88ee3-acb7-47c8)

В инете есть решение, точно сейчас не напишу, у себя поправил, суть в том что рантаймброкер не может нормально запуститься. В реестре надо на пару веток дать разрешения для Администраторы, далее через *dcomcnfg* - службы и компоненты - компьютеры - мой компьютер - настройка DCOM - для runtimebroker в разрешениях на запуск и активацию добавить network service и local service и system.
конкретнее тут:
Скрытый текст
http://answers.microsoft.com/en-us/windows/forum/windows_10-security/event-id-10016-runtime-broker/18c291c6-f2a1-4f3c-b4ad-2b7ff59fd9f9?auth=1
Закрыть

## Проблемы с Wi-Fi
- [Пропадает интернет (Wi-Fi) в Windows 10 после выхода из спящего режима](https://help-wifi.com/reshenie-problem-i-oshibok/propadaet-internet-wi-fi-v-windows-10-posle-vyxoda-iz-spyashhego-rezhima/).
Это происходит потому, что для экономии, система отключает Wi-Fi адаптер. А после включения, он уже не может нормально работать, поэтому и пропадает интернет. Эта проблема очень часто возникает только при работе от батареи.Все что нужно сделать, это запретить "десятке" отключать беспроводной сетевой адаптер.

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

## Tips
- [Бесплатно продлеваем Kiwi for Gmail](https://dailysoftwaredeal.com/seller/giveaway-kiwi-for-gmail-windows-mac-1-year-license/). Тут идет покупка, если из приложения не доступно пока. https://www.kiwiforgmail.com/. Code: KiwiForFree
- [Как создать локальную учетную запись в Windows 10](http://windowstips.ru/notes/18570)
- [4 Ways To Boot Into Safe Mode In Windows 10](http://www.digitalcitizen.life/4-ways-boot-safe-mode-windows-10)

- [ms-setting:display and ms-personalization-background problem](http://www.windows10forums.com/threads/ms-setting-display-and-ms-personalization-background-problem.1247/)
Hey Guyz. I found a solution for settings and updates. Download this update [3081424](https://support.microsoft.com/kb/3081424). And download the utility Microsoft Troubleshooter and fix it. Download it from here http://aka.ms/diag_settings
- [Settings doesn’t launch, or launches the Store instead](http://answers.microsoft.com/en-us/windows/forum/windows_10-other_settings/settings-doesnt-launch-or-launches-the-store/ec439819-7ee4-4b4d-abdd-35d82e04c55f)

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
Пример использования `icacls` и `takeown` для получения доступа ко всем файлам несистемного диска..
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


## Настройка VPN и браузеров
- [How to disable images in firefox](https://support.mozilla.org/en-US/questions/981640)
- [How to turn off images in Firefox](https://www.ghacks.net/2015/03/24/how-to-turn-off-images-in-firefox/)
- [Image Block add-on](https://addons.mozilla.org/en-US/firefox/addon/image-block/)

## Проблемы с сетевым подключением
- [Неопознанная сеть без доступа к Интернету - причины и решение](https://ocomp.info/neopoznannaya-set-bez-interneta.html)

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

## Photoshop
- COOL! [20 Free Spray Paint Photoshop Brushes with Splatters & Drips](https://blog.spoongraphics.co.uk/freebies/20-free-spray-paint-photoshop-brushes-with-splatters-drips)

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

## Руководство по установке подсистемы Windows для Linux в Windows 10
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

# Настройка рабочего Windows10 с нуля
- Отключаем в ярлыках Рабочего стола тени шрифта (описано выше).
- Ставим английский язык по умолчанию и при входе в систему (описано выше).
- Устанавливаем Ubuntu под Windows [WSL 1](https://docs.microsoft.com/ru-ru/windows/wsl/install-win10)
- Ставим Package Manager [Chocolatey](https://chocolatey.org/)
- Устанавливаем FiraCode для RStudio.
- Ставим [OpenVPN Community edition](https://openvpn.net/community-downloads/)
- Ставим SSH клиент [Bitvise SSH Client/xShell]
- Ставим SnagIt, блокируем его в файерволе (wf.msc) или касперском. [Best practices for configuring Защитник Windows firewall](https://docs.microsoft.com/ru-ru/windows/security/threat-protection/windows-firewall/best-practices-configuring).
Переносим базы SangIt
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
- Ставим EmEditor, отключаем в Касперском доступ в инет. 
	- Ставим проверку русского языка [Spellcheck](https://www.emeditor.com/text-editor-features/more-features/spellcheck/). На момент установки словари жили [здесь](https://extensions.openoffice.org/en/project/slovari-dlya-russkogo-yazyka-dictionaries-russian). After download a dictionary, change the file extension from .oxt to .zip, extract the Zip file, and then copy *.dic and *.aff files into the Dictionaries sub folder of the EmEditor install folder (usually C:\Program Files\EmEditor\Dictionaries).
	- Ставим для *.R подсветку синтаксиса [EmEditor Syntax ](https://www.emeditor.com/wpfb_file_category/syntax-files/), а именно, [R syntax file](https://www.emeditor.com/files/r-esy/). Инструкция по установке [How can I install an EmEditor syntax file?](http://www.emeditor.org/en/faq_setup_setup_syntax.html).
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
- Ставим SmartGit, переносим настройки из `%appdata%\syntevo\SmartGit\<version>\`. Читаем [How to import old settings/repositories](https://stackoverflow.com/questions/45837545/how-to-import-old-settings-repositories)
- Настраиваем Касперского для разрешения доступа Edge в инет. [Cannot open websites in Google Chrome and Edge Chromium when working with Kaspersky Security 10 for Windows Server](https://support.kaspersky.com/15392)
- После установки Касперского в режиме администратора отключаем штатный брандмауэр Windows `netsh advfirewall set allprofiles state off`
- В Google Chrome включаем режим чтения. Делается это через экспериментальные настройки. `chrome://flags/#enable-reader-mode`
- Отключаем встроенный Windows Defender. Связано это с подобными фокусами: [Штатный антивирус в Windows 10 стал помечать клиент uTorrent как вредоносное ПО, автоматически удалять его и препятствовать его повторной установке.](https://www.cnews.ru/news/top/2021-06-16_microsoft_voznenavidela_samyj) 

