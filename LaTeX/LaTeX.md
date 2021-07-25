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
- Редакторы картинок для LaTeX:
	- [Detexify](http://detexify.kirelabs.org/classify.html)
	- [LaTeXDraw](http://latexdraw.sourceforge.net/) is a graphical drawing editor for LaTeX. LaTeXDraw can be used to 1) generate PSTricks code; 2) directly create PDF or PS pictures. LaTeXDraw is developed in Java and thus runs on top of Linux, Windows, and Mac OS X. You need Java 8 to launch LaTeXDraw.
	- [Math](https://www.mathcha.io/) Online Mathematics Editor, a fast way to write and share mathematics
	- [GeoGebra Math Apps](https://www.geogebra.org/)
Get our free online math tools for graphing, geometry, 3D, and more!
	- [TikzEdt](http://www.tikzedt.org/) is a combined WYSIWYG/text editor designed for editing Tikz code.
	- [Yichuan Shen's tikzcd-editor](http://tikzcd.yichuanshen.de/)

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

## Библиография
- [sort biblatex bibliography by appearance of cites in the document {duplicate}](https://tex.stackexchange.com/questions/116088/sort-biblatex-bibliography-by-appearance-of-cites-in-the-document)
- [Biblatex citation order](https://tex.stackexchange.com/questions/51434/biblatex-citation-order)
- [How do I cite range of references? {duplicate}](https://tex.stackexchange.com/questions/103792/how-do-i-cite-range-of-references?noredirect=1&lq=1). The tags you used suggest that you use `biblatex`. In this case you could use one of the styles anding on `-comp`.

## Управление с проектами
- [Management in a large project](https://ru.overleaf.com/learn/latex/Management_in_a_large_project)