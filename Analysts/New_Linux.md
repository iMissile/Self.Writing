# Блоги и сборники рецептов
- [Linux Tips, Tricks and Tutorials | Linuxize](https://linuxize.com/)

# другие дистрибутивы
- [Reasons for which I don't use Manjaro anymore](https://github.com/arindas/manjarno)

# SSD
- [Настройка Ubuntu для работы с SSD](http://help.ubuntu.ru/wiki/ssd)
- [Ubuntu Gnome 16.04 LTS{How-to} установка на SSD или SSD+HDD в UEFI, часть 1](https://www.youtube.com/watch?v=F_QtH-0eZB8)
- [Список лучших мультимедиа программ для Ubuntu](http://forum.ubuntu.ru/index.php?topic=169108.0)
- [Отключение связки ключей в Ubuntu 16.04](https://squizzer.net/?p=7388)
- Изменение пароля из командной строки. `sudo passwd <имя учетки>`

- [Ubuntu. Boot has 0 Mb](https://askubuntu.com/questions/218783/the-volume-boot-has-only-0-bytes-disk-space-remaining)
`sudo apt-get autoclean && sudo apt-get autoremove`

# Upgrade
- [How to upgrade](https://ubuntu.com/server/docs/upgrade-introduction). This article details how to upgrade an Ubuntu Server or Ubuntu cloud image to the next release.
- [How to upgrade from Ubuntu 20.04 LTS to 22.04 LTS](https://www.cyberciti.biz/faq/upgrade-ubuntu-20-04-lts-to-22-04-lts/)

# shell commands
- [Linux cp command](https://www.computerhope.com/unix/ucp.htm)
- [Linux Rename File Command](https://www.cyberciti.biz/faq/linux-rename-file/)
- [Linux 101 Hacks. Hack 45. Advanced compression using zip command](https://linux.101hacks.com/archive-compression/advanced-compression-using-zip-command/)
- [How to Use zip Command in Linux](https://tecadmin.net/how-to-use-zip-command-line-linux/)
- [Example Uses Of The Linux "gzip" Command](https://www.lifewire.com/example-	uses-of-the-linux-gzip-command-4078675)
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
- [How to ignore certain filenames using “find”?](https://superuser.com/questions/397307/how-to-ignore-certain-filenames-using-find)


- Чтобы забрать архив. [Архивирование файлов в Linux](https://losst.ru/arhivatsiya-v-linux). Архив != сжатие.
	- Упаковка файла: `$ tar -cvf archive.tar.gz /path/to/files`
	- А чтобы распаковать архив tar linux: `$ tar -xvf archive.tar.gz`. [Recursive tar compression?](https://askubuntu.com/questions/834717/recursive-tar-compression/834720)
	- посмотреть кусочек файла: [View the Beginning of Text Files with head](https://www.linode.com/docs/tools-reference/tools/view-the-beginning-of-text-files-with-head)
Для сжатия надо + использовать флаг `z`?
[Zip]\[unzip](https://www.computerhope.com/unix/unzip.htm)
- [12 Useful “df” Commands to Check Disk Space in Linux](https://www.tecmint.com/how-to-check-disk-space-in-linux/)
- [How do I delete all but 10 newest files in Linux?](https://superuser.com/questions/268344/how-do-i-delete-all-but-10-newest-files-in-linux/268345)
- [How do I set environment variables?](https://askubuntu.com/questions/730/how-do-i-set-environment-variables). 
In bash you can set variables like this: `export CATALINA_HOME=/opt/catalina`
- [How to Check your Ubuntu Version](https://linuxize.com/post/how-to-check-your-ubuntu-version/). `lsb_release -a`
- [Writing Comments in Bash Scripts](https://linuxize.com/post/bash-comments/)
- [Run git pull over all subdirectories {duplicate}](https://stackoverflow.com/questions/3497123/run-git-pull-over-all-subdirectories)
e.g 
`for i in */.git; do ( echo $i; cd $i/..; git pull; ); done`
`ls | xargs -P10 -I{} git -C {} pull`
- Посмотреть размер директорий: `du -h --max-depth=1`

## копирование директорий
- [Rsync (Remote Sync): 10 Practical Examples of Rsync Command in Linux](https://www.tecmint.com/rsync-local-remote-file-synchronization-commands/)
`rsync -avzP 'root@10.0.0.224:/home/data/mt_admin/files/1002\ External-share/6\ x5/2\ POS/gk_202005/' /ext/logs_202005/`
- [How To Resume Partially Transferred Files Over SSH Using Rsync](https://www.ostechnix.com/how-to-resume-partially-downloaded-or-transferred-files-using-rsync/)
- [Copying files using rsync from remote server to local machine](https://stackoverflow.com/questions/9090817/copying-files-using-rsync-from-remote-server-to-local-machine)
cp- Используем команду `cp` для ручного управления процессом копирования. [`cp -irv ./<source>/* ./<destination>`](https://explainshell.com/explain?cmd=cp+-irv)
- COOL! [Recursively copy files from one directory to another](https://askubuntu.com/questions/802238/recursively-copy-files-from-one-directory-to-another). Тут подробно разбирается, почему не получится напрямик cp испоользовать.
	- [`find /media/MyBook/Music -type f -iname '*.mp3' -exec  cp -at /media/HDD/Music {} +`](https://explainshell.com/explain?cmd=find+%2Fmedia%2FMyBook%2FMusic+-type+f+-iname+%27*.mp3%27+-exec+cp+-at+%2Fmedia%2FHDD%2FMusic+%7B%7D+%2B)
	
## регулярки по файлам
- [How to remove lines from the text file containing specific words through terminal?](https://askubuntu.com/questions/354993/how-to-remove-lines-from-the-text-file-containing-specific-words-through-termina). grep/sed/awk approach
- [Is \d not supported by grep's basic expressions?](https://stackoverflow.com/questions/6901171/is-d-not-supported-by-greps-basic-expressions)
- Подробно [How to use grep command In Linux / UNIX with examples](https://www.cyberciti.biz/faq/howto-use-grep-command-in-linux-unix/)
- [How can I grep recursively, but only in files with certain extensions?](https://stackoverflow.com/questions/12516937/how-can-i-grep-recursively-but-only-in-files-with-certain-extensions)
`grep -r --include=\*.json -E -o 'evt_type.{60}'`
- [Regular expressions in grep ( regex ) with examples](https://www.cyberciti.biz/faq/grep-regular-expressions/)

## права доступа
- [How can I check the permissions of a specific group?](https://askubuntu.com/questions/162417/how-can-i-check-the-permissions-of-a-specific-group)
- [“Other” permissions on files](https://unix.stackexchange.com/questions/132245/other-permissions-on-files)
- [How to Copy Files Between Servers via SSH Using Midnight Commander](https://www.lampdocs.com/how-to-copy-files-via-ssh-using-midnight-commander/)
- [Заходим по ssh через Midnight Commander](http://softhelp.org.ua/?p=6889)
- Натолкнулись на проблему управления правами в проекте с Workbench. Оказалось, что система ACL куда шире, чем показывается в `ls -al`. Есть спец. утилиты `setfacl`.
[ACL Linux с использованием setfacl](https://itsecforu.ru/2019/03/14/%F0%9F%9A%A7-acl-linux-%D1%81-%D0%B8%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5%D0%BC-setfacl/)

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
- [How to Update Git to a Newest Version on Linux(Ubuntu 20.04 LTS)](https://www.cyberithub.com/how-to-update-git-to-a-newest-version-on-linux-ubuntu-20-04-lts/)

## Изменение владельца папке (рекурсивное)
`chown shiny:shiny /ext -R`
- [How to Recursively Change the File's Permissions in Linux](https://linuxize.com/post/chmod-recursive/)

## Изменение прав на запуск
- [How to make a file (e.g. a .sh script) executable, so it can be run from a terminal](https://askubuntu.com/questions/229589/how-to-make-a-file-e-g-a-sh-script-executable-so-it-can-be-run-from-a-termi) `chmod +x filename.sh`


# разбиваем pdf на части
Используем утилиту `pdftk` и инструкцию [HowTo: Split PDF File – Linux Command Line](https://www.shellhacks.com/split-pdf-file-linux-command-line/)
- [Как установить pdftk в Ubuntu 18.04 Bionic?](https://ubuntugeeks.com/questions/267120/how-can-i-install-pdftk-in-ubuntu-18-04-bionic)
- [](https://linuxhint.com/install_pdftk_ubuntu/). Method 3 (recommended) Install the PDFtk snap
```
sudo apt-get install snap
sudo snap install pdftk
```

# tmux
- [Getting started with Tmux](https://linuxize.com/post/getting-started-with-tmux/)
- [Tmux on Windows](https://codeandkeep.com/Tmux-on-Windows/). Written on August 8, 2020

# ubuntu не загружается, только GRUB виден
- [How do I boot my PC from GRUB? {duplicate}](https://askubuntu.com/questions/929833/how-do-i-boot-my-pc-from-grub)

# установка на изолированной машине
С помощью доп. ключей установщика можно подготовить полные сборки бинарников на билд машине и перетащить их потом на машину в закрытом контуре.
Информация от Игоря по centos, наработки из STC:
```
dnf install --downloadonly --downloaddir=/root/epel-packages/gdal-devel/ gdal-devel
cd /root/epel-packages/gdal-devel/ && rpm -ivh *.rpm
```
Детально можно читать в инете, например:
- centos
	- [Download RPM Package Using DNF without Installing it](https://linuxopsys.com/topics/download-rpm-using-dnf)
	- [Download RPM packages locally with DNF](https://nts.strzibny.name/download-rpm-packages-locally-with-dnf/)
- ubuntu
	- [How to download deb packages using apt in Ubuntu and Debian](https://www.simplified.guide/ubuntu/apt-download-only)
	- [How to download package not install it with apt-get command?](https://unix.stackexchange.com/questions/408346/how-to-download-package-not-install-it-with-apt-get-command)


# проблемы с менеджером пакетов
- [Как исправить ошибку «E: Could not get lock /var/lib/dpkg/lock» в Ubuntu Linux](https://omgubuntu.ru/kak-ispravit-oshibku-e-could-not-get-lock-var-lib-dpkg-lock-v-ubuntu-linux/)

# zip
- [Zip all files in directory?](https://unix.stackexchange.com/questions/57013/zip-all-files-in-directory)
- [How to tell gzip to keep original file?](https://unix.stackexchange.com/questions/46786/how-to-tell-gzip-to-keep-original-file)
- [Example Uses of the Linux gzip Command](https://www.lifewire.com/example-uses-of-the-linux-gzip-command-4078675)
- [Сжатие и архивация файлов с помощью Gzip, Zip и Tar](http://www.rhd.ru/docs/manuals/enterprise/RHEL-AS-2.1-Manual/getting-started-guide/s1-zip-tar.html)
- [GZip every file separately](https://stackoverflow.com/questions/1792078/gzip-every-file-separately)
```
parallel gzip ::: *
gzip -r .
```
- [Check validity of gz file](https://unix.stackexchange.com/questions/359303/check-validity-of-gz-file). `gzip -v -t file.gz`
- [How do I gunzip all files recursively in a target directory?](https://askubuntu.com/questions/620571/how-do-i-gunzip-all-files-recursively-in-a-target-directory)
- [Script to create individual zip files for each .txt file it finds and move them after](https://stackoverflow.com/questions/12321167/script-to-create-individual-zip-files-for-each-txt-file-it-finds-and-move-them)
- [Test integrity of ZIP file?](https://unix.stackexchange.com/questions/197127/test-integrity-of-zip-file). `unzip -t file`
- [Example Uses Of The Linux "gzip" Command](https://www.lifewire.com/example-uses-of-the-linux-gzip-command-4078675)
- [Linux zip command](https://www.computerhope.com/unix/zip.htm)
- [How to zip multiple files into separate archives?](https://superuser.com/questions/430388/how-to-zip-multiple-files-into-separate-archives)
```
find . -name '*.txt.*' -print -exec zip '{}'.zip '{}' \; -exec mv '{}'.zip '{}' \;
```
Find the .txt files
The first -exec zips the files
The second -exec renames the zipped files to the original names
- [Bash get filename from given path on Linux or Unix](https://www.cyberciti.biz/faq/bash-get-filename-from-given-path-on-linux-or-unix/)
- [Create zip file and ignore directory structure](https://stackoverflow.com/questions/9710141/create-zip-file-and-ignore-directory-structure)
- [How to zip files with same name but different extension?](https://unix.stackexchange.com/questions/417163/how-to-zip-files-with-same-name-but-different-extension)
- [Linux 101 Hacks. Hack 45. Advanced compression using zip command](https://linux.101hacks.com/archive-compression/advanced-compression-using-zip-command/)
- [How to Use zip Command in Linux](https://tecadmin.net/how-to-use-zip-command-line-linux/)
- [How To: Disk Full? - Check Your Trash](https://ubuntuforums.org/showthread.php?t=898573). Гуляем командами по директориям
```
df -Th | sort
du -sh * | sort -n
```
- [How to split a gzip file to several small ones on Linux?](https://www.systutorials.com/how-to-split-a-gzip-file-to-several-small-ones-on-linux/)

# GNU parallel, Исполнение в параллель
- [PARALLELISING JOBS WITH GNU PARALLEL](https://blog.ronin.cloud/gnu-parallel/)
- [A short tutorial on Gnu Parallel](https://www.polarmicrobes.org/a-short-tutorial-on-gnu-parallel/)
- [Get more done at the Linux command line with GNU Parallel](https://opensource.com/article/18/5/gnu-parallel). Turn your computer into a multi-tasking powerhouse.
- [Learn Multi-Threading Bash scripts with GNU Parallel](https://adamtheautomator.com/how-to-speed-up-bash-scripts-with-multithreading-and-gnu-parallel/)
- `parallel gzip ::: *`
GNU Parallel is a fantastic tool that should be used far more in this world where CPUs are only getting more cores rather than more speed. There are loads of examples that we would all do well to take 10 minutes to read
[GNU Parallel Tutorial](https://www.gnu.org/software/parallel/parallel_tutorial.html)
- [What's the difference between nohup and ampersand](https://stackoverflow.com/questions/15595374/whats-the-difference-between-nohup-and-ampersand).
`nohup` + `Rscript`+ `&` сработал) шикардос)
- [Differences Between GNU Parallel And Alternatives](https://www.gnu.org/software/parallel/parallel_alternatives.pdf)
- [Run a specifiable number of commands in parallel - contrasting xargs -P, GNU parallel, and "moreutils" parallel](https://stackoverflow.com/questions/42651475/run-a-specifiable-number-of-commands-in-parallel-contrasting-xargs-p-gnu-par)
- [How can I install GNU Parallel alongside Moreutils on Ubuntu/Debian?](https://superuser.com/questions/917577/how-can-i-install-gnu-parallel-alongside-moreutils-on-ubuntu-debian)

# timing
- [How can I measure the execution time of a terminal process?](https://askubuntu.com/questions/53444/how-can-i-measure-the-execution-time-of-a-terminal-process).
You can use time: `time ls -R`
For a line-by-line delta measurement, try [`gnomon`](https://askubuntu.com/questions/53444/how-can-i-measure-the-execution-time-of-a-terminal-process).

# пакеты
- [Install jq on Ubuntu 20.04](https://lindevs.com/install-jq-on-ubuntu/)
```
sudo apt update
sudo apt install -y jq
# When installation is finished, check jq version:
jq --version
```

# grep/sed
- COOL! [How can I replace each newline (\n) with a space using sed?](https://stackoverflow.com/questions/1251999/how-can-i-replace-each-newline-n-with-a-space-using-sed)
GNU sed has an option, `-z`, for null-separated records (lines). You can just call:
```
sed -z 's/\n/ /g'
!! NOTE: на windows файлах `[\r\n]` !!
```
- [Replace string containing newline in huge file](https://unix.stackexchange.com/questions/137391/replace-string-containing-newline-in-huge-file)
- Отличный поток по обсуждению принципиальных подходов по замене новой строки. `sed` не самый лучший инструмент для этого. [How can I replace each newline (\n) with a space using sed?ъ(https://stackoverflow.com/questions/1251999/how-can-i-replace-each-newline-n-with-a-space-using-sed)