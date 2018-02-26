
- [PVSM: Рубрика «clickhouse»](http://www.pvsm.ru/cat/clickhouse)
- Примеры запросов с группировкой по времени: [пример 1](https://gist.github.com/alexey-milovidov/2dee968eb95df63b271208f89d3697c3); [пример 2](https://gist.github.com/alexey-milovidov/6fd9246ce44b48345bee3a0df3da5ab0)

## Канал в телеграме
http://telegrammy.net/group/clickhouse_ru/page87.htm

## Полезные командочки
- Вертикальный вывод длинных таблиц: `select * from view_states_tg1h_phase2 limit 1 format Vertical;`

## Репозиторий митапов
- [Presentations, meetups and talks for ClickHouse](https://github.com/yandex/clickhouse-presentations.git)

## План запросов
- Вопрос: есть ли способ получить из ClickHouse план исполнения запроса или что-то вроде того?
Ответ: Что-то похожее на план выполнения запроса есть в логе - смотрите по словам Query pipeline: Там довольно скудная информация, к тому же этот план выводится по части запроса на локальном сервере.
[Помощь по команде `find/locate`](https://www.gnu.org/software/findutils/)
Ищем файл командами `locate --all "clickhouse-server.log"` или `find / -name "clickhouse-server.log"`.
Файл найден здесь: `/var/databases/clickhouse-server/log/clickhouse-server.log`


## Подвал
a BETWEEN b AND c - равнозначно a >= b AND a <= c
