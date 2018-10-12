
- [PVSM: Рубрика «clickhouse»](http://www.pvsm.ru/cat/clickhouse)
- Примеры запросов с группировкой по времени: [пример 1](https://gist.github.com/alexey-milovidov/2dee968eb95df63b271208f89d3697c3); [пример 2](https://gist.github.com/alexey-milovidov/6fd9246ce44b48345bee3a0df3da5ab0)
- [ClickHouse: New Open Source Columnar Database](https://www.percona.com/blog/2017/02/13/clickhouse-new-opensource-columnar-database/)
- [ClickHouse monitoring with Zabbix](https://www.altinity.com/blog/2018/9/3/clickhouse-monitoring-zabbix)

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

## Вопрос первичного ключа
Возникло в ходе проектной проработки:
```
[18.07.2018 19:19:55] Alexander Tkachev: я пытался нарыть информацию по этим ключам, нашел полезного - https://medium.com/@f1yegor/clickhouse-primary-keys-2cf2a45d7324
и из телеграма:
Alexey Milovidov, [10.04.17 00:21]
Разница в порядке указания столбцов в первичном ключе есть и она очень важна. Данные в кусках сортируются лексикографически по первичному ключу. То есть, если ключ (a, b) - данные будут отсортированы по столбцу a. А для каждого множества строк с одинаковым значением столбца a - по столбцу b.

Alexey Milovidov, [10.04.17 00:23]
Если вы указали условие (равенство, неравенство, IN, комбинация логических связок от этих условий) на столбец a в WHERE - индекс позволит выбирать диапазоны в данных.

Если вы не указали условие на a, но указали только условие на b - индекс всё-равно может работать, но хуже и лишь при некоторых условиях - если в данных встречаются длинные диапазоны с одинаковыми значениями a - тогда в таких диапазонах ClickHouse сможет выбрать поддипазоны с нужными значениями b и пропустить остальные.
[18.07.2018 19:21:26] Владимир Панфилов: [18 июля 2018 г. 19:19] Alexander Tkachev: 

<<< если в данных встречаются длинные диапазоны с одинаковыми значениями a - тогда в таких диапазонах ClickHouse сможет выбрать поддипазоны с нужными значениями b и пропустить остальные.У нас как раз такой случай
[18.07.2018 19:22:44] Владимир Панфилов: После сортировки для каждого сегмента будет идти отсортированный список по всем типам событий
```

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

# Запрос для просмотра пространства имен БД и таблиц
См. [источник](https://clickhouse.yandex/docs/ru/operations/system_tables/)
`select distinct(database) from system.columns`
либо
`select * from system.tables`

# Дамп таблиц
- [Dump/Import data from clickhouse](https://groups.google.com/forum/#!topic/clickhouse/Dx0CsFGbk7c)
1. Dump of data:
`clickhouse-client --query="SELECT * FROM table FORMAT Native" > table.native`
Native is the most efficient format. 
CSV, TabSeparated, JSONEachRow are more portable: you may import/export data to another DBMS.
2. Dump of metadata:
`clickhouse-client --query="SHOW CREATE TABLE table" --format=TabSeparatedRaw > table.sql`
3. Restore of metadata:
`clickhouse-client < table.sql`
4. Restore of data:
`clickhouse-client --query="INSERT INTO table FORMAT Native" < table.native`
