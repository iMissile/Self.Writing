## LaTeX
- COOL! [Differences between LuaTeX, ConTeXt and XeTeX](https://tex.stackexchange.com/questions/36/differences-between-luatex-context-and-xetex)
- [��������� \No ������ �� babel](https://www.linux.org.ru/forum/general/9583562). 
������ ��, ����� �������� `\newcommand{\No}{\textnumero}` � ��������� ��������� � ��� ����� ��������.
- [The Russian Language in the babel system , Igor A. Kotelnikov](http://ctan.math.illinois.edu/languages/babel/contrib/russian/russianb.pdf).  ... Since earlier versions babel did not support XeLATEX (at least for some languages including Russian), the polyglossia package was generally recommended in the past for use with XeLATEX as a replacement for babel. Nowadays, babel can be used with any engines, including LATEX, PDFLATEX, LuaLATEX, and XeLATEX. Nevertheless some troubles may occur with some languages which have no promptly updated .ldf files.
- [Polyglossia vs Babel](https://tex.stackexchange.com/questions/88481/polyglossia-vs-babel)
- [Polyglossia: An Alternative to Babel for XeLEATEX and LuaLATEX](http://mirrors.ibiblio.org/CTAN/macros/xetex/latex/polyglossia/polyglossia.pdf)
- [How to Write Multilingual Text with Different Scripts in LaTeX](https://www.overleaf.com/latex/examples/how-to-write-multilingual-text-with-different-scripts-in-latex/wfdxqhcyyjxz#.W6D44mj7SUk)
- [Polyglossia ignores my custom hyphenation](https://tex.stackexchange.com/questions/229915/polyglossia-ignores-my-custom-hyphenation)
- [Changing language back and forth with polyglossia](https://tex.stackexchange.com/questions/186156/changing-language-back-and-forth-with-polyglossia)
- [ShareLaTeX XeLaTeX user guide](https://ru.sharelatex.com/learn/latex/XeLaTeX)
- [Overleaf: What OTF/TTF fonts are supported via fontspec?](https://www.overleaf.com/help/193-what-otf-slash-ttf-fonts-are-supported-via-fontspec#.W6EG_Gj7SUk)
- [Overleaf: Gallery � Fonts](https://www.overleaf.com/gallery/tagged/fonts#.W6EG-mj7SUk)
- [Overleaf: I have a custom font I'd like to load to my document. How can I do this?](https://www.overleaf.com/help/73-i-have-a-custom-font-id-like-to-load-to-my-document-how-can-i-do-this#.W6EHzGj7SUk)
- � Overleaf �������� �������� �� ������� _PT Sans_:
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
	- [ptsans � PT Sans font and LATEX support](https://ctan.org/pkg/ptsans)
	- [Support package for PT Sans](http://mirror.hmc.edu/ctan/obsolete/fonts/ptsans/doc/fonts/ptsans/ptsans.pdf)
	- [\fontspec all the fonts!](https://www.overleaf.com/articles/slash-fontspec-all-the-fonts/qnsxyhrgjsgs)
	- [I have a custom font I'd like to load to my document How can I do this?](https://www.overleaf.com/learn/latex/Questions/I_have_a_custom_font_I%27d_like_to_load_to_my_document._How_can_I_do_this%3F)
```
Using a custom font
Add the .ttf or .otf file to your project, by clicking on �Add files� on the top of your file list, and then selecting �Upload from > computer�. Browse to your .ttf/.otf files and upload them.
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
- ��������� �������� ��� LaTeX:
	- [Detexify](http://detexify.kirelabs.org/classify.html)
	- [LaTeXDraw](http://latexdraw.sourceforge.net/) is a graphical drawing editor for LaTeX. LaTeXDraw can be used to 1) generate PSTricks code; 2) directly create PDF or PS pictures. LaTeXDraw is developed in Java and thus runs on top of Linux, Windows, and Mac OS X. You need Java 8 to launch LaTeXDraw.
	- [Math](https://www.mathcha.io/) Online Mathematics Editor, a fast way to write and share mathematics
	- [GeoGebra Math Apps](https://www.geogebra.org/)
Get our free online math tools for graphing, geometry, 3D, and more!
	- [TikzEdt](http://www.tikzedt.org/) is a combined WYSIWYG/text editor designed for editing Tikz code.
	- [Yichuan Shen's tikzcd-editor](http://tikzcd.yichuanshen.de/)

## ������ ��� ������� TeXLive
- [! LaTeX Error: File `titling.sty' not found. #115](https://github.com/rstudio/bookdown/issues/115)
- LaTeX Error: File 'framed.sty' not found. ������ ���������� [`sudo yum -y install texlive-framed`](https://github.com/rstudio/rmarkdown/issues/39)
- LaTeX Error: File 'titling.sty' not found. ������ ���������� `sudo yum -y install texlive-titling`

������� ���� � LaTeX:
- [Overleaf. ������� ���� � LaTeX: XeLaTeX](https://www.overleaf.com/latex/templates/5-dot-2-2-russkii-iazyk-v-latex-xelatex/skfzmvgdgvnk)
- [XeLaTeX ��� �� ������� ������� �������� ������� � ������������� pdf](http://astronu.jinr.ru/wiki/index.php/XeLaTeX_%D0%B8%D0%BB%D0%B8_%D0%BD%D0%B0_%D0%BF%D0%BE%D1%80%D1%8F%D0%B4%D0%BE%D0%BA_%D1%83%D0%BB%D1%83%D1%87%D1%88%D0%B8%D0%BC_%D0%BA%D0%B0%D1%87%D0%B5%D1%81%D1%82%D0%B2%D0%BE_%D1%88%D1%80%D0%B8%D1%84%D1%82%D0%BE%D0%B2_%D0%B2_%D0%BE%D0%BA%D0%BE%D0%BD%D1%87%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%D0%BC_pdf)
- Package fontenc Error: Encoding file 't2aenc.def' not found. ������ ���������� [`sudo yum -y install texlive-cyrillic`](http://tex.stackexchange.com/questions/5079/what-is-wrong-with-my-cyrillic-text)
 � `yum install texlive-collection-langcyrillic`
- Font T2A/cmr/m/n/12=larm1200 at 12.0pt not loadable: Metric (TFM) file not found. ������ ���� � ������ [Error in TeX Live � Font � not loadable: Metric (TFM) file not found](http://tex.stackexchange.com/questions/75166/error-in-tex-live-font-not-loadable-metric-tfm-file-not-found). ������� ������� -- ������ ��� font ������: `yum -y install texlive-*font*`
- [��������� �� XeTeX, �������� ������ `! Corrupted NFSS tables`](http://tex.stackexchange.com/questions/237188/corrupted-nfss-tables)
- pdfLaTeX ��� Windows ���� ����� ������: ` pdfTeX error (font expansion): auto expansion is only possible with scalable fonts.`. ������ ������� ������ 
[On pdfTeX error (font expansion): auto expansion is only possible with scalable fonts, microtype package](http://tex.stackexchange.com/questions/283960/on-pdftex-error-font-expansion-auto-expansion-is-only-possible-with-scalable).
���� ����������, ��� ������� [� ���� ����� `microtype`](http://tex.stackexchange.com/questions/10706/pdftex-error-font-expansion-auto-expansion-is-only-possible-with-scalable). ���� ��� ���������������� � ��������������� .tex �����, �� ���������� ��������, �� ����� ������� � ��� bold.
���� ������� ��������� ����� `cm-super`
- [How to set font to Arial throughout the entire document?](http://tex.stackexchange.com/questions/23957/how-to-set-font-to-arial-throughout-the-entire-document)
- COOL! �������� ����� �������. [Cyrillic in (La)TeX](http://tex.stackexchange.com/questions/816/cyrillic-in-latex)
������� � Linux Libertine ���� ������� �����: [fontspec error: �font-not-found�](http://tex.stackexchange.com/questions/266101/fontspec-error-font-not-found).
������ `\setmainfont{Linux Libertine O}`, ��������� � ������� ������� `fc-list | grep "Linux Libertine" | grep ".otf"`.
- [Linux Libertine font](http://www.linuxlibertine.org/index.php?id=1&L=1).
	- ������ ��� �����
	- ������ ��� CentOS �������� `sudo yum install linux-liber*`. ���� ������ ������������� �����: `/usr/share/fonts/linux-libertine/LinLibertine_*`
	- � ��� ���� ����� LaTeX [`libertine`](https://www.ctan.org/tex-archive/fonts/libertine/)
	- [Libertine Font problem with XeLaTeX](http://tex.stackexchange.com/questions/105970/font-problem-with-xelatex)


## ������� � overleaf
`babel` �������. ������ ������������ `polyglossia
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
% \setmainfont{PT Sans} % ������ ������ ������������ � ���� ������
% ������� �� �����, ��������� � Overleaf
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

## ������� �������������� ������ ������� � MikTeX 2019 ����
- ������ `Package hyperref Warning: Option `pagecolor' is not available anymore.`. ��� �������� ��������� ���� ����������� ��� pdf
- `Package caption2 Warning: ****************************************************
(caption2)                THIS PACKAGE IS OBSOLETE
...
New documents should use the regular `caption' package v3.x instead.`
������ ������������ ������ caption, ���� caption-eng.pdf, [�����������](https://gitlab.com/axelsommerfeldt/caption)
- `l.15 \hypersetup
                {bookmarksnumbered=true}
? `