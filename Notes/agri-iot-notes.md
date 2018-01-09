# Настройка машины-сборщика данных

## Настройка Linux
- [How to accurately check if package is installed in yum?](https://serverfault.com/questions/558936/how-to-accurately-check-if-package-is-installed-in-yum)
Для нормального функционирования сервера требуется корректно настроить текущее время и его своевременное обновление с определенной периодичностью. Детали смотрим в статье ["Как установить, изменить время и часовой пояс в CentOS 7"](https://serveradmin.ru/ustanovka-nastroyka-i-sinhronizatsiya-vremeni-v-centos/).  

Важные комментарии к статье: Подскажите, пожалуйста, почему после перезагрузки ОС ntp может не стартовать?
Команду `systemctl enable ntpd` выполнил.

Разобрался. Дело в том что CentOS7 для синхронизации времени по умолчанию использует сервис chrony. ntpd не будет стартовать автоматически пока не отключишь chrony.
Что бы отключить chrony нужно выполнить команду: `systemctl disable chronyd.service`
А вообще chrony по функциям очень сильно напоминает ntpd.

Также смотрим статью ["CentOS 7 настройка сервера"](https://serveradmin.ru/centos-7-nastroyka-servera/). Тут учтены нюансы, связанные с сервисом chrony в 7-ой версии CentOS.

### Файервол
Штатно CentOS 7 идет с новым брэндмауэром -- `firewalld`. По настройке можно поглядеть на 
- [Настройка firewalld CentOS 7 с примерами команд](https://bozza.ru/art-259.html)
- [НАСТРОЙКА БРАНДМАУЭРА FIREWALLD В CENTOS 7](https://www.8host.com/blog/nastrojka-brandmauera-firewalld-v-centos-7/)
```
firewall-cmd --get-active-zones
sudo firewall-cmd --set-default-zone=trusted
sudo firewall-cmd --reload
firewall-cmd --get-active-zones
```




### Настройка синхронизации времени
В 7-ой версии CentOS настройку делаем через утилиту chrony (детали в статьях, указанных выше).

 - Устанавливаем (если не стоит): `yum install -y chrony`
 - Запускаем chrony и добавляем в автозагрузку: 
 	- `systemctl start chronyd`
 	- `systemctl enable chronyd`
 - Проверяем, нормально ли запустился: `systemctl status chronyd`

### Добавление OS репозиториев
Для инсталляции различного софта необходимо подключить репозитории в CentOS. Наиболее популярные это EPEL и rpmforge (note: в январе 2017 больше не поддерживается), поэтому добавим их. Сначала ставим EPEL. С ним все просто, он добавляется из стандартного репозитория:
`yum -y install epel-release`

### Перезагрузка
`reboot now`

### Операции с файлами
- [How do I remove a full directory in Linux?](http://www.computerhope.com/issues/ch000798.htm) `rm -rf mydir`
- [How do I recursively delete directories with wildcard?](http://unix.stackexchange.com/questions/23576/how-do-i-recursively-delete-directories-with-wildcard)
	- С натяжкой (см. детали выше) `find . -type d -name "00LOCK*" -delete`. Но не удаляет непустые директории.
	- `find . -type d -name '00LOCK*' -exec rm -r {} +` (. -- от текущего пользователя, / --от корня)
- Посмотреть рзмер папок в директории с глубиной до первых директорий: `du -h --max-depth=1`

## Установка R
Установка под Linux не совсем прозрачно описана, поэтому читаем отдельные блоги.

- [Yum, шпаргалка](https://habrahabr.ru/post/301292/)
- Неплохой гид про борьбу с 'dependency hell': ["Installing RStudio — an advanced GUI for R — on CentOS 6"](https://biolives.wordpress.com/2013/07/09/installing-rstudio-an-advanced-gui-for-r-on-centos-6/). Там находим решение с пакетом Cairo.
- Пошаговая инструкция. [How Install R / R Studio on CentOS 7](http://linoxide.com/linux-how-to/install-r-rstudio-centos-7/). Важно, что R работает не из под рута.
- [How to install R on CentOS](http://stackoverflow.com/questions/37769985/how-to-install-r-on-centos). Речь идет об инсталляции староq версии R. The installed version is 3.3.0. I would like to install version 2.X but I don't know how.
- На заметку: при инсталляции пакетов возникло диагностическое сообщение "Delta RPMs disabled because /usr/bin/applydeltarpm not installed". Надо почитать.
- Проверяем версию CentOS командой `uname -a`
- Ставим RStudio Server по [инструкции](https://www.rstudio.com/products/rstudio/download-server/) с RStudio 
- [Запускаем RStudio](http://youriporhosname:8787/) и логинимся под созданным non-root пользователем.
- Ставим Python по инструкции. The IUS repo community has done a wonderful job of providing the absolute latest Python 3 releases as rpm packages for RHEL and CentOS that easily install alongside the default system Python.
	- [Install Latest Python on CentOS 7](http://www.codeghar.com/blog/install-latest-python-on-centos-7.html)
	- Еще инструкция: ["How To Install Python 3 and Set Up a Local Programming Environment on CentOS 7"](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-centos-7)
	- [How to Install Pip on CentOS 7](https://www.liquidweb.com/kb/how-to-install-pip-on-centos-7/)
```
sudo yum install -y https://centos7.iuscommunity.org/ius-release.rpm
sudo yum install R
sudo yum update
```
	 
- При установке пакетов под root (для всех) запускаем R от рута `sudo -i R` и прогоняему установку. Для успешного прогона необходимо доставлять системные либы (CentOS specific commands).
`groupinstall` ставит серию связанных в группу пакетов. Информацию по этой группе можно посмотреть командой
`yum groupinfo X11`

```
	sudo yum -y install wget epel-release chrony tree
 	sudo yum -y install R

	sudo yum groupinstall X11
	sudo yum groupinstall "Development Tools"

	sudo yum install libcurl-devel
	sudo yum install openssl-devel
	sudo yum install cyrus-sasl-devel
	sudo yum install libxml2-devel
	sudo yum install libpng-devel
	sudo yum install libjpeg-devel
	sudo yum install python
	sudo yum install python-devel
	sudo yum install proj
	sudo yum install proj-devel
	sudo yum install mesa-libGL mesa-libGL-devel mesa-libGLU mesa-libGLU-devel
	sudo yum install gmp-devel
	sudo yum install mpfr-devel
	sudo yum install cairo-devel
	sudo yum install libXt-devel
	sudo yum install gtk2-devel
	sudo yum install v8-devel
	sudo yum install udunits2
	sudo yum install udunits2-devel
	sudo yum install xorg-x11-server-Xvfb
	sudo yum install unixODBC*
	sudo yum install postgresql-devel
        sudo yum install mariadb-devel mysql-devel
	sudo yum install gcc-gfortran*
	sudo yum install texlive*
	sudo yum install ufw
        sudo yum install dejavu*
	sudo yum install psmisc
	sudo yum install rrdtool
        sudo yum install wireshark
	# а это надо для RStudio Connect
	sudo yum install dejavu-fonts-common dejavu-sans-mono-fonts rrdtool
	# а это для RStudio Server
	sudo yum install psmisc
	sudo yum install lrzsz
	# а это для картографии (увы, gdal встает старый, ветки 1.x)
	sudo yum install gdal* proj-devel proj-epsg proj-nad protobuf-devel geos-devel

	'# # надо выяснять актуальную версию
	sudo yum install java-1.8.0-openjdk.x86_64 
	
	'# это я бы не ставил, если не потребуется
	sudo yum -y groupinstall "X Window System" "Desktop" "Fonts" "General Purpose Desktop"
	sudo yum install -y https://centos7.iuscommunity.org/ius-release.rpm
	sudo yum update	
```

### Готовая последовательность команд по установке пакетов
**Загоняем в одну команду** `yum install package1 package2 package3......`, [How to install multiple packages using yum](http://www.linuxquestions.org/questions/linux-newbie-8/how-to-install-multiple-packages-using-yum-850364/):
```
sudo yum -y install epel-release chrony tree
sudo yum -y install R
sudo yum -y install -y https://centos7.iuscommunity.org/ius-release.rpm

sudo yum -y groupinstall X11
sudo yum -y groupinstall "Development Tools"

sudo yum -y install wget libcurl-devel openssl-devel cyrus-sasl-devel libxml2-devel libpng-devel libjpeg-devel python python-devel proj proj-devel mesa-libGL mesa-libGL-devel mesa-libGLU mesa-libGLU-devel gmp-devel mpfr-devel cairo-devel libXt-devel gtk2-devel v8-devel udunits2 udunits2-devel xorg-x11-server-Xvfb unixODBC* postgresql-devel mariadb-devel mysql-devel gcc-gfortran* texlive*, ufw, dejavu*, psmisc, rrdtool, wireshark, lrzsz

sudo yum -y install dejavu-fonts-common dejavu-sans-mono-fonts rrdtool psmisc lrzsz gdal* proj-devel proj-epsg proj-nad protobuf-devel geos-devel
```
и
```
	'# это я бы не ставил, если не потребуется
	sudo yum -y groupinstall "X Window System" "Desktop" "Fonts" "General Purpose Desktop"
	sudo yum update	
```


- Поиск пакетов по репозиторию: `sudo yum search python | grep dev`

- Пакеты надо ставить из под рута, в помощь очень полезные статьи:
	- [Using R — Installing Packages](http://mazamascience.com/WorkingWithData/?p=728)
	- [Using R — Package Installation Problems](http://mazamascience.com/WorkingWithData/?p=1185)
	- Обновление установленных пакетов делаем из под рута в консоли R с помощью пакета pacman: `pacman::p_update(update = TRUE, ask = FALSE)`
	- Еще проще сделать обновление R функцией `update.packages()`
	- Поглядим что вообще лежит в репозитории `yum repo-pkgs epel list gdal*`
	- Поглядим, какие пакете установлены в системе: `rpm -qa | grep gdal`


- Запуск скрипта из консоли linux: `R < script.R --no-save`. Выводит все на экран, можно поглядеть ошибки
### Проблемы при установке пакетов

- Картография
	- При установке пакета `tmap` потащилась вся картография. Надо ставить GDAL. (configure: error: gdal-config not found or not executable). Ответ ищем в [Installing GDAL on CentOS?](https://gis.stackexchange.com/questions/130324/installing-gdal-on-centos). Ошибка *libproj and/or proj_api.h not found in standard search locations*. Это связано с пакетом RGDAL (картография). Ответ находим здесь: [rgdal package installation](http://stackoverflow.com/questions/15248815/rgdal-package-installation).
	- Установка пакета rgl потребовала еще массу системных пакетов. Детали читаем здесь: ["How to install R “rgl” package under centos 6?"](http://stackoverflow.com/questions/33512641/how-to-install-r-rgl-package-under-centos-6)
[Ставить надо с EPEL](https://fedoraproject.org/wiki/EPEL/FAQ#howtouse). Решение: ставим все пакеты `sudo yum install gdal*` + сопутствующие `sudo yum install proj-devel proj-epsg proj-nad`
	- Для вспомогательного пакета `protolite` требуется поставить в ОС пакет `protobuf-devel`.
	- Для пакета `rgeos` требуется библиотека `libgeos`: [Error installing R package for Linux](https://stackoverflow.com/questions/38924767/error-installing-r-package-for-linux). Попутно выясняем, что в репозитории CentOS эта библиотека переименована. [centos libgeos repository missing](https://stackoverflow.com/questions/42097501/centos-libgeos-repository-missing). В итоге, ставится командой `sudo yum install geos-devel`
	- Пакет `sf` не компилируется, выходит с ошибкой `configure: error: sf is not compatible with GDAL versions below 2.0.0`. Какая-то проблема между различными компонентами gdal (gdal-config is part of the package libgdal-dev, while gdalinfo is part of gdal-bin.). Несколько изысканий. [trouble installing “sf” due to “gdal”](https://stackoverflow.com/questions/44973639/trouble-installing-sf-due-to-gdal). И [Different output of gdalinfo --version and gdal-config in Xenial](https://gis.stackexchange.com/questions/246615/different-output-of-gdalinfo-version-and-gdal-config-in-xenial). Смотрим установленную версию командой `gdalinfo --version` и `gdal-config --version`. Смотрим на [пакеты gdal](https://apps.fedoraproject.org/packages/gdal): 
Надо собирать самостоятельно [[gdal-dev] How to install GDAL 2.x on CentOS 7 without being by building from source?](https://lists.osgeo.org/pipermail/gdal-dev/2017-February/046024.html).
Поглядим что вообще лежит в репозитории `yum repo-pkgs epel list gdal*`
Для сборки отсылают сюда: [RPM resource gdal](https://www.rpmfind.net/linux/rpm2html/search.php?query=gdal)

Есть альтернативные предложения: [(1) How to install GDAL 2.x on CentOS 7 without building from source?](https://www.tutel.me/c/gis/questions/227929/how+to+install+gdal+2x+on+centos+7+without+being+by+building+from+source). Рекомендуют не полную Anaconda, а miniconda.
[(2) How to install GDAL 2.x on CentOS 7 without building from source?](https://gis.stackexchange.com/questions/227929/how-to-install-gdal-2-x-on-centos-7-without-building-from-source)
- Самостоятельная сборка GDAL по шагам:
	1. Удалить системную библиотеку: `yum remove gdal-1.11.4` и  `yum remove gdal-devel-1.11.4 gdal-doc-1.11.4 gdal-libs-1.11.4`
	2. Проверить систему `rpm -qa | grep gdal`
	3. скачать архив и исходниками gdal-а куда-нибудь (у меня в /tmp). (http://download.osgeo.org/gdal/CURRENT/)
	4. распаковать `tar zxvf ./gdal-2.2. ....tar.gz`
	5. зайти туда: `cd /tmp/gdal-2.2....`
	6. сказать: `./configure`
	7. сказать: `make`
	8. сказать: `make install` (от root)
	9. в `/root/.bash_profile` добавить в PATH `:/usr/local/bin`, `source ~/.bash_profile` 


- В логах возникала ошибка **Error in readRDS(pfile) : error reading from connection when updating, loading, installing packages**. Возможные варианты решения:
	- [RStudio Support](https://support.rstudio.com/hc/en-us/community/posts/203864278-Error-in-readRDS-pfile-error-reading-from-connection-when-updating-loading-installing-packages): Fixed by reinstalling ggthemes which had some 0 sized files previously. In general might be fixed by looking for such files. These can be found with
`find /usr/local/lib64/R/site-library/ /usr/lib64/R/library/ /usr/lib/R/site-library/ ~/.local/lib/ -iname '*rds' -a -size 0`. Указываем 64, поскольку инсталляция у нас 64-х битная.
- Установка пакета Rmpfr приводит к таким ошибкам: 
	- *GNU MP not found, or not 4.1.4 or up, see http://gmplib.org*. Решение этой проблемы читаем здесь: ["In R, using Ubuntu, try to install a lib depending on GMP C lib, it won't find GMP, but I have GMP installed"](http://stackoverflow.com/questions/22277440/in-r-using-ubuntu-try-to-install-a-lib-depending-on-gmp-c-lib-it-wont-find-g). И на [сайте GMP](https://gmplib.org/). GMP is a free library for arbitrary precision arithmetic, operating on signed integers, rational numbers, and floating-point numbers. There is no practical limit to the precision except the ones implied by the available memory in the machine GMP runs on. GMP has a rich set of functions, and the functions have a regular interface.
	- "configure: error: Header file mpfr.h not found; maybe use --with-mpfr-include=INCLUDE_PATH ERROR: configuration failed for package ‘Rmpfr’". Решение читаем здесь: ["R package Rmpfr"](http://stackoverflow.com/questions/31311050/r-package-rmpfr)
- Установка пакета Cairo:
	- Ошибка [xlib-backend.c:34:74: fatal error: X11/Intrinsic.h: No such file or directory. compilation terminated](http://stackoverflow.com/questions/23642353/error-message-installing-cairo-package-in-r) лечится установкой `libXt-devel'
- Установка пакета mongolite:
	- Ошибка [R: Error in dyn.load(file, DLLpath = DLLpath, …)](http://stackoverflow.com/questions/38943764/r-error-in-dyn-loadfile-dllpath-dllpath)
- Установка пакета gWidgetstcltk, связанного с установкой extremevalues:
	- Ошибка "Error in structure(.External(.C_dotTclObjv, objv), class = "tclObj")" 
	- Связанная ошибка [no DISPLAY variable so Tk is not available for R](http://terradelfoc.blogspot.ru/2014/10/no-display-variable-so-tk-is-not.html)
	
	Это все вызвано отсутствием подсистемы X11 на машине. По идее лечится (но не получилось) установкой всего графического десктопа: [Installing the Graphical Window System (X.org-X11) and the Default Desktop Environment on CentOS 6](http://www.linuxquestions.org/questions/blog/gearge-611791/installing-the-graphical-window-system-x-org-x11-and-the-default-desktop-environment-on-centos-6-4098/). Если пакеты с tk\tcl интерфейсом не требуются, то можно и не ставить.   
	Есть еще вариант: ["How to run R on a server without X11, and avoid broken dependencies"](http://stackoverflow.com/questions/1710853/how-to-run-r-on-a-server-without-x11-and-avoid-broken-dependencies). Тут рекомендуют "*Use the virtual framebuffer X11 server -- we do the same to build packages requiring X11 for R builds in headless chroots*." Читаем дальше [How to install and configure Xvfb in Linux/Centos](http://ithubinfo.blogspot.ru/2013/11/how-to-install-and-configure-xvfb-in.html)  
	
	Эмуляция X11 приводит к проблеме появления окна с выбором CRAN репозитория, а в консоли это не отображается. Поэтому надо вручную установить репозиторий. Детали читаем в переписке ["How to select a CRAN mirror in R"](http://stackoverflow.com/questions/11488174/how-to-select-a-cran-mirror-in-r). Как резюме, перед инсталляцией надо исполнить команду `chooseCRANmirror(graphics=FALSE, ind=37)`. 37 -- Россия, список индексов отображается просто командой `chooseCRANmirror()`.
	
	УРА!!!!! Набор шаманств позволил поставить пакет следующими командами:
	```
	sudo yum install xorg-x11-server-Xvfb
	sudo -i xvfb-run R --no-save
	chooseCRANmirror(graphics=FALSE, ind=37)
	pacman::p_load("gWidgetstcltk")
	```
- Установка пакета `printr` делается ручками. В CRAN его нет, а частный репозиторий организован криво. Последовательность команд такова:
```
wget https://yihui.name/xran/src/contrib/printr_0.0.6.tar.gz
install.packages(<pathtopackage>, repos = NULL, type="source")
install.packages("printr_0.0.6.tar.gz", repos = NULL, type="source")
```
- Установка пакета `DiagrammeRsvg` требует установки библиотек V8
- Установка пакета `ggforce` требует установки библиотек udunits2
- Установка пакета `udunits2`, используемого пакетом `thomasp85/ggforce` приводит к ошибке:
```
     -----Error: udunits2.h not found-----
     If the udunits2 library is installed in a non-standard location,
     use --configure-args='--with-udunits2-lib=/usr/local/lib' for example,
     or --configure-args='--with-udunits2-include=/usr/include/udunits2'
     replacing paths with appropriate values for your installation.
     You can alternatively use the UDUNITS2_INCLUDE and UDUNITS2_LIB
     environment variables.
     If udunits2 is not installed, please install it.
     It is required for this package.
```
Частично почитать ответы по загрузке пакета `udunits2` можно здесь: ["Installing packages with complex dependencies"](https://github.com/PecanProject/pecan/issues/71). После установки библиотек ищем расположение h файлов следующей командой `find . -type f -name udunits2.h` и запускаем инсталляцию с параметрами:
`install.packages("udunits2", configure.args='--with-udunits2-include=/usr/include/udunits2/')`

**Может возникнуть ситуация**, когда потребуется доставлять фортран. Детально (в т.ч. и про управление пользователями) можно почитать в этой публикации: ["Install RStudio Server on centOS6.5"](http://blog.supstat.com/2014/05/install-rstudio-server-on-centos6-5/): 
`sudo yum install gcc-gfortran*`

- Проблема при установке RODBC: "ODBC headers sql.h and sqlext.h not found". Решается установкой `yum install unixODBC*`

- Проблема при установке stringi: 
```
checking for ICU4C >= 52... no
*** ICU4C 50.1.2 has been detected
*** Minimal requirements, i.e., ICU4C >= 52, are not met
trying URL 'https://raw.githubusercontent.com/gagolews/stringi/master/src/icu55/data/icudt55l.zip'
```
Читаем файл [INSTALL](https://github.com/gagolews/stringi/blob/0410dbde81bd9329914a6674aea76b2b4d68c25c/INSTALL): 'The stringi package depends on the ICU4C >= 52 library' (a custom subset of ICU4C 55.1 is shipped with the package).

Подробно описано в [How to get latest version of ICU instead the default v50.1?](https://www.centos.org/forums/viewtopic.php?t=60684). Там решение не найдено.
Идем на домашнюю страницу проекта: [ICU-TC Home Page](http://site.icu-project.org/)
Шаги по установке (оказалось, не работает)
```
tar zxvf icu4c-59_1-src.tgz
cd icu/source
./configure # сделали makefile убедились, что все ок
make
sudo make install
```
Рабочий вариант найден здесь:
- [How to install stringi from local file (ABSOLUTELY no Internet Access)](https://stackoverflow.com/questions/31942322/how-to-install-stringi-from-local-file-absolutely-no-internet-access)
- [How to install stringi library from archive and install the local icu52l.zip](https://stackoverflow.com/questions/27553452/how-to-install-stringi-library-from-archive-and-install-the-local-icu52l-zip)
Скачиваем пакет [ICU](https://raw.githubusercontent.com/gagolews/stringi/master/src/icu55/data/icudt55l.zip), требуемый для сборки `stringi` (конкретный адрес будет виден в сообщениях об ошибке при сборке stringi).
Инсталлируем командой `install.packages("stringi", configure.vars="ICUDT_DIR=/tmp/")`, положив перед этим в `/tmp` файл `icudt55l.zip`
- Для Connect пробуем следующий ход:
1. Скачать и положить `icudt55l.zip` (а может из zip тоже).
2. Исправляем в `/usr/lib64/R/etc/Renviron`:
```
# manual ICUDT
ICUDT_DIR=/opt/icu55/data
# --------------------
```
- RMySQL не ставится. Требует системных библиотек, решается командой `sudo yum -y install mariadb-devel mysql-devel`

- Подключение к MS SQL из-под linux требует доп. шагов по установке драйверов

["Установка Microsoft ODBC Driver for SQL Server для Linux и macOS"](https://docs.microsoft.com/ru-ru/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server):
```
sudo su
curl https://packages.microsoft.com/config/rhel/7/prod.repo > /etc/yum.repos.d/mssql-release.repo
exit
sudo yum remove unixODBC-utf16 unixODBC-utf16-devel #to avoid conflicts
sudo ACCEPT_EULA=Y yum install msodbcsql
```

## Установка RStudio Server
[Страница загрузки](https://www.rstudio.com/products/rstudio/download-server/)

- Prerequisites  
RStudio Server v0.99 requires RedHat or CentOS version 5.4 (or higher) as well as an installation of R. You can install R for RedHat and CentOS using the instructions on CRAN: https://cran.rstudio.com/bin/linux/redhat/README.

See the [Getting Started document](https://support.rstudio.com/hc/en-us/articles/200552306-Getting-Started) for information configuring and managing the server.

By default RStudio Server runs on port 8787 and accepts connections from all remote clients. After installation you should therefore be able to navigate a web browser to the following address to access the server:
`http://<server-ip>:8787`

## Purging RStudio Connect
Глава 14 в Admin Guide

### Управление пользователями
Тут не все прозрачно, пытаемся разобраться по частям.

- Создаем в linux пользователяю [CentOS Guide. 33.2.2. Adding a User](https://www.centos.org/docs/5/html/5.1/Deployment_Guide/s2-users-add.html):
	- Issue the useradd command to create a locked user account: `useradd <username>`
	- Unlock the account by issuing the passwd command to assign a password and set password aging guidelines: `passwd <username>`

- [The Complete Guide to “useradd” Command in Linux – 15 Practical Examples](http://www.tecmint.com/add-users-in-linux/)


- [RStudio prohibits signing in with a user id below 100. Make sure your user id is above this threshold.](https://support.rstudio.com/hc/en-us/articles/200717203-RStudio-Server-Log-in-and-User-Authentication-Problems). А root имеет id=0.
- [How can I look up a username by id in linux?](http://unix.stackexchange.com/questions/36580/how-can-i-look-up-a-username-by-id-in-linux). `id -u <user-name>`

[Дополнительные ограничения](https://support.rstudio.com/hc/en-us/articles/200552306-Accessing-RStudio-Server-Open-Source):  
- RStudio Server will not permit logins by system users (those with user ids lower than 100).  
- User credentials are encrypted using RSA as they travel over the network.  
- You can manage users with standard Linux user administration tools like useradd, userdel, etc.  
- Each user needs to be created with a home directory.

If you are unable to access the server after installation, you should run the verify-installation command to output additional diagnostics:
`$ sudo rstudio-server verify-installation`

В официальной документации на RStudio Server Pro есть такой пункт:
```
3.2 Restricting Access to Specific Users
3.2.1 Minimum User Id
By default RStudio Server only allows normal (as opposed to system) users to successfully authenticate.
The minimum user id is determined by reading the UID_MIN value from the /etc/login.defs
file. If the file doesn’t exist or UID_MIN isn’t defined within it then a default value of 1000 is used.
You change the minimum user id by specifying the auth-minimum-user-id option. For example:
/etc/rstudio/rserver.conf
```
## Установка Shiny Server
Зависимости:
```
===========================================================================================================================================
 Package                          Архитектура      Версия                    Репозиторий                                             Размер
===========================================================================================================================================
Установка:
 shiny-server                     x86_64           1.5.3.770-1               /shiny-server-commercial-1.5.3.770-rh5-x86_64           288 M
Установка зависимостей:
 dejavu-fonts-common              noarch           2.33-6.el7                base                                                     64 k
 dejavu-sans-mono-fonts           noarch           2.33-6.el7                base                                                    433 k
 psmisc                           x86_64           22.20-11.el7              base                                                    141 k
 rrdtool                          x86_64           1.4.8-9.el7               base                                                    440 k
```

### Open Source edition
Читаем оригинальную инструкцию по инсталляции ["Installing Shiny Server Open Source"](https://www.rstudio.com/products/shiny/download-server/)

### Pro edition
Загружаем пакет [отсюда](https://www.rstudio.com/products/shiny/download-commercial/)

После инсталляции и проверки запуска настраиваем доступ в админскую консоль:
"
This configuration will also create an administrative dashboard running on port 4151. The admin interface requires that a user authenticate themselves, which is discussed further in the chapter on Authentication & Security. The configuration will attempt to use a flat-file authentication system stored at `/etc/shiny-server/passwd`; an empty database is created for you here during installation. To create a new user named admin in this file to allow you to login to the dashboard, execute the following command
```
$ sudo /opt/shiny-server/bin/sspasswd /etc/shiny-server/passwd admin
and then enter and verify the password you wish to use for this user.
```
"

## Проверяем жизнеспособность
Once installed, view the [Administrator’s Guide](http://docs.rstudio.com/shiny-server/) to learn how to manage and configure Shiny Server. Stay up to date on Shiny Server news and software updates by subscribing above.

- Проверяем, что процесс запущен:  
`sudo systemctl status shiny-server`
- Cмотрим log файл:  
`cat /var/log/shiny-server.log`

По умолчанию Shiny Server доступен по порту 3838.
Админ консоль (Pro версия) доступна по порту 4151

Смапируем наше приложение на location '/iot'. 
Делается это в конфиге `/etc/shiny-server/shiny-server.conf`. Читаем мануал '2.2.2 Location'  
И рестартуем сервер  
`sudo systemctl restart shiny-server`

При проблемах функционирования начинаем читать логи:  
- `systemctl status shiny-server.service`  
- `journalctl -xe` for details.

Местоположение логов приложений определяется в конфиге:	
```
location / {
  log_dir /var/log/shiny-server/;
}
```
- Как запретить удалять логи приложений. Краткая статья про логи: [Shiny Server Error Logs](https://support.rstudio.com/hc/en-us/articles/115003717168-Shiny-Server-Error-Logs)
You can override this behavior using the `preserve_logs` configuration option. If you set `preserve_logs true`; in your configuration file, Shiny Server will never delete the logs from your R processes, regardless of their exit code.
- [Troubleshooting applications in Shiny Server Pro](https://support.rstudio.com/hc/en-us/articles/220315848-Troubleshooting-applications-in-Shiny-Server-Pro)
Ответ: `preserve_logs` надо ставить на top level. После запуска видно, что не хватает прав создать файл логгера приложения.
Надо дать полные права пользователю `shiny` (он в конфиге прописан как `run_as`) на `/srv/shiny-server`.
Можно командой `sudo chown -R shiny /srv/shiny-server`
- Удаление директории в Linux: [How do I remove a full directory in Linux?](https://www.computerhope.com/issues/ch000798.htm): `rm -rf mydir`
- Кирилл придумал такое решение:
	1. поменял у `/srv/shiny-server` группу на `shiny` (была root)
	2. поставил на `/srv/shiny-server` флаг `setguid`, что бы при копировании туда файлов наследовалась группа (https://en.wikipedia.org/wiki/Setuid#setgid_on_directories)
	3. сделал `chmod g+rwx /srv/shiny-server`
- [Give user write access to folder {duplicate}](https://askubuntu.com/questions/402980/give-user-write-access-to-folder)

- Ошибка при запуске: `/opt/shiny-server/ext/activation/license-manager: error while loading shared libraries: libssl.so.6: cannot open shared object file: No such file or directory`. 
Поиск библиотеки `find / -name libssl.so` дает следующее: `/usr/lib64/libssl.so`. Ответ -- поставил версию не под тот CentOS.

## Настройка локального репозитория
См. документацию по установке, п. [1.3.4 Install Shiny](http://docs.rstudio.com/shiny-server/#stopping-and-starting)
Setup the Server for Secure Package Installation
You should also specify a secure default CRAN mirror in this same file. You can do that using the following code:
```
local({
  r <- getOption("repos")
  r["CRAN"] <- "https://cran.rstudio.com/"
  options(repos=r)
})
```

### Обновление Shiny Server
Читаем [Upgrading Shiny Server](https://support.rstudio.com/hc/en-us/articles/216080017-Upgrading-Shiny-Server):
If you are upgrading to a later version of Shiny Server Open-source or Pro, you can do so by downloading the newer package and installing it using your package manager:
```
sudo gdebi <shiny-server-package.deb>
```
or
```
sudo yum install --nogpgcheck <shiny-server-package.rpm>
```

Your configuration and settings will be unchanged from the previous version, and if you are running Shiny Server Pro, your license status will remain untouched as well.


### Управление Shiny Server
Читаем ["1.4 Stopping and Starting"](http://docs.rstudio.com/shiny-server/#stopping-and-starting)
CentOS:
```
sudo systemctl status shiny-server
sudo systemctl start shiny-server
sudo systemctl stop shiny-server
sudo systemctl restart shiny-server
```


### Настройка Shiny Server для нескольких пользователей
Читаем мануал + разъяснительную статью ["Shiny Server Quick Start: Run Shiny Server on multiple ports"](https://support.rstudio.com/hc/en-us/articles/219045167-Shiny-Server-Quick-Start-Run-Shiny-Server-on-multiple-ports)

Конфигурационный файл расположен `/etc/shiny-server/shiny-server.conf`
По шагам:
1. Включаем в конфиге многопользовательский режим. При этом все пользовательские приложения будут мэпиться на `~/ShinyApps`. 
2. Делаем линк (мягкая ссылка) разрабатываемого приложения в эту директорию. Общая форма команды `$ ln -s <SOURCE> <LINK_NAME>`
	- [Create a symbolic link relative to the current directory](https://unix.stackexchange.com/questions/84175/create-a-symbolic-link-relative-to-the-current-directory)
3. Меняем конфиг сервера и рестартуем.
4. Проверяем по путям 
	- `http://10.0.0.228:3838/` -- общая стартовая страница с приложениями
	- `http://10.0.0.228:3838/example1/` -- общее приложение по ссылке 
	- `http://ip:3838/users/ruser/iot/` -- частное приложение
	
Конфигурация выглядит следующим образом:
```
    # Instruct Shiny Server to run applications as the user ':HOME_USER:', where
    # possible (this username only takes effect in locations managed by
    # 'user_dirs'). In all other locations, we should fall back to the 'shiny' user.
    run_as :HOME_USER: shiny;
    
    # Specify the authentication method to be used.
    # Initially, a flat-file database stored at the path below.
    # auth_passwd_file /etc/shiny-server/passwd;
    
    # Log all Shiny output to files in this directory
    log_dir /var/log/shiny-server;
    
    # Define a server that listens on port 3838
    server {
      listen 3838;
    
      # Define a location at the base URL
      location / {
    
        # Host the directory of Shiny Apps stored in this directory
        site_dir /srv/shiny-server;
    
        # Log all Shiny output to files in this directory
        log_dir /var/log/shiny-server;
    
        # When a user visits the base URL rather than a particular application,
        # an index of the applications available in this directory will be shown.
        directory_index on;
      }
    
      # Define a location at the URL "/example1"
      location /example1 {
        app_dir /srv/shiny-server/sample-apps/hello;
      }
    
      # Define a location at the URL "/users"
      location /users {
        # Allow users to host their own apps in ~/ShinyApps
        user_dirs;
        
        # Optionally, you can restrict the privilege of hosting Shiny applications
        # only to members of a particular Linux group.
        # members_of shinyUsers;    
        
        # When a user visits the base URL rather than a particular application,
        # an index of the applications available in this directory will be shown.
        directory_index on;
      }
    
    }
```

for any user who is a member of the shinyUsers group, publicly host any Shiny application available in the user's ~/ShinyApps directory. For instance, if a user named tina who is a member of the shinyUsers group, has /home/tina as a home directory, and has an application called shinyApp1 in /home/tina/ShinyApps/, that application would be available on this server at the URL http://server.com/tina/shinyApp1. Any other application in /home/tina/ShinyApps/ would also be publically available at a similar URL.

## Настройка git на GitHub и на клиенте
- [Репозиторий кода](https://github.com/iMissile/agri-iot-code)
- [Репозиторий данных](https://github.com/iot-rus/agri-iot-data)

На машине-сборщике эти репозитории частично мапируются на директории scripts & data. В scripts делаем выгрузку скриптов, а в data делаем клон репозитория данных.
Детально смотрим статью ["Working with Git on Linux"](http://guides.beanstalkapp.com/version-control/git-on-linux.html)


### Multiple account
Для справки смотрим официцальный мануал ["Set Up Git"](https://help.github.com/articles/set-up-git/).

- [Multiple GitHub Accounts & SSH Config](http://stackoverflow.com/questions/3225862/multiple-github-accounts-ssh-config)
- [Multiple SSH Keys settings for different github account](https://gist.github.com/jexchan/2351996)
- [Could not open a connection to your authentication agent](http://stackoverflow.com/questions/17846529/could-not-open-a-connection-to-your-authentication-agent). You might need to start ssh-agent before you run the ssh-add command:
```
eval `ssh-agent -s`
ssh-add
```
- [Start ssh-agent on login](http://stackoverflow.com/questions/18880024/start-ssh-agent-on-login/18915067#18915067)


### Настройка прав на стороне клиента

`git commit` после инициализации репозитория и добавления файлов дает такое сообщение":

```
*** Please tell me who you are.

Run

	git config --global user.email "you@example.com"
	git config --global user.name "Your Name"

to set your account's default identity.
Omit --global to set the identity only in this repository.
```
Надо настроить git клиента для этого репозитория.

### Генерируем ключ для подключения к репозиториям
- Создаем пару открытый\закрытый ключ командой `ssh-keygen -t rsa`. Ключи размещаются в системной директории `/root/.ssh/id_rsa`
- Смотрим ключ командами `cd ~/.ssh/`, `cat id_rsa.pub`
- [Добавляем ключ в аккаунт GitHub\Adding a new SSH key to your GitHub account](https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/)
- Проверяем установку соединения: `ssh git@github.com`
- ВАЖНО!!!! При аутентификации через ssh необходимо писать правильную ссылку на репозиторий. **Не через HTTP, а через SSH**, ссылка должна выглядеть подобным образом: `git@github.com:iot-rus/agri-iot-data.git`

Если соединение не устанавливается (ошибка доступа), проходим процедуру лечения:
["Help, I keep getting a 'Permission Denied (publickey)' error when I push!"](https://gist.github.com/adamjohnson/5682757)

ВАЖНО!: репозиторий сломался, когда я его перевел с авторизации по HTTP на авторизацию по SSH. При этом надо лечить существующий клон репозитория. Ответ по смене ссылки репозитория читаем здесь: ["Changing a remote's URL"](https://help.github.com/articles/changing-a-remote-s-url/)

#### Генерация нескольких ключей
Для простых задач можно ограничиться одним ключом, но есть возможность для каждого хоста сделать свой RSA ключ.
Для этого надо сделать несколько отдельных ключей и прописать их в файле `$HOME/.ssh/config`:

```
Host mt-zoo-ubuntu01 mt-zoo-ubuntu01.media-tel.ru
   HostName mt-zoo-ubuntu01
   IdentityFile ~/.ssh/id_rsa
   User kirill

Host mt-zoo-kirill01 mt-zoo-kirill01.media-tel.ru
   HostName mt-zoo-kirill01
   IdentityFile ~/.ssh/id_rsa_2
   User kirill
```
### Устанавливаем поведение git push

Цитата:
*Отстал от жизни: GIT хочет непонятного (push, matching, simple, current, upstream) Попытался после годового перерыва попробовать запушить парочку изменений в свой давний проект (репозитарий на bitbucket.org).

А мне в ответ:*

```
WARNING: push.default is unset; its implicit value is changing in
Git 2.0 from 'matching' to 'simple'. To squelch this message
and maintain the current behavior after the default changes, use:

  git config --global push.default matching

To squelch this message and adopt the new behavior now, use:

  git config --global push.default simple

See 'git help config' and search for 'push.default' for further information.
(the 'simple' mode was introduced in Git 1.7.11. Use the similar mode
'current' instead of 'simple' if you sometimes use older versions of Git)

To git@bitbucket.org:***/***.git
 ! [rejected]        master -> master (non-fast-forward)

ERROR: failed to push some refs to 'git@bitbucket.org:***/***.git'
hint: Updates were rejected because a pushed branch tip is behind its remote
hint: counterpart. If you did not intend to push that branch, you may want to
hint: specify branches to push or set the 'push.default' configuration variable
hint: to 'simple', 'current' or 'upstream' to push only the current branch.
```

From git v1.7.11 release notes:

A new mode for push, "simple", which is a cross between "current"
and "upstream", has been introduced. "git push" without any refspec
will push the current branch out to the same name at the remote
repository only when it is set to track the branch with the same
name over there. The plan is to make this mode the new default
value when push.default is not configured.

Use new mode:

`git config --global push.default simple`

## Технические шаги
### Выгрузка репозитория погоды
Репозиторий данных ручками создали на GitHub. На машине-сборщике первоначальную инсталляцию делаем руками. В верхней директории запускаем команду `git clone https://github.com/iot-rus/agri-iot-data data`. Здесь мы принудительно меняем имя директории.

В принципе, надо делать пустные файлы данных сразу на GitHub. Тогда не придется их добавлять ручками на клиентской стороне. Но если не сделал, то можно это исправить командой `git add <name>` 

ВАЖНО!: репозиторий сломался, когда я его перевел с авторизации по HTTP на авторизацию по SSH. При этом надо лечить существующий клон репозитория. Ответ по смене ссылки репозитория читаем здесь: ["Changing a remote's URL"](https://help.github.com/articles/changing-a-remote-s-url/)


### Первоначальная выгрузка скриптов на linux машине
- Проверка установленной версии git командой `git version`
- Обновляем последние версии скриптов из репозитория. Существует несколько вариантов
	
**Вариант 1**. Используем средства GIT

[How to checkout only one file from git repository?](http://stackoverflow.com/questions/2466735/how-to-checkout-only-one-file-from-git-repository) 

Now we can! As this is the first result on google, I thought I'd update this to the latest standing. With the advent of git 1.7.9.5, we have the git archive command which will allow you to retrieve a single file from a remote host.

`git archive --remote=git://git.foo.com/project.git HEAD:path/to/directory filename | tar -x`

See answer in full here [http://stackoverflow.com/a/5324532/290784](http://stackoverflow.com/a/5324532/290784)
	
**Вариант 2**. Используем веб функционал для выгрузки.

For me `wget` to the raw url turned out to be the best and easiest way to download one particular file.

Open the file in the browser and click on "Raw" button. Now refresh your browser, copy the url and do a wget or curl on it.

`wget https://github.abc.abc.com/raw/abc/folder1/master/folder2/myfile.py?token=DDDDnkl92Kw8829jhXXoxBaVJIYW-h7zks5Vy9I-wA%3D%3D -O myfile.py`

This is the easiest solution, and works for any raw txt one could find. `curl https://example.com/raw.txt > savedFile.txt`

### Не забываем делать скрипты sh исполняемыми
- [Администратор в Ubuntu, или Что такое sudo](http://help.ubuntu.ru/wiki/%D1%81%D1%83%D0%BF%D0%B5%D1%80%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8C_%D0%B2_ubuntu).
- Отмечаем скрипт как исполняемый: `sudo chmod 777 путь_к_файлу` или `sudo chmod +x путь_к_файлу`.  
Чтобы запустить из командной строки, необходимо указывать полный путь: `/root/...` либо `./...`

- Следующий вопрос. Как получить в sh скрипте путь запуска скрипта? Суть в том, что данные он должен выкачивать в структуре, относительной своего расположения, а на разных машинах его размещение может меняться. Ответ смотрим здесь: [Handling positional parameters](http://wiki.bash-hackers.org/scripting/posparams). Но задача не так проста как кажется. Вот длинные дебаты: ["Getting the source directory of a Bash script from within"](http://stackoverflow.com/questions/59895/getting-the-source-directory-of-a-bash-script-from-within).
- После ответа на предыдущий вопрос натыкаемся на следующую задачу: развернуть '..' в композитном пути в полный путь. И опять начинаются дебаты и различные альтернативы. Смотрим, например, [How to convert “..” in path names to absolute name in a bash script?](http://stackoverflow.com/questions/6643853/how-to-convert-in-path-names-to-absolute-name-in-a-bash-script) или [Normalizing Path Names with Bash](http://www.linuxjournal.com/content/normalizing-path-names-bash)


### Детали по просмотру файловой структуры
Q: [How to list all the files in a tree (a directory and its subdirs)?](http://askubuntu.com/questions/15419/how-to-list-all-the-files-in-a-tree-a-directory-and-its-subdirs)  

Для просмотра древовидной структуры возможна масса вариантов.  
- `ls -alR`
- `sudo yum install tree` &  потом `tree filepath`

### Настройка cron

Параллельные вычисления в УрО РАН: [Запуск задач по расписанию - crond](http://parallel.uran.ru/node/394)

#### Редактирование личного расписания 

- `crontab file` – скопировать личное расписание из файла
- `crontab -e` – запуск редактора vi для правки расписания
- `crontab -l` – просмотреть расписание
- `crontab -r` – удалить расписание

Игорь предлагает стартовать от базового расписания, редактируем командой `vi /etc/crontab`

#### Отключаем отправку почтовых сообщений
По умолчанию cron отправляет почту после каждого задания. Это можно отключить.
- [Disable The Mail Alert By Crontab Command On a Linux or Unix-like Systems](https://www.cyberciti.biz/faq/disable-the-mail-alert-by-crontab-command/).
- [Stop Cron Daemon from Sending Email for Each Job](http://www.putorius.net/2015/03/stop-cron-daemon-from-sending-email-for.html). См. п.3 3. "Configure crond to send the script output to the system log, and disable sending mail of output".

You can configure crond by editing the /etc/sysconfig/crond file and changing the CRONDARGS line.  Adding the "-s" argument will send the output to the system log, and adding the "-m off" argument will disable crond from sending emails of the job output.

For example:

	[root@centos7 ~]# cat /etc/sysconfig/crond
	# Settings for the CRON daemon.
	# CRONDARGS= :  any extra command-line startup arguments for crond
	CRONDARGS=-s -m off

You will have to restart the crond service to read the new arguments:
`systemctl restart crond.service`

Итоговая команда: `*/10 * * * * root /root/scripts/weather.sh` НЕ РАБОТАЕТ. Ошибка в лог файлах
#### А где искать логи cron?
В части CentOS ответ был найден в ветке [Where to find the Crontab logs in CentOS](http://unix.stackexchange.com/questions/176229/where-to-find-the-crontab-logs-in-centos).

Cron logs on CentOS 6 are located in `/var/log/cron` by default. This only logs the execution of commands, not the results or exit statuses. The output of the executed command goes to the user's mail by default (root's mail in this case). An alternate email can be specified by the MAILTO variable inside of the crontab.

You should look at adjusting logrotate rules, instead of your custom cron, which already handles deletion of `/var/log/secure` logs.

#### Разбираемся с ошибкой /bin/bash: root: command not found в личном расписании
Читаем детальную статью ["Crontab error "/bin/sh: root: command not found"](http://rhosted.blogspot.ru/2010/04/crontab-error-binsh-root-command-not.html).
Там все очень подробно описано и разобрано. 
ПРАВИЛЬНАЯ итоговая команда: `*/10 * * * * /root/scripts/weather.sh`, в личном расписании не требуется указания имени пользователя.


# Настройка данных для использования R

Настройку git веду по подсказкам из ["Multiple GitHub Accounts & SSH Config"](http://stackoverflow.com/questions/3225862/multiple-github-accounts-ssh-config)

1. логинимся по ruser, все делаем от него.
2. Включаем в WinSCP отображение скрытых файлов (`Ctrl+Alt+H`)
3. создаем 2 ключа для GitHub: data и code. ~ надо принудительно раскрыть в `/home/user/`, иначе не генерируется
	- `ssh-keygen -t rsa -C "mail1@gmail.com"`,  `~/.ssh/id_rsa_data`.
	- `ssh-keygen -t rsa -C "mail2@gmail.com"`,  `~/.ssh/id_rsa_code`
4. Добавляем ключи в репозитории GitHub.
5. Прописываем созданные ключи в директории $HOME/.ssh/config`:
```
 # Data GitHub
Host github.com-data
    HostName github.com
    PreferredAuthentications publickey
    User git
    IdentityFile ~/.ssh/id_rsa_data

 # Code GitHub
Host github.com-code
    HostName github.com
    PreferredAuthentications publickey
    User git
    IdentityFile ~/.ssh/id_rsa_code
```
5. Запускаем ssh агента: `eval $(ssh-agent -s)`
6. Добавляем ключи и проверяем:
```
ssh-add ~/.ssh/id_rsa_data
ssh-add ~/.ssh/id_rsa_code
ssh-add -l
```
7. Проверяем корректность подключений
```
ssh -T git@github.com-code
ssh -T git@github.com-data
```
В случае успеха должно быть сообщение "Hi <USER>! You've successfully authenticated, but GitHub does not provide shell access."
9. создаем структуру директорий
	cd ~
	mkdir IoT
	cd ./IoT
10. Клонируем репозитории в директории IoT и модифицируем конфигурации
```
git clone git@github.com:iot-rus/agri-iot-data.git data
git clone git@github.com:iMissile/agri-iot-code.git code
```
для возможности коммитов устанавливаем дефолтовых пользователей этих директорий:
```
cd code
git config user.name "<NAME>"
git config user.email "<MAIL>@gmail.com"
cd data
git config user.name "<NAME>"
git config user.email "<MAIL>@gmail.com"
```
11. Проверяем конфигурации командой `git config -l`  
12. Смотрим настройки удаленного репозитория: `git remote -v`
13. Меняем настройки удаленного репозитория в соответствии с именами, указанными в  git config (иначе коммит не проходит, поскольку система не знает, какой ключ использовать).
```
code:
git remote set-url origin git@github.com-code:kuchaguangjie/pygtrans.git
data:
git remote set-url origin git@github.com-data:kuchaguangjie/pygtrans.git
```
13. Настраиваем исполнение скрипта в crone от лица ruser:
```
cd ~/IoT/code/cron-scripts/
sudo chmod +x ./request_weather.sh
crontab -e 
*/1 * * * * ~/IoT/code/cron-scripts/request_weather.sh
```
14. Рестартуем cron, проверяем исполнение задач cron по лог файлу: 
```
systemctl restart crond.service
cat /var/log/cron (под рутом)
 # или только строчки с коммитами
cat /var/log/cron | egrep  "file.? changed" 
```
15. Настроим новую модель поведения `git push`:
```
git config --global push.default matching
 # git config --global push.default simple
```

# Настройка RStudio Connect
## Деинсталляция RStsudio Server (free)
Информацию черпаем из статьи [Upgrading RStudio Server](https://support.rstudio.com/hc/en-us/articles/216079967-Upgrading-RStudio-Server):
- Удаляем текущую версию RStudio Server с помощью package manager: `sudo yum remove rstudio-server`.
Перед этим желательно перестроить старый кеш: `yum makecache fast`

## Обновление R
Под CentOS делаем следующей командой: `yum update R`. Детали найдены в статье [How do i update R on Cent OS?](http://superuser.com/questions/750440/how-do-i-update-r-on-cent-os)

## Инсталляция RStudio Connect
- [Страница для загрузки](https://www.rstudio.com/products/connect/download-commercial/) 45-ти дневной демо версии
`wget https://s3.amazonaws.com/rstudio-connect/centos6.3/x86_64/rstudio-connect-1.5.0-7-x86_64.rpm`
`wget https://s3.amazonaws.com/rstudio-connect/centos6.3/x86_64/rstudio-connect-1.5.4-1-x86_64.rpm`

- Проверяем созданных пользователей: `cat /etc/passwd`. Детальнее можно поглядеть, например, здесь: [Linux Command: List All Users In The System](https://www.cyberciti.biz/faq/linux-list-users-command/)
- Как дать права на запись для конкретного пользователя? `chown/chmod`. [Give user write access to folder {duplicate}](https://askubuntu.com/questions/402980/give-user-write-access-to-folder)
- Настраиваем почтовый адрес Connect. Секция `SenderEmail`, `vi /etc/rstudio-connect/rstudio-connect.gcfg` и перезапускаем
`sudo systemctl restart rstudio-connect`, `sudo systemctl status rstudio-connect`
- Запускаем `http://your-connect-server:3939/` и создаем аккаунт! [The first account will be marked as an RStudio Connect administrator.](http://docs.rstudio.com/connect/admin/getting-started.html#installation)
- Настраиваем параметры отправки почтовых сообщений в консоли в закладке [Email Settings](http://10.0.0.229:3939/connect/#/admin/settings):
В частности, настройки для отправки через [Yandex.почта](https://yandex.ru/support/mail-new/mail-clients.html#pop3)
- [Проверяем статус](https://support.rstudio.com/hc/en-us/articles/232221028-How-do-I-renew-my-RStudio-Connect-license-on-the-server-) демо лицензии:
```
$ sudo /opt/rstudio-connect/bin/license-manager status
$ sudo /opt/rstudio-connect/bin/license-manager status-offline
```
с версии 1.5.4 license manager глобально переписан и набор команд расширен. Список команд `sudo /opt/rstudio-connect/bin/license-manager`
Offline активация проводится по XML запросу на странице [RStudio Trial License Activation Form](http://apps.rstudio.com/trial-activation/)

- Подключаем RStudio IDE для публикации приложений. Приложения по умолчанию публикуются по такому пути: `/var/lib/rstudio-connect/apps/`
Лог файлы приложений, если таковые создаются, размещаются в соотв. версию публикации, например, `/var/lib/rstudio-connect/apps/9/51/app.log`.
Поискать можно такой командой: `: sudo find / -name 'app.log'`


### Проблема с публикацией
При компиляции выдает ошибку `Error in yaml::yaml.load(string, ...) : 
  Reader error: control characters are not allowed: #98 at 71`. И падает.

- Есть закрытый тикет на гитхабе: [Unable publish to RStudio Connect : Error in yaml::yaml.load(enc2utf8(string), ...) : Reader error: control characters are not allowed: #81 at 276 #115](https://github.com/rstudio/rsconnect/issues/115)
Он отсылает к проблеме в `packrat`: [Fall back to UTF-8 encoding on failure to determine format #329](https://github.com/rstudio/packrat/pull/329)


### Под капотом RStudio Connect
- [RStudio Connect: Admin Guide - RStudio Documentation in pdf](docs.rstudio.com/connect/admin/index.pdf)
- [5 Server Management](http://docs.rstudio.com/connect/1.4.2/admin/server-management.html). This section describes common administrative tasks for RStudio Connect.
	- `sudo systemctl restart rstudio-connect`
- [Where can I find the files created by RStudio Connect?](https://support.rstudio.com/hc/en-us/articles/227009188-Where-can-I-find-the-files-created-by-RStudio-Connect-). В частности, The RStudio Connect server log is located at `/var/log/rstudio-connect.log`. This file is owned by root with permissions 0600. Это же самое указано в документации, [4 Files & Directories](http://docs.rstudio.com/connect/admin/files-directories.html)
	- [A "live" view of a logfile on Linux](https://www.howtogeek.com/howto/ubuntu/a-live-view-of-a-logfile-on-linux/). Команда `tail -f /path/thefile.log`
- При попытке отправить отчет по Email (иконка Email Report) выдается ошибка `Error: Internal Server Error [500]`. Статья [How To Fix a 500 Internal Server Error ](https://www.lifewire.com/500-internal-server-error-explained-2622938): *The 500 Internal Server Error is a very general HTTP status code that means something has gone wrong on the website's server, but the server could not be more specific on what the exact problem is*. 
В конфиге Apache командой `tail -f /var/log/rstudio-connect.access.log` видим такую запись: `[17/Mar/2017:09:55:13 +0300] "POST /__api__/variants/4/sender?email=me HTTP/1.1" 500 0`
Проблема решилась установкой параметра `Server` в конфигурационном файле RStudio Connect: "The Server.SenderEmail property is the email address from which Connect sends emails. It is important that the sendmail or SMTP configuration RStudio Connect uses be willing and able to send email from this SenderEmail address. Otherwise, Connect will not be able to successfully send email. See Section 2.2.4 for more details about mail sending."
- При запуске без интернета в логах возникает ошибка:
`rsrv rserver-monitor[114033]: ERROR Error executing RRD command: [cd /var/lib/rstudio-connect/metrics/rrd] (Unexpected error for OK message: OK u:0,00 s:0,02...` 
RRD в Connect используется для мониторинга своего статуса: [14 Historical Metrics](http://docs.rstudio.com/connect/admin/metrics.html)
- Есть ощущение, что при публикации создаются манифесты для каждого пакета исходя из конфигурации пакетов, которые есть на машине разработчика.
В частности, поиск `grep -R www.stats.ox.ac.uk /var/lib/`
cat /var/lib/rstudio-connect/apps/2/8/manifest.json


### Обновление RStudio Connect
- [5.3 Upgrading](http://docs.rstudio.com/connect/admin/server-management.html#upgrading)
```The RStudio Connect version number is visible on the lefthand navigation pane. The latest version is available on the download page along with release notes.

To upgrade:
    Download the latest .rpm or .deb file
    Run the install command:
    Ubuntu:
    sudo gdebi <rstudio-connect-version.deb>
    Red Hat/CentOS:
    sudo yum install --nogpgcheck <rstudio-connect-version.rpm>

The new version of RStudio Connect will install on top of an earlier installation. Existing configuration settings are respected. During installation the RStudio Connect service is restarted. Total downtime is less than 10 minutes.```

Через удаление: [14 Purging RStudio Connect](http://docs.rstudio.com/connect/admin/purge.html)

После апдейта и Connect и R смотрим лог файл командой `tail -f /var/log/rstudio-connect.log` и видим ошибку:
`2017/04/03 13:45:34 Unable to locate an R installation: Unable to parse R version: ''`
Диагностика этой ошибки предлагается в статье ['Rstudio preview 99.1252 can't find R'](https://support.rstudio.com/hc/en-us/community/posts/211204788-Rstudio-preview-99-1252-can-t-find-R):
Удаление залоченных директорий: `rm -r mydir`

Can you confirm that R does print some output when attempting to call e.g.
`/tools/bioinfo/app/R-3.2.1/bin/R --slave --vanilla -e "R.home('home')"`
It seems like R is successfully being discovered, but RStudio is failing to call R and parse the associated version information.

Решение:
появилась новая надстройка в `/etc/rstudio-connect/rstudio-connect.gcfg` в секции `[Server]`, отвечающая за используемые версии R.
Детально см. главу [12 R](http://docs.rstudio.com/connect/admin/r.html#r) в руководстве администратора.
Добавляем сканирование установленных R и перезапускаем Connect.
```
[Server]
RVersionScanning = false
```


# Инсталляция LaTeX

- Centos 7 latex install
```
yum -y install texlive texlive-latex texlive-xetex
yum -y install texlive-collection-fontsrecommended
yum -y install texlive-collection-latex
yum -y install texlive-collection-latexrecommended
yum -y install texlive-xetex-def
yum -y install texlive-collection-xetex
Only if needed:
yum -y install texlive-collection-latexextra
```

или одной строчкой: `sudo yum install texlive texlive-latex texlive-xetex texlive-collection-fontsrecommended texlive-collection-latex texlive-collection-latexrecommended  texlive-xetex-def texlive-collection-xetex`
`
В документации RStudio Connect указано:
`texlive-full # very large dependency, but needed to render PDF documents from R Markdown`. Но такого пакета под CentOS не нашлось.

Ищем, где же установлен TexLive manager: `find / -name 'tl*'` А в CentOS его нет
[CentOS Latex - Install package manually (no tlmgr)](http://tex.stackexchange.com/questions/289404/centos-latex-install-package-manually-no-tlmgr)
Все делаем через `yum`. Поиск по репозиторию осуществляем с помощью [`yum search cyrillic`](https://www.centos.org/docs/5/html/yum/sn-searching-packages.html)

- Ставим `sudo yum -y install texlive-cyrillic texlive-collection-langcyrillic texlive-cyrillic-doc`

## Ошибки при запуске TeXLive
- [! LaTeX Error: File `titling.sty' not found. #115](https://github.com/rstudio/bookdown/issues/115)
- LaTeX Error: File 'framed.sty' not found. Решаем установкой [`sudo yum -y install texlive-framed`](https://github.com/rstudio/rmarkdown/issues/39)
- LaTeX Error: File 'titling.sty' not found. Решаем установкой `sudo yum -y install texlive-titling`

Русский язык в LaTeX:
- [Overleaf. Русский язык в LaTeX: XeLaTeX](https://www.overleaf.com/latex/templates/5-dot-2-2-russkii-iazyk-v-latex-xelatex/skfzmvgdgvnk)
- [XeLaTeX или на порядок улучшим качество шрифтов в окончательном pdf](http://astronu.jinr.ru/wiki/index.php/XeLaTeX_%D0%B8%D0%BB%D0%B8_%D0%BD%D0%B0_%D0%BF%D0%BE%D1%80%D1%8F%D0%B4%D0%BE%D0%BA_%D1%83%D0%BB%D1%83%D1%87%D1%88%D0%B8%D0%BC_%D0%BA%D0%B0%D1%87%D0%B5%D1%81%D1%82%D0%B2%D0%BE_%D1%88%D1%80%D0%B8%D1%84%D1%82%D0%BE%D0%B2_%D0%B2_%D0%BE%D0%BA%D0%BE%D0%BD%D1%87%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%D0%BC_pdf)
- Package fontenc Error: Encoding file 't2aenc.def' not found. Решаем установкой [`sudo yum -y install texlive-cyrillic`](http://tex.stackexchange.com/questions/5079/what-is-wrong-with-my-cyrillic-text)
 и `yum install texlive-collection-langcyrillic`
- Font T2A/cmr/m/n/12=larm1200 at 12.0pt not loadable: Metric (TFM) file not found. Ответы ищем в статье [Error in TeX Live – Font … not loadable: Metric (TFM) file not found](http://tex.stackexchange.com/questions/75166/error-in-tex-live-font-not-loadable-metric-tfm-file-not-found). Вариант решения -- ставим все font пакеты: `yum -y install texlive-*font*`
- [Переходим на XeTeX, получаем ошибку `! Corrupted NFSS tables`](http://tex.stackexchange.com/questions/237188/corrupted-nfss-tables)
- pdfLaTeX под Windows дает такую ошибку: ` pdfTeX error (font expansion): auto expansion is only possible with scalable fonts.`. Читаем длинную статью 
[On pdfTeX error (font expansion): auto expansion is only possible with scalable fonts, microtype package](http://tex.stackexchange.com/questions/283960/on-pdftex-error-font-expansion-auto-expansion-is-only-possible-with-scalable).
Есть подозрение, что виноват [в этом пакет `microtype`](http://tex.stackexchange.com/questions/10706/pdftex-error-font-expansion-auto-expansion-is-only-possible-with-scalable). Если его закомментировать в сгенерированном .tex файле, то компиляция проходит, но шрифт светлый и нет bold.
Надо ручками поставить пакет `cm-super`
- [How to set font to Arial throughout the entire document?](http://tex.stackexchange.com/questions/23957/how-to-set-font-to-arial-throughout-the-entire-document)
- COOL! Классный обзор методов. [Cyrillic in (La)TeX](http://tex.stackexchange.com/questions/816/cyrillic-in-latex)
РЕШЕНИЕ С Linux Libertine было найдено ЗДЕСЬ: [fontspec error: “font-not-found”](http://tex.stackexchange.com/questions/266101/fontspec-error-font-not-found).
Ставим `\setmainfont{Linux Libertine O}`, обнаружил с помощью команды `fc-list | grep "Linux Libertine" | grep ".otf"`.
- [Linux Libertine font](http://www.linuxlibertine.org/index.php?id=1&L=1).
	- Ставим под винду
	- Ставим под CentOS командой `sudo yum install linux-liber*`. Фонт найден установленным здесь: `/usr/share/fonts/linux-libertine/LinLibertine_*`
	- А еще есть пакет LaTeX [`libertine`](https://www.ctan.org/tex-archive/fonts/libertine/)
	- [Libertine Font problem with XeLaTeX](http://tex.stackexchange.com/questions/105970/font-problem-with-xelatex)

Инсталляция одной строчкой: `sudo yum install texlive-framed texlive-titling texlive-cyrillic texlive-*font* linux-liber*`



### Ставим полноценный TexLive

В конечном итоге все рекомендуют удалить штатный texlive и поставить ручками самому. [TeX Live - Quick install](https://www.tug.org/texlive/quickinstall.html)
[A different idea: Just uninstall all the TeXlive stuff coming from the repositories and install "the real stuff" instead](https://www.centos.org/forums/viewtopic.php?t=52472): https://www.tug.org/texlive/quickinstall.html

- Сносим пакеты, поставленные из репозитория CentOS: `yum remove texlive*`
- Чтобы не возникала ошибка Perl (`Can't locate Digest/MD5.pm in @INC...`), перед запуском инсталлятора необходимо доставить perl пакеты командой `yum install perl-Tk perl-Digest-MD5`. Детальнее читаем тут: [Error during installation of TeXLive 2012 in Fedora](https://tex.stackexchange.com/questions/100309/error-during-installation-of-texlive-2012-in-fedora)

- Инструкция по сетевой установке [здесь](Installing TeX Live over the Internet).
Скачиваем [сетевой инсталлятор](http://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz)
	- Скачиваем `wget http://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz`
	- Распаковываем `tar -xvzf install-tl-unx.tar.gz`
	- Запускаем исталлятор `./install-tl -gui text`
Проблема с инсталляцией R в том, что он тащит за собой texlive (dependencies)
```
Installing:
 R                             x86_64                 3.3.2-3.el7             epel                  27 k
Installing for dependencies:
 R-core                        x86_64                 3.3.2-3.el7             epel                  51 M
 R-core-devel                  x86_64                 3.3.2-3.el7             epel                 101 k
 R-devel   
```
- [10 Yum Exclude Examples to Skip Packages for Linux Yum Update (How to Yum Exclude Kernel Updates)](http://www.thegeekstuff.com/2014/11/yum-exclude-examples/)
LaTeX необходим R для сборки документации, как минимум. Пытаемся поставить без него командой `yum --skip-broken -x 'tex*' install R`
!!!!!
- [When removing Texlive, it also removes R. How to stop that?](https://www.centos.org/forums/viewtopic.php?t=57885)
- [How to remove everything related to TeX Live for fresh install on Ubuntu?](http://tex.stackexchange.com/questions/95483/how-to-remove-everything-related-to-tex-live-for-fresh-install-on-ubuntu)

# Elastic Stack (ELK)

Не забываем ставить время на машинах!
Как узнать время и дату через консоль: `date`
 - Устанавливаем (если не стоит): `yum install -y chrony`
 - Запускаем chrony и добавляем в автозагрузку: 
 	- `systemctl start chronyd`
 	- `systemctl enable chronyd`

## Интересные ресурсы в инете
- [driskell/log-courier](https://github.com/driskell/log-courier). Log Courier, a lightweight log shipper with Logstash integration.
- [Сбор и анализ логов демонов в Badoo](https://habrahabr.ru/company/badoo/blog/280606/)

## Elastic Search
- На [Docker Hub](https://hub.docker.com/_/elasticsearch/) ES более не доступен.
This image is officially deprecated in favor of the elasticsearch image provided by elastic.co which is available to pull via `docker.elastic.co/elasticsearch/elasticsearch:[version] like 5.2.1`. This image will receive no further updates after 2017-06-20 (June 20, 2017). Please adjust your usage accordingly.

- [Install Elasticsearch with Docker](https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html). Elasticsearch is also available as a Docker image. The image is built with X-Pack.

- Хорошие подробные статьи
	- ['Установка и настройка Elasticsearch в Ubuntu 16.04'](https://www.8host.com/blog/ustanovka-i-nastrojka-elasticsearch-v-ubuntu-16-04/)
	- [Установка и настройка Elasticsearch в CentOS 7](https://www.8host.com/blog/ustanovka-i-nastrojka-elasticsearch-v-centos-7/)
	- [Установка и настройка Elasticsearch+kibana+logstash+filebeat5](https://denisitpro.wordpress.com/2017/02/05/%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B0-elasticsearchkibanalogstashfilebeat5/comment-page-1/). При написании, я старался сразу делать более безопасную настройку ELK5, а не просто «оно включилось, значит работает»
	- [How To Gather Infrastructure Metrics with Packetbeat and ELK on Ubuntu 14.04](https://www.digitalocean.com/community/tutorials/how-to-gather-infrastructure-metrics-with-packetbeat-and-elk-on-ubuntu-14-04). Тут весьма подробненько разобрано
	- [How To Install Elasticsearch, Logstash, and Kibana (ELK Stack) on Ubuntu 14.0](https://www.digitalocean.com/community/tutorials/how-to-install-elasticsearch-logstash-and-kibana-elk-stack-on-ubuntu-14-04). Тут красивая картинка про потоки данных. Все линейно!

Берем инструкцию по дефолтной установке с сайта ES: [Install Elasticsearch with RPM](https://www.elastic.co/guide/en/elasticsearch/reference/5.0/rpm.html)

1. Ставим Java OpenJDK: (https://www.8host.com/blog/ustanovka-i-nastrojka-elasticsearch-v-centos-7/)
	- Для просмотра доступных в репозитории версий используем команду `yum search java-1.`
	- Устанавливаем OpenJDK: `sudo yum install java-1.8.0-openjdk.x86_64`
	- Проверяем, что установка JRE прошла успешно: `java -version`
2. Ставим ключ ES и репозиторий. Так лучше, потому что будет апдейтиться автоматически.
3. Командой `ps -p 1` выясняем как именно управляются сервисы в nix. В нашем случае этот `systemd`:
	- Смотрим пункт 'Running Elasticsearch with systemd'


### Настройка ES
И тут выясняется, что на 1 Гб Java запускаться не хочет. В статусе ES это отображается
```
# There is insufficient memory for the Java Runtime Environment to continue.
# Native memory allocation (mmap) failed to map 2060255232 bytes for committing reserved memory.
# Possible reasons:
#   The system is out of physical RAM or swap space
#   In 32 bit mode, the process size limit was hit
# Possible solutions:
#   Reduce memory load on the system
#   Increase physical memory or swap space
#   Check if swap backing store is full
#   Use 64 bit Java on a 64 bit OS
#   Decrease Java heap size (-Xmx/-Xms)
#   Decrease number of Java threads
#   Decrease Java thread stack sizes (-Xss)
#   Set larger code cache with -XX:ReservedCodeCacheSize=
```

- Урезаем требования ES по объему памяти:
	- идем в директорию `cd /etc/elasticsearch/`
	- в файле jvm.options меняем требования по памяти `Xms2g\Xmx2g` на `Xms512m\Xmx512m` соответственно

- Настраиваем фаервол. Разрешаем доступ к порту 22 отовсюду, к 9200 только с рабочего адреса.
Ставим `ufw`: yum install ufw
[Далее детали по настройке: 3. Защита Elasticsearch](https://www.8host.com/blog/ustanovka-i-nastrojka-elasticsearch-v-ubuntu-16-04/)
```
sudo ufw allow 22
sudo ufw allow from TRUSTED_IP to any port 9200
sudo ufw enable
sudo ufw status
```

IP=87.238.96.18: `sudo ufw allow from 87.238.96.18 to any port 9200`
IP=216.92.243.227: (www.elastichq.org)
sudo ufw allow from 216.92.243.227 to any port 9200
И открываем доступ к ES извне:
```
sudo nano /etc/elasticsearch/elasticsearch.yml
# Найдите строку network.bind_host, раскомментируйте её и измените её значение на 0.0.0.0:
. . .
network.host: 0.0.0.0
. . .
sudo systemctl restart elasticsearch
```

смотрим статус `systemctl status elasticsearch`

Проверяем: `http://89.223.29.108:9200/?pretty`, `http://89.223.29.108:9200/_nodes?pretty`

Меняем конфигурацию в файле `/etc/elasticsearch/elasticsearch.yml`

- Можно сменить адрес порта

- Мы предполагаем запускаться на одном сервере (я не нашел таких параметров).
Предположим, что у вас одна нода Elasticsearch; в таком случае лучше настроить один шард и 0 реплик. Таким образом, их значения будут выглядеть так (не забудьте удалить # в начале строки):
```
. . .
index.number_of_shards: 1
index.number_of_replicas: 0
. . .
```

### Выгрузка документов из ES
- [Dump all documents of Elasticsearch](https://stackoverflow.com/questions/19243074/dump-all-documents-of-elasticsearch)
- [Import and export tools for elasticsearch](https://github.com/taskrabbit/elasticsearch-dump)
- [taskrabbit/elasticsearch-dump. Import and export tools for elasticsearch](https://github.com/taskrabbit/elasticsearch-dump)
	- Ставим командой `yum install elasticdump`, предварительно гасим ES, а то ругается на нехватку памяти.
При этом при запуске команды из мануала
```
elasticdump \
  --input=http://localhost:9200/packetbeat-2017.05.02 \
  --output=/tmp/my_index.json \
  --type=data
```
сразу сталкиваемся с ошибкой:
```
Sun, 25 Sep 2016 13:07:15 GMT | Error Emitted => {"error":{"root_cause":[{"type":"parsing_exception","reason":"The field [fields] is no longer supported, please use [stored_fields] to retrieve stored fields or _source filtering if the field is not
```
На эту тему есть тикет [Support Elasticsearch 5 #259](https://github.com/taskrabbit/elasticsearch-dump/issues/259) в котором есть частное решение.
```
elasticdump \
  --input=http://localhost:9200/packetbeat-2017.05.02 \
  --output=/tmp/my_index.json \
  --type=data \
  --limit=1000 \
  --searchBody '{"query": { "match_all": {} }, "stored_fields": ["*"], "_source": true }'
```
- Чтобы забрать архив. [Архивирование файлов в Linux](https://losst.ru/arhivatsiya-v-linux). Архив != сжатие.
	- Упаковка файла: `$ tar -cvf archive.tar.gz /path/to/files`
	- А чтобы распаковать архив tar linux: `$ tar -xvf archive.tar.gz`
	- посмотреть кусочек файла: [View the Beginning of Text Files with head](https://www.linode.com/docs/tools-reference/tools/view-the-beginning-of-text-files-with-head)

### ES GUI
- [Elastic HQ](http://www.elastichq.org/). Sleek, intuitive, and powerful ElasticSearch Management and Monitoring.
У меня папка плагинов ES 5.x (для инсталляции на системе) лежит здесь: `/usr/share/elasticsearch/plugins
Пытаемся запустить командой `./elasticsearch-plugin install royrusso/elasticsearch-HQ`
`

### Игры с Elasticsearch
- [Основы Elasticsearch](https://habrahabr.ru/post/280488/)

## Установка и настройка Packetbeat
- [Download Packetbeat](https://www.elastic.co/downloads/beats/packetbeat). Лучше, если настроим репозиторий
Packetbeat can also be installed from our package repositories using apt or yum. See [Repositories in the Guide](https://www.elastic.co/guide/en/beats/packetbeat/current/setup-repositories.html).
Смотрим пошаговую инструкцию в разделе YUM.
- Погружаемся в настройку [Getting Started With Packetbeat](https://www.elastic.co/guide/en/beats/packetbeat/current/packetbeat-getting-started.html)

### Настройка конфиг файла PB
Файл расположен тут -- `/etc/packetbeat/packetbeat.yml`
Пример полных настроек лежит тут: `/etc/packetbeat/packetbeat.full.yml`
Смотрим сетевые интерфейсы следюущими командами, см ['How can I find available network interfaces?'](https://unix.stackexchange.com/questions/125400/how-can-i-find-available-network-interfaces):
```
ifconfig -a # The simplest method I know to list all of your interfaces is
ip link show # If you're on a system where that has been made obsolete, you can use
```
- Важно настроить параметры сбора с сетевого интерфейса. См. ['Sniffing options'](https://www.elastic.co/guide/en/beats/packetbeat/current/configuration-interfaces.html)
!!! Note. When you specify **any** for the device, the interfaces are **not set** to promiscuous mode.

[FAQ: Packetbeat doesn’t see any packets when using mirror ports?](https://www.elastic.co/guide/en/beats/packetbeat/current/faq.html)


Меняем настройки в секции `General`
```
name: PB-Lab
# tags: ["service-X", "web-tier"]
tags: ["experimental"]
output.elasticsearch:
  # Array of hosts to connect to.
  hosts: ["89.223.29.108:9200"]
logging.level: warning
```
И рестартуем Packetbeat: `sudo systemctl restart packetbeat` (`sudo service packetbeat restart` -- так было в убунте)

Шаблоны парсинга packetbeat лежат в `/etc/packetbeat/packetbeat.template.json`

### Тонкая настройка протоколов
- [Is it possible to see HTTP POST data from requests in Packetbeat?](https://stackoverflow.com/questions/39144057/is-it-possible-to-see-http-post-data-from-requests-in-packetbeat). You must also specify the content types of the requests that you wish to include the body for via the `include_body_for` config setting.


Теперь на сервере ELK 
- почистим предыдущие записи
`curl -XDELETE 'http://localhost:9200/packetbeat-*'`
- и проверим поступление данных: `http://89.223.29.108:9200/packetbeat-*/_search?pretty`

## Установка и настройка Kibana
Идем по мануалу с официального сайта, делаем по ветке [Установка через репозиторий](https://www.elastic.co/guide/en/kibana/current/rpm.html)
Создаем `kibana.repo` на машине с packetbeat.
Скачиваем, устанавливаем и включаем автоматический запуск.
`
sudo /bin/systemctl daemon-reload
sudo /bin/systemctl enable kibana.service
`

### Конфигурируем Kibana
Настройки лежат в файле `/etc/kibana/kibana.yml`

В сконфигурированной системе можно заменить `server.host`: In the Kibana configuration file, find the line that specifies server.host, and replace the IP address ("0.0.0.0" by default) with "localhost"
```
server.host: 10.0.0.232
server.name: "Kibana-Lab"
elasticsearch.url: "http://89.223.29.108:9200"
```

Запускаем: `http://10.0.0.232:5601`, пытаемся поиграть с фильтрами: [Kibana Queries and Filters](https://www.elastic.co/guide/en/beats/packetbeat/current/kibana-queries-filters.html)

- Непонятная ситуация.
Строку `10.0.0.232` ищет, строку `source.ip:"10.0.0.178"` ищет, а `source.ip:"10.0.0.232"` -- нет.
А!!! был еще фильтр, которые я из Available Fields наделал.

# ClickHouse


## Инсталляция
IP: 10.0.0.234
- Инструкцию по установке берем с официального сайта: [Начало работы](https://clickhouse.yandex/docs/ru/getting_started.html).
- Обновление пакетов в Ubuntu: `sudo apt-get update`
- [Ubuntu version history](https://en.wikipedia.org/wiki/Ubuntu_version_history)
	-  Ubuntu 16.04 LTS (Xenial Xerus)
	-  Ubuntu 14.04 LTS (Trusty Tahr)
- Прописали репозиторий: `deb http://repo.yandex.ru/clickhouse/xenial stable main`
- Смотрим по вопросам FAQ: [FAQ по ClickHouse (на русском)](https://github.com/hatarist/clickhouse-faq/wiki/Russian)
	- [Как открыть доступ к серверу по сети?](https://github.com/hatarist/clickhouse-faq/wiki/Russian). Добавить/изменить в `clickhouse-server/config.xml` тег `<listen_host>,` например:
```
<listen_host>10.55.33.77</listen_host>
```
Можно раскомментировать имеющуюся там запись с ::, в таком случае ClickHouse будет доступен по всем IPv4/IPv6-адресам сервера:
```
<listen_host>::</listen_host>
```

- Ставим на Win машину ODBC клиент [yandex/clickhouse-odbc](https://github.com/yandex/clickhouse-odbc/releases)
- Тестовые данные, упоминаемые в процессе установки [ClickHouse/doc/example_datasets/](https://github.com/yandex/ClickHouse/tree/master/doc/example_datasets)
- [Яндекс открывает ClickHouse](https://habrahabr.ru/company/yandex/blog/303282/). Тут есть про старт с данными.
- [ClickHouse/doc/getting_started/getting_started_ru.md](https://github.com/yandex/ClickHouse/blob/master/doc/getting_started/getting_started_ru.md)

- Проверяем под Win настройки ODBC клиентов: [Check the ODBC SQL Server Driver Version (Windows)](https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/check-the-odbc-sql-server-driver-version-windows), [Open the ODBC Data Source Administrator](https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/open-the-odbc-data-source-administrator). "To open the ODBC Data Source Administrator in Windows 10  On the Start page, type ODBC Data Sources. The ODBC Data Sources Destop App should appear as a choice." **Выбираем 32 или 64 в зависимости от установленного драйвера.
- Смотрим статью по подключению R через ODBC: [Databases using R](https://rviews.rstudio.com/2017/05/17/databases-using-r/)
- Пакет `DBI`: [DBI](http://rstats-db.github.io/DBI/)
- [R with Teradata ODBC](https://downloads.teradata.com/blog/odbcteam/2016/02/r-with-teradata-odbc)
- [Complete Guide to R for DataDirect ODBC/JDBC](https://www.progress.com/blogs/complete-guide-to-r-for-datadirect-odbc-jdbc)
- [Connect to ODBC databases (using the DBI interface)](https://github.com/rstats-db/odbc)
- [clickhouse: DBI database connector for external clickhouse databases](https://rdrr.io/github/hannesmuehleisen/clickhouse-r/man/clickhouse.html)
	- [Rstats client for ClickHouse (https://clickhouse.yandex)](https://github.com/hannesmuehleisen/clickhouse-r)


## Запуск

Используем tabbix.io: (не взлетел) 
http://10.0.0.234:8123

## Tutorial
- [ClickHouse Tutorial](https://clickhouse.yandex/tutorial.html)

## Разбираемся с `hannesmuehleisen/clickhouse-r`
- При штатном запуске выдает ошибку 
```
> d <- dbReadTable(con, "mtcars")
Note: method with signature ‘DBIConnection#character’ chosen for function ‘dbReadTable’,
 target signature ‘clickhouse_connection#character’.
 "clickhouse_connection#ANY" would also be valid
Error in .local(conn, statement, ...) : 
  Code: 62, e.displayText() = DB::Exception: Syntax error: failed at position 15: "mtcars" FORMAT TabSeparatedWithNames, expected identifier, e.what() = DB::Exception
```
Эта ошибка возникает в методе `setMethod("dbSendQuery", "clickhouse_connection", function(conn, statement, use = c("memory", "temp"), ...) {`
Почему рушится именно здесь и не реагирует на browser внутри dbReadTable не до конца понятно.
```
setMethod("dbReadTable", "clickhouse_connection", function(conn, name, ...) {
  browser()
	dbGetQuery(conn, paste0("SELECT * FROM ", name))
})
```
- Судя по стеку, сначала вызывается метод dbIsValid, который делает запрос `"select 1"`.
- Происходит это в `64 stopifnot(dbIsValid(con))` метода `dbConnect()`!
- Сделав дебаг видим, что `dbReadTable(con, "mtcars")` трансформируется в `"SELECT * FROM \"mtcars\""`
- Это происходит в строчке `sql_name <- dbQuoteIdentifier(conn, x = name, ...)`. `"mtcars"` превращается в `"\"mtcars\"". Исходник функции ищем на [github](https://github.com/rstats-db/odbc/search?utf8=%E2%9C%93&q=dbQuoteIdentifier&type=). 
В районе [148 строки](https://github.com/rstats-db/odbc/blob/e061c61da7dcec2fe6bb25592b822224e8caa5bc/R/Connection.R):
```
setMethod(
  "dbQuoteIdentifier", c("OdbcConnection", "character"),
  function(conn, x, ...) {
    if (nzchar(conn@quote)) {
      x <- gsub(conn@quote, paste0(conn@quote, conn@quote), x, fixed = TRUE)
    }
    DBI::SQL(paste(conn@quote, encodeString(x), conn@quote, sep = ""))
  })
```
читаем в хелпе про `nzchar()`

- При инициализации dbConnect выдается такое сообщение
```
Note: method with signature ‘DBIConnection#character’ chosen for function ‘dbReadTable’,
 target signature ‘clickhouse_connection#character’.
 "clickhouse_connection#ANY" would also be valid
```
- в DBI::Connect.R есть определение класса:
```
setClass(
  "OdbcConnection",
  contains = "DBIConnection",
  slots = list(
    ptr = "externalptr",
    quote = "character",
    info = "ANY"
  )
)
```
- нашел похожую ошибку: [dbWriteTable does not work for tbl_df](https://github.com/rstats-db/DBI/issues/92)

# PostgreSQL
## Подключение
развернутый инстанс:
```
пользователь sudo -u postgres -i
psql
\connect channel_list
\dt
\d+ tv_list -- посмотреть определение таблицы
\q -- выход из отображения select
\l -- посмотерть кодировки текстовых данных в таблицах
```

# Установка экосистемы R в оффлайн режиме

Стартовая конфигурация:
1. Все пакеты CentOS установлены.
2. RStudio Connect скачан.
3. miniCRAN размещен в директории `~/miniCRAN`
4. Запускаем под пользователем root консоль `sudo -i`
5. Переходим в домашнюю директорию пользователя `cd /home/ruser`
6. Переносим репозиторий в `/opt`: `mv /home/ruser/miniCRAN /opt/`. Если не получается перезаписать репозиторий, просто его предварительно удаляем командой `sudo rm -r /opt/miniCRAN/`
7. Скачиваем пакет [ICU](https://raw.githubusercontent.com/gagolews/stringi/master/src/icu55/data/icudt55l.zip), требуемый для сборки `stringi` (конкретный адрес будет виден в сообщениях об ошибке при сборке stringi.
Инсталлируем командой `install.packages("stringi", configure.vars="ICUDT_DIR=/tmp/")`, положив перед этим в `/tmp` файл `icudt55l.zip`
- Для Connect пробуем следующий ход:
1. Скачать и положить `icudt55l.zip` (а может из zip тоже).
2. Исправляем в `/usr/lib64/R/etc/Renviron`:
```
# manual ICUDT
ICUDT_DIR=/opt/icu55/data
# --------------------

1. Заходим в R `sudo -i R`, проверяем пути расположения библиотек `.libPaths()`. 
2. Важное замечание: для сборки документации потребуется Rmarkdown
3. Запускаем последовательность команд для установки пакетов из локального репозитория:
pkgs_needed <- c("packrat")
local_repo  <- "/opt/miniCRAN"
# OPTIONAL: If you are not running R from the instance library as recommended, you must specify the path
#   .libPaths()[1] 
# lib <- .libPaths()[1]

install.packages(pkgs_needed, repos = file.path("file://", normalizePath(local_repo, winslash = "/")), dependencies = TRUE)

install.packages(pkgs_needed,
		 repos = file.path("file://", normalizePath(local_repo, winslash = "/")),
		 # repos = file.path(local_repo),
                 # lib = lib,
                 # type = "win.binary",
		 # type = "source",
                 dependencies = TRUE
                 )
installed.packages() 
3. Изменяем глобальные настройки репозитория, необходимо для работы Connect, который ставится из под рута.
Где эти настройки живут в *nix -- надо уточнять. Возможно, здесь: `cat /usr/lib64/R/etc/Renviron`
```
packrat::repos_add(miniCRAN = "file:///opt/miniCRAN")
packrat::repos_remove('CRAN')
# проверим
getOption("repos")
```
В файле `/usr/lib64/R/etc/repositories` прописаны репозитории в которые ходит R.
Поиск по файлам: `grep -R www.stats.ox.ac.uk /var/lib/`
4. После этого можно ставить пакеты с помощью штатного `install.packages()`
```
# "stringi" надо собирать вручную 
pkgs_needed <- c("knitr", "rmarkdown", "rsconnect", "packrat",
                 "tidyverse", "readxl", "magrittr", "hrbrthemes", "Cairo",
                 "shiny", "shinythemes", "shinyBS", "shinyjs", "config", "DBI", "RODBC", "RPostgreSQL",
                 "tictoc", "anytime", "fasttime", "futile.logger", "iterators", "foreach", "doParallel")
install.packages(pkgs_needed)
```
5. Создадим админа по умолчанию: http://10.0.0.183:3939 radmin:radmin, внешняя почта
6. При создании нового аккаунта в IDE указываем адрес сервера с портом.
7. Посмотрим лог сервера. The RStudio Connect server log is located at `/var/log/rstudio-connect.log`. This file is owned by root with permissions 0600.
8. Актуализируем настройки коннекта с Java командой `sudo R CMD javareconf`.
9. Местоположение и назначение логов Connect описаны в [4 Files & Directories](http://docs.rstudio.com/connect/1.4.0/admin/files-directories.html)

# Изменение переменных окружения для скриптов
- Изменение переменных окружения на сервере linux
```
vi /etc/environment
R_CONFIG_ACTIVE=media-tel
source /etc/environment
echo $R_CONFIG_ACTIVE
sudo systemctl restart rstudio-connect
```
- Управление конфигурационными файлами в пакете `config`: [Configurations](https://github.com/rstudio/config)
You can specify which configuration is currently active by setting the `R_CONFIG_ACTIVE` environment variable. The `R_CONFIG_ACTIVE` variable is typically set within a site-wide `Renviron` or `Rprofile` (see R Startup for details on these files).
- В случае с RStudio Connect `R_CONFIG_ACTIVE` задается в файле `find / -type f -name Rprofile`, файл находится здесь: `/usr/lib64/R/library/base/R/Rprofile`
`find / -type f -name Renviron`, файл найден здесь: `/usr/lib64/R/etc/Renviron`
- RStudio Connect переопределяет значение `R_CONFIG_ACTIVE`. Место найдено путем поиска по файлам из директории `cd /opt/rstudio-connect/`.
Запускаем команду `grep -R R_CONFIG_ACTIVE *`
Ответ находим в мануале RStudio Connect: [12.8 Using the config Package](http://docs.rstudio.com/connect/admin/process-management.html#using-the-config-package)
```
The config package makes it easy to manage environment specific configuration values in R code. For example, you might want to use one value for a variable locally, and another value when deployed on RStudio Connect. The package vignette contains more information.

The desired configuration is identified to the config package by the R_CONFIG_ACTIVE environment variable. By default, R processes launched by RStudio Connect set R_CONFIG_ACTIVE to rsconnect. The value can be changed by modifying the Applications.RConfigActive configuration setting. Note that the value of R_CONFIG_ACTIVE is not available during package installation.
```
Меняем значение параметра `Applications.RConfigActive` в файле `/etc/rstudio-connect/rstudio-connect.gcfg`:
```
[Applications]
RConfigActive = media-tel
```

## Автономная работа R
- Инструкция от Микрософт. [Create a Local Package Repository Using miniCRAN](https://docs.microsoft.com/en-us/sql/advanced-analytics/r/create-a-local-package-repository-using-minicran)
- [How to install R packages on an off-line SQL Server 2016 instance](http://blog.revolutionanalytics.com/2016/05/minicran-sql-server.html)
- R Startup
	- [R for Enterprise: Understanding R’s Startup](https://rviews.rstudio.com/2017/04/19/r-for-enterprise-understanding-r-s-startup/)
	- [Rprofile — кастомизируем рабочее окружение](http://aakinshin.net/ru/blog/post/r-rprofile/)
	- [Efficient R programming. R startup](https://csgillespie.github.io/efficientR/3-3-r-startup.html#r-startup)
	- [Fun with .Rprofile and customizing R startup](http://www.onthelambda.com/2014/09/17/fun-with-rprofile-and-customizing-r-startup/)
	- [locate the “.Rprofile” file generating default options](https://stackoverflow.com/questions/13735745/locate-the-rprofile-file-generating-default-options)
```
You could run the following to list existing files on your system among those listed on the page:

candidates <- c( Sys.getenv("R_PROFILE"),
                 file.path(Sys.getenv("R_HOME"), "etc", "Rprofile.site"),
                 Sys.getenv("R_PROFILE_USER"),
                 file.path(getwd(), ".Rprofile") )
```
- [R Installation and Administration. 6.6 Setting up a package repository](https://cran.r-project.org/doc/manuals/R-admin.html#Setting-up-a-package-repository)
- local CRAN-like repository
	- [Using miniCRAN to create a local CRAN repository](https://cran.r-project.org/web/packages/miniCRAN/vignettes/miniCRAN-introduction.html)
	- [Using repositories other than CRAN with miniCRAN](https://cran.r-project.org/web/packages/miniCRAN/vignettes/miniCRAN-non-CRAN-repos.html)
	- [How to Set Up a Custom CRAN-like Repository](https://rstudio.github.io/packrat/custom-repos.html)
	- Пакет для выбора репозиториев: [setRepositories {utils}](https://stat.ethz.ch/R-manual/R-devel/library/utils/html/setRepositories.html)
- [RStudio Connect. Package Management. 13.2 Private Repositories](http://docs.rstudio.com/connect/admin/index.pdf#page42)
	- [Process management in RStudio Connect](https://support.rstudio.com/hc/en-us/articles/226871847-Process-management-in-RStudio-Connect)
	- [Для последней версии Connect](http://docs.rstudio.com/connect/admin/package-management.html)
	- [Deploying connect app with private repository](https://support.rstudio.com/hc/en-us/community/posts/115001095768-Deploying-connect-app-with-private-repository)
	- [Package management in RStudio Connect](https://support.rstudio.com/hc/en-us/articles/226871467-Package-management-in-RStudio-Connect)
	- [Package Management for Offline RStudio Connect Installations](https://support.rstudio.com/hc/en-us/articles/115006298728-Package-Management-for-Offline-RStudio-Connect-Installations)
	- [R not reading Rprofile.site at startup](https://superuser.com/questions/891127/r-not-reading-rprofile-site-at-startup). Смотрим из консоли командой `R RHOME`
`/usr/lib64/R/library/base/R/Rprofile` -- system Rprofile
	- [Problem Installing Packages](https://support.rstudio.com/hc/en-us/articles/200554786-Problem-Installing-Packages)


- [How to select a CRAN mirror in R](https://stackoverflow.com/questions/11488174/how-to-select-a-cran-mirror-in-r)
- [Installing packages without the internet](https://www.mango-solutions.com/blog/installing-packages-without-the-internet)
- [How to Set Up a Custom CRAN-like Repository](https://rstudio.github.io/packrat/custom-repos.html)
Andrie de Vries and Alex Chubaty
July 12, 2016
- [devtools](https://cran.r-project.org/web/packages/devtools/README.html)
Возникают вопросы о том, откуда взять и как записать SHA в DESCRIPTION. Похожий вопрос на SoF: 
 - [Programmatically set fields in DESCRIPTION file for R package](https://stackoverflow.com/questions/44871619/programmatically-set-fields-in-description-file-for-r-package)
- Как посмотреть commit hash в консоли? [How to retrieve the hash for the current commit in Git?](https://stackoverflow.com/questions/949314/how-to-retrieve-the-hash-for-the-current-commit-in-git)
```

To get the full SHA:
$ git rev-parse HEAD
cbf1b9a1be984a9f61b79a05f23b19f66d533537
To get the shortened version:
$ git rev-parse --short HEAD
cbf1b9a
```
Или так
```
Commit hash
git show -s --format=%H
Abbreviated commit hash
git show -s --format=%h
Click here for more git show examples.
```

Что надо делать с пользовательскими пакетами? 
1. на клиентской машине ставим пакет из репозитория с помощью `devtools::install_github()`.
2. devtools прописывает в DESCRIPTION установленного пакета SHA, берем его и используем для [переименования исходников пакета](https://support.rstudio.com/hc/en-us/articles/226871467-Package-management-in-RStudio-Connect).
3. Помещаем этот файл в соотв. ветку в `Server.SourcePackageDir`. Подробно про этот параметр читаем здесь: [A Configuration Options](http://docs.rstudio.com/connect/admin/appendix-configuration.html). Папку для пакетов необходимо создать, иначе Connect не стартует.

Распаковали пакет
tar zxvf 42c592db2eaec99492cff6dc22e6b4df37776472.tar.gz 
Зашли внутрь и пересобрали
cd /<внутрь>
tar zcvf ../42c592db2eaec99492cff6dc22e6b4df37776472.tar.gz *
Посмотрели содержимое
tar ztvf 42c592db2eaec99492cff6dc22e6b4df37776472.tar.gz
Удалили содержание (всю директорию)
rm -rf <dir>
Работаем с .tar.gz в Windows: [IZArc is the easiest way to Zip, Unzip and Encrypt files for free](http://www.izarc.org/)


# ================= Управление правами доступа при мапировании папок, советы от Кирилла ====================
один из вариантов -
сделать sudo chmod -R o+rx /home/another_user_you_want_to_access

мой вариант должен работать.
но если таких случаев будет >1, то можно создать группу и добавить всех пользователей кому нужен доступ к домашним каталогам других в группе в это группу.
На каталого пользователей дать доступ на rx для группы.

т.к. так
groupadd statisticians
usermod -a -G statisticians stat_user1
usermod -a -G statisticians stat_user2

chown -R :statisticians /srv/shiny-server
chown -R :statisticians /home/stat_user1
chown -R :statisticians /home/stat_user2
теперь пользователи группы могу писать в /srv/shiny-server поскольку и они и /srv/shiny-server в одной группе.
пользователям надо перелогиниться если они в shell-е сейчас.