# Блоги и сборники рецептов
- [Linux Tips, Tricks and Tutorials | Linuxize](https://linuxize.com/)

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
- COOL! [How to Remove (Delete) Directory in Linux](https://linuxize.com/post/remove-directory-linux/)
`$ find . -type d -name '*_cache' -exec rm -r {} +`
`$ find /dir -type d -empty -delete`


- Чтобы забрать архив. [Архивирование файлов в Linux](https://losst.ru/arhivatsiya-v-linux). Архив != сжатие.
	- Упаковка файла: `$ tar -cvf archive.tar.gz /path/to/files`
	- А чтобы распаковать архив tar linux: `$ tar -xvf archive.tar.gz`. [Recursive tar compression?](https://askubuntu.com/questions/834717/recursive-tar-compression/834720)
	- посмотреть кусочек файла: [View the Beginning of Text Files with head](https://www.linode.com/docs/tools-reference/tools/view-the-beginning-of-text-files-with-head)
Для сжатия надо + использовать флаг `z`?
[Zip]\[unzip](https://www.computerhope.com/unix/unzip.htm)
- [12 Useful “df” Commands to Check Disk Space in Linux](https://www.tecmint.com/how-to-check-disk-space-in-linux/)
- [Rsync (Remote Sync): 10 Practical Examples of Rsync Command in Linux](https://www.tecmint.com/rsync-local-remote-file-synchronization-commands/)
`rsync -avzP 'root@10.0.0.224:/home/data/mt_admin/files/1002\ External-share/6\ x5/2\ POS/gk_202005/' /ext/logs_202005/`
- [How To Resume Partially Transferred Files Over SSH Using Rsync](https://www.ostechnix.com/how-to-resume-partially-downloaded-or-transferred-files-using-rsync/)
- [Copying files using rsync from remote server to local machine](https://stackoverflow.com/questions/9090817/copying-files-using-rsync-from-remote-server-to-local-machine)
- [How do I delete all but 10 newest files in Linux?](https://superuser.com/questions/268344/how-do-i-delete-all-but-10-newest-files-in-linux/268345)

## права доступа
- [How can I check the permissions of a specific group?](https://askubuntu.com/questions/162417/how-can-i-check-the-permissions-of-a-specific-group)
- [“Other” permissions on files](https://unix.stackexchange.com/questions/132245/other-permissions-on-files)
- [How to Copy Files Between Servers via SSH Using Midnight Commander](https://www.lampdocs.com/how-to-copy-files-via-ssh-using-midnight-commander/)
- [Заходим по ssh через Midnight Commander](http://softhelp.org.ua/?p=6889)

# Windows + Linux
- [Windows for a Linux guy](https://dev.to/azure/windows-for-a-linux-guy-390p)
- [How to tell the difference between apt-get upgrade, apt-get dist-upgrade, and do-release-upgrade](https://www.techrepublic.com/article/how-to-tell-the-difference-between-apt-get-upgrade-apt-get-dist-upgrade-and-do-release-upgrade/)

# Ubuntu, управление пакетами
- [How to install/repair texlive-doc on Ubuntu?](https://tex.stackexchange.com/questions/470019/how-to-install-repair-texlive-doc-on-ubuntu)
- [How to install packages without documentation?](https://askubuntu.com/questions/221241/how-to-install-packages-without-documentation)
- [Remove documentation to save hard drive space](https://askubuntu.com/questions/129566/remove-documentation-to-save-hard-drive-space)
And removing them:
```
apt-get remove --purge \
  texlive-fonts-recommended-doc texlive-latex-base-doc texlive-latex-extra-doc \
  texlive-latex-recommended-doc texlive-pictures-doc texlive-pstricks-doc
```
- [Check Debian/Ubuntu Linux package version using apt-get/aptitude command](https://www.cyberciti.biz/faq/debian-ubuntu-linux-apt-get-aptitude-show-package-version-command/)

## Изменение владельца папке (рекурсивное)
`chown shiny:shiny /ext -R`
- [How to Recursively Change the File's Permissions in Linux](https://linuxize.com/post/chmod-recursive/)

## Изменение прав на запуск
- [How to make a file (e.g. a .sh script) executable, so it can be run from a terminal](https://askubuntu.com/questions/229589/how-to-make-a-file-e-g-a-sh-script-executable-so-it-can-be-run-from-a-termi) `chmod +x filename.sh`
