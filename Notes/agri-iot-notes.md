# Настройка машины-сборщика данных

## Настройка Linux
Для нормального функционирования сервера требуется корректно настроить текущее время и его своевременное обновление с определенной периодичностью. Детали смотрим в статье ["Как установить, изменить время и часовой пояс в CentOS 7"](https://serveradmin.ru/ustanovka-nastroyka-i-sinhronizatsiya-vremeni-v-centos/).  

Важные комментарии к статье: Подскажите, пожалуйста, почему после перезагрузки ОС ntp может не стартовать?
Команду `systemctl enable ntpd` выполнил.

Разобрался. Дело в том что CentOS7 для синхронизации времени по умолчанию использует сервис chrony. ntpd не будет стартовать автоматически пока не отключишь chrony.
Что бы отключить chrony нужно выполнить команду: `systemctl disable chronyd.service`
А вообще chrony по функциям очень сильно напоминает ntpd.

Также смотрим статью ["CentOS 7 настройка сервера"](https://serveradmin.ru/centos-7-nastroyka-servera/). Тут учтены нюансы, связанные с сервисом chrony в 7-ой версии CentOS.

### Настройка синхронизации времени
В 7-ой версии CentOS настрйку делаем через утилиту chrony (детали в статьях, указанных выше).

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



## Установка R и RStudio Server

- Prerequisites  
RStudio Server v0.99 requires RedHat or CentOS version 5.4 (or higher) as well as an installation of R. You can install R for RedHat and CentOS using the instructions on CRAN: https://cran.rstudio.com/bin/linux/redhat/README.

Установка под Linux не совсем прозрачно описана, поэтому читаем отдельные блоги.

- Неплохой гид про борьбу с 'dependency hell': ["Installing RStudio — an advanced GUI for R — on CentOS 6"](https://biolives.wordpress.com/2013/07/09/installing-rstudio-an-advanced-gui-for-r-on-centos-6/). Там находим решение с пакетом Cairo.
- Пошаговая инструкция. [How Install R / R Studio on CentOS 7](http://linoxide.com/linux-how-to/install-r-rstudio-centos-7/). Важно, что R работает не из под рута.- 
- [How to install R on CentOS](http://stackoverflow.com/questions/37769985/how-to-install-r-on-centos). The installed version is 3.3.0. I would like to install version 2.X but I don't know how.
- На заметку: при инсталляции пакетов возникло диагностическое сообщение "Delta RPMs disabled because /usr/bin/applydeltarpm not installed". Надо почитать.
- Проверяем версию CentOS командой `uname -a`
- Ставим RStudio Server по [инструкции](https://www.rstudio.com/products/rstudio/download-server/) с RStudio 
- [Запускаем RStudio](http://youriporhosname:8787/) и логинимся под созданным non-root пользователем.
- Ставим Python по инструкции. The IUS repo community has done a wonderful job of providing the absolute latest Python 3 releases as rpm packages for RHEL and CentOS that easily install alongside the default system Python.
	- [Install Latest Python on CentOS 7](http://www.codeghar.com/blog/install-latest-python-on-centos-7.html)
	- Еще инструкция: ["How To Install Python 3 and Set Up a Local Programming Environment on CentOS 7"](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-centos-7)
	- [How to Install Pip on CentOS 7](https://www.liquidweb.com/kb/how-to-install-pip-on-centos-7/)
```
$ sudo yum install -y https://centos7.iuscommunity.org/ius-release.rpm
$ sudo yum update
```
	 
- При установке пакетов по root (для всех) запускаем R от рута `sudo -i R` и прогоняему установку. Для успешного прогона необходимо доставлять системные либы (CentOS specific commands).
```
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
	sudo yum groupinstall X11
	sudo yum install gmp-devel
	sudo yum install mpfr-devel
	sudo yum install cairo-devel
	sudo yum install libXt-devel
	sudo yum install gtk2-devel
	sudo yum install v8-devel
	sudo yum install udunits2
	sudo yum install udunits2-devel
	sudo yum install xorg-x11-server-Xvfb
	
	'# это я бы не ставил, если не потребуется
	sudo yum -y groupinstall "X Window System" "Desktop" "Fonts" "General Purpose Desktop"
	sudo yum install -y https://centos7.iuscommunity.org/ius-release.rpm
	sudo yum update	
```
- Поиск пакетов по репозиторию: `sudo yum search python | grep dev`

- Пакеты надо ставить из под рута, в помощь очень полезные статьи:
	- [Using R — Installing Packages](http://mazamascience.com/WorkingWithData/?p=728)
	- [Using R — Package Installation Problems](http://mazamascience.com/WorkingWithData/?p=1185)
	- Обновление установленных пакетов делаем из под рута в консоли R с помощью пакета pacman: `p_update(update = TRUE, ask = FALSE, ...)`
	-  Еще проще сделать обновление R функцией `update.packages()`

### Проблемы при установке пакетов

- В логах возникала ошибка **Error in readRDS(pfile) : error reading from connection when updating, loading, installing packages**. Возможные варианты решения:
	- [RStudio Support](https://support.rstudio.com/hc/en-us/community/posts/203864278-Error-in-readRDS-pfile-error-reading-from-connection-when-updating-loading-installing-packages): Fixed by reinstalling ggthemes which had some 0 sized files previously. In general might be fixed by looking for such files. These can be found with
`find /usr/local/lib64/R/site-library/ /usr/lib64/R/library/ /usr/lib/R/site-library/ ~/.local/lib/ -iname '*rds' -a -size 0`. Указываем 64, поскольку инсталляция у нас 64-х битная.
- Ошибка *libproj and/or proj_api.h not found in standard search locations*. Это связано с пакетом RGDAL (картография). Ответ находим здесь: [rgdal package installation](http://stackoverflow.com/questions/15248815/rgdal-package-installation).
- Установка пакета rgl потребовала еще массу системных пакетов. Детали читаем здесь: ["How to install R “rgl” package under centos 6?"](http://stackoverflow.com/questions/33512641/how-to-install-r-rgl-package-under-centos-6)
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

**Может возникнуть ситуация**, когда потребуется доставлять фортран. Детально (в т.ч. и про управление пользователями) можно почитать в этой публикации: ["Install RStudio Server on centOS6.5"](http://blog.supstat.com/2014/05/install-rstudio-server-on-centos6-5/)

### Управление пользователями
Тут не все прозрачно, пытаемся разобраться по частям.

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
## Установка RStudio Shiny Server
Читаем оригинальную инструкцию по инсталляции ["Installing Shiny Server Open Source"](https://www.rstudio.com/products/shiny/download-server/)

Once installed, view the [Administrator’s Guide](http://docs.rstudio.com/shiny-server/) to learn how to manage and configure Shiny Server. Stay up to date on Shiny Server news and software updates by subscribing above.

- Проверяем, что процесс запущен:  
`sudo systemctl status shiny-server`
- Cмотрим log файл:  
`/var/log/shiny-server.log`

По умолчанию Shiny Server доступен по порту 3838.

Смапируем наше приложение на location '/iot'. Делается это в конфиге `/etc/shiny-server/shiny-server.conf`. Читаем мануал '2.2.2 Location'  
И рестартуем сервер  
`sudo systemctl restart shiny-server`

При проблемах функционирования начинаем читать логи:  
- `systemctl status shiny-server.service`  
- `journalctl -xe` for details.


### Управление Shiny Server
Читаем х"1.4 Stopping and Starting"](http://docs.rstudio.com/shiny-server/#stopping-and-starting)


### Настройка Shiny Server для нескольких пользователей
Читаем мануал + разъяснительную статью ["Shiny Server Quick Start: Run Shiny Server on multiple ports"](https://support.rstudio.com/hc/en-us/articles/219045167-Shiny-Server-Quick-Start-Run-Shiny-Server-on-multiple-ports)

По шагам
1. Включаем в конфиге многопользовательский режим. При этом все пользовательские приложения будут мэпиться на `~/ShinyApps`. 
2. Делаем линк (мягкая ссылка) разрабатываемого приложения в эту директорию.
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
11. Проверяем конфиурации командой `git config -l`  
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
`wget https://s3.amazonaws.com/rstudio-connect/centos6.3/x86_64/rstudio-connect-1.4.4.1-16-x86_64.rpm`

- Проверяем созданных пользователей: `cat /etc/passwd`. Детальнее можно поглядеть, например, здесь: [Linux Command: List All Users In The System](https://www.cyberciti.biz/faq/linux-list-users-command/)
- Запускаем `http://your-connect-server:3939/` и создаем аккаунт! [The first account will be marked as an RStudio Connect administrator.](http://docs.rstudio.com/connect/admin/getting-started.html#installation)
- Настраиваем почтовый адрес Connect. Секция `SenderEmail`, `vi /etc/rstudio-connect/rstudio-connect.gcfg` и перезапускаем
`sudo systemctl restart rstudio-connect`, `sudo systemctl status rstudio-connect`
- Настраиваем параметры отправки почтовых сообщений в консоли в закладке [Email Settings](http://10.0.0.229:3939/connect/#/admin/settings):
В частности, настройки для отправки через [Yandex.почта](https://yandex.ru/support/mail-new/mail-clients.html#pop3)
- [Проверяем статус](https://support.rstudio.com/hc/en-us/articles/232221028-How-do-I-renew-my-RStudio-Connect-license-on-the-server-) демо лицензии:
```
$ sudo /opt/rstudio-connect/bin/license-manager status
$ sudo /opt/rstudio-connect/bin/license-manager status-offline
```
- Подключаем RStudio IDE для публикации приложений.



### Под капотом RStudio Connect
- [RStudio Connect: Admin Guide - RStudio Documentation in pdf](docs.rstudio.com/connect/admin/index.pdf)
- [5 Server Management](http://docs.rstudio.com/connect/1.4.2/admin/server-management.html). This section describes common administrative tasks for RStudio Connect.
	- `sudo systemctl restart rstudio-connect`
- [Where can I find the files created by RStudio Connect?](https://support.rstudio.com/hc/en-us/articles/227009188-Where-can-I-find-the-files-created-by-RStudio-Connect-). В частности, The RStudio Connect server log is located at `/var/log/rstudio-connect.log`. This file is owned by root with permissions 0600. Это же самое указано в документации, [4 Files & Directories](http://docs.rstudio.com/connect/admin/files-directories.html)
	- [A "live" view of a logfile on Linux](https://www.howtogeek.com/howto/ubuntu/a-live-view-of-a-logfile-on-linux/). Команда `tail -f /path/thefile.log`
- При попытке отправить отчет по Email (иконка Email Report) выдается ошибка `Error: Internal Server Error [500]`. Статья [How To Fix a 500 Internal Server Error ](https://www.lifewire.com/500-internal-server-error-explained-2622938): *The 500 Internal Server Error is a very general HTTP status code that means something has gone wrong on the website's server, but the server could not be more specific on what the exact problem is*. 
В конфиге Apache командой `tail -f /var/log/rstudio-connect.access.log` видим такую запись: `[17/Mar/2017:09:55:13 +0300] "POST /__api__/variants/4/sender?email=me HTTP/1.1" 500 0`
Проблема решилась установкой параметра `Server` в конфигурационном файле RStudio Connect: "The Server.SenderEmail property is the email address from which Connect sends emails. It is important that the sendmail or SMTP configuration RStudio Connect uses be willing and able to send email from this SenderEmail address. Otherwise, Connect will not be able to successfully send email. See Section 2.2.4 for more details about mail sending."

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

или одной строчкой: `yum install texlive texlive-latex texlive-xetex texlive-collection-fontsrecommended texlive-collection-latex texlive-collection-latexrecommended  texlive-xetex-def texlive-collection-xetex`
`
В документации RStudio Connect указано:
`texlive-full # very large dependency, but needed to render PDF documents from R Markdown`. Но такого пакета под CentOS не нашлось.

Ищем, где же установлен TexLive manager: `find / -name 'tl*'` А в CentOS его нет
[CentOS Latex - Install package manually (no tlmgr)](http://tex.stackexchange.com/questions/289404/centos-latex-install-package-manually-no-tlmgr)
Все делаем через `yum`. Поиск по репозиторию осуществляем с помощью [`yum search cyrillic`](https://www.centos.org/docs/5/html/yum/sn-searching-packages.html)

- Ставим `yum install texlive-collection-langcyrillic install texlive-cyrillic-doc`

Ошибки при запуске TeXLive
- LaTeX Error: File 'framed.sty' not found. Решаем установкой [`yum -y install texlive-framed`](https://github.com/rstudio/rmarkdown/issues/39)
- LaTeX Error: File 'titling.sty' not found. Решаем установкой `yum -y install texlive-titling`

Русский язык в LaTeX:
- [Overleaf. Русский язык в LaTeX: XeLaTeX](https://www.overleaf.com/latex/templates/5-dot-2-2-russkii-iazyk-v-latex-xelatex/skfzmvgdgvnk)
- [XeLaTeX или на порядок улучшим качество шрифтов в окончательном pdf](http://astronu.jinr.ru/wiki/index.php/XeLaTeX_%D0%B8%D0%BB%D0%B8_%D0%BD%D0%B0_%D0%BF%D0%BE%D1%80%D1%8F%D0%B4%D0%BE%D0%BA_%D1%83%D0%BB%D1%83%D1%87%D1%88%D0%B8%D0%BC_%D0%BA%D0%B0%D1%87%D0%B5%D1%81%D1%82%D0%B2%D0%BE_%D1%88%D1%80%D0%B8%D1%84%D1%82%D0%BE%D0%B2_%D0%B2_%D0%BE%D0%BA%D0%BE%D0%BD%D1%87%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%D0%BC_pdf)
- Package fontenc Error: Encoding file 't2aenc.def' not found. Решаем установкой [`yum -y install texlive-cyrillic`](http://tex.stackexchange.com/questions/5079/what-is-wrong-with-my-cyrillic-text)
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
	- Ставим под CentOS командой `yum install linux-liber*`. Фонт найден установленным здесь: `/usr/share/fonts/linux-libertine/LinLibertine_*`
	- А еще есть пакет LaTeX [`libertine`](https://www.ctan.org/tex-archive/fonts/libertine/)
	- [Libertine Font problem with XeLaTeX](http://tex.stackexchange.com/questions/105970/font-problem-with-xelatex)

Инсталляция одной строчкой: `yum install texlive-framed texlive-titling texlive-cyrillic texlive-*font*`



### Ставим полноценный TexLive

В конечном итоге все рекомендуют удалить штатный texlive и поставить ручками самому. [TeX Live - Quick install](https://www.tug.org/texlive/quickinstall.html)
[A different idea: Just uninstall all the TeXlive stuff coming from the repositories and install "the real stuff" instead](https://www.centos.org/forums/viewtopic.php?t=52472): https://www.tug.org/texlive/quickinstall.html

- Сносим пакеты, поставленные из репозитория CentOS: `yum remove texlive*`
- Чтобы не возникала ошибка Perl (`Can't locate Digest/MD5.pm in @INC...`), перед запуском инсталлятора необходимо доставить perl пакеты командой `yum install perl-Tk perl-Digest-MD5`. Детальнее читаем тут: [Error during installation of TeXLive 2012 in Fedora](t)

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
