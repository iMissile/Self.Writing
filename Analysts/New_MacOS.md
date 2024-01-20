# апгрейд Macbook Pro
- [Своими силами: как заменить/проапгрейдить HDD/SSD и RAM в MacBook Pro](http://lifehacker.ru/2011/08/18/how-to-upgrade-hddssdram/)
- [Как выбрать тип оперативной памяти для вашего Mac](http://macilove.com/news/how-to-choose-the-type-of-ram-for-your-mac/). Инструкция по замене оперативной памяти для iMac, MacBook, Mac Pro, Mac mini
 	– формат SO-DIMM DDR3
	– 67,6 x 30 мм
	– 2 или 4 ГБ
	– 204 контакта
	– ОЗУ PC3-12800 DDR3, 1600 МГц
- [MacBook Pro: извлечение или установка модулей памяти](https://support.apple.com/ru-ru/HT201165). В этой статье описан процесс извлечения и установки модулей памяти в ноутбуках MacBook Pro.
- [Клонирование жесткого диска через установщик MacOS](http://applemix.ru/2012/03/22/klonirovanie-zhestkogo-diska-cherez-ustanovshhik-macos.html)
- [Как самостоятельно настроить новый SSD-диск в OS X Yosemite](http://lifehacker.ru/2014/11/05/ssd-os-x/)
- [Оптимизация OS X для продления жизни SSD](https://geektimes.ru/company/ocz/blog/265746/)
- [Disk Utility: How to Resize a Mac Volume (OS X El Capitan or Later)](http://macs.about.com/od/systemutilities/fl/Disk-Utility-How-to-Resize-a-Mac-Volume-OS-X-El-Capitan-or-Later.htm)
- [Мнение экспертов. MacBook Pro и 16 гигабайт оперативной памяти](http://appleinsider.ru/macbook-pro/mnenie-ekspertov-macbook-pro-i-16-gigabajt-operativnoj-pamyati.html)
- Апгрейд памяти
	- [Crucial: Apple MacBook Pro (13-inch and 15-inch, Mid 2012) compatible upgrades](http://www.crucial.com/usa/en/compatible-upgrade-for/Apple/macbook-pro-%2813-inch-and-15-inch%2C-mid-2012%29)
	- [Kingston: Модули памяти конкретных систем для Apple MacBook Pro 13-inch and 15-inch (Mid 2012)]http://www.kingston.com/ru/memory/search?DeviceType=&Mfr=APP&Line=MacBook%20Pro&Model=78047)
	- [Kingston 4GB 1600MHz DDR3L (PC3-12800) SO-DIMM for Mac](http://maccentre.ru/shop/memory/ram-memory/?filter_params=87:621;91:642;86:612)
	- [Какой тип памяти (1.35 или 1.5В) у Macbook pro mid 2012?](https://toster.ru/q/83200). Планирую увеличить оперативную память macbook pro md102 (i7/8Gb 1600MHz) id2012 до 16Gb, стал выбирать и столкнулся с тем, что есть два типа памяти DDR3 (1.5В) и DDR3L (1.35В).

апгрейд памяти:
- [Оперативная память 8GB DDR3 PC12800 (1600MHz) SO-DIMM CL11, Transcend для Mac (Apple)](http://www.maxmemory.ru/product_123392.html)
- [DDR II Hynix (3rd) 2Gb 800Mhz PC6400](http://maxmemory.ru/product_121293.html)
(3020+1370)*2 + 250 (курьеры - отдельные персонажи )
9000 будет

- [Foxconn G41MX-F 2.0](http://www.foxconnchannel.com/ProductDetail.aspx?T=motherboard&U=en-us0000463)

# SSD
- [Что такое TRIM и зачем его включать](http://macosworld.ru/kingston-hyperx-fury-ssd-v-macbook/)
Особенность SSD такова, что перед записью какой либо информации всегда нужно очистить блок памяти, в который она будет записана. Чтобы не тратить на это время непосредственно перед записью и существует команда TRIM. Она позволяет очищать «грязные» блоки в свободное время.Увы, но в OS X команда TRIM отключена для сторонних SSD, поэтому со временем их производительность падает.
То есть, TRIM не добавит вам скорости, но будет поддерживать её на максимально возможном уровне за счёт предварительно очистки «грязных» блоков.
Включить TRIM можно специальными утилитами вроде [Trim Enabler](https://www.cindori.org/trim-enabler-and-yosemite/) и [Chameleon SSD Optimizer](http://chameleon.alessandroboschini.com/). Лично я воспользовался последним.
- [MacBook Pro 13" Unibody Early 2011 Hard Drive Replacement](https://ru.ifixit.com/Guide/MacBook+Pro+13-Inch+Unibody+Early+2011+Hard+Drive+Replacement/5119)
- [The EVO speed issues may be related to the 840 EVO's issues with the nand voltage degradation.](https://www.gearslutz.com/board/music-computers/1012589-enable-trim-3rd-party-ssd-yosemite-tried-disk-sensei.html)
- [Chameleon SSD Optimizer: enanche your ssd performance](http://chameleon.alessandroboschini.com/). Apple added a new command named “trimforce” from OS X 10.10.4 and OS X 10.11 (El Capitan). 
To run trimforce type the following command into the terminal window : `sudo trimforce enable`
- [Disk Sensei](https://www.cindori.org/software/disksensei/). [Safely enable Trim on Yosemite and El Capitan!](https://www.cindori.org/safely-enable-trim-on-yosemite-and-el-capitan/)
- [Can Alfred work without Spotlight enabled?](https://www.alfredapp.com/help/troubleshooting/indexing/spotlight/) Alfred relies on the same OS X metadata index as Spotlight. As such, it's important for you to let Spotlight run on your Mac to maintain an index of the files on it. Turning off Spotlight indexing will still allow you to use Alfred as a web launcher but you'll no longer be able to find files on your Mac. Take a look at the [Indexing Troubleshooting page](https://www.alfredapp.com/help/troubleshooting/indexing/) for help with indexing issues.

# Статейки про всякие фичи
- [10 tiny features I love about OS X El Capitan](http://www.imore.com/10-tiny-features-i-love-os-x-el-capitan).
- [27 secret features in Mac OS X El Capitan](http://www.macworld.co.uk/feature/mac-software/27-secret-features-in-mac-os-x-el-capitan-3626097/)
- [6 Great Apps To Measure You Mac’s Performance](http://www.chriswrites.com/6-great-apps-to-measure-you-macs-performance/)
- [60 горячих клавиш для продуктивной работы в Safari](https://lifehacker.ru/50-poleznyx-goryachix-klavish-dlya-produktivnoj-raboty-v-safari/)
- [Open a Mac app from an unidentified developer](https://support.apple.com/guide/mac-help/open-a-mac-app-from-an-unidentified-developer-mh40616/mac)


# Backups
- [Arq](https://www.arqbackup.com/) Backs up all your computers. Simple. Awesome. 
Arq automatically backs up all your Macs and PCs. Your files are stored securely, readable only by you.
- [Amazon Cloud Drive](https://www.amazon.com/clouddrive/home). Unlimited Cloud Storage from Amazon
- [TimeMachineEditor](http://tclementdev.com/timemachineeditor/)
TimeMachineEditor is a software for OS X that lets you change the default one-hour backup interval of Time Machine. You can change the interval or create a more sophisticated scheduling (see screenshots below)

## OpenVPN
- [Tunnelblick	free software for OpenVPN on OS X and macOS](https://tunnelblick.net/)
	- [Настройка OpenVPN на Mac OS X](http://www.freeproxy.ru/ru/vpn/mac-os-x/openvpn.htm)
	- [Строим OpenVPN мост под Mac OSX](https://geektimes.ru/post/206322/)

## OpenConnect
Замена CiscoAnyConnect
http://macappstore.org/openconnect/
http://www.infradead.org/openconnect/download.html
https://openconnect.github.io/openconnect-gui/ (edited) 

## Интересные утилиты
- [iTerm2](https://www.iterm2.com/downloads.html) -- удобная бесплатная замена для штатного терминала.
- [Cyberduck](https://cyberduck.io) is a libre server and cloud storage browser for Mac and Windows with support for FTP, SFTP, WebDAV, Amazon S3, OpenStack Swift, Backblaze B2, Microsoft Azure & OneDrive, Google Drive and Dropbox.
- [MacPass](https://macpassapp.org/). A free, open-source, KeePass-compatible password manager for macOS.
- [Strongbox](https://strongboxsafe.com/). A Password Manager for Apple devices. Password Safe & KeePass compatible
- [SyncPass](https://itunes.apple.com/app/id533858341)
- 1password
	- [download 1password6](https://discussions.agilebits.com/discussion/91012/download-1password6)
- [Полезные сочетания клавиш macOS, о которых я не знал](https://appleinsider.ru/mac-os-x/poleznye-sochetaniya-klavish-macos-o-kotoryx-ya-ne-znal.html)


## Как сделать ресет для OneDrive
- COOL! [ONEDRIVE SYNC ISSUES? HOW TO RESET ONEDRIVE FOR MAC THE EASY WAY!](
https://www.hightechdad.com/2017/02/06/onedrive-sync-issues-how-to-reset-onedrive-for-mac-the-easy-way/). Сохранил в Evernote
- [Onedrive restrictions and limitations when you sync files and folders](https://support.microsoft.com/en-us/help/3125202/restrictions-and-limitations-when-you-sync-files-and-folders)
- [OneDrive sync issues: MAC OS X](https://answers.microsoft.com/en-us/onedrive/wiki/odwork-odfiles/onedrive-sync-issues-mac-os-x/28942f7f-2ce6-47a5-8d56-f47fc2bffbab?auth=1)
- OneDrive не работает с файлами с общей длиной имени >255 и содержащими символы [|"?:] или ведущий пробел.
   сбой в файле `matrix_elem.nb`: `Export[".\\output\\vv_index.mjson", vvtable, "ExpressionJSON"]`

## iCloud
- [Ошибка подключения Mac к ICloud. Как я решил проблему](https://ddr5.ru/oshibka-podklyucheniya-mac-k-icloud/)

# Распродажа софта
- [$2 tuesday](http://twodollartues.com/)
- [MacAppDeals](http://www.macappdeals.com/). Your Source To Finding Discounts On Great Mac Software
- [MacUpdate](http://www.macupdate.com/) simplifies finding, buying and installing apps for your Mac
- [BundleHunt](http://bundlehunt.com/). A one-stop daily deals site
- [Stack Social](https://stacksocial.com/)
- [AppShopper](http://appshopper.com/mac/)
- [AppGratis](http://appgratis.com/). Перестаньте платить! Ежедневные бесплатные приложения и скидки!

# Софт под Мак
## Tools
- [AppZapper](http://www.appzapper.com/). The Unistaller Apple forgot
- [A look back at 2015: My Top Mac Apps](http://brettterpstra.com/2016/02/17/a-look-back-at-2015-my-top-mac-apps/)
- [Homebrew. The missing package manager for OS X](http://brew.sh/)
- [Default Folder X](http://www.stclairsoft.com/DefaultFolderX/index.html)
- [Alfred](https://www.alfredapp.com/). Spotlight replacement & extension

## Текстовые редакторы
- [Выбор текстового редактора или «хочу все в одном»](http://habrahabr.ru/post/260865/). Победил Brackets


# Запуск Windows программ под Mac
- [Как легко запускать Windows-приложения на Mac? Приложение Wineskin](http://lifehacker.ru/2014/03/03/kak-legko-zapuskat-windows-prilozhenie-na-mac-prilozhenie-wineskin/)
- [Три способа запустить Windows программу на Mac OS](http://geekpro.ru/tri-sposoba-zapustit-windows-programmu-na-mac-os)

# Hack
- [MacX.ws](https://macx.ws)
- [Mac Torrent Download](http://www.mac-torrent-download.net/application/utility/arq-4-15-1/)
- [CrossOver](https://www.codeweavers.com/)
	- [CrossOver - запуск любых Windows программ под Mac OS](http://macintoshim.ru/emulators/crossover---zapusk-lyubyh-windows-programm-pod-mac-os.html)
	- [CrossOver 15](https://macx.ws/mac-os-unix/3200-crossover-15.html)

# Полезные сайты про macos
- [ixrevo](http://ixrevo.me/blog/). Привет! Меня зовут Александр Сокол. Я интересуюсь музыкой, наукой, компьютерами Mac, веб-дизайном, WordPress разработкой и веду этот блог.
- [MacOS World](http://macosworld.ru/). Про программы.
- [Set up Git and Mercurial (Mac OSX)](https://confluence.atlassian.com/bitbucket/set-up-git-and-mercurial-mac-osx-269981802.html)


# Как полностью удалить Office для Mac 2011
- [How to Completely Uninstall Office 2011 for Mac OS X](http://www.howtogeek.com/212650/how-to-completely-uninstall-office-2011-for-mac/). Очень хорошая подробная статья про удаление в картинках.
- [Как полностью удалить Microsoft Office 2011 из OS X](http://macilove.com/news/how-to-completely-remove-microsoft-office-2011-from-os-x/). Пошаговая инструкция по удалению пакета Office 2011 и всех его сопутствующих файлов из Mac OS X
- [База знаний Microsoft](https://support.microsoft.com/ru-ru/kb/2398768)
- [Mathtype & Office 365](http://www.dessci.com/en/products/mathtype_mac/faqs.htm#office_versions)
	Mac Office 2016: MathType is not yet compatible with this version of Office. Microsoft decided to sandbox Office. Sandboxing is an Apple security technology that, as its name implies, isolates each application from others running on the same computer in order to protect them against malware. Unfortunately, this also prevents MathType from interacting with them. We are working with Microsoft engineers on a solution but it will require significant work to implement. We wish we could give you a more definite answer. In the meantime, MathType 6.7 for Mac still works great with Office 2011 for Mac. Thank you for your patience.


# Перенос базы Evernote на другой диск
1. Вообще, зачем это надо: [Slim down your SSD with symbolic link](http://www.macworld.com/article/2148490/slim-down-your-ssd-with-symbolic-links.html#tk.nl_mwdaily)
2. [How to Change from the Appstore to the Direct Download Version of Evernote](http://www.christopher-mayo.com/?p=135)
2. Как изменить расположение баз: [This is how I changed the Evernote Data folder to another Hard Drive](https://discussion.evernote.com/topic/37689-this-is-how-i-changed-the-evernote-data-folder-to-another-hard-drive/).
3. Как найти расположение баз Evernote: [Where in the World is Evernote?](https://www.evernote.com/shard/s74/sh/9fad0837-0cb4-4cd4-bfe4-5409dd632127/f5a70bbcd598bd2810ac4b388944f660)


Итого, 
1. Сносим Evernote с помощью CleanMyMac, если стояла инсталляция с AppStore. Загружаем с сайта www.evernote.com
2. В пользовательской директории делаем видимой папку Библиотеки. Вбиваем в Терминале **chflags nohidden ~/Library**
3. Ищем базу данных. [5.6 Version of the Direct Download](http://www.christopher-mayo.com/?p=135)
/Users/Your Username Here/Library/Application Support/com.evernote.Evernote/accounts/
Переносим ее на внешний диск.
4. Переходим в терминале в директорию где надо сделать ссылку с данными. Делаем Symbolic Link с помощью команды ln -s "перетаскиваем в терминал директорию, ссылку на которую надо сделать"
5. Обратно скрываем папку Библиотеки. Вбиваем в Терминале **chflags hidden ~/Library**

# iOS
- [Как продлить время автономной работы iPhone с iOS 9](https://www.iphones.ru/iNotes/481843)
- ["Null" app can't be deleted](https://discussions.apple.com/thread/6861025?start=0&tstart=0)
- [Erasing All iPhone Skype Data and Chats Permanently](https://www.imyfone.com/ios-data-erase/permanently-erase-all-skype-tracks-on-iphone/)
- [iPhone Backup Extractor](https://reincubate.com/ru/iphone-backup-extractor/)
Восстановление и передача потерянных сообщений iPhone, фотографий, календарей, контактов, заметок, местоположений и данных из резервных копий iPhone и iCloud.

## iPhone backup & restore
- [Зашифрованные резервные копии на iPhone, iPad или iPod touch](https://support.apple.com/ru-ru/HT205220)
- [Как восстановить потерянный резервный пароль iPhone - 5 способов](https://reincubate.com/ru/support/how-to/iphone-backup-password-encrypted/)
- [Ты забыл пароль резервной копии iPhone. Как отключить](https://www.iphones.ru/iNotes/694246)

# Разное
- [Top 10 Best VPN](http://www.top10bestvpn.com/). Find the Best VPN Service for You. Check out our top VPN services for total privacy, protection and super-fast connections.
- Открытие и переименование файлов
	- [[Mac для чайников] №29 Переименование](http://i-ekb.ru/2010/11/mak-dlya-chajnikov-29-pereimenovanie/). Если вы хотите, открыть файл, вы можете либо дважды щелкнуть по нему, либо выбрать его и нажать Command + O или Command + Стрелка Вниз на клавиатуре. А, отнюдь, не Enter, как в Windows.
	- [Как открыть программу на Mac](http://appleprofi.ru/kak-otkryt-programmu-na-mac/)
- [Запятая и точка на русской клавиатуре Mac. Удобное сочетание клавиш](http://yablyk.com/037778-lajfxak-udobnyj-sposob-nabora-zapyatoj-i-tochki-na-os-x/)
- [Finder минималиста](http://macosworld.ru/finder-minimalista/)
- [OS X Mavericks: Как открыть программу от неустановленного разработчика](https://support.apple.com/kb/PH14369?locale=ru_RU&viewlocale=ru_RU). 1) В Finder найдите программу, которую нужно открыть. Не используйте для этого Launchpad. В Launchpad нельзя использовать контекстное меню.
2) Нажмите клавишу Control, затем нажмите значок программы. 3) В контекстном меню выберите «Открыть». 4) Нажмите «Открыть».
Дополнительный вариант настроек через меню безопасности можно найти здесь: [Вариант 2 - Запуск Firefox через Системные настройки](https://support.mozilla.org/ru/kb/firefox-ne-zapuskaetsya-posle-ustanovki-ego-na-mac)
- [Как правильно смотреть любое видео на Mac](http://kakpravilno.info/kak-pravilno-smotret-ljuboe-video-na-mac-46.html)
- [Bluetooth]
	- [How To Fix ‘Bluetooth Not Available’ Mac OS X Problem](http://www.howtoturnitoffandonagain.com/2016/03/01/how-to-fix-bluetooth-not-available-mac-os-x-problem/)
	- [Fixing a “Bluetooth Not Available” Error on a Mac](http://osxdaily.com/2014/02/17/fix-bluetooth-not-available-error-mac/)
- [How to Check Package File for Malware Before You Install It in Mac](https://www.maketecheasier.com/check-dmg-malware-mac/)
	
	
# Настройка клавиатуры и шрифтов
## Церковнославянские шрифты
- [Как ввести символ unicode на mac без цифровой клавиатуры?](https://coderoad.ru/48312049/%D0%9A%D0%B0%D0%BA-%D0%B2%D0%B2%D0%B5%D1%81%D1%82%D0%B8-%D1%81%D0%B8%D0%BC%D0%B2%D0%BE%D0%BB-unicode-%D0%BD%D0%B0-mac-%D0%B1%D0%B5%D0%B7-%D1%86%D0%B8%D1%84%D1%80%D0%BE%D0%B2%D0%BE%D0%B9-%D0%BA%D0%BB%D0%B0%D0%B2%D0%B8%D0%B0%D1%82%D1%83%D1%80%D1%8B).
Сначала убедитесь , что вход Unicode Hex включен в System Preferences > Keyboard > Input Sources
Он должен появиться в левом поле с другими языковыми клавиатурами. Если ввод Unicode Hex там недоступен, нажмите кнопку + ниже, прокрутите список языков до самого низа и выберите другие, выберите ввод Unicode Hex в поле сведений справа и нажмите кнопку Добавить.
Теперь ввод Unicode Hex должен быть доступен в строке меню среди других языков, выберите его, и вы сможете ввести unicode символа, удерживая Option во время ввода цифр.
- [Ирмологион](http://irmologion.ru/)
	- [Шрифты в кодировке UCS8](http://irmologion.ru/fonts.html#atop)
	
## Установка для работы Лиды
1. Смотрим содержимое шрифта и юникод символы
- [FontDrop!](https://fontdrop.info/)
Simple and easy way to view the content of font files.
- [Fun With Fonts With FontDrop!](https://viktornuebel.medium.com/fun-with-fonts-bdc1b5e5d4b9)

2. 

3. Доп ссылки
- [Старославянские кириллические шрифты.. Обсуждение на LiveInternet](https://www.liveinternet.ru/users/5406319/post430118925/)
- [Ссылка от Ольги](http://tapenik.ru/shrifti/Flavius.ttf). [Страничка со шрифтами](https://tapenik.ru/shrifti.html)

- [Как ввести символ unicode на mac без цифровой клавиатуры?](https://coderoad.ru/48312049/%D0%9A%D0%B0%D0%BA-%D0%B2%D0%B2%D0%B5%D1%81%D1%82%D0%B8-%D1%81%D0%B8%D0%BC%D0%B2%D0%BE%D0%BB-unicode-%D0%BD%D0%B0-mac-%D0%B1%D0%B5%D0%B7-%D1%86%D0%B8%D1%84%D1%80%D0%BE%D0%B2%D0%BE%D0%B9-%D0%BA%D0%BB%D0%B0%D0%B2%D0%B8%D0%B0%D1%82%D1%83%D1%80%D1%8B).
Сначала убедитесь , что вход Unicode Hex включен в System Preferences > Keyboard > Input Sources
Он должен появиться в левом поле с другими языковыми клавиатурами. Если ввод Unicode Hex там недоступен, нажмите кнопку + ниже, прокрутите список языков до самого низа и выберите другие, выберите ввод Unicode Hex в поле сведений справа и нажмите кнопку Добавить.
Теперь ввод Unicode Hex должен быть доступен в строке меню среди других языков, выберите его, и вы сможете ввести unicode символа, удерживая Option во время ввода цифр.


## Трюки
- [Как изменить расположение точки и запятой на клавиатуре Mac (macOS)?](https://dzen.ru/a/XwRE3IpexVf_swv3)
Все просто: в настройках клавиатуры язык "Русский" поменять на "Русский ПК"

# Менеджер пакетов
- [Git is not working after macOS Update (xcrun: error: invalid active developer path (/Library/Developer/CommandLineTools)]().
The problem is that Xcode Command-line Tools needs to be updated.
Solution #1
Go back to your terminal and enter:
`xcode-select --install`

# Работа с фотографиями в Mac
- [Как слить фото с камеры на Mac OS X без iPhoto?](https://www.stableit.ru/2012/03/mac-os-x-iphoto.html) Используем "Захват изображений" ('Image Capture')
- [Как скопировать (перенести) фото с iPhone на компьютер (Инструкция)](http://macnoob.ru/ifaq/kak-skopirovat-perenesti-foto-s-iphone-na-kompyuter/)
- [iFunBox](http://www.i-funbox.com/). The File and App Management Tool for iPhone, iPad & iPod Touch. It's available on Windows and Mac OSX, ... and It's Free !

# Midnight commander
https://mdex-nn.ru/page/midnight-commander-na-macos.html
https://midnight-commander.org/wiki/Binaries
https://appstudio.org/articles/66933.html
http://louise.hu/poet/midnight-commander-for-mac-os-x/

# Аналоги Origin
- [SciDAVis](http://scidavis.sourceforge.net/index.html) is a free application for Scientific Data Analysis and Visualization.
- [QtiPlot](https://www.qtiplot.com/) - Data Analysis and Scientific Visualisation

# Проблемы с перемонтированием дисков
- [Make Mac eject external drives when going to slumber or sleep/wake](https://apple.stackexchange.com/questions/362847/make-mac-eject-external-drives-when-going-to-slumber-or-sleep-wake)
- [Is there any way to re-mount an ejected USB device on a Mac?](https://superuser.com/questions/960058/is-there-any-way-to-re-mount-an-ejected-usb-device-on-a-mac/969320#969320)
- [USB flash drive doesn't remount automatically](https://apple.stackexchange.com/questions/381037/usb-flash-drive-doesnt-remount-automatically)
- [Mount & Unmount Drives from the Command Line in Mac OS X](https://osxdaily.com/2013/05/13/mount-unmount-drives-from-the-command-line-in-mac-os-x/)
```
diskutil apfs list
diskutil mount /dev/disk1
```
- [Automatically eject external disks on sleep and reconnect after on OS X](https://www.atpeaz.com/automaticlly-eject-external-disks-on-sleep-reconnect-after-os-x/)

# Mac, python & homebrew
- https://docs.brew.sh/Homebrew-and-Python
- https://formulae.brew.sh/formula/brew-pip
- https://gist.github.com/Daeinar/4383663
- https://www.freecodecamp.org/news/python-version-on-mac-update/
- https://apple.stackexchange.com/questions/284824/remove-and-reinstall-python-on-mac-can-i-trust-these-old-references
- https://stackoverflow.com/questions/52175456/how-to-fix-missing-dependencies-for-python-homebrew

# NTFS
- [How do I convert an NTFS external HDD to exFAT without formatting](https://answers.microsoft.com/en-us/windows/forum/all/how-do-i-convert-an-ntfs-external-hdd-to-exfat/9d833d2e-35fb-49f9-a88b-1db089e5fa6d).

You can use FUSE for macOS to write over NTFS formatted disk by following these steps:
- Download osxfuse.
- Install it.