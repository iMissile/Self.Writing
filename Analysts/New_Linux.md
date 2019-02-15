# SSD
- [Настройка Ubuntu для работы с SSD](http://help.ubuntu.ru/wiki/ssd)
- [Ubuntu Gnome 16.04 LTS{How-to} установка на SSD или SSD+HDD в UEFI, часть 1](https://www.youtube.com/watch?v=F_QtH-0eZB8)
- [Список лучших мультимедиа программ для Ubuntu](http://forum.ubuntu.ru/index.php?topic=169108.0)
- [Отключение связки ключей в Ubuntu 16.04](https://squizzer.net/?p=7388)
- Изменение пароля из командной строки. `sudo passwd <имя учетки>`

- [Ubuntu. Boot has 0 Mb](https://askubuntu.com/questions/218783/the-volume-boot-has-only-0-bytes-disk-space-remaining)
`sudo apt-get autoclean && sudo apt-get autoremove`


# shell commands
- [Linux cp command](https://www.computerhope.com/unix/ucp.htm)
- [Linux Rename File Command](https://www.cyberciti.biz/faq/linux-rename-file/)
- [Linux 101 Hacks. Hack 45. Advanced compression using zip command](https://linux.101hacks.com/archive-compression/advanced-compression-using-zip-command/)
- [How to Use zip Command in Linux](https://tecadmin.net/how-to-use-zip-command-line-linux/)
- [Example Uses Of The Linux "gzip" Command](https://www.lifewire.com/example-uses-of-the-linux-gzip-command-4078675)
- [Linux zip command](https://www.computerhope.com/unix/zip.htm)
- [How to zip multiple files into separate archives?](https://superuser.com/questions/430388/how-to-zip-multiple-files-into-separate-archives)
```
find . -name '*.txt.*' -print -exec zip '{}'.zip '{}' \; -exec mv '{}'.zip '{}' \;
```
Find the .txt files
The first -exec zips the files
The second -exec renames the zipped files to the original names

