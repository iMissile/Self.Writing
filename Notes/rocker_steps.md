# Windows
[boot2docker](http://boot2docker.io/) for Windows устарел, заменен [docker machine](https://docs.docker.com/machine/overview/)

# Lab
hostname: ilya-lab
IP: 10.0.1.30
login/password: root/ilya-lab

# Docker steps
- [Читаем про docker](https://docs.docker.com/get-started/#docker-concepts)
- Ставим docker под centos по инструкции [Get Docker CE for CentOS](https://docs.docker.com/install/linux/docker-ce/centos/) со страницы [About Docker CE](https://docs.docker.com/install/). После установки запускаем и проверяем:
	- Start Docker `sudo systemctl start docker`
	- Verify that docker is installed correctly by running the hello-world image. `sudo docker run hello-world`
- Подключим Epel репозиторий `sudo yum -y install epel-release htop tree`

# Rocker
- [The Rocker Project](https://www.rocker-project.org/). Docker Containers for the R Environment
- Отличная презентация по старту. "Rocker: Using R on Docker. A Hands-On Introduction", Dirk Eddelbuettel, Pre-Conference Tutorial, useR! 2015, June 30, 2015.

После установки docker выполняем базовые шаги:
- Забираем image с хаба: `docker pull r-base`
- Смотрим, какие у нас есть локальные images: `docker images <r-base>`

- r-base можно прямо запустить из контейнера командой `docker run --rm -ti r-base`. Детали по запуску контейнера можно прочитать [здесь](https://hub.docker.com/r/_/r-base/)
- запускаем контейнер tidyverse: 
	- [rocker/tidyverse](https://hub.docker.com/r/rocker/tidyverse/). Version-stable build of R, rstudio, and R packages
	- Детали по запуску смотрим здесь: [Using the RStudio image](https://github.com/rocker-org/rocker/wiki/Using-the-RStudio-image)
	- Запуск rstudio контейнер как демон (взял из презентации 15 года, слайд 29: `docker run -d -p 8787:8787 rocker/r-studio`. А также с wiki выше. (по умолчанию: username: rstudio\password: rstudio)
- посмотрим запущенные процессы: `docker ps`
- удалим dangling images (с тегом none) командой `docker image prune`. Взял [отсюда](https://stackoverflow.com/questions/33913020/docker-remove-none-tag-images)
- удаляем отдельный образ: `docker image rm my_r`

## Делаем свой docker
- Создаем Dockerfile
- В директории запускаем `docker build --rm true -t my_r .` -t <tag> 
    - When you build your images add “–rm” this should help with removing any intermediate and none images. ‘’‘docker build --rm ‘’’
    - Полезный ответ на вопрос [`How to remove <none> images after building`](https://forums.docker.com/t/how-to-remove-none-images-after-building/7050): 
`docker images -f "dangling=true" -q` -- получаем список ID контенеров с пустым тэгом. Полная команда такова (детали читаем на странице):
`docker rmi $(docker images --filter "dangling=true" -q --no-trunc) 2>/dev/null`
либо так: `docker images -q -f dangling=true | xargs --no-run-if-empty docker rmi`, взято [отсюда](https://gist.github.com/ngpestelos/4fc2e31e19f86b9cf10b)
- [VOLUME секция](https://docs.docker.com/v17.09/engine/reference/builder/#volume)
- не забываем, что в ...

## Запускаем Shiny App
- докер, собранный в варианте локального shiny app, для использования его в shinyproxy запускаем командой: `docker run --rm -p 3838:3838 -ti squid_r`
- запуск командной строки в собранном докере (нюансы [здесь](https://gist.github.com/mitchwongho/11266726)): `docker run -it <image> /bin/bash`

## Полезные утилиты
- [littler: R at the Command-Line via 'r'](https://cran.r-project.org/web/packages/littler/index.html)
    - Исходное описание [на сайте Dirk Eddelbuettel](http://dirk.eddelbuettel.com/code/littler.html)

## Используемые параметры apt-get
[Источник](http://manpages.ubuntu.com/manpages/xenial/man8/apt-get.8.html)
```
-q, --quiet
           Quiet; produces output suitable for logging, omitting progress indicators. More q's
           will produce more quiet up to a maximum of 2. You can also use -q=# to set the quiet
           level, overriding the configuration file. Note that quiet level 2 implies -y; you
           should never use -qq without a no-action modifier such as -d, --print-uris or -s as
           APT may decide to do something you did not expect. Configuration Item: quiet.
--no-install-recommends
           Do not consider recommended packages as a dependency for installing. Configuration
           Item: APT::Install-Recommends
-y, --yes, --assume-yes
           Automatic yes to prompts; assume "yes" as answer to all prompts and run
           non-interactively. If an undesirable situation, such as changing a held package,
           trying to install a unauthenticated package or removing an essential package occurs
           then apt-get will abort. Configuration Item: APT::Get::Assume-Yes.
```

## Параметры `install2.r`
[Источник](https://github.com/eddelbuettel/littler/blob/master/inst/examples/install2.r)

```
Usage: install2.r [-r REPO...] [-l LIBLOC] [-h] [-x] [-s] [-d DEPS] [--error] [--] [PACKAGES ...]
-r --repos REPO     repository to use, or NULL for file [default: getOption]
-l --libloc LIBLOC  location in which to install [default: /usr/local/lib/R/site-library]
-d --deps DEPS      install suggested dependencies as well [default: NA]
-e --error          throw error and halt instead of a warning [default: FALSE]
-s --skipinstalled  skip installing already installed packages [default: FALSE]
-h --help           show this help text
-x --usage          show help and short example usage
```

## Пример образа Артема Клевцова
```
FROM rocker/r-ver:3.4.2

MAINTAINER Artem Klevtsov "a.a.klevtsov@gmail.com"

RUN apt-get update && \
    apt-get install -y \
            libcurl4-openssl-dev \
            libssl-dev \
            libxml2-dev \
            libmariadb-client-lgpl-dev \
            libpq-dev && \
    echo 'options(Ncpus = parallel::detectCores())' >> /usr/local/lib/R/etc/Rprofile.site && \
    echo 'options(shiny.port = 3838)' >> /usr/local/lib/R/etc/Rprofile.site && \
    echo 'options(shiny.host = "0.0.0.0")' >> /usr/local/lib/R/etc/Rprofile.site && \
    echo 'options(shiny.sanitize.errors = FALSE)' >> /usr/local/lib/R/etc/Rprofile.site && \
    install2.r tidyverse && \
    install2.r futile.logger && \
    install2.r checkmate testthat && \
    install2.r DBI RMariaDB RPostgreSQL && \
    install2.r -r http://Rdatatable.github.io/data.table data.table && \
    install2.r rmarkdown && \
    install2.r shiny shinyjs shinyAce shinydashboard && \
    install2.r DT && \
    install2.r plotly && \
    mkdir -p /srv/shiny && \
    rm -rf /var/lib/apt/lists/*

EXPOSE 3838

VOLUME /srv/shiny

WORKDIR /srv/shiny

CMD ["Rscript", "-e", "shiny::runApp('/srv/shiny')"]
```

# Запуск ShinyProxy

Основаня инструкций по SP: https://www.shinyproxy.io/getting-started/	
## Предварительная подготовка на CentOS
- Посмотрели на статус существующего docker: `sudo service docker status`
- Прописали его как сервис
[Start a docker container on CentOS at boot time as a linux service](https://esalagea.wordpress.com/2016/01/21/start-a-docker-container-on-centos-at-boot-time-as-a-linux-service/)
- Читаем статью [Using systemd to control the Docker daemon](https://success.docker.com/article/using-systemd-to-control-the-docker-daemon)
- Создали руками директорию `/etc/systemd/system/docker.service.d/` и в ней файл `/etc/systemd/system/docker.service.d/override.conf`
Файл пришлось руками подправлять, чтобы можно было подключаться к докеру без указания порта
```
[Service]
ExecStart=
ExecStart=/usr/bin/dockerd -D -H tcp://127.0.0.1:2375 -H unix:///var/run/docker.sock
```

- Чистим docker от прошлых образов: [Docker: Remove all images and containers](https://techoverflow.net/2013/10/22/docker-remove-all-images-and-containers/)
```
#!/bin/bash
# Delete all containers
docker rm $(docker ps -a -q)
# Delete all images
docker rmi $(docker images -q)
```
При запуске возникла ошибка:
```
***************************
APPLICATION FAILED TO START
***************************

Description:

Web server failed to start. Port 8080 was already in use.
```
## Как понять, какие порты заняты какими процессами
- [3 Ways to Find Out Which Process Listening on a Particular Port](https://www.tecmint.com/find-out-which-process-listening-on-a-particular-port/)
- [Linux Find Out Which Process Is Listening Upon a Port](https://www.cyberciti.biz/faq/what-process-has-open-linux-port/)
```
netstat -tulpn
```


- Имя и пароль по умолчанию берем с репозитория shinyproxy: [openanalytics/shinyproxy](https://github.com/openanalytics/shinyproxy). ShinyProxy - Open Source Enterprise Deployment for Shiny https://www.shinyproxy.io
Running the application
java -jar shinyproxy-2.0.3.jar 
Navigate to http://localhost:8080 to access the application. If the default configuration is used, authentication will be done against the LDAP server at ldap.forumsys.com; to log in one can use the user name "tesla" and password "password".


## Запуск на чистой Ubuntu 18.x
- Проверяем наличие java 8 командой `java -version`
Если нет, ставим командой `sudo apt install openjdk-8-jre-headless`

- Проверяем наличие docker командой `sudo service docker status`
Если нет, ставим по инструкции [Get Docker CE for Ubuntu](https://docs.docker.com/install/linux/docker-ce/ubuntu/).
После установки проверяем работоспособность докера с помощью тестового образа: `sudo docker run hello-world`.
И опять проверяем статус сервиса командой `sudo service docker status`

- Добавляем кастомный порт. 
Создаем руками директорию `/etc/systemd/system/docker.service.d/` и в ней файл `/etc/systemd/system/docker.service.d/override.conf`
Файл пришлось руками подправлять, чтобы можно было подключаться к докеру без указания порта
```
[Service]
ExecStart=
ExecStart=/usr/bin/dockerd -D -H tcp://127.0.0.1:2375 -H unix:///var/run/docker.sock
```
- Загружаем .jar и запускаем ShinyProxy ручном режиме.
[Страничка загрузки](https://www.shinyproxy.io/downloads/). Скачиваем в домашнюю директорию и запускаем.

- Загружаем demo docker для ShinyProxy
Добавляем image командой `sudo docker pull openanalytics/shinyproxy-demo`

# Запускаем констуктор в контейнере
1. Исходники живут за пределом контейнера. Создали ~/R/ на машине с shinyproxy
2. Стянули ветку huawei командой `git clone -b huawei --single-branch https://gitlab.com/TV-stat/mts-tv-stat.reports.git`