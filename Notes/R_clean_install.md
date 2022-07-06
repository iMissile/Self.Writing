# Установка R на CentOS 7.x
## подключаем репозитории
sudo yum update
sudo yum -y install chrony
systemctl start chronyd
systemctl enable chronyd
systemctl status chronyd

sudo yum -y install epel-release
uname -a

## ставим R
sudo yum -y install wget epel-release chrony tree ncdu glances
sudo yum -y install R

## ставим доп либы, необходимые для пакетов R
sudo yum -y groupinstall X11
sudo yum -y groupinstall "Development Tools"

sudo yum -y install wget libcurl-devel openssl-devel cyrus-sasl-devel libxml2-devel libpng-devel libjpeg-devel python python-devel proj proj-devel mesa-libGL mesa-libGL-devel mesa-libGLU mesa-libGLU-devel gmp-devel mpfr-devel cairo-devel libXt-devel gtk2-devel v8-devel udunits2 udunits2-devel xorg-x11-server-Xvfb unixODBC* postgresql-devel mariadb-devel mysql-devel gcc-gfortran* texlive*, ufw, dejavu*, psmisc, rrdtool, wireshark, lrzsz

sudo yum -y install dejavu-fonts-common dejavu-sans-mono-fonts rrdtool psmisc lrzsz gdal* proj-devel proj-epsg proj-nad protobuf-devel geos-devel

Установку пакетов будем делать из командной строки, поэтому сразу накатим хелпер
sudo yum -y install R-littler R-littler-examples

## ставим все, что касается LaTeX
sudo yum -y install texlive texlive-latex texlive-xetex texlive-collection-fontsrecommended texlive-collection-latex texlive-collection-latexrecommended  texlive-xetex-def texlive-collection-xetex
Добавляем поддержку кириллицы
sudo yum -y install texlive-cyrillic texlive-collection-langcyrillic texlive-cyrillic-doc texlive-framed texlive-titling texlive-*font* linux-liber*

## обновляем пакеты в R
sudo -i R
update.packages(ask=FALSE)

- Как поставить пакеты в R, если есть проблемы с https сертификатами. Выдает ошибку:
```
Warning messages:
1: In download.file(url, destfile = f, quiet = TRUE) :
 URL 'https://cran.r-project.org/CRAN_mirrors.csv': status was 'Peer certificate cannot be authenticated with given CA certificates'
2: package ‘httr’ is not available (for R version 3.4.4) 
```
решил вопрос путем обхода секьюрности флагами: `install.packages("httr", method="wget", extra="--no-check-certificate")`

При установке пакетов под root (для всех) запускаем R от рута `sudo -i R` и прогоняему установку
================== В консоли R
После установки библиотек ищем расположение h файлов следующей командой `find . -type f -name udunits2.h` и запускаем инсталляцию с параметрами:
install.packages("udunits2", configure.args='--with-udunits2-include=/usr/include/udunits2/')

chooseCRANmirror(graphics=FALSE, ind=37)
pacman::p_load("gWidgetstcltk")


# Offfline Инсталляция
## Создаем репозиторий miniCRAN
- Используем пакет miniCRAN для инициализации репозитория. 
Считаем, что локальная директория /opt/miniCRAN уже создана.
```
library("miniCRAN")
tags <- c("tidyverse", "lubridate", "glue", "scales", "forcats", "readxl", "magrittr", "stringi", "stringr", 
          "futile.logger", "jsonlite", "Cairo", "RColorBrewer", "extrafont", "hrbrthemes", "DBI", "RPostgreSQL", 
          "config", "shiny", "shinyjqui", "shinythemes", "shinyBS", "shinyjs", "shinyWidgets", "shinycssloaders", 
          "formattable", "anytime", "tictoc", "digest", "officer", "openxlsx", "assertr", "checkmate")
pkgList <- pkgDep(tags, suggests=TRUE, enhances=FALSE)
makeRepo(pkgList, path="d:/temp/miniCRAN", repos="https://cloud.r-project.org/", type=c("source"))
```

## Установка собственных пакетов с Github
1. Скачали единым zip файлом https://github.com/iMissile/dvtdspack
2. Ставим с локального файла: `devtools::install_local(path="C:/Users/Ilya/Downloads/dvtdspack-master.zip")`. Если просто выкачивать zip с гитхаба, то инсталляция не получится, zip файл содержит файлы пакета внутри папки. 

Команда `install.packages("C:/Users/Ilya/Downloads/dvtdspack-master.zip", repos=NULL)` работает криво и просто гонит содержимое zip в библиотеку, без компиляции и без переименования (остается тэг `-master`)


# Установка продуктов RStudio

## Установка RStudio Server
- [Страница инсталляции стабильной версии](https://www.rstudio.com/products/rstudio/download-server/)
- [Preview релизы](https://www.rstudio.com/products/rstudio/download/preview/)

Не забыть завести отдельного пользователя с uid > 100 !:
`sudo useradd <username>`
`sudo passwd <username>`

!!! Важно, на Ubuntu есть специфика

## Установка RStudio Shiny Server free
[Страница загрузки](https://www.rstudio.com/products/shiny/download-server/)
Для удобства работы оставим однопользовательский режим работы Shiny Server, делаем мапирование домашних директорий R пользователей на `/srv/shiny-server` командой `ln -s <SOURCE> <LINK_NAME>`:
`sudo ln -s /home/ruser/R/<app> /srv/shiny-server/<app>`

Запуск скрипта из консоли linux: `R < script.R --no-save`. Выводит все на экран, можно поглядеть ошибки

## Установка RStudio Connect
1. Заходим на страницу загрузки https://www.rstudio.com/products/connect/download-commercial/
2. Проверяем срок демо лицензии: 
sudo /opt/rstudio-connect/bin/license-manager status-offline


================== Web Доступ
Shiny Server
- `http://10.0.0.239:3939/` -- общая стартовая страница с приложениями
RStudio Server
- `http://<server-ip>:8787`


# Установка R на Ubuntu 18.x LTS ====== Инсталляция под UBUNTU ========

- [apt-get(8) - Linux man page](https://linux.die.net/man/8/apt-get)
- [Debian. Разъясните про --no-install-recommends.](https://www.linux.org.ru/forum/desktop/11909791)
- [25 Useful Basic Commands of APT-GET and APT-CACHE for Package Management](https://www.tecmint.com/useful-basic-commands-of-apt-get-and-apt-cache-for-package-management/)
- [UBUNTU packages](https://packages.ubuntu.com/)
```
sudo apt-get update -q && \
sudo apt-get -y --no-install-recommends install \
chrony \
wget \
tree \
libcurl4-openssl-dev \
libsasl2-dev \
libxml2-dev \
libpng-dev \
libjpeg-dev \
python \
python-dev \
libegl1-mesa \
libegl1-mesa-dev \
libglu1-mesa \
libglu1-mesa-dev \
libgmp-dev \
libmpfr-dev \
libcairo2-dev \
libxt-dev \
gtk2-engines \
libv8-dev \
libudunits2-0 \
unixODBC* \
postgresql \
libmariadb-dev \
libmysqlclient-dev \
gfortran-6 \
texlive* \
ufw \
dejavu* \
rrdtool \
psmisc \
lrzsz \
gdal* \
libproj-dev \
r-cran-rprotobuf \
libprotobuf-dev \
libgeos-dev
```

```
sudo apt-get -y --no-install-recommends install \
mesa-common-dev \
libudunits2-dev \
libssl-dev \
curl \
fonts-dejavu \
fonts-dejavu-core \
fonts-dejavu-extra \
ttf-dejavu \
ttf-dejavu-core \
ttf-dejavu-extra \
postgresql-server-dev-10
```
Возня с `Roboto Condensed`
```
sudo apt-get -y --no-install-recommends install \
fonts-roboto
```

Ставим вместе с рекомендованными пакетами
```
sudo apt-get -y install \
gcc \
g++ \
lzma \
lzma-dev \
liblzma-dev \
lbzip2 \
libbz2-dev \
libblas-dev \
liblapack-dev \
gfortran \
libmagick++-dev \
libpcre2-dev \
ncdu \
glances
```
# r-cran-littler

- [library missing cannot find -lbz2 in arch](https://stackoverflow.com/questions/49841635/library-missing-cannot-find-lbz2-in-arch)
`/usr/bin/ld: cannot find -lbz2`
Ставим `sudo apt-get install libbz2-dev`
- [Question: cannot find -llapack + -lblas for package install](https://support.bioconductor.org/p/67326/)
`sudo apt-get install libblas-dev liblapack-dev`

Пакеты, нужные для RStudio Server. В принципе, он их сам может затащить при инсталляции.
```
sudo apt-get install \
lib32gcc1 \
lib32stdc++6 \
libc6-i386 \
libclang-6.0-dev \
libclang-common-6.0-dev \
libclang-dev \
libclang1-6.0 \
libobjc-7-dev \
libobjc4
```

Пакет, нужный для plumber 1.x
```
sudo apt-get install \
libsodium-dev
```

Пакет, нужный для ragg 4.x
```
Configuration failed to find the harfbuzz freetype2 fribidi library. Try installing:
 * deb: libharfbuzz-dev libfribidi-dev (Debian, Ubuntu, etc)
 * rpm: harfbuzz-devel fribidi-devel (Fedora, EPEL)
 * csw: libharfbuzz_dev libfribidi_dev (Solaris)
 * brew: harfbuzz fribidi (OSX)
```

# x11-xserver-utils


## Ставим R под Ubuntu
- [How To Install R on Ubuntu 18.04](https://www.digitalocean.com/community/tutorials/how-to-install-r-on-ubuntu-18-04)
```
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9
sudo add-apt-repository 'deb https://cloud.r-project.org/bin/linux/ubuntu bionic-cran35/'
sudo apt update
sudo apt install r-base
```


Ставим пакет [`littler`](http://dirk.eddelbuettel.com/code/littler.html)
И включаем его в путь:
- либо в текущей сессии `export PATH=$PATH:/usr/lib/R/site-library/littler/examples`
- либо добавить в настройки bash путем редактирования ресурсного файла: `vi .bashrc`
И передавать потом окружение через параметры команды sudo:
`sudo --preserve-env=PATH -i`

### Как сделать downgrade пакета в Ubuntu
- [How to downgrade a package via apt-get?](https://askubuntu.com/questions/138284/how-to-downgrade-a-package-via-apt-get)
In my opinion, you should first uninstall or purge the package, like:
```
sudo apt-get remove <package>
or
sudo apt-get purge <package>
```
- Актуально для Rstudio Server. [How to downgrade the .deb package to older version](https://unix.stackexchange.com/questions/426263/how-to-downgrade-the-deb-package-to-older-version)
- [How to purge software installed by gdebi?](https://ubuntuforums.org/showthread.php?t=2366442). You can purge packages you installed with gdebi.
(You can purge any package you installed, regardless of installation method)
`sudo apt-get purge rstudio-server`


### Ставим R пакеты
- Возникла проблемка в RStudio Server, выдает в ноутбук ошибку "" . 
Должно лечиться установкой библиотеки libpango (для генерации png)
`sudo apt-get install libpango1.0-dev`. 
	- Детали [здесь](https://support.rstudio.com/hc/en-us/community/posts/200642948-RStudio-Server-unable-to-open-connection-to-X11-display).
	- Еще есть похожая статья [Shiny-server on ubuntu 16 error: "unable to open connection to X11 display "](https://community.rstudio.com/t/shiny-server-on-ubuntu-16-error-unable-to-open-connection-to-x11-display/11722). Can you execute `capabilities()` in the version of R that you are using on the server, and share the output? I am curious if you have the system dependencies required to support generating PNG graphics.
Это все не очень помогло, поэтому поставил подсистему X11 командой `sudo apt install xorg`. Детали в обсуждении [Installing X11 on Ubuntu 18.04](https://askubuntu.com/questions/1071996/installing-x11-on-ubuntu-18-04/1072003)
И опять не помогло, читаем дальше [R unable to start device PNG - capabilities() has TRUE for PNG?](https://stackoverflow.com/questions/24999983/r-unable-to-start-device-png-capabilities-has-true-for-png). Рекомендуют ставить `xvfb` (Virtual Framebuffer 'fake' X server):
`sudo apt-get install xvfb`
	- Еще одно решение: [How to run R scripts on servers without X11](https://stackoverflow.com/questions/13067751/how-to-run-r-scripts-on-servers-without-x11)
	- [How to run R on a server without X11, and avoid broken dependencies](https://stackoverflow.com/questions/1710853/how-to-run-r-on-a-server-without-x11-and-avoid-broken-dependencies)
Все равно не работает, получаем ошибку в summarytools::dfSummary
```
> v_df %>% select(reg_date) %>%
+     summarytools::dfSummary(dfSummary.graph.col = FALSE)
Data Frame Summary  
v_df  
Dimensions: 1227713 x 1  
Duplicates: 1226961  

------------------------------------------------------------------------------------------------------------
No   Variable    Stats / Values      Freqs (% of Valid)    Graph                        Valid      Missing  
---- ----------- ------------------- --------------------- ---------------------------- ---------- ---------
1    reg_date    min : 2016-09-10    752 distinct values             :                  1227713    0        
     [Date]      med : 2017-11-02                                    :                  (100%)     (0%)     
                 max : 2018-10-01                                  : :                                      
                 range : 2y 0m 21d                               . : : . . : :                              
                                                               . : : : : : : :                              
------------------------------------------------------------------------------------------------------------
Warning message:
In png(png_loc <- tempfile(fileext = ".png"), width = 150 * graph.magnif,  :
  unable to open connection to X11 display ''
```
Пробуем по советам из [Shiny-server on ubuntu 16 error: "unable to open connection to X11 display ''](https://stackoverflow.com/questions/51576691/shiny-server-on-ubuntu-16-error-unable-to-open-connection-to-x11-display) поставить
`sudo apt-get install -y qpdf libx11-dev libpng-dev libjpeg62`


- [GNU Operating System. Findutils](https://www.gnu.org/software/findutils/)
- Для `jqr` надо ставить либы...
```
Configuration failed because libjq was not found.
On Ubuntu 14.04 or 16.04 you can use the PPA:
  sudo add-apt-repository -y ppa:opencpu/jq
  sudo apt-get update
  sudo apt-get install libjq-dev
On other sytems try installing:
 * deb: libjq-dev (Debian, Ubuntu 16.10 and up).
 * rpm: jq-devel (Fedora, EPEL)
 * csw: libjq_dev (Solaris)
 * brew: jq (OSX)
```

- для `flextable`\`magick` надо ставить либы
```
Configuration failed because Magick++ was not found. Try installing:
 - deb: 'libmagick++-dev' (Debian, Ubuntu)
 - rpm: 'ImageMagick-c++-devel' (Fedora, CentOS, RHEL)
 - csw: 'imagemagick_dev' (Solaris)
```

```
sudo /usr/lib/R/site-library/littler/examples/install2.r --error --deps TRUE \
curl
```

```
sudo /usr/lib/R/site-library/littler/examples/install2.r --error --deps TRUE \
tidyverse \
Cairo \
gdtools \
git2r \
shiny \
shinyjs \
DT \
shinyjqui \
shinythemes \
shinyBS \
shinyWidgets \
shinycssloaders \
futile.logger \
extrafont \
hrbrthemes \
anytime \
tictoc \
re2r \
officer \
openxlsx \
assertr \
checkmate \
promises \
future \
magrittr \
readxl \
lubridate \
tictoc \
checkmate \
openxlsx \
hrbrthemes \
stringi
```

```
sudo /usr/lib/R/site-library/littler/examples/install2.r --error --deps TRUE \
data.table \
jsonlite \
jqr \
readtext \
iterators \
foreach \
doParallel
```

### Готовим окружение для RStudio
Не забыть завести отдельного пользователя с uid > 100 !:
`sudo useradd <username>`
`sudo passwd <username>`

Надо создать пользователя `ruser` с домашней директорией. В убунте есть специфика, читаем суть здесь:
- [Why is the home directory not created when I create a new user?](https://unix.stackexchange.com/questions/182180/why-is-the-home-directory-not-created-when-i-create-a-new-user)
- [Create the home directory while creating a user {duplicate}](https://askubuntu.com/questions/393463/create-the-home-directory-while-creating-a-user)

```
useradd -m USERNAME
```
You have to use -m, otherwise no home directory will be created. If you want to specify the path of the home directory, use -d and specify the path:
```
useradd -m -d /PATH/TO/FOLDER USERNAME
```

Ну а если уж пользователь был создан, то читаем здесь:
- [Add a Home directory for already created user when no direct root login available](https://serverfault.com/questions/576354/add-a-home-directory-for-already-created-user-when-no-direct-root-login-availabl)
Либо просто удалить пользователя командой: `sudo userdel ruser`

## Апгрейдим R под Ubuntu
- [How to Check your Ubuntu Version](https://linuxize.com/post/how-to-check-your-ubuntu-version/). `lsb_release -a`
- Проблемы при апдейте
- [Apt unmet dependencies while installing R on Ubuntu 16.04](https://askubuntu.com/questions/1125448/apt-unmet-dependencies-while-installing-r-on-ubuntu-16-04)
- [Troubles with the installation of R on Ubuntu 18.04](https://unix.stackexchange.com/questions/558380/troubles-with-the-installation-of-r-on-ubuntu-18-04). Тут оказалось рабочее решение:
The issue was the old dependencies. I ran this command to fix the issue
`sudo apt-get -u dist-upgrade`
- [Ubuntu – Unmet dependencies when trying to install r-base](https://itectec.com/ubuntu/ubuntu-unmet-dependencies-when-trying-to-install-r-base/)
```
sudo apt install --fix-broken
sudo apt-get update
sudo apt-get upgrade
```

Надо разбираться с проблемами зависимостей.... Спускаться вниз
- [How to upgrade from Ubuntu 18.04 LTS to 20.04 LTS today](https://ubuntu.com/blog/how-to-upgrade-from-ubuntu-18-04-lts-to-20-04-lts-today)
`sudo do-release-upgrade -d`
- [Trouble installing RStudio Server on Ubuntu--can't find R, but it's there](https://community.rstudio.com/t/trouble-installing-rstudio-server-on-ubuntu-cant-find-r-but-its-there/10212)
`sudo rstudio-server verify-installation`
- [RStudio (OpenSource) Initialization error](https://community.rstudio.com/t/rstudio-opensource-initialization-error/45405)
- [rstudio initialization error unable to connect to service](https://community.rstudio.com/t/rstudio-initialization-error-unable-to-connect-to-service/85099)
To reset RStudio's state in version 1.3 and later:

The .rstudio , .config , and .local directories, as well as the .RData and .Rhistory files, are located in each user's default working directory (typically their home directory). This means that you would also have to delete `~/.config/rstudio/` and `~/.local/share/rstudio/` for that particular user.
И вот это РЕАЛЬНО сработало!


- [How to update R 3.x to the new R 4.x in Linux Ubuntu](https://medium.com/@hpgomide/how-to-update-your-r-3-x-to-the-r-4-x-in-your-linux-ubuntu-46e2209409c3)
First, you need to check the file ‘/etc/apt/sources.list’, and look for the line. ‘deb https://cloud.r-project.org/bin/linux/ubuntu focal-cran40/’
If you don’t have this line, you can run the following in a terminal session to use the R CRAN version:
$ sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9
$ sudo add-apt-repository 'deb https://cloud.r-project.org/bin/linux/ubuntu focal-cran40/'
Now install R by typing:
$ sudo apt install r-base
After that, check the R version.
$ R --version
Updating R 3.x packages to the new R 4.0.
As R 4.0 introduced several changes to base functions, programmers had to rewrite their packages. In order to update your already installed, just type the following in the R console:
update.packages(ask = FALSE, checkBuilt = TRUE)
This will probably will take a few minutes.
If you’re lazy like me, you’re ready to go. However, If want to update all your packages at once, stay with me.
Update all packages
In the R console, create an object with all installed packages in the previous version. You have to point to your installation. Mine was:
‘/home/henriquegomide/R/x86_64-pc-linux-gnu-library/3.6/’
old_packages <- installed.packages(lib.loc = "/home/henriquegomide/R/x86_64-pc-linux-gnu-library/3.6/
")
head(old_packages[, 1])
After that, compare the packages you had in 3.6 to your new 4.0 installation:
new_packages <- installed.packages()
missing_packages <- as.data.frame(old_packages[
!old_packages[, "Package"] %in% new_packages[, "Package"],
])
Then:
install.packages(missing_packages$Package)
This will probably take several minutes to run.
References
https://linuxize.com/post/how-to-install-r-on-ubuntu-20-04/
https://www.r-bloggers.com/get-all-your-packages-back-on-r-4-0-0/

# RHEL 8 / CentOS 8
- [Install R & RStudio on CentOS 8 / RHEL 8 Linux](https://computingforgeeks.com/install-r-and-rstudio-on-centos-rhel-linux/)