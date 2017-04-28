yum update
yum install -y chrony
systemctl start chronyd
systemctl enable chronyd
systemctl status chronyd

yum -y install epel-release
uname -a

yum wget install libcurl-devel openssl-devel cyrus-sasl-devel libxml2-devel libpng-devel libjpeg-devel python python-devel proj proj-devel mesa-libGL mesa-libGL-devel mesa-libGLU mesa-libGLU-devel gmp-devel mpfr-devel cairo-devel libXt-devel gtk2-devel v8-devel udunits2 udunits2-devel

yum groupinstall X11
yum install xorg-x11-server-Xvfb
yum groupinstall "Development Tools"
yum update

yum install R



При установке пакетов под root (для всех) запускаем R от рута `sudo -i R` и прогоняему установку
================== В консоли R
После установки библиотек ищем расположение h файлов следующей командой `find . -type f -name udunits2.h` и запускаем инсталляцию с параметрами:
install.packages("udunits2", configure.args='--with-udunits2-include=/usr/include/udunits2/')

chooseCRANmirror(graphics=FALSE, ind=37)
pacman::p_load("gWidgetstcltk")


================== Web Доступ
Shiny Server
- `http://10.0.0.228:3838/` -- общая стартовая страница с приложениями
- `http://10.0.0.228:3838/example1/` -- общее приложение по ссылке 
- `http://ip:3838/users/ruser/iot/` -- частное приложение
RStudio Server
- `http://<server-ip>:8787`