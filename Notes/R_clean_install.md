# подключаем репозитории
yum update
yum -y install chrony
systemctl start chronyd
systemctl enable chronyd
systemctl status chronyd

yum -y install epel-release
uname -a

# ставим R
sudo yum -y install wget epel-release chrony tree
sudo yum -y install R

# ставим доп либы, необходимые для пакетов R
sudo yum -y groupinstall X11
sudo yum -y groupinstall "Development Tools"

sudo yum -y install wget libcurl-devel openssl-devel cyrus-sasl-devel libxml2-devel libpng-devel libjpeg-devel python python-devel proj proj-devel mesa-libGL mesa-libGL-devel mesa-libGLU mesa-libGLU-devel gmp-devel mpfr-devel cairo-devel libXt-devel gtk2-devel v8-devel udunits2 udunits2-devel xorg-x11-server-Xvfb unixODBC* postgresql-devel gcc-gfortran* texlive*, ufw, dejavu*, psmisc, rrdtool, lrzsz

sudo yum -y install dejavu-fonts-common dejavu-sans-mono-fonts rrdtool psmisc lrzsz gdal* proj-devel proj-epsg proj-nad protobuf-devel geos-devel

# ставим все, что касается LaTeX
sudo yum -y install texlive texlive-latex texlive-xetex texlive-collection-fontsrecommended texlive-collection-latex texlive-collection-latexrecommended  texlive-xetex-def texlive-collection-xetex
Добавляем поддержку кириллицы
sudo yum -y install texlive-cyrillic texlive-collection-langcyrillic texlive-cyrillic-doc texlive-framed texlive-titling texlive-*font* linux-liber*

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