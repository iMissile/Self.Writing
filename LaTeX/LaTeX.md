## LaTeX
- COOL! [Differences between LuaTeX, ConTeXt and XeTeX](https://tex.stackexchange.com/questions/36/differences-between-luatex-context-and-xetex)
- [Поддержка \No убрана из babel](https://www.linux.org.ru/forum/general/9583562). 
Вообще да, можно вставить `\newcommand{\No}{\textnumero}` в преамбулу документа и все будет работать.
- [The Russian Language in the babel system , Igor A. Kotelnikov](http://ctan.math.illinois.edu/languages/babel/contrib/russian/russianb.pdf).  ... Since earlier versions babel did not support XeLATEX (at least for some languages including Russian), the polyglossia package was generally recommended in the past for use with XeLATEX as a replacement for babel. Nowadays, babel can be used with any engines, including LATEX, PDFLATEX, LuaLATEX, and XeLATEX. Nevertheless some troubles may occur with some languages which have no promptly updated .ldf files.
- [LaTeX/polyglossia](https://ru.wikibooks.org/wiki/LaTeX/polyglossia)
- [Polyglossia vs Babel](https://tex.stackexchange.com/questions/88481/polyglossia-vs-babel)
- [Polyglossia: An Alternative to Babel for XeLEATEX and LuaLATEX](http://mirrors.ibiblio.org/CTAN/macros/xetex/latex/polyglossia/polyglossia.pdf)
- [How to Write Multilingual Text with Different Scripts in LaTeX](https://www.overleaf.com/latex/examples/how-to-write-multilingual-text-with-different-scripts-in-latex/wfdxqhcyyjxz#.W6D44mj7SUk)
- [Polyglossia ignores my custom hyphenation](https://tex.stackexchange.com/questions/229915/polyglossia-ignores-my-custom-hyphenation)
- [Changing language back and forth with polyglossia](https://tex.stackexchange.com/questions/186156/changing-language-back-and-forth-with-polyglossia)
- Артефакты babel. 'miktex "\bbl@beforestart"'.
- [ShareLaTeX XeLaTeX user guide](https://ru.sharelatex.com/learn/latex/XeLaTeX)
- [Multilingual typesetting on Overleaf using polyglossia and fontspec](https://ru.overleaf.com/learn/latex/Multilingual_typesetting_on_Overleaf_using_polyglossia_and_fontspec)
- [Overleaf's polyglossia package with Cyrillic fonts](https://tex.stackexchange.com/questions/539296/overleafs-polyglossia-package-with-cyrillic-fonts)
```
Package polyglossia Error: The current latin font LiberationMono(0) does not contain the "Cyrillic" script!
(polyglossia)                Please define \cyrillicfont with \newfontfamily command.
```
- [Overleaf: What OTF/TTF fonts are supported via fontspec?](https://www.overleaf.com/help/193-what-otf-slash-ttf-fonts-are-supported-via-fontspec#.W6EG_Gj7SUk)
- [Overleaf: Gallery — Fonts](https://www.overleaf.com/gallery/tagged/fonts#.W6EG-mj7SUk)
- [Overleaf: I have a custom font I'd like to load to my document. How can I do this?](https://www.overleaf.com/help/73-i-have-a-custom-font-id-like-to-load-to-my-document-how-can-i-do-this#.W6EHzGj7SUk)
- В Overleaf Возникли проблемы со шрифтом _PT Sans_:
```
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!
! fontspec error: "font-not-found"
! 
! The font "PT Sans" cannot be found.
! 
! See the fontspec documentation for further information.
! 
! For immediate help type H <return>.
!...............................................  
                                                  
l.18 \setmainfont{PT Sans}
```
	- [TTF fonts are supported via fontspec?](https://www.overleaf.com/learn/latex/Questions/What_OTF/TTF_fonts_are_supported_via_fontspec%3F)
	- [ptsans – PT Sans font and LATEX support](https://ctan.org/pkg/ptsans)
	- [Support package for PT Sans](http://mirror.hmc.edu/ctan/obsolete/fonts/ptsans/doc/fonts/ptsans/ptsans.pdf)
	- [\fontspec all the fonts!](https://www.overleaf.com/articles/slash-fontspec-all-the-fonts/qnsxyhrgjsgs)
	- [I have a custom font I'd like to load to my document How can I do this?](https://www.overleaf.com/learn/latex/Questions/I_have_a_custom_font_I%27d_like_to_load_to_my_document._How_can_I_do_this%3F)
```
Using a custom font
Add the .ttf or .otf file to your project, by clicking on “Add files” on the top of your file list, and then selecting “Upload from > computer”. Browse to your .ttf/.otf files and upload them.
Use the following syntax instead for the \setxxxfont commands:
\setmainfont{[CrimsonText-Regular.ttf]}
or

\setmainfont{CrimsonText}[ 
Extension = .ttf,
UprightFont = *-Regular,
...]
You can also declare a new font family to use it in arbitrary situations:

\newfontfamily{\crimson}{CrimsonText}
[Extension = .ttf, UprightFont = *-Regular, ...]
{\crimson This text uses the CrimsonText font}
```
- [Putting two images beside each other](https://tex.stackexchange.com/questions/148438/putting-two-images-beside-each-other)

## Редакторы картинок для LaTeX:
- [Detexify](http://detexify.kirelabs.org/classify.html)
- [LaTeXDraw](http://latexdraw.sourceforge.net/) is a graphical drawing editor for LaTeX. LaTeXDraw can be used to 1) generate PSTricks code; 2) directly create PDF or PS pictures. LaTeXDraw is developed in Java and thus runs on top of Linux, Windows, and Mac OS X. You need Java 8 to launch LaTeXDraw.
- [Math](https://www.mathcha.io/) Online Mathematics Editor, a fast way to write and share mathematics
- [GeoGebra Math Apps](https://www.geogebra.org/)
Get our free online math tools for graphing, geometry, 3D, and more!
- [TikZEdt](http://www.tikzedt.org/) is a combined WYSIWYG/text editor designed for editing Tikz code.
- COOL! [TikZiT](https://tikzit.github.io/). TikZiT is a super simple GUI editor for graphs and string diagrams. Its native file format is a subset of PGF/TikZ, which means TikZiT files can be included directly in papers typeset using LaTeX. 
- [Yichuan Shen's tikzcd-editor](http://tikzcd.yichuanshen.de/)
- [An Overleaf extension for recognizing symbols](https://latex.net/extexify/)
- [List of TikZ Editor {duplicate}](https://tex.stackexchange.com/questions/80418/list-of-tikz-editor)
- COOL! [LaTeX Graphics using TikZ: A Tutorial for Beginners (Part 2)—Generating TikZ Code from GeoGebra](https://ru.overleaf.com/learn/latex/LaTeX_Graphics_using_TikZ%3A_A_Tutorial_for_Beginners_(Part_2)%E2%80%94Generating_TikZ_Code_from_GeoGebra)
- [GeoGebra. Export to LaTeX (PGF, PSTricks) and Asymptote Tools](https://wiki.geogebra.org/en/Export_to_LaTeX_(PGF,_PSTricks)_and_Asymptote)
- [Need help to export tikz code from geogebra](https://tex.stackexchange.com/questions/445331/need-help-to-export-tikz-code-from-geogebra)

## TikZ
- COOL! e-book [Unlocking LaTeX Graphics](https://latex-graphics.com/)

### TikZ & R
- [tikzDevice](https://daqana.github.io/tikzDevice/). The tikzDevice package provides a graphics output device for R that records plots in a LaTeX-friendly format. 
	- COOL! [tikzDevice v0.12.3](https://stubner.me/2019/08/tikzdevice-v0-12-3/)

1.1
https://texample.net/tikz/examples/angles-quotes/

1.28, 1.29, 1.30 
https://texample.net/tikz/examples/animated-distributions/
https://texample.net/tikz/examples/complex-plane/
https://texample.net/tikz/examples/is-lm-diagram/

- COOL! [TikZ. Gaussian distributions & statistical tests](https://tikz.net/gaussians/)
- [Plotting bell shaped curve in TikZ-PGF](https://tex.stackexchange.com/questions/43610/plotting-bell-shaped-curve-in-tikz-pgf)
- COOL! Отличное решение по позиционированию якорей для прямоугольника (rectangle anchor). [How to establish node-anchor-like points on a (tikz) rectangle path (is there a better method than the one described)?](https://tex.stackexchange.com/questions/47704/how-to-establish-node-anchor-like-points-on-a-tikz-rectangle-path-is-there-a)
- [How to make a label near the corners of a rectangle in Tikz?](https://tex.stackexchange.com/questions/651752/how-to-make-a-label-near-the-corners-of-a-rectangle-in-tikz)
- COOL! [LaTeX course. TikZ](http://uva-fnwi.github.io/LaTeX/extra1/Tikz/)
- [Positioning node on tikz path](https://tex.stackexchange.com/questions/428923/positioning-node-on-tikz-path)
- COOL! [PGF/TikZ Manual](https://tikz.dev/tikz-shapes)
- [Tikz: function and node's position](https://tex.stackexchange.com/questions/160327/tikz-function-and-nodes-position)
- [Define a variable in TikZ](https://tex.stackexchange.com/questions/12859/define-a-variable-in-tikz)
- [How do I use pgfmathdeclarefunction to create define a new pgf function?](https://tex.stackexchange.com/questions/15435/how-do-i-use-pgfmathdeclarefunction-to-create-define-a-new-pgf-function)
- [Specifying the width and height of a tikzpicture](https://tex.stackexchange.com/questions/75449/specifying-the-width-and-height-of-a-tikzpicture)
- [LaTeX - Scale and change aspect ratio of PGFPlots tikzpicture](https://gordonlesti.com/latex-scale-and-change-aspect-ratio-of-pgfplots-tikzpicture/)
- [How to set plot box aspect ratio](https://tex.stackexchange.com/questions/303213/how-to-set-plot-box-aspect-ratio)
- Нашел как позиционировал подпись к оси. [Latex pgfplots loglogaxis scaling](https://stackoverflow.com/questions/35077667/latex-pgfplots-loglogaxis-scaling)
- [pgfplots - How to draw zero line for y (from xmin to xmax) when one uses symbolic x coords?](https://tex.stackexchange.com/questions/192074/pgfplots-how-to-draw-zero-line-for-y-from-xmin-to-xmax-when-one-uses-symboli)
- [PGFPlots how to add a label "0" to the origin](https://tex.stackexchange.com/questions/78763/pgfplots-how-to-add-a-label-0-to-the-origin)
- !!! /pgfplots/every axis x label (style, no value)
/pgfplots/every axis y label (style, no value)
/pgfplots/every axis z label (style, no value)
Used only for x, y, or z labels, respectively and installed after ‘every axis label’.
The initial settings are set by xlabel absolute and its variants (if the initial configuration compat=pre
1.3 is active) or xlabel near ticks which provides the better spacing as it incorporates the tick label
sizes to compute the position.
Attention: These styles will be overwritten by axis x line and/or axis y line. Please remember
to place your modifications after the axis line variations.
- COOL! [tikz, How to define a constant and then use it in drawing {duplicate}](https://tex.stackexchange.com/questions/235444/tikz-how-to-define-a-constant-and-then-use-it-in-drawing)
- [Clipping a path using a node](https://tex.stackexchange.com/questions/46541/clipping-a-path-using-a-node)
- [Strutting around: What's the difference between \strut, \mathstrut and \vphantom?](https://tex.stackexchange.com/questions/41185/strutting-around-whats-the-difference-between-strut-mathstrut-and-vphantom)
- [Connecting 2 coordinates in tikz](https://tex.stackexchange.com/questions/615839/connecting-2-coordinates-in-tikz)
- [How can I force the pgfplots coordinate system and the tikz coordinate system to match and why do they not match by default?](https://tex.stackexchange.com/questions/101166/how-can-i-force-the-pgfplots-coordinate-system-and-the-tikz-coordinate-system-to)
- [Merging plots in TikZ](https://tex.stackexchange.com/questions/113783/merging-plots-in-tikz)



- [How to rotate a pgfplot?](https://tex.stackexchange.com/questions/134904/how-to-rotate-a-pgfplot)
- [Tikz : rotate a fill pattern]()
- [pgfplots mark opacity](https://tex.stackexchange.com/questions/355052/pgfplots-mark-opacity)


### relative positioning & alignment
- [TikZ: Node at same x-coordinate as another node, but specified y-coordinate?](https://tex.stackexchange.com/questions/18389/tikz-node-at-same-x-coordinate-as-another-node-but-specified-y-coordinate)
- [How to get one component of a tikz/PGF coordinate?](https://stackoverflow.com/questions/1588568/how-to-get-one-component-of-a-tikz-pgf-coordinate)
- [Extract x, y coordinate of an arbitrary point on curve in TikZ](https://www.latex4technics.com/?note=17MG)
- [How to add a node in the middle of the line with tikz?](https://tex.stackexchange.com/questions/17136/how-to-add-a-node-in-the-middle-of-the-line-with-tikz)
- [Moving a node a bit](https://tex.stackexchange.com/questions/198831/moving-a-node-a-bit)
- [How to align tikzpicture by their axis?](https://tex.stackexchange.com/questions/522704/how-to-align-tikzpicture-by-their-axis)

### pgf intersection
- [Intersections in PGFplots](https://tex.stackexchange.com/questions/21408/intersections-in-pgfplots)
- [pgf Intersections sample](https://www.latex4technics.com/?note=997UG3)
- [pgf intersections sample 2](https://www.latex4technics.com/?note=2T3T)
- [TikZ, refer to intersection with x-axis](https://tex.stackexchange.com/questions/574555/tikz-refer-to-intersection-with-x-axis)

### filling
- [Filling an Area Between Two Curves](https://latexdraw.com/filling-an-area-between-two-curves/)
- [Hatch a rectangle in TikZ](https://tex.stackexchange.com/questions/54464/hatch-a-rectangle-in-tikz)
- [Latex, PgfPlots - Filling areas under and between curves](https://www.sqlpac.com/en/documents/latex-pgfplots-tikz-filling-areas-under-and-between-curves.html)
- [Fill between and soft clipping doesn't work as expected {duplicate}](https://tex.stackexchange.com/questions/295104/fill-between-and-soft-clipping-doesnt-work-as-expected)
- [Filling an area with a pattern between two curves (without an equation)](https://tex.stackexchange.com/questions/228630/filling-an-area-with-a-pattern-between-two-curves-without-an-equation)
- [Pgfplots: fillbetween, enlargelimits and soft clip have interesting interactions](https://tex.stackexchange.com/questions/449829/pgfplots-fillbetween-enlargelimits-and-soft-clip-have-interesting-interactions)
- [Filling surface between a line and an arc in tikz](https://tex.stackexchange.com/questions/647306/filling-surface-between-a-line-and-an-arc-in-tikz)
- [Warning Tikzfillbetween and change pattern](https://tex.stackexchange.com/questions/411568/warning-tikzfillbetween-and-change-pattern).
	- `'fill between': Could not activate graphics layer 'pre main'. Filled path will be on top of the other ones. Please ensure that 'premain' is somewhere in the layer list (or set '/tikz/fill between/on layer=').`
	EDIT: The warning is fixed by this:
On Preambler:
```
\pgfdeclarelayer{ft}
\pgfdeclarelayer{bg}
\pgfsetlayers{bg,main,ft}
```
On Tikz
```
\tikzfillbetween[of=Consume and Income, on layer=ft]
```

### foreach
- [\foreach not behaving in axis environment](https://tex.stackexchange.com/questions/170664/foreach-not-behaving-in-axis-environment)
- [How to use the Foreach Loop in LaTeX](https://latexdraw.com/how-to-use-the-foreach-loop-in-latex/)


### labelling, also angles
- [Move label of an angle in Tikz](https://tex.stackexchange.com/questions/502638/move-label-of-an-angle-in-tikz)
- [Angle between two vectors tikz LaTeX](https://tex.stackexchange.com/questions/590735/angle-between-two-vectors-tikz-latex)
- [pgfplots: extra x tick; tick length; affecting axis label position](https://tex.stackexchange.com/questions/592056/pgfplots-extra-x-tick-tick-length-affecting-axis-label-position)
- [Label angle with tikz](https://tex.stackexchange.com/questions/20826/label-angle-with-tikz), tzplot package
- [How to label angle](https://www.reddit.com/r/LaTeX/comments/1izgk49/how_to_label_angle/), tkz-euclide package


## Ошибки при запуске TeXLive
- [! LaTeX Error: File `titling.sty' not found. #115](https://github.com/rstudio/bookdown/issues/115)
- LaTeX Error: File 'framed.sty' not found. Решаем установкой [`sudo yum -y install texlive-framed`](https://github.com/rstudio/rmarkdown/issues/39)
- LaTeX Error: File 'titling.sty' not found. Решаем установкой `sudo yum -y install texlive-titling`

Русский язык в LaTeX:
- [Overleaf. Русский язык в LaTeX: XeLaTeX](https://www.overleaf.com/latex/templates/5-dot-2-2-russkii-iazyk-v-latex-xelatex/skfzmvgdgvnk)
- [XeLaTeX или на порядок улучшим качество шрифтов в окончательном pdf](http://astronu.jinr.ru/wiki/index.php/XeLaTeX_%D0%B8%D0%BB%D0%B8_%D0%BD%D0%B0_%D0%BF%D0%BE%D1%80%D1%8F%D0%B4%D0%BE%D0%BA_%D1%83%D0%BB%D1%83%D1%87%D1%88%D0%B8%D0%BC_%D0%BA%D0%B0%D1%87%D0%B5%D1%81%D1%82%D0%B2%D0%BE_%D1%88%D1%80%D0%B8%D1%84%D1%82%D0%BE%D0%B2_%D0%B2_%D0%BE%D0%BA%D0%BE%D0%BD%D1%87%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%D0%BC_pdf)
- Package fontenc Error: Encoding file 't2aenc.def' not found. Решаем установкой [`sudo yum -y install texlive-cyrillic`](http://tex.stackexchange.com/questions/5079/what-is-wrong-with-my-cyrillic-text)
 и `yum install texlive-collection-langcyrillic`
- Font T2A/cmr/m/n/12=larm1200 at 12.0pt not loadable: Metric (TFM) file not found. Ответы ищем в статье [Error in TeX Live – Font … not loadable: Metric (TFM) file not found](http://tex.stackexchange.com/questions/75166/error-in-tex-live-font-not-loadable-metric-tfm-file-not-found). Вариант решения -- ставим все font пакеты: `yum -y install texlive-*font*`
- [Переходим на XeTeX, получаем ошибку `! Corrupted NFSS tables`](http://tex.stackexchange.com/questions/237188/corrupted-nfss-tables)
- pdfLaTeX под Windows дает такую ошибку: ` pdfTeX error (font expansion): auto expansion is only possible with scalable fonts.`. Читаем длинную статью 
[On pdfTeX error (font expansion): auto expansion is only possible with scalable fonts, microtype package](http://tex.stackexchange.com/questions/283960/on-pdftex-error-font-expansion-auto-expansion-is-only-possible-with-scalable).
Есть подозрение, что виноват [в этом пакет `microtype`](http://tex.stackexchange.com/questions/10706/pdftex-error-font-expansion-auto-expansion-is-only-possible-with-scalable). Если его закомментировать в сгенерированном .tex файле, то компиляция проходит, но шрифт светлый и нет bold.
Надо ручками поставить пакет `cm-super`
- [How to set font to Arial throughout the entire document?](http://tex.stackexchange.com/questions/23957/how-to-set-font-to-arial-throughout-the-entire-document)
- COOL! Классный обзор методов. [Cyrillic in (La)TeX](http://tex.stackexchange.com/questions/816/cyrillic-in-latex)
РЕШЕНИЕ С Linux Libertine было найдено ЗДЕСЬ: [fontspec error: “font-not-found”](http://tex.stackexchange.com/questions/266101/fontspec-error-font-not-found).
Ставим `\setmainfont{Linux Libertine O}`, обнаружил с помощью команды `fc-list | grep "Linux Libertine" | grep ".otf"`.
- [Linux Libertine font](http://www.linuxlibertine.org/index.php?id=1&L=1).
	- Ставим под винду
	- Ставим под CentOS командой `sudo yum install linux-liber*`. Фонт найден установленным здесь: `/usr/share/fonts/linux-libertine/LinLibertine_*`
	- А еще есть пакет LaTeX [`libertine`](https://www.ctan.org/tex-archive/fonts/libertine/)
	- [Libertine Font problem with XeLaTeX](http://tex.stackexchange.com/questions/105970/font-problem-with-xelatex)


## Находки с overleaf
`babel` устарел. Теперь используется `polyglossia
```
\documentclass[9pt, compress, xcolor=table]{beamer}

\usetheme{m}

\usepackage{amsmath,amssymb}
\usepackage{booktabs}
\usepackage[scale=2]{ccicons}
\usepackage{minted}
% \usepackage[utf8]{inputenc}
% \usepackage[T2A]{fontenc}
% \usepackage[english, russian]{babel}
%%% For accessing system, OTF and TTF fonts
%%% (would have been loaded by polylossia anyway)
\usepackage{fontspec}
%%% For language switching -- like babel, but for xelatex
\usepackage{polyglossia}
% \setmainfont{PT Sans} % вообще шрифты определяются в теме бимера
% заменим на шрифт, доступный в Overleaf
% https://www.overleaf.com/learn/latex/Questions/I_have_a_custom_font_I%27d_like_to_load_to_my_document._How_can_I_do_this%3F
% \setmainfont{[./fonts/FiraSans-Regular.ttf]}
% \setmainfont{Noto Sans}
\setmainlanguage{russian}
\setotherlanguages{english} %% or other languages

\usepackage{graphicx}
\usepackage{tabu} % https://ru.sharelatex.com/learn/Tables
\DeclareGraphicsExtensions{.pdf,.jpg,.png}
\graphicspath{{../images/}{./images/}}

```
- [How to change paragraph spacing in LaTeX](https://www.overleaf.com/learn/latex/Articles/How_to_change_paragraph_spacing_in_LaTeX)
- [хOptimising very large image files](https://www.overleaf.com/learn/how-to/Optimising_very_large_image_files)
- [Адаптация шаблона отчета о НИР в XeTeX](http://dkhramov.dp.ua/Comp.NIRReportXeTeX#.XbijF5ozaUk)
- [LaTeX: Numero sign ('№') {duplicate}](https://tex.stackexchange.com/questions/40564/latex-numero-sign). `\textnumero`
- [What's the best way to write e-mail addresses?](https://tex.stackexchange.com/questions/268/whats-the-best-way-to-write-e-mail-addresses).
There are a number of things that you can try:
(with the hyperref package):
`\url{email address}`
or more simply (for monospace font):
`\texttt{email address}`
- [\newpage,\clearpage and \cleardoublepage not working](https://tex.stackexchange.com/questions/65698/newpage-clearpage-and-cleardoublepage-not-working/65699). It happens because TeX thinks the page is empty, so `\newpage` is ignored. Use ``\null\newpage instead

## Попытка скомпилировать старые проекты в MikTeX 2019 года
- ошибка `Package hyperref Warning: Option `pagecolor' is not available anymore.`. Это касалось настройки вида гиперссылок для pdf
- `Package caption2 Warning: ****************************************************
(caption2)                THIS PACKAGE IS OBSOLETE
...
New documents should use the regular `caption' package v3.x instead.`
Читаем документацию пакета caption, файл caption-eng.pdf, [репозиторий](https://gitlab.com/axelsommerfeldt/caption)
- `l.15 \hypersetup
                {bookmarksnumbered=true}
? `

## Проблемы MikTeX
- При сборке под win возникла ошибка.
```
! Undefined control sequence.
\grffile@org@Ginclude@graphics ... \set@curr@file
                                                  {#1}\edef \uq@curr@file {\...
```
[Undefined control sequence in \graphics after the latest MikTeX update {#380}](https://github.com/MiKTeX/miktex/issues/380)

## Кавычки и цитаты
- [Typesetting quotations](https://www.overleaf.com/learn/latex/Typesetting_quotations)

## Библиография
- [sort biblatex bibliography by appearance of cites in the document {duplicate}](https://tex.stackexchange.com/questions/116088/sort-biblatex-bibliography-by-appearance-of-cites-in-the-document)
- [Biblatex citation order](https://tex.stackexchange.com/questions/51434/biblatex-citation-order)
- [How do I cite range of references? {duplicate}](https://tex.stackexchange.com/questions/103792/how-do-i-cite-range-of-references?noredirect=1&lq=1). The tags you used suggest that you use `biblatex`. In this case you could use one of the styles anding on `-comp`.
- [JabRef](https://www.jabref.org/) is the real open source bibliography reference manager. It uses BibTeX as its native format. It is an excellent editor for BibTeX files allowing you to perform several actions when dealing with such data.

## Управление с проектами
- [Management in a large project](https://ru.overleaf.com/learn/latex/Management_in_a_large_project)

## Пакеты
- [How to set fontsize of 14pt in article class {duplicate}](https://tex.stackexchange.com/questions/628936/how-to-set-fontsize-of-14pt-in-article-class)
	- Opt 1: `\documentclass[14pt]{extarticle}`
	- Opt 2: With the fontsize package you can set arbitrary sizes and adjust the line spacing accordingly. For example, you can set `\normalisze` to `14.4pt` with:
`\usepackage[fontsize=14.4]{fontsize}`
- [Create diagram using `xymatrix`](https://tex.stackexchange.com/questions/414832/create-diagram-using-xymatrix)

# Word
- [Craft beautiful equations in Word with LaTeX](https://www.nature.com/articles/d41586-019-01796-1)
- [LATEX EQUATION TO WORD (2007 TO 365): 3 METHODS [2022]](https://www.pickupbrain.com/ms-word/latex-equation-to-word/)
- [Rmarkdown. Equations not appearing in word](https://community.rstudio.com/t/equations-not-appearing-in-word/40228)

# Конвертация html -> LaTeX
- [How to convert HTML with mathjax into Latex using Pandoc?](https://stackoverflow.com/questions/11338049/how-to-convert-html-with-mathjax-into-latex-using-pandoc)
With the latest version of pandoc (1.12.2), you can do this:
```pandoc -f html+tex_math_dollars+tex_math_single_backslash -t latex```
Much nicer! If you don't want to convert math delimited by \( and \), just do
```pandoc -f html+tex_math_dollars -t latex```