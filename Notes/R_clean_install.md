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
sudo yum -y install wget epel-release chrony tree
sudo yum -y install R

## ставим доп либы, необходимые для пакетов R
sudo yum -y groupinstall X11
sudo yum -y groupinstall "Development Tools"

sudo yum -y install wget libcurl-devel openssl-devel cyrus-sasl-devel libxml2-devel libpng-devel libjpeg-devel python python-devel proj proj-devel mesa-libGL mesa-libGL-devel mesa-libGLU mesa-libGLU-devel gmp-devel mpfr-devel cairo-devel libXt-devel gtk2-devel v8-devel udunits2 udunits2-devel xorg-x11-server-Xvfb unixODBC* postgresql-devel mariadb-devel mysql-devel gcc-gfortran* texlive*, ufw, dejavu*, psmisc, rrdtool, wireshark, lrzsz

sudo yum -y install dejavu-fonts-common dejavu-sans-mono-fonts rrdtool psmisc lrzsz gdal* proj-devel proj-epsg proj-nad protobuf-devel geos-devel

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
[Страница загрузки](https://www.rstudio.com/products/rstudio/download-server/)

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
gfortran

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

### Ставим R пакеты
- [GNU Operating System. Findutils](https://www.gnu.org/software/findutils/)
- Для `jqr` надо ставить либы...
``
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

