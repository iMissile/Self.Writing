# 0. Подготовка ОС и сертификатов

## Ubuntu 22.x
```
# Обновление списка пакетов
sudo apt update

# Установка Snap (обычно уже установлен) и Certbot
sudo snap install core
sudo snap refresh core
sudo snap install --classic certbot

# Создание символической ссылки для удобного запуска
sudo ln -s /snap/bin/certbot /usr/bin/certbot
```

## Ubuntu 24.x

* apt update — работает без изменений
* Snap — предустановлен в Ubuntu 24.04 по умолчанию
* Certbot из Snap — официально рекомендуемый способ для Ubuntu 24.04

```
# Установка Snap (на всякий случай, если вдруг не установлен)
sudo apt install -y snapd

# Snapd уже установлен, но требует перезагрузки или запуска служб
sudo systemctl enable --now snapd.socket
sudo systemctl start snapd

# Дождитесь инициализации snapd (важно!)
sudo snap wait system seed.loaded

# Теперь установите core
sudo snap install core
sudo snap refresh core

# Установите certbot
sudo snap install --classic certbot

# Создайте символическую ссылку
sudo ln -s /snap/bin/certbot /usr/bin/certbot

# Проверьте установку
certbot --version
```



```
--- создание срт ---
# OLD sudo certbot certonly --standalone -d math.schastev.com --staple-ocsp -m ishutov@gmail.com --agree-tos
sudo certbot certonly --standalone -d mlops.schastev.com --staple-ocsp -m ishutov@gmail.com --agree-tos


# Сертфикат и ключ вот тут (туту ссылка, но именно на нее будем "натравливать" наш сервис):
Certificate is saved at: /etc/letsencrypt/live/math.schastev.com/fullchain.pem
Key is saved at:         /etc/letsencrypt/live/math.schastev.com/privkey.pem

--- обновление срт ---
# OLD certbot certonly --standalone --force-renew -d math.schastev.com --staple-ocsp -m ishutov@gmail.com --agree-tos
certbot certonly --standalone --force-renew -d mlops.schastev.com --staple-ocsp -m ishutov@gmail.com --agree-tos

```

# 0. Ставим Docker-engine

```
# 1. Удалите старые версии, если они были
sudo apt-get remove docker docker-engine docker.io containerd runc

# 2. Установите зависимости для добавления репозитория
sudo apt-get update
sudo apt-get install ca-certificates curl

# 3. Добавьте официальный GPG-ключ Docker
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# 4. Добавьте репозиторий Docker в APT
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update

# 5. Установите Docker Engine и необходимые плагины
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin

docker --version
```

# 0. Ограничиваем место для docker контейнеров
```
[igor.schastiev@schastievi ~]$ cat /etc/docker/daemon.json
{
  "default-address-pools": [
    { "base": "172.31.0.0/16", "size": 26 }
  ],
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "50m",
    "max-file": "3"
  }
}
```

```
root@ishutov:~# nano /etc/docker/daemon.json
root@ishutov:~# systemctl restart docker
root@ishutov:~# systemctl enable docker
Synchronizing state of docker.service with SysV service script with /usr/lib/systemd/systemd-sysv-install.
Executing: /usr/lib/systemd/systemd-sysv-install enable docker
root@ishutov:~# systemctl status docker
```

# 1. Поднятие 3x-ui в контейнере

Создаем директории /app/3x-ui,  /app/3x-ui/db
yml кладем в приложение.

```
[igor.schastiev@schastievi 3x-ui]$ cat docker-compose_3x-ui.yml
services:
  3xui:
    image: ghcr.io/mhsanaei/3x-ui:v3.3.0
    container_name: 3x-ui
    ports:
      # Web-admin + subscripton 
      - "12053:12053/tcp"
      - "12096:12096/tcp"
      # 👇 This single line opens the entire range for both TCP and UDP
      - "443:443/tcp"
      - "9000:9000/tcp"
      - "9001:9001/tcp"
      - "9002:9002/tcp"
      - "9003:9003/tcp"
      - "9004:9004/tcp"
      - "9005:9005/tcp"
      - "443:443/udp"
      - "9000:9000/udp"
      - "9001:9001/udp"
      - "9002:9002/udp"
      - "9003:9003/udp"
      - "9004:9004/udp"
      - "9005:9005/udp"
    volumes:
      - "$PWD/db/:/etc/x-ui/"
      - "/etc/letsencrypt/:/etc/letsencrypt/:ro"
    environment:
      XRAY_VMESS_AEAD_FORCED: "false"
      XUI_ENABLE_FAIL2BAN: "true"
      LANG: "C.UTF-8"
      LC_ALL: "C.UTF-8"
    tty: true
    restart: unless-stopped
[igor.schastiev@schastievi 3x-ui]$
```

Запуск докера 
```
docker compose -f docker-compose_3x-ui.yml up -d
```

Настраиваем 3x-ui
0. Добавляем в панель сертификаты в панель и подписки
1. Изменить пользователя/пароль
2. Изменить порты
Перенастраиваем порты внутри (для web & subscription), дописываем 1, меняем конфиг, рестартим
3. Делаем 2FA

При настройке подключения указываем ключи из локальной директории докера:
```
ls -al /etc/letsencrypt/live/math.schastev.com/
```


# 2. настройка маршрутизации

```
[igor.schastiev@schastievi 3x-ui]$ sudo cat /etc/sysconfig/iptables
*filter
:INPUT ACCEPT [0:0]
-A INPUT -m state --state RELATED,ESTABLISHED -j ACCEPT
-A INPUT -p icmp -j ACCEPT
-A INPUT -i lo -j ACCEPT
## Accept ssh
-A INPUT -p tcp -m state --state NEW -m tcp --dport 22 -j ACCEPT
## Certbot auto web server for cert renew
-A INPUT -p tcp -m state --state NEW -m tcp --dport 80 -j ACCEPT
## SS v2ray
-A INPUT -p tcp -m state --state NEW -m tcp --dport 443 -j ACCEPT
-A INPUT -p udp -m state --state NEW -m udp --dport 443 -j ACCEPT
## SS
-A INPUT -p tcp -m state --state NEW -m tcp --dport 8443 -j ACCEPT
-A INPUT -p udp -m state --state NEW -m udp --dport 8443 -j ACCEPT
## Accept Input for shadowsocks-rust services
-A INPUT -p tcp -m tcp --dport 40000:49999 -j ACCEPT
-A INPUT -p udp -m udp --dport 40000:49999 -j ACCEPT
## Accept zabbix
-A INPUT -p udp -m udp -s 87.238.96.18 --dport 10050 -j ACCEPT
-A INPUT -p tcp -m tcp -s 87.238.96.18 --dport 10050 -j ACCEPT
## Accept 3x-ui User interface
-A INPUT -p tcp -m tcp -s 87.238.96.18 --dport 12053 -j ACCEPT
## Accept 3x-ui Subscription interface
-A INPUT -p tcp -m tcp -s 87.238.96.18 --dport 12096 -j ACCEPT
## Accept 3x-ui vless 18443 port
-A INPUT -p tcp -m tcp --dport 18443 -j ACCEPT
## Accept 3x-ui vless, reality, xhttp 18443 port
-A INPUT -p tcp -m tcp --dport 18080 -j ACCEPT
## Accept 3x-ui vless, reality, xhttp 8080, 8880, 8008 port
-A INPUT -p tcp -m tcp --dport 8080 -j ACCEPT
-A INPUT -p tcp -m tcp --dport 8880 -j ACCEPT
-A INPUT -p tcp -m tcp --dport 8008 -j ACCEPT
## For HYSTERIA
-A INPUT -p tcp -m tcp --dport 9090 -j ACCEPT
-A INPUT -p udp -m udp --dport 9090 -j ACCEPT
## For HYSTERIA 3x-ui
-A INPUT -p udp -m udp --dport 9091 -j ACCEPT
-A INPUT -p udp -m udp --dport 9092 -j ACCEPT
-A INPUT -p udp -m udp --dport 9093 -j ACCEPT
-A INPUT -p udp -m udp --dport 9094 -j ACCEPT
-A INPUT -p udp -m udp --dport 9095 -j ACCEPT

## Reject other  input
-A INPUT -j REJECT --reject-with icmp-host-prohibited

:FORWARD ACCEPT [0:0]
-A FORWARD -j REJECT --reject-with icmp-host-prohibited

:OUTPUT ACCEPT [0:0]

COMMIT

*nat
:PREROUTING ACCEPT [0:0]

:POSTROUTING ACCEPT [0:0]
## NAT pure SS trafic
-A POSTROUTING -o ens3 -j MASQUERADE

:OUTPUT ACCEPT [0:0]

COMMIT
[igor.schastiev@schastievi 3x-ui]$
```

# 3. Настройка резервного копирования

Запуск
```
sudo apt install cron
systemctl status cron
# автозапуск
systemctl enable cron
```
```
[igor.schastiev@schastievi 3x-ui]$ cat /etc/crontab
SHELL=/bin/bash
PATH=/sbin:/bin:/usr/sbin:/usr/bin
MAILTO=root

# For details see man 4 crontabs

# Example of job definition:
# .---------------- minute (0 - 59)
# |  .------------- hour (0 - 23)
# |  |  .---------- day of month (1 - 31)
# |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
# |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat
# |  |  |  |  |
# *  *  *  *  * user-name  command to be executed

00 4 15 */2 * root certbot certonly --standalone --force-renew -d mlops.schastev.com --staple-ocsp -m ishutov@gmail.com --agree-tos
06 4 15 * * root systemctl restart docker
[igor.schastiev@schastievi 3x-ui]$
```

# 9. Диагностика подключений
```
# определяем ethernet port
ifconfig
# слушаем конкретный порт
apt install tcpdump
tcpdump -i ens3 udp port 9000
tcpdump -i ens3 tcp port 9000
```
и смотрим подключения

Проверяем настройки файервола на ubuntu 24.x
```
ufw status
```