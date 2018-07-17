# Windows
[boot2docker](http://boot2docker.io/) for Windows устарел, заменен [docker machine]

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
- Смотрим, какие у нас есть локальные images: `docker images r-base`

- r-base можно прямо запустить из контейнера командой `docker run --rm -ti r-base`. Детали по запуску контейнера можно прочитать [здесь](https://hub.docker.com/r/_/r-base/)
- запускаем контейнер tidyverse: 
	- [rocker/tidyverse](https://hub.docker.com/r/rocker/tidyverse/). Version-stable build of R, rstudio, and R packages
	- Детали по запуску смотрим здесь: [Using the RStudio image](https://github.com/rocker-org/rocker/wiki/Using-the-RStudio-image)
	- Запуск rstudio контейнер как демон (взял из презентации 15 года, слайд 29: `docker run -d -p 8787:8787 rocker/r-studio`. А также с wiki выше. (по умолчанию: username: rstudio\password: rstudio)
- посмотрим запущенные процессы: `docker ps`

## Делаем свой docker
- Создаем Dockerfile
- В директории запускаем `docker build -rm -t my_r .` -t <tag> 
    - When you build your images add “–rm” this should help with removing any intermediate and none images. ‘’‘docker build --rm ‘’’
    - Полезный ответ на вопрос [`How to remove <none> images after building`](https://forums.docker.com/t/how-to-remove-none-images-after-building/7050): 
`docker images -f "dangling=true" -q` -- получаем список ID контенеров с пустым тэгом. Полная команда такова (детали читаем на странице):
`docker rmi $(docker images --filter "dangling=true" -q --no-trunc) 2>/dev/null`
либо так: `docker images -q -f dangling=true | xargs --no-run-if-empty docker rmi`, взято [отсюда](https://gist.github.com/ngpestelos/4fc2e31e19f86b9cf10b)

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