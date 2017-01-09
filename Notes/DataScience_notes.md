- [Запчасти к мясорубке Zelmer](http://vaprom.ru/shop/c16.zelmer.htm)


# 09.01.2017

## Reports
- [Markdown to PDF](http://www.markdowntopdf.com/). Just select a file that contains some markup and we'll convert it to a pdf in a snap.

## R
- [The Most Important Commodity in 2017 is Data](https://rud.is/b/2017/01/04/the-most-important-commodity-in-2017-is-data/)
- [ReportLab](http://www.reportlab.com/). Generating PDFs from Wall Street to Wikipedia. 
We build solutions to generate rich, attractive and fully bespoke PDF documents at incredible speeds. Serve high quality personalised documents in real time and support all kinds of delivery from web downloads to digital print from a single API.

## Python
- [Creating PDF Reports with Pandas, Jinja and WeasyPrint](http://pbpython.com/pdf-reports.html)

# 29.12.2016
## R
- [Behind the scenes of CRAN](http://blog.h2o.ai/2016/12/behind-the-scenes-of-cran/). Just from my point of view as a package maintainer.
	Весьма интересно поглядеть про автотесты и поиск причины поломки. https://github.com/Rdatatable/data.table/blob/master/inst/tests/tests.Rraw#L444-L447
- [Authentication Proxy on Shiny Open Source](http://blog.datascienceheroes.com/authentication-proxy-on-shiny-open-source/)
- [Adding Authentication to Shiny Server in 4 Simple Steps](https://auth0.com/blog/adding-authentication-to-shiny-server/). Learn how to add authentication to your free Shiny Server setup and secure your interactive R apps!
	- [Auth0 + Shiny proxy](https://github.com/auth0/shiny-auth0). This server proxies a shiny instance protecting it with Auth0
	- [Auth0](https://auth0.com). Auth0 is an enterprise-grade platform for modern identity. We give you tools that eliminate the friction of authentication for your applications and APIs - all accessible through your account dashboard.
	- [Webtask](https://webtask.io/). All you need is code. Run code with an HTTP call. No provisioning. No deployment.
- [Shiny: Generating downloadable reports](https://shiny.rstudio.com/articles/generating-reports.html). After interacting with a Shiny application and getting it certain state, your users may want to download a report in HTML or PDF format. You can easily add the ability to generate a report with knitr and rmarkdown at the click of a button.
	- [PDF report download Demo app](http://shiny.rstudio.com/gallery/download-knitr-reports.html)
- [Top 10 things that suck about Sweave](https://www.r-bloggers.com/top-10-things-that-suck-about-sweave/). December 1, 2010
- [How to create PDF reports with R](http://blog.revolutionanalytics.com/2010/12/how-to-create-pdf-reports-with-r.html). December 01, 2010
- [Generate Report in R](http://stackoverflow.com/questions/37097535/generate-report-in-r)
- [create pdf reports in a loop (using latex and knitr) {duplicate}](http://stackoverflow.com/questions/25413091/create-pdf-reports-in-a-loop-using-latex-and-knitr)
```{r}
createReport <- function(xmlfile, Rnwfile) {
  ff <- parse xmlfile
  extract relevant data from ff
  calculate stats and generate tables and figures
  call knitr such that the correct variable names, stats, etc are fed into the Rnw file
  knit into a pdf file
  save the pdf file on disc
}
```
- [create pretty PDF report file in R](http://stackoverflow.com/questions/31054359/create-pretty-pdf-report-file-in-r)
- [Automated PDF reports using R Markdown](https://www.orchardplatform.com/blog/automated-pdf-reports-using-r-markdown-2/). **There are a few limitations, and LaTeX is a bit difficult to work with, but the R Markdown facility is by far the best PDF report builder that we have found so far.** Пример [отчетика](http://www.orchardplatform.com/wp-content/uploads/2015/09/Consumer-Unsecured-Quarterly-Profile.pdf)
- [Create PDF reports using R, R Markdown, LaTeX and knitr (on Windows 10)](https://medium.com/@sorenlind/create-pdf-reports-using-r-r-markdown-latex-and-knitr-on-windows-10-952b0c48bfa9)
- [Create multiple customized reports using latex, sweave, and R](https://www.linkedin.com/pulse/creating-repetitive-reports-using-latex-sweave-r-anissa-mike)


## Radio
- [Multimedia with LTE - real bonding instead of only Load Balancing](https://www.viprinet.com/en/technology/combinable-media/lte-4g)
- [Paplink MAX Multi-Cellular Router](http://www.peplink.com/products/max-cellular-router/multi-cellular/#M700). Quad USB Rugged Mobile Router
- [SpeedFusionTM Bonding Technology](http://www.peplink.com/technology/speedfusion-bonding-technology/)
- [Rerouting T1 signal over a wide area network](https://www.google.com/patents/US9094152)
- [Введение в LTE-Advanced](http://www.russianelectronics.ru/leader-r/review/2187/doc/56316/)
- [Building a Software-Defined Radio](http://www.digikey.com/en/articles/techzone/2014/feb/building-a-software-defined-radio)
- [Software-Defined Radio Solutions from Analog Devices](http://www.analog.com/media/en/news-marketing-collateral/solutions-bulletins-brochures/Software-Defined-Radio-Solutions-From-ADI.pdf)
- [OpenLTE](http://openlte.sourceforge.net/). OpenLTE is an open source implementation of the 3GPP LTE specifications.


# 27.12.2016
## R
- COOL! [Data Preparation, Long Form and tl;dr Form](http://www.win-vector.com/blog/2016/12/data-preparation-long-form-and-tldr-form/). Or alternately, below is the tl;dr (“too long; didn’t read”) form.
Our concrete advice is: when building a supervised model (regression or classification) in R, prepare your training, test, and application data by doing the following.
- COOL! [Why you should master R (even if it might eventually become obsolete)](http://sharpsightlabs.com/blog/master-r-obsolete)

# 26.12.2016
## R
- Материалы для обучения R. [Descriptive Analytics-Part 5: Data Visualisation (Spatial data)](http://r-exercises.com/2016/12/26/descriptive-analytics-part-5-data-visualisation-spatial/)
- [Functional programming and unit testing for data munging with R available on Leanpub](http://www.brodrigues.co/2016/12/24/functional-programming-and-unit-testing-for-data-munging-with-r-available-on-leanpub)

## Shiny
- [Googly: An interactive app for analyzing IPL players, matches and teams using R package yorkr](https://gigadom.wordpress.com/2016/12/25/googly-an-interactive-app-for-analyzing-ipl-players-matches-and-teams-using-r-package-yorkr/). Само приложение хостится [здесь](https://tvganesh.shinyapps.io/googly/)

# 23.12.2016
## R
- [Comparative examples using replyr:let](http://www.win-vector.com/blog/2016/12/comparative-examples-using-replyrlet/)


# 22.12.2016

## Games
- [REVIEW: SPACE FOOD TRUCK BY JP MARR 10 DEC 2016](http://www.pockettactics.com/reviews/review-space-food-truck/)
	- [OML has posted a series of video tutorials to YouTube](https://www.youtube.com/user/onemanleftstudios)
## R
- [Work on lists of datasets instead of individual datasets by using functional programming](http://www.brodrigues.co/2016/12/21/work-on-lists-of-datasets-instead-of-individual-datasets-by-using-functional-programming)
- [Inspecting R in GDB (with Python)](https://random-remarks.net/2016/12/21/inspecting-r-in-gdb-with-python/). Today I spent a few hours debugging a hanging R process that left a zombie sh which so far suggests bug (race condition?) in R’s system2() call.
- [R for Enterprise: How to Scale Your Analytics Using R](https://www.rstudio.com/rviews/2016/12/21/r-for-enterprise-how-to-scale-your-analytics-using-r/)

# 21.12.2016
## R
- Статья [Debugging Shiny applications](http://shiny.rstudio.com/articles/debugging.html)
- Презентация [Debugging with Shiny](http://rpubs.com/jmcphers/149638)
- [Shiny tips & tricks for improving your apps and solving common problems](http://deanattali.com/blog/advanced-shiny-tips/)
- [Using R packages and education to scale Data Science at Airbnb](https://medium.com/airbnb-engineering/using-r-packages-and-education-to-scale-data-science-at-airbnb-906faa58e12d)
- [ggplot2 tech themes, scales, and geoms https://twitter.com/ricardobion](https://github.com/ricardo-bion/ggtech)

# 20.12.2016
## Math
- [Среднеквадратическая ошибка модели. RMSE\MSE](http://statistica.ru/glossary/general/srednekvadraticheskaya-oshibka/)
- [Среднеквадратичная ошибка (RMSE)](http://gis-lab.info/qa/rmse.html). Краткое объяснение что такое RMSE применительно к данным ДЗЗ
- [Compare R-squared from two different Random Forest models](http://stats.stackexchange.com/questions/13869/compare-r-squared-from-two-different-random-forest-models)

## R
- [Baseline Characteristics Tables with qwraps2](http://www.peteredewitt.com//2016/summary-table/)
- [Secondary Axis in ggplot2 v2.2.0](http://www.peteredewitt.com/2016/secondary-axis-ggplot2-v2.2.0/)
### Gantt Charts
- COOL! [Gantt charts with R](http://stackoverflow.com/questions/3550341/gantt-charts-with-r). Подборка различных методик.
- COOL! [Revisiting Gantt Charts](http://mescal.imag.fr/membres/arnaud.legrand/blog/2013/03/20/revisiting-gantt-charts.php)
- [Gantt charts in R](http://lazappi.id.au/gantt-charts-in-r/). Using DiagrammeR/mermaid
- [Gantt Chart in R](https://rpubs.com/mramos/ganttchart). Using plotrix
- [PlotPrjNetworks](https://cran.r-project.org/web/packages/PlotPrjNetworks/index.html): Useful Networking Tools for Project Management
- [Plotting “time of day” data using ggplot2](https://nsaunders.wordpress.com/2010/04/14/plotting-time-of-day-data-using-ggplot2/)
- [Gantt Charts in R using Plotly](http://moderndata.plot.ly/gantt-charts-in-r-using-plotly/)
- [vis.js](http://visjs.org/). A dynamic, browser based visualization library. The library is designed to be easy to use, to handle large amounts of dynamic data, and to enable manipulation of and interaction with the data. The library consists of the components DataSet, Timeline, Network, Graph2d and Graph3d.
- [TimelineJS](http://timeline.knightlab.com/). Beautifully crafted timelines that are easy and intuitive to use.
- [Variance charts](https://variancecharts.com/). Build powerful data visualizations for the web. Without writing JavaScript. Timeline.
Variance empowers engineers, designers, journalists, scientists, and analysts to build elegant bespoke data graphics for the web, using only HTML & CSS. Our intuitive, markup-based grammar emphasizes clear, practical graphics and serves as the foundation for a wide range of visualizations.
- Другие инструменты. [What open source or free tool makes beautiful Gantt Charts?](https://www.quora.com/What-open-source-or-free-tool-makes-beautiful-Gantt-Charts)
	- [Online Gantt Chart Software](http://www.teamgantt.com/)
	- [Office timeline](https://www.officetimeline.com/)
- COOL! [10 Unmissable Tools for the Gantt Chart Guru](http://www.eventmanagerblog.com/tools-gantt-chart/)
- [Instagantt](https://instagantt.com/). Gantt Charts for Asana
- [GanttProject](http://www.ganttproject.biz/index.php). Free project scheduling and management app for Windows, OSX and Linux.
- [Gantic](http://www.ganttic.com/tour). Ganttic is a resource planning software for the big and the small. It gets things done.
- [Liquid Planner](https://www.liquidplanner.com/). Good Teams Plan. Great Teams Execute. Try the only Dynamic Project Management solution designed for fast-moving teams.
- [Gantter](http://gantter.com/). FREE cloud-based project scheduling.

## DS
- [What is rosettaHUB?](https://www.rosettahub.com/welcome) A revolutionary cloud-native platform designed to empower data scientists, researchers and educators who need virtual, collaborative and traceable access to data science tools and infrastructures


# 19.12.2016
## Windows
- [AutoHotkey (AHK)](https://autohotkey.com/) is a free, open-source macro-creation and automation software for Windows that allows users to automate repetitive tasks.
- [Determining which program trapping which hot key shortcut](http://superuser.com/questions/219629/determining-which-program-trapping-which-hot-key-shortcut)
- [Hotkey Commander (Abbreviation HC)](http://hkcmdr.anymania.com/index.html) is a powerful hotkey managing and overriding tool for Windows®. If you are a frequent hotkey user, you may found that while hotkeys bring much convenience and advantages, they act rudely and annoyingly sometimes. Hotkeys are usually defined or registered by individual applications. Some moral applications would allow users to redefine their hotkey combination so that they don't conflict with other hotkeys. Some "evil" applications won't at all. No matter what more and more hotkeys may become chaos and make you confused at last. Even if you don't use hotkeys at all, you may want to disable or override hotkeys occasionally so as not to be interrputed by their default actions.

## R
- [Minding the zoo{keeper} with R](https://rud.is/b/2016/12/16/minding-the-zookeeper-with-r/)
- [R graphs and tables in Power BI Desktop](https://tomaztsql.wordpress.com/2016/12/18/r-graphs-and-tables-in-power-bi-desktop/)
- COOL! [SPEED UP YOUR CODE: PARALLEL PROCESSING WITH MULTIDPLYR](http://www.mattdancho.com/code-tools/2016/12/18/multidplyr.html)
- [hadley/multidplyr. Partitioned data frames for 'dplyr'](https://github.com/hadley/multidplyr)
- [Using googlesheets and mailR packages in R to automate reporting](http://pacha.hk/googlesheets_automatic_reporting.html)
- [Customizable defaults for Positioning Functions](http://directlabels.r-forge.r-project.org/examples.html)/. Не совсем в идеологии ggplot.

## DS
- [Why Type 1 errors are more important than Type 2 errors (if you care about evidence)](http://daniellakens.blogspot.ru/2016/12/why-type-1-errors-are-more-important.html)

# 16.12.2016
## Shiny
- [Dynamically generated Shiny UI](http://www.mango-solutions.com/wp/2016/12/dynamically-generated-shiny-ui/) 15 Dec 16, Gábor Csárdi — Mango Solutions
- COOL! [ggplot2 graph quality in shiny on shinyapps.io](http://stackoverflow.com/questions/26285786/ggplot2-graph-quality-in-shiny-on-shinyapps-io).
- [R Shiny server not rendering correct ggplot font family](http://stackoverflow.com/questions/31859911/r-shiny-server-not-rendering-correct-ggplot-font-family)
Just a guess, try including `library(Cairo);options(shiny.usecairo=TRUE)` in your server.R or in global.R.
- [Shiny 0.12: Interactive Plots with ggplot2](https://blog.rstudio.org/2015/06/16/shiny-0-12-interactive-plots-with-ggplot2/)
You can use mouse events to read mouse coordinates, select or deselect points, and implement zooming. Here are some example applications:
	- [Basic interactions](http://shiny.rstudio.com/gallery/plot-interaction-basic.html)
	- [Zooming](http://shiny.rstudio.com/gallery/plot-interaction-zoom.html)
	- [Advanced interactions: This demonstrates many advanced features of interactive plots.](http://shiny.rstudio.com/gallery/plot-interaction-advanced.html)
	- [Excluding points {as depicted in the screen capture above}](http://shiny.rstudio.com/gallery/plot-interaction-exclude.html)
- [Selecting rows of data](http://shiny.rstudio.com/articles/selecting-rows-of-data.html)
- [Shiny Interactive plots articles](http://shiny.rstudio.com/articles/#interactive-plots)
- [Shiny + GGplot - mouse click coordinates](http://stackoverflow.com/questions/30781379/shiny-ggplot-mouse-click-coordinates)
	- [Global options for Shiny](https://shiny.rstudio.com/reference/shiny/latest/shiny-options.html)
- [Debugging Shiny applications](http://shiny.rstudio.com/articles/debugging.html). `options(shiny.error = browser)` Showcase Mode!!!
- [showcase display mode for published app in shinyapps.io](http://stackoverflow.com/questions/26291523/showcase-display-mode-for-published-app-in-shinyapps-io)
You can provide information about your app that Shiny showcase will use by creating a DESCRIPTION file.
- [Scoping rules for Shiny apps](https://shiny.rstudio.com/articles/scoping.html)
- [Shiny Display modes](http://shiny.rstudio.com/articles/display-modes.html)
- [Effectively debugging Shiny apps](http://stackoverflow.com/questions/31920286/effectively-debugging-shiny-apps)
- [Display element ids for debugging Shiny apps](http://blog.mckuhn.de/2016/04/display-element-ids-for-debugging-shiny.html)

## R
- При использовании 'geom_nodelabel_repel'(`ggnetwork`) возникает следующая ошибка: "Ignoring unknown parameters: segment.color"
	- [ggrepel: plot labels above points](http://stackoverflow.com/questions/39943123/ggrepel-plot-labels-above-points/39947042#39947042)
	- [geom_nodetext_repel](https://www.rdocumentation.org/packages/ggnetwork/versions/0.5.1/topics/geom_nodetext_repel) From ggnetwork v0.5.1. Draw Repulsive Node Labels. All arguments to these geoms are identical to those of geom_text_repel and geom_label_repel.
Да все потому что ПЕРЕИМЕНОВАЛИ `segment.color` в `segment.coloUr`
- Разобрался с ошибкой в geom_edgetext. Надо ставить из github `devtools::install_github("briatte/ggnetwork")`, там ошибка исправлена: 
[avoid removal of perfectly orthogonal edges (closes #5) ](https://github.com/briatte/ggnetwork/commit/8b7043fd05fa1eb5702a7aab6ede1e6afb5d1e9d)
- COOL! [10 tips for making your R graphics look their best](http://blog.revolutionanalytics.com/2009/01/10-tips-for-making-your-r-graphics-look-their-best.html)
- COOL! [Exporting nice plots from R](http://gforge.se/2013/02/exporting-nice-plots-in-r/) A vital part of statistics is producing nice plots, an area where R is outstanding. The graphical ablility of R is often listed as a major reason for choosing the language. It is therefore funny that exporting these plots is such an issue in Windows. This post is all about how to export anti-aliased, high resolution plots from R in Windows.
См. пункт "lines and text anti-aliased - not fills/polygons"
- [How to plot smoother curves in R](http://stackoverflow.com/questions/15447622/how-to-plot-smoother-curves-in-r)
- [imager: an R package for image processing](http://dahtah.github.io/imager/imager.html)
- Работа с графом. Соседи, соединительные грани, пути.
	- [neighbors function in igraph package in R](http://stackoverflow.com/questions/29096085/neighbors-function-in-igraph-package-in-r)
	- [igraph edge between two vertices](http://stackoverflow.com/questions/12964332/igraph-edge-between-two-vertices)
	- [igraph get edge from - to value](http://stackoverflow.com/questions/21243965/igraph-get-edge-from-to-value)
	- [How to get id vertex from name vertex in R and Igraph?](http://stackoverflow.com/questions/10124168/how-to-get-id-vertex-from-name-vertex-in-r-and-igraph)
- [igraph R Traps](http://igraph.wikidot.com/r-traps)
- [ggpmisc 0.2.13. Debugging ggplots](https://cran.r-project.org/web/packages/ggpmisc/vignettes/debug.html)

- igraph manual !!!
It is often desirable to follow vertices along a number of graph operations, and vertex ids don’t
allow this because of the renumbering. The solution is to assign attributes to the vertices. These are
kept by all operations, if possible. See more about attributes in the next section.

# 15.12.2016
## English
- [Обучающие мультфильмы на английском](http://www.english-cartoons.ru/educationalenglishcartoons.html)

## R
- [Современное прогнозирование. Использование R](http://forecasting.svetunkov.ru/using-r/)
- Проблема со структурой data.frame, полученного с помощью `ggnetwork`. вместо векторов создаются матрицы nx1.
[Can't mutate despite object as data.frame](http://stackoverflow.com/questions/38328609/cant-mutate-despite-object-as-data-frame)
	- [R-friendly way to convert R data.frame column to a vector?](http://stackoverflow.com/questions/7070173/r-friendly-way-to-convert-r-data-frame-column-to-a-vector)
	- [Change the class of many columns in a data frame](http://stackoverflow.com/questions/3796266/change-the-class-of-many-columns-in-a-data-frame)
	- [How to convert data.frame column from Factor to numeric {duplicate}](http://stackoverflow.com/questions/27528907/how-to-convert-data-frame-column-from-factor-to-numeric)
	- [How to convert a factor to an integer\numeric without a loss of information?](http://stackoverflow.com/questions/3418128/how-to-convert-a-factor-to-an-integer-numeric-without-a-loss-of-information)
	- [R -apply- convert many columns from numeric to factor](http://stackoverflow.com/questions/34124444/r-apply-convert-many-columns-from-numeric-to-factor)
- [How to normalize data to 0-1 range?](http://stats.stackexchange.com/questions/70801/how-to-normalize-data-to-0-1-range)
	-  if you have `clusterSim` package, Simply do - `normX = data.Normalization(x, type="n4");`
- [Scale a series between two points](http://stackoverflow.com/questions/5468280/scale-a-series-between-two-points)
	- `scale(x,center=min(x),scale=diff(range(x)))`
	- `rescale(s, to=c(0,10))`
	- `rescale(s, from=c(0, max(s)))`

# 14.12.2016
## Медицина
1 шт. Беродуал Н аэр д/ингал 200доз 10мл Boehringer Ingelheim	Германия	484,00
2 шт. Вильпрафен таб покр пл/о 500мг №10 Астеллас Фарма/Теммлер Верке ГмбХ	Германия	527,00
1 шт. Кораксан таб п/о 7,5мг №56 Servier/Сердикс ООО	Россия	1170,49
1 шт. Валокордин капли 50мл Krewel Meuselbach	Германия	231,00

## R
- [CCTZ is a C++ library for translating between absolute and civil times using the rules of a time zone](http://dirk.eddelbuettel.com/blog/2016/12/12/#rcppcctz_0.1.0)
- [nanotime 0.0.1: New package for Nanosecond Resolution Time for R](http://dirk.eddelbuettel.com/blog/2016/12/16/#nanotime_0.0.1)

## R Interactive plots
- [Interactive plots](https://shiny.rstudio.com/articles/plot-interaction.html)
- [Interactive plotting in shiny using mouse clicks](http://stackoverflow.com/questions/28023342/interactive-plotting-in-shiny-using-mouse-clicks)
- [Interactive hovering Shiny graphs](http://stackoverflow.com/questions/32251987/interactive-hovering-shiny-graphs)
- [Plot Interaction Zoom](https://gallery.shinyapps.io/105-plot-interaction-zoom/)
- [How to add a background image to ggplot2 graphs](http://datascienceplus.com/how-to-add-a-background-image-to-ggplot2-graphs/)
- COOL! [R ggplot background image not showing](http://howtoprogram.eu/question/r-ggplot-background-image-not-showing,17169)
- [The 'rsvg' Package: High Quality Image Rendering in R](https://www.opencpu.org/posts/svg-release/)
- [Introduction to cowplot](https://cran.r-project.org/web/packages/cowplot/vignettes/introduction.html). The cowplot package is a simple add-on to ggplot2.
- [Crime in Downtown Houston, Texas : Combining ggplot2 and Google Maps](https://github.com/tidyverse/ggplot2/wiki/crime-in-downtown-houston,-texas-:-combining-ggplot2-and-google-maps)
- [Annotating Plots](http://chrisalbon.com/r-stats/annotating-plots.html)
- [Plot labels at ends of lines](http://stackoverflow.com/questions/29357612/plot-labels-at-ends-of-lines)
- [R package grid disappeared?](http://stackoverflow.com/questions/29349398/r-package-grid-disappeared) According to the [grid changelog](https://stat.ethz.ch/R-manual/R-devel/library/grid/doc/changes.txt), it became a base package with version 1.8.0. Therefore, it no longer needs to be available on the CRAN repository.
- COOL! [Network visualization with R](http://kateto.net/network-visualization). Тут, кстати, есть ссылка на хорошую версию в PDF. Почти то же самое, но в статике: [Network Analysis and Visualization with R and igraph](http://kateto.net/networks-r-igraph). 
- [USC Annenberg Networks Network: A Prezi Introduction](http://kateto.net/2011/01/usc-annenberg-networks-network-an-introduction/)
- [R igraph manual pages](http://igraph.org/r/doc/). Use this if you are using igraph from R
	- [Layouts](www.londonr.org/download/?id=97), стр 41.
A layout is just a set of x and y coordinates. They can be specified manually but more often we will use
one of the layout_ functions.
- COOL! [Preparing Network Data in R](http://www.mjdenny.com/Preparing_Network_Data_In_R.html)
- [Going viral with R's igraph package](http://blog.ryanwalker.us/2014/03/going-viral-with-rs-igraph-package.html)
- COOL! [ggnetwork: Network geometries for ggplot2](https://cran.r-project.org/web/packages/ggnetwork/vignettes/ggnetwork.html)
	- [gplot.layout From sna](http://www.rdocumentation.org/packages/sna/functions/gplot.layout) Vertex Layout Functions For Gplot. Various functions which generate vertex layouts for the gplot visualization routine.
	- COOL! [A guide to the gplot layout algorithms of the sna library for R](http://www.melissaclarkson.com/resources/R_guides/documents/gplot_layout_Ver1.pdf)
- [How to control the igraph plot layout with Fixed Positions?](http://stackoverflow.com/questions/5364264/how-to-control-the-igraph-plot-layout-with-fixed-positions)
- разбираем принцип устройства ggnetwork::fortify.network: https://github.com/briatte/ggnetwork/blob/0e572df0d3a715416a3ed08de598042b76f0537c/R/fortify-network.R
Вроде как можно просто матрицу подсунуть!: `class(layout) == "matrix" &&`
- COOL! [sctyner/geomnet](https://github.com/sctyner/geomnet). geomnet is a package built on top of the most recent major ggplot2 release. It provides a ggplot2 geom called geom_net to visualize graphs and networks.
- [R code for igraph animation](http://www.joyofdata.de/blog/r-code-for-igraph-animation/)
- [More network analysis with igraph and Cytoscape](https://rpubs.com/keiono/cyrest3)
- [From igraph to network and back again](https://brokeringclosure.wordpress.com/2010/08/25/from-igraph-to-network-and-back-again/)
- [Short tutorial on using functions in package "intergraph"](https://cran.r-project.org/web/packages/intergraph/vignettes/howto.html)
- [Intergraph](http://mbojan.github.io/intergraph/) R package with coercion routines for network data objects
	- [Short tutorial on using functions in package “intergraph”](http://mbojan.github.io/intergraph/howto.html#network-igraph)
- COOL! [Interactive and Dynamic Network Visualization in R](http://curleylab.psych.columbia.edu/netviz/). slides from my NYC R Meetup Talk on 6th April 2016.
- COOL! [Examples for the igraph package](http://michael.hahsler.net/SMU/LearnROnYourOwn/code/igraph.html)

# 13.12.2016
## R
- [Taking a Subset of a Data Frame in R](https://qualityandinnovation.com/2016/12/13/taking-a-subset-of-a-data-frame-in-r/)
- COOL! [(A Very) Experimental Threading in R](https://random-remarks.net/2016/12/11/a-very-experimental-threading-in-r/)
- [THREADING IN R?](https://matloff.wordpress.com/2016/12/11/threading-in-r/)
- [pqR - a pretty quick version of R](http://www.pqr-project.org/)
- [Chaos, bifurcation diagrams and Lyapunov exponents with R (2)](http://a-blog-from-sydney.blogspot.ru/2016/12/chaos-bifurcation-diagrams-and-lyapunov.html)
- [Using PostgreSQL in R: A quick how-to](http://www.win-vector.com/blog/2016/02/using-postgresql-in-r/)
- [The Case For Using -> In R](http://www.win-vector.com/blog/2016/12/the-case-for-using-in-r/)

## Dev
- [RawGit](http://rawgit.com/) serves raw files directly from GitHub with proper Content-Type headers.
# 12.12.2016
## R
- [Don’t give up on single trees yet…. An interactive tree with Microsoft R](https://longhowlam.wordpress.com/2016/12/10/dont-give-up-on-single-trees-yet-an-interactive-tree-with-microsoft-r/)
- COOL! [The case for index-free data manipulation](http://www.win-vector.com/blog/2016/12/the-case-for-index-free-data-manipulation/)
SQL is actually a rich modeling environment with interesting semantics due to its relation to E.F. Codd’s relational model. However, working with SQL databases presents a number of practical difficulties.
- COOL! [Grid search in the tidyverse](https://drsimonj.svbtle.com/grid-search-in-the-tidyverse). For anyone who’s unfamiliar with the term, grid search involves running a model many times with combinations of various hyperparameters. The point is to identify which hyperparameters are likely to work best. A more technical definition from Wikipedia, grid search is:

an exhaustive searching through a manually specified subset of the hyperparameter space of a learning algorithm
- [Creating beautiful charts in chinese with ggplot2](http://pacha.hk/ggplot2_chinese.html)
- [XLConnect: Excel Connector for R. Provides comprehensive functionality to read, write and format Excel data](https://cran.r-project.org/web/packages/XLConnect/index.html)

## IoT
- [Создание интеллектуальных датчиков с использованием сервисов Bluemix Business Rules, Watson IoT Platform и Insights for Weather](https://www.ibm.com/developerworks/ru/library/bpm/1604_siddiqui-bluemix-trs/)
- [OpenLoRa](http://openlora.com/forum/)
- [Lora-net/LoRaMac-node](https://github.com/Lora-net/LoRaMac-node). Reference implementation and documentation of a LoRa network node. The LoRaWAN stack API documentation can be found at: [http://stackforce.github.io/LoRaMac-doc/](http://stackforce.github.io/LoRaMac-doc/)
- [Gateway IMST IC880A / RBPI](https://www.thethingsnetwork.org/forum/t/gateway-imst-ic880a-rbpi/134)
- [TheThingsNetwork/lora_gateway](https://github.com/TheThingsNetwork/lora_gateway). Driver/HAL to build a gateway using a concentrator board based on Semtech SX1301 multi-channel modem and SX1257/SX1255 RF transceivers.
- [TheThingsNetwork/packet_forwarder](https://github.com/TheThingsNetwork/packet_forwarder). A LoRa packet forwarder is a program running on the host of a LoRa gateway that forwards RF packets receive by the concentrator to a server through a IP/UDP link, and emits RF packets that are sent by the server.
- COOL! [Building your LoRa devices](http://cpham.perso.univ-pau.fr/LORA/LoRaDevices.html)
- COOL! [From zero to LoRaWAN in a weekend](https://github.com/ttn-zh/ic880a-gateway/wiki)
- [iC880A - LoRaWAN Concentrator 868MHz](http://www.wireless-solutions.de/products/radiomodules/ic880a)
- [LoRa Modems and Modules](https://www.loriot.io/lora-end-nodes.html). Our aim is to support all the LoRaWAN compliant modems in the LoRa ecosystem. We suggest using either the manufacturer's stack or adapting the IBM's LMiC implementation of the LoRaWAN end device protocol.
- [Address Space in LoRaWAN](https://www.thethingsnetwork.org/wiki/LoRaWAN/Address-Space)
- [IEEE Guidelines for 64-bit Global Identifier (EUI-64)](http://standards.ieee.org/develop/regauth/tut/eui64.pdf)
- [A Closer Look at LoRaWAN and The Things Network](https://www.rs-online.com/designspark/a-closer-look-at-lorawan-and-the-things-network)
- [The Things Network with the Moteino and RN2483](https://github.com/lukastheiler/ttn_moteino)


# 09.12.2016
## Arduino
- [Я презираю Arduino](https://geektimes.ru/post/255760/)
- [Arduino Pro Mini](http://arduino.ru/Hardware/ArduinoBoardProMini) или [тут](http://arduino-diy.com/arduino-pro-mini)
- [Arduino Pro Mini (Eng)](https://www.arduino.cc/en/Main/ArduinoBoardProMini)
- [Интерфейс I2C](http://robocraft.ru/blog/communication/780.html)
- [Описание шины I2C](http://www.itt-ltd.com/reference/ref_i2c.html)
- [Термистор и Arduino](http://arduino-diy.com/arduino-thermistor)


## R
### Tasks
- Проблема с импортом Excel файла (Пермяков). Ошибка "Error: Need one name and type for each column". Тикет открыт: [Error using col_names and col_types](https://github.com/hadley/readxl/issues/81)
Да, импортируется пустая последняя колонка....

Ищем в тексте внутри гитхаба:
https://github.com/hadley/readxl/search?utf8=%E2%9C%93&q=Need+one+name+and+type+for+each+column
Если покопаться поглубже, то выплывают blank колонки в еще большем числе
ctypes <- readxl:::xlsx_col_types(datafile) дает 152 против 148 видимых. Связано это с тем, что у этих 4-х колонок изменено форматирование.


### R as web-service
- [Calling R as a web service with parameters and load a JSON?](http://stackoverflow.com/questions/30141204/calling-r-as-a-web-service-with-parameters-and-load-a-json)
- [How do I expose R code as a web service?](https://www.quora.com/How-do-I-expose-R-code-as-a-web-service)
Hadley Wickham, Chief Scientist, RStudio:
There are quite a few packages that will help you do this, but I can’t remember all their names off the top of my head (and I’m sure you’re just as good at googling as I am). The one that I’d start with is plumbr, by Jeff Allen (Jeff works at RStudio with me, but this is a personal project, not an official RStudio project).
- [plumber](https://github.com/trestletech/plumber) allows you to create a REST API by merely decorating your existing R source code with special comments. Take a look at an example.
- [Quickstart: Add your first R function to Blockspring](https://www.blockspring.com/docs/r-quickstart)
- [CRAN Task View: Web Technologies and Services](https://cran.r-project.org/web/views/WebTechnologies.html)
- [Microsoft/deployr-rserve](https://github.com/Microsoft/deployr-rserve/releases)
- [FastRWeb - Fast Interactive Web Framework for Data Mining Using R](https://rforge.net/FastRWeb/). Infrastrcture for creating rich, dynamic web content using R scripts while maintaining very fast response time. CRAN [page](https://cran.r-project.org/web/packages/FastRWeb/index.html)
- [OpenCPU](https://www.opencpu.org/) - an API for Embedded Scientific Computing.
	- [Introduction to OpenCPU for R on EC2 with Python](http://www.joyofdata.de/blog/introduction-to-opencpu-for-r-on-ec2-with-python/)
	- [How to run a custom.R script using OpenCPU](http://stackoverflow.com/questions/37978834/how-to-run-a-custom-r-script-using-opencpu)
	- [Send an image file using opencpu for processing](http://stackoverflow.com/questions/29211599/send-an-image-file-using-opencpu-for-processing)
OpenCPU is a system for embedded scientific computing and reproducible research. The OpenCPU server provides a reliable and interoperable HTTP API for data analysis based on R. You can either use the public servers or host your own.
- [Jug is a small web development framework for R which relies heavily upon the httpuv package. It’s main focus is to make building APIs for your code as easy as possible.](https://cran.r-project.org/web/packages/jug/vignettes/jug.html)

### Shiny
- [Arrow72/CoolDashboard](https://github.com/Arrow72/CoolDashboard). R dashboard as a designer http://ru-datascience.ru/2015/10/28/dizajnerskij-dashboard/
- [R: How to Layout and Design an Infographic](http://alstatr.blogspot.ru/2015/02/r-how-to-layout-and-design-infographic.html)
- [Cairo](https://cran.r-project.org/web/packages/Cairo/index.html) graphics device that can be use to create high-quality vector (PDF, PostScript and SVG) and bitmap output (PNG,JPEG,TIFF), and high-quality rendering in displays (X11 and Win32).


## Python
- COOL! [PYTHON FOR EXCEL. FREE & OPEN SOURCE](https://www.xlwings.org/)
- [vinta/awesome-python](https://github.com/vinta/awesome-python). A curated list of awesome Python frameworks, libraries, software and resources http://awesome-python.com/
- [ПИТОНТЬЮТОР](http://pythontutor.ru/). УЧИТЕ ПИТОН. Бесплатный курс по программированию с нуля. Работает прямо в браузере.

# 08.12.2016

## Operationalization = DeployR on Windows R Server 9.0.1
1. [Включаем иконки на рабочем столе Win 2012 Serer](http://did5.ru/it/windows/kak-dobavit-ikonku-kompyuter-na-rabochij-stol-v-windows-server-2012.html)
1. Инсталлируем R Server (вопросы с лицензией пока открыты)
1. [Настраиваем DeployR](https://msdn.microsoft.com/en-us/microsoft-r/operationalize/configuration-initial)
1. [Запускаем диагностику](https://msdn.microsoft.com/en-us/microsoft-r/operationalize/admin-utility#test)

## R
- [Visualizing 15k Instagram Posts with TrelliscopeJS](http://ryanhafen.com/blog/insta-trelliscopejs)
- [Pipe Dream. Plusses and Arrows and Percents, oh my!]()https://dariustg.github.io/2016/12/pipe-dream.html)
- [Automating R Demonstration Videos](https://www.stat.auckland.ac.nz/~paul/Reports/Video/PoC/video-poc.html)
- [Using replyr::let to Parameterize dplyr Expressions](http://www.win-vector.com/blog/2016/12/using-replyrlet-to-parameterize-dplyr-expressions/)
- [Structural Equation Modelling in R (Part 1)](http://pacha.hk/sem_r_part_1.html)
- [Getting started with Microsoft R Client is as easy as 1-2-3](https://msdn.microsoft.com/en-us/microsoft-r/r-client-get-started)

## Development
- [DeepGit is a tool to investigate the history of source code. It is based on git blame and makes it easy to trace changes to a line or block of code. DeepGit will detect code movements, even if lines are not identical.](http://www.syntevo.com/deepgit/?referrer=program&edition=foundation)

## Microsoft
- [Как добавить иконку Компьютер на рабочий стол в Windows Server 2012](http://did5.ru/it/windows/kak-dobavit-ikonku-kompyuter-na-rabochij-stol-v-windows-server-2012.html)
- [Microsoft R Client provides a free taste of R Server](http://www.infoworld.com/article/3094828/data-science/microsoft-r-client-provides-a-free-taste-of-r-server.html). It's limited in power, but low in price: R Client provides a reduced but functional set of features from the full Microsoft R Server product
- [Installing DeployR for Microsoft R Server 2016 (8.0.5) on Windows](https://msdn.microsoft.com/en-us/microsoft-r/deployr-install-on-windows)
- [Configuring R Server for Operationalization](https://msdn.microsoft.com/en-us/microsoft-r/operationalize/configuration-initial). Operationalization = DeployR.
- [mrsdeploy Remote Execution functions in Microsoft R (vignette)](https://msdn.microsoft.com/en-us/microsoft-r/mrsdeploy/mrsdeploy-remoteexec-vignette)
- [Comparing Operationalization in R Server 9.0 to DeployR 8.x](https://msdn.microsoft.com/en-us/microsoft-r/operationalize/about-compare-to-8.0.5)
- [Microsoft R Server 9.0.1](https://my.visualstudio.com/downloads)
	- [Operationalization with R Server](https://msdn.microsoft.com/en-us/microsoft-r/operationalize/about)
А вот, что обнаружилось в EULA при инсталляции отдельного дистрибутива Microsoft R Server 9.0.1:
```
Microsoft R Server for Windows, supplement to Microsoft SQL Server 2016 Enterprise Core
PLEASE NOTE: Refer to your license terms for Microsoft SQL Server 2016 Enterprise Core software (the “software”) to identify the entity licensing this supplement to you and for support information. You may use a copy of this supplement with each validly licensed copy of the software. You may not use this supplement if you do not have (a) a valid license or subscription to the software, and (b) active Software Assurance covering the software. The license terms for the software apply to your use of this supplement.
```


# 07.12.2016
## DS
- [Deep Learning Cheat Sheet](https://hackernoon.com/deep-learning-cheat-sheet-25421411e460)
- mermaid Diagrams and flowcharts from textsimilar to markdown. [Gant diagrams](http://knsv.github.io/mermaid/gantt.html)
- [Gantt Charts in R using Plotly](http://moderndata.plot.ly/gantt-charts-in-r-using-plotly/)
- [Generating an interactive Gantt/timeline chart in R](https://www.packtpub.com/mapt/book/Big-Data-and-Business-Intelligence/9781783989508/2/ch02lvl1sec34/Generating%20an%20interactive%20Gantt/timeline%20chart%20in%20R)
- [MPP to XLS online converter](http://www.zamzar.com/convert/mpp-to-xls/). Convert MPP to XLS - Convert your file now - online and free - this page also contains information on the MPP and XLS file extensions.

# 06.12.2016
## R
- [Optimization matchup: R's glpkAPI vs Julia's JuMP](http://rsnippets.blogspot.ru/2016/12/optimization-matchup-rs-glpkapi-vs.html)
- [How to Get paid Udemy courses for free?](https://www.quora.com/How-to-Get-paid-Udemy-courses-for-free)
- [Creating and Hosting a Personal Site on GitHub](http://jmcglone.com/guides/github-pages/). A step-by-step beginner's guide to creating a personal website and blog using Jekyll and hosting it for free using GitHub Pages.

# 05.12.16
## R
- [How to set up your own R blog with Github pages and Jekyll Bootstrap](https://shiring.github.io/blogging/2016/12/04/diy_your_own_blog)
	- [Jekyll Installation](http://jekyllrb.com/docs/installation/). Getting Jekyll installed and ready-to-go should only take a few minutes.
- [bookdown: Authoring Books and Technical Documents with R Markdown](https://bookdown.org/yihui/bookdown/)
- [Introduction of the pdfsearch package](http://educate-r.org//2016/12/02/intro_pdfsearch.html)
- COOL! [Relational operators for intervals with the intrval R package](http://peter.solymos.org/code/2016/12/02/relational-operators-for-intervals-with-the-intrval-r-package.html)
- INTERACTIVE VISUALISATION, SHINY [D3PartitionR 0.3.0 is available on CRAN](https://antoineguillot.wordpress.com/2016/12/02/d3partitionr-0-3-0-is-available-on-cran/)
- [An extensive tutorial of D3partitionR 0.2](https://antoineguillot.wordpress.com/2016/11/20/an-extensive-tutorial-of-d3partitionr-0-2/)
- [High Performance CommonMark and Github Markdown Rendering in R](http://ropensci.org/blog/blog/2016/12/02/commonmark)
- [Be careful evaluating model predictions](http://www.win-vector.com/blog/2016/12/be-careful-evaluating-model-predictions/)
- [Parametric variable names and dplyr](http://www.win-vector.com/blog/2016/12/parametric-variable-names-and-dplyr/)
- [plumber — Convert R Code to a Web API](http://trestletech.com/2015/06/rapier-convert-r-code-to-a-web-api/)
- [When Documents Become Databases – Tabulizer R Wrapper for Tabula PDF Table Extractor](https://blog.ouseful.info/2016/05/02/when-documents-become-databases-tabulizer-r-wrapper-for-tabula-pdf-table-extractor/)
- [ropenscilabs/tabulizer](https://github.com/ropenscilabs/tabulizer) Bindings for Tabula PDF Table Extractor Library
tabulizer is not yet on CRAN. To install the latest development version you can:
```
if(!require("ghit")){
    install.packages("ghit")
}
# on 64-bit Windows
ghit::install_github(c("ropenscilabs/tabulizerjars", "ropenscilabs/tabulizer"), INSTALL_opts = "--no-multiarch")
# elsewhere
ghit::install_github(c("ropenscilabs/tabulizerjars", "ropenscilabs/tabulizer"))
```

## Windows
- [Chocolatey - Software Management Automation](https://chocolatey.org/). The package manager for Windows


# 02.12.2016
## R
- [ggplot2: multiple legends for the same aesthetic](http://www.quantide.com/ggplot-multiple-legends-for-the-same-aesthetic/)
- [BERT: a newcomer in the R Excel connection](http://www.thertrader.com/2016/11/30/bert-a-newcomer-in-the-r-excel-connection/)

# 01.12.2016
## R
- [Наглядная статистика. Используем R!](https://cran.r-project.org/doc/contrib/Shipunov-rbook.pdf) А. Б. Шипунов, Е. М. Балдин, П. А. Волкова, А. И. Коробейников, С. А. Назарова, С. В. Петров, В. Г. Суфиянов. 13 июля 2014 г.
- [Анализ данных с R.](http://www.inp.nsk.su/~baldin/DataAnalysis/R/) © А. Б. Шипунов, Е. М. Балдин
- [Функции в R](http://aakinshin.net/ru/blog/r/functions/) Дата: 02 июня 2013
- [Раскрашиваем R в терминале: пакет colorout](http://aakinshin.net/ru/blog/r/colorout/)
- [Perpetuum Software. Advanced reporting and data visualization components for .NET](http://www.perpetuumsoft.com/Home.aspx?lang=en)
- Все, пропал бесплатный DeployR. [Microsoft R Product Comparison](https://msdn.microsoft.com/en-us/microsoft-r/microsoft-r-getting-started#compare-prods)
- [Лицензирование SQL Server](https://www.microsoft.com/ru-ru/server-cloud/products/sql-server/purchasing.aspx)
- [SQL Server 2016 SP1 Developer edition is now free](https://www.microsoft.com/en-us/sql-server/sql-server-editions-developers)
- [SQL Server 2016 Developer, Release date 01.06.2016](https://my.visualstudio.com/Downloads?q=SQL%20Server%20Developer)
- [SQL Server 2016 RTM Enterprise on Windows Server 2012 R2 Virtual Machine](https://azure.microsoft.com/en-us/marketplace/partners/microsoft/sqlserver2016rtmenterprisewindowsserver2012r2/?wt.mc_id=sqL16_vm)

- [](http://www.r-graph-gallery.com/)
- [A List of ggplot2 extensions](https://www.ggplot2-exts.org/). This site tracks and lists ggplot2 extensions developed by R users in the community. The aim is to make it easy for R users to find developed extensions.
- [Recreating the vaccination heatmaps in R](https://benjaminlmoore.wordpress.com/2015/04/09/recreating-the-vaccination-heatmaps-in-r/)
- [Making Faceted Heatmaps with ggplot2](https://rud.is/b/2016/02/14/making-faceted-heatmaps-with-ggplot2/)

## DS
- [Статистика ожиданий SQL Server'а или пожалуйста, скажите мне, где болит](https://habrahabr.ru/post/216309/#comment_8863343)

# 30.11.2016
## R
- [elasticsearchr: a Lightweight Elasticsearch Client for R](https://alexioannides.com/2016/11/28/elasticsearchr-a-lightweight-elasticsearch-client-for-r/)
- [Introduction to Sub-Processes in R](https://cran.r-project.org/web/packages/subprocess/vignettes/intro.html)
- [dynamically-generate-rmarkdown-chunks-to-display-datatable](https://gist.github.com/ReportMort/e54ec050d97d79996189)

# 29.11.2016
## Math
- COOL! [Visualizing fits, inference, implications of (G)LMMs](http://www.ashander.info/posts/2015/04/D-RUG-mixed-effects-viz/)
- COOL! [An overview of gradient descent optimization algorithms](http://sebastianruder.com/optimizing-gradient-descent/index.html)

## R Markdown
- [Rmarkdown and DT: result do not render](http://stackoverflow.com/questions/33343241/rmarkdown-and-dt-result-do-not-render)
- [Is it possible to have sortable(Interactive) table in rMarkdown?](http://stackoverflow.com/questions/27120002/is-it-possible-to-have-sortableinteractive-table-in-rmarkdown)
- [Howto include js dependencies of DT datatable in Rmarkdown using knitr and pandoc](http://stackoverflow.com/questions/28303827/howto-include-js-dependencies-of-dt-datatable-in-rmarkdown-using-knitr-and-pando)
- [Programmatically creating Markdown tables in R with KnitR](http://stackoverflow.com/questions/15488350/programmatically-creating-markdown-tables-in-r-with-knitr)
- [An Introduction to The printr Package](http://yihui.name/printr/)

# 28.11.2016
## IP adressing
- [Online IP calcuator](http://ip-calculator.ru)
- [ip validator](http://formvalidation.io/validators/ip/). Validate an IP address. Support both IPv4 and IPv6

## R
- [Converting decimal to binary in R?](http://stackoverflow.com/questions/6614283/converting-decimal-to-binary-in-r)
- [Converting Decimal to Binary in R](https://196sigma.wordpress.com/2012/02/09/converting-decimal-to-binary-in-r/)
- [Building a column selecter](https://edwinth.github.io/blog/column-selecter/)
- [Daily metric tracking with ggplot2](http://johnmackintosh.com/2016-11-27-calendar-heatmaps/)
- [F is for Forecast. First steps with time series and prediction in R](http://johnmackintosh.com/2016-11-14-f-for-forecast/)
- [ggExtra is Extra useful](http://johnmackintosh.com/2016-04-04-ggextra-is-extra-handy/)
- [ggExtra: R package for adding marginal histograms to ggplot2](http://deanattali.com/2015/03/29/ggExtra-r-package/)
- [InveRness RUG - Intro to ggplot2](https://cdn.rawgit.com/johnmackintosh/ggplotdemo/master/pres.html#1). Отличные HTML слайды
- [RevoTreeView sample](http://rawgit.com/longhowlam/titanicTree/master/tree.html)
- [Slaying CIDR Orcs with Triebeard (a.k.a. fast trie-based ‘IPv4-in-CIDR’ lookups in R)](https://rud.is/b/2016/07/12/slaying-cidr-orcs-with-triebeard-a-k-a-fast-trie-based-ipv4-in-cidr-lookups-in-r/)
- [elasticsearchr: a Lightweight Elasticsearch Client for R](https://alexioannides.com/2016/11/28/elasticsearchr-a-lightweight-elasticsearch-client-for-r/)

## Документирование
- [ОФОРМЛЕНИЕ ДИССЕРТАЦИИ И АВТОРЕФЕРАТА](http://dis.finansy.ru/ofr/oformlen06.htm). Основные нормативные параметры форматирования. Из книги проф. Селеткова С. Г. "Соискателю ученой степени"
Количество знаков:
в строке - 60-64;
на странице (полностью заполненной) - 1800-1960.

# 25.11.2016
## DS
- [import of a opj file (Origin)](http://mathematica.stackexchange.com/questions/92745/import-of-a-opj-file-origin)
- [The Origin® Link for Mathematica®](http://www.originlab.com/doc/Origin-Help/ExternalAPP-Mathematica-Link) tool provides access to Mathematica from within Origin. The tool allows the Origin user to exchange worksheet and matrix data between Origin and Mathematica, to evaluate Mathematica expressions, and to create Origin graphs using Mathematica functions.
To utilize the tool from Origin, you'd better have Mathematica version 8 or higher (minimum support version is 4.2) installed on your computer either as a local or network copy.
- [23.5.1 Data Analysis in Origin with R Console](http://www.originlab.com/doc/Origin-Help/Analysis-Origin-Rconsole)
- [EventStudio System Designer 6](http://eventhelix.com/). Model object and message interactions in text. Visualize with sequence diagrams and context diagrams.
- [What are eTOM and TAM? Should you be using them?](http://www.ossline.com/2014/05/what-are-etom-and-tam-should-you-be-using-them.html)


# 24.11.2016
## R
- [Reading data from google sheets into R](http://www.opiniomics.org/reading-data-from-google-sheets-into-r/)
- COOL! [Announcing ggforce: Accelerating ggplot2](http://www.data-imaginist.com/2016/Announcing-ggforce/). Репозиторий [здесь](https://github.com/thomasp85/ggforce)
- COOL! [ggalt.  Extra Coordinate Systems, Geoms, Statistical Transformations & Scales for 'ggplot2'](https://github.com/hrbrmstr/ggalt). Also available on CRAN.
- [October Package Picks](https://www.rstudio.com/rviews/2016/11/23/october-package-picks/) by Joseph Rickert

# 23.11.2016
## Open-Source
- [It's an open-source world: ​78 percent of companies run open-source software](http://www.zdnet.com/article/its-an-open-source-world-78-percent-of-companies-run-open-source-software/)
Black Duck Software and North Bridge's survey found open-source software in businesses everywhere, but few are managing it worth a darn.
- [2016 Future of Open Source Survey Results](http://www.slideshare.net/blackducksoftware/2016-future-of-open-source-survey-results)

# 22.11.2016
## DS
- [Web Scraper](http://webscraper.io/). Web Scraper is a company specializing in data extraction from web pages. We offer 2 great options for our users. Our free Google Chrome Extension, and our Enterprise Data Extraction Service.]
- [Tune Machine Learning Algorithms in R (random forest case study)](http://machinelearningmastery.com/tune-machine-learning-algorithms-in-r/) TuneRF.

## e-books
- [Essays on the formal aspects of electromagnetic theory](http://gen.lib.rus.ec/book/index.php?md5=1549856b87339e19788ed724f5e32ff9) by Akhlesh Lakhtakia
	- [at Libgen.io](http://libgen.io/ads.php?md5=1549856B87339E19788ED724F5E32FF9)

# 21.11.2016
## R
- [Tracking progress in R](https://kevinkuang.net/tracking-progress-in-r-ad97998c359f#.2y2rp9kv0). An better (and still easy) solution is to adopt a package named pbapply. According to its dev page, the package has been very popular — 90k downloads.
	- [Tracking the progress of mc*apply with progress bar](https://github.com/kvnkuang/pbmcapply)
- [Bayesian Blood](https://fronkonstin.com/2016/11/17/bayesian-blood/)
- [Source code files for the book Reproducible Research with R/RStudio http://christophergandrud.github.io/RepResR-RStudio/](https://github.com/christophergandrud/Rep-Res-Book)
- [CommandCenter2000!](https://github.com/mexindian/CommandCenter). This repo helps track R jobs
- [How to change language settings in R](http://stackoverflow.com/questions/13575180/how-to-change-language-settings-in-r). You can set this using the Sys.setenv() function. My R session defaults to English, so I'll set it to French and then back again:
```
> Sys.setenv(LANG = "fr")
> 2 + x
Erreur : objet 'x' introuvable
> Sys.setenv(LANG = "en")
> 2 + x
Error: object 'x' not found
```
- [RStudio: Using Different Versions of R](https://support.rstudio.com/hc/en-us/articles/200486138-Using-Different-Versions-of-R)

## R & Access
Прикольно, но удалось решить эту задачку без танцев с бубном, только посредством установки доп. драйверов. Непонятно почему.
1. Установил Microsoft Access Database Engine 2010 Redistributable. [x64!](https://www.microsoft.com/en-us/download/confirmation.aspx?id=13255). При этом у меня стоит Office365 x32.
2.
```
library("RODBC") #load package

# эксперимент №1: https://gist.github.com/dainiuxt/23ce714e0deedc8da9a0

Sys.setenv(LANG = "en")
db <- file.path("./data/Access2007PureSQL.accdb") #connect database.
# normalizePath(db, winslash="/")
# db <- file.path("Access2007PureSQL.accdb") #connect database.

#Note the UNIX style slash (/). "\" is "escape character" so all "\"you should replace either with "/" or "\\"
# channel <- odbcConnectAccess2007(db) #internal RODBC function
# outputFile = paste(normalizePath(dirname(inputFile)),"\\", "my_file.ext", sep = "")
# Error in odbcConnectAccess(db): odbcConnectAccess is only usable with 32-bit Windows
channel <- odbcConnectAccess2007(db) #internal RODBC function

table_list <- sqlTables(channel) # запросим список таблиц
dataSetName <- sqlFetch(channel, "Products") #read particular table from Access database file.
close(channel) #do not forget this, otherwise you lock access database from editing.
```
- [R RODBC Show all tables](http://stackoverflow.com/questions/31521908/r-rodbc-show-all-tables)

Общая проблема: доступ к access базе можно обеспечить только через 32-х битный драйвер, а его может использовать только 32-х битный R
- [How to connect R with Access database in 64-bit Window?](http://stackoverflow.com/questions/13070706/how-to-connect-r-with-access-database-in-64-bit-window). Запуск отдельного процесса и общение через сокеты.
- [How to Connect to an MS Access database in R](http://rprogramming.net/connect-to-ms-access-in-r/)
- [Query MS Access DB from R with 64-bit Windows](http://stackoverflow.com/questions/36160751/query-ms-access-db-from-r-with-64-bit-windows)
- [Connect MS Access database to R (RStudio) in Windows](https://gist.github.com/dainiuxt/23ce714e0deedc8da9a0)
- [Microsoft Access Database Engine 2010 Redistributable](https://www.microsoft.com/en-us/download/details.aspx?id=13255). I think the problem is as error message suggests - you don't have x64 Microsoft Access driver installed. Check it in **Control panel - ODBC Data Sources (x64)** on the Drivers tab. If it's not there, try to install Microsoft Access Database Engine 2010 Redistributable.
- [Using 64-bit Applications with Microsoft Access Database Files](https://www.altova.com/Access-Database-OLEDB-32bit-64bit.html). **There is currently an unfortunate limitation of the 64-bit ACE driver – it cannot co-exist with 32-bit versions of Microsoft Office.**
- Steps to use, assuming 32 bit Access on windows 8
	- Select 32 bit R (is just a setting in R studio)
	- search on windows for Set up ODBC data sources (32 bit)
	- Go to System DSN>Add
	- Choose Driver do Microsoft Access (*.mdb) > Finish
	- Data source name: ProjecnameAcc
	- Description: ProjectnameAcc
	- Make sure to actually select the database > OK
Now I could run the code that I liked
```
channel <- odbcConnect("ProjectnameAcc")
Table1Dat <- sqlFetch(channel, "Table1")
```


## R. Solving the Task
- [Filtering row which contains a certain string using dplyr](http://stackoverflow.com/questions/22850026/filtering-row-which-contains-a-certain-string-using-dplyr)
`str_detect`
- [Using dplyr mutate to find position of character in string](http://stackoverflow.com/questions/37170093/using-dplyr-mutate-to-find-position-of-character-in-string)
- [replace NA in a dplyr chain](http://stackoverflow.com/questions/21714867/replace-na-in-a-dplyr-chain)
- [Replace missing values](https://rdrr.io/cran/tidyr/man/replace_na.html). replace_na(data, replace = list(), ...)
- [R ggplot2: stat_count() must not be used with a y aesthetic error in Bar graph](http://stackoverflow.com/questions/39679057/r-ggplot2-stat-count-must-not-be-used-with-a-y-aesthetic-error-in-bar-graph)
- "Как решить задачу выравнивания осей X у разных графиков", см ссылки ниже от 26.05.16 (R), grid.draw
- [Listing all files matching a full-path pattern in R](http://stackoverflow.com/questions/10353540/listing-all-files-matching-a-full-path-pattern-in-r)
- [Regular expression to match line that doesn't contain a word?](http://stackoverflow.com/questions/406230/regular-expression-to-match-line-that-doesnt-contain-a-word)
- [Cookbook for R >> Basics Working with NULL, NA, and NaN](http://www.cookbook-r.com/Basics/Working_with_NULL_NA_and_NaN/)
- [na.omit() for lists in R]()https://gist.github.com/rhochreiter/7029236): `na.omit.list <- function(y) { return(y[!sapply(y, function(x) all(is.na(x)))]) }`
- [Simplest way to get rbind to ignore column names](http://stackoverflow.com/questions/19297475/simplest-way-to-get-rbind-to-ignore-column-names)
- [Reordering columns in a large dataframe](http://stackoverflow.com/questions/18339370/reordering-columns-in-a-large-dataframe). To move specific columns to the beginning or end of a data.frame, use select from the dplyr package and its everything() function. In this example we are sending to the end:
```
library(dplyr)
df %>%
  select(-b, -c, everything())
```
- [normalizePath {base}: Express File Paths in Canonical Form](https://stat.ethz.ch/R-manual/R-devel/library/base/html/normalizePath.html)
- [How do I get the absolute path of an input file in R](http://stackoverflow.com/questions/13311180/how-do-i-get-the-absolute-path-of-an-input-file-in-r)

# 18.11.2016
## R & Excel
Не все файлы excel, особенно сформированные во внешних BI, могут быть прочитаны сторонними парсерами.
Например, при открытии xls файла, присланного Казариным, получаем такую ошибку: `zip file './data-verification/022 - Отчет о см. ст. по ОКС (Отчет №3).xls' cannot be opened`

- [Problem reading some xlsx - Error: Couldn't find 'xl/worksheets/sheet1.xml'](https://github.com/hadley/readxl/issues/80)
- [Unwanted *printed* output from read_excel](https://github.com/hadley/readxl/issues/82) `DEFINEDNAME: 21 00 00 01 0`. Suggested [Workaround](https://github.com/hadley/readxl/issues/82#issuecomment-166767220)
- [Bad Zip File Error from reading XLS files](https://community.qlik.com/thread/75785)


# 17.11.2016
## R
- [dplyr & r: Anonymous functions myst be parenthesized](http://stackoverflow.com/questions/28074797/dplyr-r-anonymous-functions-myst-be-parenthesized)
- [Convenient Data Exchange between R and Microsoft Excel](https://github.com/gdemin/excel.link). The excel.link package mainly consists of two rather independent parts: one is for transferring data/graphics to running instance of Excel, another part - work with data table in Excel in similar way as with usual data.frame.


# 16.11.2016
## DS
- [Introducing the Team Data Science Process from Microsoft](https://blogs.technet.microsoft.com/machinelearning/2016/10/11/introducing-the-team-data-science-process-from-microsoft/)
- [Probability Distributions Library for JavaScript](http://statisticsblog.com/probability-distributions/)
- COOL! [Why you need version control](http://ellisp.github.io/blog/2016/09/16/version-control)

## R Markdown & Notebooks
- [My table looks better than yours](https://www.stat.ubc.ca/~jenny/STAT545A/topic10_tablesCSS.html)
- [pander: An R Pandoc Writer](http://rapporter.github.io/pander/)
- [R Code Chunks](http://rmarkdown.rstudio.com/authoring_rcodechunks.html)
- COOL! [Render reports directly from R scripts](http://brooksandrew.github.io/simpleblog/articles/render-reports-directly-from-R-scripts/)
	- [A collection of css themes for Markdown http://jasonm23.github.io/markdown-css-themes/](https://github.com/jasonm23/markdown-css-themes)
	- [Markdown css themes Preview](http://jasonm23.github.io/markdown-css-themes/)

## R
- [Introducing R-hub, the R package builder service](http://blog.revolutionanalytics.com/2016/10/r-hub-public-beta.html)
	- [The r-hub builder](https://builder.r-hub.io/)
- rJava: версия R и версия Java должны совпадать (либо оба x86, либо оба x64)
	- [package or namespace load failed for ‘rJava’ #49]
	- [R - Error: .onLoad failed in loadNamespace() for 'rJava'](http://stackoverflow.com/questions/37735108/r-error-onload-failed-in-loadnamespace-for-rjava)
This error is often resolved by installing a Java version (i.e. 64-bit Java or 32-bit Java) that fits to the type of R version that you are using (i.e. 64-bit R or 32-bit R). This problem can easily effect Windows 7 users, since they might have installed a version of Java that is different than the version of R they are using.
Note that it is necessary to ‘manually download and install’ the 64 bit version of JAVA. By default, the download page gives a 32 bit version .
You can pick the exact version of Java you wish to install from this link. If you might (for some reason) work on both versions of R, you can install both version of Java (Installing the “Java Runtime Environment” is probably good enough for your needs). (Source: Uwe Ligges)
Other possible solutions is trying to re-install rJava.
If that doesn’t work, you could also manually set the directory of your Java location by setting it before loading the library:
```
Sys.setenv(JAVA_HOME='C:\\Program Files\\Java\\jre7') # for 64-bit version
Sys.setenv(JAVA_HOME='C:\\Program Files (x86)\\Java\\jre7') # for 32-bit version
library(rJava)
```

## R ggplot
- [ggedit – interactive ggplot aesthetic and theme editor](https://www.r-statistics.com/2016/11/ggedit-interactive-ggplot-aesthetic-and-theme-editor/)
- Диагностика графических объектов: `library(gtable) gtable_show_layout(ggplotGrob(gp2))`
- [Align multiple ggplot graphs with and without legends](http://stackoverflow.com/questions/26159495/align-multiple-ggplot-graphs-with-and-without-legends)
- [baptiste/gridextra: arranging ggplot](https://github.com/baptiste/gridextra/wiki/arranging-ggplot)
- [R grid.arrange: nrow * ncol >= n is not TRUE](http://stackoverflow.com/questions/33694159/r-grid-arrange-nrow-ncol-n-is-not-true)
- [Combine plots that have a legend with one that doesn't](http://stackoverflow.com//questions/38017042/combine-plots-that-have-a-legend-with-one-that-doesnt). Разбираются с ошибкой `Error: ncol(x) == ncol(y) is not TRUE`. The reason you are getting the error is because one of your 3 gtable objects has 5 columns while the other has 6 (the p.3 object has 5 because you exclude the legend). You can check out the different layouts of the gtable objects by doing:
```
library(gtable)
gtable_show_layout(ggplotGrob(p.1))
gtable_show_layout(ggplotGrob(p.2))
gtable_show_layout(ggplotGrob(p.3))
```
- [Displaying tables as grid graphics](ftp://cran.r-project.org/pub/R/web/packages/gridExtra/vignettes/tableGrob.html)
- [Arranging multiple grobs on a page](https://cran.r-project.org/web/packages/gridExtra/vignettes/arrangeGrob.html)
- [ggplot2 - Easy way to mix multiple graphs on the same page](http://www.sthda.com/english/wiki/ggplot2-easy-way-to-mix-multiple-graphs-on-the-same-page-r-software-and-data-visualization)
	- [Mix table, text and ggplot2 graphs](http://www.sthda.com/english/wiki/ggplot2-easy-way-to-mix-multiple-graphs-on-the-same-page-r-software-and-data-visualization#mix-table-text-and-ggplot2-graphs)
	- [Add a common legend for multiple ggplot2 graphs](http://www.sthda.com/english/wiki/ggplot2-easy-way-to-mix-multiple-graphs-on-the-same-page-r-software-and-data-visualization#add-a-common-legend-for-multiple-ggplot2-graphs)
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

## Revolution Analytics
Recommended Sites
- [FlowingData](http://flowingdata.com/). Modern data visualization
- [One R Tip A Day](http://onertipaday.blogspot.com/). Code examples for graphics and analysis
- [Probability and statistics blog](http://www.statisticsblog.com/). Monte Carlo simulations in R
- [R Bloggers](http://www.r-bloggers.com/). Daily news and tutorials about R, contributed by R bloggers worldwide.
- [R Project group on analyticbridge.com](http://www.analyticbridge.com/group/rprojectandotherfreesoftwaretools). Community and discussion forum
- [Statistical Modeling, Causal Inference, and Social Science](http://www.stat.columbia.edu/~cook/movabletype/mlm/). Andrew Gelman's statistics blog

# 15.11.2016
## DS
- [Do data scientists use Excel?](http://datascience.stackexchange.com/questions/5443/do-data-scientists-use-excel)
	- [European Spreadsheet Risks Interest Group - Horror Stories](http://www.eusprig.org/horror-stories.htm)
	- [You shouldn’t use a spreadsheet for important work (I mean it)](http://www.eusprig.org/horror-stories.htm)
	- [Microsoft's Excel Might Be The Most Dangerous Software On The Planet](http://www.forbes.com/sites/timworstall/2013/02/13/microsofts-excel-might-be-the-most-dangerous-software-on-the-planet/)
	- [Destroy Your Data Using Excel With This One Weird Trick!](http://randyzwitch.com/excel-destroys-data/)
	- [Excel spreadsheets are hard to get right](http://www.win-vector.com/blog/2014/11/excel-spreadsheets-are-hard-to-get-right/)


# 14.11.2016
## Docker
- [Разработка → 350+ полезных ресурсов, книг и инструментов для работы с Docker](https://habrahabr.ru/company/1cloud/blog/275015/). перевод 

## Python 2 or Python 3 for DataScience
 - [Киллер-фичи Python 3](http://alxpy.com/blog/killer-features-of-python-3/), JANUARY 22, 2015
 - [10 awesome features of Python that you can't use because you refuse to upgrade to Python 3](http://www.asmeurer.com/python3-presentation/python3-presentation.pdf)
 - COOL! [Will Scientists Ever Move to Python 3?](https://jakevdp.github.io/blog/2013/01/03/will-scientists-ever-move-to-python-3/). March 2016: Please note the date on this post. Given the developments in the last three years, I would no longer agree with much of what I've written here. In particular, I substantially underestimated the ability of tools like six and python-future to enable single-codebase Python 2/3 support, and virtually all scientific packages now use such tools to support both. Short version: just use Python 3. There's almost no reason not to any more.

## R и целые числа (Int 32)
- COOL! [R in a 64 bit world](http://www.win-vector.com/blog/2015/06/r-in-a-64-bit-world/)
- COOL! [My criticism of R numeric summary](http://www.win-vector.com/blog/2016/08/my-criticism-of-r-numeric-summary/#more-4319)
- COOL! [Appendix D. What Every Computer Scientist Should Know About Floating-Point Arithmetic](http://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html)
- [Calculations precision level in R](http://stackoverflow.com/questions/18742985/calculations-precision-level-in-r)
- [Correcting “summary” in R with appropriate # of digits of precision](http://stackoverflow.com/questions/7840073/correcting-summary-in-r-with-appropriate-of-digits-of-precision)

- [Book Review: Statistics Done Wrong](http://blog.revolutionanalytics.com/2015/07/book-review-statistics-done-wrong.html) by Joseph Rickert

## R
- [Ordering categories within ggplot2 facets](https://drsimonj.svbtle.com/ordering-categories-within-ggplot2-facets)
- [RStudio IDE Easy Tricks You Might’ve Missed](https://www.rstudio.com/rviews/2016/11/11/easy-tricks-you-mightve-missed/)
- COOL! [Explicitly calling return in a function or not](http://stackoverflow.com/questions/11738823/explicitly-calling-return-in-a-function-or-not)

## R
- [Data Manipulation with sparklyr on Azure HDInsight](http://blog.revolutionanalytics.com/2016/11/data-manipulation-with-sparklyr-on-azure-hdinsight.html)
# 10.11.2016
## R
- [Numerical Mathematics Task View devoted to "Multi-Precision Arithmetic and Symbolic Mathematics"](https://cran.r-project.org/web/views/NumericalMathematics.html)
	- [How to work with large numbers in R?](http://stackoverflow.com/questions/22466328/how-to-work-with-large-numbers-in-r)
- [R - How to test for character(0) in IF statement](http://stackoverflow.com/questions/25640161/r-how-to-test-for-character0-in-if-statement)
- [What is the difference between NULL and character(0) in R?](http://stackoverflow.com/questions/7195248/what-is-the-difference-between-null-and-character0-in-r)

# 09.11.2016
## R
- [R Views: an R Community Blog](https://www.rstudio.com/rviews/)

## Availability
- [Reliability and availability basics](http://www.eventhelix.com/RealtimeMantra/FaultHandling/reliability_availability_basics.htm)
- [System Reliability and Availability](http://www.eventhelix.com/RealtimeMantra/FaultHandling/system_reliability_availability.htm)
- [Failure Rates, MTBFs, and All That](http://www.mathpages.com/home/kmath498/kmath498.htm)
- [Infinite Parallel Redundancy](http://www.mathpages.com/home/kmath326/kmath326.HTM)
- [Mean Time Between Failures & Mean Time To Repair](http://world-class-manufacturing.com/KPI/mtbf.html)
- [MTBF online calculator](http://www.pixelbeat.org/docs/reliability_calculator/)

# 08.11.2016
## R
- [The Lab-R-torian blog](http://labrtorian.com)
	- [Make Easy Heatmaps to Visualize your Turnaround Times](http://labrtorian.com/2016/09/08/make-easy-heatmaps-to-visualize-your-turnaround-times/)
	- [Conditional Formatting of a Table in R](http://labrtorian.com/2016/11/07/conditional-formatting-of-a-table-in-r/)
- [Useful tools for shiny developers in the new version of shinyjs](http://deanattali.com/blog/shinyjs-v08/)
- [avoid string printed to console getting truncated (in RStudio)](http://stackoverflow.com/questions/36800475/avoid-string-printed-to-console-getting-truncated-in-rstudio)
- [list output truncated - How to expand listed variables with str() in R](http://stackoverflow.com/questions/28895044/list-output-truncated-how-to-expand-listed-variables-with-str-in-r):
You can use the argument list.len: `str(df, list.len=ncol(df))`

## Encodings & web scrapping
- [Selector Gadget](http://selectorgadget.com/)
- [Best practices for writing an API package](https://cran.r-project.org/web/packages/httr/vignettes/api-packages.html)
- [httr quickstart guide](https://cran.r-project.org/web/packages/httr/vignettes/quickstart.html)
- [httr: a friendly http package for R](https://github.com/hadley/httr)
- [Force character vector encoding from “unknown” to “UTF-8” in R](http://stackoverflow.com/questions/23699271/force-character-vector-encoding-from-unknown-to-utf-8-in-r). 
To check whether each string consists of valid UTF-8 byte sequences, call: `all(stri_enc_isutf8(poli.dt$word))`
- [Encoding issue while scraping website in R](http://stackoverflow.com/questions/33012907/encoding-issue-while-scraping-website-in-r)
- [R rvest encoding errors with UTF-8](http://stackoverflow.com/questions/37867465/r-rvest-encoding-errors-with-utf-8)
- [R: rvest - is not proper UTF-8, indicate encoding?](http://stackoverflow.com/questions/32833894/r-rvest-is-not-proper-utf-8-indicate-encoding)
- [encoding issues with rvest, “Â ” appearing instead of a space in character strings](http://stackoverflow.com/questions/37903528/encoding-issues-with-rvest-%C3%82-appearing-instead-of-a-space-in-character-strin)
- [Using rvest to Scrape an HTML Table](http://blog.corynissen.com/2015/01/using-rvest-to-scrape-html-table.html)
- [How to Scrape Japanese Text Using the rvest Package](http://masterr.org/r/how-to-scrape-Japanese-text-using-rvest/)
- [Web scraping with `rvest` in R](http://francojc.github.io/web-scraping-with-rvest/)
- [HTML Widgets: Advanced Topics](https://cran.r-project.org/web/packages/htmlwidgets/vignettes/develop_advanced.html)
- [rvest tutorial: scraping the web using R](rvest tutorial: scraping the web using R)
- Javascript generated pages
	- [Scraping Javascript generated data](http://stackoverflow.com/questions/15330393/scraping-javascript-generated-data)
	- [Short R tutorial: Scraping Javascript Generated Data with R](https://www.datacamp.com/community/tutorials/scraping-javascript-generated-data-with-r)
	- [download javascript-loading data from the web using R? tricky web scraping](http://stackoverflow.com/questions/27993898/download-javascript-loading-data-from-the-web-using-r-tricky-web-scraping)
	- [CasperJS](http://casperjs.org/). Navigation scripting & testing for PhantomJS and SlimerJS
	- [mozilla/geckodriver](https://github.com/mozilla/geckodriver). WebDriver <-> Marionette proxy 
	- [RSelenium: R Bindings for Selenium WebDriver](https://cran.r-project.org/web/packages/RSelenium/index.html)
	- [How to drive a Web browser with R (and RSelenium)](http://www.computerworld.com/article/2971265/application-development/how-to-drive-a-web-browser-with-r-and-rselenium.html)
	- [Trying to run RSelenium (Windows 7/ Mac OS X)](http://stackoverflow.com/questions/32129427/trying-to-run-rselenium-windows-7-mac-os-x). [1] "Connecting to remote server" Undefined error in RCurl call.
	- [webscraping with Selenium - part 1](http://thiagomarzagao.com/2013/11/12/webscraping-with-selenium-part-1/)
	- [Scraping gnarly sites with phantomjs & rvest](https://gist.github.com/hrbrmstr/dc62bb2b35617e9badc5)
	- [Web-Scraping JavaScript rendered Sites](https://flovv.github.io/Scrape-JS-Sites/)
	- [Scrape webpage with phantomjs and rvest](http://stackoverflow.com/questions/35446515/scrape-webpage-with-phantomjs-and-rvest)
	- [How to scrape all the hotel reviews from HolidayIQ using Rvest and phantomJS](http://stackoverflow.com/questions/36152621/how-to-scrape-all-the-hotel-reviews-from-holidayiq-using-rvest-and-phantomjs)

## RSelenium
1. Качаем Selenium
1. Качаем RSelenium: `devtools::install_github("ropensci/RSelenium")`
1. Качаем WebDriver, кладем в PATH (лучше рядом). [ChromeDriver - WebDriver for Chrome](https://sites.google.com/a/chromium.org/chromedriver/downloads)
1. Запускаем `remDr <- remoteDriver(browserName = "chrome")`, описание здесь:[RSelenium: Driving OS/Browsers local and remote](https://cran.r-project.org/web/packages/RSelenium/vignettes/RSelenium-saucelabs.html)

## Google
- [Как обезопасить аккаунт, который был взломан в прошлом?](https://productforums.google.com/forum/?utm_medium=email&utm_source=footer#!topic/gmail-ru/XK2-BLWfWKs)
- [где в gmail находится архив? я отправил письма в архив и теперь не могу их найти](https://productforums.google.com/forum/#!topic/gmail-ru/ByqLwh1laVQ)
'-is:chat -in:draft -in:trash -in:inbox -in:sent -in:spam -is:starred'

- [iOS, url schemes](http://ios-swift-dev.blogspot.ru/2016/05/url-schemes.html): 
Name - Gmail
com.google.sso.390630100053://
com.google.sso.532713016892-ev29m8tv9gejefcvvv1o3coj5bhkc1ar://
googlegmail://
googlegmail-x-callback:// 

# 07.11.2016
## R
- [Rocker - explanation and motivation for Docker containers usage in applications development](http://r-addict.com/2016/10/03/Rocker-Presentation-eRka10.html)
	- [Rocker: explanation and motivation for Docker containers usage in applications development](http://r-addict.com/eRka10/#/). Marcin Kosiński. September 30, 2016
	- Font Awesome. [Cheatsheet](http://fontawesome.io/cheatsheet/). The complete Font Awesome 4.7.0 icon reference
- [R Markdown Format for reveal.js Presentations](https://github.com/rstudio/revealjs)
- RStudio. [Presentations with reveal.js](http://rmarkdown.rstudio.com/revealjs_presentation_format.html)
- [A Simple Guide to S3 Methods](http://www.njtierney.com/r/missing%20data/rbloggers/2016/11/06/simple-s3-methods/). [Драфт](https://arxiv.org/abs/1608.07161) публикации
- [Evaluating the Design of the R Language](http://r.cs.purdue.edu/pub/ecoop12.pdf)
- [Timeseries forecasting using extreme gradient boosting](http://ellisp.github.io/blog/2016/11/06/forecastxgb).
	- [The forecastxgb](https://github.com/ellisp/forecastxgb-r-package/) package provides time series modelling and forecasting functions that combine the machine learning approach of Chen, He and Benesty's xgboost with the convenient handling of time series and familiar API of Rob Hyndman's forecast. It applies to time series the Extreme Gradient Boosting proposed in Greedy Function Approximation: A Gradient Boosting Machine, by Jermoe Friedman in 2001. xgboost has become an important machine learning algorithm; nicely explained in this accessible documentation.
	- [Introduction to Boosted Trees](http://xgboost.readthedocs.io/en/latest/model.html)
- [The Bigmemory Project](http://www.bigmemory.org/). Working with Massive Matrix-like Objects in R. syncronicity -- UNIX only package!!!!!!
```
devtools::install_github("kaneplusplus/bigmemory")
devtools::install_github("kaneplusplus/bigtabulate")
devtools::install_github("kaneplusplus/biganalytics")
devtools::install_github("kaneplusplus/bigalgebra")
devtools::install_github("kaneplusplus/synchronicity")
```

## Parallel & optimization
- [FasteR! HigheR! StrongeR! - A Guide to Speeding Up R Code for Busy People](http://www.noamross.net/blog/2013/4/25/faster-talk.html)
- COOL [R: parallel computing in 5 minutes (with foreach and doParallel)](http://blog.aicry.com/r-parallel-computing-in-5-minutes/)
- COOL [How-to go parallel in R – basics + tips](http://gforge.se/2015/02/how-to-go-parallel-in-r-basics-tips/). См. п. "Debugging"
Debugging is especially hard when working in a parallelized environment. You cannot simply call browser/cat/print in order to find out what the issue is.
	- Never use set.seed(), use clusterSetRNGStream() instead, to set the cluster seed if you want reproducible results
- [When does foreach call .combine?](http://stackoverflow.com/questions/18704115/when-does-foreach-call-combine)
- [foreach as List Comprehensions](ftp://cran.r-project.org/pub/R/web/packages/foreach/vignettes/foreach.pdf). см документ "Using The foreach Package"
If you're familiar with the Python programming language, it may have occurred to you that the foreach package provides something that is not too dierent from Python's list comprehensions. In fact, the foreach package also includes a function called when which can prevent some of the evaluations from happening, very much like the \if" clause in Python's list comprehensions.
- [“un-register” a doParallel cluster](http://stackoverflow.com/questions/25097729/un-register-a-doparallel-cluster)
- [How can I print when using %dopar%](http://stackoverflow.com/questions/10903787/how-can-i-print-when-using-dopar)
- [How to log when using foreach (print or futile.logger)](http://stackoverflow.com/questions/38828344/how-to-log-when-using-foreach-print-or-futile-logger)
- [R parallel computing with snowfall - writing to files from separate workers](http://stackoverflow.com/questions/12994063/r-parallel-computing-with-snowfall-writing-to-files-from-separate-workers)
- [How to log using futile logger from within a parallel method in R?](http://stackoverflow.com/questions/20930112/how-to-log-using-futile-logger-from-within-a-parallel-method-in-r)
- [Shared memory in parallel foreach in R](http://stackoverflow.com/questions/31575585/shared-memory-in-parallel-foreach-in-r)
	- [reading global variables using foreach in R](http://stackoverflow.com/questions/18028452/reading-global-variables-using-foreach-in-r)
	- [writing to global environment when running in parallel](http://stackoverflow.com/questions/6251662/writing-to-global-environment-when-running-in-parallel)
- [future: A Future API for R](https://github.com/HenrikBengtsson/future). The purpose of the future package is to provide a very simple and uniform way of evaluating R expressions asynchronously using various resources available to the user.
In programming, a future is an abstraction for a value that may be available at some point in the future. The state of a future can either be unresolved or resolved. As soon as it is resolved, the value is available instantaneously. If the value is queried while the future is still unresolved, the current process is blocked until the future is resolved. It is possible to check whether a future is resolved or not without blocking. Exactly how and when futures are resolved depends on what strategy is used to evaluate them. For instance, a future can be resolved using a "lazy" strategy, which means it is resolved only when the value is requested. Another approach is an "eager" strategy, which means that it starts to resolve the future as soon as it is created. Yet other strategies may be to resolve futures asynchronously, for instance, by evaluating expressions concurrently on a compute cluster.
	- [Asynchronous and Distributed Programming in R with the Future Package](https://alexioannides.com/2016/11/02/asynchronous-and-distributed-programming-in-r-with-the-future-package/)
	- [Remote Processing Using Futures](http://www.jottr.org/2016/10/remote-processing-using-futures.html)
	- [HenrikBengtsson/future](https://github.com/HenrikBengtsson/future)
- [R foreach error: Unserialize(node$con) when combining results](http://stackoverflow.com/questions/33444931/r-foreach-error-unserializenodecon-when-combining-results)
- [Problems using foreach parallelization](http://stackoverflow.com/questions/5007458/problems-using-foreach-parallelization)
- [Parallelization in R: %dopar% vs %do%. Why using a single core yields to better performance?](http://stackoverflow.com/questions/15194465/parallelization-in-r-dopar-vs-do-why-using-a-single-core-yields-to-better)
- [Why is the parallel package slower than just using apply?](http://stackoverflow.com/questions/14614306/why-is-the-parallel-package-slower-than-just-using-apply)
- [Why is foreach() %do% sometimes slower than for?](http://stackoverflow.com/questions/10411871/why-is-foreach-do-sometimes-slower-than-for)
- [Monitoring progress of a foreach parallel job](http://blog.revolutionanalytics.com/2015/02/monitoring-progress-of-a-foreach-parallel-job.html)
- COOL! [Netcat for Windows](https://joncraton.org/blog/46/netcat-for-windows/). Netcat is a simple networking utility which reads and writes data across network connections using the TCP/IP protocol. It's a wonderful tool for debugging all kinds of network problems.
- [Increasing the speed of {raster} processing with R](http://www.gis-blog.com/)
	- [Part 1/3](http://www.gis-blog.com/increasing-the-speed-of-raster-processing-with-r-part-13/)
	- [Part 2/3: Parallelisation](http://www.gis-blog.com/increasing-the-speed-of-raster-processing-with-r-part-23-parallelisation/)
	- [Part 3/3: Cluster](http://www.gis-blog.com/increasing-the-speed-of-raster-processing-with-r-part-33-cluster/)


- Полезные команды
	- registerDoSEQ() -- выход из параллельного блока foreach (# specify that %dopar% should run sequentially)
	- tracemem() -- This function marks an object so that a message is printed whenever the internal code copies the object. It is a major cause of hard-to-predict memory use in R.

## Other
- [Pattern recognition for satellite imagery – Terrapattern](http://www.gis-blog.com/pattern-recognition-for-satellity-imagery-terrapattern/)
- [Plot Google Maps images in R using geocoding {dismo}](http://www.gis-blog.com/plot-google-maps-images-in-r-using-geocoding-dismo/)
- [Visual Studio for Mac - Introducing Visual Studio for Mac](https://msdn.microsoft.com/en-us/magazine/mt790182.aspx)


# 03.11.2016
## R & Spark
- [sparkR programming guide](https://spark.apache.org/docs/latest/sparkr.html)
- [sparkR API documentation](https://spark.apache.org/docs/latest/api/R/index.html)
- Building a Data Science Platform for R&D:
	- [Part 1 – Setting-Up AWS](https://alexioannides.com/2016/08/16/building-a-data-science-platform-for-rd-part-1-setting-up-aws/)
	- [Part 2 – Deploying Spark on AWS using Flintrock](https://alexioannides.com/2016/08/18/building-a-data-science-platform-for-rd-part-2-deploying-spark-on-aws-using-flintrock/)
	- [Part 3 – R, R Studio Server, SparkR & Sparklyr](https://alexioannides.com/2016/08/22/building-a-data-science-platform-for-rd-part-3-r-r-studio-server-sparkr-sparklyr/)
	- [Part 4 – Apache Zeppelin & Scala Notebooks](https://alexioannides.com/2016/08/29/building-a-data-science-platform-for-rd-part-4-apache-zeppelin-scala-notebooks/)

## Tools
- LogViewer
	- [Log viewer on Windows {closed}](http://superuser.com/questions/153/log-viewer-on-windows)
	- [Windows log tail viewer {duplicate}](http://superuser.com/questions/190205/windows-log-tail-viewer)
	- [Log Expert](http://logexpert.codeplex.com/). Windows tail program and log file analyzer.
	- [mTAIL](http://ophilipp.free.fr/op_tail.htm) is a Windows Program that works like the Unix Command TAIL.
	- [ReflectInsight - Log Viewer for NLog, Log4net, Enterprise Library & Debug/Trace](http://insightextensions.codeplex.com/)


# 01.11.2016
## R
- [Learn to Create, Publish and Profit from R Projects](http://www.arilamstein.com/membership/). Платно, но выглядит интересно.
- mapmate
	- [mapmate 0.1.0](https://blog.snap.uaf.edu/2016/11/01/mapmate-0-1-0/). mapmate has now been updating from version 0.0.2 to 0.1.0 on Github.
	- [Usage examples and limitations](https://leonawicz.github.io/mapmate/usage_and_limitations.html) by Matthew Leonawicz
- [rbokeh Version 0.5.0 Released](http://ryanhafen.com/blog/rbokeh-0-5-0)

# 31.10.2016
## R
- [What is ShinyProxy?](http://www.shinyproxy.io/) ShinyProxy is your favourite way to deploy Shiny apps in an enterprise context. It has built-in functionality for LDAP authentication and authorization, makes securing Shiny traffic (over TLS) a breeze and has no limits on concurrent usage of a Shiny app. 
	- [ShinyProxy 0.6.0 released!](https://www.openanalytics.eu/blog/shinyproxy-060-released) ShinyProxy is a novel, open source platform to deploy Shiny apps for the enterprise or larger organizations.
- [Fastest Way to Add New Variables to A Large Data.Frame](https://statcompute.wordpress.com/2016/10/31/fastest-way-to-add-new-variables-to-a-large-data-frame/). Как раз исследуется вопрос о скорости различных подходов к вычислению.
- [R Package clickstream: Analyzing Clickstream Data with Markov Chains](https://www.jstatsoft.org/article/view/v074i04)
- [Calculating Moving Averages and Historical Flow Quantiles](https://owi.usgs.gov/blog/moving-averages/) by Laura DeCicco

# 29.10.2016
## R
- [jottR Jotter on R](http://www.jottr.org/)
	- [Remote Processing Using Futures](http://www.jottr.org/2016/10/remote-processing-using-futures.html)
- [ReporteRs](http://davidgohel.github.io/ReporteRs/) is an R package for creating Microsoft (Word docx and Powerpoint pptx) and html documents. It does not require any Microsoft component to be used. It runs on Windows, Linux, Unix and Mac OS systems. This is the ideal tool to automate reporting generation from R.
	- [A quick exploration of the ReporteRs package](https://statbandit.wordpress.com/2016/10/28/a-quick-exploration-of-reporters/)
- [Create and format Word documents using R software and Reporters package](http://www.sthda.com/english/wiki/create-and-format-word-documents-using-r-software-and-reporters-package)

# 27.10.2016
## R
- [arules: Association Rule Mining with R — A Tutorial](http://michael.hahsler.net/research/arules_RUG_2015/demo/)
- [Sharing our R Programs — With Style](http://blog.revolutionanalytics.com/2016/10/sharing-r-code-with-style.html)
- [September Package Picks by Joseph Rickert](https://www.rstudio.com/2016/10/26/september-package-picks/)
	- [plotwidgets : Spider Plots, ROC Curves, Pie Charts and More for Use in Other Plots](https://mran.revolutionanalytics.com/package/plotwidgets/)
	- [Plotluck - “I’m feeling lucky” for ggplot](https://mran.revolutionanalytics.com/web/packages/plotluck/vignettes/plotluck.html)
	- [thief : Temporal Hierarchical Forecasting](https://mran.revolutionanalytics.com/package/thief/)
- archivist package
	- [News from archivist 2.0 on eRum2016 conference](http://r-addict.com/2016/10/26/archivist-on-eRum2016.html)
	- [archivist 2.0: (News from) Managing Data Analysis Results Toolkit](http://r-addict.com/eRum2016/#/). Presentation by Marcin Kosiński, October 13, 2016
	- [archivist.github: Tools for Archiving, Managing and Sharing R Objects via GitHub](https://cran.r-project.org/web/packages/archivist.github/)
	- [archivist and GitHub integration: archivist.github](http://r-addict.com/archivist.github/)
	- [The list of blog-posts and conference talks about archivist](http://pbiecek.github.io/archivist/Posts.html)
	- COOL! [All your models belong to us: how to combine package archivist and function trace()](http://smarterpoland.pl/index.php/2016/05/all-your-models-belong-to-us-how-to-combine-package-archivist-and-function-trace/)
- [Radiant](https://github.com/radiant-rstats/radiant) is an open-source platform-independent browser-based interface for business analytics in R. The application is based on the Shiny package and can be run locally or on a server. Radiant was developed by Vincent Nijs. Please use the issue tracker on GitHub to suggest enhancements or report problems: https://github.com/radiant-rstats/radiant/issues. For other questions and comments please use radiant@rady.ucsd.edu.
- [What's the difference between seq_len() and seq_along() in the R programming language?](https://www.quora.com/Whats-the-difference-between-seq_len-and-seq_along-in-the-R-programming-language)
- [R: for loop iteration with seq_along vectors of a list](http://stackoverflow.com/questions/27848385/r-for-loop-iteration-with-seq-along-vectors-of-a-list)


## Parallel R
- [ParallelR blog](http://www.parallelr.com/blog/)
	- [R and openMP: boosting compiled code on multi-core cpu-s](http://www.parallelr.com/r-and-openmp-boosting-compiled-code-on-multi-core-cpu-s/)
- [Parallelism, R, and OpenMP](https://wrathematics.github.io/RparallelGuide/)
- [CRAN Task View: High-Performance and Parallel Computing with R](https://cran.r-project.org/web/views/HighPerformanceComputing.html)
- [A gentle introduction to parallel computing in R](http://www.win-vector.com/blog/2016/01/parallel-computing-in-r/)
- [Running R jobs quickly on many machines](http://www.win-vector.com/blog/2016/01/running-r-jobs-quickly-on-many-machines/)
- [can't open sockets for parallel cluster](http://stackoverflow.com/questions/19248598/cant-open-sockets-for-parallel-cluster)

# 25.10.2016
## Collaboration
- [Список команд чата Skype](https://habrahabr.ru/post/97561/)
- [Минимальный почтовый сервер на основе Postfix и Dovecot. Часть 1: Dovecot](https://habrahabr.ru/post/258279/)
- [Минимальный почтовый сервер на основе Postfix и Dovecot. Часть 2: Postfix](https://habrahabr.ru/post/258407/)
- [Rsyslog is a rocket-fast system for log processing]http://www.rsyslog.com/doc/v8-stable/). It offers high-performance, great security features and a modular design. While it started as a regular syslogd, rsyslog has evolved into a kind of swiss army knife of logging, being able to
	- accept inputs from a wide variety of sources,
	- transform them,
	- and output the results to diverse destinations.
- [IPVS (IP Virtual Server)](http://www.linuxvirtualserver.org/software/ipvs.html) implements transport-layer load balancing inside the Linux kernel, so called Layer-4 switching. IPVS running on a host acts as a load balancer at the front of a cluster of real servers, it can direct requests for TCP/UDP based services to the real servers, and makes services of the real servers to appear as a virtual service on a single IP address.
- [Балансировка нагрузки с LVS](https://habrahabr.ru/post/104621/)
- [Loadbalancing / failover with IPVS and keepalived](http://blackbird.si/loadbalancing-failover-with-ipvs-and-keepalived/)
- [Keepalived](http://www.keepalived.org/) is a routing software written in C. The main goal of this project is to provide simple and robust facilities for loadbalancing and high-availability to Linux system and Linux based infrastructures. Loadbalancing framework relies on well-known and widely used Linux Virtual Server (IPVS) kernel module providing Layer4 loadbalancing. 
- [Amavisd](https://www.amavis.org/) is a high-performance interface between mailer (MTA) and content checkers: virus scanners, and/or SpamAssassin.
- [ClamAV®](http://www.clamav.net/) is an open source antivirus engine for detecting trojans, viruses, malware & other malicious threats.


## R
- [Set Application Domain Name with Shiny Server](https://www.r-statistics.com/2016/10/set-application-domain-name-with-shiny-server/)
- [Google spreadsheets + google forms + R = Easily collecting and importing data for analysis](https://www.r-statistics.com/2010/03/google-spreadsheets-google-forms-r-easily-collecting-and-importing-data-for-analysis/)

# 24.10.2016
## R
- readr::read_delim
	- Добавлена [locales](https://blog.rstudio.org/2015/10/28/readr-0-2-0/) `vignette("locales")`

# 21.10.2016
## R
- New! [The R graph Gallery](http://www.r-graph-gallery.com/)
- [Do Faster Data Manipulation using These 7 R Packages](https://www.analyticsvidhya.com/blog/2015/12/faster-data-manipulation-7-packages/)
- Fast write CSV
	- [Fast csv writing for R](http://blog.h2o.ai/2016/04/fast-csv-writing-for-r/)
	- [Fast Writing of Data From R to txt|csv Files: readr package]
	- [Most efficient way of exporting large (3.9 mill obs) data.frames to text file?](http://stackoverflow.com/questions/9703068/most-efficient-way-of-exporting-large-3-9-mill-obs-data-frames-to-text-file)
	- [write.csv for large data.table in R](http://stackoverflow.com/questions/12013953/write-csv-for-large-data-table-in-r)



## Anomaly
- [Introducing practical and robust anomaly detection in a time series](https://blog.twitter.com/2015/introducing-practical-and-robust-anomaly-detection-in-a-time-series)
- [Anomaly Detection with Twitter in R](https://anomaly.io/anomaly-detection-twitter-r/).
- [Anomaly Detection Using Elasticsearch](http://info.prelert.com/prelert-elastic-user-group-meetup).
- [Anomaly.io](https://anomaly.io/). Detect unusual patterns. То, чем должен был бы быть tAdvizor.


# 20.10.2016
## R
- [mutate_each / summarise_each in dplyr: how do I select certain columns and give new names to mutated columns?](http://stackoverflow.com/questions/27027347/mutate-each-summarise-each-in-dplyr-how-do-i-select-certain-columns-and-give). Как превратиь все строковые колонки в числовые?
- R & Spark
	- [Tutorial: Scalable R on Spark with SparkR, sparklyr and RevoScaleR](http://blog.revolutionanalytics.com/2016/10/tutorial-scalable-r-on-spark.html)
	- [KDD 2016: Scalable R on Spark](https://github.com/Azure/Azure-MachineLearning-DataScience/tree/master/Misc/KDDCup2016)

## RandomForest
- [NA/NaN/Inf in foreign function call (arg 1)](https://discuss.analyticsvidhya.com/t/error-in-randomforest-default-m-y-na-nan-inf-in-foreign-function-call-arg-1-in-r/1264)
This error generally occurs in randomForest due to the following reasons:
	- If a variable passed is character
	- actual NaNs and Infs
 -[How to eliminate “NA/NaN/Inf in foreign function call (arg 7)” running predict with randomForest](http://stackoverflow.com/questions/21964078/how-to-eliminate-na-nan-inf-in-foreign-function-call-arg-7-running-predict-w)
One cause of the error message:
    NA/NaN/Inf in foreign function call (arg X)
When training a randomForest is having character-class variables in your data.frame. If it comes with the warning:

## DevOps
- [Когда Chef и Puppet — не решение. Часть 1](https://habrahabr.ru/post/263595/)
- [Managing code with r10k](https://docs.puppet.com/pe/latest/r10k.html). r10k is a code management tool that allows you to manage your environment configurations (such as production, testing, and development) in a source control repository. Based on the code in your control repo branches, r10k creates environments on your master and installs and updates the modules you want in each environment.
- [Capistrano](http://capistranorb.com/). A remote server automation and deployment tool written in Ruby.
- [The Ultimate List of Deployment Tools](https://xebialabs.com/the-ultimate-devops-tool-chest/deployment/)

# 19.10.2016
- Not well-formed XML. Undefined 'deg' entity.
Проблема в том, что всякие &deg; не распознаются xml парсером, пока не добавишь определение всяких ENTITY. Это не проблема xml2.
[“Reference to undefined entity” error in XML file](https://alexatnet.com/articles/reference-undefined-entity-error-xml-file)
You may think that if entities are added into XHTML documents they can be added to XML feed too. Good idea but it will add to feed for about 30Kb of DOCTYPE definition. If it is OK, then only what you need to do is to download the following plain text files:
	- http://www.w3.org/TR/xhtml1/DTD/xhtml-lat1.ent
	- http://www.w3.org/TR/xhtml1/DTD/xhtml-symbol.ent
	- http://www.w3.org/TR/xhtml1/DTD/xhtml-special.ent
```
<!DOCTYPE feed [
 paste the content of xhtml-lat1.ent, 
 xhtml-symbol.ent and xhtml-special.ent here ]>
```

# 18.10.2016
## R
- [Model assessment. Purrr + dplyr](http://r4ds.had.co.nz/model-assess.html)
- [How to Manipulate Files in R](http://www.dummies.com/programming/r/how-to-manipulate-files-in-r/). Occasionally, you may want to write a script in R that will traverse a given folder and perform actions on all the data in the files or a subset of files in that folder.
To get a list of files in a specific folder, use `list.files()` or `dir()`. These two functions do exactly the same thing, but for backward-compatibility reasons, the same function has two names
- [Working with files and folders in R](http://www.masterdataanalysis.com/r/working-with-files-and-folders-in-r/)
- [Find duplicated elements with dplyr](http://stackoverflow.com/questions/28244123/find-duplicated-elements-with-dplyr)
- COOL! [Selecting columns and renaming are so easy with dplyr](https://blog.exploratory.io/selecting-columns-809bdd1ef615)
- [replace string in R giving a vector of patterns and vector of replacements](http://stackoverflow.com/questions/28529823/replace-string-in-r-giving-a-vector-of-patterns-and-vector-of-replacements)

# 17.10.2016
## R
- [XML XPath syntax](http://www.w3schools.com/xml/xpath_syntax.asp)
- COOL! [How do R and Python complement each other in data science?](http://stats.stackexchange.com/questions/238726/how-do-r-and-python-complement-each-other-in-data-science)
- [Interview with J.J. Allaire](Interview with J.J. Allaire)

# 14.10.2016
## R
- Convert Character Vector between Encodings
```
iconv(x, from = "", to = "", sub = NA, mark = TRUE, toRaw = FALSE)
iconvlist()
```
- [Converting a \u escaped Unicode string to ASCII](http://stackoverflow.com/questions/17761858/converting-a-u-escaped-unicode-string-to-ascii)
- [Decode <e8> <e9> etc. characters in R](http://stackoverflow.com/questions/10110585/decode-e8-e9-etc-characters-in-r)
- [stringi: Character String Processing Facilities](https://cran.r-project.org/web/packages/stringi/)
	- `stri_enc_list(simplify = FALSE)`
- [UTF-8 encoder/decoder](https://mothereff.in/utf-8)
- [STAT 545: Regular Expression in R](http://stat545.com/block022_regular-expression.html)
- [R: gsub of exact full string with fixed = T](http://stackoverflow.com/questions/30918550/r-gsub-of-exact-full-string-with-fixed-t)

## Office & Python
- [Use VBA SaveAs in Excel 2007-2016](http://www.rondebruin.nl/win/s5/win001.htm)
- [Python and Microsoft Office – Using PyWin32](http://www.blog.pythonlibrary.org/2010/07/16/python-and-microsoft-office-using-pywin32/)


# 13.10.2016
## R
- install.packages("RDocumentation")
library("RDocumentation")
Do you want to automatically load RDocumentation when you start R? [y|n] y
Congratulations!
R will now use RDocumentation to display your help files.
If you're offline, R will just display your local documentation.
To avoid automatically loading the RDocumentation package, use disable_autoload().
If you don't want the ? and help functionality to show RDocumentation pages, use disable_override().
- [3 Reasons to Learn Caret](https://www.datacamp.com/community/blog/3-reasons-to-learn-caret)
- [Tutorial: Scalable R on Spark with SparkR, sparklyr and RevoScaleR](http://blog.revolutionanalytics.com/2016/10/tutorial-scalable-r-on-spark.html). [all of the materials available on Github](https://github.com/Azure/Azure-MachineLearning-DataScience/tree/master/Misc/KDDCup2016)
- Filling in NAs with last non-NA value
	- [R: dplyr – Update rows with earlier/previous rows values](http://www.markhneedham.com/blog/2015/06/28/r-dplyr-update-rows-with-earlierprevious-rows-values/)
	- [Filling in NAs with last non-NA value](http://www.cookbook-r.com/Manipulating_data/Filling_in_NAs_with_last_non-NA_value/)
	- [Replace missing value with previous value](http://stackoverflow.com/questions/14655286/replace-missing-value-with-previous-value)
- data.frame: select column by name
	- [how can i tell select() in dplyr that the string it is seeing is a column name in a data frame](http://stackoverflow.com/questions/22028937/how-can-i-tell-select-in-dplyr-that-the-string-it-is-seeing-is-a-column-name-i)
	- dplyr.pdf: 
'''
vars <- c("Petal.Length", "Petal.Width")
select(iris, one_of(vars))
'''

# 12.10.2016
## Blog
- [Top 16 Blogging Platforms For 2016](https://www.hover.com/blog/top-16-blogging-platforms-for-2016/)

## R
- [access attributes of a class in R](http://stackoverflow.com/questions/6449565/access-attributes-of-a-class-in-r)
- [corrr 0.2.1 now on CRAN](https://drsimonj.svbtle.com/corrr-021-now-on-cran). [Using corrr](https://cran.r-project.org/web/packages/corrr/vignettes/using-corrr.html)

# 11.10.2016
## R
- COOL! [The ggiraph package let R users to make ggplot interactive](http://davidgohel.github.io/ggiraph/introduction.html). The package is an htmlwidget.
- [Mapping (historic) tracks in ggplot2](http://spatial.ly/2016/10/mapping-historic-tracks-ggplot2/)
- [Streamline your analyses linking R to SAS: the workfloweR experiment](http://datascienceplus.com/streamline-your-analyses-linking-r-to-sas/)
- [Animate maps with mapmate: R package for map- and globe-based still image sequences](https://blog.snap.uaf.edu/2016/10/10/animate-maps-with-mapmate-r-package-for-map-and-globe-based-still-image-sequences/)
- [Shiny leaflet example](https://uasnap.shinyapps.io/ex_leaflet/) by Matthew Leonawicz

# 10.10.2016
## R
- [Extending accessibility of open-source statistical software to the masses: A shiny case study.](http://educate-r.org//2016/10/07/canam.html) Brandon LeBeau, University of Iowa
- [Haven](http://haven.tidyverse.org/index.html) allows you to load foreign data formats (SAS, SPSS and Stata) in to R by wrapping the fantastic ReadStat C library written by Evan Miller.
- [R Tutorial. S3 Classes](http://www.cyclismo.org/tutorial/R/s3Classes.html)
- [R Tutorial. S4 Classes](http://www.cyclismo.org/tutorial/R/s4Classes.html)
- Open Source Patent Analytics. A work in progress home for the WIPO Open Source Patent Analytics Manual. [Reading and Writing an Excel File in R](http://poldham.github.io/reading-writing-excel-files-R/)


# 07.10.2016
## DataScience
- [Text Mining in R and Python: 8 Tips To Get Started](https://www.datacamp.com/community/blog/text-mining-in-r-and-python-tips)
- [BeakerTM](http://beakernotebook.com/). The Data Scientist's Laboratory
Beaker is a notebook-style development environment for working interactively with large and complex datasets. Its plugin-based architecture allows you to switch between languages or add new ones with ease, ensuring that you always have the right tool for any of your analysis and visualization needs.
- [Jupyter Notebook](https://jupyter.org/). Open source, interactive data science and scientific computing across over 40 programming languages.
- DeepLearning
	- [Computational Network Toolkit](https://www.cntk.ai/). Production-quality, Open Source, Multi-machine, Multi-GPU, Highly efficient RNN training, Speech, Image, Text
	- [Computational Network Toolkit (CNTK)](https://github.com/Microsoft/CNTK)
	- [Microsoft releases CNTK, its open source deep learning toolkit, on GitHub](http://blogs.microsoft.com/next/2016/01/25/microsoft-releases-cntk-its-open-source-deep-learning-toolkit-on-github/)

## R
- [Basic Forecasting Methods using R](https://gallery.cortanaintelligence.com/Notebook/Basic-Forecasting-Methods-using-R-1)
- [R Wrong encoding in Rstudio console (but ok in R GUI and ggplot2)](http://stackoverflow.com/questions/19900668/r-wrong-encoding-in-rstudio-console-but-ok-in-r-gui-and-ggplot2). `Sys.setlocale("LC_CTYPE", "en_RU.UTF-8")` Did the job! now utf files with Cyrillic characters display properly in the R/RStudio Console. But that only seems to work until R or RStudio is restarted.
- [UTF-8 with R Markdown, knitr and Windows](http://stackoverflow.com/questions/39022872/utf-8-with-r-markdown-knitr-and-windows?noredirect=1&lq=1)
- [R Markdown & knitr (encoding)](https://support.rstudio.com/hc/en-us/community/posts/200635258-R-Markdown-knitr-encoding-)

Под Windows консоль переключается так 9[Table of locales](https://docs.moodle.org/dev/Table_of_locales)):
```
Sys.setlocale("LC_CTYPE", "English")
Sys.setlocale("LC_CTYPE", "Russian_Russia.1251")
```


# 06.10.2016
## R color palettes
- [The viridis color palettes](https://cran.r-project.org/web/packages/viridis/vignettes/intro-to-viridis.html)
- [A Wes Anderson color palette for R](https://github.com/karthik/wesanderson)
- [Colors (ggplot2)](https://habrahabr.ru/company/piter/blog/276675/)
- [Introducing artyfarty: a theming package for ggplot2](http://fishyoperations.com/2016/10/05/introducing-artyfarty.html)
	- [ggplot2 theme presets](https://github.com/Bart6114/artyfarty). artyfarty focuses on providing easy access to a few 'nice' ggplot theme, it also includes a number of predefined palettes and watermark convenience functions.

artyfarty is a work in progress. For now you can install the development version using devtools.

## R
- [Extract elements from nested list only using functions from purrr package](http://stackoverflow.com/questions/34751624/extract-elements-from-nested-list-only-using-functions-from-purrr-package)
- [R Notebooks](http://rmarkdown.rstudio.com/r_notebooks.html) An R Notebook is an R Markdown document with chunks that can be executed independently and interactively, with output visible immediately beneath the input.
NOTE: R Notebooks are new feature of RStudio, and are currently available only in the RStudio Preview Release. If you want to try out the features described below please install the preview release.
Overview

# 05.10.2016
## R
- [The Art of the Chart: Weather Radials](http://www.highcharts.com/blog/209-the-art-of-the-chart-weather-radials)
- [Visualizing the Daily Variability of Bitcoin with Quandl and Highcharts](https://fronkonstin.com/2016/10/04/visualizing-the-daily-variability-of-bitcoin-with-quandl-and-highcharts/)
- [Linpe: make sending and receiving data analysis faster and easier](http://www.quantide.com/linpe-make-sending-receiving-data-analysis-faster-easier/)
- [Metrum Research Group](http://metrumrg.com/opensourcetools.html) At MRG, we are strong advocates of open-source software development efforts. In fact, we make several of the useful tools we've developed for our own work available as free, open-source software under GPL. 
- [Example models for Stan http://mc-stan.org/](https://github.com/stan-dev/example-models). This repository holds open source Stan models, data simulators, and real data. There are models translating those found in books, most of the BUGS examples, and some basic examples used in the manual.

- SaveRDS
	- [A better way of saving and loading objects in R](http://www.fromthebottomoftheheap.net/2012/04/01/saving-and-loading-r-objects/)
	- [saveRDS and compression](http://rpubs.com/hadley/saveRDS). Experiment by Hadley Wickham
	- [Effect of compression type and file complexity on saveRDS size and speed](http://rpubs.com/dgrtwo/saveRDS). Experiment by David Robinson. Github [source](https://gist.github.com/dgrtwo/de967c2714e3ff490439)
- [gather on tibble = Error: Each variable must have a unique name](https://github.com/hadley/tidyr/issues/231). It looks like one solution is to specify key and value names by myself. It's a pity that key = "key", value = "value" aren't the default parameters.

## RandomForest
- [Trees, Random Forsets, Boosting for Continuous Variable Prediction](http://rstudio-pubs-static.s3.amazonaws.com/156481_80ee6ee3a0414fd38f5d3ad33d14c771.html)
- [Getting random forest prediction accuracy for a continuous variable in R](http://stackoverflow.com/questions/29996435/getting-random-forest-prediction-accuracy-for-a-continuous-variable-in-r)
- COOL! [Part 4a: Modelling - predicting the amount of rain](http://theanalyticalminds.blogspot.ru/2015/04/part-4a-modelling-predicting-amount-of.html)
- [Разработка → Препроцессинг данных и анализ моделей tutorial](https://habrahabr.ru/post/173049/)
- COOL! [Заметки по R: Случайный лес (random forest)](http://bdemeshev.github.io/r_cycle/cycle_files/22_forest.html)
- COOL! [Разработка → Модель Random Forest для классификации, реализация на c#](https://habrahabr.ru/post/215453/)
- [Random Forest с примерами на R](http://www.algorithmist.ru/2012/05/random-forest-r.html)

## Other
- [Лучшие плагины для Mozilla FireFox (мой выбор)](http://sonikelf.ru/luchshie-plaginy-dlya-mozilla-firefox-ili-moj-lyubimyj-brauzer/)
- [Logentries](https://logentries.com/). Cloud Live Log Management and Analytics

# 04.10.2016
## R
- LDA
	- COOL! [A gentle introduction to topic modeling using R](https://eight2late.wordpress.com/2015/09/29/a-gentle-introduction-to-topic-modeling-using-r/)
	- [Введение для новичков: что такое Латентное размещение Дирихле (LDA)?](https://mebius.io/analysis/intro-to-LDA). Популярно о сложном — об известнейшем методе машинного обучения под названием «Латентное размещение Дирихле».
- [Bayesian and frequentist reasoning in plain English](http://stats.stackexchange.com/questions/22/bayesian-and-frequentist-reasoning-in-plain-english)
- Блестящий цикла материалов про LDA:
	- [Вероятностные модели: от наивного Байеса к LDA, часть 1](https://habrahabr.ru/company/surfingbird/blog/228249/)
	- [Вероятностные модели: LDA, часть 2](https://habrahabr.ru/company/surfingbird/blog/230103/)
- [Find out more about Themescape](http://ip-science.thomsonreuters.com/winningmove/secure/TI_Themescape_QT.html)
- [Консалтинговая контора по DataScience](https://projectbotticelli.com/). Взял с конференции Микрософт:[Putting Science into the Business of Data Science](https://channel9.msdn.com/Events/Machine-Learning-and-Data-Sciences-Conference/Data-Science-Summit-2016/MSDSS05), Date: September 26, 2016, Speakers: Rafal Lukawiecki

# 03.10.2016
## R
- [Danger, Caution H2O steam is very hot!!](https://longhowlam.wordpress.com/2016/10/01/danger-caution-h2o-steam-is-very-hot/)
- [Some insights in soccer transfers using Market Basket Analysis](https://longhowlam.wordpress.com/2016/09/12/some-insights-in-soccer-transfers-using-market-basket-analysis/)

# 29.09.2016
## Data Science
- [Wakari.io](https://wakari.io/). Web-based Python Data Analysis
- [Domino makes data scientists more productive and facilitates collaborative, reproducible, reusable analysis.](https://www.dominodatalab.com/)
- Google Cloud Platform
	- [Architecture: Real-Time Stream Processing for IoT](https://cloud.google.com/solutions/architecture/real-time-stream-processing-iot)


## Value Proposition
- [26 Value Proposition Examples That Convert Visitors](https://sumome.com/stories/value-proposition-examples)
- [7 of the Best Value Proposition Examples We’ve Ever Seen](http://www.wordstream.com/blog/ws/2016/04/27/value-proposition-examples)

# 28.09.2016
## R
- Тонкий тюнинг readxl
	- Настройка параметров импорта: ["Specifying Column Types when Importing xlsx Data to R with Package readxl"](http://stackoverflow.com/questions/31633891/specifying-column-types-when-importing-xlsx-data-to-r-with-package-readxl/31634003)
`readxl:::xlsx_col_types(path = "a.xlsx", nskip = 116, n = 1)`
- Как обработать колонки с отсутстующими именами (NA). См. документацию по tibble: repair_names ensures its input has non-missing and unique names (duplicated names get a numeric
suffix). Valid names are left as is.
- [Removing NA in dplyr pipe [duplicate]](http://stackoverflow.com/questions/26665319/removing-na-in-dplyr-pipe)
- [Removing NA observations with dplyr::filter()](http://stackoverflow.com/questions/28857653/removing-na-observations-with-dplyrfilter)
na.omit(), complete.cases()
- [R FAQ. How does R handle date values?](http://www.ats.ucla.edu/stat/r/faq/dates.htm). 
```
as.numeric(as.Date(edates, origin = "1900-01-01"))
[1] -3514  8415 14707
```
When R looks at dates as integers, its origin is January 1, 1970.
```
    as.numeric(as.Date(edates, origin = "1900-01-01"))
    [1] -3514  8415 14707
    startdate <- "1970-01-01"
    as.numeric(as.Date(startdate))
```

# 27.09.2016
## R
- [Upgrading to plotly 4.0 (and above)](http://nvxwizlsnzsgc5db.obwg65bonr4q.cmle.ru/upgrading-to-plotly-4-0-and-above/)

# 24.09.2016
## Wolfram
- [Color Schemes](https://reference.wolfram.com/language/guide/ColorSchemes.html). The Wolfram Language includes a wide selection of carefully chosen color schemes that can immediately be used throughout the Wolfram Language graphics and visualization system.

## Изыскания по yandex.taxi
- dplyr unique
	- [Select unique values with 'select' function in 'dplyr' library](http://stackoverflow.com/questions/25571547/select-unique-values-with-select-function-in-dplyr-library)
	- [Select distinct/unique rows](https://rdrr.io/cran/dplyr/man/distinct.html)
	- [Using purrr with dplyr](http://lionel-.github.io/2015/10/08/using-purrr-with-dplyr/). Мапируем на каждую колонку
- dplyr conditional mutate
	- [Better syntax for mutate() than nested "ifelse" functions #1518](https://github.com/hadley/dplyr/issues/1518)
	- [can dplyr package be used for conditional mutating?](http://stackoverflow.com/questions/24459752/can-dplyr-package-be-used-for-conditional-mutating)
	- [Using conditions in dplyr::mutate](http://stackoverflow.com/questions/28080814/using-conditions-in-dplyrmutate)
	- [R for Data Science, 19.4 Conditional execution](http://r4ds.had.co.nz/functions.html#conditional-execution)
	- [Equivalent of SQL CASE #631. Closed](https://github.com/hadley/dplyr/issues/631). `case_when` конструкция.	
	- [dplyr mutate with function call returning incorrect value](http://stackoverflow.com/questions/36300381/dplyr-mutate-with-function-call-returning-incorrect-value).
You could also use Vectorize
	- [Use variable names in functions of `dplyr`](http://stackoverflow.com/questions/24569154/use-variable-names-in-functions-of-dplyr)

- [Woking with Dates and Times with lubridate in R](https://rpubs.com/davoodastaraky/lubridate)
- [Window functions and grouped mutate/filter](https://cran.r-project.org/web/packages/dplyr/vignettes/window-functions.html)
- [rminer: Data Mining Classification and Regression Methods](https://cran.r-project.org/web/packages/rminer/). Facilitates the use of data mining algorithms in classification and regression (including time series forecasting) tasks by presenting a short and coherent set of functions.
- [TimeZones](http://unicode.org/repos/cldr/trunk/common/supplemental/windowsZones.xml)

# 23.09.2016
## Microsoft
- [How to Install and Use the Linux Bash Shell on Windows 10](http://www.howtogeek.com/249966/how-to-install-and-use-the-linux-bash-shell-on-windows-10/).
Windows 10’s Anniversary Update offers a big new feature for developers: A full, Ubuntu-based Bash shell that can run Linux software directly on Windows. This is made possible by the new “Windows Subsystem for Linux” Microsoft is adding to Windows 10.
	- Документация находится на веб-сайте https://aka.ms/wsldocs

## Data Science
- COO-O-L! [Which tool should I use?](http://brohrer.github.io/which_tool_should_i_use.html). Data Science and Robots Blog

## R
- [String manipulations on full names](http://f.briatte.org/r/string-manipulation-on-full-names)
- [Handling and Processing Strings in R](http://gastonsanchez.com/Handling_and_Processing_Strings_in_R.pdf), Gaston Sanchez
- [Using purrr with dplyr](http://lionel-.github.io/2015/10/08/using-purrr-with-dplyr/)
08 October 2015

## Telco operator churn
- [Анализ оттока клиентов с помощью Машинного обучения Azure](https://azure.microsoft.com/ru-ru/documentation/articles/machine-learning-azure-ml-customer-churn-scenario/)
- [Negative Correlation Learning for Customer Churn Prediction: A Comparison Study](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC4386545/)
- [Customer churn prediction using improved balanced random forests](http://lib.cufe.edu.cn/upload_files/file/20140521/3_20140521_Customer%20churn%20prediction%20using%20improved%20balanced%20random%20forests.pdf)
- [Churn prediction in telecom using Random Forest and PSO based data balancing in combination with various feature selection strategies](https://www.researchgate.net/publication/256918723_Churn_prediction_in_telecom_using_Random_Forest_and_PSO_based_data_balancing_in_combination_with_various_feature_selection_strategies)

# 22.09.2016
## Machine Learning & Random Forest
- [7 tools in every data scientist’s toolbox](http://blog.datadive.net/7-tools-in-every-data-scientists-toolbox/)
- [Interpreting random forests](http://blog.datadive.net/interpreting-random-forests/)
- [A Complete Tutorial on Tree Based Modeling from Scratch (in R & Python)](https://www.analyticsvidhya.com/blog/2016/04/complete-tutorial-tree-based-modeling-scratch-in-python/)
- [A Gentle Introduction to Random Forests, Ensembles, and Performance Metrics in a Commercial System](https://citizennet.com/blog/2012/11/10/random-forests-ensembles-and-performance-metrics/)
- [Деревья принятия решений с примерами на R](http://www.algorithmist.ru/2012/05/decision-trees-in-r.html)
- [Random Forest с примерами на R](http://www.algorithmist.ru/2012/05/random-forest-r.html)
- [Использование Random Forest (случайного леса) для предсказания цен акций](http://rforfinance.ru/random-forest/)
- [Random Forests](https://www.stat.berkeley.edu/~breiman/RandomForests/). Leo Breiman and Adele Cutler
Random Forests(tm) is a trademark of Leo Breiman and Adele Cutler and is licensed exclusively to Salford Systems for the commercial release of the software.
Our trademarks also include RF(tm), RandomForests(tm), RandomForest(tm) and Random Forest(tm).


## Big Data
- [Informatica Big Data Management and Ranger Integration](http://blogs.informatica.com/2016/06/07/informatica-big-data-management-and-ranger-integration/)

## R
- [Welcome to the Tidyverse](http://blog.revolutionanalytics.com/2016/09/tidyverse.html)
- [The tidy tools manifesto](https://mran.microsoft.com/web/packages/tidyverse/vignettes/manifesto.html). Hadley Wickham. 2016-09-09
- [Creating nests without tidyr](http://nacnudus.github.io/crossprod/creating-nests-without-tidyr)
- [Nest repeated values in a list-variable](https://www.rdocumentation.org/packages/tidyr/versions/0.6.0/topics/nest). Тут вместе с онлайн консолью выполнения кода.
- [mrdwab/splitstackshape](https://github.com/mrdwab/splitstackshape). R functions to split concatenated data, conveniently stack columns of data.frames, and conveniently reshape data.frames. 
- [the most useful R function of the week: unnest from tidyr](http://bioinfoblog.it/2015/02/the-most-useful-r-command-unnest-from-tidyr/)
- [Crossprod blog](http://nacnudus.github.io/crossprod/)
- Queuing theory with R. The simmer package is a relatively new R package for discrete event simulation (DES). It’s an exciting development, because there isn’t a lot of open-source DES software. SimPy seems to be the only serious competitor for teaching DES and queueing theory.
	- [Simmer vs SimPy: The Bank, Part I](http://nacnudus.github.io/crossprod/simmer-vs-simpy-the-bank-part-i)
	- [Simmer vs SimPy: The Bank, Part II](http://nacnudus.github.io/crossprod/simmer-vs-simpy-the-bank-part-ii)
	- [Hacking the Data Science Radar with Data Science]
- [Introduction to R](https://ramnathv.github.io/pycon2014-r/). These are notes for an introductory R workshop I am teaching for Python Programmers.
- [Will Stanton's Data Science Blog](http://will-stanton.com/)
	- [Why you should learn Spark if you want to be a data scientist](http://will-stanton.com/why-you-should-learn-spark-if-you-want-to-be-a-data-scientist/)
	- [Machine Learning with R: An Irresponsibly Fast Tutorial](http://will-stanton.com/machine-learning-with-r-an-irresponsibly-fast-tutorial/). Анализ данных проекта "Титаник\Titanic" с помощью пакета 'caret'

# 21.09.2016
## R
- [Handling and Processing Strings in R - Gaston Sanchez](http://gastonsanchez.com/Handling_and_Processing_Strings_in_R.pdf)
- [R / Notes](http://f.briatte.org/r/). This page contains a collection of short notes on using the R statistical software.
Интересный блог с практическими примерами.
	- [ggnetwork: Network geometries for ggplot2](http://f.briatte.org/r/ggnetwork-network-geometries-for-ggplot2)
	- [String manipulations on full names](http://f.briatte.org/r/string-manipulation-on-full-names)
- Проверка объектов на схожесть:
	- [Testing](http://r-pkgs.had.co.nz/tests.html). There are two basic ways to test for equality: expect_equal(), and expect_identical(). expect_equal() is the most commonly used: it uses all.equal() to check for equality within a numerical tolerance. If you want to test for exact equivalence, or need to compare a more exotic object like an environment, use expect_identical(). It’s built on top of identical().
	- [identical {base}](https://stat.ethz.ch/R-manual/R-devel/library/base/html/identical.html). Test Objects for Exact Equality. 
The safe and reliable way to test two objects for being exactly equal. It returns TRUE in this case, FALSE in every other case.
	- [all.equal {base}](https://stat.ethz.ch/R-manual/R-devel/library/base/html/all.equal.html). Test if Two Objects are (Nearly) Equal.
all.equal(x, y) is a utility to compare R objects x and y testing ‘near equality’. If they are different, comparison is still made to some extent, and a report of the differences is returned. Do not use all.equal directly in if expressions—either use isTRUE(all.equal(....)) or identical if appropriate.

## R Slicing
- [Data Science with R by Garrett Grolemund](http://garrettgman.github.io/tidying/). Data Tidying
“Tidy datasets are all alike but every messy dataset is messy in its own way.” – Hadley Wickham
- [Convert R vector to string vector of 1 element](http://stackoverflow.com/questions/13973116/convert-r-vector-to-string-vector-of-1-element).
Use the collapse argument to paste: 
```
paste(a,collapse=" ")
[1] "aa bb cc
```
- [How to split a data frame?](http://stackoverflow.com/questions/3302356/how-to-split-a-data-frame)
- [Split data.table into roughly equal parts](http://stackoverflow.com/questions/32125795/split-data-table-into-roughly-equal-parts)
- [Emulate split() with dplyr group_by: return a list of data frames](http://stackoverflow.com/questions/33775239/emulate-split-with-dplyr-group-by-return-a-list-of-data-frames)
- [tidyr 0.4.0](https://blog.rstudio.org/2016/02/02/tidyr-0-4-0/). There are two big features in this release: support for nested data frames, and improved tools for turning implicit missing values into explicit missing values. Пришел отсюда: [with recent version of tidyr (0.4.1), you could replace do(vals=data.frame(.)) by nest(). vals will be named data by default – aurelien Mar 8 at 12:01](http://stackoverflow.com/questions/33775239/emulate-split-with-dplyr-group-by-return-a-list-of-data-frames)
- [I'll add the data.table version for anyone else Googling it (i.e., @BondedDust's solution translated to data.table)](http://stackoverflow.com/questions/4126326/how-to-quickly-form-groups-quartiles-deciles-etc-by-ordering-columns-in-a/27646599#27646599):
```
library(data.table)
setDT(temp)
temp[ , quartile := cut(value,
                        breaks = quantile(value, probs = seq(0, 1, by = 1/4)),
                        labels = 1:4, right = FALSE)]
```


# 20.09.2016
## Other
- [HighLoad++ 2016](http://www.highload.ru). Профессиональная конференция разработчиков высоконагруженных систем

## R
- [CRAN Task View: High-Performance and Parallel Computing with R](https://cran.r-project.org/web/views/HighPerformanceComputing.html)
- [A brief foray into parallel processing with R](https://beckmw.wordpress.com/2014/01/21/a-brief-foray-into-parallel-processing-with-r/), January 21, 2014
- [A few thoughts on the existing code parallelization](http://www.vesnam.com/Rblog/existing-code-parallelization-yes-or-no/), September 17, 2016
- [Хабр: Разработка → Запуск функций R на нескольких машинах](https://habrahabr.ru/company/infopulse/blog/309052/)
- [Хабр: Разработка → Небольшое введение в параллельное программирование на R](https://habrahabr.ru/company/infopulse/blog/307708/)


# 19.09.2016
## R
- [R 3.3.0 is another motivation for Docker](http://r-addict.com/2016/05/13/Docker-Motivation.html)
- [Monitoring R Applications with RZabbix](http://r-addict.com/2016/09/15/RZabbix-Announcement.html)
	- [Monitoring Analytics](https://github.com/monitoringartist/monitoring-analytics). R statistical computing and graphic tool for monitoring metrics from data scientists https://hub.docker.com/r/monitoringartist/monitoring-analytics
- [Why Averages Suck and Percentiles are Great](http://apmblog.dynatrace.com/2012/11/14/why-averages-suck-and-percentiles-are-great/)

## R + Business
- [17 Revolution Analytics Case Studies](http://www.featuredcustomers.com/vendor/revolution-analytics-1/case-studies)
- [Why The R Programming Language Is Good For Business](https://www.fastcompany.com/3030063/why-the-r-programming-language-is-good-for-business)
Thanks to one company, the same code that is revolutionizing the scientific community is now moving up the ranks of the business world.
	- "R can do literally everything, and all new research is done in R. So especially for businesses that really want to out-compete their competitors on the basis of advanced analytics, they can get access to everything they need within R, things that might not come for five or 10 years through commercial software," says Smith.

## Big Data
- [Поминки по Big Data](http://www.globalcio.ru/workshops/1358/)
- [Конец Big Data](http://fastsalttimes.com/sections/obzor/628.html). Видимо, перепечатка.
- [The Demise of Big Data, Its Lessons and the State of Things to Come](https://www.gartner.com/doc/3115022/demise-big-data-lessons-state)
- [The end of Big Data. It’s all over now.](http://blogs.gartner.com/andrew_white/2015/08/20/the-end-of-big-data-its-all-over-now/) by Andrew White  |  August 20, 2015
- [Big Data Isn’t Obsolete. It’s Normal.](http://blogs.gartner.com/nick-heudecker/big-data-is-now-normal/) by Nick Heudecker  |  August 20, 2015
- [NewProLab facebook](https://www.facebook.com/newprolab/posts/1054494544663918:0)

## Auto
- [Курьер](https://dostavista.ru/order?standard)
- [Разборка](http://евроавто.рф/)

# 16.09.2016
## Machine Learning
- [10 More lessons learned from building real-life Machine Learning systems — Part I — Medium](https://medium.com/@xamat/10-more-lessons-learned-from-building-real-life-ml-systems-part-i-b309cafc7b5e)
- [Machine Learning is Fun! Part 2 — Medium](https://medium.com/@ageitgey/machine-learning-is-fun-part-2-a26a10b68df3)
- [A Neural Network in 11 lines of Python (Part 1) - i am trask](http://iamtrask.github.io/2015/07/12/basic-python-network/)
- [The state of Computer Vision and AI: we are really, really far away](http://karpathy.github.io/2012/10/22/state-of-computer-vision/)

## Web
- [Wix](http://ru.wix.com/) Все начинается с красивого сайта. Создайте свой. Это легко и бесплатно.

## BigData
- [Все итоги ICBDA 2015](http://rb.ru/list/vse-itogi-icbda-2015/)
- [RusBase](http://rb.ru/)

## Time-series
- [Change point analysis](http://stats.stackexchange.com/questions/59755/change-point-analysis). Could someone please explain change point to me. I'm using the package in R, and I don't really understand what the different methods mean, the pros and cons of each, and I especially do not understand the penalty value. When you increase the penalty value, what does that mean and what does it do? I have done a good amount of research online but I just keep finding the cran R and quick R sites, which are good, but the way they say it just isn't cutting it for me.
- [Change Point Detection Packages in R](http://things-about-r.tumblr.com/post/106806522699/change-point-detection-in-time-series-with-r-and):
	- [CPM](https://cran.r-project.org/web/packages/cpm/index.html) – “Parametric and Nonparametric Sequential Change Detection in R”:
    Useful for detecting multiple change points in a time series from an unknown underlying distribution. Another bonus is that the method is applicable to data streams, where an observation is only considered once. Because of the “stream nature” of the cpm approach a second output are the detection points themselves. They mark the time when the change point is detected by the algorithm and quantify the delay. Unfortunately the cpm package is no longer maintained on CRAN. For windows users I uploaded a zipped version of the installed package from my R library here. It should work with R 3.0 and 3.1 under Windows 7/8.
	- [BCP](https://cran.r-project.org/web/packages/bcp/index.html) – “An R Package for Performing a Bayesian Analysis of Change Point Problems”:
    A package using Markov Chain Monte Carlo to find multiple change points within a sequence. The implementation is generalized to the multivariate case where we expect that within a segment all sequences have a constant mean where the mean is not necessarily the same for all sequences. Finding change points in multivariate time series is not discussed in this posting.
	- [ECP](https://cran.r-project.org/web/packages/ecp/index.html) – “An R Package for Nonparametric Multiple Change Point Analysis of Multivariate Data”:
    Another package for the detection of multiple change points within a time series that is also applicable to multivariate time series and makes no assumptions about the distribution. It uses an approach similar to hierarchical clustering with either a divisive or an agglomerative procedure to identify the change points. Even if it is not explicitly stated, most probably the “E” stands for energy as the method is using the energy statistic of Székely and Rizzo to identify changes.

## R
### R+Business
- [Why The R Programming Language Is Good For Business](https://www.fastcompany.com/3030063/why-the-r-programming-language-is-good-for-business).
Thanks to one company, the same code that is revolutionizing the scientific community is now moving up the ranks of the business world.
- [17 Revolution Analytics Case Studies](http://www.featuredcustomers.com/vendor/revolution-analytics-1/case-studies)
- [Revolution Analytics Review](http://www.butleranalytics.com/revolution-analytics-review/)

### Technical
- [tidyverse 1.0.0](https://blog.rstudio.org/2016/09/15/tidyverse-1-0-0/). The tidyverse is a set of packages that work in harmony because they share common data representations and API design. The tidyverse package is designed to make it easy to install and load core packages from the tidyverse in a single command.
```{r}
library(tidyverse)
tidyverse_conflicts()
tidyverse_update()
```
- [The ensurer package](https://cran.r-project.org/web/packages/ensurer/vignettes/ensurer.html)
- [colourpicker: A colour picker widget for Shiny apps, RStudio, R-markdown, and 'htmlwidgets'](http://deanattali.com/blog/colourpicker-package/)
- COOL! [Reading and combining many tidy data files in R](http://serialmentor.com/blog/2016/6/13/reading-and-combining-many-tidy-data-files-in-R)
- [Simple algorithm for online outlier detection of a generic time series](http://stats.stackexchange.com/questions/1142/simple-algorithm-for-online-outlier-detection-of-a-generic-time-series)
- [Simpler R coding with pipes > the present and future of the magrittr package](https://www.r-statistics.com/2014/08/simpler-r-coding-with-pipes-the-present-and-future-of-the-magrittr-package/)
- COOL! [Use of ~ (tilde) in R programming Language](http://stackoverflow.com/questions/14976331/use-of-tilde-in-r-programming-language). 
The thing on the right of <- is a formula object. It is often used to denote a statistical model, where the thing on the left of the ~ is the response and the things on the right of the ~ are the explanatory variables. So in English you'd say something like "Species depends on Sepal Length, Sepal Width, Petal Length and Petal Width".
The myFormula <- part of that line stores the formula in an object called myFormula so you can use it in other parts of your R code.
Other common uses of formula objects in R
	- The lattice package uses them to [specify the variables to plot](http://www.inside-r.org/packages/CRAN/lattice/docs/xyplot).
	- The ggplot2 package uses them to [specify panels for plotting](http://www.inside-r.org/packages/CRAN/ggplot2/docs/facet_wrap).
	- The dplyr package uses them for [non-standard evaulation](http://cran.r-project.org/web/packages/dplyr/vignettes/nse.html).
- dplyr & operator ~ (tilde). NSE = [non-standard evaulation](http://cran.r-project.org/web/packages/dplyr/vignettes/nse.html)
- [Non-standard evaluation](https://cran.r-project.org/web/packages/lazyeval/vignettes/lazyeval.html)
- [R: PARALLEL COMPUTING IN 5 MINUTES](http://blog.aicry.com/r-parallel-computing-in-5-minutes/)

# 15.09.2016
## R
- [R-bloggers. 2175 search results for "time series"](https://www.r-bloggers.com/search/time%20series/page/4/)
- Blog [Data * Science + R](http://things-about-r.tumblr.com/). Exploring the world of data with R, Tableau and other nice stuff 
	- [Change Point Detection in Time Series with R and Tableau](http://things-about-r.tumblr.com/post/106806522699/change-point-detection-in-time-series-with-r-and). 
- [bayes.js: A Small Library for Doing MCMC in the Browser](http://www.sumsar.net/blog/2015/12/bayes-js-a-small-library-for-doing-mcmc-in-the-browser/)
- [Autocorrelation functions of materially different time series](http://ellisp.github.io/blog/2015/09/19/timeseries-same-acf)

## Math
- [Using R for Time Series Analysis](http://a-little-book-of-r-for-time-series.readthedocs.io/en/latest/src/timeseries.html)
- [Calculating Pearson correlation and significance in Python](http://stackoverflow.com/questions/3949226/calculating-pearson-correlation-and-significance-in-python)
- STAT 510. Applied Time Series Analysis. [8.2 Cross Correlation Functions and Lagged Regressions](https://onlinecourses.science.psu.edu/stat510/node/74)
- [Pearson product-moment correlation coefficient](https://en.wikipedia.org/wiki/Pearson_product-moment_correlation_coefficient)

# 14.09.2016
## R
- [Spurious correlations](http://www.tylervigen.com/spurious-correlations)
- [Creating an animation using R](http://datascienceplus.com/creating-an-animation-using-r/)
- [Exploring ways for using DiagrammeR to generate graphs/plots that can be exported to svg and included in knitr documents.](http://www.carlboettiger.info/2015/05/15/diagrammer.html)
	- [Week 14 | Exporting Widget](http://www.buildingwidgets.com/blog/2015/4/9/week-14-exporting-widget)
- [Creating network visualisations interactively with DiagrammeR and Shiny](https://timesenses.wordpress.com/2016/01/05/creating-network-visualisations-interactively-with-diagrammer-and-shiny/)
- [Using DiagrammeR in Word document (generated using rMarkdown)](http://stackoverflow.com/questions/30307191/using-diagrammer-in-word-document-generated-using-rmarkdown)

- [Trelliscope: Detailed Visualization of Large Complex Data in R](https://github.com/tesseradata/trelliscope)
	- [trelliscope - Tutorial](http://tessera.io/docs-trelliscope/#introduction). Trelliscope provides a way to flexibly visualize large, complex data in great detail from within the R statistical programming environment. Trelliscope is a component in the Tessera environment.
	- [trelliscope v.0.9.4 by Ryan Hafen](http://www.rdocumentation.org/packages/trelliscope/versions/0.9.4)
- [PhantomJS](http://phantomjs.org/) is a headless WebKit scriptable with a JavaScript API. It has fast and native support for various web standards: DOM handling, CSS selector, JSON, Canvas, and SVG.
- [Capturing wild widgets with webshot](https://rud.is/b/2016/03/04/capturing-wild-widgets-with-webshot/)
	- Winston Chang released his webshot package to CRAN this past week. The package wraps the immensely useful phantomjs utility and makes it dirt simple to capture whole or partial web pages in R. One beautiful bonus feature of webshot is that you can install phamtomjs with it (getting phantomjs to work on Windows is a pain).
- [An Introduction to the webshot Package](https://cran.r-project.org/web/packages/webshot/vignettes/intro.html)

- [Заметки по R: R внутри документов](http://bdemeshev.github.io/r_cycle/cycle_files/26_literate_programming.html)
- [File path issues in R using Windows (“Hex digits in character string” error)](http://stackoverflow.com/questions/8425409/file-path-issues-in-r-using-windows-hex-digits-in-character-string-error)
- [Efficiently convert backslash to forward slash in R](http://stackoverflow.com/questions/17605563/efficiently-convert-backslash-to-forward-slash-in-r)

## R. вывод в файл содержания htmlwidget
текст функции widgetThumbnail {trelliscope} [здесь](https://gist.github.com/hrbrmstr/b5e8ec60490b825ea889)
под windows эта функция в PhantomJS не работает, поскольку они генерирую в js файле такую ссылку:
file://C:\Users\Ilya\AppData\Local\Temp\RtmpC49SU3\file4ac030a64c90.html
а надо
file:///D:/iwork.GH/R.projects/_phjs/file4ac030a64c90.html

Наверное, это связано со спецсимволами
А имя файла, включая путь, генерится функцией tempfile() {base}, но там слеши выдаются закрытыми
Если запустить `phantomjs --debug=true file4ac0211e48f0.js`, то видна диагностика. При неправильных слешах пропадает последняя директория и всякие htmlwidgets.js не находятся


# 13.09.2016
## Mathematica
- [How to export large graphics?](http://mathematica.stackexchange.com/questions/296/how-to-export-large-graphics)
- [Formats for Text in Graphics](https://reference.wolfram.com/language/tutorial/FormatsForTextInGraphics.html)
This tells the Wolfram Language what default text style to use for all subsequent plots.
In[4]:=	
 Click for copyable input
✕ SetOptions[Plot, BaseStyle -> {FontFamily -> "Times", FontSize -> 14}];

## R
- [Upgrade notes for Shiny 0.14](http://shiny.rstudio.com/articles/upgrade-0.14.html)
- [What is Parallel Computing?](http://www.parallelr.com/r-with-parallel-computing/)

# 12.09.2016
## Tools
- [Upgrading Git/Mercurial in SourceTree for Windows](https://confluence.atlassian.com/sourcetreekb/upgrading-git-mercurial-in-sourcetree-for-windows-695108075.html). Место загрузки изменилось: https://www.mercurial-scm.org/downloads

# 08.09.2016
## R
- [HW Checker: R, AppScripts, & Google Forms](http://data-steve.github.io/build-homework-checker-pt1/)
- [Integrating Google Spreadsheet/Apps Script with R: Enabling social network analysis in TAGS](https://mashe.hawksey.info/2012/01/tags-r/)
- [RStudio v0.99 Preview: Graphviz and DiagrammeR](https://blog.rstudio.org/2015/05/01/rstudio-v0-99-preview-graphviz-and-diagrammer/). May 1, 2015 in RStudio IDE	
- [Create Graph Diagrams and Flowcharts Using R](http://rpackages.ianhowson.com/cran/DiagrammeR/)
	- [R + mermaid.js](http://rpackages.ianhowson.com/cran/DiagrammeR/man/mermaid.html). Make diagrams in R using mermaid.js with infrastructure provided by htmlwidgets. 
- [V8: Embedded JavaScript Engine for R](https://cran.r-project.org/web/packages/V8/index.html). An R interface to Google's open source JavaScript engine. V8 is written in C++ and implements ECMAScript as specified in ECMA-262, 5th edition. In addition, this package implements typed arrays as specified in ECMA 6 used for high-performance computing and libraries compiled with 'emscripten'.
- [rio: A Swiss-Army Knife for Data I/O](https://cran.r-project.org/web/packages/rio/README.html)

## Tools
- [Mermaid](https://knsv.github.io/mermaid/#mermaid). Generation of diagrams and flowcharts from text in a similar manner as markdown.

# 07.09.2016
## R
- [Hadleyverse](http://blog.revolutionanalytics.com/2015/03/hadleyverse.html)
- [The Hitchhiker's Guide to the Hadleyverse](http://adolfoalvarez.cl/the-hitchhikers-guide-to-the-hadleyverse/)
- ebook [A MODERN DIVE into Data with R](https://ismayc.github.io/moderndiver-book/)
- ebook in GIF. [Getting used to R, RStudio, and R Markdown](https://ismayc.github.io/rbasics-book/index.html)
- [R manually set shape by factor](http://stackoverflow.com/questions/26218002/r-manually-set-shape-by-factor)

## Shiny
- [JavaScript Events in Shiny](https://cran.r-project.org/web/packages/shiny/vignettes/events.html)

# 02.09.2016
## R
- [Dean Attali's Shiny Server](http://daattali.com/shiny/)

# 01.09.2016
## CoolVendors in Data Science
- [Satalia](https://www.satalia.com/)
- [Algorithmia](https://algorithmia.com/)
- [Dato](https://turi.com/index.html), ранее https://dato.com.
- [SparkBeyond](http://www.sparkbeyond.com/)
- [CoSMo](https://www.thecosmocompany.com/)

## Math
- [Статистика вокруг нас](https://habrahabr.ru/company/stepic/blog/250527/)
- [Online курс 'Основа статистики' ](https://stepic.org/course/%D0%9E%D1%81%D0%BD%D0%BE%D0%B2%D1%8B-%D1%81%D1%82%D0%B0%D1%82%D0%B8%D1%81%D1%82%D0%B8%D0%BA%D0%B8-76/syllabus)

## R
- [R AnalyticFlow](http://r.analyticflow.com/en/) is a data analysis software that utilizes the R environment for statistical computing.
In addition to intuitive user interface, it also provides advanced features for R experts. These features enable you to share the processes of data analysis between users with differing levels of proficiency. R AnalyticFlow works on Windows, Mac OS X, and Linux and is free for any use.
- [useR 2016 tutorial on "Understanding and creating interactive graphics"](https://github.com/tdhock/interactive-tutorial)

# 31.08.2016
## R
- [ezknitr](http://deanattali.com/blog/ezknitr-package/): R package to avoid the typical working directory pain when using knitr
- [revealjs](https://cran.rstudio.com/web/packages/revealjs/): R Markdown format for 'reveal.js' presentations, a framework for easily creating beautiful presentations using HTML.
- [The printr](http://yihui.name/printr/) (read “printer” or “print R”) package is a companion package to knitr. Its main purpose is to extend the S3 generic function knit_print() in knitr, which is the default value of the chunk option render, as explained in the vignette knit_print.html.
- validate package. [Rules in text files](https://cran.r-project.org/web/packages/validate/vignettes/rule-files.html) by Mark van der Loo and Edwin de Jonge
- [FiveThirtyEight. Our 47 Weirdest Charts From 2015](http://fivethirtyeight.com/features/our-47-weirdest-charts-from-2015/). Отличная инфографика. А вот их доклад на UseR! 2016: [FiveThirtyEight's data journalism workflow with R](https://channel9.msdn.com/events/useR-international-R-User-conference/useR2016/FiveThirtyEights-data-journalism-workflow-with-R)
- [YAML](http://www.yaml.org/): YAML Ain't Markup Language

# 30.08.2016
## R
- COOL. [Shiny tips & tricks for improving your apps and solving common problems](http://deanattali.com/blog/advanced-shiny-tips/). Github [sources](https://github.com/daattali/advanced-shiny#readme)
- [shinyjs](https://github.com/daattali/shinyjs). Easily improve the user interaction and user experience in your Shiny apps in seconds
- [Joe Cheng RPubs](https://rpubs.com/jcheng)
- [Interactive scatterplots with scatterD3](https://cran.r-project.org/web/packages/scatterD3/vignettes/introduction.html)
- PURRR. Type stable functions. Look at RStudio blog: [purrr 0.2.0, January 6, 2016 in Packages](https://blog.rstudio.org/2016/01/06/purrr-0-2-0/)
- [Use quick formula functions in purrr::map (+ base vs tidtyverse idiom comparisons/examples)](https://rud.is/b/2016/07/26/use-quick-formula-functions-in-purrrmap-base-vs-tidtyverse-idiom-comparisonsexamples/)
- [addinslist package](http://deanattali.com/blog/addinslist-package/). An RStudio addin to discover and install RStudio addins
- [The R Package Known As DiagrammeR](http://rich-iannone.github.io/DiagrammeR/). R + RStudio + htmlwidgets + JavaScript + d3.js + viz.js + mermaid.js
Generate graph diagrams using text in a Markdown-like syntax.
- [timevis](https://daattali.com/shiny/timevis-demo/). An R package for creating timeline visualizations. GitHub [code](https://github.com/daattali/timevis).
- [Crosstalk](https://github.com/rstudio/crosstalk). A package for R that enhances htmlwidgets with client side, inter-widget interactions (currently linked brushing and filtering).
- [robservable](https://github.com/ramnathv/robservable) is an R package that brings observables to R. It provides a generic framework to create reactive widgets that can interact with each other using a shiny-like API. This will allow R users to build entire web apps with interactive widgets that can be rendered purely in a browser.
- [set color scaling of a vector in R](http://stackoverflow.com/questions/27810944/set-color-scaling-of-a-vector-in-r)
```{r}
# Create a color function that will return colors in the range we want
colorfunc = colorRamp(c("blue","white","red"))
# Use colorfunc to create colors that range from blue to white to red across the range of x
mycolors = rgb(colorfunc(x), maxColorValue=255)
```
- [htmlwidgets for R - gallery](http://gallery.htmlwidgets.org/). 76 registered widgets available to explore (30.08.2016)

## R Markdown
- [R Markdown from RStudio](http://rmarkdown.rstudio.com/)
- [Bookdown: Authoring Books with R Markdown](https://bookdown.org/yihui/bookdown/). Yihui Xie, 2016-07-19
- [knitr in a knutshell a minimal tutorial](http://kbroman.org/knitr_knutshell/). KnitR is a really important tool for reproducible research. You create documents that are a mixture of text and code; when processed through KnitR, the code is replaced by the results and/or figures produced.
- [Tufte Handout](https://rstudio.github.io/tufte/). An implementation in R Markdown. JJ Allaire and Yihui Xie
- [Tutorial R Markdown](http://www.jacolienvanrij.com/Tutorials/tutorialMarkdown.html) by Jacolien van Rij
- [knitr](http://yihui.name/knitr/). Elegant, flexible and fast dynamic report generation with R
- [Introduction to knitr](https://sachsmc.github.io/knit-git-markr-guide/knitr/knit.html)

## Web
- [CSS для Чайников](http://technologyweb.org/div-%D0%B8-span/)
- [MobX was formerly known as Mobservable.](https://github.com/mobxjs/mobx) Simple, scalable state management.

# 29.08.2016
## R
- [How to reshape data in R: tidyr vs reshape2](http://www.milanor.net/blog/reshape-data-r-tidyr-vs-reshape2/). Ну не заменяют они друг друга, а дополняют
- [How to expand color palette with ggplot and RColorBrewer](http://novyden.blogspot.ru/2013/09/how-to-expand-color-palette-with-ggplot.html)
- [How to generate column dependent random variable with dplyr](http://stackoverflow.com/questions/30352497/how-to-generate-column-dependent-random-variable-with-dplyr)
- Dual axes
	- [Dual axes time series plots may be ok sometimes after all](http://ellisp.github.io/blog/2016/08/18/dualaxes). Dual axis time series charts are often deprecated, but the standard alternatives have weaknesses too. In some circumstances, if done carefully, dual axis time series charts may be ok after all. In particular, you can choose two vertical scales so the drawing on the page is equivalent to drawing two indexed series, but retaining the meaningful mapping to the scale of the original variables.
	- [Dual axes time series plots with various more awkward data](http://ellisp.github.io/blog/2016/08/28/dualaxes2). TL;DR Summary:
I finish enhancements of the dual axes time series plotting function in R so it handles reasonably well series that may start at different times, have different frequencies, or include negatives.
	- [Two Y-Axes](https://kieranhealy.org/blog/archives/2016/01/16/two-y-axes/). Matt remarked that “Friends don’t let friends use two y-axes”. It’s a good rule. The topic came up a couple of times during the data visualization short course I taught last semester. Using two y-axes makes it even easier than usual to fool yourself (or someone else) about the degree of association between two variables. This is because you can adjust the scaling of the axes to relative to one another in way that moves the data series around more or less however you like.
	- [Dual axes for ggplot2](https://gist.github.com/jslefche/e4c0e9f57f0af49fca87). Modified from: [ggplot2-adding-secondary-transformed-x-axis-on-top-of-plot](https://stackoverflow.com/questions/21026598/ggplot2-adding-secondary-transformed-x-axis-on-top-of-plot) & [dual_axis_in_ggplot2](https://rpubs.com/kohske/dual_axis_in_ggplot2)
	- [R: single plot with two different y-axes](http://www.gettinggeneticsdone.com/2015/04/r-single-plot-with-two-different-y-axes.html)

## Web
- [Google Web Designer](http://www.google.com/webdesigner/). Create engaging, interactive HTML5-based designs and motion graphics that can run on any device.

# 26.08.2016
## R
- [Analysis of the #7FavPackages hashtag](http://varianceexplained.org/r/seven-fav-packages/)
- [Microsoft ratchets up its R enthusiasm](http://www.computerworld.com/article/3109533/business-intelligence/microsoft-ratchets-up-its-r-enthusiasm.html)
- [R with Power BI: Import, Transform, Visualize and Share](http://blog.revolutionanalytics.com/2016/08/powerbi-and-r.html)
- [Python style logging in R](http://mazamascience.com/WorkingWithData/?p=1727)

# 25.08.2016
## Bootstrap & HTML
- [Уроки по Bootstrap. Урок №1: что это и как начать с ним работать ](http://dedushka.org/uroki/6901.html)
- [7 Bootstrap Editors for Rapid Development of Responsive Websites](https://bootstrapbay.com/blog/bootstrap-editors/)
- [Reveal.js](http://lab.hakim.se/reveal-js/). The HTML Presentation Framework.
	- [Исходники на Github](https://github.com/hakimel/reveal.js/)

## R
- [Rperform](https://github.com/analyticalmonk/rperform). R package for tracking performance metrics across git versions and branches. https://analyticalmonk.github.io/Rperform
- [A Helpful Way to Install R Packages Hosted on GitHub](https://cran.r-project.org/web/packages/githubinstall/vignettes/githubinstall.html). Koji MAKIYAMA (@hoxo_m), 2016-08-11
- [The pacman package](https://github.com/trinker/pacman) is an R package management tool that combines the functionality of base library related functions into intuitively named functions.
- [githubinstall package](https://cran.r-project.org/web/packages/githubinstall/vignettes/githubinstall.html). The githubinstall package provides a way to install packages on GitHub by only their package names just like install.packages(). [Запись на блоге автора](http://mockquant.blogspot.ru/2016/06/githubinstall-new-r-package-for-easy-to.html)
- COOL! User R 2016!. Effective Shiny Programming. [Slides](https://cdn.rawgit.com/jcheng5/user2016-tutorial-shiny/master/slides.html). Joe Cheng <joe@rstudio.com> #useR2016 — June 27, 2016
- R as ETL
	- [ETL for Medium Data](http://www.science.smith.edu/~bbaumer/talks/useR_talk.html)
	- Небольшой холивар. [R vs Pentaho Spoon as an ETL tool (closed)](http://stackoverflow.com/questions/14996712/r-vs-pentaho-spoon-as-an-etl-tool)
	- [etl: Extract-Transform-Load Framework for Medium Data](https://cran.r-project.org/web/packages/etl/index.html)
	- [R package to facilitate ETL operations](https://github.com/beanumber/etl)

## Полезные функции
 - `sessionInfo()`
 - githubibstall: `gh_show_source("mutate", repo = "dplyr")` or `library(dplyr); gh_show_source(mutate)`. Show the Source Code of Functions on GitHub.
По githubistall смотри: [A Helpful Way to Install R Packages Hosted on GitHub](https://cran.r-project.org/web/packages/githubinstall/vignettes/githubinstall.html);
[A Helpful Way to Install R Packages](https://github.com/hoxo-m/githubinstall); [githubinstall 0.1.0: New Feature for A Helpful Way to Install R Packages Hosted on GitHub](http://mockquant.blogspot.ru/)

# 23.08.2016
## R
- [Hadley Wickham twitter](https://twitter.com/hadleywickham)
- [#rstats Twitter](https://twitter.com/hashtag/rstats?src=hash)
- [forcats](https://github.com/hadley/forcats). forcats provides tools for categorical variables (forcats is an anagram of factors).
- ggplot2
	- [ggplot2 extensions - gallery](http://www.ggplot2-exts.org/)
	- [ggpolypath](https://github.com/mdsumner/ggpolypath). A ggplot2 geom for polygons with holes, called 'geom_polypath'.
- [Plotting background data for groups with ggplot2](https://drsimonj.svbtle.com/plotting-background-data-for-groups-with-ggplot2)
- [Improving R animated GIFs with tweenr](http://lenkiefer.com/2016/05/29/improving-R-animated-gifs-with-tweenr)
- [Efficient R programming. E-book](https://csgillespie.github.io/efficientR/)
- [Bookdown: Authoring Books with R Markdown. E-book](https://bookdown.org/yihui/bookdown/). Yihui Xie, 2016-07-19

- [JSM 2016 session on Reproducibility in Statistics and Data Science](http://citizen-statistician.org/2016/08/03/jsm-2016-session-on-reproducibility-in-statistics-and-data-science/)
	- [Links to slides from JSM 2016](https://github.com/kbroman/JSM2016slides). Links to slides to talks at the 2016 Joint Statistical Meetings in Chicago, Illinois. Pull requests welcome! Or add an issue, or tweet @kwbroman or email Karl Broman.
- [Comparison of Statistical Packages](https://r-economics.com/2016/04/02/comparison-of-statistical-packages/)

## Microsoft
- [Активация Office 365, Office 2016 или Office 2013](https://support.office.com/ru-ru/article/%D0%90%D0%BA%D1%82%D0%B8%D0%B2%D0%B0%D1%86%D0%B8%D1%8F-Office-365-Office-2016-%D0%B8%D0%BB%D0%B8-Office-2013-1144e0de-e849-496e-8e33-ed6fb1b34202)
- [Поиск ключа продукта Office](https://support.office.com/ru-ru/article/%D0%9F%D0%BE%D0%B8%D1%81%D0%BA-%D0%BA%D0%BB%D1%8E%D1%87%D0%B0-%D0%BF%D1%80%D0%BE%D0%B4%D1%83%D0%BA%D1%82%D0%B0-Office-12a5763a-d45c-4685-8c95-a44500213759)

# 22.08.2016
# R CO-O-O-OL!
- [SNAP TECH](https://blog.snap.uaf.edu/). Technological solutions at SNAP, giving back to the community we learn from every day
	- [Customizable charts: Alaska communities, daily precipitation](https://uasnap.shinyapps.io/ak_daily_precipitation/)
	- [Community Charts v4 Lite](https://uasnap.shinyapps.io/cc4liteFinal/). Explore the climate outlook for your community
- [Matthew Leonawicz](http://leonawicz.github.io/) Statistician | Statistical Programmer | useR
- RStudio IDE: How did I not know about Alt-Shift-K (shows all keyboard shortcuts)?

- [Combining data tables and sparklines](http://leonawicz.github.io/HtmlWidgetExamples/ex_dt_sparkline.html). Examples using Edmonton, Alberta climate data
In the examples below, I use a 1950 - 2009 subset of SNAP’s 2-km resolution downscaled CRU 3.2 temperature and precipitation data for Edmonton, Alberta to demonstrate the use of the DT package for data tables and the sparkline package for inline graphs as well as integration of inline graphs into data tables. These packages make use of the htmlwidgets package and are interfaces to the jQuery plugins dataTables and sparkline.
- [sparklines for R](http://fishyoperations.com/2015/04/10/sparklines-for-R.html)
- [htmlwidgets for R - gallery](http://gallery.htmlwidgets.org/)
- [visNetwork](http://datastorm-open.github.io/visNetwork/) is an R package for network visualization, using vis.js javascript library (http://visjs.org/). All remarks and bugs are welcome on github : https://github.com/datastorm-open/visNetwork.
- [Sparkline](https://github.com/htmlwidgets/sparkline). This is an experimental R package that provides support for jquery sparkline as a HTML widget.


# .io projects
- [cimon.io](https://cimon.io/). BUILD AND DEPLOY AUTOMATION
- [codepen.io](http://codepen.io/). CodePen is a playground for the front end web. Show off your latest creation and get feedback. Build a test case for that pesky bug. Find example design patterns and inspiration for your projects.
- [CodeShare](https://codeshare.io/). Share code in real-time with other developers
- [Squad. Code Together](https://squadedit.com/). Squad is a web-based collaborative IDE. We make it simple to open, edit and share code in real time.
- [jsfiddle.net](https://jsfiddle.net/). Test your JavaScript, CSS, HTML or CoffeeScript online with JSFiddle code editor.
- [Online Coding. repl.it](https://repl.it/languages/javascript)
- [Online JavaScript console](https://jsconsole.com/)

# 19.08.2016
- [Enterprise Mashups](https://msdn.microsoft.com/en-us/library/bb906060.aspx) by Larry Clarkin and Josh Holmes. The Architecture Journal
- [Mash-up and visualise your data](http://www.lovesdata.com/blog/2014/mash-visualise-data)
- [x2w.js - xls2web jQuery plug-in](https://github.com/xls2web/x2w/). x2w.js is a jQuery plugin that bridges your custom Microsoft Excel spreadsheet saved on Onedrive (former Skydrive) and your website DOM elements. Inspired by www.excelmashup.com this small library is aimed at making your Excel mash-up development process as easy as calling your spreadheet by token and further processing of a JSON response.


# 18.08.2016
## R
- [Making fast, good decisions with the FFTrees R package](http://nathanieldphillips.com/2016/08/making-fast-good-decisions-with-the-fftrees-r-package/)

- [JASP](https://jasp-stats.org/), a low fat alternative to SPSS, a delicious alternative to R. Bayesian statistics made accessible.

## Other
- [map.aviasales.ru](http://map.aviasales.ru)
- [Chart: It’s not your imagination, US gun violence is over the top this summer](http://qz.com/741391/its-not-your-imagination-gun-violence-is-over-the-top-this-summer/)
- [Donald Trump’s Ghostwriter Tells All](http://www.newyorker.com/magazine/2016/07/25/donald-trumps-ghostwriter-tells-all). “The Art of the Deal” made America see Trump as a charmer with an unfailing knack for business. Tony Schwartz helped create that myth—and regrets it.

## Visualization
- [The Counted. People killed by police in the US](http://www.theguardian.com/us-news/ng-interactive/2015/jun/01/the-counted-police-killings-us-database)
- [The math of mass shootings](https://www.washingtonpost.com/graphics/national/mass-shootings-in-america/)

# 11.07.2016
## Software Development
- [Когда «agile» (не) к месту](http://makhmetov.ru/articles/agile.html)

# 06.07.2016
## Software Development
- [International Function Point Users Group](http://www.ifpug.org/)
- [AUDITING FUNCTION POINT COUNTS](http://www.softwaremetrics.com/fpsteps.htm)
- [Измерение трудозатрат на разработку информационной системы по методике COCOMO II и с помощью хронометража](http://itue.ru/?p=311)
- [Function Point Languages Table. Version 5.0](http://www.qsm.com/resources/function-point-languages-table). The QSM Function Points Languages Table contains updated function point language gearing factors for 37 distinct programming languages/technologies. The data supporting release 5.0 was drawn from 2192 recently completed function point projects from the QSM database.  The sample included 126 languages, 37 of which had sufficient data to be included in the table.
- [COCOMO II - Constructive Cost Model Online Calculator](http://csse.usc.edu/tools/COCOMOII.php)

# 05.07.2016
## R
- [The ggthemr package – Theme and colour your ggplot figures](http://www.shanelynn.ie/themes-and-colours-for-r-ggplots-with-ggthemr/). 
Shane Lynn. Data science, Startups, Data visualisation. Currently building KillBiller.com
- [Analysis of Weather data using Pandas, Python, and Seaborn](http://www.shanelynn.ie/analysis-of-weather-data-using-pandas-python-and-seaborn/)


# 04.07.2016
- [How to Apply Machine Learning to Event Processing](http://www.rtinsights.com/big-data-machine-learning-software-event-processing-analytics/)

## Visualization
- Plot.ly [Click callback for pie chart](https://github.com/plotly/plotly.js/issues/105)
- Click Events in R.
	- [How to bind callback functions to click events in R charts with JavaScript](https://plot.ly/r/click-events/)
- [Sisense](https://www.sisense.com/). Simplifying Business Intelligence for Complex Data. The only business intelligence software that lets you easily prepare and analyze both big and disparate datasets. 
	- [Embedding Dashboards and Widgets](https://www.sisense.com/documentation/embedding-dashboards-widgets/)
- [DASH](https://www.thedash.com/). Create beautiful dashboards with a few clicks. Dash is realtime dashboards for your website, your business, and your life. Your first dashboard is free forever.

## R
- [TIBCO Enterprise Runtime for R (TERR)](http://spotfire.tibco.com/discover-spotfire/what-does-spotfire-do/predictive-analytics/tibco-enterprise-runtime-for-r-terr)


# 01.07.2016
- [Gapminer. A fact-based worldview](https://www.gapminder.org/)

## DevOps
- [The Periodic Table of DevOps Tools](https://dzone.com/articles/the-periodic-table-of-devops-tools-v2-is-here-1). Или на [XebiaLabs](https://xebialabs.com/periodic-table-of-devops-tools/)

# 30.06.2106

## R
- [rud.is](https://rud.is/b/). "In God we trust. All others must bring data"
- excellent 6-part [Beginners guide to R](http://www.computerworld.com/s/article/9239625/Beginner_s_guide_to_R_Introduction)
- [Advanced Beginner's Guide to R](http://www.computerworld.com/resources/106345/advanced-beginners-guide-to-r.html)
- [Plotly R figure reference](https://plot.ly/r/reference/)
- [Pining for the fjoRds & monitoring SSL/TLS certificate expiration in R with flexdashboard](https://rud.is/b/2016/05/01/pining-for-the-fjords-monitoring-ssltls-certificate-expiration-in-r-with-flexdashboard/)
- [split data.frame into list by rows](http://stackoverflow.com/questions/5110732/r-converting-each-row-of-a-data-frame-into-a-list-item)
```
df2 <- data.frame(x = as.numeric(df.label$x), y = -df.label$y, text = as.character(df.label$text), showarrow = TRUE, stringsAsFactors = FALSE)
am <- split(df2, 1:nrow(df2))
a <- lapply(am, as.list)
```
соображения
```
# list(annotation = a) дает ошибку 
# "Error in FUN(X[[i]], ...) : 'options' must be a fully named list, or have no names (NULL)"
# Не совсем ясно, почему. Но plotly_build(p2)$layout$annotations существет и туда засунута легенда
# если сделать так:   layout(annotations = NULL) %>% layout(annotations = a), то все проходит
```
- [flexdashboard Examples](http://rmarkdown.rstudio.com/flexdashboard/examples.html)
The examples below illustrate the use of flexdashboard with various packages and layouts. If you want to learn more about how the dashboards were created each example includes a link to it’s source code.

# 29.06.2016
## R
- [Express Intro to dplyr. Working The Data Like a Boss!](https://rollingyours.wordpress.com/2016/06/29/express-intro-to-dplyr/).
- Slides
	- [jsonlite and mongolite](http://bit.ly/mongo-slides) from [UseR! 2015](http://user2015.math.aau.dk/oral_sessions)
	- [The gridGraphics Package](https://www.stat.auckland.ac.nz/~paul/Talks/useR2015/gridgraphics.html)


## plotly
- [geom_label() in plotly](https://github.com/ropensci/plotly/issues/546) -> [ Dynamic list of unsupported geoms #348](https://github.com/ropensci/plotly/issues/348)

# 28.06.2016
## Other
- [CTRLQ.org. SEARCH BY IMAGE. Know more about any photograph with Google Reverse Image Search](https://ctrlq.org/google/images/)
- [TinEye Reverse Image Search](https://www.tineye.com/)
- [Best Reverse Image Search Engines, Apps And Its Uses (2016)](http://beebom.com/reverse-image-search-engines-apps-uses/)

# 27.06.2016
## R
- [Data Science End-to-End Walkthrough. Microsoft SQL Server 2016](https://msdn.microsoft.com/en-gb/library/mt612857.aspx)
- COOL! [Microsoft Analytics in 2016](http://www.cybaea.net/journal/2016/06/24/Microsoft-Analytics-in-2016)
 -[Fixing R’s design flaws in a new version of pqR](https://radfordneal.wordpress.com/2016/06/25/fixing-rs-design-flaws-in-a-new-version-of-pqr/). Operator `..`
- [archivist](http://pbiecek.github.io/archivist/). Archiving, Managing and Sharing R Objects. 
Archivist allows you to store selected artifacts as binary files together with their metadata and relations. Archivist allows you to share artifacts with others, either through a shared folder or github. Archivist allows you to look for already created artifacts by using its class, name, date of creation or other properties. It also facilitates restoring such artifacts. Archivist allows to check if a new artifact is the exact copy of the one that was produced some time ago. This might be useful either for testing or caching.
- [Easy data validation with the validate package](http://www.markvanderloo.eu/yaRb/2016/03/25/easy-data-validation-with-the-validate-package/)

## Shiny
- [Shiny + archivist = reproducible interactive exploration](http://smarterpoland.pl/index.php/2016/06/shiny-archivist-reproducible-interactive-exploration/). [Archivist](http://pbiecek.github.io/archivist/) is a package for management of R objects. It allows you to create a repository (local folder or git repo) and push all interesting R objects to it. Each object will be stored along with its metadata. Each object will get it’s unique key, i.e. md5hash.
Then you or your collaborators may access these objects from any R process, local or remote.] 

# 24.06.2016
## Shiny
- [Stop Shiny and Close Browser Together](http://data-steve.github.io/shiny-shutdown-with-browser-close/). We wanted to be able to deploy local instances of shiny app and then when user is done with session, the user can close out the session by closing the browser and shutting down shiny server at same time.
- [Scaling and Performance - Tuning Applications in Shiny Server Pro](https://support.rstudio.com/hc/en-us/articles/220546267-Scaling-and-Performance-Tuning-Applications-in-Shiny-Server-Pro). Added: June 07, 2016
- [Scaling and Performance Tuning with shinyapps.io](http://shiny.rstudio.com/articles/scaling-and-tuning.html). Added: 07 Jan 2015
- [3.8 Reactivity Log](http://docs.rstudio.com/shiny-server/#server-hierarchy)
- [How do I deploy Shiny applications to Shiny Server?](https://support.rstudio.com/hc/en-us/articles/221319028-How-do-I-deploy-Shiny-applications-to-Shiny-Server-)
- [What web server is used by Shiny Server and Shiny Server Pro?](https://support.rstudio.com/hc/en-us/articles/218294977-What-web-server-is-used-by-Shiny-Server-and-Shiny-Server-Pro-). A: We currently use Node.js.
	- [What is Node.js? {closed}](http://stackoverflow.com/questions/1884724/what-is-node-js)
	- [Node.js - Introduction. What is Node.js?](http://www.tutorialspoint.com/nodejs/nodejs_introduction.htm). Node.js is a server side platform built on Google Chrome's JavaScript Engine (V8 Engine). Node.js was developed by Ryan Dahl in 2009 and its latest version is v0.10.36. The definition of Node.js as supplied by its official documentation is as follows −
```
Node.js is a platform built on Chrome's JavaScript runtime for easily building fast and scalable network applications. Node.js uses an event-driven, non-blocking I/O model that makes it lightweight and efficient, perfect for data-intensive real-time applications that run across distributed devices.
```

## R
- [Open Analytics. Architect](https://www.openanalytics.eu/products). Data scientists manage rich data sources, build statistical models and communicate findings. They work at the intersection of computer science and statistics and often rely on a multitude of tools to keep on top. 
- [Fastest way to check if dataframe is empty {duplicate}](http://stackoverflow.com/questions/30808195/fastest-way-to-check-if-dataframe-is-empty)

# 23.06.2016
## R
- Полезные команды для анализа инсталляции R:
	- `packageStatus()`
	- `sessionInfo()`
	- `update.packages(checkBuilt=TRUE)`

- [A step by step (screenshots) tutorial for upgrading R on Windows](http://www.r-statistics.com/2015/06/a-step-by-step-screenshots-tutorial-for-upgrading-r-on-windows/)
- [UpdateR package: update R version with a function (on MAC OSX)](https://andreacirilloblog.wordpress.com/2015/10/22/updater-package-update-r-version-with-a-function-on-mac-osx/)
- Ручное обновление R под Mac. [Update R using RStudio](http://stackoverflow.com/questions/13656699/update-r-using-rstudio)
- [Greek and alpha numeric in ggplot2 axis labels](http://stackoverflow.com/questions/15841538/greek-and-alpha-numeric-in-ggplot2-axis-labels)

## Dashboards
- [Dashbuilder](http://dashbuilder.org/) (Development is sponsored by Red Hat) is a full featured web application which allows non-technical users to visually create business dashboards.
Dashboard data can be extracted from heterogeneous sources of information such as JDBC databases or regular text files.
- [Business dashboard software for teams who want to continuously monitor the health of their business.](https://www.klipfolio.com/)
- [Bring your data to life with Microsoft Power BI](https://powerbi.microsoft.com/en-us/). Microsoft Power BI transforms your company's data into rich visuals for you to collect and organize so you can focus on what matters to you. Stay in the know, spot trends as they happen, and push your business further.
- [opCharts | Modern Charts, UI and Dashboards](https://opmantek.com/opcharts-dashboards-charts-management/). Modern, dynamic, interactive charting, custom dashboards and a RESTful API to visualize NMIS data and more. opCharts is ideal as a custom user interface and a customer portal.
- [iDasboards](http://www.idashboards.com/). Since our launch in 2003, iDashboards has provided clients with an easy-to-implement dashboard solution that offers dynamic chart and table options. While most competitors focus on numbers, we believe that the big picture should be attractive as well.


## Shiny etc.
- [New Zealand Tourism Dashboard](https://mbienz.shinyapps.io/tourism_dashboard_prod/). The New Zealand Tourism Dashboard is a one-stop shop for all information about tourism. It brings together a range of tourism datasets produced by MBIE and Statistics New Zealand into one easy-to-use tool. Information is presented using dynamic graphs and data tables.
	- [Just a short note](http://ellisp.github.io/blog/2016/02/24/tourism-dashboard/) that in my day job we’ve released the New Zealand Tourism Dashboard, launched by the Associate Minister for Tourism earlier today. It’s built with R and Shiny and I won’t say more about it than that to avoid mixing up my work and outside-work hats. Except that it’s really really awesome, and there’s an enormous amount of data in there to explore. Great work by the team.
	- Source code, minus a few design elements, is now available at [GitHub](https://github.com/nz-mbie/tourism-dashboard-public)
- [R-bloggers. 1012 search results for "Shiny"](http://www.r-bloggers.com/search/shiny/)

## Other
- [Scarabey.org](www.scarabey.org)

# 22.06.2016

## R
- COOL. [How to reshape data in R: tidyr vs reshape2](http://www.milanor.net/blog/reshape-data-r-tidyr-vs-reshape2/)
- Reproducible research
	- PirateGrunt. Pirates, grunts, etc. [represtools is on CRAN](http://pirategrunt.com/r/2016/06/21/ReprestoolsOnCran/)
	- [represtools. Reproducible research tools](http://pirategrunt.com/represtools/)
- [Research Triangle Analysts](http://www.rtpanalysts.org/home) is a unique forum for data enthusiasts in the Research Triangle of North Carolina (Raleigh, Durham, Chapel Hill, and the surrounding area).
- [Introducing the p-hacker app: Train your expert p-hacking skills](http://www.nicebread.de/introducing-p-hacker/)
- [MonetDBLite because fast](http://www.asdfree.com/2016/06/monetdblite-because-fast.html)


## IoT
- [InitialState](https://www.initialstate.com/). The Place To Keep Your Data. Data analytics for the internet of things.
- [Tutorial: How to send data to Initial State in SiteWhere](http://blog.initialstate.com/tutorial-how-to-send-data-to-initial-state-in-sitewhere/)
- ЖЖ Олега Артамонова. [Unwired Devices LLC и «Интернет вещей»](http://olegart.livejournal.com/1487714.html).

# 21.06.2016

## R
- ggplot leneds tweaking
	- [Turning off some legends in a ggplot](http://stackoverflow.com/questions/14604435/turning-off-some-legends-in-a-ggplot)
	- [Remove extra legends in ggplot2](http://stackoverflow.com/questions/11714951/remove-extra-legends-in-ggplot2)
- [Increase the size of variable-size points in ggplot2 scatter plot (duplicate)](http://stackoverflow.com/questions/20251119/increase-the-size-of-variable-size-points-in-ggplot2-scatter-plot)
- [setTimeLimit persists after function completes](http://stackoverflow.com/questions/12514899/settimelimit-persists-after-function-completes). Снимем лимиты времени, чтобы избежать ошибки "In is.gtable(x) : reached elapsed time limit"
- [How to expand color palette with ggplot and RColorBrewer](http://novyden.blogspot.ru/2013/09/how-to-expand-color-palette-with-ggplot.html)
# 20.06.2016
## R
- Join .CSV files
	- [Merge all files in a directory using R into a single dataframe](https://psychwire.wordpress.com/2011/06/03/merge-all-files-in-a-directory-using-r-into-a-single-dataframe/)
	- [Repeating things: looping and the apply family](http://nicercode.github.io/guides/repeating-things/)
	- [Using Lapply to Import Files to R](http://brianmannmath.github.io/blog/2014/01/20/using-lapply-to-import-files-to-r/)

- ['install_github' gives timeout reached error #877](https://github.com/hadley/devtools/issues/877). 
You'll need to do something like
```
library(httr)
with_config(use_proxy(...), install_github(...))
```

- [Five Interactive R Visualizations With D3, ggplot2, & RStudio](http://moderndata.plot.ly/interactive-r-visualizations-with-d3-ggplot2-rstudio/)
- [ggnet2: network visualization with ggplot2](https://briatte.github.io/ggnet/)

# Wolfram
- [How to color each point with a different color in ListPlot??](http://community.wolfram.com/groups/-/m/t/504085)

# 17.06.2016
## R
- [foreach]
	- [The Wonders of foreach](http://www.exegetic.biz/blog/2013/08/the-wonders-of-foreach/). Posted by Andrew Collier on 25 August 2013.
	- [How-to go parallel in R – basics + tips](http://gforge.se/2015/02/how-to-go-parallel-in-r-basics-tips/)
	- [For each row in an R dataframe](http://stackoverflow.com/questions/1699046/for-each-row-in-an-r-dataframe)
- [Check existence of directory and create if doesn't exist](http://stackoverflow.com/questions/4216753/check-existence-of-directory-and-create-if-doesnt-exist)

## DeployR
- Работа с внешними файлами
	- [Adding Files to External Directories](https://msdn.microsoft.com/en-us/microsoft-r/deployr-admin-manage-big-data)
	- [DeployR Open - Restrict file system access](http://stackoverflow.com/questions/36709291/deployr-open-restrict-file-system-access)
	- [Loading Data into the R Session](https://msdn.microsoft.com/en-us/microsoft-r/deployr-repository-manager/deployr-repository-manager-testing-debugging-scripts). Ищем такой пункт в тексте.
	- [Repository-Managed Files](https://msdn.microsoft.com/en-us/microsoft-r/deployr-api-reference). Ищем такой пункт в тексте.
	- [6.3 Working with the Project Workspace APIs](https://deployr.revolutionanalytics.com/documents/dev/api-doc/guide/single.html#projectworkspaceload)
	- [6.4 Working with the Project Directory APIs](https://deployr.revolutionanalytics.com/documents/dev/api-doc/guide/single.html#projectdirectory). "6.4.7 /r/project/directory/load"
- [The DeployR command line interface](https://github.com/Microsoft/deployr-cli)
- [DeployR. Simple R Analytics Integration for Application Developers](https://github.com/deployr)

# 16.06.16
## R
- [githubinstall: New R Package for Easy to Install R Packages on GitHub](http://mockquant.blogspot.ru/2016/06/githubinstall-new-r-package-for-easy-to.html). The githubinstall package provides a way to install packages on GitHub by only the package names just like install.packages(). githubinstall() suggests the GitHub repository from package names, and asks whether you want to execute the installation.
- [The R Project for Maps](http://www.web-maps.com/gisblog/?p=2365). R changes things in the geospatial world. The R project originated as a modular statistics and graphics toolkit. Unless you happen to be a true math prodigy, statistics are best visualized graphically. With powerful graphics libraries, R has evolved into a useful platform for ad hoc spatial analysis.
- [Welcome to R Tools for Visual Studio Preview!](http://microsoft.github.io/RTVS-docs/)
- [Introduction to data.tree](http://cran.r-project.org/web/packages/data.tree/vignettes/data.tree.html)
- [ipub. bridging finance and IT](http://ipub.com): 
	- [Solving Tic-Tac-Toe with R data.tree](http://ipub.com/tic-tac-toe/)
	- [Reference semantics in R](http://ipub.com/reference-semantics/)
- [MRAN checkpoint. Reproducibility: Using Fixed CRAN Repository Snapshots](https://mran.revolutionanalytics.com/documents/rro/reproducibility/)
- [Images as x-axis labels (updated)](http://jcarroll.com.au/2016/06/03/images-as-x-axis-labels-updated/)
- [Using caret to compare models](http://blog.revolutionanalytics.com/2016/05/using-caret-to-compare-models.html)
- [Good R Packages](http://blog.revolutionanalytics.com/2016/05/good-r-packages.html)

- COOL!. [For each row in an R dataframe](http://stackoverflow.com/questions/1699046/for-each-row-in-an-r-dataframe)

## IoT
- [IoT – Internet of Things (das Ding an sich)](http://www.web-maps.com/gisblog/?p=2404)
- [Azure IoT Suite](http://www.web-maps.com/gisblog/?p=2404)

# 15.06.16
## R
- Linear Regression
	- [Fitting & Interpreting Linear Models in R](http://blog.yhat.com/posts/r-lm-summary.html)
	- [Slides from my talk on the broom package](http://varianceexplained.org/r/broom-slides/)
	- [broom: a package for tidying statistical models into data frames](http://varianceexplained.org/r/broom-intro/)
	- [Estimated Simple Regression Equation](http://www.r-tutor.com/elementary-statistics/simple-linear-regression/estimated-simple-regression-equation)
- [Size of each object in R’s workspace](http://isomorphism.es/post/92559575719/size-of-each-object-in-rs-workspace)

# 14.06.16

## R
- Get current function name
	- [How to get the name of the calling function inside the called routine?](http://stackoverflow.com/questions/15595478/how-to-get-the-name-of-the-calling-function-inside-the-called-routine)
Or just deparse(sys.call()) – hadley Mar 25 '13 at 23:45
@hadley, nope, that gets the current call. I want the call one level above. – Ferdinand.kraft Mar 25 '13 at 23:54
Oh, that wasn't clear from your question. Try sys.call(-1) – hadley Mar 26 '13 at 13:13
@hadley, thanks, this is even better! – Ferdinand.kraft Mar 26 '13 at 15:58 

# 10.05.2016

## R
- [';--have i been pwned?](https://haveibeenpwned.com/). Check if you have an account that has been compromised in a data breach. Вариант использования взят [отсюда](http://itsalocke.com/hibpwned-on-cran/)
А отсылка на визуализацию ведет сюда: [World's Biggest Data Breaches. Selected losses greater than 30,000 records (updated 6th May 2016)](http://www.informationisbeautiful.net/visualizations/worlds-biggest-data-breaches-hacks/)
- [R for Publication by Page Piccinini: Lesson 3 – Logistic Regression](http://datascienceplus.com/r-for-publication-by-page-piccinini-lesson-3-logistic-regression/)
- Разбивка на диапазоны. Ключевое слово -- "ДИСКРЕТИЗАЦИЯ". См. область из машинного обучения. `discretize {arules}`, см. [Convert a Continuous Variable into a Categorical Variable](http://www.inside-r.org/packages/cran/arules/docs/discretize)
- Conditional dplyr mutate
	- [dplyr mutate/replace on a subset of rows](http://stackoverflow.com/questions/34096162/dplyr-mutate-replace-on-a-subset-of-rows)
	- [Function to replace values for specific rows #425](https://github.com/hadley/dplyr/issues/425)
- [Handling factor variables in dplyr](http://stackoverflow.com/questions/27879121/handling-factor-variables-in-dplyr). 
I want to use dplyr to extract the last value in grade.history and check it against current.grade: <...skipped...>. However, dplyr seems to convert the factors to integers, so I get this: <...skipped...>
- [dplyr join warning: joining factors with different levels](http://stackoverflow.com/questions/30468412/dplyr-join-warning-joining-factors-with-different-levels).
You can make sure that both factors have the same levels before merging
```
combined <- sort(union(levels(x$a), levels(y$a)))
n <- left_join(mutate(x, a=factor(a, levels=combined)),
    mutate(x, a=factor(a, levels=combined)))
# Joining by: "a"
class(n$a)
#[1] "factor"
```

## Visulization
- [Learn data-visualization](http://www.informationisbeautiful.net/about/). I’m David McCandless, a London-based author, writer and designer. I’ve written for The Guardian, Wired and others. I’m into anything strange and interesting. 
These days I’m an independent data journalist and information designer. A passion of mine is visualizing information – facts, data, ideas, subjects, issues, statistics, questions – all with the minimum of words.

## Steam
- [Как вернуть деньги за игры, купленные в Steam](http://kanobu.ru/articles/kak-vernut-dengi-za-igryi-kuplennyie-v-steam-369053/)

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
- [STAT 545: Computing by groups within data.frames with plyr](http://stat545.com/block013_plyr-ddply.html#introduction-to-ddply)
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
Showcase Mode!!!
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
- COOL. [ggrepel: Avoid overlapping of text labels](https://cran.r-project.org/web/packages/ggrepel/vignettes/ggrepel.html)
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
- [Sense.io](https://sense.io/). !! Sense is now part of Cloudera!! A Modern Platform for Data Science and Big Data Analytics.
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
