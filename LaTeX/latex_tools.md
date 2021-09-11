# Материалы по LaTeX
- [Лекции МИФИ](http://theor.mephi.ru/wiki/index.php?title=LaTex)
- Презентация ["Документы и презентации в LaTeX (Introduction to LaTeX)"](https://www.coursera.org/course/latex) на Coursera.org
- [TeX - LaTeX Stack Exchange](http://tex.stackexchange.com/) is a question and answer site for users of TeX, LaTeX, ConTeXt, and related typesetting systems. It's 100% free, no registration required. 

# TikZ для Beamer LaTeX
## Что такое TikZ
- [Краткое введение в TikZ](http://cremeronline.com/LaTeX/minimaltikz.pdf)
- [TikZ & PGF manual](http://mirrors.ctan.org/graphics/pgf/base/doc/pgfmanual.pdf)
- Ю. А. Кирютенко. [TikZ & PGF. Создание графики в LATEX2ε-документах](http://open-edu.rsu.ru/files/pgf-ru-all-method.pdf). — Ростов-на-Дону, 2014, 277 c.
- [Tikz online editor](https://pickedshares.com/en/tikz-online-editor/)
- [TikZ and PGF examples](https://texample.net/tikz/examples/all/?page=2)
- [Scale coordinates in the direction of a vector in TikZ](https://tex.stackexchange.com/questions/429565/scale-coordinates-in-the-direction-of-a-vector-in-tikz)
- [TikZ manual newest version online?](https://tex.stackexchange.com/questions/49698/tikz-manual-newest-version-online)
- PGF online manual. [9 Syntax for Path Specifications](https://stuff.mit.edu/afs/athena/contrib/tex-contrib/beamer/pgf-1.01/doc/generic/pgf/version-for-tex4ht/en/pgfmanualse9.html)
- COOL! [Tutorial 17.1a - PGF/Tikz](https://www.flutterbys.com.au/stats/tut/tut17.1a.html). Relative coordinate, Incremental/Non-incremental

- [TikzEdt](http://www.tikzedt.org/) is a combined WYSIWYG/text editor designed for editing Tikz code.
- [LaTeX for technics[(https://www.latex4technics.com/?note=HIHZ3U)


## Tikz tips
- [Two methods of specifying a closed path: by repeating the starting coordinate at the end vs. by using `cycle`](https://tex.stackexchange.com/questions/375295/two-methods-of-specifying-a-closed-path-by-repeating-the-starting-coordinate-at/375303)
- [Saving and reusing/combining paths in TikZ?](https://tex.stackexchange.com/questions/26627/saving-and-reusing-combining-paths-in-tikz)
```
\begin{tikzpicture}
  \newcommand{\aaa}{(0,0) -- (2,2) -- (4,1)}
  \newcommand{\bbb}{(6,-2) -- (3,-2)}
  \filldraw[color=red,fill=blue] \aaa -- \bbb -- cycle;
\end{tikzpicture}
```
- [Reusable Values in Tikz](https://www.reddit.com/r/LaTeX/comments/4rq1p0/reusable_values_in_tikz/)
```
\begin{tikzpicture}
\def\a{5};
\draw (0,0) rectangle ++(\a,\a);
\end{tikzpicture}
```
- [Filling an Area Between Two Curves](https://latexdraw.com/filling-an-area-between-two-curves/)
- [Filling between an ellipse and a line](https://tex.stackexchange.com/questions/101554/filling-between-an-ellipse-and-a-line)
- COOL! Здесь вообще компактно. [how to fill intersection of 2 shapes in latex tikz package {duplicate}](https://tex.stackexchange.com/questions/103047/how-to-fill-intersection-of-2-shapes-in-latex-tikz-package)
- [Where is the pattern list gallery for pgfplots?](https://tex.stackexchange.com/questions/114646/where-is-the-pattern-list-gallery-for-pgfplots)
- [Tikz: issue when combining arcs and arrows?](https://tex.stackexchange.com/questions/460885/tikz-issue-when-combining-arcs-and-arrows).
```
\usetikzlibrary{arrows.meta,bending} % <--- added

\def\centerarc[#1](#2)(#3:#4:#5);%
%Syntax: [draw options] (center) (initial angle:final angle:radius)
    {
    \draw[#1]([shift=(#3:#5)]#2) arc (#3:#4:#5);
    }
```
- [Drawing empty, large arrow](https://tex.stackexchange.com/questions/404739/drawing-empty-large-arrow). `\usetikzlibrary{shapes.arrows}`
- Dimension line
	- [Draw dimension of a line as a decoration in TikZ](https://tex.stackexchange.com/questions/37901/draw-dimension-of-a-line-as-a-decoration-in-tikz)
	- COOL! [Dimensioning of a technical drawing in TikZ](https://tex.stackexchange.com/questions/14901/dimensioning-of-a-technical-drawing-in-tikz)
	- COOL! [Tikz-dimline label position (Dimension lines)](https://tex.stackexchange.com/questions/468143/tikz-dimline-label-position-dimension-lines)
	- [tikz-dimline – Technical dimension lines using PGF/TikZ](https://www.ctan.org/tex-archive/graphics/pgf/contrib/tikz-dimline?lang=en)
	- Тут краткий рецепт, включая `shift`. [How to set a code block using \tikzset](https://tex.stackexchange.com/questions/295856/how-to-set-a-code-block-using-tikzset)
- [Adjust position of node label](https://tex.stackexchange.com/questions/153391/adjust-position-of-node-label)
- [Learn How to Draw a Cylinder Shape in TikZ](https://latexdraw.com/cylinder-shape-in-tikz/)
- [Draw 3D Cylinder](https://www.latex4technics.com/?note=32AE)

## tikz angle label
- [Angles examples](https://texample.net/tikz/examples/feature/angles/). `\usetikzlibrary{angles}`
- Проблемка с ployglossia и надписями tikz. парсер рвет. [Polyglossia setotherlanguage conflicts with tikz library quotes](https://tex.stackexchange.com/questions/522815/polyglossia-setotherlanguage-conflicts-with-tikz-library-quotes).
Solution: According to what I find adding `\usetikzlibrary{babel}` fixes it

- COOL! [Move label of an angle in Tikz](https://tex.stackexchange.com/questions/502638/move-label-of-an-angle-in-tikz)
- [draw two tangent cones in tikz](https://tex.stackexchange.com/questions/576204/draw-two-tangent-cones-in-tikz)
- [TikZ: normal and tangent vectors added to ellipse 2](https://tex.stackexchange.com/questions/120706/tikz-normal-and-tangent-vectors-added-to-ellipse-2?rq=1)
- [How can I fix 'Missing \endcsname inserted' this error when using Tikz for Overleaf?](https://stackoverflow.com/questions/61544871/how-can-i-fix-this-error-when-using-tikz-for-overleaf)

# Анимация презентаций в аспекте фокусировки внимания слушателей
- [Пример анимированного выделения части текста](http://www.texample.net/tikz/examples/beamer-arrows/) на TeXample.net
- [Примеры комбинаций TikZ и Beamer](http://www.texample.net/tikz/examples/tag/beamer/) на TeXample.net

## Статьи в блоге ShareLatex по работе связки TikZ+beamer
- [Basic Drawing Using TikZ](https://www.sharelatex.com/blog/2013/08/27/tikz-series-pt1.html)
- [Generating TikZ Code](https://ru.sharelatex.com/blog/2013/08/28/tikz-series-pt2.html) from [GeoGebra](http://www.geogebra.org/) for LaTeX Documents and Beamer Presentations.
- [Creating Mind Maps Using TikZ](https://www.sharelatex.com/blog/2013/09/04/tikz-series-pt5.html)
- [Creating Flowcharts with TikZ](https://www.sharelatex.com/blog/2013/08/29/tikz-series-pt3.html)

## Русскоязычные материалы
- [Диаграммы в LaTeX](http://habrahabr.ru/post/81751/)

## Сопутствующие инструменты
- [Geogebra](http://www.geogebra.org/) is a multi-platform mathematics software that gives everyone the chance to experience the extraordinary insights that math makes possible. Представляет собой удобный кроссплатформенный инструмент для визуального создания диаграмм и генерации TikZ кода.

## Мультиязычность
- [Multilingual typesetting on Overleaf using polyglossia and fontspec](https://ru.overleaf.com/learn/latex/Multilingual_typesetting_on_Overleaf_using_polyglossia_and_fontspec)

