
- [PVSM: Рубрика «clickhouse»](http://www.pvsm.ru/cat/clickhouse)
- Примеры запросов с группировкой по времени: [пример 1](https://gist.github.com/alexey-milovidov/2dee968eb95df63b271208f89d3697c3); [пример 2](https://gist.github.com/alexey-milovidov/6fd9246ce44b48345bee3a0df3da5ab0)
- [ClickHouse: New Open Source Columnar Database](https://www.percona.com/blog/2017/02/13/clickhouse-new-opensource-columnar-database/)

## Канал в телеграме
http://telegrammy.net/group/clickhouse_ru/page87.htm

## Полезные командочки
- Вертикальный вывод длинных таблиц: `select * from view_states_tg1h_phase2 limit 1 format Vertical;`

## Репозиторий митапов
- [Presentations, meetups and talks for ClickHouse](https://github.com/yandex/clickhouse-presentations.git)

## План запросов
- Вопрос: есть ли способ получить из ClickHouse план исполнения запроса или что-то вроде того?
Ответ: Что-то похожее на план выполнения запроса есть в логе - смотрите по словам Query pipeline: Там довольно скудная информация, к тому же этот план выводится по части запроса на локальном сервере.
[Помощь по команде `find/locate`](https://www.gnu.org/software/findutils/).
Команда `locate` ищет по кэшу.
Ищем файл командами `locate --all "clickhouse-server.log"` или `find / -name "clickhouse-server.log"`.
Файл найден здесь: `/var/databases/clickhouse-server/log/clickhouse-server.log`

## Проблемы с использованием памяти при запросах
Разбираемся с ошибкой "DB::Exception: Memory limit (for query) exceeded"
- [Memory limit (for query) exceeded](https://groups.google.com/forum/#!topic/clickhouse/JhW9x9clTl8)
`max_bytes_before_external_sort` вычисляется только для той структуры данных, которая используется для сортировки. 
Во время обработки запроса, память может тратиться и на другие структуры данных тоже.
Понимаю, что в связи с этим, настройкой пользоваться неудобно. Это потому что мы сделали лишь такую минимальную реализацию.
Скорее всего, достаточно выставить её в значение, в два раза меньше max_memory_usage.
- [Использование памяти при слиянии результатов распределенного запроса](https://groups.google.com/forum/#!topic/clickhouse/bvnqS_ecwU4)
```
<max_memory_usage>6000000000</max_memory_usage>
<max_bytes_before_external_group_by>3000000000</max_bytes_before_external_group_by>
<max_bytes_before_external_sort>3000000000</max_bytes_before_external_sort>
```
- [ClickHouse: New Open Source Columnar Database](https://www.percona.com/blog/2017/02/13/clickhouse-new-opensource-columnar-database/)
```
SET max_memory_usage = 128000000000; #128G
SET max_memory_usage = 128000000000; #128G
If you don’t have that much memory available, ClickHouse can “spill” data to disk by setting this:
set max_bytes_before_external_group_by=20000000000; #20G
set max_memory_usage=40000000000; #40G
set max_bytes_before_external_group_by=20000000000; #20G
set max_memory_usage=40000000000; #40G
```
According to the documentation, if you need to use max_bytes_before_external_group_by it is recommended to set max_memory_usage to be ~2x of the size of max_bytes_before_external_group_by

**Пробуем фиксить для себя**
```
set max_bytes_before_external_group_by=7000000000; #7G
set max_memory_usage=14000000000; #14G
set max_bytes_to_sort=7000000000
set max_bytes_before_external_sort=7000000000
пока не работает :(
```
## Подвал
a BETWEEN b AND c - равнозначно a >= b AND a <= c


URL http://10.0.0.238:10080
Логин: alex, Пароль qaz_wsx_123
Логин: a.tkachev, Пароль qwe_asd_1

# Запрос для определения размеров таблиц в КХ:
```
SELECT
    database,
    table,
    sum(rows) AS rows,
    formatReadableSize(sum(bytes + marks_size)) AS size
FROM system.parts
WHERE active
GROUP BY
    database,
    table
ORDER BY
    database ASC,
    table ASC
```

# Запрос для просмотра активных запросов