mkdir -p /app/hysteria
cd /app/hysteria
nano docker-compose_hysteria.yml
---
services:
  hysteria:
    image: tobyxdd/hysteria:v2.9.2
    container_name: hysteria
    ports:
      - "9100:9100/udp"
    volumes:
      - "/app/hysteria/9100-config.yaml:/etc/hysteria/9100-config.yaml"
      - "/etc/letsencrypt/:/etc/letsencrypt/:ro"
    command: ["server", "-c", "/etc/hysteria/9100-config.yaml"]
    tty: true
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "/bin/sh", "-c", "if cat /proc/net/udp | grep -q ':238C'; then exit 0; else exit 1; fi"]
      interval: 1m
      timeout: 30s
      retries: 3
      start_period: 10s
    deploy:
      replicas: 1
      resources:
        limits:
          cpus: '0.5'
          memory: 1G
---
vim 9100-config.yaml
---
listen: 0.0.0.0:9100

tls:
  cert: /etc/letsencrypt/live/mlops.schastev.com/fullchain.pem
  key: /etc/letsencrypt/live/mlops.schastev.com/privkey.pem

auth:
  type: userpass
  userpass:
    User001: dg35MpR2xV9qLwN4 ##  own
    User002: Xy5Zsyr5Wc3FjH1R ## 
    User003: Tn9GvKsjd64YcMx7 ## 
    User004: djt9zJpR6Xa1NdUe8 ##
    User005: Ze5VcXbdjr9HtYpK4 ## 
    User006: Rwdhr9jF3Xa6UgQz1 ## 
    User007: Bp4LkZx7Vm2QcJw9N ## 
    User008: Hyhky0fE8Ws1XnCv5 ## 
    User009: Ap6LmsferVc9FjNw4 ## 
    User010: CcgrtRfYk3Np5MbZ2 ##
    User011: Fg8ty674Lk9XzCvB2 ##
    User012: dhfteWq3AsDfGhJ7 ##
    User013: Mty57VcXz1LkPpO9 ##
    User014: Uj8MkLp2QwErTy4 ##
    User015: Ht7fht8w3QsDfG5 ##
    User016: Zr9XcVyiu9k2JhG6 ##
    User017: Wqetr6fGhJk1LpO8 ##
    User018: Vbtyu6wErTy3UiO9 ##
    User019: srer3vBnMmLk4JhG7 ##
    User020: er45fGhJkLp1QwE3 ##
    User021: jk89tUiOoPp2AaSs4 ##
    User022: ade4bVcXzLl3KkH6 ##
    User023: Po9IiUyTtRrty67w1 ##
    User024: ert4hGfDdQs2WwRr5 ##
    User025: fg56cVbNmAs3DdFg8 ##

masquerade:
  type: proxy
  proxy:
    url: https://www.bbc.com/
    rewriteHost: true
---

Client URLs (examples)
---
Happ Proxy:
hysteria2://User001:dg35MpR2xV9qLwN4@85.137.89.99:9100?type=hysteria&mport&security=tls&sni=mlops.schastev.com&alpn=h3&fp=chrome&allowInsecure=0&echfq=none#Netherland-hysteria-9100

v2Box:
hysteria2://User001%3Adg35MpR2xV9qLwN4@85.137.89.99:9100?type=hysteria&mport&security=tls&sni=mlops.schastev.com&alpn=h3&fp=chrome&allowInsecure=0&echfq=none#Netherland-hysteria-9100