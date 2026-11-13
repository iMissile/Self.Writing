# RustDesk Server на wolfram-server.ru

Самохостинг [RustDesk](https://rustdesk.com/) (открытый аналог TeamViewer / AnyDesk) на Ubuntu 24.

**Дата развёртывания:** 12.11.2026  
**Режим:** Docker Compose + `network_mode: host`  
**Статус:** работает, клиенты подключаются

---

## 1. Что установлено

На сервере крутятся два контейнера из образа `rustdesk/rustdesk-server:latest`:

| Сервис | Роль |
|--------|------|
| **hbbs** | ID-сервер / rendezvous (регистрация клиентов, NAT hole punching) |
| **hbbr** | Relay (если прямой P2P не сложился) |

Клиенты скачиваются с [rustdesk.com](https://rustdesk.com/). Трафик идёт через ваш сервер, не через публичные серверы RustDesk.

| Параметр | Значение |
|----------|----------|
| Хост (DNS) | `wolfram-server.ru` |
| IP | `153.80.246.207` |
| Hostname ОС | `wfs219691.com` |
| Каталог | `/opt/rustdesk/` |
| Данные и ключи | `/opt/rustdesk/data/` |
| Публичный ключ (Key) | `1eDRXkufROJeWv6xUPq8aCjf3zbWO1krl+dg2N2BY8I=` |
| Relay в hbbs | `-r wolfram-server.ru:21117` |

---

## 2. Порты

Должны быть открыты **на UFW и в облачном firewall / security group** (если есть):

| Порт | Протокол | Назначение |
|------|----------|------------|
| 21115 | TCP | тест типа NAT |
| 21116 | TCP + **UDP** | ID / hole punching |
| 21117 | TCP | relay |
| 21118 | TCP | websocket hbbs (web-клиент, опционально) |
| 21119 | TCP | websocket hbbr (web-клиент, опционально) |

**UDP 21116** часто забывают — без него соединение долгое или всегда через relay.

---

## 3. Доступ по SSH (как ставили)

С рабочей Windows-машины:

```bash
ssh -o HostKeyAlias=153.80.246.207 \
  -i ~/.ssh/wolfram-bootstrap-agent-win \
  root@wolfram-server.ru
```

Или по IP:

```bash
ssh -o HostKeyAlias=153.80.246.207 \
  -i ~/.ssh/wolfram-bootstrap-agent-win \
  root@153.80.246.207
```

Ключ `~/.ssh/id_rsa` и пользователь `ilya` на этот хост **не** пускают. Каталог `~/.ssh/wolfram-server-recovery` — это директория, не ключ; OpenSSH его не читает.

В `known_hosts` записан IP `153.80.246.207`; для имени `wolfram-server.ru` удобен `HostKeyAlias`.

---

## 4. Установка по шагам (как было сделано)

Выполнять **на сервере** под `root` (после SSH из §3).

### 4.1. Проверка «ещё не стоит»

```bash
hostname
find / -name 'id_ed25519.pub' 2>/dev/null
ss -tulpn | grep -E '2111[5-9]' || echo 'ports free'
command -v docker || echo 'no docker'
```

Ожидание до установки: ключа нет, портов 2111x нет, Docker может отсутствовать.

### 4.2. Docker

Если Docker ещё нет:

```bash
curl -fsSL https://get.docker.com | sh
docker --version
docker compose version
```

На момент установки: Docker `29.9.3`, Compose `v5.7.1`.

### 4.3. Каталог и compose (host mode)

```bash
mkdir -p /opt/rustdesk/data
cat > /opt/rustdesk/docker-compose.yml <<'EOF'
services:
  hbbs:
    container_name: hbbs
    image: rustdesk/rustdesk-server:latest
    command: hbbs -r wolfram-server.ru:21117
    volumes:
      - ./data:/root
    network_mode: "host"
    depends_on:
      - hbbr
    restart: unless-stopped

  hbbr:
    container_name: hbbr
    image: rustdesk/rustdesk-server:latest
    command: hbbr
    volumes:
      - ./data:/root
    network_mode: "host"
    restart: unless-stopped
EOF
```

`-r wolfram-server.ru:21117` — адрес relay, который hbbs раздаёт клиентам. Имя должно резолвиться с интернета в этот сервер.

На Linux официально предпочтителен **`network_mode: host`**: меньше сюрпризов с UDP/NAT, чем у проброса портов.

### 4.4. Firewall (UFW)

```bash
ufw allow 21115/tcp comment 'rustdesk-nat'
ufw allow 21116/tcp comment 'rustdesk-id-tcp'
ufw allow 21116/udp comment 'rustdesk-id-udp'
ufw allow 21117/tcp comment 'rustdesk-relay'
ufw allow 21118/tcp comment 'rustdesk-web-hbbs'
ufw allow 21119/tcp comment 'rustdesk-web-hbbr'
ufw status numbered
```

SSH / 80 / 443 уже были разрешены; их не трогали.

### 4.5. Запуск

```bash
cd /opt/rustdesk
docker compose pull
docker compose up -d
docker compose ps
docker compose logs --tail=50
```

В логах при первом старте ожидаемо:

- `Private/public key written to id_ed25519/id_ed25519.pub`
- `Key: 1eDRXkufROJeWv6xUPq8aCjf3zbWO1krl+dg2N2BY8I=`
- hbbs: Listening on tcp/udp `:21116`, tcp `:21115`, websocket `:21118`
- hbbr: Listening on tcp `:21117`, websocket `:21119`
- `relay-servers=["wolfram-server.ru:21117"]`

### 4.6. Права на ключи

```bash
chmod 700 /opt/rustdesk/data
chmod 600 /opt/rustdesk/data/id_ed25519
chmod 644 /opt/rustdesk/data/id_ed25519.pub
```

Приватный ключ **не** копировать клиентам и не светить. Клиентам нужен только `.pub`.

### 4.7. Проверка на сервере

```bash
ls -la /opt/rustdesk/data/
cat /opt/rustdesk/data/id_ed25519.pub
ss -tulpn | grep -E '2111[5-9]'
docker compose -f /opt/rustdesk/docker-compose.yml ps
```

Ожидание: оба контейнера `Up`, слушаются TCP 21115–21119 и UDP 21116, файл `id_ed25519.pub` существует.

### 4.8. Проверка снаружи (с ПК)

PowerShell:

```powershell
foreach ($p in 21115,21116,21117,21118,21119) {
  $r = Test-NetConnection wolfram-server.ru -Port $p -WarningAction SilentlyContinue
  "{0}: {1}" -f $p, $r.TcpTestSucceeded
}
```

Ожидание: все `True` (UDP 21116 так не проверяется — смотрите логи при реальном коннекте).

---

## 5. Настройка клиентов

### 5.1. Установка

Скачать клиент с [https://rustdesk.com/](https://rustdesk.com/) на каждое устройство (Windows / Linux / macOS / Android / iOS).

### 5.2. Сеть

1. Открыть **Settings → Network** (или «Сеть»).
2. Разблокировать редактирование (карандаш / unlock).
3. Заполнить:

| Поле | Значение |
|------|----------|
| **ID Server** | `wolfram-server.ru` |
| **Relay Server** | `wolfram-server.ru` |
| **API Server** | *(пусто — у OSS нет API)* |
| **Key** | `1eDRXkufROJeWv6xUPq8aCjf3zbWO1krl+dg2N2BY8I=` |

4. Apply / OK.

Статус должен стать **Ready** / готов. Если клиент всё ещё ходит на публичные серверы RustDesk — Key или ID Server не применились.

Тот же Key можно снова прочитать на сервере:

```bash
cat /opt/rustdesk/data/id_ed25519.pub
```

### 5.3. Первое соединение

1. На **обоих** устройствах прописать сервер (§5.2).
2. На целевом устройстве взять его **ID** (главное окно клиента).
3. С управляющего устройства ввести этот ID → Connect.
4. На целевом подтвердить одноразовый пароль **или** заранее задать постоянный пароль в настройках безопасности.
5. По желанию на «серверных» машинах: постоянный пароль + автозапуск RustDesk.

---

## 6. Эксплуатация

### Обновление образа

```bash
cd /opt/rustdesk
docker compose pull
docker compose up -d
docker compose ps
docker compose logs --tail=30
```

### Логи

```bash
cd /opt/rustdesk
docker compose logs -f --tail=100
# или по сервису:
docker logs hbbs --tail=100
docker logs hbbr --tail=100
```

### Остановка / старт

```bash
cd /opt/rustdesk
docker compose stop
docker compose start
# полный пересоздать:
docker compose down
docker compose up -d
```

`down` **не** удаляет `./data` (том — bind mount), ключи сохраняются.

### Бэкап

Критично сохранить каталог `/opt/rustdesk/data/`, особенно:

- `id_ed25519` — приватный
- `id_ed25519.pub` — публичный (тот же, что в клиентах)
- `db_v2.sqlite3*` — база ID

Потеря приватного ключа = все клиенты надо перенастроить на **новый** Key после пересоздания.

Пример:

```bash
tar -czf /root/rustdesk-data-$(date +%F).tgz -C /opt/rustdesk data
```

---

## 7. Типичные сбои

| Симптом | Что проверить |
|---------|----------------|
| Клиент не Ready | ID Server / Key; опечатка в Key; DNS `wolfram-server.ru` |
| Key mismatch | В клиенте старый или чужой Key; на сервере пересоздали `data/` |
| Долго соединяется / только relay | Открыт ли **UDP 21116** на UFW и у провайдера |
| Порт снаружи закрыт | `ufw status`; облачный firewall; `ss -tulpn \| grep 2111` |
| Контейнеры не Up | `docker compose logs`; конфликт портов |
| После `docker compose down` и чистки `data/` | Ключ новый — обновить Key во **всех** клиентах |

---

## 8. WOL (Wake-on-LAN)

Magic packet уходит **только из той же LAN**, что и машина-отправитель (как у бесплатного AnyDesk). Self-hosted `hbbs`/`hbbr` на wolfram-server.ru **не** шлёт WOL: сервер — ID/relay, не «always-on сосед» в LAN цели. Источник: [discussion #1249](https://github.com/rustdesk/rustdesk/discussions/1249). Сводка сторонних утилит — в `New_Windows.md` → **Wake-on-LAN**.

### 8.1. Настройка цели (машина, которую будят)

1. **BIOS/UEFI** — включить Wake-on-LAN / Wake on PCI-E / Power On by PCI-E (название зависит от платы).
2. **Windows, NIC** — Диспетчер устройств → сетевой адаптер → Свойства → Управление электропитанием:
   - разрешить устройству выводить компьютер из ждущего режима;
   - «Только при помощи волшебного пакета» / **Wake on magic packet** (если есть отдельная вкладка Advanced — тоже).
3. **RustDesk на цели** — не запрещать LAN discovery:
   - Settings → Security → снять **Deny LAN discovery** / «Отклонять обнаружение в LAN» (если стояло);
   - либо опция `enable-lan-discovery=Y` при кастомной установке.
4. Клиент на цели лучше как служба + автозапуск, чтобы после пробуждения сразу принимал соединение (§5.3).
5. Один раз пока цель **включена**: с управляющей машины в той же LAN открыть вкладку **Discovered** (иконка навигатора / «Обнаруженные») и дождаться скана — RustDesk запомнит **MAC** (без этого WOL из UI не из чего слать).

### 8.2. Использование (Flutter-клиент)

1. Управляющая и целевая машины — **одна L2/LAN** (или один broadcast-домен). Из другой сети / через интернет пункт WOL в OSS не доставит пакет.
2. Главное окно → вкладка **Discovered** (не Favorites / Recent: у Flutter пункт WOL только здесь, даже если цель в избранном — [discussion #12274](https://github.com/rustdesk/rustdesk/discussions/12274)).
3. На плитке цели → **WOL** / Wake on LAN → ждать загрузки NIC и старта ОС/службы RustDesk → Connect по ID как обычно.
4. Sciter-клиент (старый UI) показывал WOL и на обычных remotes; актуальный Flutter — ориентироваться на Discovered.

### 8.3. Если не будит

| Проверка | Как |
|----------|-----|
| WOL на железе/ОС | BIOS + «Wake on magic packet»; тест вне RustDesk: [wol-rs](https://github.com/fengyc/wol-rs/releases/tag/v1.1.0) или `wakeonlan aa:bb:cc:dd:ee:ff` |
| MAC известен клиенту | Цель хоть раз была online в **Discovered** с этой управляющей машины |
| Same LAN | Отправитель не за VPN/другой подсетью без broadcast |
| Сон vs выключение | Часть NIC будит из sleep/hibernate, но не из soft-off (S5) — смотреть документацию платы |
| Избранное без WOL | Искать цель во вкладке Discovered, не в Favorites |

С другой сети — не через UI RustDesk: UpSnap / WakeMeOnLAN / WOL на роутере / always-on хост *в LAN цели* (`New_Windows.md`).

---

## 9. Чего сознательно нет

- **RustDesk Server Pro** (веб-консоль, адресная книга, SSO) — не ставили; это отдельный продукт.
- Nginx перед 21116/21117 не нужен: это не HTTP-сервис.
- API Server в клиенте пустой — у OSS нет своего API endpoint.
- Удалённый WOL «через сервер / через другой online-peer в LAN цели» из UI OSS — нет; только same-LAN с отправителя (§8).

Официальная документация:  
[Self-host / Docker](https://rustdesk.com/docs/en/self-host/rustdesk-server-oss/docker/)

---

## 10. Краткая шпаргалка клиента

```
ID Server:    wolfram-server.ru
Relay Server: wolfram-server.ru
Key:          1eDRXkufROJeWv6xUPq8aCjf3zbWO1krl+dg2N2BY8I=
```

Сервер: `/opt/rustdesk/` на `153.80.246.207` (`wfs219691.com`), host networking, UFW 21115–21119 (+ UDP 21116).
