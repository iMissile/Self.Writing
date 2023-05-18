# network & graph
- COOL! [Benchmark of popular graph/network packages](https://www.timlrx.com/2019/05/05/benchmark-of-popular-graph-network-packages/)
```
The benchmark was carried out using a Google Compute n1-standard-16 instance (16vCPU Haswell 2.3GHz, 60 GB memory). I compare 5 different packages:
 - graph-tool
 - igraph
 - networkit
 - networkx
 - snap
```

# fonts
- Проблема со шрифтами. `In grid.Call(C_textBounds, as.graphicsAnnot(x$label),  ... :
  font family not found in Windows font database`
 - [Fonts not available in R after importing](https://stackoverflow.com/questions/56072340/fonts-not-available-in-r-after-importing)
 - [Changing fonts in ggplot2](https://stackoverflow.com/questions/34522732/changing-fonts-in-ggplot2/51906008#51906008).
 After intalling the package extraFont and running font_import like this (it took like 5 minutes):
```
library(extrafont)
font_import()
loadfonts(device = "win")
```
Another option is to use showtext package which supports more types of fonts (TrueType, OpenType, Type 1, web fonts, etc.) and more graphics devices, and avoids using external software such as Ghostscript.
```
# install.packages('showtext', dependencies = TRUE)
library(showtext)
```
- COOL! [yixuan/showtext](https://github.com/yixuan/showtext). Using Fonts More Easily in R Graphs
- [How can I resolve the "No Font Name" issue when importing fonts into R using extrafont?](https://stackoverflow.com/questions/61204259/how-can-i-resolve-the-no-font-name-issue-when-importing-fonts-into-r-using-ext)
As it was mentioned by @Moritz Schwarz, the problem is traced to `Rttf2pt1`.

According to a solution proposed here, downgrading it to 1.3.8 will fix the problem:
```
library(extrafont)
library(remotes)
remotes::install_version("Rttf2pt1", version = "1.3.8")
extrafont::font_import()
```
- Тут [Correctly finds font directory, but says "No FontName. Skipping" for all fonts](https://issueexplorer.com/issue/wch/extrafont/88) это же решение.
- [Custom fonts with ragg](http://www.r-graph-gallery.com/custom-fonts-in-R-and-ggplot2.html)
- [Changing fonts in ggplot2](https://stackoverflow.com/questions/34522732/changing-fonts-in-ggplot2)
- [Can't change fonts in ggplot/geom_text](https://stackoverflow.com/questions/14733732/cant-change-fonts-in-ggplot-geom-text)
You must import the system fonts using the command:
`font_import(paths = NULL, recursive = TRUE, prompt = TRUE, pattern = NULL)`. If you have a lot of fonts, this solution will take a long time. Use `pattern = "Times"` or something to reduce the number of fonts loaded

# ggplot
- COOL! Slides. [Designing ggplots. making clear figures that communicate](https://designing-ggplots.netlify.app/#1)
- Slides. [Creating Beautiful Data Visualizations in R: a ggplot2 Crash Course](https://sctyner.github.io/talks/Conferences/user2020/#1)
- Slides. [Plot a lot with ggplot2 to find plots](https://prital.netlify.app/talks/rladies2021/rladies-ggplot2#1)
- [ggplot2 aesthetic cheatsheet](https://tinyurl.com/y3y8wyap)
- [Use prismatic with after_scale() for finer control of colors in ggplot2](https://www.hvitfeldt.me/blog/use-prismatic-with-after_scale-for-finer-control-of-colors-in-ggplot2/)
- COOL! [ggplot tweaks](https://twitter.com/yutannihilat_en/status/1287402204987396096) or [doc](https://ggplot2.tidyverse.org/reference/scale_colour_continuous.html). Did you know the latest version of ggplot2 allows you to set the default colour/fill scale functions via global options? Since the version was a minor update, there was no release blog post, so you might not notice this big news...
- COOL! [The Evolution of a ggplot (Ep. 1)](https://cedricscherer.netlify.app/2019/05/17/the-evolution-of-a-ggplot-ep.-1/) Posted by Cédric on Friday, May 17, 2019
- [How I make the "Making of" videos](https://karaman.is/blog/2020/07/making-of/). I came across the idea when I saw Cédric’s gif in his tutorial The Evolution of a ggplot (Ep. 1).
- COOL! [ggfree: ggplot2-style plots with just base R graphics](https://github.com/ArtPoon/ggfree)
- [HOW TO BUILD A TUFTE-STYLE WEATHER GRAPH IN R USING GGPLOT2](https://johndjohnson.info/post/how-to-build-a-tufte-style-weather-graph-in-r-using-ggplot2/)
- COOL! [ggfittext](https://wilkox.org/ggfittext/). ggfittext provides a ggplot2 geom for fitting text into boxes.
- [New version of my ggplot2 theme reference sheet using mtcars!](https://twitter.com/_isabellamb/status/1269815940629184514?s=20)
[PDF/PNG](https://isabella-b.com/blog/ggplot2-theme-elements-reference/)
- [ggplot2 Theme Elements Demonstration](https://henrywang.nl/ggplot2-theme-elements-demonstration/)
- [Composing ggplot geoms](https://twitter.com/grant_mcdermott/status/1275134627871481856?s=20) A shortcut I like to use is calling multiple geoms in an lapply() call, since this automatically generates a list. Works well for investigating plotting variations, e.g.
```
ggplot(diamonds, aes(carat)) +
  lapply(c(50,200), function(b) geom_histogram(bins=b, alpha=0.3))
```
- COOL! [giocomai/ganttrify](https://github.com/giocomai/ganttrify). Create beautiful Gantt charts with ggplot2 https://apps.europeandatajournalism.e…
- `ggplot::geom_curve`. Красиво делают стрелочки для надписей на графике. [eRum 2020. Tips from an R Journalist](http://www.machlis.com/eRum2020/#17)

- COOL! [{mdthemes} is on CRAN: markdown powered themes for {ggplot2}](https://thomasadventure.blog/posts/mdthemes-is-on-cran-markdown-powered-themes-for-ggplot2/)
- [Allow hms object in breaks argument to scale_*_date {closed}](https://github.com/tidyverse/ggplot2/issues/2894)
- [ggplot2 3.3.0](https://www.tidyverse.org/blog/2020/03/ggplot2-3-3-0/). Bi-directional geoms and stats!!!
- COOL! [A Summer of RStudio and ggplot2](https://education.rstudio.com/blog/2019/10/a-summer-of-rstudio-and-ggplot2/) by Dewey Dunnington
- [A List of ggplot2 extensions](https://exts.ggplot2.tidyverse.org/)
This site tracks and lists ggplot2 extensions developed by R users in the community.
The aim is to make it easy for R users to find developed extensions.
- [erocoar/gghalves](https://github.com/erocoar/gghalves). Easy half-half geoms in ggplot2 https://erocoar.github.io/gghalves/
- [ggtext: Improved text rendering support for ggplot2](https://wilkelab.org/ggtext/)
This package provides rich-text (basic HTML and Markdown) support for ggplot2. Rich text can be used in plot annotations (plot titles, subtitles, captions, axis labels, legends, etc.) and to visualize textual data, as one would normally do with geom_text().
- [The ggplot2 extension gallery now lives at https://exts.ggplot2.tidyverse.org](https://exts.ggplot2.tidyverse.org). Please update your bookmarks. The old link is no longer safe to visit.
- [How to Make Animated Histograms in R, with ggplot and gganimate](https://flowingdata.com/2020/05/13/animated-histograms-ggplot-gganimate/)
- Thomas Lin Pedersen ggplot2 workshop.
	- [ggplot2 workshop part 1](https://www.youtube.com/watch?v=h29g21z0a68&feature=youtu.be).
	- [ggplot2 workshop part 2](https://www.youtube.com/watch?v=0m4yywqNPVY&feature=youtu.be)
- COOL! [thematic](https://rstudio.github.io/thematic/). Unified and automatic theming of ggplot2, lattice, and base R graphics.
- COOL! [Vertical intervals: lines, crossbars & errorbars](https://ggplot2.tidyverse.org/reference/geom_linerange.html)
- [Easy ggplot2 Theme customization with {ggeasy}](https://www.programmingwithr.com/easy-ggplot2-theme-customization-with-ggeasy/)
- Повтор. [blogR on Svbtle](https://drsimonj.svbtle.com/)
	- [Label line ends in time series with ggplot2](https://drsimonj.svbtle.com/label-line-ends-in-time-series-with-ggplot2)
	- COOL! [Visualising Residuals](https://drsimonj.svbtle.com/visualising-residuals)
- Делаем вторую ось для дискрета
	- [Duplicating (and modifying) discrete axis in ggplot2](https://stackoverflow.com/questions/48964760/duplicating-discrete-x-axis-for-ggplot)
	- [Duplicating discrete x-axis for ggplot {duplicate}](https://stackoverflow.com/questions/45361904/duplicating-and-modifying-discrete-axis-in-ggplot2)
- Отображение функций в ggplot
	- [Compute function for each x value](https://ggplot2.tidyverse.org/reference/stat_function.html)
	- [Draw function without data in ggplot2](https://kohske.wordpress.com/2010/12/25/draw-function-without-data-in-ggplot2/)
- COOL! [ggrough is an R package that converts your ggplot2 plots to rough/sketchy charts, using the excellent javascript roughjs library.](https://xvrdm.github.io/ggrough/)
- [yixuan/showtext](https://github.com/yixuan/showtext). Using Fonts More Easily in R Graphs
- COOL! [Data exploration with alluvial plots - An introduction to easyalluvial](https://www.datisticsblog.com/2018/10/intro_easyalluvial/)
- COOL! [Visualising Model Response with easyalluvial](https://www.datisticsblog.com/2019/04/visualising-model-response-with-easyalluvial/)
- COOL! [erblast/easyalluvial](https://github.com/erblast/easyalluvial) create alluvial plots with a single line of code
- [parcats](https://erblast.github.io/parcats/index.html).
Create ‘plotly.js’ Parallel Categories Diagrams Using this Htmlwidget and ‘easyalluvial’
Complex graphical representations of data are best explored using interactive elements. ‘parcats’ adds interactive graphing capabilities to the ‘easyalluvial’ package. The ‘plotly.js’ parallel categories diagrams offer a good framework for creating interactive flow graphs that allow manual drag and drop sorting of dimensions and categories, highlighting single flows and displaying mouse over information. The ‘plotly.js’ dependency is quite heavy and therefore is outsourced into a separate package.
- [easyalluvial: Generate Alluvial Plots with a Single Line of Code](https://cran.r-project.org/web/packages/easyalluvial/index.html)
Alluvial plots are similar to sankey diagrams and visualise categorical data over multiple dimensions as flows. (Rosvall M, Bergstrom CT (2010) Mapping Change in Large Networks. PLoS ONE 5(1): e8694.  Their graphical grammar however is a bit more complex then that of a regular x/y plots. The 'ggalluvial' package made a great job of translating that grammar into 'ggplot2' syntax and gives you many options to tweak the appearance of an alluvial plot, however there still remains a multi-layered complexity that makes it difficult to use 'ggalluvial' for explorative data analysis. 'easyalluvial' provides a simple interface to this package that allows you to produce a decent alluvial plot from any dataframe in either long or wide format from a single line of code while also handling continuous data. It is meant to allow a quick visualisation of entire dataframes with a focus on different colouring options that can make alluvial plots a great tool for data exploration.
- [The Hitchhiker's Guide to Ggplot2 + The Hitchhiker's Guide to Plotnine](https://pacha.hk/blog/2019/12/21/the-hitchhikers-guide-to-ggplot2---the-hitchhikers-guide-to-plotnine/)
- COOL! [R Tips: How to force the Y Axis breaks in ggplot2 to be integers from Stack Overflow: How to display only integer values on an axis using ggplot2](http://rolandtanglao.com/2018/04/30/p1-how-to-force-y-axis-breaks-to-be-integers-in-ggplot2/)
- COOL! Learning [malcolmbarrett/designing.ggplots](https://github.com/malcolmbarrett/designing.ggplots). Install Workshop Materials for Designing ggplots
- [clauswilke/ggtextures](https://github.com/clauswilke/ggtextures). Drawing textured rectangles and bars with ggplot
- [Align axis label on the right with ggplot2](https://stackoverflow.com/questions/37488075/align-axis-label-on-the-right-with-ggplot2)
- [Construct labelling specification](https://ggplot2.tidyverse.org/reference/labeller.html)
- COOL! [JohnCoene/grapher](https://github.com/JohnCoene/grapher). ✍️ Interactive graphs https://grapher.network
- COOL! [How to change facet labels?](https://stackoverflow.com/questions/3472980/how-to-change-facet-labels)
- COOL! [ggparty](https://github.com/martin-borkovec/ggparty) ggplot2 visualizations for the partykit package.
- [ggparty: Graphic Partying](https://cran.r-project.org/web/packages/ggparty/vignettes/ggparty-graphic-partying.html) ggparty aims to extend ggplot2 functionality to the partykit package. It provides the necessary tools to create clearly structured and highly customizable visualizations for tree-objects of the class 'party'.
- Learning. [HOW TO SAVE A GGPLOT](https://www.datanovia.com/en/blog/how-to-save-a-ggplot/)
- [Making a background color gradient in ggplot2](https://aosmith.rbind.io/2019/10/14/background-color_gradient/)
- Learning. Интересные примеры. [Data Visualization with ggplot2 (Part 1) - Chapter 4 and 5](https://rpubs.com/williamsurles/294957)
- Условное форматирование меток в ggplot. [How to put ggplot2 ticks labels between dollars?](http://stackoverflow.com/questions/20326946/how-to-put-ggplot2-ticks-labels-between-dollars)
- [gghalves](https://cran.r-project.org/web/packages/gghalves/readme/README.html) makes it easy to compose your own half-half plots via ggplot2. Think displaying a boxplot next to jittered points, or violin plots side by side with dotplots.
- COOL! [Streamgraphs in ggplot2 with ggstream](https://r-charts.com/evolution/ggstream/)
- Проблемы с ggstream. [Error in data.frame(x = full_values$x, y = yy[, iStream * 2], group = as.integer(.group)) : #18 {Open}](https://github.com/davidsjoberg/ggstream/issues/18).
Ошибка случается здесь: https://github.com/davidsjoberg/ggstream/blob/cfed4bc3d17879b061198f4594397706b6db50f6/R/min_wiggle.R#L120
`out <- data.frame(x = full_values$x`, выяснил через `debugonce(ggstream:::new_wiggle)`
- COOL! [ggpage](https://emilhvitfeldt.github.io/ggpage/). ggpage is a package to create pagestyled visualizations of text based data. It uses ggplot2 and final returns are ggplot2 objects
- COOL! [wilkelab/ungeviz](https://github.com/wilkelab/ungeviz). Tools for visualizing uncertainty with ggplot2
- COOL! [Practical ggplot2](https://wilkelab.org/practicalgg/)
- ggplot
	- [log-scale Breaks Are Not Always Useful #100 {Closed}](https://github.com/r-lib/scales/issues/100)
	- [No legend with trans = log10 for certain fill/color values #2295 {Closed}]
- COOL! [Using ggplot2 for functional time series](https://robjhyndman.com/hyndsight/ftsviz/)
- [An updated version of The Hitchhiker's Guide to Ggplot2](https://pacha.hk/blog/2019/09/08/an-updated-version-of-the-hitchhikers-guide-to-ggplot2/)
	- [The Hitchhiker's Guide to Ggplot2](https://leanpub.com/hitchhikers_ggplot2)
- COOL! [Calendar Heatmaps in ggplot](https://ryanplant.netlify.com/post/calendar-heatmaps-in-ggplot/)
- [ggplot2. the R Graph Gallery](http://r-graph-gallery.com/ggplot2-package.html)
- решаем проблемы со шрифтами в R в windows
	- [Error in grid.Call(L_textBounds, as.graphicsAnnot(x$label), x$x, x$y, : Polygon edge not found](https://stackoverflow.com/questions/10581440/error-in-grid-calll-textbounds-as-graphicsannotxlabel-xx-xy-polygon)
	- [Ggplot2: Fonts and cross-platform reproducibility](https://community.rstudio.com/t/ggplot2-fonts-and-cross-platform-reproducibility/3565)
```
library(extrafont)
#font_import() only do this one time - it takes a while
loadfonts(dev="win")
windowsFonts()
```
- [Force R to stop plotting abbreviated axis labels - e.g. 1e+00 in ggplot2](https://stackoverflow.com/questions/14563989/force-r-to-stop-plotting-abbreviated-axis-labels-e-g-1e00-in-ggplot2). Интересное возможное решение
```
 # Did you try something like :
options(scipen=10000)
 # before plotting ?
```
- [Forcing a 1e3 instead of 1000 format in ggplot R](https://stackoverflow.com/questions/18600115/forcing-a-1e3-instead-of-1000-format-in-ggplot-r/18600721#18600721)
`scales::math_format`
- [Axes (ggplot2)](http://www.cookbook-r.com/Graphs/Axes_(ggplot2)/)
- [ggplot2 Tutor](https://rpubs.com/KamleshJha/ggplot)
- [How to keep ggplot font size constant when varying figure width](https://tex.stackexchange.com/questions/145745/how-to-keep-ggplot-font-size-constant-when-varying-figure-width)
- COOL! [How to plot fitted lines with ggplot2](https://aosmith.rbind.io/2018/11/16/plot-fitted-lines/)
- [Adding a regression line on a ggplot](https://stackoverflow.com/questions/15633714/adding-a-regression-line-on-a-ggplot)
- [How to plot fitted lines with ggplot2](https://aosmith.rbind.io/2018/11/16/plot-fitted-lines/)
- COOL! [hrbrmstr/ggalt](https://github.com/hrbrmstr/ggalt). 🌎 Extra Coordinate Systems, Geoms, Statistical Transformations & Scales for 'ggplot2' https://cran.r-project.org/web/packag…
	- Dev версия сильно опережает CRAN. [ggalt](https://yonicd.github.io/ggalt/index.html)
A compendium of ‘geoms’, ‘coords’, ‘stats’, scales and fonts for ‘ggplot2’, including splines, 1d and 2d densities, univariate average shifted histograms, a new map coordinate system based on the ‘PROJ.4’-library and the ‘StateFace’ open source font ‘ProPublica’.
- [Transforming the breaks to match a scale](http://freerangestats.info/blog/2015/09/07/transforming-breaks-in-a-scale)
- [Increase number of axis ticks](https://stackoverflow.com/questions/11335836/increase-number-of-axis-ticks)
- [ggplot2 change axis limits for each individual facet panel](https://stackoverflow.com/questions/51735481/ggplot2-change-axis-limits-for-each-individual-facet-panel). This is a long-standing feature request (see, e.g., 2009, 2011, 2016) which is tackled by a separate package `facetscales`.
	- [facetscales](https://github.com/zeehio/facetscales)
The goal of facetscales is to let you use facet_grid with different scales per plot. This is useful for instance to display in different facets magnitudes with different units.
- [ggrepel examples](https://cran.r-project.org/web/packages/ggrepel/vignettes/ggrepel.html) by Kamil Slowikowski, 2019-05-06
- [Remove 'a' from legend when using aesthetics and geom_text](https://stackoverflow.com/questions/18337653/remove-a-from-legend-when-using-aesthetics-and-geom-text)
- [How do I remove the 'a' in legends when I use geom_label_repel?](https://community.rstudio.com/t/how-do-i-remove-the-a-in-legends-when-i-use-geom-label-repel/68895)
- [Add row in each group using dplyr and add_row()](https://stackoverflow.com/questions/43403282/add-row-in-each-group-using-dplyr-and-add-row)
- `geom-smooth`: [Understanding the confidence band from a polynomial regression](https://stats.stackexchange.com/questions/82603/understanding-the-confidence-band-from-a-polynomial-regression)
- [Center bars of histogram using ggplot2](https://stackoverflow.com/questions/34180300/center-bars-of-histogram-using-ggplot2)
- [ggplot: Calculated aesthetics](https://ggplot2.tidyverse.org/reference/stat.html)
- [R ggplot2: stat_count() must not be used with a y aesthetic error in Bar graph](https://stackoverflow.com/questions/39679057/r-ggplot2-stat-count-must-not-be-used-with-a-y-aesthetic-error-in-bar-graph)
- [Data Binning and Plotting](http://www.jdatalab.com/data_science_and_data_mining/2017/01/30/data-binning-plot.html)
- [thomasp85/patchwork](https://github.com/thomasp85/patchwork). The Composer of ggplots
- [Easy multi-panel plots in R using facet_wrap() and facet_grid() from ggplot2](http://www.zevross.com/blog/2019/04/02/easy-multi-panel-plots-in-r-using-facet_wrap-and-facet_grid-from-ggplot2/). One of the most powerful aspects of the R plotting package ggplot2 is the ease with which you can create multi-panel plots. With a single function you can split a single plot into many related plots using `facet_wrap()` or `facet_grid()`.
- COOL! [UNDERSTANDING GGPLOT: AN EXAMPLE](http://jdobr.es/blog/data-vis-with-ggplot/)
- COOL! [How to Set ggplot Facets Coords Individually](http://www.zachburchill.ml/ggplot_facets/)
- [Be Awesome in ggplot2: A Practical Guide to be Highly Effective - R software and data visualization](http://www.sthda.com/english/wiki/be-awesome-in-ggplot2-a-practical-guide-to-be-highly-effective-r-software-and-data-visualization)
- [12 Extensions to ggplot2 for More Powerful R Visualizations](https://mode.com/blog/r-ggplot-extension-packages)
- [Introduction to ggridges](https://cran.r-project.org/web/packages/ggridges/vignettes/introduction.html)
- [Setting individual axis limits with facet_wrap and scales = “free” in ggplot2](https://stackoverflow.com/questions/18046051/setting-individual-axis-limits-with-facet-wrap-and-scales-free-in-ggplot2)
- [facetscales](https://github.com/zeehio/facetscales)
The goal of facetscales is to let you use facet_grid with different scales per plot. This is useful for instance to display in different facets magnitudes with different units.
- [You Can Design a Good Chart with R. But do R users invest in design?](https://medium.com/data-visualization-society/you-can-design-a-good-chart-with-r-5d00ed7dd18e)
- COOL! [https://drsimonj.svbtle.com/ordering-categories-within-ggplot2-facets](https://drsimonj.svbtle.com/ordering-categories-within-ggplot2-facets)
- [logspline: Routines for Logspline Density Estimation](https://cran.rstudio.org/web/packages/logspline/index.html)
Contains routines for logspline density estimation. The function oldlogspline() uses the same algorithm as the logspline package version 1.0.x; i.e. the Kooperberg and Stone (1992) algorithm (with an improved interface). The recommended routine logspline() uses an algorithm from Stone et al (1997).
- [gglogspline](https://git.rud.is/hrbrmstr/gglogspline)
A ‘ggplot2’ Extension for Visualizing Density, Distribution, Hazard, or Survival Functions using the ‘logspline’ Package
- [Quick hit: Some ggplot2 Stat for {logspline}](https://rud.is/b/2019/06/18/quick-hit-some-ggplot2-stat/)
- [hrbrmstr/ggalt](https://github.com/hrbrmstr/ggalt/)
Extra Coordinate Systems, Geoms, Statistical Transformations & Scales for 'ggplot2'
- [ggthemes](https://jrnold.github.io/ggthemes/)
- [ggthemes. ALL YOUR FIGURE ARE BELONG TO US](https://yutannihilation.github.io/allYourFigureAreBelongToUs/ggthemes/)
- [ggplot2: place text at right location](https://www.gl-li.com/2017/08/18/place-text-at-right-location/)
- [Label line ends in time series with ggplot2](https://drsimonj.svbtle.com/label-line-ends-in-time-series-with-ggplot2)
- COOL! [REORDERING AND FACETTING FOR GGPLOT2](https://juliasilge.com/blog/reorder-within/).
	- [David Robinson's Personal R Package](https://github.com/dgrtwo/drlib)
	- [`reorder_within`](https://github.com/dgrtwo/drlib/blob/master/R/reorder_within.R)
	- [Ordering Categories within ggplot2 Facets](https://trinkerrstuff.wordpress.com/2016/12/23/ordering-categories-within-ggplot2-facets/)
- [How do I access the data frame that has been passed to ggplot()?](https://stackoverflow.com/questions/45088454/how-do-i-access-the-data-frame-that-has-been-passed-to-ggplot)
- [How to Turn Your ggplot2 Visualization into an Interactive Tweet](https://datatitian.com/how-to-turn-your-ggplot2-visualization-into-an-interactive-tweet/)
- [cowplot – Streamlined plot theme and plot annotations for ggplot2](https://github.com/wilkelab/cowplot)
- [Changing Glyph in legend in ggplot2](https://www.hvitfeldt.me/blog/changing-glyph-in-ggplot2/)
- [Add legend for stroke points ggplot2](https://stackoverflow.com/questions/58290389/add-legend-for-stroke-points-ggplot2)
- [Changing shapes used for scale_shape() in ggplot2](https://stackoverflow.com/questions/1478532/changing-shapes-used-for-scale-shape-in-ggplot2)
- COOL! [lemon: Freshing Up your 'ggplot2' Plots](https://cran.rstudio.com/web/packages/lemon/)
Functions for working with legends and axis lines of 'ggplot2', facets that repeat axis lines on all panels, and some 'knitr' extensions.
- [ggdendro: Create Dendrograms and Tree Diagrams Using 'ggplot2'](https://cran.r-project.org/web/packages/ggdendro/index.html)
This is a set of tools for dendrograms and tree plots using 'ggplot2'. The 'ggplot2' philosophy is to clearly separate data from the presentation. Unfortunately the plot method for dendrograms plots directly to a plot device without exposing the data. The 'ggdendro' package resolves this by making available functions that extract the dendrogram plot data. The package provides implementations for tree, rpart, as well as diana and agnes cluster diagrams.
- [Ariel Muldoon blog](https://aosmith.rbind.io/). Там много чего есть про использование ggplot.
	- COOL [The small multiples plot: how to combine ggplot2 plots with one shared axis](https://aosmith.rbind.io/2019/05/13/small-multiples-plot/)
	- [Embedding subplots in ggplot2 graphics](https://aosmith.rbind.io/2019/04/22/embedding-subplots/)
- [How can I view the computed varialbles computed by ggplot2 geom_boxplot?](https://stackoverflow.com/questions/39820118/how-can-i-view-the-computed-varialbles-computed-by-ggplot2-geom-boxplot)
- COOL! Как достать информацию из построенного графика ggplot? `ggplot_build(gp)$data -> m`, там вся структура по слоям.
	- [Get Quantile values from geom_boxplot()](https://stackoverflow.com/questions/34977882/get-quantile-values-from-geom-boxplot)
	- [Extracting details](https://campus.datacamp.com/courses/data-visualization-with-ggplot2-part-3/ggplot2-internals?ex=13)
- [How to add number of observations to a ggplot2 boxplot](https://medium.com/@gscheithauer/how-to-add-number-of-observations-to-a-ggplot2-boxplot-b22710f7ef80)
- [How do I turn the numeric output of boxplot (with plot=FALSE) into something usable?](https://stackoverflow.com/questions/8844845/how-do-i-turn-the-numeric-output-of-boxplot-with-plot-false-into-something-usa)
- COOL [Aligning labels with ggrepel](https://stackoverflow.com/questions/47492191/aligning-labels-with-ggrepel)
- COOL! [Label line ends in time series with ggplot2](https://drsimonj.svbtle.com/label-line-ends-in-time-series-with-ggplot2). @drsimonj here with a quick share on making great use of the secondary y axis with ggplot2 – super helpful if you’re plotting groups of time series!
- [Floating bar chart with trend line on secondary axis](https://stackoverflow.com/questions/45981366/floating-bar-chart-with-trend-line-on-secondary-axis)
- [Label on the side of box plot in R - ggplot](https://stackoverflow.com/questions/50372943/label-on-the-side-of-box-plot-in-r-ggplot)
- [The Complete ggplot2 Tutorial - Part1 | Introduction To ggplot2 (Full R code)](http://r-statistics.co/Complete-Ggplot2-Tutorial-Part1-With-R-Code.html)
- [Creating plots in R using ggplot2 - part 10: boxplots](http://t-redactyl.io/blog/2016/04/creating-plots-in-r-using-ggplot2-part-10-boxplots.html)
- COOL! [raivokolde/pheatmap](https://github.com/raivokolde/pheatmap). Pretty heatmaps
- [GGPLOT LEGEND TITLE, POSITION AND LABELS](https://www.datanovia.com/en/blog/ggplot-legend-title-position-and-labels/)
- COOL! [ggforce](https://ggforce.data-imaginist.com/index.html) is a package aimed at providing missing functionality to ggplot2 through the extension system introduced with ggplot2 v2.0.0. Broadly speaking ggplot2 has been aimed primarily at explorative data visualization in order to investigate the data at hand, and less at providing utilities for composing custom plots a la D3.js. ggforce is mainly an attempt to address these “shortcoming” (design choices might be a better description). The goal is to provide a repository of geoms, stats, etc. that are as well documented and implemented as the official ones found in ggplot2.
	- [The ggforce Awakens (again)](https://www.data-imaginist.com/2019/the-ggforce-awakens-again/) Mar 7, 2019
	- Очень хороший [пример аннотирования](https://gist.github.com/Ryo-N7/67ca1c364c342a82c4098918082ca445), взял из [твита](https://twitter.com/R_by_Ryo/status/1129773418184925184?s=20)
- COOL! [The Evolution of a ggplot (Ep. 1)](https://cedricscherer.netlify.com/2019/05/17/the-evolution-of-a-ggplot-ep.-1/). Posted by Cédric on Friday, May 17, 2019
- [10 Steps to Better Graphs in R](https://michaeltoth.me/10-steps-to-better-graphs-in-r.html)
- [A Detailed Guide to ggplot colors](https://michaeltoth.me/a-detailed-guide-to-ggplot-colors.html)
- [ZOOMING IN ON MAPS WITH SF AND GGPLOT2](https://datascience.blog.wzb.eu/2019/04/30/zooming-in-on-maps-with-sf-and-ggplot2/)
- [Detailed Guide to the Bar Chart in R with ggplot](https://michaeltoth.me/detailed-guide-to-the-bar-chart-in-r-with-ggplot.html)
- [A Detailed Guide to the ggplot Scatter Plot in R](https://michaeltoth.me/a-detailed-guide-to-the-ggplot-scatter-plot-in-r.html)
- COOL! [Adding Custom Fonts to ggplot in R](http://gradientdescending.com/adding-custom-fonts-to-ggplot-in-r/)
- Можно ли посадить Shiny приложение на локальные шрифты?
	- [RC font not rendering in shiny #19 {Open}](https://github.com/hrbrmstr/hrbrthemes/issues/19)
	- COOL! [Webfonts in ggplot2](https://jackolney.github.io/blog/post/2016-08-15-ggplot2-font/), AUGUST 15, 2016. R GGPLOT2 TRUETYPE WEBFONTS SHOWTEXT]
	- COOL! [google-webfonts-helper](https://google-webfonts-helper.herokuapp.com/fonts). A Hassle-Free Way to Self-Host Google Fonts
- BBC Visual ggplot
	- COOL! [BBC Visual and Data Journalism cookbook for R graphics](https://bbc.github.io/rcookbook/)
	- [How the BBC Visual and Data Journalism team works with graphics in R](https://medium.com/bbc-visual-and-data-journalism/how-the-bbc-visual-and-data-journalism-team-works-with-graphics-in-r-ed0b35693535)
	- [bbc/bbplot](https://github.com/bbc/bbplot). R package that helps create and export ggplot2 charts in the style used by the BBC News data team
- [ggplot2. A quantile-quantile plot](https://ggplot2.tidyverse.org/reference/geom_qq.html)
- [R Coding Style Guide](https://irudnyts.github.io//r-coding-style-guide/) by Iegor Rudnytskyi, PhD student in Actuarial Science at HEC Lausanne
- [charlatan: Make Fake Data](https://cran.r-project.org/web/packages/charlatan/)
Make fake data, supporting addresses, person names, dates, times, colors, coordinates, currencies, digital object identifiers ('DOIs'), jobs, phone numbers, 'DNA' sequences, doubles and integers from distributions and within a range.
- [ggeffects 0.8.0 now on CRAN: marginal effects for regression models](https://strengejacke.wordpress.com/2019/01/14/ggeffects-0-8-0-now-on-cran-marginal-effects-for-regression-models-rstats/)
- [ggdist: Visualizations of distributions and uncertainty](https://mjskay.github.io/ggdist/)
- [Changing the look of your ggplot2 objects](https://www.meganstodel.com/posts/ggplot2-hawks-2/)
- COOL! [Multi-level labels with ggplot2](https://dmitrijskass.netlify.app/2019/06/30/multi-level-labels-with-ggplot2/)
- [Quick example using guide_axis() with corrr()](https://github.com/brshallo/guide_axis-example)
- [ggnewscale](https://eliocamp.github.io/ggnewscale/)
- [a ggplot2 grammar guide](https://evamaerey.github.io/ggplot2_grammar_guide/a	bout) by Gina Reynolds
- COOL! [tidyexplain. Tidy Animated Verbs](https://www.garrickadenbuie.com/project/tidyexplain/)
- [ggdist](https://mjskay.github.io/ggdist/) Visualizations of Distributions and Uncertainty
- COOL! [A bar chart 5 ways in ggplot2](https://themockup.blog/posts/2020-08-05-a-bar-chart-5-ways/)
- [ggplot2 3.3.0](https://www.tidyverse.org/blog/2020/03/ggplot2-3-3-0/)
- COOL! Попытка нарисовать контуры в полярных координатах привела к массе вопросов. Частичные ответы про интерполяцию по сетке: [Contour levels corresponding to variable levels in ggplot2](https://stackoverrun.com/ru/q/9812655)
```
   # теперь готовим матрицу для градиентной заливки
   # берем идеи отсюда: http://stackoverflow.com/questions/24410292/how-to-improve-interp-with-akima
   # и отсюда: http://www.kevjohnson.org/making-maps-in-r-part-2/
```
- [Remove 'a' from legend when using aesthetics and geom_text](https://stackoverflow.com/questions/18337653/remove-a-from-legend-when-using-aesthetics-and-geom-text)
- [Dynamically use range of pretty breaks to set limits in ggplot](https://stackoverflow.com/questions/53753970/dynamically-use-range-of-pretty-breaks-to-set-limits-in-ggplot)
- [ggplotly geoms](https://beta.rstudioconnect.com/jjallaire/htmlwidgets-ggplotly-geoms/htmlwidgets-ggplotly-geoms.html)
- COOL! [ggplot2: Mastering the basics](http://www.rebeccabarter.com/blog/2017-11-17-ggplot2_tutorial/)
- [ggridges: Ridgeline Plots in 'ggplot2'](https://cran.r-project.org/web/packages/ggridges/index.html)
Ridgeline plots provide a convenient way of visualizing changes in distributions over time or space. This package enables the creation of such plots in 'ggplot2'.
- [ggformula: Formula Interface to the Grammar of Graphics](https://cran.r-project.org/web/packages/ggformula/). Provides a formula interface to 'ggplot2' graphics.
- [ggformula](http://www.mosaic-web.org/ggformula/index.html). ggformula introduces a family of graphics functions, `gf_point()`, `gf_density()`, and so on, bring the formula interface to `ggplot()`.
- Интересно. [Formula Interface for ggplot2](https://cran.r-project.org/web/packages/ggformula/vignettes/ggformula.html)
- [The Problem – Binning for Length Frequency Histograms](http://derekogle.com/fishR/2016-03-10-Histograms-with-w)
- [jitter geom_line()](https://stackoverflow.com/questions/10866047/jitter-geom-line). `geom_line(position = position_jitter(w = 0.02, h = 0))` or
If you just want to prevent two lines from overlapping exactly, there is now a better way: `position_dodge()`, which "adjusts position by dodging overlaps to the side". This is nicer than adding jitter to any line, even when it's not needed.
- [Jitter lines in ggplot - code works without "position =" argument](https://community.rstudio.com/t/jitter-lines-in-ggplot-code-works-without-position-argument/56049)
- COOL! [How to Add Labels Directly in ggplot2? Hint: Use Secondary Axis Trick](https://datavizpyr.com/direct-labeling-with-secondary-axis-trick-ggplot2-r/)
- [ggside: Plot Linear Regression using Marginal Distributions (ggplot2 extension)](https://www.business-science.io/code-tools/2021/05/18/marginal_distributions.html)
- Боремся с легендами. 
	- COOL! [Controlling legend appearance in ggplot2 with override.aes](https://aosmith.rbind.io/2020/07/09/ggplot2-override-aes/)
	- [Remove extra legends in ggplot2](https://stackoverflow.com/questions/11714951/remove-extra-legends-in-ggplot2). `geom_point(aes(colour=group, alpha = .8), show.legend = F)`
	- [How to specify legend width in ggplot](https://community.rstudio.com/t/how-to-specify-legend-width-in-ggplot/23060). `theme(legend.key.width = unit(4, "cm"))`
- COOL! [The Evolution of a ggplot (Ep. 1)](https://www.cedricscherer.com/2019/05/17/the-evolution-of-a-ggplot-ep.-1/#polish) Posted by Cédric on Friday, May 17, 2019 
- [Aesthetic specifications](https://ggplot2.tidyverse.org/articles/ggplot2-specs.html). Здесь также про то, как работать с кастомными шрифтами.
- [Cookbook for R GraphsFonts](http://www.cookbook-r.com/Graphs/Fonts/)
- [12 Extensions to ggplot2 for More Powerful R Visualizations](https://mode.com/blog/r-ggplot-extension-packages/)
- [10 Tips to Customize Text Color, Font, Size in ggplot2 with `element_text()`](https://cmdlinetips.com/2021/05/tips-to-customize-text-color-font-size-in-ggplot2-with-element_text/)
- [15 Tips to Customize lines in ggplot2 with element_line()](https://cmdlinetips.com/2021/05/tips-to-customize-lines-in-ggplot2-with-element_line/)
- [8 tips to use element_blank() in ggplot2 theme](https://cmdlinetips.com/2021/06/ggplot2-theme-element_blank-tips/)
- COOL! Как эффективно применить `ggfx` [Better data communication with {ggplot2}, part 2](https://giulia-ruggeri.medium.com/better-data-communication-with-ggplot2-part-2-615a5180ccb)
- COOL! [Plotting background data for groups with ggplot2](https://drsimonj.svbtle.com/plotting-background-data-for-groups-with-ggplot2)
- [ggsunburst](https://github.com/didacs/ggsunburst). ggsunburst offers a set of tools to plot adjacency diagrams using ggplot2.
- [grafify](https://grafify-vignettes.netlify.app/) An R package for easy graphs, ANOVAs and post-hoc comparisons
- [Streetmaps](https://ggplot2tutor.com/tutorials/streetmaps). Create a streetmap of your favorite city with ggplot2 and powerpoint
- [Off-label uses in ggplot2](https://www.tidyverse.org/blog/2021/06/off-label-uses-in-ggplot2/)
- [Point labels perpendicular to a curve in ggplot2](https://wjschne.github.io/posts/point-labels-perpendicular-to-a-curve-in-ggplot2/) by W. Joel Schneider
- [Scatterplot with automatic text repel](http://www.r-graph-gallery.com/web-scatterplot-and-ggrepel.html)
- [The ggh4x package is a ggplot2 extension package](https://teunbrand.github.io/ggh4x/index.html). It provides some utility functions that don’t entirely fit within the ‘grammar of graphics’ concept —they can be a bit hacky— but can nonetheless be useful in tweaking your ggplots. 
- [ggfittext](https://wilkox.org/ggfittext/index.html) provides some ggplot2 geoms for fitting text into boxes.
- Slides. [Best practices for programming with ggplot2](https://fishandwhistle.net/slides/rstudioconf2020/#1)
- COOL! [Reorder legend to match order of plot elements in ggplot2](https://www.nsgrantham.com/reorder-legend-ggplot2)
- [`patchwork::inset_element`](https://patchwork.data-imaginist.com/reference/inset_element.html) Create an inset to be added on top of the previous plot
- [davidsjoberg/ggbump](https://github.com/davidsjoberg/ggbump). A geom for ggplot to create bump plots
- COOL! [Combining inset plots with facets using ggplot](https://clarewest.github.io/blog/post/2019-08-27-combining-inset-plots-with-facets-using-ggplot/)
- [Remove all of x axis labels in ggplot](https://stackoverflow.com/questions/35090883/remove-all-of-x-axis-labels-in-ggplot)
- [ggplot2 - The unit of size](https://stackoverflow.com/questions/17311917/ggplot2-the-unit-of-size)
- [ggplot geom_text font size control](https://stackoverflow.com/questions/25061822/ggplot-geom-text-font-size-control)
- [scale_x_discrete with numeric drops axis with no warning #2970 {Closed}](https://github.com/tidyverse/ggplot2/issues/2970)
- [ggplot with 2 y axes on each side and different scales](https://stackoverflow.com/questions/3099219/ggplot-with-2-y-axes-on-each-side-and-different-scales)
- [Reordering and facetting for ggplot2](https://juliasilge.com/blog/reorder-within/)
- COOL! [Setting the Graphics Device in a RMarkdown Document](https://www.jumpingrivers.com/blog/r-knitr-markdown-png-pdf-graphics/). The {ragg} Package
Setting the agg_png() function from the {ragg} package as the graphics device is somewhat more tricky as it doesn’t come pre-defined within {knitr}. The {knitr} docs states that
- [Circular barplot with R and ggplot2](https://www.r-graph-gallery.com/web-circular-barplot-with-R-and-ggplot2.html)
- COOL! [3 alternatives to a discrete color scale legend in ggplot2](https://www.nsgrantham.com/legend-alternatives-ggplot2)
- [Using ggplot2, can I insert a break in the axis?](https://stackoverflow.com/questions/7194688/using-ggplot2-can-i-insert-a-break-in-the-axis)
- [How do I access the data frame that has been passed to ggplot()?](https://stackoverflow.com/questions/45088454/how-do-i-access-the-data-frame-that-has-been-passed-to-ggplot)
- Slides [Cracking open the internals of ggplot. A {ggtrace} showcase](https://yjunechoe.github.io/ggtrace-talk/#1)
- Slides also. [Beyond Bar and Box Plots. Hands–on code to create and style chart alternatives with ggplot2](https://z3tt.github.io/beyond-bar-and-box-plots/)
- [I’ve Stopped Using Box Plots. Should You?](https://nightingaledvs.com/ive-stopped-using-box-plots-should-you/)
- COOL! [Recreating the New York Times COVID-19 Spiral Graph](https://bydata.github.io/nyt-corona-spiral-chart/)
- [ggplot: How to increase spacing between faceted plots?](https://stackoverflow.com/questions/3681647/ggplot-how-to-increase-spacing-between-faceted-plots)
- Error in (function (filename = "Rplot%03d.png", width = 480, height = 480, : unable to start png() device.
	- [Unable to initiate png device Rnotebook(https://community.rstudio.com/t/unable-to-initiate-png-device-rntebook/3658)
	- [Error : Unable to start png() device](https://stackoverflow.com/questions/45113597/error-unable-to-start-png-device?)
	- [Rstudio Global Changes: show chunk output in console via CLI?](https://stackoverflow.com/questions/48110571/rstudio-global-changes-show-chunk-output-in-console-via-cli)
- [ggplot2 3.3.0. More control over aesthetic evaluation](https://www.tidyverse.org/blog/2020/03/ggplot2-3-3-0/#more-control-over-aesthetic-evaluation)
- [Complete themes in ggplot](https://rpubs.com/Mentors_Ubiqum/default_themes)
- [Get, set, and modify the active theme](https://ggplot2.tidyverse.org/reference/theme_get.html)
- COOL! [grafify](https://grafify-vignettes.netlify.app/) An R package for easy graphs, ANOVAs and post-hoc comparisons]
- Workshop. [Визуализируй это: визуализация данных в R. Балтыжакова Татьяна](https://baltti.github.io/workshop-DH21/ggplot2-tutorial-DH.html)
- COOL! [ggplot2/ggplot_theme_system_cheatsheet.pdf](https://github.com/claragranell/ggplot2/blob/main/ggplot_theme_system_cheatsheet.pdf)
- COOL! [ragg, svglite, and the new graphics features](https://www.tidyverse.org/blog/2022/02/new-graphic-features/)
- [7.2 Using Mathematical Expressions in Annotations](https://r-graphics.org/recipe-annotate-text-math). Use `annotate(geom = "text")` with `parse = TRUE`
- COOL! [Formatting Math Symbols and Expressions in ggplot Labels](https://www.benjaminackerman.com/post/2019-03-08-equation_labels/). In order to add math notation to those labels, we can use the `expression()` function to specify the label text.
- [plotmath {grDevices}](https://stat.ethz.ch/R-manual/R-devel/library/grDevices/html/plotmath.html). Mathematical Annotation in R
- [Визуализируй это: визуализация данных в R](https://baltti.github.io/workshop-DH21/ggplot2-tutorial-DH.html) by Балтыжакова Татьяна
- [Overlaying histograms with ggplot2 in R](https://stackoverflow.com/questions/6957549/overlaying-histograms-with-ggplot2-in-r)
- COOL! [Quick and easy ways to deal with long labels in ggplot2](https://www.andrewheiss.com/blog/2022/06/23/long-labels-ggplot/)
- [The path to {ggpath}](https://posit.co/blog/the-path-to-ggpath). A 2.5 year long story about the open source R community and the #nflverse.
- [ggplot2::scale_x_time: Formatting hms objects](https://stackoverflow.com/questions/58395236/ggplot2scale-x-time-formatting-hms-objects)



## ggplot debug & performance
- [ggpmisc 0.2.13. Debugging ggplots](https://cran.r-project.org/web/packages/ggpmisc/vignettes/debug.html)
- [gginnards](https://docs.r4photobiology.info/gginnards/). Package ‘gginnards’ (Explore the innards of ‘ggplot2’) is a set of extensions to R package ‘ggplot2’ and tools specially useful when learning how to write extensions and when debugging newly defined stats and geoms.
- COOL! [User Guide: 1 Debugging ggplots](https://cran.r-project.org/web/packages/gginnards/vignettes/user-guide-1.html)
- [`ggdebug` - a package for debugging ggplot stats](https://coolbutuseless.github.io/2019/03/26/ggdebug-a-package-for-debugging-ggplot-stats/)
- [Gggplot2 Internals - An Unofficial Reference](https://htmlpreview.github.io/?https://github.com/brodieG/ggbg/blob/development/inst/doc/extensions.html)
- [pter 1 Demystifying ggplot2](https://rud.is/books/creating-ggplot2-extensions/demystifying-ggplot2.html)
- [Internals of ggplot2](https://ggplot2-book.org/internals.html)
- [ggplot2. Profiling Performance](https://ggplot2.tidyverse.org/articles/profiling.html)
- [Benchmark plot creation time. Broken down into construct, build, render and draw times.](https://ggplot2.tidyverse.org/reference/benchplot.html)
- Отличная подборка тестирования различных драйверов и функций по отрисовке графических примитивов. [High-level Graphics Benchmarking](https://github.com/thomasp85/plotting_benchmark)
- [Ragg Performance](https://rpubs.com/jeroenooms/ragg)
- [Working with R, Cairo graphics, custom fonts, and ggplot](https://www.andrewheiss.com/blog/2017/09/27/working-with-r-cairo-graphics-custom-fonts-and-ggplot/)
The Cairo graphics library makes it easy to embed custom fonts in PDFs and create high resolution PNGs (with either AGG or Cairo).
- [Saving R Graphics across OSs](https://www.jumpingrivers.com/blog/r-graphics-cairo-png-pdf-saving/)
- [Package 'grDevices'](https://r-universe.dev/manuals/grDevices.html)

## ggplot smooth
- [`geom_smooth` with `facet_grid` and different fitting functions](https://stackoverflow.com/questions/44912496/geom-smooth-with-facet-grid-and-different-fitting-functions)
- [supplying custom knot values to `geom_smooth()` by facet](https://stackoverflow.com/questions/63388121/supplying-custom-knot-values-to-geom-smooth-by-facet)
- [Ggplot change "k" in "gam" formula of `geom_smooth()`](https://community.rstudio.com/t/ggplot-change-k-in-gam-formula-of-geom-smooth/1948)
- [How to use a custom method in ggplot2 for fitting smooth line {closed}](https://stats.stackexchange.com/questions/432132/how-to-use-a-custom-method-in-ggplot2-for-fitting-smooth-line)
- [Piecewise Regression and Splines](https://bookdown.org/tpinto_home/Beyond-Linearity/piecewise-regression-and-splines.html)
- [Smooth terms in GAM](https://stat.ethz.ch/R-manual/R-devel/library/mgcv/html/smooth.terms.html) smooth.terms {mgcv}.
- [HOW CAN I EXPLORE DIFFERENT SMOOTHS IN GGPLOT2? | R FAQ](https://stats.oarc.ucla.edu/r/faq/how-can-i-explore-different-smooths-in-ggplot2/)

## Dual axes
- [Dual axes time series plots may be ok sometimes after all](http://ellisp.github.io/blog/2016/08/18/dualaxes). Dual axis time series charts are often deprecated, but the standard alternatives have weaknesses too. In some circumstances, if done carefully, dual axis time series charts may be ok after all. In particular, you can choose two vertical scales so the drawing on the page is equivalent to drawing two indexed series, but retaining the meaningful mapping to the scale of the original variables.
- [Dual axes time series plots with various more awkward data](http://ellisp.github.io/blog/2016/08/28/dualaxes2). TL;DR Summary:
I finish enhancements of the dual axes time series plotting function in R so it handles reasonably well series that may start at different times, have different frequencies, or include negatives.
- [Two Y-Axes](https://kieranhealy.org/blog/archives/2016/01/16/two-y-axes/). Matt remarked that “Friends don’t let friends use two y-axes”. It’s a good rule. The topic came up a couple of times during the data visualization short course I taught last semester. Using two y-axes makes it even easier than usual to fool yourself (or someone else) about the degree of association between two variables. This is because you can adjust the scaling of the axes to relative to one another in way that moves the data series around more or less however you like.
- [Dual axes for ggplot2](https://gist.github.com/jslefche/e4c0e9f57f0af49fca87). Modified from: [ggplot2-adding-secondary-transformed-x-axis-on-top-of-plot](https://stackoverflow.com/questions/21026598/ggplot2-adding-secondary-transformed-x-axis-on-top-of-plot) & [dual_axis_in_ggplot2](https://rpubs.com/kohske/dual_axis_in_ggplot2)
- [R: single plot with two different y-axes](http://www.gettinggeneticsdone.com/2015/04/r-single-plot-with-two-different-y-axes.html)
- [Dual axes charts in ggplot2 - why they can be useful and how to make them](https://www.johnmackintosh.net/blog/2022-03-13-dual-axis/)

## highlighting
- COOL! [gghighlight 0.3.2](https://yutani.rbind.io/post/2021-06-07-gghighlight-032/)
	- [Highlighting with ggplot2: The Old School and New School Way](https://www.littlemissdata.com/blog/highlight)
- COOL! [gghighlight 0.2.0](https://yutani.rbind.io/post/gghighlight-0-2-0/). gghighlight 0.2.0 is on CRAN a while ago. This post briefly introduces the three new features. For basic usages, please refer to “Introduction to gghighlight”.
- [Anatomy of gghighlight](https://yutani.rbind.io/post/2018-06-03-anatomy-of-gghighlight/)
- [Highlight a single "bar" in ggplot](https://stackoverflow.com/questions/45820250/highlight-a-single-bar-in-ggplot)

## palettes
- COOL! [vankesteren/firatheme](https://github.com/vankesteren/firatheme) a ggplot2 theme with fira font
- [Mikata-Project/ggthemr](https://github.com/Mikata-Project/ggthemr). Themes for ggplot2.
- [BlakeRMills/MetBrewer](https://github.com/BlakeRMills/MetBrewer). Color palette package in R inspired by works at the Metropolitan Museum of Art in New York
- COOL! [cols4all](https://github.com/mtennekes/cols4all). The cols4all is a new R package for selecting color palettes. “Color for all” refers to our mission that colors should be usable for not just people with normal color vision, but also for people with color vision deficiency. Currently, this package contains palettes from several popular and lesser known color palette series: Color Brewer, Viridis, Kovesi, Paul Tol, Scico, Carto, Tableau and Wes Anderson. Own palettes series can be added as well.
- COOL! [colorspace: New Tools for Colors and Palettes](https://eeecon.uibk.ac.at/~zeileis/news/colorspace/)
A major update (version 1.4.0) of the R package colorspace has been released to CRAN, enhancing many of the package's capabilities, e.g., more refined palettes, named palettes, ggplot2 color scales, visualizations for assessing palettes, shiny and Tcl/Tk apps, color vision deficiency emulation, and much more.
- [Generate Color Palettes](https://rpkgs.datanovia.com/ggpubr/reference/get_palette.html)
Generate a palette of k colors from ggsci palettes, RColorbrewer palettes and custom color palettes. Useful to extend RColorBrewer and ggsci to support more colors.
- [TOP R COLOR PALETTES TO KNOW FOR GREAT DATA VISUALIZATION](https://www.datanovia.com/en/blog/top-r-color-palettes-to-know-for-great-data-visualization/)
- COOL! [How to create a color palette in R with more than 15 colors with ggplot2 #19 {Closed}](https://github.com/duttashi/visualizer/issues/19)
- [#40 RCOLORBREWER : GET A LONGER PALETTE](https://www.r-graph-gallery.com/40-rcolorbrewer-get-a-longer-palette/)
- [THE PAUL TOL 21-COLOR SALUTE](https://tradeblotter.wordpress.com/2013/02/28/the-paul-tol-21-color-salute/)
- COOL! [Some thoughts about colors: Color spaces](https://clauswilke.com/art/post/colors-color-spaces). Art by Claus O. Wilke
- COOL! [Polychrome: Qualitative Palettes with Many Colors](https://cran.rstudio.com/web/packages/Polychrome/index.html). Tools for creating, viewing, and assessing qualitative palettes with many (20-30 or more) colors.
- [colortools: Tools for colors in a Hue-Saturation-Value (HSV) color model](https://cran.r-project.org/web/packages/colortools/index.html). R package with handy functions to help users select and play with color schemes in an HSV color model
- [colorBrewer interactive tool](https://www.computerworld.com/article/3184778/6-useful-r-functions-you-might-not-know.html). First, install tmaptools with install.packages("tmaptools"), then load tmaptools with library("tmaptools") and run palette_explorer() (or, don't load tmaptools and run tmaptools::palette_explorer() ). You'll see all available palettes as in the image above, as well as sliders to adjust options like number of colors. There's also info about basic syntax for using a color scheme below each group of palettes.
- [Scientific Journal and Sci-Fi Themed Color Palettes for ggplot2](https://cran.r-project.org/web/packages/ggsci/vignettes/ggsci.html)
- [ggplot: How to create a discrete color palette that fits the data automatically?](https://stackoverflow.com/questions/13995296/ggplot-how-to-create-a-discrete-color-palette-that-fits-the-data-automatically)
- COOL! [BUILDING COLOR PALETTE PROOFS OF CONCEPT WITH PURRR AND GGPLOT2](https://data-chronicler.netlify.com/2020/01/08/2019-12-30-building-color-palette-proof-of-concepts-with-purrr-and-ggplot2/)
- [Multiple color (and fill) scales with ggplot2](https://eliocamp.github.io/codigo-r/2018/09/multiple-color-and-fill-scales-with-ggplot2/)
	- [`ggnewscale`](https://eliocamp.github.io/ggnewscale/) tries to make it painless to use multiple scales in `ggplot2`.
	- [Distinct color palettes for two different groups in ggplot2](https://stackoverflow.com/questions/47901720/distinct-color-palettes-for-two-different-groups-in-ggplot2)



## facet
- [Useful labeller functions](https://ggplot2.tidyverse.org/reference/labellers.html). Labeller functions are in charge of formatting the strip labels of facet grids and wraps. 
- Создание собственных меток в facet (идея):
```
# формируем кастомный генератор меток для фасета
storeLabeller <- function(string) {
  paste0("SAP ID = ", string)
}

    # посмотрим на распределение остатков по времени
    dfplot <- p2_df %>%
      ggplot(aes(timestamp, value)) +
      geom_point(shape = 21, size = 1.5, alpha = 0.2) +
      geom_smooth() +
      # отобразим дату перевода на БАХУС
      geom_vline(aes(xintercept = bswitch_date), colour = "red", lwd = 1.5) +
      scale_x_date( 
        date_breaks = "1 week",
        limits = base::range(p2_df$timestamp, na.rm = TRUE)
        ) +
      scale_y_log10(labels = scales::trans_format("log10", scales::math_format(10^.x))) +
      theme_ipsum_rc() +
      # раскладка по заводу SAP (номер магазина)
      facet_wrap(~store_id, ncol = 2, scales = "free", labeller = labeller(store_id = storeLabeller)) +
      guides(colour = FALSE) +
      # Трюк 'ось X': включаем ось x у всех графиков
      theme(axis.text.x = element_text(angle = 90, hjust = 1, vjust = 0.5)) +
      xlab("Дата") +
      ylab("Отрицательный остаток") +
      ggtitle(label = "Динамика совокупных остатков")
```
- [Overlaying facetted histograms with normal curve using ggplot2](https://data-se.netlify.app/2021/06/23/overlaying-facetted-histograms-with-normal-curve-using-ggplot2/)

# extensions
- [eulerr](https://jolars.github.io/eulerr/index.html) generates area-proportional Euler diagrams that display set relationships (intersections, unions, and disjoints) with circles or ellipses
- [ggantrify](https://github.com/giocomai/ganttrify) Create beautiful Gantt charts with ggplot2
- COOL! [gtExtras](https://jthomasmock.github.io/gtExtras/index.html). The goal of gtExtras is to provide some additional helper functions to assist in creating beautiful tables with gt.

=======
- COOL! Как эффективно применить `ggfx` [Better data communication with {ggplot2}, part 2](https://giulia-ruggeri.medium.com/better-data-communication-with-ggplot2-part-2-615a5180ccb)

# upset graph
- COOL! [UpSet Homepage](https://upset.app/). Visualizing Intersecting Sets
- [UpSet: Visualization of Intersecting Sets](https://vdl.sci.utah.edu/publications/2014_infovis_upset/)
- [UpSetR: An R Package For The Visualization Of Intersecting Sets And Their Properties](https://vdl.sci.utah.edu/publications/2017_bioinformatics_upsetr/)
- [UpSetR](https://github.com/hms-dbmi/UpSetR) generates static UpSet plots.
- [ComplexHeatmap. UpSet plot](https://jokergoo.github.io/ComplexHeatmap-reference/book/upset-plot.html)
UpSet plot provides an efficient way to visualize intersections of multiple sets compared to the traditional approaches, i.e. the Venn Diagram. 

# other
- [ggplot2 Version of Figures in Lattice: Multivariate Data. Visualization with R](https://learnr.files.wordpress.com/2009/08/latbook.pdf)
- COOL! [Altair: Declarative Visualization in Python](https://altair-viz.github.io/)
	- [vegawidget](https://vegawidget.github.io/vegawidget/index.html)
The goal of vegawidget is to render Vega-Lite and Vega specifications as htmlwidgets, and to provide you a means to communicate with a Vega chart using JavaScript or Shiny.
	- [ggvega](https://vegawidget.github.io/ggvega/)
The goal of ggvega is to translate a ggplot2 object to a Vega-Lite specification.
	- [vlbuildr](https://vegawidget.github.io/vlbuildr/index.html)
The goal of vlbuildr is to provide an R api for building up vega-lite specs.
- [trelliscopejs](https://hafen.github.io/trelliscopejs/). Trelliscope is a scalable, flexible, interactive approach to visualizing data.
	- [Better examples of how you export a Trelliscope object {#24}](https://github.com/hafen/trelliscopejs/issues/24).
```
facet_trelliscope(~ country + continent, nrow = 2, ncol = 7, width = 300, path = "/tmp/gap")
list.files("/tmp/gap")
```
	
- COOL! [a ggplot2 grammar guide](https://evamaerey.github.io/ggplot2_grammar_guide/about)
- COOL! Для того, чтобы `render_graph` в `DiagrammeR` работал и сохранял граф в файл, необходимо доставлять руками библиотеки `DiagrammeRSVG` и `V8`. Они отсутствуют в явных зависимостях.
- Хорошая статья с визуализациями. [Tracking covid-19 excess deaths across countries](https://www.economist.com/graphic-detail/coronavirus-excess-deaths-tracker)
- [Waffle chart (square pie) in ggplot2](https://r-charts.com/part-whole/waffle-chart-ggplot2/)
- [The juicr R package](https://github.com/mjlajeunesse/juicr) is a GUI interface to automated, semi-automated, and manual tools for extracting data from scientific images -- like scatter or bar plots that contain data, or other images with information that can be converted numerically or coordinates classified.


# font
- COOL! [Taking Control of Plot Scaling](https://www.tidyverse.org/blog/2020/08/taking-control-of-plot-scaling/)
- [Modern Text Features in R](https://www.tidyverse.org/blog/2021/02/modern-text-features/)
- COOL! [Understanding text size and resolution in ggplot2](https://www.christophenicault.com/post/understand_size_dimension_ggplot2/)
- Меняем шрифт вывода кода в Quarto с помощью CSS:
```{css, echo=FALSE}
.cell-output-stdout {
  font-size: 14px;
}
```

# d3
- [Fullstack D3 and Data Visualization: Build beautiful data visualizations with D3](https://www.amazon.com/Fullstack-Data-Visualization-beautiful-visualizations/dp/0991344650)
- [D3 TO R TO D3](https://maya.rbind.io/post/2020/d3-to-r-to-d3/)
- COOL! [A starting point to explore data visualization using D3.js](https://github.com/TheRobBrennan/explore-data-visualization-with-D3)

# ggplot tutorial
- [Graphic Design with ggplot2](https://rstudio-conf-2022.github.io/ggplot2-graphic-design/). How to Create Engaging and Complex Visualizations in R
An rstudio::conf(2022) Workshop by Cédric Scherer

# Tables

## DT DataTable
- [changing font size in R DataTables (DT)](https://stackoverflow.com/questions/44101055/changing-font-size-in-r-datatables-dt)
- [Change Text Size in DataTable](https://datatables.net/forums/discussion/66743/change-text-size-in-datatable)

## gt
- [Create interactive links in gt table (in rmarkdown)](https://community.rstudio.com/t/create-interactive-links-in-gt-table-in-rmarkdown/70266/2)
- `html()` will tell gt to deal with the text as html content. You can create the text yourself. I used htmltools helper
- `md()` will tell get to consider the text as markdown, and it will process it to render as html.
- [Embed links to cells of R's gt tables](https://stackoverflow.com/questions/68720533/embed-links-to-cells-of-rs-gt-tables)
- [Embedding custom HTML in gt tables](https://themockup.blog/posts/2020-10-31-embedding-custom-features-in-gt-tables/index.html)
- [Adding images to group headers using text_transform in a gt table](https://stackoverflow.com/questions/73068835/adding-images-to-group-headers-using-text-transform-in-a-gt-table)
- Как не красить ячейки с `NA`. [R gt table make NA values not appear](https://stackoverflow.com/questions/73599951/r-gt-table-make-na-values-not-appear)
```
colors = scales::col_numeric(
      palette = pal,
      domain = c(0, 20),
      na.color = "transparent"
    )
```
- [R gt_table adjust row height](https://stackoverflow.com/questions/64127905/r-gt-table-adjust-row-height)
- [Basic gt Styling Reference](https://adrumm.quarto.pub/basic-gt-styling-reference/)
- gt & js
	- [JavaScript onClick event - HTML table](https://stackoverflow.com/questions/21033368/javascript-onclick-event-html-table)
	- [Find table cell value on cell (table) click using JavaScript](http://dotnetlearners.com/javascript/find-table-cell-value-on-cell-table-click-using-javascript)
- [The table.font.size option has no effect on column labels #337 {Closed}](https://github.com/rstudio/gt/issues/337)
- Quarto. [07 - Plots, Graphics, and tables](https://rstudio-conf-2022.github.io/get-started-quarto/materials/07-plots-tables.html#/plots-graphics-and-tables).
- [Set {gt} table header height](https://stackoverflow.com/questions/73588003/set-gt-table-header-height). Есть такое магическое слово `inherited`, которое перекрывает настройки!
Но для всех таблиц!!! `table.gt_table` переопределяет! Найдено такое решение `as_raw_html(inline_css = TRUE)`:
```{r}
#| label: plot traces with gt (debug)
#| column: page
#| results: asis

events_dt %>%
  .[event != "Probing"] %>%
  .[, open_date := as.Date(min(start)), by = case_id] %>%
  .[open_date >= as.Date(g_probing_time) - 30] %>%
  buildBPTraces() %>%
  setDT() %>%
  tableBPTraces(max_psteps = 12) %>%
  tab_options(table.font.size = "small") %>%
  # чтобы не было inherited параметров и tab_options работал в полную при рендере
  as_raw_html(inline_css = TRUE)
  # tab_options(table.font.size = px(4L))
  # opt_css(
  #   css = "
  #   .gt_table {
  #     font-size: 12px !important;
  #   }",
  #   add = FALSE
  # )
  # table.additional_css
```

- Slides! [Beautiful Tables in R. gt and the grammar of tables](https://themockup.blog/static/slides/intro-tables.html#1) by Tom Mock, 2021-08-30
- [gt tables in Quarto Pub without slide CSS styling](https://stackoverflow.com/questions/72904794/gt-tables-in-quarto-pub-without-slide-css-styling)
- COOL! [Graphing in gt](https://jthomasmock.github.io/gtExtras/articles/plots-in-gt.html)
- COOL! [New Features and Serious Upgrades in {gt} 0.8.0](https://posit.co/blog/new-features-upgrades-in-gt-0-8-0/)
The v0.8.0 release of gt is quite exciting so we want to show you all the things you can now do when making tables!
- COOL! [New formatting functions in {gt} 0.9.0](https://posit.co/blog/new-formatting-functions-in-gt-0-9-0/)

### font issues gt + quarto
- [Change in Quarto from Rstudio RStudio 2022.07.1+554 to 2022.07.2+576 #3357](https://github.com/quarto-dev/quarto-cli/discussions/3357). Probably caused by some CSS overwriting the table CSS.
If you don't want Quarto or anything actually to take over the styling, then you should consider to use `gt::as_raw_html(data, inline_css = TRUE)` (https://gt.rstudio.com/reference/as_raw_html.html).

## reactable
- [A couple useful JavaScript aggregation and formatting functions for {reactable}](https://www.zajichekstats.com/post/reactable-javascript/)
- [Interactive Drill-down Tables using {reactable}](https://rpubs.com/StevenDuttRoss/flextable2)
- [Conditional Styling](https://glin.github.io/reactable/articles/conditional-styling.html)
- Офигенский пример таблички, с картинками, спарклайнами и немного js. [Tidyverse in Numbers](https://szymanskir.quarto.pub/tidyverse_in_numbers/)

# ECharts
- [Форматирование меток осей](https://echarts.apache.org/en/option.html#xAxis.axisLabel.formatter)
- [R echarts4r - format dates in axis](https://stackoverflow.com/questions/63838914/r-echarts4r-format-dates-in-axis)
- [Mark area](https://echarts.apache.org/examples/en/editor.html?c=line-sections)
- [Multple mark area style #52 {Open}](https://github.com/JohnCoene/echarts4r/issues/52)

# Observable
- [A beginner's guide to using Observable JavaScript, R, and Python with Quarto](https://www.infoworld.com/article/3674789/a-beginners-guide-to-using-observable-javascript-r-and-python-with-quarto.html)
- [Observable JS](https://quarto.org/docs/interactive/ojs/)
- [Wrangling data in JavaScript with Arquero: a primer for R users](https://observablehq.com/@observablehq/data-wrangling-with-arquero-from-r)
- [Introducing Arquero](https://observablehq.com/@uwdata/introducing-arquero)
- COOL! [Pass R object to Observable in Quarto](https://stackoverflow.com/questions/73873681/pass-r-object-to-observable-in-quarto)
- [Observable Imports in Quarto](https://timelyportfolio.github.io/quarto_tests/examples/quarto_observable_imports/quarto_observable_imports.html)
- [An Illustrated Guide to Arquero Verbs](https://observablehq.com/@uwdata/an-illustrated-guide-to-arquero-verbs)
- [Plot from ggplot2](https://observablehq.com/@observablehq/plot-from-ggplot2)
- [Observable Plot](https://observablehq.com/@observablehq/plot)
- [obsplot](https://juba.github.io/obsplot/index.html) is an experimental attempt at using Observable Plot as HTML widget in R.
- Sample. [Connected Scatter](https://observablehq.com/@observablehq/connected-scatter)
- COOL! [outlier 2022](https://observablehq.com/collection/@observablehq/outlier-2022)
- Painting with Data: D3.js [Interacting with Data](https://observablehq.com/@observablehq/pwd3-interacting-with-data)
- COOL! [Interactive filtering](https://observablehq.com/@observablehq/arsc-part-2-interactive-filtering). Building an advanced report from simple components.
- [Introduction to inputs](https://observablehq.com/@observablehq/inputs?collection=@observablehq/observable-libraries-for-visualization)
In Observable, though, cells run in the order they’re needed—what’s called a reactive dataflow.
	- [OBSERVABLE INPUTS › TABLE · API](https://observablehq.com/@observablehq/input-table)
	- [Observable's not JavaScript](https://observablehq.com/@observablehq/observable-javascript). JavaScript on Observable is almost — but not entirely — vanilla
	- [How Observable Runs](https://observablehq.com/@observablehq/how-observable-runs)
	- [Reactive Dataflow](https://observablehq.com/@observablehq/reactive-dataflow)
- [Debugging a function in observable](https://talk.observablehq.com/t/debugging-a-function-in-observable/2246)
- [Peak Detection for Data Visualization](https://observablehq.com/@yurivish/peak-detection)
- [Recreating an Altman-Gardner Plot in Javascript based on the dabest package in R](https://observablehq.com/@lorenasandoval88/altman-gardner-plot)

## ojs_define
- [OJS Data Sources](https://quarto.org/docs/interactive/ojs/data-sources.html)
- [Use dataframe created in R codechunk in ojs codechunk in quarto](https://stackoverflow.com/questions/73080070/use-dataframe-created-in-r-codechunk-in-ojs-codechunk-in-quarto)
Solution: Use the `ojs_define()` function to make data processed in Python or R available to `{ojs}` cells (this function should be called in the R or Python cell).
- [`ojs_define()` in Quarto Book to define variable in all chapters {#3587}](https://github.com/quarto-dev/quarto-cli/discussions/3587).
Solution: Use imports across pages instead:
```{ojs}
import { x } from "./foo.qmd";
```


## API & manuals
- [Observable Inputs](https://github.com/observablehq/inputs)
- [Input: Table](https://observablehq.com/@observablehq/input-table)
- [Hello, Inputs!](https://observablehq.com/@observablehq/hello-inputs)

# Graph
- COOL! [cyjShiny: Cytoscape.js Shiny Widget (cyjShiny)](https://cran.r-project.org/web/packages/cyjShiny/index.html). Для него необходимо ставить пакет [`graph`](http://www.bioconductor.org/packages/release/bioc/html/graph.html) с Биокондуктора.
