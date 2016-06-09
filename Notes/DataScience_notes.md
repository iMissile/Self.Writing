# 09.06.2016
## R
- ['names' attribute \[9\] must be the same length as the vector \[1\]](http://stackoverflow.com/questions/14153092/meaning-of-ddply-error-names-attribute-9-must-be-the-same-length-as-the-vec)
```
> mode(priority.train)
[1] "list"
> names(priority.train)
[1] "Date"       "From.EMail" "Subject"    "Message"    "Path"      
> sapply(priority.train, mode)
       Date  From.EMail     Subject     Message        Path 
     "list" "character" "character" "character" "character" 
> sapply(priority.train, class)
> length(priority.train)
[1] 5
> nrow(priority.train)
[1] 1250
> ncol(priority.train)
[1] 5
> str(priority.train)
```
- [How to flatten nested data frames returned from jsonlite](http://stackoverflow.com/questions/26498185/how-to-flatten-nested-data-frames-returned-from-jsonlite)

# 07.06.2016
## OS
- [Copy files over SSH]
	- [WinSCP. Copy a file from a Windows command line](http://winscp.net/forum/viewtopic.php?t=4989)
	- [Scripting and Task Automation](http://winscp.net/eng/docs/scripting)
	- [Automate file transfers (or synchronization) to FTP server or SFTP server](http://winscp.net/eng/docs/guide_automation)
	- [How to Transfer Files Using PuTTY](http://www.it.cornell.edu/services/managed_servers/howto/file_transfer/fileputty.cfm)
	- [PyTTY manual. Chapter 5: Using PSCP to transfer files securely](http://the.earth.li/~sgtatham/putty/0.67/htmldoc/Chapter5.html)
	- [In Windows, how do I transfer files using an SSH or SFTP client?](https://kb.iu.edu/d/akjs)
- [Run commands over SSH]
	- [SSH Via Command Prompt Or Batch File In Windows](http://technologyplusblog.com/2012/networking/ssh-via-command-prompt-or-batch-file-in-windows/)
	- [PuTTY manual. Chapter 7: Using the command-line connection tool Plink](http://the.earth.li/~sgtatham/putty/0.67/htmldoc/Chapter7.html)
	- [How can I send multiple commands to Interactive telnet/ssh session from command line?](http://stackoverflow.com/questions/17253636/how-can-i-send-multiple-commands-to-interactive-telnet-ssh-session-from-command)
    Create a file input.txt with content:
```
    53
    GIVE 5 next 3
```

    Run plink like this:
```
    plink user@host < input.txt
```
ОБЯЗАТЕЛЬНО файл input.txt закончить CR+CL

## R integration
- [DeployR](https://deployr.revolutionanalytics.com/documents/getting-started/about/) is an integration technology for deploying R analytics inside web, desktop, mobile, and dashboard applications as well as backend systems. DeployR turns your R scripts into analytics web services, so R code can be easily executed by applications running on a secure server.
	- [Application Developer Documentation and Tools. Version 8.0.0](https://deployr.revolutionanalytics.com/dev/)


## R & Computer Science
- [HPCC Systems (High Performance Computing Cluster)](https://hpccsystems.com/why-hpcc-systems) is an open source, massive parallel-processing computing platform for big data processing and analytics.
- [Domino Data Lab](https://www.dominodatalab.com/). A Platform to Accelerate Data Science


# 06.06.2016
## R
- Operator [, [[, $
	- [Subsetting](http://adv-r.had.co.nz/Subsetting.html). Advanced R by Hadley Wickham
	- [The most important distinction between [, [[ and $ is that the [ can select more than one element whereas the other two select a single element.](http://stackoverflow.com/questions/9624169/how-to-subset-from-a-list-in-r)
- [Create an empty data.frame](http://stackoverflow.com/questions/10689055/create-an-empty-data-frame). The most efficient way to do this is to use structure to create a list that has the class "data.frame":
```
structure(list(Date = as.Date(character()), File = character(), User = character()), class = "data.frame")
```
- [Understanding data.table](http://r-norberg.blogspot.ru/2016/06/understanding-datatable-rolling-joins.html) by Rolling Joins

- R Profiling
	- [Profiling in R](http://ipub.com/r-profiling/). R has a built in performance and memory profiling facility: Rprof. Type  ?Rprof into your console to learn more. The way the profiler works is as follows:
    		* you start the profiler by calling Rprof, providing a filename where the profiling data should be stored
    		* you call the R functions that you want to analyse
    		* you call Rprof(NULL) to stop the profiler
    		* you analyse the file created by Rprof, typically using  summaryRprof
	- [Profiling with RStudio and profvis](https://blog.rstudio.org/2016/05/23/profiling-with-rstudio-and-profvis/). RStudio Blog

# 03.06.2016
## R & Wolfram
- [How-To: Equivalent of R's dplyr::summarize in Wolfram Language ](http://community.wolfram.com/groups/-/m/t/579134)

# 02.06.2016
## R
- [How to access the last value in a vector?](http://stackoverflow.com/questions/77434/how-to-access-the-last-value-in-a-vector). Целое исследование с тестами.

# 01.06.2016
## R
- [A million ways to connect R and Excel](http://www.thertrader.com/2014/02/11/a-million-ways-to-connect-r-and-excel/)

# 31.05.2016
## Date
- [Date and Time Formats](https://www.w3.org/TR/NOTE-datetime)
```
1994-11-05T08:15:30-05:00 corresponds to November 5, 1994, 8:15:30 am, US Eastern Standard Time.
1994-11-05T13:15:30Z corresponds to the same instant.
```

## R & Tidy Data & join
- [Tidy data](https://cran.r-project.org/web/packages/tidyr/vignettes/tidy-data.html). Hadley Wickham, 2016-02-05

- [Data Processing with dplyr & tidyr](https://rpubs.com/bradleyboehmke/data_wrangling) Brad Boehmke, February 13th, 2015
- [Data Tidying. Data Science with R by Garrett Grolemund](http://garrettgman.github.io/tidying/)
- [Two-table verbs](https://cran.r-project.org/web/packages/dplyr/vignettes/two-table.html)
- [STAT 545: Cheatsheet for dplyr join functions](http://stat545.com/bit001_dplyr-cheatsheet.html)
- [SQL join в картинках](https://encrypted.google.com/search?q=sql+join&tbm=isch)


# 30.05.2016
## Медиа-Тел
- Общество с ограниченной ответственностью «Медиа-тел» (ООО «Медиа-тел»). [Карточка реквизитов](http://card.1os.su/media-tel.bitrix24.ru)
```
Общество с ограниченной ответственностью «Медиа-тел» (ООО «Медиа-тел»)
Директор Кушнарев Кирилл Викторич
Телефон: +7 (499) 272-76-58
Адрес: 119002, г. Москва, ул. Арбат, д.28
Веб-сайт: http://media-tel.ru
ИНН: 7704241358
КПП: 770401001
ОГРН: 1037700097731
Р/с: 40702810702450000018
БИК:
044525593
АО "АЛЬФА-БАНК"
К/с: 30101810200000000593
```

## R
- Task Scheduller
	- [Track your local R scheduled tasks with CommandCenter2000!!!](http://amitkohli.com/track-your-local-r-scheduled-tasks-with-commandcenter2000/)
	- [taskscheduleR: R package to schedule R scripts with the Windows task manager](http://www.bnosac.be/index.php/blog/56-taskscheduler-r-package-to-schedule-r-scripts-with-the-windows-task-manager)
	- [New RStudio add-in to schedule R scripts](http://www.bnosac.be/index.php/blog/57-new-rstudio-add-in-to-schedule-r-scripts)
- ggplot & Legends:
	- Multiple legends for the same aesthetic. [Тут](http://www.r-bloggers.com/multiple-legends-for-the-same-aesthetic-2/) с картинками. А [тут](http://www.milanor.net/blog/multiple-legends-for-the-same-aesthetic-2/) исходная публикация 
	- [ggplot2-plotly-cookbook/legends.R](https://github.com/chriddyp/ggplot2-plotly-cookbook/blob/master/legends.R)
	- [Remove fill around legend key in ggplot](http://stackoverflow.com/questions/21066077/remove-fill-around-legend-key-in-ggplot)
	- [Legend key features overridden - remove fill and diagonal line](http://stackoverflow.com/questions/28971135/legend-key-features-overridden-remove-fill-and-diagonal-line)
	- [Adding legend entry makes all other legend entries diagonal and rectangles](http://www.lfpsc.com/article/dbegbahj-adding-legend-entry-makes-all-other-legend-entries-diagonal-and-rectangles.html)
- [filter for complete cases in data.frame using dplyr (case-wise deletion)](http://stackoverflow.com/questions/22353633/filter-for-complete-cases-in-data-frame-using-dplyr-case-wise-deletion)


# 27.05.16
## Shiny
- [The application unexpectedly exited. Diagnostic information has been dumped to the JavaScript error console. #864](https://github.com/rstudio/shiny/issues/864)

## R
- [Pacman package](https://github.com/trinker/pacman). The pacman package is an R package management tool that combines the functionality of base library related functions into intuitively named functions. This package is ideally added to .Rprofile to increase workflow by reducing time recalling obscurely named functions, reducing code and integrating functionality of base functions to simultaneously perform multiple actions. 
- COOL! [wakefield](https://trinkerrstuff.wordpress.com/2015/04/30/wakefield-random-data-set-part-ii/) is designed to quickly generate random data sets. The user passes n (number of rows) and predefined vectors to the r_data_frame function to produce a dplyr::tbl_df object. `devtools::install_github("trinker/wakefield")`
- Преобразование Date в POSIXct осуществляется в UTC
```
m <- dmy("25-05-2016")
m
[1] "2016-05-25"
str(m)
 Date[1:1], format: "2016-05-25"
dput(m)
structure(16946, class = "Date")
as.POSIXct(m)
[1] "2016-05-25 03:00:00 MSK"
```

- Пример правильного преобразования: `force_tz(with_tz(as.POSIXct(dmy("25-05-2016")), tz = "GMT"), tz = "Europe/Moscow")`
as.POSIXct дает в местной локали (со смещением в часах), отматываем время к нулевой отметке -- к GMT, дальше форсируем использование интересуемой часовой зоны.

## R color
- [Create Colorful Graphs in R with RColorBrewer and Plotly](http://moderndata.plot.ly/create-colorful-graphs-in-r-with-rcolorbrewer-and-plotly/)

# 26.05.16
## R
- Как решить задачу выравнивания осей X у разных графиков
	- [Align a double line chart and a bar plot on the x axis when both charts have the same X axis. ggplot2](http://stackoverflow.com/questions/31573288/align-a-double-line-chart-and-a-bar-plot-on-the-x-axis-when-both-charts-have-the)
	- [Align x axes of box plot and line plot using ggplot](http://stackoverflow.com/questions/30402930/align-x-axes-of-box-plot-and-line-plot-using-ggplot)
	- [Formatting dates on X axis in ggplot2](http://stackoverflow.com/questions/11748384/formatting-dates-on-x-axis-in-ggplot2)
	- [ggplot bar chart for time series](http://stackoverflow.com/questions/28557393/ggplot-bar-chart-for-time-series)
	- [Align multiple ggplot2 graphs with a common x axis and different y axes, each with different y-axis labels](https://gist.github.com/tomhopper/faa24797bb44addeba79)
	- [using ggsave and arrangeGrob after updating gridExtra to 2.0.0](http://stackoverflow.com/questions/33823361/using-ggsave-and-arrangegrob-after-updating-gridextra-to-2-0-0)
	- [gridExtra github](https://github.com/baptiste/gridextra)
Какие тут есть соображения (из ссылок сверху)
1. you have to equalize the plot widths `Bar_plot$widths <-Line_plot$widths `. But in general you also need to equalize the plot widths. If, for example, the y labels on one of the plots take up more space than on the other, even if you use the same axis on each plot, they will not line up when passed to grid.arrange. Соображения [здесь](http://stackoverflow.com/questions/30402930/align-x-axes-of-box-plot-and-line-plot-using-ggplot)
2. with the dev version of gridExtra, I would do `grid.draw(join(g1, g2, along=2))`. Соображения [здесь](http://stackoverflow.com/questions/31573288/align-a-double-line-chart-and-a-bar-plot-on-the-x-axis-when-both-charts-have-the)
3. The gridlines on the x axes will be aligned if you use `scale_x_continuous` to force ggplot to use limits you specify. Now, when you add the layers, the axes will share the common scaling. Соображения [здесь](http://stackoverflow.com/questions/30402930/align-x-axes-of-box-plot-and-line-plot-using-ggplot)
- [Setting limits with scale_x_datetime and time data](http://stackoverflow.com/questions/30607514/setting-limits-with-scale-x-datetime-and-time-data). 
I want to set bounds for the x-axis for a plot of time-series data which features only time (no dates). My limits are:
```
lims <- strptime(c("03:00","16:00"), format = "%H:%M")
```
And my ggplot prints fine, but when I add this to scale_x_datetime`scale_x_datetime(limits = lims)`
I get Error: `Invalid input: time_trans works with objects of class POSIXct only`
>> the error message says that you should use as.POSIXct on lims. You also need to add the date (year, month and day) in lims, because by default it will be `2015, which is off limits.

- [Introduction to ggbio](http://rpubs.com/lcollado/ggbioIntro)

# 24.05.16
## DVCS
- [Mercurial Server for Windows](https://hglabhq.com/). Behind-the-firewall self-hosted Mercurial server and source control management system

# 23.05.16
## R
- [The curl package: a modern R interface to libcurl](https://cran.r-project.org/web/packages/curl/vignettes/intro.html)

# 20.05.16
## R
- [Append an object to a list in R in amortized constant time, O(1)?](http://stackoverflow.com/questions/2436688/append-an-object-to-a-list-in-r-in-amortized-constant-time-o1)

# 19.05.16

## R + Shiny + DT
- [How to sort a dataframe by a timestamp column formatted as “%d/%m/%Y %H:%M:%S” for Shiny R script](http://stackoverflow.com/questions/36635045/how-to-sort-a-dataframe-by-a-timestamp-column-formatted-as-d-m-y-hms-f/36643209#36643209)
- [Prevent column name wrap in shiny DataTable](http://stackoverflow.com/questions/31293506/prevent-column-name-wrap-in-shiny-datatable)

# 18.05.16

## Beeline
- [Популярная проблема: как отключить смс на Билайне правильно?](http://x-tarif.ru/kak-otklyuchit-sms-na-bilayne.html)

## R
- [How to run R scripts from the command line](https://support.rstudio.com/hc/en-us/articles/218012917-How-to-run-R-scripts-from-the-command-line)
- [Run R script from command line](http://stackoverflow.com/questions/18306362/run-r-script-from-command-line)

# 17.05.16

## R
- [Check for installed packages before running install.packages()](http://stackoverflow.com/questions/9341635/check-for-installed-packages-before-running-install-packages)
- [Elegant way to check for missing packages and install them?](http://stackoverflow.com/questions/4090169/elegant-way-to-check-for-missing-packages-and-install-them)
- Logging
	- [A futile try/catch.](https://cartesianfaith.com/2013/05/29/futile-logger-1-3-3-rc-available/) It is now possible to capture non-futile warnings and errors by wrapping a block in ftry, which is essentially a wrapper around tryCatch.
	- [futile.logger is a logging utility for R.](https://github.com/zatonovo/futile.logger) Originally built based on log4j, the latest version introduces a new API that is more consistent with R idioms. In practice this means an interface that works equally well in the shell for interactive use and also in scripts for system use.
	- [How to log using futile logger from within a parallel method in R?](http://stackoverflow.com/questions/20930112/how-to-log-using-futile-logger-from-within-a-parallel-method-in-r)
	- [logR -- Extended logging solution](https://github.com/jangorecki/logR).
	- [Is there any standard logging package for R?](http://stackoverflow.com/questions/1928332/is-there-any-standard-logging-package-for-r)

## Shiny
- [Debugging Shiny applications](http://shiny.rstudio.com/articles/debugging.html). `options(shiny.error = browser)`
- [How can I save the result of str() as a string in R?](http://stackoverflow.com/questions/30964224/how-can-i-save-the-result-of-str-as-a-string-in-r). `capture.output` will create a character vector (one element for each line printed to the console). If you want it in one string, you could concatenate it with paste(foo, collapse="\n").
- [Shiny: What is the option setting to display in the console the messages between server and ui](http://stackoverflow.com/questions/23002712/shiny-what-is-the-option-setting-to-display-in-the-console-the-messages-between). `options(shiny.trace = TRUE)`
- [Write error messages for your UI with validate](http://shiny.rstudio.com/articles/validation.html)
- `sessionInfo()`


# 16.05.16
## Shiny Server
- [Where to deploy R project in local shiny server {closed}](http://stackoverflow.com/questions/36565085/where-to-deploy-r-project-in-local-shiny-server)

# 13.05.16
## R
- [You want to use different fonts in your graphs.](http://www.cookbook-r.com/Graphs/Fonts/)
- [extrafont package](https://github.com/wch/extrafont). The extrafont package makes it easier to use fonts other than the basic PostScript fonts that R uses. Fonts that are imported into extrafont can be used with PDF or PostScript output files. On Windows, extrafont will also make system fonts available for bitmap output.
- COOL. [ggrepel: Avoid overlapping of text labels](http://www.sthda.com/english/wiki/ggplot2-texts-add-text-annotations-to-a-graph-in-r-software)
- Autoresize text
	- [Mixing ggplot2 graphs with other graphical output](https://github.com/hadley/ggplot2/wiki/Mixing-ggplot2-graphs-with-other-graphical-output)
	- [ggplot2 texts: Add text annotations to a graph in R software](http://www.sthda.com/english/wiki/ggplot2-texts-add-text-annotations-to-a-graph-in-r-software)
	- [Automatically scale font size (etc.) of ggplot2 inside an Rmarkdown document](http://stackoverflow.com/questions/28835491/automatically-scale-font-size-etc-of-ggplot2-inside-an-rmarkdown-document)
	- [ggplot2: geom_text resize with the plot and force/fit text within geom_bar](http://stackoverflow.com/questions/36319229/ggplot2-geom-text-resize-with-the-plot-and-force-fit-text-within-geom-bar)
	- [Creating a text grob that automatically adjusts to viewport size](https://ryouready.wordpress.com/2012/08/01/creating-a-text-grob-that-automatically-adjusts-to-viewport-size/)
	- [unit {grid}. Function to Create a Unit Object](http://www.inside-r.org/r-doc/grid/unit)
	- [textGrob placement relative to changing plot size](http://stackoverflow.com/questions/28415461/textgrob-placement-relative-to-changing-plot-size)
	- [R ggplot2 arrangeGrob() – arrange ggplots on a page](https://jonkimanalyze.wordpress.com/2014/03/26/ggplot2-arrangegrob-arrange-ggplots-on-a-page/)
- [git2r - An R Package to Interface Git](http://srug.ropensci.org/git2r-2015-07-08-srug.html#/) by Stefan Widgren. Stockholm R useR group, 2015-07-08
- [git2r: Provides Access to Git Repositories](https://github.com/ropensci/git2r). Interface to the 'libgit2' library, which is a pure C implementation of the 'Git' core methods. Provides access to 'Git' repositories to extract data and running some basic 'Git' commands.


# 12.05.16
## R
- [Combining date and time into a Date column for plotting](http://stackoverflow.com/questions/24105984/combining-date-and-time-into-a-date-column-for-plotting)
- [How to get your very own RStudio Server and Shiny Server with DigitalOcean](http://deanattali.com/2015/05/09/setup-rstudio-shiny-server-digital-ocean/)

## ggplot
- [How to nicely annotate a ggplot2 (manual)](http://stackoverflow.com/questions/2409357/how-to-nicely-annotate-a-ggplot2-manual)
- [Benchmark plot creation time. Broken down into construct, build, render and draw times.](http://docs.ggplot2.org/current/benchplot.html)

## General
- [пересчитываем из гектопаскалей (hPa) в мм рт. столба](https://www.unitjuggler.com/%D0%BF%D0%B5%D1%80%D0%B5%D0%B2%D0%BE%D0%B4-pressure-%D0%B8%D0%B7-hPa-%D0%B2-mmHg.html)


# 11.05.16
## Weather
- [И снова Яндекс.Погода для сайта: время суток, направление ветра и прочие параметры](https://habrahabr.ru/post/233243/)

## R
- [Read a CSV from github into R](http://stackoverflow.com/questions/14441729/read-a-csv-from-github-into-r)
- Ура-а-а-а! Решена проблема с unicode файлами под виндой. [How to source() .R file saved using UTF-8 encoding?](http://stackoverflow.com/questions/5031630/how-to-source-r-file-saved-using-utf-8-encoding). Меняем `source()` на `eval(parse(filename, encoding="UTF-8"))` или на
```
source.utf8 <- function(f) {
    l <- readLines(f, encoding="UTF-8")
    eval(parse(text = l), envir=.GlobalEnv)
}
```

## ggplot tweaks
- [Plotting rectangles in ggplot2 - Invalid input: time_trans works with objects of class POSIXct only [Resolved]](http://blogs.candoerz.com/question/79734/plotting-rectangles-in-ggplot2-invalid-input-time_trans-works-with-objects-of-class-posixct-only.aspx). Здесь пытаются сделать что-то в виде диграмм ганта средствами ggplot.
- [Оно же](http://stackoverflow.com/questions/32590776/plotting-rectangles-in-ggplot2-invalid-input-time-trans-works-with-objects-of), но на stackoveflow.
- Как нарисовать график для переменной X, выступающей в качестве фактора. [Using `geom_line()` with X axis being factors](http://stackoverflow.com/questions/16350720/using-geom-line-with-x-axis-being-factors)
- [X-axis major and minor tick date labels and breaks (epicurve)](http://stackoverflow.com/questions/26118963/x-axis-major-and-minor-tick-date-labels-and-breaks-epicurve)
- [# build the plot](http://stackoverflow.com/questions/26118963/x-axis-major-and-minor-tick-date-labels-and-breaks-epicurve): `gg2 <- ggplot_gtable(ggplot_build(gg1))`
- [Introduction to cowplot](https://cran.r-project.org/web/packages/cowplot/vignettes/introduction.html). The cowplot package is a simple add-on to ggplot2. It is meant to provide a publication-ready theme for ggplot2, one that requires a minimum amount of fiddling with sizes of axis labels, plot backgrounds, etc. Its primary purpose is to give my students and postdocs an easy way to make figures that I will approve of. Thus, this package meets my personal needs and tastes. Yours may be different.
- [An Introduction on How to Make Beautiful Charts With R and ggplot2](http://minimaxir.com/2015/02/ggplot-tutorial/)
- [Annotate ggplot with an extra tick and label](http://stackoverflow.com/questions/29824773/annotate-ggplot-with-an-extra-tick-and-label)
- Произвольные форматтеры для меток
	- [How to put ggplot2 ticks labels between dollars?](http://stackoverflow.com/questions/20326946/how-to-put-ggplot2-ticks-labels-between-dollars)
	- [Can you change the default scale_x_datetime?](http://stackoverflow.com/questions/16239830/can-you-change-the-default-scale-x-datetime)
	- Что делать, если метки на графике надо расставить по фиксированным местам? [how to fix x-axis and y-axis scale](http://stackoverflow.com/questions/30799845/how-to-fix-x-axis-and-y-axis-scale)
	- [ggplot: conflict between date_breaks() and limits](http://stackoverflow.com/questions/29212722/ggplot-conflict-between-date-breaks-and-limits)

# 06.05.16
## R
- [Changing R default library path using .libPaths in Rprofile.site fails to work](http://stackoverflow.com/questions/15170399/changing-r-default-library-path-using-libpaths-in-rprofile-site-fails-to-work)
Месторасположение файла `C:\Program Files\R\R-3.3.0\etc\Rprofile.site`
В ProgramFiles записать не может, поэтому RStudio гонит сюда:
`Installing package into ‘C:/Users/<User>/Documents/R/win-library/3.3’`
- [Aesthetics: group](http://docs.ggplot2.org/current/aes_group_order.html).
- [How to plot factors in a specified order in ggplot](http://rstudio-pubs-static.s3.amazonaws.com/7433_4537ea5073dc4162950abb715f513469.html). We need to change the order of factor levels by specifying the order explicitly.
- [convert data.frame column format from character to factor](http://stackoverflow.com/questions/9251326/convert-data-frame-column-format-from-character-to-factor)
- [How to change factor labels into string in a data frame](http://stackoverflow.com/questions/19204729/how-to-change-factor-labels-into-string-in-a-data-frame)
- COOL! [R Learning Module. Factor variables](http://www.ats.ucla.edu/stat/r/modules/factor_variables.htm). Здесь я нашел ответ!!! `ses.order <- ordered(ses, levels = c("low", "middle", "high"))`

## Weather
- [How to use API key in API call](http://openweathermap.org/appid)

# 05.05.16
## General
- [Samsung. Форма проверки регистрации электронной гарантии](http://www.samsung.com/ru/support/ewarranty/)

# 04.05.16
## R
- [Best way to make a custom palette with ggplot2](http://amitkohli.com/best-way-to-make-a-custom-palette-with-ggplot2/)
```
#' @export
#' @rdname scale_brewer
scale_fill_distiller <- function(..., type = "seq", palette = 1, direction = -1, values = NULL, space = "Lab", na.value = "grey50", guide = "colourbar") {
  type <- match.arg(type, c("seq", "div", "qual"))
  if (type == "qual") {
    warning("Using a discrete colour palette in a continuous scale.\n  Consider using type = \"seq\" or type = \"div\" instead", call. = FALSE)
  }
  continuous_scale("fill", "distiller",
    gradient_n_pal(brewer_pal(type, palette, direction)(6), values, space), na.value = na.value, guide = guide, ...)
}
```
- [Gradient of n colors ranging from color 1 and color 2](http://stackoverflow.com/questions/13353213/gradient-of-n-colors-ranging-from-color-1-and-color-2)
- [Error in continuous_scale when using scale_fill_gradient](http://stackoverflow.com/questions/33363108/error-in-continuous-scale-when-using-scale-fill-gradient). Scale_fill_distiller -> scale_fill_gradientn
- Хак по работе функции scale_fill_distiller: [GitHub.  ggplot2/R/scale-brewer.r](https://github.com/hadley/ggplot2/blob/master/R/scale-brewer.r)
- [How to get multiple ggplot2 scale_fill_gradientn with same scale?](http://stackoverflow.com/questions/22235580/how-to-get-multiple-ggplot2-scale-fill-gradientn-with-same-scale)

# 29.04.2016
## R
- [Assign categories based on relations](http://stackoverflow.com/questions/19118080/assign-categories-based-on-relations)
	- [Does ifelse really calculate both of its vectors every time? Is it slow?](http://stackoverflow.com/questions/16275149/does-ifelse-really-calculate-both-of-its-vectors-every-time-is-it-slow/16275201)

## Shiny
- [Interactively change the selectInput choices](http://stackoverflow.com/questions/16173325/interactively-change-the-selectinput-choices)
- [Shiny example: dynamic input fields](https://gist.github.com/wch/4211337)


# 28.04.2016
## Wolfram
- [How to | Display the Timing of an Evaluation in a Notebook Window](https://reference.wolfram.com/language/howto/DisplayTheTimingOfAnEvaluationInANotebookWindow.html)
- [TimeUsed[]](https://reference.wolfram.com/language/ref/TimeUsed.html) gives the total number of seconds of CPU time used so far in the current Wolfram System session.
- [AbsoluteTiming[expr]](https://reference.wolfram.com/language/ref/AbsoluteTiming.html) evaluates expr, returning a list of the absolute number of seconds in real time that have elapsed, together with the result obtained.
- [Timing[expr]](https://reference.wolfram.com/language/ref/Timing.html) evaluates expr, and returns a list of the time in seconds used, together with the result obtained. 

## R
- Shiny Reactive Programming
	- [Reactivity: An overview](http://shiny.rstudio.com/articles/reactivity-overview.html)
	- [A few things I learned about shiny (and reactive programming)](https://shinydata.wordpress.com/2015/02/02/a-few-things-i-learned-about-shiny-and-reactive-programming/)
	- [Reactive Programming with R Shiny](http://www.alshum.com/shiny-reactive/)
- [GridExtra. Arranging multiple grobs on a page](https://cran.r-project.org/web/packages/gridExtra/vignettes/arrangeGrob.html)
- [Quick-R. Combining Plots](http://www.statmethods.net/advgraphs/layout.html)
- [Combined plot of ggplot2 (Not in a single Plot), using par() or layout() function? [duplicate]](http://stackoverflow.com/questions/9490482/combined-plot-of-ggplot2-not-in-a-single-plot-using-par-or-layout-functio)

## DS
- [Two Y-Axes](https://kieranhealy.org/blog/archives/2016/01/16/two-y-axes/). Matt remarked that “Friends don’t let friends use two y-axes”. It’s a good rule. The topic came up a couple of times during the data visualization short course I taught last semester. Using two y-axes makes it even easier than usual to fool yourself (or someone else) about the degree of association between two variables. This is because you can adjust the scaling of the axes to relative to one another in way that moves the data series around more or less however you like.
- [Dual axes for ggplot2](https://gist.github.com/jslefche/e4c0e9f57f0af49fca87). Modified from: [ggplot2-adding-secondary-transformed-x-axis-on-top-of-plot](https://stackoverflow.com/questions/21026598/ggplot2-adding-secondary-transformed-x-axis-on-top-of-plot) & [dual_axis_in_ggplot2](https://rpubs.com/kohske/dual_axis_in_ggplot2)
- [R: single plot with two different y-axes](http://www.gettinggeneticsdone.com/2015/04/r-single-plot-with-two-different-y-axes.html)


# 27.04.2016
## DS
- [Wes Anderson Palettes](https://github.com/karthik/wesanderson). Tired of generic mass produced palettes for your plots? Short of adding an owl and dressing up your plot in a bowler hat, here's the most indie thing you can do to one. First round of palettes derived from the amazing Tumblr blog Wes Anderson Palettes.
- [The viridis color palettes] (https://cran.r-project.org/web/packages/viridis/vignettes/intro-to-viridis.html). Bob Rudis, Noam Ross and Simon Garnier
- [Introduction to ggthemes](https://cran.r-project.org/web/packages/ggthemes/vignettes/ggthemes.html)
- [ggthemr](https://github.com/cttobin/ggthemr). Themes for ggplot2. The idea of this package is that you can just set the theme and then forget about it. You shouldn't have to change any of your existing code. There are several parts to a theme:

## Shiny
- [Dean Attali's Shiny Server](http://daattali.com/shiny/)
- Scoping in Shiny
	- [Scoping rules for Shiny apps](http://shiny.rstudio.com/articles/scoping.html)
	- [Scoping (depricated)](http://rstudio.github.io/shiny/tutorial/#scoping)
	- [Use R scripts and data](http://shiny.rstudio.com/tutorial/lesson5/). См. пункт "Execution" 
- [Using DT in Shiny](https://rstudio.github.io/DT/shiny.html)
- [Control the height in fluidRow in R shiny](http://stackoverflow.com/questions/25340847/control-the-height-in-fluidrow-in-r-shiny). HTML +CSS

# 26.04.2016
## General
- [Альфабанк. Услуга «Мой контроль»](https://alfabank.ru/retail/cards/mycontrol/)

## Development
- [Painless Merge Conflict Resolution in Git](http://blog.wuwon.id.au/2010/09/painless-merge-conflict-resolution-in.html). 
  При установке Github Desktop Merge tools указывается во временном конфиг файле gitconfig: C:\Users\<User>\AppData\Local\GitHub\PortableGit_<... numbers ...>\mingw32\etc\
Добавляем в конфиг:
```
[merge]
	tool = am
[mergetool]
	prompt = true
	keepBackup = false
[mergetool "am"]
	cmd = \"C:/Program Files/Araxis/Araxis Merge/Merge.exe\" \"$LOCAL\" \"$REMOTE\" \"$BASE\" \"$MERGED\"
	trustExitCode = true
```
После выполнения настроек запускаем из командной строки git: `git mergetool`

- [MAC: How do I configure Araxis Merge for use with Git?](http://stackoverflow.com/questions/14593817/how-do-i-configure-araxis-merge-for-use-with-git)
`git config --global mergetool.araxis.path "/Applications/Araxis Merge.app/Contents/Utilities/compare"`
После этого запускаем vim: [How to locate the git config file in Mac {duplicate}](http://stackoverflow.com/questions/16283280/how-to-locate-the-git-config-file-in-mac)
Добавляем в конфиг файл.
	- `vim ~/.gitconfig`
	- ESC+I -- переход в режим редактирования
	- ESC+:+wq! -- выход с сохранением после редактирования

[merge]
	tool = am
[mergetool]
	prompt = true
	keepBackup = false

## R
- [Determining memory usage of objects? (duplicate)](http://stackoverflow.com/questions/1395270/determining-memory-usage-of-objects)
	При крайне простой процедуре округления, 130 кб данных превращаются в 35 мегабайт. POSIXct (520 байт) превращается в POSIXlt, размером в 2 кб каждая запись:
```
> t <- row.df$timestamp
> object.size(t)
130232 bytes
> m <- lapply(row.df$timestamp, function(x){round(x, units="hours")})
> object.size(m)
35022280 bytes
```
Решение:
```
# m <- lapply(row.df$timestamp, function(x){round(x, units="hours")}) # так из 130 кб получаем 35 Мб, надо использовать round_date {lubridate}
# m <- lapply(t, function(x){round_date(x, unit = "hour")}) # тут получаем 8Мб !!!
# m <- round_date(t, unit = "hour") # самый быстрый и компактный вариант
```

# 25.04.2016
## DS
- [OpenWeatherMap](http://openweathermap.org/api). Our weather API is simple, clear and free. We also offer higher levels of support, please see our paid plan options. To access the API you need to sign up for an API key if you are on a free or paid plan. 

# 21.04.2016
## DS + GIS
Глобальная проблема -- очень долго выводится тепловая карта посредством geom_tile. проблема в том, что при выводе каждого полигона осуществляется преобразование координат.
можно использоват geom_raster, но при этом возникают проблемы с наложением координат.

Детально можно почитать в ряде следующих статей:
"I am having a problem combining geom_raster and ggmap. They each work independently, but when I try to combine the two I get the error message "Error: geom_raster only works with Cartesian coordinates""
- [geom_raster and ggmap](https://groups.google.com/forum/embed/#!topic/ggplot2/nqzBX22MeAQ)
```
Perhaps the best way to see it is through example :

library(ggmap)
gc <- geocode('the white house')



# the bad way  
qmap('washington, dc', zoom = 10) + # ok
  geom_point(colour = 'red', data = gc) +
  coord_cartesian()

  
qmap('washington, dc', zoom = 7) + # slightly north?
  geom_point(colour = 'red', data = gc) +
  coord_cartesian()

  
qmap('washington, dc', zoom = 4) + # in northern pennsylvania
  geom_point(colour = 'red', data = gc) +
  coord_cartesian()  

  
qmap('washington, dc', zoom = 1) + # potus = santa claus
  geom_point(colour = 'red', data = gc) +
  coord_cartesian()
```
- [Add raster to base map: Set Alpha and fill to inset_raster() in ggplot2](http://stackoverflow.com/questions/33530055/add-raster-to-base-map-set-alpha-and-fill-to-inset-raster-in-ggplot2)
- [R: ggmap – Overlay shapefile with filled polygon of regions](http://www.markhneedham.com/blog/2014/11/17/r-ggmap-overlay-shapefile-with-filled-polygon-of-regions/)

# 20.04.2016
## DS
- [R shiny. Error pops up while using ggmap](http://stackoverflow.com/questions/28935768/r-shiny-error-pops-up-while-using-ggmap)
- [The basic plot interaction demo](http://shiny.rstudio.com/gallery/plot-interaction-basic.html)
- [Shiny Apps and ggmaps](http://keeganhin.es/blog/maps.html)
- [Experimenting With R – Point to Point Mapping With Great Circles](https://blog.ouseful.info/2014/03/24/experimenting-with-r-point-to-point-mapping-with-great-circles/)
- [ShinyMap. Data product developement course project](http://rstudio-pubs-static.s3.amazonaws.com/23390_18f799a4d9ea46c392460b252fed6f15.html#1) by Eric Fan, Engineer. 
- [Making Maps in R (Part 1)](http://www.kevjohnson.org/making-maps-in-r/). COOL!
- [Making Maps in R (Part 2)](http://www.kevjohnson.org/making-maps-in-r-part-2/). COOL! нашел ответ про контурные карты
- [Social Data Science. Lectures](http://sebastianbarfort.github.io/sds/slides/)
	- [Lecture 4: Data Visualization in R (maps). Social Data Science](http://sebastianbarfort.github.io/sds/slides/lecture4.html) by Sebastian Barfort. September, 2015
- [R: Isotherms as isolines using ggplot2](http://stackoverflow.com/questions/32679844/r-isotherms-as-isolines-using-ggplot2)


# 19.04.2016
## General
- [Получение международного водительского удостоверения](https://www.gosuslugi.ru/pgu/service/10000467319_10000029570.html#!_places)
	- 2 ОЭР МО ГИБДД ТНРЭР № 5 ГУ МВД России по г. Москве (Киевская, 20)
	- 2 отделение по экзаменационной работе МО ГИБДД ТНРЭР №1 ГУ МВД России по г. Москве (ул. Б. Ордынка, д.8)
	- ГУОБДД МВД России

# DS
- [Using with() and by()](http://www.statmethods.net/stats/withby.html)
- [Displaying Maps and Spatial Data](http://www.unomaha.edu/mahbubulmajumder/data-science/fall-2014/lectures/06-display-spatial-data/06-display-spatial-data.html#/) by Mahbubul Majumder, PhD. Sep 11, 2014
- [Methods for doing heatmaps, level / contour plots, and hexagonal binning](http://stackoverflow.com/questions/7851602/methods-for-doing-heatmaps-level-contour-plots-and-hexagonal-binning)
	The options for 2D plots of (x,y,z) in R are a bit numerous. However, grappling with the options is a bit of a challenge, especially in the case that all three are continuous.
	To clarify the problem (and possibly assist in explaining why I might be getting tripped up with contour or image), here is a possible classification scheme:
	- Case 1: The value of z is not provided but is a conditional density based on values in (x,y). (Note: this is essentially relegating the calculation of z to a separate function - a density estimation. Something still has to use the output of that calculation, so allowing for arbitrary calculations would be nice.)
	- Case 2: (x,y) pairs are unique and regularly spaced. This implies that only one value of z is provided per (x,y) value.
	- Case 3: (x,y) pairs are unique, but are continuous. Coloring or shading is still determined by only 1 unique z value.
	- Case 4: (x,y) pairs are not unique, but are regularly spaced. Coloring or shading is determined by an aggregation function on the z values.
	- Case 5: (x,y) pairs are not unique, are continuous. Coloring / shading must be determined by an aggregation function on the z values.
- [GEOG 414/515:  Advanced Geographic Data Analysis. Contouring and surface fitting](http://www.geog.uoregon.edu/bartlein/old_courses/geog414f03/lectures/lec13.htm). Ключевые слова: "Three-dimensional interpolation"
- [3D spline surface]
	- [Obtain spline surface on R](http://stackoverflow.com/questions/24810501/obtain-spline-surface-on-r)
	- [R: Plotting a 3D surface from x, y, z](http://stackoverflow.com/questions/3979240/r-plotting-a-3d-surface-from-x-y-z)
	- [How to improve interp with akima?](http://stackoverflow.com/questions/24410292/how-to-improve-interp-with-akima)

# 05.04.2016
## Python
- [geopy](https://geopy.readthedocs.org/en/1.10.0/#) is a Python 2 and 3 client for several popular geocoding web services. 
geopy makes it easy for Python developers to locate the coordinates of addresses, cities, countries, and landmarks across the globe using third-party geocoders and other data sources.
geopy is tested against CPython 2.7, CPython 3.2, CPython 3.4, PyPy, and PyPy3.
- Yandex. Клуб API Карт. [Параметры в URL панорамы](https://yandex.ru/blog/mapsapi/10932)

## DS
- [Static API Карт](https://tech.yandex.ru/maps/staticapi/). Статичные изображения Яндекс.Карт, отдаваемые по HTTP-запросу.
- [Everything You Never Wanted to Know About Google Maps' Parameters](https://moz.com/ugc/everything-you-never-wanted-to-know-about-google-maps-parameters).
- [URL to dynamic Google Map with path](http://stackoverflow.com/questions/13883615/url-to-dynamic-google-map-with-path)
- GIS
	- [Visualising your hiking trails and photos with My Tracks, R and Leaflet](http://mhermans.net/hiking-gpx-r-leaflet.html)
	- [Intro to GIS mapping in R](http://remi-daigle.github.io/GIS_mapping_in_R/)
	- [Tips for reading spatial files into R with rgdal](http://zevross.com/blog/2016/01/13/tips-for-reading-spatial-files-into-r-with-rgdal/)
	- [Geospatial Data Processing and Analysis in R](http://rpubs.com/ajlyons/rspatialdata). Andy Lyons, Stanford University, The Berkeley R Language Beginner Study Group, August 19, 2014
	- [Возможности работы с пространственными данными статистического пакета R](http://gis-lab.info/qa/rspatial.html)
	- [Spatial.ly R Spatial Tips](http://spatial.ly/r/)
	- [Geospatial Data in R](http://nathanlane.info/tutorials/2015/10/18/taking-geospatial-data-to-r-how-to-ditch-arcgis.html)
	- [Geospatial Data in R and Beyond](http://www.maths.lancs.ac.uk/~rowlings/Teaching/UseR2012/)
	- [Applied Spatial Data Science with R](http://blog.dominodatalab.com/applied-spatial-data-science-with-r/) by Daniel Emaasit
	- [Introduction to visualising spatial data in R](https://github.com/Robinlovelace/Creating-maps-in-R). Introductory tutorial on graphical display of geographical information in R, to contribute to teaching material. For the context of this tutorial and a video introduction, please see here: http://robinlovelace.net/r/2014/01/30/spatial-data-with-R-tutorial.html
	- COOL. NEON Spatial Data Lessions:
		- [Neon Spatial Vector Data in R](http://data-lessons.github.io/NEON-R-Spatial-Vector/)
		- [Neon Raster Data in R](http://data-lessons.github.io/NEON-R-Spatial-Raster/).
	- [writeOGR column limit error: “Creating Name field failed”](http://gis.stackexchange.com/questions/93135/writeogr-column-limit-error-creating-name-field-failed)
	- [GPX-overview: R function create overview .gpx files (using leaflet RgoogleMaps)](http://www.digital-geography.com/gpx-overview-r-function-create-overview-gpx-files-using-leaflet-rgooglemaps)
	- [Переход от одной системы координат к другой - методы трансформации](http://gis-lab.info/qa/datum-transform-methods.html)


## GPS & GIS
- [Trails](https://trails.io/en/). Your iPhone GPS tracks logbook. Record all your outdoor activities be it hiking, jogging, cycling, canoeing or skiing down the Alps.
- [Google CRS](http://spatialreference.org/ref/sr-org/google-projection/)
- [Recommended Web sites with GPS trails in GPX format](http://www.expertgps.com/tutorials/recommended-web-sites-with-gps-trails-in-gpx-format.asp)
- [How do I convert a set of latitude/longitude coordinates with timestamps to a GPX tracklog?](http://gis.stackexchange.com/questions/94087/how-do-i-convert-a-set-of-latitude-longitude-coordinates-with-timestamps-to-a-gp)
- [Convert a GPS file to plain text or GPX](http://www.gpsvisualizer.com/convert_input)
- [Find coordinates by moving around the map](http://mondeca.com/index.php/en/any-place-en). This page uses the Google Maps API to find out accurate geographical coordinates (latitude and longitude) for any place on Earth.
It provides two ways to search, either by moving around the map and zooming in, or by typing an address if the place is unknown. The default location and address are those of Mondeca office in Paris.
Comments and questions to bernard.vatant at mondeca dot com
- [Работа с геолокациями в режиме highload](https://habrahabr.ru/post/228023/)
- [Вычисление расстояния и начального азимута между двумя точками на сфере](http://gis-lab.info/qa/great-circles.html)

# 04.04.2016
## R
- [Plotting a vector field in R + ggplot](http://codereview.stackexchange.com/questions/93974/plotting-a-vector-field-in-r-ggplot)
- [vector field visualisation R](http://stackoverflow.com/questions/14936504/vector-field-visualisation-r). If there is a lot of data (the question says "big file"), plotting the individual vectors may not give a very readable plot. Here is another approach: the vector field describes a way of deforming something drawn on the plane; apply it to a white noise image. Here is a example from the R-Help of **pracma-package**.
- [Draw a circle with ggplot2](http://stackoverflow.com/questions/6862742/draw-a-circle-with-ggplot2)
- [assign multiple new variables in a single line in R](http://stackoverflow.com/questions/7519790/assign-multiple-new-variables-in-a-single-line-in-r)

# 01.04.2016
## Math
- [Равномерное распределение точек на диске](http://dxdy.ru/topic91607.html)
- [Spreading points on a disc and on a sphere](http://blog.marmakoide.org/?p=1)
- [Иллюстрации на Геогебре]():
	- [Isocel disc tesselation](http://tube.geogebra.org/student/m286087)
	- [Points distributed on a disc](http://tube.geogebra.org/student/m286063)
	- [Distribution points over unit disk](http://tube.geogebra.org/material/show/id/424961)
- [GeoGebra](http://www.geogebra.org/). The Graphing Calculator for Functions, Geometry, Algebra, Calculus, Statistics and 3D Math!. Dynamic mathematics for learning and teaching
- [Wolfram MathWorld. Sphere Point Picking](http://mathworld.wolfram.com/SpherePointPicking.html)
- [Distributing points on the sphere](https://www.maths.unsw.edu.au/about/distributing-points-sphere)

# 30.03.2016
## Office
- Есть проблема с нумерацией страниц в колонтитулах: "Ошибка! Только основной документ", далее:
	- [Некоторые рекомендации по организации автонумерации при написании научных статей и диссертаций средствами Microsoft Word](https://habrahabr.ru/post/187398/)
	- [Field codes: Seq (Sequence) field](https://support.office.com/en-us/article/Field-codes-Seq-Sequence-field-062a387b-dfc9-4ef8-8235-29ee113d59be?rs=en-US&ui=en-US&ad=US) или перевод на русский [Коды полей: SEQ (последовательность)](https://support.office.com/ru-ru/article/%D0%9A%D0%BE%D0%B4%D1%8B-%D0%BF%D0%BE%D0%BB%D0%B5%D0%B9-SEQ-%D0%BF%D0%BE%D1%81%D0%BB%D0%B5%D0%B4%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D1%8C-062a387b-dfc9-4ef8-8235-29ee113d59be?rs=ru-RU&ui=ru-RU&ad=RU)
	- [Как создать две различные схемы нумерации страниц в одном и том же документе Microsoft Word 2002](http://www.interface.ru/home.asp?artId=16736)

# 29.03.2016
## PID
- [Control System Lectures](https://www.youtube.com/watch?v=oBc_BHxw78s&list=PLUMWjy5jgHK1NC52DXXrriwihVrYZKqjk)
- [Understanding PID in 4 minutes](https://www.youtube.com/watch?v=wbmEUi2p-nA)
- [PID Math Demystified ](https://www.youtube.com/watch?v=JEpWlTl95Tw)
- [Teaching Old Motors New Tricks - Part 1](https://www.youtube.com/watch?v=fpTvZlnrsP0)


# 25.03.2016
## DS
- [MRAN Frequently Asked Questions](https://mran.revolutionanalytics.com/faq/). Here are some common questions about Microsoft R Open. Got a question that isn’t answered here? Contact us.
	- [Reproducibility: Using Fixed CRAN Repository Snapshots](https://mran.revolutionanalytics.com/documents/rro/reproducibility/)
- [Highcharter](http://jkunst.com/highcharter/) is a R wrapper for highcharts javascript libray and its modules. Highcharts is very mature and flexible javascript charting library and it has a great and powerful API.
	- [Highcharts Demos](http://www.highcharts.com/demo)
	- [Highcharts R code Examples](http://jkunst.com/highcharter/highcharts.html)


# 24.03.2016
## Graphics
- [Pixlr](https://pixlr.com/editor/). Online Image Editor by Autodesk

## DS
- [Visualizing MBTA Data. An interactive exploration of Boston's subway system](http://mbtaviz.github.io/).
	- [MBTA Subway Delays](https://mbta.meteor.com/)

## Other
- [Как мы строили метро](http://www.metro.ru/library/kak_my_stroili_metro/). В марте нынешнего года редакция «Истории метро» выпустила в свет книгу «Рассказы строителей метро» — первый сборник по истории московского метрополитена имени Л. М. Кагановича, написанный ударниками и ударницами — строителями метро.

Настоящая книга — второй сборник по истории метро. Он написан инженерами, архитекторами, политическими работниками вместе со славной армией ударников и ударниц, комсомольцев и комсомолок, построившими лучший по всеобщему признанию метро в мире — московский метрополитен имени Л. М. Кагановича.
# 22.03.2016
## IoT
- [Корректная реализация разностной схемы ПИД регулятора. Tutorial](https://habrahabr.ru/post/143388/)
- [ПИД-регулятор своими руками. Tutorial](https://habrahabr.ru/post/145991/)

## Math
- [MathWorks Help. PID Controller Types for Tuning](http://www.mathworks.com/help/control/ug/pid-controller-types-for-tuning.html)
- [Wolfram SystemModeller](http://forum.ru-board.com/topic.cgi?forum=35&topic=1174&start=0&limit=1&m=38#1), на [сайте Wolfram](http://www.wolfram.com/system-modeler/)
- Wolfram Help
	- [Архитектура ПИД регуляторов](https://www.wolfram.com/mathematica/new-in-9/enhanced-control-systems/pid-controller-architectures.html)
	- [PID Controller Architectures](https://reference.wolfram.com/language/example/PIDControllerArchitectures.html)
	- [PIDTune](https://reference.wolfram.com/language/ref/PIDTune.html)
	- [PID Control of a Tank Level. Interraction View](http://demonstrations.wolfram.com/PIDControlOfATankLevel/)
- [PID Control-R](http://oddhypothesis.blogspot.ru/2013/02/pid-control-r.html)

## Software
- [Definition: Iterative and Incremental Development](https://blogs.msdn.microsoft.com/aridle/2007/07/25/definition-iterative-and-incremental-development/)
- [Scrum.org](https://www.scrum.org/Resources)
- [Scrum Guides](http://www.scrumguides.org/)


# 21.02.2016
## DS
- Яндекс геокодирование. [Параметры HTTP-запроса](https://tech.yandex.ru/maps/doc/geocoder/desc/concepts/input_params-docpage/)
	- [Пример запроса] (https://geocode-maps.yandex.ru/1.x/?format=json&geocode=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0,%20%D0%B4%D0%BE%D0%BC%2024,%20%D1%83%D0%BB%D0%B8%D1%86%D0%B0%20%D0%9D%D0%BE%D0%B2%D1%8B%D0%B9%20%D0%90%D1%80%D0%B1%D0%B0%D1%82)
- [ФИАС - Федеральная Информационная Адресная Система](http://www.ifias.ru/)

## IoT
- [PID Control of the Heat Exchanger](http://controlguru.com/pid-control-of-the-heat-exchanger/)


# 18.03.2016
## DVCS
- [Moving and Renaming Files on GitHub](https://github.com/blog/1436-moving-and-renaming-files-on-github)
- [20. Moving files](https://githowto.com/moving_files)

## IoT
- [EMBEDDED](http://www.embedded.com/). Cracking the code to systems development
	- [PID without a PhD](http://www.embedded.com/design/prototyping-and-development/4211211/PID-without-a-PhD) by Tim Wescott, October 01, 2000. Можно искать в гугле полную pdf статью.

## iOS
- [Wacom Bamboo Stylus fineline](http://wacom.ru/styluses/fineline.html). Профессиональный инструмент для творческой личности.
Используйте в полной мере все возможности iPad®. Представляем принципиально новое перо Bamboo Stylus fineline! Благодаря этому высокоточному перу для создания заметок, рукописного ввода и зарисовок ваши идеи обретут крылья. Начните работу и посмотрите, как ведущие приложения* поддерживают Bamboo Stylus fineline:

# 17.03.2016
## MacOS
- [CrossOver](https://www.codeweavers.com/)
	- [CrossOver - запуск любых Windows программ под Mac OS](http://macintoshim.ru/emulators/crossover---zapusk-lyubyh-windows-programm-pod-mac-os.html)
	- [CrossOver 15](https://macx.ws/mac-os-unix/3200-crossover-15.html)

## IoT
- [Навигация в закрытых помещениях – от идеи до рабочего прототипа](http://www.dataart.ru/blog/2015/09/navigatsiya-v-zakry-ty-h-pomeshheniyah-ot-idei-do-rabochego-prototipa/)
- [Навигация в помещениях с iBeacon и ИНС](https://habrahabr.ru/post/245325/)
- [Системы локального позиционирования ](http://www.wless.ru/technology/?tech=11)
- [Indoor-навигация: Большой обзор iBeacon Hardware](https://habrahabr.ru/company/navigine/blog/269195/)
- [Фильтр Калмана — Введение](https://habrahabr.ru/post/140274/). Фильтр Калмана — это, наверное, самый популярный алгоритм фильтрации, используемый во многих областях науки и техники. Благодаря своей простоте и эффективности его можно встретить в GPS-приемниках, обработчиках показаний датчиков, при реализации систем управления и т.д.

## DS
- [A First Look at the Kalman Filter](http://www.quant-econ.net/jl/kalman.html)
- [Kalman filter example visualised with R](http://www.magesblog.com/2015/01/kalman-filter-example-visualised-with-r.html)
- [Measuring temperature with my Arduino](http://www.magesblog.com/2014/12/measuring-temperature-with-my-arduino.html)
- [Filtering Sensor Data with a Kalman Filter](http://interactive-matter.eu/blog/2009/12/18/filtering-sensor-data-with-a-kalman-filter/). December 18, 2009 in Tinkering


# 15.03.2016
- [SmartCat](http://www.smartcat.pro/ru/). Одно решение для всех переводческих задач. Эффективно. Технологично. Бесплатно.
	- [Сравнение сервисов Переводчик Google и ABBYY SmartCAT.Pro](https://startpack.ru/compare/google-translate/abbyy-smartcat-pro)

## IoT
- [Новостной портал Russia M2M News](http://www.m2mrussianews.com/)

# 10.03.2016
# Tools
- [Instant Logo Search](http://instantlogosearch.com/). Search & download thousands of logos instantly
# 09.03.2016
## DS
- [21 Must-Know Data Science Interview Questions and Answers](http://www.kdnuggets.com/2016/02/21-data-science-interview-questions-answers.html)
- [Jut](http://www.jut.io/). Jut is the company behind Juttle
Juttle is a powerful new open source dataflow language and streaming analytics platform.

Juttle can connect to multiple data back ends, easily run queries, perform sophisticated analytics, and enrich or join disparate data, to power smart alerting or compelling visualizations.

Deploy alongside your production infrastructure to drive dashboards or alerts, use the Juttle Engine to power application analytics, or embed client-side as part of your presentation layer.

# 04.03.2016
## R + Shiny
- Action Buttons
    - [Using Action Buttons](http://shiny.rstudio.com/articles/action-buttons.html). This article describes five patterns to use with Shiny’s action buttons and action links. Action buttons and action links are different from other Shiny widgets because they are intended to be used exclusively with `observeEvent()` or `eventReactive()`.
    - [Using Action Demo](http://shiny.rstudio.com/gallery/actionbutton-demo.html)
    - [Depricated Shiny Tutorial. Reactivity Overview](http://rstudio.github.io/shiny/tutorial/#reactivity-overview). It’s easy to build interactive applications with Shiny, but to get the most out of it, you’ll need to understand the reactive programming model used by Shiny.
    - [Using Leaflet with Shiny](https://rstudio.github.io/leaflet/shiny.html)

## R
- Functional Programming
    - [What's the difference between lapply and do.call in R?](http://stackoverflow.com/questions/10801750/whats-the-difference-between-lapply-and-do-call-in-r)
    - [funprog {base}](https://stat.ethz.ch/R-manual/R-devel/library/base/html/funprog.html). Common Higher-Order Functions in Functional Programming Languages
    - [Advanced R by Hadley Wickham: Functional programming](http://adv-r.had.co.nz/Functional-programming.html)


# 03.03.2016
## IoT
- [Open Source Hardware in the 1970s](https://dzone.com/articles/open-source-hardware-1970s-edition). How open source hardware has been kicking around since before the Internet, through popular magazines and manufacturing standards.
- [Five million pages of AM FM & TV Broadcasting history online](http://www.americanradiohistory.com/)

## Viz
- [Plot.ly in Shiny](http://www.showmeshiny.com/plot-ly-in-shiny/). Link ggplot2 plots to Plot.ly to create interactive, web-based plots drawn with D3.js and rendered with Shiny. Само приложение [здесь](https://plotly.shinyapps.io/plotly_in_shiny/)


## R tips
- [R function as() lapply() rbind() and do.call() for use in TweetFrame()](https://github.com/lmaccherone/Lumenize/issues/60)
    - as() performs a type coercion: in other words it changes one type to another type.
    - lapply() applies a function onto all of the elements of a list.
In the command below, lapply(tweetList, as.data.frame), applies the as.data.frame() coercion to each element in tweetList.
    - the rbind() function “binds” together the elements that are supplied to it into a row-by-row structure.
    - the do.call() function executes a function call, but unlike just running the function from the console, allows for a variable number of arguments to be supplied to the function.
The whole command we will use looks like this:
```
tweetDF <- do.call("rbind", lapply(tweetList, + as.data.frame))
```
    - as.data.frame() coerces each list element into a row
    - lapply() applies this to all of the elements in tweetList
    - rbind() takes all of the rows and puts them together
    - do.call() gives rbind() all the rows as individual elements

This takes a list of 500 tweet items (tweetList) and makes it a rectangular data frame. Each of the 500 tweet items had 10 fields, so now we can treat it as 500 observations of 10 variables.

Calling rbind this way sends the 500 results of lapply() to rbind to make one data frame instead of making each tweet into a list.

    TweetFrame() - Return a dataframe based on a  # search of Twitter
```
TweetFrame<-function(searchTerm, maxTweets)
{
twtList<-searchTwitter(searchTerm,n=maxTweets)
return(do.call("rbind",+  lapply(twtList,as.data.frame)))
}
```

- [as.data.frame.list: Convert a list of vectors to a data frame.](http://jason.bryer.org/TriMatch/docs/as.data.frame.list.html)
- [15 Easy Solutions To Your Data Frame Problems In R](https://www.datacamp.com/community/tutorials/15-easy-solutions-data-frame-problems-r)
- [R list to data frame](http://stackoverflow.com/questions/4227223/r-list-to-data-frame)
I have a nested list of data. Its length is 132 and each item is a list of length 20. Is there a quick way to convert this structure into a data frame that has 132 rows and 20 columns of data?

The package data.table has the function `rbindlist` which is a superfast implementation of `do.call(rbind, list(...))`.

It can take a list of lists, data.frames or data.tables as input.

- В ответ на предыдующее написана функция [as.data.frame.list.R](https://gist.github.com/jbryer/4676064)

# 02.03.2016
- [How InfluxDB Stores Data](http://grisha.org/blog/2015/03/20/influxdb-data/)
- [Blueflood](http://blueflood.io/) is a multi-tenant distributed metric processing system created by engineers at Rackspace. It is used in production by the Rackspace Monitoring team to process metrics generated by their monitoring systems. Blueflood is capable of ingesting, rolling up and serving metrics at a massive scale.

## R
- [Flatten a list. RosettaCode.org](https://rosettacode.org/wiki/Flatten_a_list)

# 01.03.2016
## MacOS
- [Copied](http://copiedapp.com/). A Full Featured Clipboard Manager for iOS and OS X.

## DS
- [lazyeval](https://github.com/hadley/lazyeval) by Hadley Wickham. 
Lazy evaluation is a principled way to do non-standard evaluation (NSE) in R. It is centered around formulas which capture an expression and the current environment.
- [rvest: easy web scraping with R](http://blog.rstudio.org/2014/11/24/rvest-easy-web-scraping-with-r/)
- [Hadley Wickham](http://hadley.nz/), Chief Scientist at RStudio, and an Adjunct Professor of Statistics at the University of Auckland.
	- [R for Data Science](http://r4ds.had.co.nz/). This is the book site for “R for data science”. This book will teach you how to do data science with R: You’ll learn how to get your data into R, get it into the most useful structure, transform it, visualise it and model it. In this book, you will find a practicum of skills for data science. Just as a chemist learns how to clean test tubes and stock a lab, you’ll learn how to clean data and draw plots—and many other things besides. These are the skills that allow data science to happen, and here you will find the best practices for doing each of these things with R. You’ll learn how to use the grammar of graphics, literate programming, and reproducible research to save time. You’ll also learn how to manage cognitive resources to facilitate discoveries when wrangling, visualizing, and exploring data. (R for Data Science was formally called Data Science with R in Hands-On Programming with R)

[**Big Data**](http://r4ds.had.co.nz/intro.html)
_Many big data problems are often small data problems **in disguise**_. Often your complete dataset is big, but the data needed to answer a specific question is small. It’s often possible to find a subset, subsample, or summary that fits in memory and still allows you to answer the question that you’re interested in. The challenge here is finding the right small data, which often requires a lot of iteration. We’ll touch on this idea in transform.

- [R Maps in Microsoft Power BI: Getting Started](https://dataveld.wordpress.com/2016/02/15/getting-started-with-r-maps-in-microsoft-power-bi/)
- [R Maps in Microsoft Power BI: Small Multiples](https://dataveld.wordpress.com/2016/02/18/r-maps-in-microsoft-power-bi-small-multiples/)

- [Sensu](https://sensuapp.org/). Monitoring for today's infrastructure. Monitor servers, services, application health, and business KPIs. Get notified about failures before your users do. Collect and analyze custom metrics. Give your business the competitive advantage it deserves.
- [Tools That Work With Graphite](http://graphite.readthedocs.org/en/latest/tools.html)
- [RainTank](http://raintank.io/)ю openSaaS monitoring from the team behind Grafana.


# 29.02.2016
## DS
- [Ваш персональный курс по Big Data](https://sohabr.net/habr/post/252743/)
- [Ваши вопросы о Data Science](https://sohabr.net/habr/post/259321/)
- [MLClass | Твой путь в DataScience](http://mlclass.ru/)
- [Demystifying Data Science: 4 Kinds of Data Science Jobs and 8 Skills that Will Get You Hired](http://blog.udacity.com/2014/11/data-science-job-skills.html)
- [Moscow Data Science](http://www.meetup.com/Moscow-Data-Science/). Группа для людей, занимающихся и/или интересующихся Data Science, анализом, майнингом и визуализацией структурированных и неструктурированных данных. Keywords: Data science, visualization, business analytics, predictive modeling, data mining, web analytics, business intelligence, computational finance, quant, operations research, machine learning, data analysis, data warehousing, text mining, BI.
- [Профессия Data Scientist: как не ошибиться с выбором](https://habrahabr.ru/company/airbnb/blog/237081/)
- [Sense.io](https://sense.io/). A Modern Platform for Data Science and Big Data Analytics.
Go beyond BI. Accelerate data science from exploration to production using R, Python, Spark and more. Deploy pipelines and models on-premise or in the cloud.

## MQQT
- [MQTT Essentials: Part 1 – Introducing MQTT](http://www.hivemq.com/blog/mqtt-essentials-part-1-introducing-mqtt)
- [MQTT Essentials Part 2: Publish & Subscribe](http://www.hivemq.com/blog/mqtt-essentials-part2-publish-subscribe)
- [MQTT Essentials Part 3: Client, Broker and Connection Establishment](http://www.hivemq.com/blog/mqtt-essentials-part-3-client-broker-connection-establishment)
- [MQTT Essentials Part 4: MQTT Publish, Subscribe & Unsubscribe](http://www.hivemq.com/blog/mqtt-essentials-part-4-mqtt-publish-subscribe-unsubscribe)
- [MQTT Essentials Part 5: MQTT Topics & Best Practices](http://www.hivemq.com/blog/mqtt-essentials-part-5-mqtt-topics-best-practices)
- [MQTT Essentials Part 6: Quality of Service 0, 1 & 2](http://www.hivemq.com/blog/mqtt-essentials-part-6-mqtt-quality-of-service-levels)
- [MQTT Essentials Part 7: Persistent Session and Queuing Messages](http://www.hivemq.com/blog/mqtt-essentials-part-7-persistent-session-queuing-messages)
- [MQTT Essentials Part 8: Retained Messages](http://www.hivemq.com/blog/mqtt-essentials-part-8-retained-messages)


# 26.02.2016
- [DevMate](http://devmate.com/) is 100% free now. App Development and Distribution Platform. Advanced Marketing Metrics & Analytics
- [Backblaze coupon](http://www.retailmenot.com/view/backblaze.com?c=7626828). 25% Off 1 Or 2 Year Subscription
- [Связной. Планшет Apple iPad Air 2 128Gb Wi-Fi + Cellular (серый)](http://www.svyaznoy.ru/catalog/notebook/7063/2200859)
- [Volter](http://www.volter.su). Стабилизаторы напряжения.
- [Энергия](http://energiya.msk.ru). Стабилизаторы напряжения.

## DS
- [DataRobot](https://www.datarobot.com/). If it's not DataRobot, it's not Data Science. The world's best data scientists have built the most advanced machine learning platform ever... for you.
- [The Fallacy of Sample Size](http://datadrivensecurity.info/blog/posts/2015/Nov/samplesize/)
- [Alteryx](http://www.alteryx.com/). The Leading Platform for Self-Service Data Analytics
- [Platfora](http://www.platfora.com/) is the leading full-stack big data discovery platform for Hadoop and Spark. We bring together traditionally separate tools to streamline and simplify data discovery.
	- [ESG Lab Review: End-to-end Big Data Discovery with Platfora](http://www.esg-global.com/lab-reports/esg-lab-review-end-to-end-big-data-discovery-with-platfora/)
- [CUBA](https://www.cuba-platform.ru/). Высокоуровневая Java платформа для создания корпоративных информационных систем
	- [YARG](https://www.cuba-platform.ru/YARG) — open-source библиотека для генерации отчётов
- [Webscraping. SSRMC lectures in Web Scraping, HT 2014](http://fredheir.github.io/WebScraping/)
- [Scrapy](http://scrapy.org/)
An open source and collaborative framework for extracting the data you need from websites. In a fast, simple, yet extensible way.

## IoT
- [PubNup](https://www.pubnub.com/). Realtime Apps Made Simple. The global data stream network for IoT, Mobile, and Web applications

# 25.02.2016
## Blogging
- [GitHub Pages](https://pages.github.com/). Websites for you and your projects.
Hosted directly from your GitHub repository. Just edit, push, and your changes are live.
- [Get Started With GitHub Pages (Plus Bonus Jekyll)](https://24ways.org/2013/get-started-with-github-pages/) by Anna Debenham
- [Jekyll + GitHub Pages](http://jekyllrb.com/docs/github-pages/)

## UI
- [CUBA platform](https://www.cuba-platform.ru/). Высокоуровневая Java платформа для создания корпоративных информационных систем

## IoT
- [ThingWorx](http://www.thingworx.com/). Платформа ThingWorx предоставляет полноценную интеллектуальную среду для разработки приложений, которую можно использовать в качестве среды выполнения, и обладает следующими характеристиками.
