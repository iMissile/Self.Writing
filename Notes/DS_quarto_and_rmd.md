# Quarto
## releases
- [quarto webR 0.4.0: Ball of Yarn (02-05-2024)](https://quarto-webr.thecoatlessprofessor.com/qwebr-release-notes.html#ball-of-yarn-02-05-2024)

## Quarto general
- [awesome quarto](https://github.com/mcanouil/awesome-quarto). A curated list of Quarto talks, tools, examples & articles! Contributions welcome!
- [rstudio::conf 2022 Workshop](https://rstudio-conf-2022.github.io/get-started-quarto/) Getting Started with Quarto by Tom Mock
- [Notes on Changing from Rmarkdown/Bookdown to Quarto](https://www.njtierney.com/post/2022/04/11/rmd-to-qmd/)
- [FAQ for R Markdown Users](https://quarto.org/docs/faq/rmarkdown.html)
- [Quarto Troubleshooting](https://quarto.org/docs/troubleshooting/). Если нужно из не-интерактивной сессии трейс получить и всё такое.
- [Quarto prs & issues](https://rpubs.com/rich_i/quarto-prs-issues)
- COOL! [6 Productivity Hacks for Quarto](https://posit.co/blog/6-productivity-hacks-for-quarto/)
- COOL! [Welcome to Quarto](https://quarto.org). A scientific and technical publishing system built on Pandoc (RStudio)
- [Component Layout](https://quarto.org/docs/interactive/layout.html). Тут активно упоминается про `:::`.
```
::: {.classname}
Div
:::
```
will [generate html `div`](https://quarto.org/docs/authoring/markdown-basics.html#other-blocks).
- [Quarto, Python, and VS Code: Quarto Reports In VS Code](https://appsilon.com/quarto-python-and-vscode/)
- COOL! [Notes on Changing from Rmarkdown/Bookdown to Quarto](https://www.njtierney.com/post/2022/04/11/rmd-to-qmd/) by Nicholas Tierney
- COOL! [Making Slides in Quarto with reveal.js](https://meghan.rbind.io/blog/quarto-slides/) by Meghan Hall
- COOL! [The ultimate guide to starting a Quarto blog](https://albert-rapp.de/posts/13_quarto_blog_writing_guide/13_quarto_blog_writing_guide.html)
This blog post is an in-depth guide on how to start blogging with Quarto.
- [Porting a distill blog to quarto](https://blog.djnavarro.net/posts/2022-04-20_porting-to-quarto/https://blog.djnavarro.net/posts/2022-04-20_porting-to-quarto/)
- Разбираемся с темами и шириной текста:
	- [Page Layout](https://quarto.org/docs/output-formats/page-layout.html)
	- [HTML Theming](https://quarto.org/docs/output-formats/html-themes.html)
- [Experimenting with Quarto](https://tshafer.com/blog/2022/06/experimenting-with-quarto)
- [Using multiple font sizes for code chunks](https://community.rstudio.com/t/using-multiple-font-sizes-for-code-chunks/26405)
- [Chunk Options](https://quarto.org/docs/computations/r.html). Есть специфика межу Quarto YAML и Rmarkdown опциями!!
- [Creating a website using Quarto and RStudio](https://quarto-workshop.netlify.app/)
- [How to publish a website FOR FREE in under 60 seconds using Quarto](https://www.youtube.com/watch?v=nuYNCPRf8Js)
- [Creating a blog with Quarto in 10 steps](https://beamilz.com/posts/2022-06-05-creating-a-blog-with-quarto/en/)
In this post, I introduce you to my new blog and show how you can create a blog with Quarto for R users.
- [Building with Quarto](https://robertmitchellv.com/blog/2022-08-building-with-quarto/building-with-quarto.html)
- [A Step-by-Step Guide: Deploying on Netlify](https://www.netlify.com/blog/2016/09/29/a-step-by-step-guide-deploying-on-netlify/)
- [Quarto Pub](https://quarto.org/docs/publishing/quarto-pub.html)
	- Может здесь кроется ответ на часть вопросов по ошибке 404. [Quarto - GitHub Pages](https://quarto.org/docs/publishing/github-pages.html)
- COOL! [R Markdown Tips, Tricks, and Shortcuts](https://www.dataquest.io/blog/r-markdown-tips-tricks-and-shortcuts)
- COOL! [RMarkdown collapsible panel](https://stackoverflow.com/questions/52576626/rmarkdown-collapsible-panel)
- [Quarto self-contained](https://quarto.org/docs/output-formats/html-basics.html#self-contained). Кроме yaml заголовка можно в командной строке еще написать `--embed-resources --standalone`
- [embed-resources works from command line, not from rstudio #2364 {Closed}](https://github.com/quarto-dev/quarto-cli/issues/2364)
- COOL! [Iterating to create tabs with gt in quarto](https://stackoverflow.com/questions/73585417/iterating-to-create-tabs-with-gt-in-quarto)
- [How can I specify global and local chunk options for a quarto pdf book?](https://stackoverflow.com/questions/73264233/how-can-i-specify-global-and-local-chunk-options-for-a-quarto-pdf-book)
- [10+ Guidelines for Better Tables in R](https://themockup.blog/posts/2020-09-04-10-table-rules-in-r/)
- [Testing methods for df_print-like custom table printing in quarto](https://gist.github.com/debruine/01b4ce274733a4a99622365e8c6df701)
- [Multi-Format Publishing](https://quarto.org/docs/prerelease/1.3/multi-format.html)
- [What I've learned making an .epub Ebook with Quarto](https://www.brodrigues.co/blog/2023-03-03-quarto_books/)
- Евгений Матеров. [Серия митапов по Quarto, проводимых 4, 11 и 18 марта 2023 года](https://github.com/materov/quarto-meetup-begin)
- [webR Code Extension for Quarto HTML Documents](https://github.com/coatless/quarto-webr)
- [vtree object is renderred in Rmarkdown but not in quarto](https://stackoverflow.com/questions/72671641/vtree-object-is-renderred-in-rmarkdown-but-not-in-quarto). Quarto works a bit differently than R Markdown as it will run R only for the knitting process, and not for the conversion to output format, here HTML.
- [How to resize figures in Quarto (PDF output)?](https://stackoverflow.com/questions/73844454/how-to-resize-figures-in-quarto-pdf-output)
- [Switching to quarto](https://jollydata.blog/posts/2022-08-06-_switching-to-quarto/switching-to-quarto.html)
I recently ported my blog to quarto. In this post I highlight the key features, that I like about quarto and that I implemented for this website.
- [Auto adjust height of widget to screen height {#3191}](https://github.com/quarto-dev/quarto-cli/discussions/3191) `widget.layout.height = "100vh"`
	- [16.4 Widget sizing](https://bookdown.org/yihui/rmarkdown/htmlwidgets-size.html)
	- [HTML Widget Sizing](https://cran.r-project.org/web/packages/htmlwidgets/vignettes/develop_sizing.html)
	- [Plotly not correctly scaled based on width and height {#4836}](https://github.com/quarto-dev/quarto-cli/issues/4836)
	- [Why is the layout of a graph from visnetwork in html too small](https://stackoverflow.com/questions/50250060/why-is-the-layout-of-a-graph-from-visnetwork-in-html-too-small)

## Quarto parametrization
- [How to use Quarto for Parameterized Reporting](https://www.mm218.dev/posts/2022-08-04-how-to-use-quarto-for-parameterized-reporting/). You know. If you wanna.
```{r}
#| eval: !expr params$state == "NY"
```
- [Quarto: Parsing an expression to chunk labels](https://stackoverflow.com/questions/74402963/quarto-parsing-an-expression-to-chunk-labels)
You could use `!expr` in your `fig-cap`: to parse an R expression like this: `#| fig-cap: !expr cap`

## Quarto & fonts
- COOL! [Setting up and debugging custom fonts](https://yjunechoe.github.io/posts/2021-06-24-setting-up-and-debugging-custom-fonts/)
In quarto, you can set the custom ragg_png device (defined above) in the YAML, like so:
```
  knitr:
    opts_chunk: 
      dev: "ragg_png"
```
- Мучаемся с ошибкой `Warning in grid.Call(C_textBounds, as.graphicsAnnot(x$label), x$x, x$y, :
семейство шрифтов не найдено в базе данных шрифтов Windows`
	- [Warning in grid.Call(C_textBounds, as.graphicsAnnot(x$label), x$x, x$y, : font width unknown for character 0x20](https://stackoverflow.com/questions/62067139/warning-in-grid-callc-textbounds-as-graphicsannotxlabel-xx-xy-font-w)
- [A beginner's guide to using Observable JavaScript, R, and Python with Quarto](https://www.infoworld.com/article/3674789/a-beginners-guide-to-using-observable-javascript-r-and-python-with-quarto.html)
- [Slidecraft 101: Colors and Fonts](https://www.emilhvitfeldt.com/post/slidecraft-colors-fonts/)
- [Slidecraft 101: Code and Output](https://www.emilhvitfeldt.com/post/slidecraft-code-output/)
	- COOL! [Use fonts with ligatures](https://www.emilhvitfeldt.com/post/slidecraft-code-output/#use-fonts-with-ligatures)
- COOL! [reveal-fonts-reprex](https://github.com/gadenbuie/reveal-fonts-reprex)
- [Quarto Sass Variables](https://quarto.org/docs/presentations/revealjs/themes.html#sass-variables)

## Quarto & blogdown
- [Using Quarto in Blogdown](https://stackoverflow.com/questions/72072249/using-quarto-in-blogdown). Migrating from Rmd to Qmd has no really advantage as you can't really use Quarto feature in a Hugo website, or at least it will be limited
- COOL! [From Blogdown to Quarto](https://www.incidentalfindings.org/posts/2022-08-30_from-blogdown-to-quarto/)
	- [Creating a blog with Quarto in 10 steps](https://beamilz.com/posts/2022-06-05-creating-a-blog-with-quarto/en/)
In this post, I introduce you to my new blog and show how you can create a blog with Quarto for R users.
- [The ultimate guide to starting a Quarto blog](https://albert-rapp.de/posts/13_quarto_blog_writing_guide/13_quarto_blog_writing_guide.html)
- [Migration from Hugo/blogdown/Wowchemy to Quarto](https://www.andreashandel.com/posts/2022-10-01-hugo-to-quarto-migration/) by Andreas Handel
- [Hugo](https://quarto.org/docs/output-formats/hugo.html)

## Quarto & css
- [Down the front-end rabbit hole](https://quartoand.me/front-end)
- COOL! [CSS Tweaks for Quarto](https://jmclawson.net/posts/quarto-css/)
- [Define a new callout in quarto](https://stackoverflow.com/questions/74647399/define-a-new-callout-in-quarto)
- [How to apply CSS style to Quarto output](https://stackoverflow.com/questions/74026514/how-to-apply-css-style-to-quarto-output)
- [Add a CSS class to single code chunks in RMarkdown](https://stackoverflow.com/questions/37944197/add-a-css-class-to-single-code-chunks-in-rmarkdown)
- [How to hide CSS chunks in Quarto (qmd)](https://community.rstudio.com/t/how-to-hide-css-chunks-in-quarto-qmd/158904)
```{css}
/*| echo: false */
h1 {
  color: blue;
}
```
- [Use a css code chunk to embed the CSS rules directly in your quarto document {#1402}](https://github.com/quarto-dev/quarto-cli/discussions/1402)
```{css, echo=FALSE}
p {
  font-size: 32px;
}
```
or raw html
```{=html}
<style>
...
</style>
```


## Quarto & Reveal.js
- [Reveal Themes](https://quarto.org/docs/presentations/revealjs/themes.html)
- [Advanced Reveal](https://quarto.org/docs/presentations/revealjs/advanced.html)
- [Repeat title slide at end of reveal.js presentation](https://stackoverflow.com/questions/76215257/repeat-title-slide-at-end-of-reveal-js-presentation)
- [Tunable title page for slides {#2948}](https://github.com/quarto-dev/quarto-cli/discussions/2948)
- [Presentations](https://quarto.org/docs/presentations/)
- Настройка тем:
	- https://www.emilhvitfeldt.com/post/slidecraft-colors-fonts/
	- [Тонкий тюнинг настройки отображения кода](https://www.emilhvitfeldt.com/post/slidecraft-code-output/)
- Для настройки локальных шрифтов (FiraCode) я пошел по другому пути
	- https://github.com/quarto-dev/quarto-cli/discussions/3064
	- https://github.com/gadenbuie/reveal-fonts-reprex
- [Block Code with revealjs {#4943}](https://github.com/quarto-dev/quarto-cli/discussions/4	943)
`.reveal pre.sourceCode code { ...`
- [Slidecraft 101: Code and Output. All about styling code and output in slidecrafting](https://emilhvitfeldt.com/post/slidecraft-code-output/)
- [Change color and background of chunk ouput in Quarto document](https://stackoverflow.com/questions/76610798/change-color-and-background-of-chunk-ouput-in-quarto-document)
Quarto code chunk output is wrapped within a Div with class cell-output. If you want to style specific chunk output, use classes chunk option to assign a class and add/modify css styles for cell-output within that <classes> class.
- [Qarto cell output params](https://quarto.org/docs/reference/cells/cells-knitr.html#cell-output)
- [Quarto: Howto use a custom (Web)font?](https://stackoverflow.com/questions/73659027/quarto-howto-use-a-custom-webfont)

## Quarto tweaks
- Quarto. [R htmltools browsable HTML does not view without explicit `print()`](https://stackoverflow.com/questions/75353004/r-htmltools-browsable-html-does-not-view-without-explicit-print)
- [How to add HTML code to a Quarto website?](https://stackoverflow.com/questions/74445505/how-to-add-html-code-to-a-quarto-website)
`{=html}`
- [Quarto HTML Code Blocks](https://quarto.org/docs/output-formats/html-code.html)
- [How to change code block height and width in quarto presentation](https://github.com/quarto-dev/quarto-cli/discussions/	2073)
- [Quarto r set max height for text output or figures](https://stackoverflow.com/questions/75204803/quarto-r-set-max-height-for-text-output-or-figures)
- [Custom Quarto Project Types](https://quarto.org/docs/extensions/project-types.html)
- [Metadata Merging](https://quarto.org/docs/projects/quarto-projects.html#metadata-includes).
Metadata defined within `_quarto.yml`, `_metadata.yml`, and document-level YAML options are merged together.
	- [Metadata Includes](https://quarto.org/docs/projects/quarto-projects.html#metadata-includes)
You might find it convenient to break your metadata into multiple files. You can do this using the metadata-files option. For example, here we include some website options within a `_quarto.yml`
- [How can I use inline code in a quarto document?](https://community.rstudio.com/t/how-can-i-use-inline-code-in-a-quarto-document/160575)
- [Quarto pr's](https://rpubs.com/rich_i/quarto-prs-issues)
- [Quarto Dates and Date Formatting](https://quarto.org/docs/reference/dates.html)
	- [Custom date for Quarto YAML header pdf document](https://stackoverflow.com/questions/75315010/custom-date-for-quarto-yaml-header-pdf-document)
- [How do I increase the width of the content column in Quarto](https://stackoverflow.com/questions/73611184/how-do-i-increase-the-width-of-the-content-column-in-quarto)
- [Quarto Project specify port for localhost](https://stackoverflow.com/questions/75715950/quarto-project-specify-port-for-localhost)
```
project:    
     preview: 
       port: 4200
```
- [Project specify port for localhost {#8965}](https://github.com/quarto-dev/quarto-cli/issues/8965)
- [Why does quarto preview always choose a new port? {#2083}](https://github.com/quarto-dev/quarto-cli/discussions/2083)

## Quarto & observable
- [Observable JS](https://quarto.org/docs/interactive/ojs/)
- [Wrangling data in JavaScript with Arquero: a primer for R users](https://observablehq.com/@observablehq/data-wrangling-with-arquero-from-r)
- [Introducing Arquero](https://observablehq.com/@uwdata/introducing-arquero)
- COOL! [Pass R object to Observable in Quarto](https://stackoverflow.com/questions/73873681/pass-r-object-to-observable-in-quarto)
- [Observable Imports in Quarto](https://timelyportfolio.github.io/quarto_tests/examples/quarto_observable_imports/quarto_observable_imports.html)
- [A beginner's guide to using Observable JavaScript, R, and Python with Quarto](https://www.infoworld.com/article/3674789/a-beginners-guide-to-using-observable-javascript-r-and-python-with-quarto.html)
- [Page layout](https://quarto.org/docs/output-formats/page-layout.html#page-layout) позволяет указывать ширины блоков текста.
- [How do I increase the width of the content column in Quarto](https://stackoverflow.com/questions/73611184/how-do-i-increase-the-width-of-the-content-column-in-quarto)
Quarto version 1.3 allows setting the width of the sidebar, the body of the document, the margin of the document, and the margins between these elements (gutters) with sidebar-width, body-width, margin-width, and gutter-width options. Read [Article Grid Customization](https://quarto.org/docs/prerelease/1.3/grid.html#background) from quarto docs for details.
```
format:
  html:
    grid: 
      body-width: 2000px
      sidebar-width: 200px
      margin-width: 200px
    toc: true
```

## Quarto & tables
- quartoExtra. [Table printing demo](https://debruine.github.io/quarto_demo/table.html) by Lisa DeBruine
This code is meant to replicate (and extend) the df_print option in rmarkdown. The code for kable or paged tables is relatively simple, and I have created a more complex function that prints short tables with kableExtra::kable() and longer tables with DT::datatable(). You have to source in the file with the knit_print.data.frame() function for each page in a website or each chapter in a book.
- Размер таблиц тоже надо бы подгонять. Спасает простой html, так говорят: [How to adjust HTML tables width to content in quarto documents?](https://community.rstudio.com/t/how-to-adjust-html-tables-width-to-content-in-quarto-documents/149395)
Add `as_raw_html()` to avoid Quarto modifying the HTML table.
	iris %>% 
	  count(Species) %>% 
	  gt() %>%
	  as_raw_html()
- COOL! [changing font size in R DataTables (DT)](https://stackoverflow.com/questions/44101055/changing-font-size-in-r-datatables-dt)
```
dt_font_size <- "9pt"

mtcars %>%
  DT::datatable(options=list(
    initComplete = htmlwidgets::JS(
      "function(settings, json) {",
      paste0("$(this.api().table().container()).css({'font-size': '", dt_font_size, "'});"),
      "}")
  ))
```
- В quarto таблицы становятся чересполосными. Отключение `opt_row_striping(row_striping = FALSE)` в gt не помогает. Конфликт со стилями quarto.
В частности с `.table`: `--bs-table-striped-bg: rgba(0, 0, 0, 0.05);`
Это вообще общая проблема конфликта стилей.
- [Remove shading from HTML tables generated using Quarto](https://forum.posit.co/t/remove-shading-from-html-tables-generated-using-quarto/183398)
- Тут подробный диалог по способам решения. [Option to disable table striping in computational tables? #6945 {Closed}](https://github.com/quarto-dev/quarto-cli/issues/6945)
As a reminder, you can try opting out Quarto HTML table processing.
You can do that for the whole document, or at the cell level (https://quarto.org/docs/authoring/tables.html#disabling-quarto-table-processing) or even do it at gt level with options quarto.disable_processing (https://gt.rstudio.com/reference/tab_options.html)


## Quarto & word
- [Changing math formulas font size in RPres](https://stackoverflow.com/questions/36531820/changing-math-formulas-font-size-in-rpres/36533612#36533612)
- [changing rmarkdown "table of contents" default title](https://stackoverflow.com/questions/52977363/changing-rmarkdown-table-of-contents-default-title/52978463#52978463)
`toc-title: "INDICE"`

## Quarto & pdf
- [Making Pretty PDFs with Quarto](https://nrennie.rbind.io/blog/making-pretty-pdf-quarto/)
- [Clipped footnotes for PDF print of revealjs #5998 {Open}](https://github.com/quarto-dev/quarto-cli/issues/5998)

## Quarto & html widgets
- ['printing' HTML widgets in programmatically generated Rmarkdown](https://stackoverflow.com/questions/64430375/printing-html-widgets-in-programmatically-generated-rmarkdown)
- [Auto adjust height of widget to screen height {#3191}](https://github.com/quarto-dev/quarto-cli/discussions/3191)
Solved by discovering viewport units!
`widget.layout.height = "100vh"`
Or to account for the already occupied screen real estate, in my case a 90 pixel high header:
`widget.layout.height = "calc(100vh - 90px)"`
- COOL! [HTML block](https://mine-cetinkaya-rundel.github.io/quarto-tip-a-day/posts/12-html-block/). Want to embed an iframe on a webpage or a slide deck? Plop the sharing code in a raw html block!
- [Quarto Report Example With Plotly and Trelliscopejs](https://jauntyjjs.github.io/Trelliscopejs_In_Quarto_Example/)
- [TrelliscopeJS with Plotly](https://ryanhafen.com/blog/trelliscopejs-plotly/)

## Quarto & Shiny
- COOL! [Combining Shiny and Quarto. A love story.](https://rappa.shinyapps.io/shiny_quarto/)
- COOL! [Quarto Dashboards](https://quarto.org/docs/dashboards/)


## RMarkdown & knitr
- COOL! [Meta RMarkdown - Taxonomy and Use cases](https://themockup.blog/posts/2020-07-25-meta-rmarkdown/)
	- "Higher, further, faster with Marvelous R Markdown - @thomas_mock" [Slides](bit.ly/marvelRMD)
- COOL! [R Markdown CmdStan Engine](https://mc-stan.org/cmdstanr/articles/r-markdown.html). Mikhail Popov
- COOL! [Useful YAML options for generating HTML reports in R](https://scienceloft.com/technical/useful-yaml-options-for-generating-html-reports-in-r/)
	- [knitr in a knutshell. Knitr with R Markdown](http://kbroman.org/knitr_knutshell/pages/Rmarkdown.html)
- [Nice tables when knitting to Word](https://community.rstudio.com/t/nice-tables-when-knitting-to-word/3840/4)
- [kableExtra and Word](https://haozhu233.github.io/kableExtra/kableExtra_and_word.html) by Hao Zhu, 2018-01-09
- COOL! [How to format kable table when knit from .rmd to Word (with bookdown)](https://stackoverflow.com/questions/47704329/how-to-format-kable-table-when-knit-from-rmd-to-word-with-bookdown)
	- The huxtable package is available. It includes similar table customization tools as kableExtra. huxtable is designed to output to LaTeX/PDF and HTML (similar to kableExtra). However, huxtable also includes a as_flextable function to convert a huxtable object to a flextable object, which can be output to Word (as noted by David above). After a lot of searching, it seems to me like huxtable is the only available package that can easily output to all of Word, HTML, and PDF with a single package.
	- This was not possible but since pandoc V2 is out, you can do it with package flextable (>= 0.4.0)(and pandoc V2). Below the code you should add into a code chunk
- COOL! [Create Awesome HTML Table with knitr::kable and kableExtra](https://cran.r-project.org/web/packages/kableExtra/vignettes/awesome_table_in_html.html) by Hao Zhu 2018-05-21
- COOL! [Huxtable](https://hughjonesd.github.io/huxtable/) is an R package to create LaTeX and HTML tables, with a friendly, modern interface. Features include control over text styling, number format, background color, borders, padding and alignment. Cells can span multiple rows and/or columns. Tables can be manipulated with standard R subsetting or dplyr functions.
- COOL! [The flextable package](https://davidgohel.github.io/flextable/) provides a framework for easily create tables for reporting. Tables can be embedded within: R Markdown documents, Microsoft Word or PowerPoint documents
- COOL! [A few methods for making tables in rmarkdown](https://rpubs.com/benmarwick/tables-rmarkdown)
- [Recommendations for Using summarytools With Rmarkdown](https://cran.r-project.org/web/packages/summarytools/vignettes/Recommendations-rmarkdown.html)
- Comments in R Markdown
	- [Comments in bookdown](https://community.rstudio.com/t/comments-in-bookdown/6808)
	- [How do I comment out text in an RMD file?](https://stackoverflow.com/questions/17046518/how-do-i-comment-out-text-in-an-rmd-file)
- COOL! [Tips and tricks for working with images and figures in R Markdown documents](http://www.zevross.com/blog/2017/06/19/tips-and-tricks-for-working-with-images-and-figures-in-r-markdown-documents/)
- COOL! Применение пакета printr! [Automatic output format in Rmarkdown](Automatic output format in Rmarkdown)
- Плавающий TOC: См. раздел [Floating TOC](http://rmarkdown.rstudio.com/html_document_format.html). А целый сайт с навигацией делается уже из набора Rmd-документов: http://rmarkdown.rstudio.com/rmarkdown_websites.html
- RMarkdown & Knitr
	- [insert portions of a markdown document inside another markdown document using knitr](https://stackoverflow.com/questions/17593912/insert-portions-of-a-markdown-document-inside-another-markdown-document-using-kn).
```
1. that is what the chunk option child is for, e.g. in second.Rmd, you can
``{r child='first.Rmd'}
``
2. that is a little bit trickier, but you can call knit_child() manually, e.g.
``{r echo=FALSE, results='asis'}
# knit the first three lines of first.Rmd
cat(knit_child(text = readLines('first.Rmd')[1:3]), sep = '\n')
``
```
	- [How to combine two RMarkdown (.Rmd) files into a single output?](https://stackoverflow.com/questions/25824795/how-to-combine-two-rmarkdown-rmd-files-into-a-single-output)
	- [Chunk options and package options](https://yihui.name/knitr/options/#child-documents). 2017-02-03
- При публикации в PDF файла RMarkdown, содержащего HTML элементы, компиляция ломается с сообщением "HTML output in non-HTML formats by adding this option to the YAML front-matter of your rmarkdown file:
always_allow_html: yes". Отчасти этот вопрос обсуждается здесь: хrendering to md_document results in error if code generates HTML #516  {Closed}](https://github.com/rstudio/rmarkdown/issues/516)
- [R Markdown for documents with logos, watermarks, and corporate styles](http://ellisp.github.io/blog/2017/09/09/rmarkdown)
	- [Demonstration page of R Markdown in combination with corporate theming](http://ellisp.github.io/presentations/rmarkdown-styled-demo.html)
- COOL! [Creating nice tables using R Markdown](https://chesterismay.wordpress.com/2015/11/17/nice-tables-using-r-markdown/)
- [Specify height and width of ggplot graph in Rmarkdown knitr output](https://stackoverflow.com/questions/39634520/specify-height-and-width-of-ggplot-graph-in-rmarkdown-knitr-output). `fig.width`, `fig.height`. Figure sizes are specified in inches and can be included as a global option of the document output format. Default is 7x5
- Когда пытаюсь опубликовать kable с указанием caption, название постоянной части "Таблица" дает ошибку при компиляции на строне Connect:
```
 ! LaTeX Error: Command \CYRT unavailable in encoding EU1.

See the LaTeX manual or LaTeX Companion for explanation.
Type  H <return>  for immediate help.
 ...

l.118 \caption{Longtable}
```
Решение указано здесь: [Russian language within figure captions in unicode-aware systems {duplicate}](https://tex.stackexchange.com/questions/110013/russian-language-within-figure-captions-in-unicode-aware-systems).
Симптоматика описана также здесь: [Cyrillic word error in Figure Captions](https://tex.stackexchange.com/questions/351510/cyrillic-word-error-in-figure-captions)
- Детали по правильному применению рецепта: [\renewcommand\tablename{name} does not work](https://tex.stackexchange.com/questions/55090/renewcommand-tablenamename-does-not-work)
```
\AtBeginDocument{%
  \renewcommand\tablename{new}
}
```
- [RMarkdown сhunk options and package options](https://yihui.name/knitr/options/)
- COOL! [One Little Thing: the knitr Chunk Option include=FALSE](https://yihui.name/en/2017/11/knitr-include-false/) by Yihui Xie, 2017-11-22
- [How to make tables float in Rmarkdown pdf document/Inserting tables causing text to disappear in pdf output](http://stackoverflow.com/questions/41705848/how-to-make-tables-float-in-rmarkdown-pdf-document-inserting-tables-causing-text)
- [Moving from Beamer to R Markdown](http://rmarkdown.rstudio.com/articles_beamer.html)
- [Simple manual RMarkdown tables that look good in HTML, PDF and DOCX](http://stackoverflow.com/questions/19997242/simple-manual-rmarkdown-tables-that-look-good-in-html-pdf-and-docx)
- [A few methods for making tables in rmarkdown](https://rpubs.com/benmarwick/tables-rmarkdown)
- [How to include LaTeX package in R Markdown?](https://tex.stackexchange.com/questions/171711/how-to-include-latex-package-in-r-markdown)
- [Knitr with R Markdown](http://kbroman.org/knitr_knutshell/pages/Rmarkdown.html). Полезный пункт  **Converting R Markdown to html**:
	- Via RStudio
	- Via the command line (or GNU make)
`R -e "rmarkdown::render('knitr_example.Rmd')"`
- Помощь по командам, ассоциированных с pandoc: `?rmarkdown::pandoc_available`
- Проблема с кодировкой pdf файла решается заданием параметра `encoding`:  `R -e "rmarkdown::render('ru-tex-pdf-examples.Rmd', encoding = 'UTF-8')"`
- Как включить в YAML заголовок r код? Решение вполне простое и элегантное: '`r format(Sys.Date(), "%B %d, %Y")`'. Детали смотрим здесь:
	- [YAML current date in rmarkdown](http://stackoverflow.com/questions/23449319/yaml-current-date-in-rmarkdown)
	- [Using R markdown and knitr: Possible to get R objects interpreted in YAML](http://stackoverflow.com/questions/25813420/using-r-markdown-and-knitr-possible-to-get-r-objects-interpreted-in-yaml)
	- [Inline R code in YAML for rmarkdown doesn't run](http://stackoverflow.com/questions/32637340/inline-r-code-in-yaml-for-rmarkdown-doesnt-run)
- [Interactive Documents: Advanced Topics. Shiny Reactives](http://rmarkdown.rstudio.com/authoring_shiny_advanced.html)
- [Using Arial in R figures destined for PLOS ONE](http://www.fromthebottomoftheheap.net/2013/09/09/preparing-figures-for-plos-one-with-r/)
- [liberation-fonts](https://pagure.io/liberation-fonts). The Liberation Fonts are intended to be replacements for the three most commonly used fonts on Microsoft systems: Times New Roman, Arial, and Courier \ New.
- Проблема со шрифтами при генерации pdf... [Error in grid.Call(L_textBounds, as.graphicsAnnot(x$label), x$x, x$y, : Polygon edge not found](http://stackoverflow.com/questions/10581440/error-in-grid-calll-textbounds-as-graphicsannotxlabel-xx-xy-polygon)
	- [RMarkdown PDF Documents](http://rmarkdown.rstudio.com/pdf_document_format.html)
	- COOL!!!! Для PDF решение кроется в строчке `knitr::opts_chunk$set(dev='cairo_pdf') # решили проблему с генерацией русского текста в графиках`. Но тогда мы получаем проблему с отображением графики в html.
	- Closed Ticket # 111: [Set knitr figure device `dev` by output type?](https://github.com/rstudio/rmarkdown/issues/111). Seconding this. I'd like to be able to set cairo_pdf for PDF output but svg for HTML outputs, like so:
```
output:
  pdf_document:
    dev: cairo_pdf
  html_document:
    dev: svg
```
- [Automatically scale font size (etc.) of ggplot2 inside an Rmarkdown document](http://stackoverflow.com/questions/28835491/automatically-scale-font-size-etc-of-ggplot2-inside-an-rmarkdown-document)
- COOL presentation. [Advanced R Markdown. Behind the Knit Button](https://slides.yihui.name/2017-rstudio-conf-rmarkdown-Yihui-Xie.html#1) by Yihui Xie, RStudio
- [Error creating notebook: non-numeric argument to binary operator; RStudio](https://stackoverflow.com/questions/45024350/error-creating-notebook-non-numeric-argument-to-binary-operator-rstudio).
Мне помогло вытирание кэша в `... \jira-nlp\.Rproj.user\shared\notebooks\160C43F1-jira_analysis`
- Очень много полезных способов по включению таблиц и картинок в Rmd. [Insert picture/table in R Markdown](https://stackoverflow.com/questions/25166624/insert-picture-table-in-r-markdown)
- Темы для R Markdown
	- RSTUDIO::CONF 2020. [Styling Shiny apps with Sass and Bootstrap 4](https://rstudio.com/resources/rstudioconf-2020/styling-shiny-apps-with-sass-and-bootstrap-4/) Joe Cheng | January 30, 2020
	- [bootstraplib](https://rstudio.github.io/bootstraplib/) Tools for styling shiny and rmarkdown from R via Bootstrap (3 or 4) Sass.
	- [One R Markdown Document, Fourteen Demos](https://rstudio.com/resources/rstudioconf-2020/one-r-markdown-document-fourteen-demos/) Yihui Xie
	- [Fast Rmarkdown Theming with thematic and bootstraplib](https://www.tillac-data.com/2020-fast-rmd-theming-with-thematic-and-bootstraplib/) Publish date: 2020-06-05
Theming in Rmarkdown can be hard. You first made some custom CSS or use a provided theme but your figures didn’t change and you have to style your ggplot2 theme. And after it you change your mind (or your boss do) and you need to move this color shade to lighter one. So you change your theme, but forgot to change it in all your CSS and something is going wrong. Same goes for fonts
- COOL! [RMarkdown Driven Development: the Technical Appendix](https://emilyriederer.netlify.app/post/rmddd-tech-appendix/)
- Dynamic chunk sizes:
	- Проблема:
@BrandonBertelsen I understand that, but knitr has to open the graphical device (with an appropriate size) before evaluating the chunk, so you have to evaluate the code in a previous chunk in order to use the objects in a latter chunk. – Yihui Xie Mar 12 '13 at 16:09
	- COOL! [How to Change fig.width and fig.height Dynamically Within an R Markdown Chunk](http://michaeljw.com/blog/post/subchunkify/)
	- [Dynamic height and width for knitr plots](https://stackoverflow.com/questions/15365829/dynamic-height-and-width-for-knitr-plots)
	- [dynamically-generate-rmarkdown-chunks-to-display-datatable](https://gist.github.com/StevenMMortimer/e54ec050d97d79996189)
	- [Figure size in R Notebook document](https://support.rstudio.com/hc/en-us/community/posts/213106048-Figure-size-in-R-Notebook-document)
- [Creating Dynamic Documents with RMarkdown and Knitr](http://rpubs.com/ivim/Rmd-v1)
- COOL! [Demo: {crosstalk} materials for a talk at EARL London 2018](https://github.com/matt-dray/earl18-crosstalk)
- [Crosstalk](https://rstudio.github.io/crosstalk/). Crosstalk is an add-on to the htmlwidgets package. It extends htmlwidgets with a set of classes, functions, and conventions for implementing cross-widget interactions (currently, linked brushing and filtering).
- [crosstalk Tutorial](https://emilyriederer.github.io/demo-crosstalk/tutorial/tutorial-rmd.html). This tutorial will help you learn to use the crosstalk package to link different htmlwidgets. After completing this tutorial, you will be able to build an application like the one below, which visualizes the number of rides at a sample of Chicago train stations in 2019 versus 2020.
- [Filter two tables with crosstalk](https://stackoverflow.com/questions/48581598/filter-two-tables-with-crosstalk)
- COOL! [How I share knowledge around R Markdown](https://themockup.blog/posts/2020-07-25-meta-rmarkdown/). A meta collection of some R Markdown strategies.
- COOL! Slides. [Making Websites in R Markdown](http://arm.rbind.io/slides/blogdown.html#1). Alison Hill | rstudio::conf | 2019-01-15
- COOL! [How I Teach R Markdown](https://alison.rbind.io/post/2020-05-28-how-i-teach-r-markdown/) by Alison Hill
- [Distill for R Markdown](https://rstudio.github.io/distill/). Scientific and technical writing, native to the web
- [Different ways to set figure size in RMarkdown](https://sebastiansauer.github.io/figure_sizing_knitr/)
- COOL! [pagedown: Create Paged HTML Documents for Printing from R Markdown](https://pagedown.rbind.io/). A Less Traveled Road to PDF and Printing
- COOL! [Access to chunk label #73 {Closed}](https://github.com/yihui/knitr/issues/73). Now you can use `knitr::opts_current$get("label")` to get the label for the current chunk. Any other options are also accessible via this object `opts_current`.
- Комментируем часть текста в rmarkdown: [4.17 Comment out text](https://bookdown.org/yihui/rmarkdown-cookbook/comments.html). [Comment out some chunks/part of Rmd file](https://stackoverflow.com/questions/46148097/comment-out-some-chunks-part-of-rmd-file)
- Compiling Rscript with knit
	- [3.3 Render an R script to a report](https://bookdown.org/yihui/rmarkdown-cookbook/spin.html)
	- [3.4 Convert R Markdown to R script](https://bookdown.org/yihui/rmarkdown-cookbook/purl.html)
- [Shiny Inception: JavaScript in Rendered Markdown](https://datawookie.dev/blog/2021/06/shiny-inception-javascript-in-rendered-markdown/)
- COOL! [Displaying verbatim code chunks in RMarkdown and Xaringan presentations](https://themockup.blog/posts/2021-08-27-displaying-verbatim-code-chunks-in-xaringan-presentations/)
- [Automatic execution of setup chunk in Rmd](https://community.rstudio.com/t/automatic-execution-of-setup-chunk-in-rmd/71483)
- Интересный момент, который ранее не замечал. Если в проекте Rmd-файл лежит не в корне, то код из .Rprofile не подгружается при генерации файла через кнопку knit. Надо юзать 
`source(here::here(".Rprofile"), chdir = TRUE)`
- COOL! [suppress console output in r markdown, but keep plot](https://stackoverflow.com/questions/30810476/suppress-console-output-in-r-markdown-but-keep-plot). Simply having  
`{r, results = 'hide'}` or  `{r, results = FALSE}` for your chunk options suppresses R output but not warnings, messages or errors. No extra functions are needed.
More details can be found here. https://yihui.org/knitr/options/#text-output
- [R markdown df_print options](https://stackoverflow.com/questions/40893742/r-markdown-df-print-options). `knitr::opts_chunk$set(echo = TRUE, rows.print=25)`
- [Rmarkdown. 7.3 Style code blocks and text output](https://bookdown.org/yihui/rmarkdown-cookbook/chunk-styling.html)

## knitr
- Jumping Rivers blog
	- [Part 1: Specifying the correct figure dimension in {knitr}](https://www.jumpingrivers.com/blog/knitr-rmarkdown-image-size/)
	- [Part 2: What image format should you use for graphics](https://www.jumpingrivers.com/blog/knitr-image-png-jpeg-svg-rmarkdown/)
	- [Part 3: Including external graphics in your document](https://www.jumpingrivers.com/blog/knitr-include-graphics-external/)
	- [Part 4: Default knitr options and hooks](https://www.jumpingrivers.com/blog/knitr-default-options-settings-hooks/)
- [How to merge code and output in chunks results ? #131 {Closed}](https://github.com/yihui/rmarkdown-cookbook/issues/131)
`knitr::opts_chunk$set(echo=TRUE, message=FALSE, warning=FALSE, results='hold')`
- COOL! [How to request an early exit when knitting an Rmd document?](https://stackoverflow.com/questions/33705662/how-to-request-an-early-exit-when-knitting-an-rmd-document).
`knitr::knit_exit()` for figuring out where the deeply broken thing is by bisecting your Rmd
- [14.7 Use `knitr::knit_expand()` to generate Rmd source](https://bookdown.org/yihui/rmarkdown-cookbook/knit-expand.html)
- Вот такую ерунду получаем, видимо, при динамической компиляции сгенерированного кода. [R Markdown won't Knit](https://community.rstudio.com/t/r-markdown-wont-knit/34627/3)
- [In grepl("\n", lines, fixed = TRUE) : input string 1 is invalid in this locale #396](https://github.com/swirldev/swirl/issues/396)
- [Run RMarkdown with arguments on the command line](https://stackoverflow.com/questions/49904943/run-rmarkdown-with-arguments-on-the-command-line)
`Rscript -e "rmarkdown::render('example.Rmd',params=list(args = myarg))"`
- [Pandoc version 1.12.1502 or higher required](https://community.rstudio.com/t/pandoc-version-1-12-1502-or-higher-required/28870).
This variable should be set in RStudio `Sys.getenv("RSTUDIO_PANDOC")`
- [Setting and getting Windows environment variables from the command prompt?](https://superuser.com/questions/79612/setting-and-getting-windows-environment-variables-from-the-command-prompt/79614)




## knitr. Запускаем Rmd -> PDF
Смотрим ссылки ниже. Важный концепт, который держим в голове -- возможность генерации отчетов из .R файлов (не .Rmd) посредством `spin`. `rmarkdown::render()` автоматически выбирает spin\knit в зависимости от расширения файла.
- При компиляции в PDF возникает ошибка `! Package inputenc Error: Unicode char Рѕ (U+43E)`. Ищем ответы здесь: [Package inputenc Error: Unicode char \u8 in RStudio](http://stackoverflow.com/questions/32794157/package-inputenc-error-unicode-char-u8-in-rstudio)
- Компиляция .tex ломается на команде '\href{}' при `inputenc=utf8` и `fontencoding=T2A`
- [Knit PDF and la-tex (russian text)](http://qa.piterdata.ninja/p/1742/). Тут много полезного про управление опциями в заголовке самого документа.
- Попытка включить T2A шрифты (видимо, так) приводит к такой ошибке: `pdfTeX error (font expansion): auto expansion is only possible with scalable fonts. \AtBegShi@Output ...ipout \box \AtBeginShipoutBox`
- Как обычно, мучаемся с русскими шрифтами в LaTeX в PDF. [Установка PSCyr для Latex](http://blog.harrix.org/article/444)
- Русские буквы, используем XeLaTeX:
```
    latex_engine: xelatex
header-includes:
 \usepackage[T2A]{fontenc}
 \usepackage[utf8]{inputenc}
 \usepackage[russian]{babel}
 \usepackage{fontspec}
 \setmainfont{Cambria}
```
- Проблема с отображением русских букв на графиках. Ошибки подобного рода:
	- Warning in title(...): неизвестна ширина символа 0xf2
	- Warning in grid.Call(L_textBounds, as.graphicsAnnot(x$label), x$x, x$y, : неизвестна ширина символа 0xf0
	- Warning in grid.Call(L_stringMetric, as.graphicsAnnot(x$label)): неизвестны шрифтовые метрики для символа 0xe
Нашел очень подробный багтрекер на эту тему в репозитории knitr: [[R Sweave] Cyrillic characters in plots #436](https://github.com/yihui/knitr/issues/436). Также полезно почитать про механику генерации графиков в идеологии knitr в книге "Dynamic Documents with R anf knitr, 2nd edition". Концепции Graphical Device, Encoding, Plot Recording (п. 7.1, 7.2). Рекомендуют использовать cairo_pdf, в т.ч. в книге (п 7.2).
В принципе, решение указывать в chunk опцию `dev="cairo_pdf"` срабатывает.
- Нюансы с подключением доп пакетов и стилей в R markdown имеют несколько решений. Примеры решений, например, в этой подборке:
	- [How to include LaTeX package in R Markdown?](http://tex.stackexchange.com/questions/171711/how-to-include-latex-package-in-r-markdown)
	- [R markdown: PDF Documents. Overview](http://rmarkdown.rstudio.com/pdf_document_format.html)
- Много полезных примеров в [Knitr with R Markdown by Karl Broman](http://kbroman.org/knitr_knutshell/pages/Rmarkdown.html)
- Читаем подробненько про схему работы knitr также в [Introduction to knitr by Michael Sachs](https://sachsmc.github.io/knit-git-markr-guide/knitr/knit.html)
- [MarkdownReports. An R function library to generate (scientific) reports easily](http://markdownreports.github.io/). MarkdownReports is a set of R functions that allows you to generate precise figures easily, and create clean reports about what you just discovered with your analysis script.
- [Programmatically creating Markdown tables in R with KnitR](http://stackoverflow.com/questions/15488350/programmatically-creating-markdown-tables-in-r-with-knitr)
- Весьма нетривиальный вопрос, а как же сделать комментарии в R markdown. В ответе [Comments in Markdown](http://stackoverflow.com/questions/4823468/comments-in-markdown) рассмотрена масса различных варианты для markdown в целом.
- [How do I insert a comment in Markdown?](https://www.quora.com/How-do-I-insert-a-comment-in-Markdown)
- Размышления про различные директории. [Working with knitr using subdirectories](http://stackoverflow.com/questions/24585254/working-with-knitr-using-subdirectories)
- Dean Attali.
	- [Knitr's best hidden gem: spin](http://deanattali.com/2015/03/24/knitrs-best-hidden-gem-spin/). Stop knitting & start spinning - spin can help you write reports much faster and avoid repeating yourself
	- [ezknitr: R package to avoid the typical working directory pain when using knitr](http://deanattali.com/blog/ezknitr-package/)
- [Compiling Reports from R Scripts](http://rmarkdown.rstudio.com/articles_report_from_r_script.html)
- [Rmarkdown and DT: result do not render](http://stackoverflow.com/questions/33343241/rmarkdown-and-dt-result-do-not-render)
- [Is it possible to have sortable(Interactive) table in rMarkdown?](http://stackoverflow.com/questions/27120002/is-it-possible-to-have-sortableinteractive-table-in-rmarkdown)
- [Howto include js dependencies of DT datatable in Rmarkdown using knitr and pandoc](http://stackoverflow.com/questions/28303827/howto-include-js-dependencies-of-dt-datatable-in-rmarkdown-using-knitr-and-pando)
- [Programmatically creating Markdown tables in R with KnitR](http://stackoverflow.com/questions/15488350/programmatically-creating-markdown-tables-in-r-with-knitr)
- [An Introduction to The printr Package](http://yihui.name/printr/)
- [My table looks better than yours](https://www.stat.ubc.ca/~jenny/STAT545A/topic10_tablesCSS.html)
- [pander: An R Pandoc Writer](http://rapporter.github.io/pander/)
- [R Code Chunks](http://rmarkdown.rstudio.com/authoring_rcodechunks.html)
- COOL! [Render reports directly from R scripts](http://brooksandrew.github.io/simpleblog/articles/render-reports-directly-from-R-scripts/)
	- [A collection of css themes for Markdown http://jasonm23.github.io/markdown-css-themes/](https://github.com/jasonm23/markdown-css-themes)
	- [Markdown css themes Preview](http://jasonm23.github.io/markdown-css-themes/)
- [Two html tables with different formats](https://community.rstudio.com/t/two-html-tables-with-different-formats/5144)
- [Create Awesome LaTeX Table with knitr::kable and kableExtra](https://haozhu233.github.io/kableExtra/awesome_table_in_pdf.pdf)
- [Using knitr and pandoc to create reproducible scientific reports](http://galahad.well.ox.ac.uk/repro/)
- [The write2 function](https://cran.r-project.org/web/packages/arsenal/vignettes/write2.html)
- COOL! Положил в Evernote. [In `knitr` how can I test for if the output will be PDF or word?](https://stackoverflow.com/questions/35144130/in-knitr-how-can-i-test-for-if-the-output-will-be-pdf-or-word)
- COOL! [Error with RMarkdown: 'is_latex_output' is not an exported object from 'namespace:knitr' #1272 {Closed}](https://github.com/rstudio/rmarkdown/issues/1272)
- [Prerendered Shiny Documents](https://rmarkdown.rstudio.com/authoring_shiny_prerendered.html). Overview
- Chunks timing
	- [How to print RMarkdown code chunk execution times? {duplicate}](https://stackoverflow.com/questions/43434239/how-to-print-rmarkdown-code-chunk-execution-times)
	- [Timing for chunks?](https://stackoverflow.com/questions/24595280/timing-for-chunks)
	- [Hook to time knitr chunks](https://stackoverflow.com/questions/30530008/hook-to-time-knitr-chunks). Try this:
```
            local({
              now = Sys.time()
              knit_hooks$set(timeit = function(before) {
                if (before) {
                  now <<- Sys.time()
                } else {
                  x = round(Sys.time() - now, digits = 3)
                  x = sprintf("%% Chunk rendering time: %s seconds.", x)
                  paste('\\end{kframe}\n', x, '\n\\begin{kframe}')
                }
              })
            })
```
- [2.6 R code chunks and inline R code](https://bookdown.org/yihui/rmarkdown/r-code.html)
- [Troubleshooting: Printing UTF-8 (Russian) in R-markdown, knitr](https://bookdown.org/gorodnichy/utf8-markdown-problem/utf8-markdown-problem.html)
- [Escaping % symbol when passed as a string from R chunk to knitr](https://tex.stackexchange.com/questions/430376/escaping-symbol-when-passed-as-a-string-from-r-chunk-to-knitr)
- [How to escape a pipe char in a code statement in a markdown table?](https://stackoverflow.com/questions/17319940/how-to-escape-a-pipe-char-in-a-code-statement-in-a-markdown-table)
- [how to render DT::datatables in a pdf using rmarkdown?](https://stackoverflow.com/questions/44543858/how-to-render-dtdatatables-in-a-pdf-using-rmarkdown)
- [How to merge and print multiple code chunks in RMarkdown?](https://stackoverflow.com/questions/52952797/how-to-merge-and-print-multiple-code-chunks-in-rmarkdown)
- [Bonus knitr and R markdown functionality. Add multiple images at a time](http://www.zevross.com/blog/2017/06/19/tips-and-tricks-for-working-with-images-and-figures-in-r-markdown-documents/#bonus-knitr-and-r-markdown-functionality)
- [widgetframe and knitr](https://cran.r-project.org/web/packages/widgetframe/vignettes/widgetframe_and_knitr.html)
- [Add an image to a table-like output in R](https://stackoverflow.com/questions/25106481/add-an-image-to-a-table-like-output-in-r)
- [How to set size for local image using knitr for markdown?](https://stackoverflow.com/questions/15625990/how-to-set-size-for-local-image-using-knitr-for-markdown)
- [Allow sql-code-chunk-results to be collected and stored in an R object #1236 {Closed}](https://github.com/rstudio/rmarkdown/issues/1236)


## knitr textwidth
- xaringan. [Font size of code {#69}](https://github.com/yihui/xaringan/issues/69)
- [5.3 Control the width of text output](https://bookdown.org/yihui/rmarkdown-cookbook/text-width.html)
- `fig-align` в YAML header не срабатывает в Quarto, а в чанках срабатывает... пока непонятно почему.
- [align multiple figures with `fig.align`](https://stackoverflow.com/questions/63731766/align-multiple-figures-with-fig-align)
- [R Markdown Tips: Code, Images, Comments, Tables, and more](https://appsilon.com/r-markdown-tips/amp/)
- knitr [11.7 Hide code, text output, messages, or plots](https://bookdown.org/yihui/rmarkdown-cookbook/hide-one.html)
- [Introducing the {renderthis} package](https://www.jhelvy.com/posts/2022-06-28-introducing-renderthis/)
A brief introduction to the {renderthis} package for rendering {xaringan} slides to different output types (previously called {xaringanBuilder})

## knitr
- [Bookdown. 3.1.6 Data frame printing](https://bookdown.org/yihui/rmarkdown/html-document.html#data-frame-printing)
- [Define an R Markdown output format](https://rmarkdown.rstudio.com/docs/reference/output_format.html)
- [Per-chunk override of global df_print specification: default, kable, tibble, or paged #1403 {Open}](https://github.com/rstudio/rmarkdown/issues/1403) `paged.print = TRUE/FALSE`
- [How to set df_print to tibble in markdown for a single R code chunk](https://stackoverflow.com/questions/51536346/how-to-set-df-print-to-tibble-in-markdown-for-a-single-r-code-chunk)
- [Conditionally display a block of text in R Markdown](https://stackoverflow.com/questions/25407102/conditionally-display-a-block-of-text-in-r-markdown)
- [How to wrap code and the output in markdown (.Rmd)](https://stackoverflow.com/questions/33481271/how-to-wrap-code-and-the-output-in-markdown-rmd).
I had this same issue until I realized that one needs to install the R package `formatR`. Once you install and load this package, use `tidy=TRUE, tidy.opts=list(width.cutoff=60)` in your chunk, or use the following line of code to set it globally:
```
knitr::opts_chunk$set(tidy.opts = list(width.cutoff = 60), tidy = TRUE)
```
- [Chunk options and package options](https://yihui.org/knitr/options/)
- [13.4 Show the chunk header in the output](https://bookdown.org/yihui/rmarkdown-cookbook/show-header.html). Set up a chunk hook named `wrapper` to wrap the chunk output inside the original chunk header and footer.
- COOL! [Generating multiple "blank" .Rmd child files from a list of names in a for loop (or similar)](https://community.rstudio.com/t/generating-multiple-blank-rmd-child-files-from-a-list-of-names-in-a-for-loop-or-similar/115925)
- [16.4 Child documents (*)](https://bookdown.org/yihui/rmarkdown-cookbook/child-document.html)
- [Child documents. Input child files into the main document](https://yihui.org/knitr/demo/child/)
- [A Brief History of R Markdown](https://slides.yihui.org/2021-Brazilian-R-Day.html#1) by Yihui Xie
- [reveal.js PDF Export](https://revealjs.com/pdf-export/). Presentations can be exported to PDF via a special print stylesheet. 

## RMarkdown
- [One Little Thing: The Docco Style with `knitr::rocco()`](https://yihui.org/en/2021/06/knitr-rocco/) A two-column HTML layout to show prose and code side by side
- Learning. [Deploying xaringan Slides: A Ten-Step GitHub Pages Workflow](https://silvia.rbind.io/blog/deploying-xaringan-slides/)

## knitr
- [When using RMarkdown, is there a way to insert images (png), knit and generate and html file that I can email and still show the images?](https://stackoverflow.com/questions/62902381/when-using-rmarkdown-is-there-a-way-to-insert-images-png-knit-and-generate-a)
- [Why should I use the here package when I'm already using projects?](https://malco.io/2018/11/05/why-should-i-use-the-here-package-when-i-m-already-using-projects/)
- [Include Images](https://poldham.github.io/minute_website/images.html)
- [Problems with embedding images in distill blog posts](https://community.rstudio.com/t/problems-with-embedding-images-in-distill-blog-posts/92136)
- [Sometimes you may prefer a certain graphical device to render plots (e.g. PNG), but the journal or stakeholders might request different formats. Кshows how easy it is to produce plots for multiple devices at once using #rmarkdown docs! [Chunk options](https://yihui.org/knitr/options/#plots)
- [Lists are my secret weapon for reporting stats with knitr](https://www.tjmahr.com/lists-knitr-secret-weapon/)
Tidying and splitting model summaries for inline reporting








# ==================================================

# 08.01.2025
- COOL! [Sharing and Remixing content across Revealjs slides with Quarto Includes](https://www.cynthiahqy.com/posts/slides-quarto-includes)
How I reused content and metadata across slides for a multi-day workshop with Quarto.
```
Since all my slides were in different folders, sharing YAML options using the directory metadata file _metadata.yml wasn’t an option. Instead I used the metadata-files: YAML option to share the same _slides.yml file across all of my slides. The only thing I had to be careful about was making sure I got the relative references correct. Even though _slides.yml and the style/ folder were both in the root directory of my repo, I had to use ../style/slides.scss to reference the custom CSS file. This is because the relative links are evaluated from the location of the slides.qmd file (i.e. inside the module folder 01a-hello-quarto/) not the root directory of the repo.
```

# 14.09.2023
## quarto plugins
- [highlightword Extension For Quarto](https://github.com/EmilHvitfeldt/quarto-revealjs-highlightword). Revealjs plugin to highlight specific parts of code.
- [codewindow Extension For Quarto](https://github.com/EmilHvitfeldt/quarto-revealjs-codewindow). Add styled codeblock windows for code.

# 17.07.2023
- [rstudio::conf 2022 Workshop. Getting Started with Quarto](https://rstudio-conf-2022.github.io/get-started-quarto/) by Tom Mock

# 15.07.2023
- [Quarto fails to render htmlwidgets when running {knitr} 1.43 with Error in add_html_caption(): #5702 {Closed}](https://github.com/quarto-dev/quarto-cli/issues/5702)
- [Slide Visibility](https://quarto.org/docs/presentations/revealjs/advanced.html#slide-visibility)
- [Uncounted Slides](https://quarto.org/docs/presentations/revealjs/advanced.html#uncounted-slides)
- [Way to remove slide-number for n^th slide in a revealjs presentation? #5566](https://github.com/quarto-dev/quarto-cli/discussions/5566)
- [In RStudio, how to print tibble in quarto/rmarkdown chunk as in console?](https://stackoverflow.com/questions/74861009/in-rstudio-how-to-print-tibble-in-quarto-rmarkdown-chunk-as-in-console)
- [Code line highlighting in Quarto revealjs presentations](https://www.pipinghotdata.com/posts/2022-05-12-code-line-highlighting-in-quarto-revealjs-presentations/). Three methods make your code lines stand out
- [Making Slides in Quarto with `reveal.js`](https://meghan.rbind.io/blog/quarto-slides/) by Meghan Hall
- [Code location in column layout in Quarto revealjs](https://stackoverflow.com/questions/76414456/code-location-in-column-layout-in-quarto-revealjs)
```{r}
#| output-location: column
#| results: hold
#| echo: true
1:10

10:1 #This should be on the left side
```
- Beamer. [How to change font size for code chunks in Quarto?](https://stackoverflow.com/questions/75891446/how-to-change-font-size-for-code-chunks-in-quarto)- [Slidecraft 101: Code and Output](https://www.emilhvitfeldt.com/post/slidecraft-code-output/). All about styling code and output in slidecrafting.
- [Quarto revealjs: increase relative font size of code chunks](https://stackoverflow.com/questions/75907436/quarto-revealjs-increase-relative-font-size-of-code-chunks)
- [Quarto tips I’ve found around the Web](https://apps.machlis.com/shiny/quartotips/)

# 10.07.2023
- [r inline code not executed? #4855 {Closed}](https://github.com/quarto-dev/quarto-cli/discussions/4855)
- [show quarto-code example in quarto document with inline code](https://community.rstudio.com/t/show-quarto-code-example-in-quarto-document-with-inline-code/155231)
- [6 Productivity Hacks for Quarto](https://posit.co/blog/6-productivity-hacks-for-quarto/)
	- [Write verbatim code chunks with echo: fenced](https://posit.co/wp-content/themes/Posit/public/markdown-blogs/6-productivity-hacks-for-quarto/index.html#write-verbatim-code-chunks-with-echo-fenced)
	- [How to resize image in Quarto revealjs presentation #5701](https://github.com/quarto-dev/quarto-cli/discussions/5701). By default, figures are stretched, meaning the width/height are set by this feature. See two ways to make it work....
EDIT: see https://quarto.org/docs/presentations/revealjs/advanced.html#stretch.
- [Vertical Align of images in Quarto Presentations](https://stackoverflow.com/questions/72941210/vertical-align-of-images-in-quarto-presentations)
```
::: {layout="[[-1], [1], [-1]]"}
![](https://placeholder.pics/svg/200){fig-align="center"}
:::
```
This is an option, though `{.absolute top=50 right=50 width="450" height="250"}`
- [Two columns layout in Quarto](https://stackoverflow.com/questions/74162212/two-columns-layout-in-quarto)
- [How to place *multiple* code chunks side by side in Quarto -> HTML?](https://stackoverflow.com/questions/74543398/how-to-place-multiple-code-chunks-side-by-side-in-quarto-html)
- [How to place code chunks side by side, letting Quarto handle page layout (e.g., mobile vs. desktop)](https://github.com/quarto-dev/quarto-cli/discussions/3423)
You can use a div with the same attribute to layout blocks in this way. For example:

:::{layout-ncol="2"}
```{r}
plot(iris)
```
```{r}
plot(ToothGrowth)
```
:::

# 29.08.2022
## Quarto slides
- COOL! Lesson [Introduction to Reproducible Publications with RStudio. Reproducible & Efficient Methods of Using Code Chunks](https://ucsbcarpentry.github.io/Reproducible-Publications-with-RStudio-Quarto/08-code-chunks/index.html)
- Slides [Intro to Quarto](https://github.com/ivelasq/2022-10-27_intro-to-quarto), 2022-10-27 R-Ladies St. Louis Presentation
- COOL! Meetup [Building a blog with Quarto. RStudio Enterprise Community Meetup](https://github.com/ivelasq/2022-08-30_building-a-blog-with-quarto) Presented by Isabella Velásquez
- [What's new in Quarto {1.4}?](https://cwickham.github.io/whats-new-in-quarto/) by Charlotte Wickham

## Additional Quarto slides
- [stoRy time with Shiny, Quarto, and Google Cloud Run](https://dru.quarto.pub/slides-3f3c/#/section) Write and Illustrate Stories with AI

# 12.09.2022
## Embedding into rmarkdown
- [How to Embed htmlwidgets into Documents](https://communicate-data-with-r.netlify.app/docs/communicate/htmlwidgets-in-documents/)
- [Insert raw html iframe into RMarkdown](https://community.rstudio.com/t/insert-raw-html-iframe-into-rmarkdown/94334)
- [iframes don't work in rmarkdown {#2027} Closed](https://github.com/rstudio/rmarkdown/issues/2027)
- [knitr. 9.3 Embed a web page](https://bookdown.org/yihui/rmarkdown-cookbook/include-url.html)
- COOL! [How to Embed a Google Sheet in a Website](https://www.groovypost.com/howto/embed-a-google-sheet-in-a-website/)
- [Вставка гугл-презентации в Rmarkdown](https://t.me/rlang_ru/111883). нашел способ — если выбрать в меню экспорта publish to web, он вообще выдает iframe
и так можно гуглопрезы в фуллскрине втыкать сразу https://support.google.com/edu/classroom/thread/11104308/how-can-i-share-slides-in-presentation-mode?hl=en
- [8. Add Line Breaks in R Markdown](https://www.dataquest.io/blog/r-markdown-tips-tricks-and-shortcuts/#:~:text=To%20break%20a%20line%20in,spaces%20and%20then%20hit%20return%20.). To break a line in R Markdown and have it appear in your output, use two trailing spaces and then hit return.
- [IFrame Backgrounds](https://quarto.org/docs/presentations/revealjs/#iframe-backgrounds). Embeds a web page as a slide background that covers 100% of the reveal.js width and height.
