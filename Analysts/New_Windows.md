1. Удалить Nvidia Update & UpdatusUser (через netplwiz)
2. Удалить Norton и прочую фигню
3. Office 365 со скидкой 50%. [Хак](http://news.microsoft.com/ru-ru/office-2016-for-windows-10/)


# Полезные твики по настройке Windows

- Win+R - вызов окна "выполнить"
	- control - вызов панели управления
	- netplwiz - управление учетными записями пользователей
	- control userpasswords2

- Запуск центра обновления Windows:
   Пуск -> Параметры -> Обновления и безопасность

Win 10 ставится на Win 8.1
SP1 можно получить через web: [Service Pack and Update Center](http://windows.microsoft.com/en-us/windows/service-packs-download)

- [Как получить Windows 10 без очереди](http://lifehacker.ru/2015/07/30/kak-poluchit-windows-10/)
	- Task Manager + запустить новый процесс как администратор Powershell -> wuauclt.exe/updatenow
- [Обновление KB 3081436 для Windows 10 приводит к бесконечной перезагрузке, как и KB 3081424, выпущенное ранее](http://gamesqa.ru/news/obnovlenie-kb-3081436-dlya-windows-10-privodit-k-beskonechnoj-perezagruzke-kak-i-kb-3081424-vypushhennoe-ranee-1538/)

Как показывает практика, проблема с установкой заключается в наличии некорректного профиля Nvidia под названием UpdatusUser.
- [What is “UpdatusUser” Folder and How to Remove it from Windows Explorer?](http://www.askvg.com/tip-what-is-updatususer-folder-and-how-to-remove-it-from-windows-explorer/)


- [Microsoft тайком загружает файлы Windows 10 пользователям Windows 7 и 8. Как с этим бороться](http://lifehacker.ru/2015/09/11/how-to-block-windows-10-upgrade-downloads/)

## Tips
- [Как создать локальную учетную запись в Windows 10](http://windowstips.ru/notes/18570)
- [4 Ways To Boot Into Safe Mode In Windows 10](http://www.digitalcitizen.life/4-ways-boot-safe-mode-windows-10)

- [ms-setting:display and ms-personalization-background problem](http://www.windows10forums.com/threads/ms-setting-display-and-ms-personalization-background-problem.1247/)
Hey Guyz. I found a solution for settings and updates. Download this update [3081424](https://support.microsoft.com/kb/3081424). And download the utility Microsoft Troubleshooter and fix it. Download it from here http://aka.ms/diag_settings
- [Settings doesn’t launch, or launches the Store instead](http://answers.microsoft.com/en-us/windows/forum/windows_10-other_settings/settings-doesnt-launch-or-launches-the-store/ec439819-7ee4-4b4d-abdd-35d82e04c55f)