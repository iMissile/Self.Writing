# Полезные сайты про macos
- [ixrevo](http://ixrevo.me/blog/). Привет! Меня зовут Александр Сокол. Я интересуюсь музыкой, наукой, компьютерами Mac, веб‑дизайном, WordPress разработкой и веду этот блог.
- [MacOS World](http://macosworld.ru/). Про программы.

# Перенос базы Evernote на другой диск
1. Вообще, зачем это надо: [Slim down your SSD with symbolic link](http://www.macworld.com/article/2148490/slim-down-your-ssd-with-symbolic-links.html#tk.nl_mwdaily)
2. [How to Change from the Appstore to the Direct Download Version of Evernote](http://www.christopher-mayo.com/?p=135)
2. Как изменить расположение баз: [This is how I changed the Evernote Data folder to another Hard Drive](https://discussion.evernote.com/topic/37689-this-is-how-i-changed-the-evernote-data-folder-to-another-hard-drive/).
3. Как найти расположение баз Evernote: [Where in the World is Evernote?](https://www.evernote.com/shard/s74/sh/9fad0837-0cb4-4cd4-bfe4-5409dd632127/f5a70bbcd598bd2810ac4b388944f660)


Итого, 
1. Сносим Evernote с помощью CleanMyMac, если стояла инсталляция с AppStore. Загружаем с сайта www.evernote.com
2. В пользовательской директории делаем видимой папку Библиотеки. **chflags nohidden ~/Library**
3. Ищем базу данных. [5.6 Version of the Direct Download](http://www.christopher-mayo.com/?p=135)
/Users/Your Username Here/Library/Application Support/com.evernote.Evernote/accounts/
Переносим ее на внешний диск.
4. Переходим в терминале в директорию где надо сделать ссылку с данными. Делаем Symbolic Link с помощью команды ln -s "перетаскиваем терминал директорию, ссылку на которую надо сделать"



## Акции и скидки
- [MacAppDeals](http://www.macappdeals.com/). Your Source To Finding Discounts On Great Mac Software

# Софт под Мак
## Tools
- [AppZapper](http://www.appzapper.com/). The Unistaller Apple forgot
## Текстовые редакторы
- [Выбор текстового редактора или «хочу все в одном»](http://habrahabr.ru/post/260865/). Победил Brackets

# Разное
- [Запятая и точка на русской клавиатуре Mac. Удобное сочетание клавиш](http://yablyk.com/037778-lajfxak-udobnyj-sposob-nabora-zapyatoj-i-tochki-na-os-x/)