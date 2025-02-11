# data.table
Философские рассуждения dplyr vs data.table:
	- COOL! [data.table vs dplyr: can one do something well the other can't or does poorly?](https://stackoverflow.com/questions/21435339/data-table-vs-dplyr-can-one-do-something-well-the-other-cant-or-does-poorly)
	- Hadley Wickham. [My take on dplyr vs data.table](https://twitter.com/hadleywickham/status/553169339751215104):
	- [dplyr on data.table, am I really using data.table?](https://stackoverflow.com/questions/27511604/dplyr-on-data-table-am-i-really-using-data-table/27520688)
- [data.table and parallel computing](https://stackoverflow.com/questions/14759905/data-table-and-parallel-computing/14763642#14763642)
- COOL! [Fast data lookups in R: dplyr vs data.table](https://appsilon.com/fast-data-lookups-in-r-dplyr-vs-data-table/)
- [Homepage Rdatatable/data.table](https://github.com/Rdatatable/data.table/wiki)
- COOL! [Advanced tips and tricks with data.table](http://brooksandrew.github.io/simpleblog/articles/advanced-data-table/)
- [Solve common R problems efficiently with data.table](https://jangorecki.github.io/blog/2015-12-11/Solve-common-R-problems-efficiently-with-data.table.html)
- [Understanding exactly when a data.table is a reference to (vs a copy of) another data.table](https://stackoverflow.com/questions/10225098/understanding-exactly-when-a-data-table-is-a-reference-to-vs-a-copy-of-another)
- [Apply function to dataframe in chunks](https://community.rstudio.com/t/apply-function-to-dataframe-in-chunks/9067)
- [fread() of file from archive](https://stackoverflow.com/questions/33341010/fread-of-file-from-archive)
- [Using `fread` to import csv file from an archive into `R` without extracting to disk](https://stackoverflow.com/questions/35644556/using-fread-to-import-csv-file-from-an-archive-into-r-without-extracting-to)
You can use such a kind of statements with fread.
`x = fread('unzip -q test/allRequests.csv.zip')`
Or with gunzip
`x = fread('gunzip -cq test/allRequests.csv.gz')`
- [Rename multiple dataframe columns, referenced by current names]|(https://stackoverflow.com/questions/9283171/rename-multiple-dataframe-columns-referenced-by-current-names). The `data.table` package has a `setnames()` function which changes column names by reference without copying the whole dataset.
- [duplicated: Determine Duplicate Rows](https://rdrr.io/rforge/data.table/man/duplicated.html) In data.table: Extension of data.frame
- [Two of my favorite data.table features](https://www.r-bloggers.com/two-of-my-favorite-data-table-features/). [Исходник](https://brandonlebeau.org/2014/01/06/two-of-my-favorite-data.table-features/):
	- Add aggregated variables to the raw data file
	- Removing duplicate observations
- [Solve common R problems efficiently with data.table](https://jangorecki.github.io/blog/2015-12-11/Solve-common-R-problems-efficiently-with-data.table.html). Written on 2015-12-11
- [R data.table change R names](https://stackoverflow.com/questions/18760287/r-data-table-change-r-names)
- Нюансы с кодировками. [robust encoding in fread (like 'fread("iconv -f ISO-8859-1 -t UTF-8 mytextfile.txt")')](https://github.com/Rdatatable/data.table/issues/1748). Ставим Latin1
`fread(path, encoding="Latin-1")`
- [Extracting unique rows from a data table in R {duplicate}](https://stackoverflow.com/questions/7562284/extracting-unique-rows-from-a-data-table-in-r)
- [Filtering out duplicated/non-unique rows in data.table](https://stackoverflow.com/questions/11792527/filtering-out-duplicated-non-unique-rows-in-data-table)
- COOL! [Benchmarking the six most used manipulations for data.tables in R](https://opremic.com/benchmarking-the-six-most-used-manipulations-for-data-tables-in-r/). Comparing formulations of the data.table package with base R and dplyr formulations
- [How to import a directory of csvs at once with base R and data.table. Can you guess which way is the fastest?](https://jozefhajnala.gitlab.io/r/r005-import-csvs/)
- [Convenience features of fread](https://github.com/Rdatatable/data.table/wiki/Convenience-features-of-fread)
- [Sort rows in data.table in decreasing order on string key `order(-x, v)` gives error on data.table 1.9.4 or earlier](https://stackoverflow.com/questions/12353820/sort-rows-in-data-table-in-decreasing-order-on-string-key-order-x-v-gives-er)
- COOL! [Fastest way to replace NAs in a large data.table](https://stackoverflow.com/questions/7235657/fastest-way-to-replace-nas-in-a-large-data-table)
- [Use data.table set() to convert all columns from integer to numeric](https://stackoverflow.com/questions/29790204/use-data-table-set-to-convert-all-columns-from-integer-to-numeric)
- [Advanced tips and tricks with data.table](http://brooksandrew.github.io/simpleblog/articles/advanced-data-table/)
- [data.table objects aren't updated in Rstudio environment panel](https://stackoverflow.com/questions/35921206/data-table-objects-arent-updated-in-rstudio-environment-panel)
- COOL! [Как посчитать ТОП N по группам](https://stackoverflow.com/questions/27766054/getting-the-top-values-by-group). см также https://stackoverflow.com/questions/20345022/convert-a-data-frame-to-a-data-table-without-copy
- [Data table fread with zip file in other directory with spaces in the name](https://stackoverflow.com/questions/50872108/data-table-fread-with-zip-file-in-other-directory-with-spaces-in-the-name)
- [Convenience features of fread](https://github.com/Rdatatable/data.table/wiki/Convenience-features-of-fread)
- COOL! Дирк перешел в наступление: [#15: Tidyverse and data.table, sitting side by side ... (Part 1)](http://dirk.eddelbuettel.com/blog/2018/01/21/#015_tidyverse_and_datatable_part_1)
- [query_if: One-to-one interface for data.table '[' method](https://rdrr.io/cran/maditr/man/query_if.html) In maditr: Pipe-Style Interface for 'data.table'
- [JOINing data in R using data.table](https://rstudio-pubs-static.s3.amazonaws.com/52230_5ae0d25125b544caab32f75f0360e775.html).  Ronald Stalder, 23-12-2014
- С различными бенчмарками! [omitting NA values with data.table](https://stackoverflow.com/questions/29928167/omitting-na-values-with-data-table)
- COOL! [What is the purpose of setting a key in data.table?](https://stackoverflow.com/questions/20039335/what-is-the-purpose-of-setting-a-key-in-data-table)
- [Access `by` variable from within `j` in data.table](https://stackoverflow.com/questions/21733151/access-by-variable-from-within-j-in-data-table)
- RIP Tutorial. [Using .SD and .SDcols](https://riptutorial.com/data-table/example/13084/using--sd-and--sdcols)
- Подменяем значения в определенных строках:
	- [How to change the last value in each group by reference, in data.table](https://stackoverflow.com/questions/21819253/how-to-change-the-last-value-in-each-group-by-reference-in-data-table)
- [Count number of records and generate row number within each group in a data.table](https://stackoverflow.com/questions/19869145/count-number-of-records-and-generate-row-number-within-each-group-in-a-data-tabl?rq=1).
`DT[ , `:=`( COUNT = .N , IDX = 1:.N ) , by = VAL ]`. Better `seq_len(.N)` instead `1:.N`
- Нюансы по слиянию таблиц. Получил в `inner_join` ошибку и стал разбираться
```
Error in vecseq(f__, len__, if (allow.cartesian || notjoin || !anyDuplicated(f__,  :
  Join results in 1595 rows; more than 1014 = nrow(x)+nrow(i). Check for duplicate key values in i each of which join to the same group in x over and over again. If that's ok, try by=.EACHI to run j for each group to avoid the large allocation. If you are sure you wish to proceed, rerun with allow.cartesian=TRUE. Otherwise, please search for this error message in the FAQ, Wiki, Stack Overflow and data.table issue tracker for advice.
```
	- [data.table: cartesian join and nomatch](https://stackoverflow.com/questions/48583006/data-table-cartesian-join-and-nomatch)
	- [Merge two data.tables](https://jangorecki.gitlab.io/data.cube/library/data.table/html/merge.html)
	- gist. [How to do joins with data.table](https://gist.github.com/nacnudus/ef3b22b79164bbf9c0ebafbf558f22a0)
	- [data.table cartesian join warning on legitimate join](https://stackoverflow.com/questions/27587287/data-table-cartesian-join-warning-on-legitimate-join):
```
Usually this was not intended and the join needs to be changed. The word 'cartesian' is used loosely in this context. The traditional cartesian join is (deliberately) difficult to achieve in data.table: where every row in i joins to every row in x (a nrow(x) * nrow(i) row result). 'cartesian' is just meant in a 'large multiplicative' sense.
```
- [Using 'on' style join with two different column names {#2383}](https://github.com/Rdatatable/data.table/issues/2383).
Sorry, you've misunderstood the documentation. Maybe the wording needs to be cleaned up.
The names of the vector passed to on must be column names in x, and the values must be columns in i: `d1[d2, on = c(A = "W")]`
You can also do `d1[d2, on = "A==W"]`
- [R Data Table - join but filter with update](https://stackoverflow.com/questions/46588340/r-data-table-join-but-filter-with-update)
- [Benchmarking the six most used manipulations for data.tables in R](https://opremic.com/benchmarking-the-six-most-used-manipulations-for-data-tables-in-r/)
- [R data.table Joins](https://medium.com/analytics-vidhya/r-data-table-joins-48f00b46ce29)

- [Find complement of a data frame (anti - join)](https://stackoverflow.com/questions/28702960/find-complement-of-a-data-frame-anti-join). Масса различных вариантов.
- А как сделать сэмплы по группам? Не все так просто
	- [Sample random rows within each group in a data.table](https://stackoverflow.com/questions/16289182/sample-random-rows-within-each-group-in-a-data-table)
	- [from data table, randomly select one row per group](https://stackoverflow.com/questions/33887083/from-data-table-randomly-select-one-row-per-group). 
Fast solution: `dt[dt[ , .I[sample(.N,1)] , by = z]$V1]`
- [Subset data frame based on number of rows per group](https://stackoverflow.com/questions/20204257/subset-data-frame-based-on-number-of-rows-per-group)
`dt[, if (.N \lq 3) .SD, by = name]` or `dt[dt[, .I[.N \lq 3], name]$V1]`

- Проблемки с кавычками внутри строк в delimited файле:
	- [fread: quotes in quoted string fields #1299 {Closed}](https://github.com/Rdatatable/data.table/issues/1299)
	- [fread should un-escape escaped quotes in fields #1109 {Open}](https://github.com/Rdatatable/data.table/issues/1109)
- [Split text string in a data.table columns](https://stackoverflow.com/questions/18154556/split-text-string-in-a-data-table-columns). Update: From version 1.9.6 (on CRAN as of Sep'15), we can use the function tstrsplit() to get the results directly (and in a much more efficient manner):
`dt[, c("PX", "PY") := tstrsplit(PREFIX, "_", fixed=TRUE)]`
	- [tstrsplit. Strsplit And Transpose The Resulting List Efficiently](https://www.rdocumentation.org/packages/data.table/versions/1.12.2/topics/tstrsplit)
- [data.table: transforming subset of columns with a function, row by row](https://stackoverflow.com/questions/36841942/data-table-transforming-subset-of-columns-with-a-function-row-by-row)
- [Row operations in data.table using `by = .I`](https://stackoverflow.com/questions/37667335/row-operations-in-data-table-using-by-i/37668187). Тут различные варианты и разбор таймингов. Без создания колонки -- `by = seq_len(NROW(dt))`. I tend to prefer `NROW`, because it also generalizes to vectors.
- [Advanced tips and tricks with data.table](http://brooksandrew.github.io/simpleblog/articles/advanced-data-table/)
- [Use equivalent of purrr:::map to iterate through data.table](https://stackoverflow.com/questions/47917614/use-equivalent-of-purrrmap-to-iterate-through-data-table)
- data.table joins
	- COOL! [Merging all column by reference in a data.table](https://stackoverflow.com/questions/45043600/merging-all-column-by-reference-in-a-data-table)
	- COOL! [Left join using data.table](https://stackoverflow.com/questions/34598139/left-join-using-data-table). If you want to add the b values of B to A, then it's best to join A with B and update A by reference as follows:
```
A[B, on = 'a', bb := i.b]
```
	- COOL! [How to do joins with data.table](https://gist.github.com/nacnudus/ef3b22b79164bbf9c0ebafbf558f22a0)
	- [Left join using data.table](https://stackoverflow.com/questions/34598139/left-join-using-data-table)
	- [JOINing data in R using data.table](https://rstudio-pubs-static.s3.amazonaws.com/52230_5ae0d25125b544caab32f75f0360e775.html) by Ronald Stalder
	- Тут иллюстрированный пример. [What does < stand for in data.table joins with on=](https://stackoverflow.com/questions/52793037/what-does-stand-for-in-data-table-joins-with-on)
	- COOL! [Notes on data.table in R](http://jeffmax.io/notes-on-datatable-in-r.html)
	- [Recode a variable using data.table](https://stackoverflow.com/questions/44590935/recode-a-variable-using-data-table)
	`DT[.(V1 = 1:2, to = 0:1), on = "V1", V1 := i.to]`
- [How to extract the first n rows per group?](https://stackoverflow.com/questions/16325641/how-to-extract-the-first-n-rows-per-group)
`DT[, .SD[1:2], by=date]` or `DT[DT[, .I[1:2], by = date]$V1]`
- COOL! Варианты с бенчмарками. [How to apply same function to every specified column in a data.table](https://stackoverflow.com/questions/16846380/how-to-apply-same-function-to-every-specified-column-in-a-data-table)
- [diff on data.table column](https://stackoverflow.com/questions/37141277/diff-on-data-table-column). We could use `shift()`:
```
dt[, diff := value - shift(value), by = variable]
```
- LOCF/NOCB. LOCF = "Last Observation Carried Forward". NOCB = "Next Observation Carried Backward".
- "Last Observation Carried Forward" = LOCF. "Next Observation Carried Backward" = NOCB.
- [Efficiently locf by groups in a single R data.table](https://stackoverflow.com/questions/37060211/efficiently-locf-by-groups-in-a-single-r-data-table/37068596)
- С бенчмарками [Remove rows conditionally from a data.table in R](https://stackoverflow.com/questions/22655060/remove-rows-conditionally-from-a-data-table-in-r)
	- [Efficiently remove rows #2890 {Closed}](https://github.com/Rdatatable/data.table/issues/2890)
- Целый квест. [Filtering out duplicated/non-unique rows in data.table](https://stackoverflow.com/questions/11792527/filtering-out-duplicated-non-unique-rows-in-data-table)
```
Maybe a new unique(..., use.key=FALSE) argument would help; now filed as FR#2483. – Matt Dowle Jan 18 '13 at 0:23
Hi @MatthewDowle. Yes, that would be a nice convenience. I think your comment in the FR is also correct--if the key is unique then use.key=FALSE could be ignored. – dnlbrky Jan 18 '13 at 14:12
1
data.table 1.9.6 (and not doubt earlier versions) has option by= which can be used to override the key. Setting by=NULL "uses all columns and acts like the analogous data.frame methods." – JWilliman Dec 1 '15 at 23:20
```
	- [Unique doesn't use keys as default anymore](https://stackoverflow.com/questions/42564617/unique-doesnt-use-keys-as-default-anymore)
- [Create new column in data.table by group](https://stackoverflow.com/questions/12620923/create-new-column-in-data-table-by-group)
- [Create a new column in a data.table from group by multiple columns](https://stackoverflow.com/questions/46134936/create-a-new-column-in-a-data-table-from-group-by-multiple-columns/46135033)
- performance различных способов сортировки [How to order data within subgroups in data.table R](https://stackoverflow.com/questions/28683712/how-to-order-data-within-subgroups-in-data-table-r)
- [fread from v.1.11.0+ no longer reads the .csv correctly, which was read perfectly in v.1.10.4-3 #2857 {Open}](https://github.com/Rdatatable/data.table/issues/2857)
- [How to create a lag variable within each group?](https://stackoverflow.com/questions/26291988/how-to-create-a-lag-variable-within-each-group)
From `data.table` versions >= v1.9.5, we can use `shift` with type as `lag` or `lead`. By default, the type is `lag`.
- [shift: Fast lead/lag for vectors and lists](https://rdrr.io/cran/data.table/man/shift.html)
- [Is my way of duplicating rows in data.table efficient?](https://stackoverflow.com/questions/8009900/is-my-way-of-duplicating-rows-in-data-table-efficient)
- COOL! Slides.[Introduction to `data.table` by Haema Nilakanta & Kim Ky](http://rpubs.com/kykimeng/intro-to-data-table)
- [How to select the first and last row within a grouping variable in a data frame?](https://stackoverflow.com/questions/8203818/how-to-select-the-first-and-last-row-within-a-grouping-variable-in-a-data-frame/8212756)
A fast and short data.table solution: `tmp[, .SD[c(1,.N)], by=id]`
- COOL! [Select first and last row from grouped data](https://stackoverflow.com/questions/31528981/select-first-and-last-row-from-grouped-data/31529043)
`df[ df[order(id, stopSequence), .I[c(1L,.N)], by=id]$V1 ]`
- [Why is `rbindlist` “better” than `rbind`?](https://stackoverflow.com/questions/15673550/why-is-rbindlist-better-than-rbind)
- [Remove rows with NA from data.table in R {duplicate}](https://stackoverflow.com/questions/28878005/remove-rows-with-na-from-data-table-in-r)
- Performance benchmark. [Remove rows with all or some NAs (missing values) in data.frame](https://stackoverflow.com/questions/4862178/remove-rows-with-all-or-some-nas-missing-values-in-data-frame).
If performance is a priority, use `data.table` and `na.omit()` with optional param `cols=`.
Краткая сводка по применению функций к группировке в `data.table`
	- [R data.table filtering on group size](https://stackoverflow.com/questions/34427383/r-data-table-filtering-on-group-size)
	- [add a 'having' parameter to `[.data.table` #788 {Open}](https://github.com/Rdatatable/data.table/issues/788)
	- [Further optimisation of `.SD` in `j` #735 {Open}](https://github.com/Rdatatable/data.table/issues/735)
	- [When should I use the `:=` operator in `data.table`?](https://stackoverflow.com/questions/7029944/when-should-i-use-the-operator-in-data-table)
```
DT["a", done := TRUE]   # binary search for group 'a' and set a flag
DT[, newcol := 42]      # add a new column by reference (no copy of existing data)
DT[, col := NULL]       # remove a column by reference
DT[, newcol := sum(v), by = group]  # like a fast transform() by group
```
	- [Advanced tips and tricks with `data.table`](http://brooksandrew.github.io/simpleblog/articles/advanced-data-table/) BY ANDREW BROOKS
data.table
- COOL! [How to efficiently calculate multiple quantiles of column z when grouping by columns (x, y)](https://stackoverflow.com/questions/47702018/how-to-efficiently-calculate-multiple-quantiles-of-column-z-when-grouping-by-col)
```
system.time(
  result2b <- dt[, {
      the_quantiles = quantile(z, c(0.5, 0.75, 0.9))
      list(
        firstval = first(z),
        q1 = the_quantiles[1],
        q2 = the_quantiles[2],
        q3 = the_quantiles[3]
      )
    }, keyby=list(x, y)]
)
```
- [An alternative to mutate_if in data.table](https://stackoverflow.com/questions/56995839/an-alternative-to-mutate-if-in-data-table/56996168)
- [.EACHI in data.table?](https://stackoverflow.com/questions/27004002/eachi-in-data-table/27004566#27004566)
- [How to apply same function to every specified column in a data.table](https://stackoverflow.com/questions/16846380/how-t	o-apply-same-function-to-every-specified-column-in-a-data-table)
- [How to exclude one column from data.table OR convert to data.table to MTS](https://stackoverflow.com/questions/12046079/how-to-exclude-one-column-from-data-table-or-convert-to-data-table-to-mts)
- [How do I exclude columns from a data.table?](https://stackoverflow.com/questions/37210489/how-do-i-exclude-columns-from-a-data-table)
Also, in case you would not wish to change the data.table, but merely return the columns except some columns, you can do:
```
dt[, .SD, .SDcols = !c('b', 'c')]
```
- [Select subset of columns in data.table R {duplicate}](https://stackoverflow.com/questions/28094645/select-subset-of-columns-in-data-table-r). You can do `dt[, !c("V1","V2","V3","V5")]` to get anti-select.
- COOL! [A data.table and dplyr tour](https://atrebas.github.io/post/2019-03-03-datatable-dplyr/) Written by Atrebas on March 3, 2019
- [R : DATA.TABLE TUTORIAL (WITH 50 EXAMPLES)](https://www.listendata.com/2016/10/r-data-table.html)
- COOL! [Using .I to return row numbers with data.table package](https://stackoverflow.com/questions/22408306/using-i-to-return-row-numbers-with-data-table-package)
- data.table subsetting
	- [deprecate programming interfaces: get, mget, eval #5886 {Open}](https://github.com/Rdatatable/data.table/issues/5886)
	- [What's the fastest way to subset a data.table?](https://stackoverflow.com/questions/23755839/whats-the-fastest-way-to-subset-a-data-table)
	- [Use variable in i of data.table subset](https://stackoverflow.com/questions/25663877/use-variable-in-i-of-data-table-subset)
	- [When column name is name of variable get(variable) generates an error and eval(variable) returnes the incorrect values #4878 {Open}](https://github.com/Rdatatable/data.table/issues/4878)
	- [data.table in r: subset using column index](https://stackoverflow.com/questions/41112658/data-table-in-r-subset-using-column-index).
	- [Subsetting data.table using variables with same name as column](https://stackoverflow.com/questions/21658893/subsetting-data-table-using-variables-with-same-name-as-column?noredirect=1&lq=1)
We can get the row index with `.I` and use that to subset the `DT`
```
DT[DT[, .I[.SD == 2], .SDcols = 1]]
```
- [Fill in missing values (nacof/nocb) in character column by group](https://stackoverflow.com/questions/61522683/fill-in-missing-values-nacof-nocb-in-character-column-by-group)
- [R: data table group by column name vector](https://stackoverflow.com/questions/45410338/r-data-table-group-by-column-name-vector)
You were almost there: `dt[, .(Count = .N, Avg = mean(get(metric))), mget(nodes)]` 
- COOL! [How to change the last value in each group by reference, in data.table](https://stackoverflow.com/questions/21819253/how-to-change-the-last-value-in-each-group-by-reference-in-data-table)
- [row number with by in data.table](https://stackoverflow.com/questions/49032276/row-number-with-by-in-data-table)
- COOL! [.SDcols=function shorthand #3950 {Closed}](https://github.com/Rdatatable/data.table/issues/3950). `data.table v1.13.0 (24 Jul 2020)`. .SDcols=is.numeric now works; i.e., SDcols= accepts a function which is used to select the columns of .SD
- [.SDcols accepts a function to filter on values #3991 {Merged}](https://github.com/Rdatatable/data.table/pull/3991)
- [Making .SD your best friend](https://rpubs.com/josemz/SDbf)
- [Filter by column index number data.table R](https://stackoverflow.com/questions/67331129/filter-by-column-index-number-data-table-r)
- [What is the equivalent of mutate_at (dplyr) in data.table?](https://stackoverflow.com/questions/57386580/what-is-the-equivalent-of-mutate-at-dplyr-in-data-table)



- [Data.Table – everything you need to know to get you started in R](https://hutsons-hacks.info/data-table-everything-you-need-to-know-to-get-you-started-in-r)
- [Merging with data.table](https://jmsallan.netlify.app/blog/merging-with-data-table/)
- [Find consecutive integers in a window of an array greater than threshold value group-wise in R](https://stackoverflow.com/questions/67571523/find-consecutive-integers-in-a-window-of-an-array-greater-than-threshold-value-g)
- COOL! под отметкой Мэта: [A gentle introduction to data.table](https://atrebas.github.io/post/2020-06-17-datatable-introduction/)
- [Verbose data.table and uncovering hidden cedta's data table awareness decisions](https://jozef.io/r911-datatable-cedta/)
- [Tidyverse and data.table, sitting side by side… and then base R walks in](https://www.enchufa2.es/archives/tidyverse-and-data-table-sitting-side-by-side-and-then-base-r-walks-in.html)
- COOL! [How do I exclude columns from a data.table?](https://stackoverflow.com/questions/37210489/how-do-i-exclude-columns-from-a-data-table?rq=1)
- [Introduction to data.table](http://rpubs.com/kykimeng/intro-to-data-table) by Haema Nilakanta & Kim Ky
- 2019.11 [Database-like ops benchmark](https://h2oai.github.io/db-benchmark/)
- andrew brooks. [Advanced tips and tricks with data.table](http://brooksandrew.github.io/simpleblog/articles/advanced-data-table/)
- COOL! Learning. [A data.table and dplyr tour](https://atrebas.github.io/post/2019-03-03-datatable-dplyr/) Written by Atrebas on March 3, 2019
- [data.table pkgdown](https://rdatatable.gitlab.io/data.table/) provides a high-performance version of base R’s data.frame with syntax and feature enhancements for ease of use, convenience and programming speed.
- [Using .SD for Data Analysis](https://rdatatable.gitlab.io/data.table/articles/datatable-sd-usage.html). 2019-11-20
- [Start using data.table - 9th July 2019](https://github.com/moj-analytical-services/coffee-and-coding-public/tree/master/2019-07-09%20Start%20using%20datatable)
- [data.table := assignments when variable has same name as a column](https://stackoverflow.com/questions/32738499/data-table-assignments-when-variable-has-same-name-as-a-column)
- [datatable (:=) column name is the same as global environment value {duplicate}](https://stackoverflow.com/questions/48256904/datatable-column-name-is-the-same-as-global-environment-value)
- [data.table - subsetting based on variable whose name is a column, too](https://stackoverflow.com/questions/40641629/data-table-subsetting-based-on-variable-whose-name-is-a-column-too/40641717)
- Тут с бенчмарками. [Keyed lookup on data.table without 'with'](https://stackoverflow.com/questions/15102068/keyed-lookup-on-data-table-without-with)
- [Subsetting data.table using variables with same name as column](https://stackoverflow.com/questions/21658893/subsetting-data-table-using-variables-with-same-name-as-column)

- [R data.table symbols and operators you should know](https://www.infoworld.com/article/3530348/r-datatable-symbols-and-operators-you-should-know.html)
Then this code will not work: 
```
dt1 <- mydt[, mycols]
```
Instead, you need to put `..` (that’s two dots) in front of the vector object name:
```
dt1 <- mydt[, ..mycols]
```
Why two dots? That seemed kind of random to me until I read the explanation. Think of it like the two dots in a Unix command-line terminal that move you up one directory. Here, you’re moving up one namespace, from the environment inside data.table brackets up to the global environment. (That really does help me remember it!)
- [data.table double dot.](https://cran.r-project.org/web/packages/data.table/data.table.pdf)
When j is a character vector of column names, a numeric vector of column positions to select or of the form startcol:endcol, and the value returned is always
a `data.table`. `with=FALSE` is not necessary anymore to select columns dynamically. Note that `x[,cols]` is equivalent to `x[,..cols]` and to `x[,cols,with=FALSE]` and to `x[,.SD,.SDcols=cols]`.
- [Why does “..” work to pass column names in a character vector variable?](https://stackoverflow.com/questions/45380628/why-does-work-to-pass-column-names-in-a-character-vector-variable)
- [Distinguishing between an external variable and a column in a data table {duplicate}](https://stackoverflow.com/questions/50711849/distinguishing-between-an-external-variable-and-a-column-in-a-data-table)
How do I get the following code to recognize the second a in `dt[a == a,]` as an external variable with value `3`?
- [data.table `:=` assignments when variable has same name as a column](https://stackoverflow.com/questions/32738499/data-table-assignments-when-variable-has-same-name-as-a-column)
`dt1[1, a := get("a", envir = .GlobalEnv)]` or use `..`
- [When column name is name of variable get(variable) generates an error and eval(variable) returnes the incorrect values #4878 {Open}](https://github.com/Rdatatable/data.table/issues/4878)
- [deprecate programming interfaces: get, mget, eval #5886 {Open}](https://github.com/Rdatatable/data.table/issues/5886)
- [Select subset of columns in data.table R {duplicate}](https://stackoverflow.com/questions/28094645/select-subset-of-columns-in-data-table-r/28094726#28094726)
- [How to expand an ellipsis (…) argument without evaluating it in R](https://stackoverflow.com/questions/13353847/how-to-expand-an-ellipsis-argument-without-evaluating-it-in-r)
- [Data.Table – everything you need to know to get you started in R](https://hutsons-hacks.info/data-table-everything-you-need-to-know-to-get-you-started-in-r)
- По мотивам рефакторига кода Гипросвязи. Аналоги `tidyr::separate_rows`:
	- [Splitting a single column into multiple observation using R](https://stackoverflow.com/questions/33113263/splitting-a-single-column-into-multiple-observation-using-r)
	- [split column in data.table to multiple rows {duplicate}](https://stackoverflow.com/questions/34712949/split-column-in-data-table-to-multiple-rows)
	- Прекрасный анализ различных подходов, проведение бенчмарка. [Split comma-separated strings in a column into separate rows](https://stackoverflow.com/questions/13773770/split-comma-separated-strings-in-a-column-into-separate-rows)
- [data.table::setcolorder. Fast column reordering of a data.table by reference](http://search.r-project.org/library/data.table/html/setcolorder.html)
- И опять! COOL! [Advanced tips and tricks with data.table](http://brooksandrew.github.io/simpleblog/articles/advanced-data-table/#fast-looping-with-set)
- [Using variable in data.table group by clause](https://stackoverflow.com/questions/31600666/using-variable-in-data-table-group-by-clause)
- [Summarise data.table when “by” grouping variables stored as vector of strings {duplicate}](https://stackoverflow.com/questions/62601509/summarise-data-table-when-by-grouping-variables-stored-as-vector-of-strings). !! Instead of `.(`, here we can use `c(`
- [Use a character vector in the `by` argument](https://stackoverflow.com/questions/48442422/use-a-character-vector-in-the-by-argument).
```
From ?data.table in the by section it says that by accepts:
  - a single character string containing comma separated column names (where spaces are significant since column names may contain spaces
even at the start or end): e.g., DT[, sum(a), by="x,y,z"]
  - a character vector of column names: e.g., DT[, sum(a), by=c("x", "y")]
```
- [реализация точечной функции `. ()` в пакете data.table](https://issue.life/questions/52312977)
- аналог unnest в `data.table`:
```
    # https://stackoverflow.com/questions/44336733/how-to-unlist-a-column-in-a-data-table
    .[, .(close_basket_uid = unlist(close_basket_uid)), by = setdiff(names(.), 'close_basket_uid')] %>%
```
- [How to 'unlist' a column in a data.table](https://stackoverflow.com/questions/44336733/how-to-unlist-a-column-in-a-data-table)
- COOL! [Fast concatenation of data.table columns into one string column](https://stackoverflow.com/questions/48233309/fast-concatenation-of-data-table-columns-into-one-string-column)
- [data.table vs. dplyr und dtplyr: Benchmarks](https://statistik-dresden.de/archives/16275)
- [data.table: Using .SD and .SDcols](https://riptutorial.com/data-table/example/13084/using--sd-and--sdcols)
- [How to pass all columns except one as argument to setkey()?](https://stackoverflow.com/questions/29368785/how-to-pass-all-columns-except-one-as-argument-to-setkey)
- [data.table - group by all except one column](https://stackoverflow.com/questions/32440399/data-table-group-by-all-except-one-column)
- [Data cleaning and exploration with data.table](https://www.meganstodel.com/posts/using-data-table/)
- [data.table NEWS](https://cran.rstudio.com/web/packages/data.table/news/news.html) or [here](https://github.com/Rdatatable/data.table/blob/master/NEWS.md)
- Warning в MacOS при сборке data.table. [ld: warning: text-based stub file are out of sync. Falling back to library file for linking](https://stackoverflow.com/questions/51314888/ld-warning-text-based-stub-file-are-out-of-sync-falling-back-to-library-file/55344565)
- [List-columns in data.table: Reducing the cognitive & computational burden of complex data](https://rstudio.com/resources/rstudioconf-2020/list-columns-in-data-table-reducing-the-cognitive-computational-burden-of-complex-data/)
- COOL! [Adding new columns to a data.table by-reference within a function not always working](https://stackoverflow.com/questions/28078640/adding-new-columns-to-a-data-table-by-reference-within-a-function-not-always-wor)
Q: Is this a pointer issue ala this issue, like serializing a data.table destroys the over-allocated pointers?
A: Yes loading from disk sets the external pointer to NULL. We will have to over-allocate again.
Q: Is there a simple way to restore them?
A: Yes. You can test for `truelength()` of the `data.table`, and if it's 0, then use `setDT()` or `alloc.col()` on it.
- [between vs inrange in data.table](https://stackoverflow.com/questions/42633033/between-vs-inrange-in-data-table)
- COOL! andrew brooks. [Advanced tips and tricks with data.table](http://brooksandrew.github.io/simpleblog/articles/advanced-data-table/#fast-looping-with-set)
- COOL! [data.table in R – The Complete Beginners Guide](https://www.machinelearningplus.com/data-manipulation/datatable-in-r-complete-guide/), by Selva Prabhakaran | Posted on November 13, 2019
- [Delete rows by reference {#635} Open](https://github.com/Rdatatable/data.table/issues/635)
- list-columns
	- [Tyson S. Barrett - List-columns in data.table. Nesting and unnesting data tables and vectors](https://osf.io/f6pxw/download)
	- [TysonStanley/tidyfast](https://github.com/TysonStanley/tidyfast). Fast and efficient alternatives to tidyr functions built on data.table https://tysonbarrett.com/tidyfast/
	- [(Much) faster unnesting with data.table](https://www.johannesbgruber.eu/post/a-faster-unnest/)
	- [How to ungroup list columns in data.table?](https://stackoverflow.com/questions/34692260/how-to-ungroup-list-columns-in-data-table)
	- [Unnest a list column directly into several columns](https://stackoverflow.com/questions/49689927/unnest-a-list-column-directly-into-several-columns)
- [What is the equivalent of mutate_at (dplyr) in data.table?](https://stackoverflow.com/questions/57386580/what-is-the-equivalent-of-mutate-at-dplyr-in-data-table)
- Сообщение "Coercing 'list' RHS to 'character' to match the type of the target column." [How to change type of target column when doing := by group in a data.table in R?](https://stackoverflow.com/questions/29643820/how-to-change-type-of-target-column-when-doing-by-group-in-a-data-table-in-r)
- [Programming with data.table](https://johnmackintosh.com/2020-01-27-flexible-datatable-functions/). getting started multiple bare variable names in data.table functions
- [data.table: Rolling functions](https://rdatatable.gitlab.io/data.table/reference/froll.html). Fast rolling functions to calculate aggregates on sliding window. Function name and arguments are experimental.
- [data.table and parallel computing](https://stackoverflow.com/questions/14759905/data-table-and-parallel-computing)
- [data.table's `cube` function](https://pavolini.net/2019/07/19/data-table-s-cube-function/)
- [Merge dataframes on timestamps and time intervals using data.table in R](https://codereview.stackexchange.com/questions/224705/merge-dataframes-on-timestamps-and-time-intervals-using-data-table-in-r)
- data.table, разбиение на колонки (CREP). Если на выходе NULL, то получаем такую ошибку
```
Error in `[.data.table`(dt, event_id == "1001", `:=`(c("ProtocolID", "ProtocolVer",  :
  Supplied 12 columns to be assigned an empty list (which may be an empty data.table or data.frame since they are lists too). To delete multiple columns use NULL instead. To add multiple empty list columns, use list(list()).
```
- [data.table and error handling using try statement](https://stackoverflow.com/questions/21084624/data-table-and-error-handling-using-try-statement)
- [Advanced tips and tricks with data.table. Assign a column with := named with a character object](http://brooksandrew.github.io/simpleblog/articles/advanced-data-table/#create-multiple-columns-with--in-one-statement)
- [Use of lapply .SD in data.table R](https://stackoverflow.com/questions/32276887/use-of-lapply-sd-in-data-table-r)
- [data.table. Using .SD and .SDcols](https://riptutorial.com/data-table/example/13084/using--sd-and--sdcols)
- [Extract a column from a data.table as a vector, by position](https://stackoverflow.com/questions/20043313/extract-a-column-from-a-data-table-as-a-vector-by-position)
- [Why do DT[ , 5] and DT[2, 5] return a 1-column data.table rather than vectors like data.frame?](https://cran.r-project.org/web/packages/data.table/vignettes/datatable-faq.html#j-num)
- [R: How to get a single element in data.table](https://stackoverflow.com/questions/21872262/r-how-to-get-a-single-element-in-data-table)
- [setNames vs. setnames in R (+ Examples) | stats & data.table Package](https://statisticsglobe.com/setnames-r-function-example)
- COOL! [How to efficiently calculate multiple quantiles of column z when grouping by columns (x, y)](https://stackoverflow.com/questions/47702018/how-to-efficiently-calculate-multiple-quantiles-of-column-z-when-grouping-by-col)
- [R data.table memory efficient rbindlist](https://stackoverflow.com/questions/47163028/r-data-table-memory-efficient-rbindlist)
- [Speed comparison of rbind, bind_rows, and  rbindlist](https://rstudio-pubs-static.s3.amazonaws.com/406521_7fc7b6c1dc374e9b8860e15a699d8bb0.html)
- COOL! [rbindlist data.tables with different number of columns](https://stackoverflow.com/questions/19584039/rbindlist-data-tables-with-different-number-of-columns)
This feature is now implemented in commit 1266 of v1.9.3. From NEWS:
- [data.table and parallel computing](https://stackoverflow.com/questions/14759905/data-table-and-parallel-computing)
- [Material of Introduction to large data management using R!](https://rstudio-pubs-static.s3.amazonaws.com/106515_13ffe11bf5f745cb9bf59cd35307795a.html)
- [Efficient reshaping using data.tables](https://cran.r-project.org/web/packages/data.table/vignettes/datatable-reshape.html)
- [chmatch: Faster match of character vectors](https://rdrr.io/rforge/data.table/man/chmatch.html)
- [Fastest way to replace NAs in a large data.table](https://stackoverflow.com/questions/7235657/fastest-way-to-replace-nas-in-a-large-data-table)
```
f_dowle3 = function(DT) {
  for (j in seq_len(ncol(DT)))
    set(DT,which(is.na(DT[[j]])),j,0)
}
```
- [na.omit.data.table: Remove rows with missing values on columns specified](https://rdrr.io/cran/data.table/man/na.omit.data.table.html)
- [Introduction to data.table](http://rpubs.com/kykimeng/intro-to-data-table)
- COOL! [Why I love `data.table`](https://eliocamp.github.io/codigo-r/en/2019/07/why-i-love-data-table/)
- COOL! [My Favorite data.table Feature](http://www.win-vector.com/blog/2019/06/my-favorite-data-table-feature/)
- [data.table is Much Better Than You Have Been Told](http://www.win-vector.com/blog/2019/06/data-table-is-much-better-than-you-have-been-told/)
- [split column in data.table to multiple rows {duplicate}](https://stackoverflow.com/questions/34712949/split-column-in-data-table-to-multiple-rows)
- [mrdwab/splitstackshape](https://github.com/mrdwab/splitstackshape) R functions to split concatenated data, conveniently stack columns of data.frames, and conveniently reshape data.frames.
- [Improving performance of appending rows to a data.table](https://stackoverflow.com/questions/30977355/improving-performance-of-appending-rows-to-a-data-table)
- COOL! [Compare data.table pipes and magrittr pipes](https://www.gl-li.com/2017/07/25/compare-data.table-pipes-and-magrittr-pipes/)
- [How to build a pipeline from data.table to magrittr and back to data.table](https://stackoverflow.com/questions/28920623/how-to-build-a-pipeline-from-data-table-to-magrittr-and-back-to-data-table)
- [gdemin/maditr](https://github.com/gdemin/maditr). Pipe-Style Interface for 'data.table'
- [Using data.table with magrittr pipes: best of both worlds](https://martinctc.github.io/blog/using-data.table-with-magrittr-pipes-best-of-both-worlds/)
```
# Use data.table syntax
flights_tb %>%
  .[, carrier_flight := paste0(carrier,"_",flight)] %>%
  .[,.(dep_delay = mean(dep_delay, na.rm = TRUE),
       arr_delay = mean(arr_delay, na.rm = TRUE)), by = carrier_flight] %>%
  dplyr::as_tibble() # Convert this back to a tibble (tidyverse) object
```
- COOL! [Creating blazing fast pivot tables from R with data.table - now with subtotals using grouping sets](https://jozefhajnala.gitlab.io/r/r912-datatable-grouping-sets/)
- [Verbose data.table and uncovering hidden cedta's data table awareness decisions](https://jozefhajnala.gitlab.io/r/r911-datatable-cedta/)
- [Convert a data frame to a data.table without copy](https://stackoverflow.com/questions/20345022/convert-a-data-frame-to-a-data-table-without-copy)
- COOL! С кучей полезных бенчмарков [Getting the top values by group](https://stackoverflow.com/questions/27766054/getting-the-top-values-by-group)
- [saghirb/R-datatable-Intro](https://github.com/saghirb/R-datatable-Intro). Workshop Materials: Introduction to R concepts and the data.table package - a tinyverse approach
- [Summarize data.table by group](https://stackoverflow.com/questions/36526141/summarize-data-table-by-group)
- COOL! [When should I use setDT() instead of data.table() to create a data.table?](https://stackoverflow.com/questions/41917887/when-should-i-use-setdt-instead-of-data-table-to-create-a-data-table)
- [R - slow performance in creating lots of data.table objects](https://stackoverflow.com/questions/28203809/r-slow-performance-in-creating-lots-of-data-table-objects)
- [names(dt) issue](https://github.com/Rdatatable/data.table/issues/5079) When we store the column names on to a variable, e.g., DT_n = names(DT), and then add/update/delete column(s) by reference. It would also modify DT_n, unless we do copy(names(DT)). https://cloud.r-project.org/web/packages/data.table/vignettes/datatable-reference-semantics.html
- COOL! [Understanding exactly when a data.table is a reference to (vs a copy of) another data.table](https://stackoverflow.com/questions/10225098/understanding-exactly-when-a-data-table-is-a-reference-to-vs-a-copy-of-another)
- COOL! [Should nafill replace NaN values? #4020 {Closed}](https://github.com/Rdatatable/data.table/issues/4020). Решено положительно в [nafill gains nan argument #4025](https://github.com/Rdatatable/data.table/pull/4025)
- [Simultaneous order, row-filter and column-select with data.table](https://stackoverflow.com/questions/30606395/simultaneous-order-row-filter-and-column-select-with-data-table)
- [select data.table R rows based on row number and condition](https://stackoverflow.com/questions/39422316/select-data-table-r-rows-based-on-row-number-and-condition)
- [Using `names(obj) <- names(dt)` could be problematic (#5079)](https://github.com/Rdatatable/data.table/issues/5079#issuecomment-901981788).
Ноги растут из [`data.table` reference semantic](https://cloud.r-project.org/web/packages/data.table/vignettes/datatable-reference-semantics.html)
When we store the column names on to a variable, e.g., DT_n = names(DT), and then add/update/delete column(s) by reference. It would also modify DT_n, unless we do copy(names(DT)).
- COOL! [Fast way to replace all blanks with `NA` in R `data.table`](https://stackoverflow.com/questions/31516192/fast-way-to-replace-all-blanks-with-na-in-r-data-table)
- [Binding list of data.tables by columns, and by reference](https://stackoverflow.com/questions/48333523/binding-list-of-data-tables-by-columns-and-by-reference)
`setDT(unlist(L, recursive = FALSE), check.names = TRUE)`
- Проблема с передачей `:=` в пакеты. Выплыло из вопроса Константина Казарина:
```
 webshot2::rmdshot("./support/quarto/data_table_in_qmd.qmd", file = "tst.png")

 При вызове генератора из командной строки получаем ошибку
 Error in `:=`(value, gear + carb) : 
   Check that is.data.table(DT) == TRUE. Otherwise, := and `:=`(...) are defined for use in j, once only and in particular ways. See help(":=").
```
	- [Using data.table package inside my own package](https://stackoverflow.com/questions/10527072/using-data-table-package-inside-my-own-package/10529888#10529888)
	- [R data.table ':=' works in direct call, but same function in a package fails](https://stackoverflow.com/questions/27980835/r-data-table-works-in-direct-call-but-same-function-in-a-package-fails)
	- [Importing data.table](https://cran.r-project.org/web/packages/data.table/vignettes/datatable-importing.html)
- [How to pretty print data tables using the same pretty printing of tibbles?](https://stackoverflow.com/questions/68738066/how-to-pretty-print-data-tables-using-the-same-pretty-printing-of-tibbles)
- Проблемы с `future`. [Issue with indexing data.tables passed to future_map_* #182 {Closed}](https://github.com/DavisVaughan/furrr/issues/182). Обсуждали [здесь](https://t.me/rlang_ru/130615)
- [How to create an empty datatable with columns names and then append datatables to it?](https://stackoverflow.com/questions/37376398/how-to-create-an-empty-datatable-with-columns-names-and-then-append-datatables-t)
	- [How to create a list with names but no entries in R/Splus?](https://stackoverflow.com/questions/5688020/how-to-create-a-list-with-names-but-no-entries-in-r-splus)
	- [Create an Empty List of Specific Length in R](https://www.tutorialkart.com/r-tutorial/r-create-empty-list-of-specific-length/#gsc.tab=0)
- Набор бенчмарков включен. [Apply a function to every specified column in a data.table and update by reference](https://stackoverflow.com/questions/16846380/apply-a-function-to-every-specified-column-in-a-data-table-and-update-by-referen)
- [Unveiling the Magic of dcast Function in R’s data.table Package](https://www.spsanderson.com/steveondata/posts/2024-02-26/index.html)

## data.table tech
- [Warning: 'Invalid .internal.selfref detected' when adding a column to a data.table returned from a function](https://stackoverflow.com/questions/20687235/warning-invalid-internal-selfref-detected-when-adding-a-column-to-a-data-tab). To understand how data.table detects copies using .internal.selfref, we'll dive into some history of data.table.
`data.table:::selfrefok(DT)`

## data.table joins
- COOL! [R data.table: update-by-reference joins](https://r-critique.com/r_datatable_update_by_reference_joins)
- [nacnudus/data.table-joins.R](https://gist.github.com/nacnudus/ef3b22b79164bbf9c0ebafbf558f22a0) How to do joins with data.table
- [How to join (merge) data frames (inner, outer, left, right)?](https://jangorecki.github.io/blog/2015-12-11/Solve-common-R-problems-efficiently-with-data.table.html)
- [Merging with data.table](https://jmsallan.netlify.app/blog/merging-with-data-table/)
- [R data.table Joins](https://medium.com/analytics-vidhya/r-data-table-joins-48f00b46ce29)
- [R Tutorial: Data.Table](https://www.dezyre.com/data-science-in-r-programming-tutorial/r-data-table-tutorial)
- [R – Data.Table Rolling Joins](https://gormanalysis.com/r-data-table-rolling-joins/)
- COOL! [Understanding data.table Rolling Joins](https://r-norberg.blogspot.com/2016/06/understanding-datatable-rolling-joins.html)
- [R – Data.Table Rolling Joins](https://www.gormanalysis.com/blog/r-data-table-rolling-joins/). July 26, 2014. R tutorial
	- Архив: [R – Data.Table Rolling Joins](https://web.archive.org/web/20230607163717/https://www.gormanalysis.com/blog/r-data-table-rolling-joins/)
- COOL! Тут есть про rolling join тоже. [Introduction to data.table](https://rpubs.com/kykimeng/intro-to-data-table) by Haema Nilakanta & Kim Ky
	- Slides [Introduction to data.table](https://kykimeng.com/slides/rnorth_data_table.html#1)
- [non-equi merge in data.table and epidemiology](https://scitilab.com/post_data/non_equi_joins/2020_11_17_non_equi_merge/)
- COOL! [The unequalled joy of non-equi joins](https://selbydavid.com/2021/02/13/joins/)
- [How does one do a full join using data.table?](https://stackoverflow.com/questions/15170741/how-does-one-do-a-full-join-using-data-table)
- [.EACHI in data.table?](https://stackoverflow.com/questions/27004002/eachi-in-data-table).
	- Продолжение [How to count occurrences combinations in data.table in R](https://stackoverflow.com/questions/25869543/how-to-count-occurrences-combinations-in-data-table-in-r/25872206#25872206)
- COOL! детальный анализ производительности join решений в data.table. [How to apply same function to every specified column in a data.table](https://stackoverflow.com/questions/16846380/how-to-apply-same-function-to-every-specified-column-in-a-data-table). 
```cols2 <- c("reg_date", "delreq_date"); .[ , (cols2) := lapply(.SD, anytime::anydate), .SDcols = cols2]```
	- use `mget`. [Replace specific values based on another dataframe](https://stackoverflow.com/a/37994369/2204410). `DF1[DF2, on = .(date, id), names(DF2)[3:4] := mget(paste0("i.", names(DF2)[3:4]))]`
- Здесь про join в data.table: [Enhanced data.frame](https://rdatatable.gitlab.io/data.table/reference/data.table.html)
Навеяно темой антиджойнов
- COOL! [Why does X\[Y\] join of data.tables not allow a full outer join, or a left join?](https://stackoverflow.com/questions/12773822/why-does-xy-join-of-data-tables-not-allow-a-full-outer-join-or-a-left-join)
- [How does one do a full join using data.table?](https://stackoverflow.com/questions/15170741/how-does-one-do-a-full-join-using-data-table)
- [Getting started with data.table](https://riptutorial.com/data-table)
- Подробное объяснение синтаксиса `[`. [data.table Details](https://rdatatable.gitlab.io/data.table/reference/data.table.html).
The way to read this out loud is: "Take DT, subset rows by i, then compute j grouped by by. Here are some basic usage examples expanding on this definition. See the vignette (and examples) for working examples.
- Jan Gorecki blog [Solve common R problems efficiently with data.table](https://jangorecki.github.io/blog/2015-12-11/Solve-common-R-problems-efficiently-with-data.table.html)
```
    # right outer join keyed data.tables
    dt1[dt2]
    # right outer join unkeyed data.tables - use `on` argument
    dt1[dt2, on = "CustomerId"]
    # left outer join - swap dt1 with dt2
    dt2[dt1, on = "CustomerId"]
    # inner join - use `nomatch` argument
    dt1[dt2, nomatch=0L, on = "CustomerId"]
    # anti join - use `!` operator
    dt1[!dt2, on = "CustomerId"]
    # inner join
    merge(dt1, dt2, by = "CustomerId")
    # full outer join
    merge(dt1, dt2, by = "CustomerId", all = TRUE)
    # see ?merge.data.table arguments for other cases
```
- [Join data.tables in R – Inner, Outer, Left & Right (4 Examples)](https://statisticsglobe.com/join-data-tables-r-inner-outer-left-right)
- [Joining verbs for data.table](https://cran.r-project.org/web/packages/table.express/vignettes/joins.html)
- [JOINing data in R using data.table](https://rstudio-pubs-static.s3.amazonaws.com/52230_5ae0d25125b544caab32f75f0360e775.html)
- [How to perform merges (joins) on two or more data frames with base R, tidyverse and data.table](https://jozef.io/r006-merge/)
- [Left join using data.table](https://stackoverflow.com/questions/34598139/left-join-using-data-table)
- [Finding Overlaps between interval sets / Efficient Overlap Joins](https://stackoverflow.com/questions/25815032/finding-overlaps-between-interval-sets-efficient-overlap-joins)
- COOL! 2014.09 New feature - [Overlapping range joins for Genomics by Arun Srinivasan](2014.09 New feature - Overlapping range joins for Genomics by Arun Srinivasan, history and benchmarks by Matt Dowle and four hour workshop, EARL Conference London [agenda] [ TO DO - link to video ]), history and benchmarks by Matt Dowle and four hour workshop, EARL Conference London
- COOL! [Overlap joins in R: a speed comparison with packages sqldf and data.table](https://www.zevross.com/blog/2015/07/09/overlap-joins-in-r-a-speed-comparison-with-packages-sqldf-and-data-table-3/)
- [IN BETWEEN A ROCK AND A CONDITIONAL JOIN](https://www.mango-solutions.com/in-between-a-rock-and-a-conditional-join/)
- [Joins and conditional matching with data.table](https://aglhurley.rbind.io/2019/02/10/joins-with-data-table/)
- [R Data Table - join but filter with update](https://stackoverflow.com/questions/46588340/r-data-table-join-but-filter-with-update)
- [How to exclude one column from data.table OR convert to data.table to MTS](https://stackoverflow.com/questions/12046079/how-to-exclude-one-column-from-data-table-or-convert-to-data-table-to-mts). `dt[,-1,with=FALSE]`
- [Why is allow.cartesian required at times when when joining data.tables with duplicate keys?](https://stackoverflow.com/questions/23087358/why-is-allow-cartesian-required-at-times-when-when-joining-data-tables-with-dupl)
- [Split text string in a data.table columns](https://stackoverflow.com/questions/18154556/split-text-string-in-a-data-table-columns)

## data.table lookup
- [Joins vs case whens - speed and memory tradeoffs](https://themockup.blog/posts/2021-02-13-joins-vs-casewhen-speed-and-memory-tradeoffs/)
- COOL! [Fast data lookups in R: dplyr vs data.table](https://appsilon.com/fast-data-lookups-in-r-dplyr-vs-data-table/)
- [fastmap](https://r-lib.github.io/fastmap/index.html) solves this problem by storing the keys as C++ std::string objects, and so it does not use the R symbol table at all.
- [Text Mining: Very Fast Word Lookup in a Large Dictionary in R with data.table and matrixStats](https://ourednik.info/maps/2019/07/09/text-mining-very-fast-word-lookup-in-a-large-dictionary-in-r-with-data-table-and-matrixstats/)


## data.table & NSE
- COOL! [Corner Cases With Non-Standard Evaluation in data.table](https://gist.github.com/brodieG/046e7cdd2acf42d95909)
- [How to use non-standard evaluation NSE to evaluate arguments on data.table?](https://stackoverflow.com/questions/57122960/how-to-use-non-standard-evaluation-nse-to-evaluate-arguments-on-data-table)
- фильтрация в I по динамической переменной
	- [How to select rows in data.table with dynamically determined column name and cut off limits?](https://stackoverflow.com/questions/33312777/how-to-select-rows-in-data-table-with-dynamically-determined-column-name-and-cut/33312823)
```
dt[eval(parse(text=name)) < limit]
# OR 
dt[eval(as.name(name))< limit] 
# OR 
dt[eval(as.symbol(name))< limit]
```
	- [Select rows in data table using a variable {duplicate}](https://stackoverflow.com/questions/39005117/select-rows-in-data-table-using-a-variable)
	- [Filter data table by dynamic column name](https://stackoverflow.com/questions/29564002/filter-data-table-by-dynamic-column-name)
- [Distinguishing between an external variable and a column in a data table {duplicate}](https://stackoverflow.com/questions/50711849/distinguishing-between-an-external-variable-and-a-column-in-a-data-table)
- [Subsetting data.table using variables with same name as column](https://stackoverflow.com/questions/21658893/subsetting-data-table-using-variables-with-same-name-as-column)
`dt[eval(.(a))] # identical to dt["b"]`
- [NSE Functions with oshka](https://cran.r-project.org/web/packages/oshka/vignettes/nse-fun.html)
- [Another thing is security when doing eval-parse for user provided input. Computing on the language is much safer in this case:](https://github.com/Rdatatable/data.table/issues/2655). jangorecki commented on Mar 28, 2018 • 

# data.table 1.15. Many new features!
- COOL! с примерами кода [#RStats {data.table} has recently received a major update with v1.15!](https://fosstodon.org/@TimTeaFan/111864136817472707)
This version ships 41 new features - below are my personal top 5 (the last one will blow your mind™ 😏)
	1. The rather cryptic walrus operator `:=` has a new alias called `let()`, making `data.table` calls less arcane and more readable.
	2. data.table’s special symbol `.I` (row index) is now available in the `by` argument of `[.data.table`, making rowwise operations clearer.
	3. `tstrsplit`, data.table’s equivalent to `tidyr::separate()`, now accepts a named list of functions in its `type.convert` argument, which will convert the new columns into the specified types.
	4. `melt()`, data.table’s equivalent to `tidyr::pivot_longer()`, now supports multiple output columns by using `measure()` or `measurev()` in its `measure.vars` argument.
	5. A new interface for programming on data.table has been added. It is built using base R's substitute-like interface via a new `env` argument to `[.data.table`.
I expect a lot of new custom data.table functions and packages that are build on-top of this interface.

- [New governance, release with new features](https://rdatatable-community.github.io/The-Raft/posts/2024-01-30-new_governance_new_release-toby_hocking/).
I am proud to report that today, the first major new data.table features in several years have been released to CRAN!
This new release, version 1.15.0, is remarkable because it is the first new feature release using the new community governance, which was adopted last month. Here is a brief timeline of the recent activities.
Функция `measure`.
- [new programming with data.table](https://johnmackintosh.net/blog/2024-02-05-dt-programming/)


## MacOS
- COOL! [R data.table and Apple M1 installation on Big Sur supporting openmp multithreading](https://investcookies.ru/post/datatable_m1/data_table_arm/). Как обойти кривизну сборки OpenMP по умолчанию.