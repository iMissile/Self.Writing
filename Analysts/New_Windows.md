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

# Настройка приложений Windows 10
- [Как включить всем привычный Просмотр Фотографий в Windows 10](http://g-ek.com/prosmotr-fotografij-v-windows-10)
- [iPhone или iPad не синхронизируется с компьютером?](http://appleinsider.ru/iphone/iphone-ili-ipad-ne-sinxroniziruetsya-s-kompyuterom-est-reshenie.html) Есть решение. Если вы столкнулись с подобной проблемой, может помочь сброс папки Lockdown на Mac или Windows
- [Невозможность создания резервной копии данных iPhone, iPad или восстановления из резервной копии в iTunes](http://app-s.ru/publ/rezervnaja_kopija_v_itunes_ne_udaetsja_vypolnit_rezervnoe_kopirovanie_ili_vosstanovlenie_iz_rezervnoj_kopii_v_itunes/1-1-0-215)
- Решение найдено в YouTube:
Диспетчер устройств -> Переносные устройства -> Apple iPad -> Обновить драйверы -> Manual -> "C:\Program Files\Common Files\Apple\Mobile Device Support\Drivers"


# Как определить ключ установки Windows
- [Почему нельзя выполнять чистую установку Windows 10 обладателям Windows 7 и 8](https://lifehacker.ru/2015/08/04/tonkosti-ustanovki-windows-10/)
- [5 простых способов как узнать ключ продукта ОС Windows 10](http://geek-nose.com/5-prostyx-sposobov-kak-uznat-klyuch-produkta-os-windows-10/)
- [Как узнать ключ продукта Windows 10](http://remontka.pro/windows-10-key/)
- Выбираем средства с GUI:
	- [Как узнать OEM ключ из UEFI](http://remontka.pro/windows-10-key/)
	- [ProduKey от NirSoft](http://www.nirsoft.net/utils/product_cd_key_viewer.html) для определения ключа Windows 10 и не только. “ProduKey” от NirSoft умеет определять ключи других копий Windows, установленных на локальном и удаленных компьютерах, в том числе на всех машинах в домене. Также он может вытащить ключ из реестра незагруженной системы. Последнее бывает необходимо при переустановке ОС, чтобы повторно активировать Windows 10, когда она потребует ключ продукта.
	- [ShowKeyPlus](https://github.com/Superfly-Inc/ShowKeyPlus/releases/). “ShowKeyPlus” – единственный продукт, который смог определить ключ установленной ОС Windows 10 и ее предшественницы Windows 7 (“семерка” в нашем примере была обновлена до “десятки”). Как и “ProduKey” от NirSoft, она не требует инсталляции и не распространяет рекламу, ее достаточно скачать и запустить. Ключи продуктов отображаются в основном окне. Нажатием “Save” их можно скопировать и сохранить в текстовом файле.
Кроме того, “ShowKeyPlus” умеет извлекать product key из реестра незагруженной ОС. Кликните для этого “Retrieve key from backup” и укажите путь к источнику – файлу Software, который находится в каталоге Буква_раздела\Windows\system32\config.
- [How To Get Windows 10 For Free If You’re Running Windows Vista or XP](http://bgr.com/2015/06/20/windows-10-free-upgrade-xp-vista/)

# Переход на SSD
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



# Проблемы Lenovo с видеодрайвером
1. Удалить Nvidia Update & UpdatusUser (через netplwiz)
2. Удалить Norton и прочую фигню
3. Office 365 со скидкой 50%. [Хак](http://news.microsoft.com/ru-ru/office-2016-for-windows-10/)

# Windows 7 и выше. Проблемы с принтером HP Laserjet 1300
- Начал решение отсюда: [Помогите найти драйвер способный печатать на HP Lasejet 1300 в Windows 7/Vista в родном для принтера разрешении 1200 dpi](http://forum.ixbt.com/topic.cgi?id=58:14)
- Нашел решение здесь: [Установка драйвера HP LaserJet 1320 в Windows 10. Решено!!!](https://dyrik.ru/windows/ustanovka-drajvera-hp-laserjet-1320-v-windows-7-windows-8-i-windows-10-resheno.html)

# Полезные твики по настройке Windows

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

## Проблемы с реестром
- [Event ID 10016 - The application-specific permission settings do not grant Local Activation permission for the COM Server application with CLSID](http://answers.microsoft.com/en-us/windows/forum/windows_8-performance/event-id-10016-the-application-specific-permission/9ff8796f-c352-4da2-9322-5fdf8a11c81e?auth=1) и [здесь](http://blog.ronnypot.nl/?p=843)
- [Параметры разрешений для конкретного приложения не дают разрешения Локально Активация для приложения COM-сервера с CLSID {D63B10C5-BB46-4990-A94F-E40B9D520160} и APPID {9CA88EE3-ACB7-47C8-AFC4-AB702511C276}](http://admsoft.ru/parametry-razreshenij-dlya-konkretnogo-prilozheniya-ne-dayut-razresheniya-lokalno-aktivaciya-dlya-prilozheniya-com-servera-s-clsid-d63b10c5-bb46-4990-a94f-e40b9d520160-i-appid-9ca88ee3-acb7-47c8)

В инете есть решение, точно сейчас не напишу, у себя поправил, суть в том что рантаймброкер не может нормально запуститься. В реестре надо на пару веток дать разрешения для Администраторы, далее через *dcomcnfg* - службы и компоненты - компьютеры - мой компьютер - настройка DCOM - для runtimebroker в разрешениях на запуск и активацию добавить network service и local service и system.
конкретнее тут:
Скрытый текст
http://answers.microsoft.com/en-us/windows/forum/windows_10-security/event-id-10016-runtime-broker/18c291c6-f2a1-4f3c-b4ad-2b7ff59fd9f9?auth=1
Закрыть


## Tips
- [Как создать локальную учетную запись в Windows 10](http://windowstips.ru/notes/18570)
- [4 Ways To Boot Into Safe Mode In Windows 10](http://www.digitalcitizen.life/4-ways-boot-safe-mode-windows-10)

- [ms-setting:display and ms-personalization-background problem](http://www.windows10forums.com/threads/ms-setting-display-and-ms-personalization-background-problem.1247/)
Hey Guyz. I found a solution for settings and updates. Download this update [3081424](https://support.microsoft.com/kb/3081424). And download the utility Microsoft Troubleshooter and fix it. Download it from here http://aka.ms/diag_settings
- [Settings doesn’t launch, or launches the Store instead](http://answers.microsoft.com/en-us/windows/forum/windows_10-other_settings/settings-doesnt-launch-or-launches-the-store/ec439819-7ee4-4b4d-abdd-35d82e04c55f)