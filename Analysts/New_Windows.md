1. Удалить Nvidia Update & UpdatusUser (через netplwiz)
2. Удалить Norton и прочую фигню
3. Office 365 со скидкой 50%. [Хак](http://news.microsoft.com/ru-ru/office-2016-for-windows-10/)


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