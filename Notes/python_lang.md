# проблемы python
- GIL:
    - [Как устроен GIL в Python](https://habr.com/ru/post/84629/)
    - [What Is the Python Global Interpreter Lock (GIL)?](https://realpython.com/python-gil/)
- Pandas BlockManager:
	- [Apache Arrow and the "10 Things I Hate About pandas"](https://wesmckinney.com/blog/apache-arrow-pandas-internals/)
	- [The one pandas internal I teach all my new colleagues: the BlockManager](https://uwekorn.com/2020/05/24/the-one-pandas-internal.html)
	- [What is BlockManager and why does it exist?](https://github.com/pydata/pandas-design/blob/a0f1d32094f5030cc06ec09c8582b5a7b7798065/source/internal-architecture.rst#what-is-blockmanager-and-why-does-it-exist)
	- [Block manager rewrite](https://pandas.pydata.org/docs/development/roadmap.html#block-manager-rewrite)

# недостатки python
- [Почему будущее не за Python](https://habr.com/ru/company/edison/blog/495610/)
- [Пока, Python. Привет, Julia❗](https://habr.com/ru/company/edison/blog/506656/)
- [Python — это медленно. Почему?](https://habr.com/ru/company/ruvds/blog/418823/)

# IDE & Installation
- [Spyder](https://www.spyder-ide.org/) is a free and open source scientific environment written in Python, for Python, and designed by and for scientists, engineers and data analysts.
- [Using Python with the RStudio IDE](https://support.rstudio.com/hc/en-us/articles/1500007929061-Using-Python-with-the-RStudio-IDE)
- [How do I install pip on macOS or OS X?](https://stackoverflow.com/questions/17271319/how-do-i-install-pip-on-macos-or-os-x)
- [How to upgrade all Python packages with pip](https://stackoverflow.com/questions/2720014/how-to-upgrade-all-python-packages-with-pip)
	 - Не работает так: The shortest and easiest on Windows.
`pip freeze > requirements.txt && pip install --upgrade -r requirements.txt && rm requirements.txt`
	- Еще решение (работает, запускаем под WT и бед не знаем). [And for python 3... pip3 install]
```
Use AWK update packages:
pip install -U $(pip freeze | awk -F'[=]' '{print $1}')

Windows PowerShell update
foreach($p in $(pip freeze)){ pip install -U $p.Split("=")[0]}
```
- [IPython. Interactive Computing](https://ipython.org/). Он же Jypiter.


# 06.06.2022
- [Skope-rules](https://github.com/scikit-learn-contrib/skope-rules). Machine learning with logical rules in Python
- [RuleFit](https://github.com/christophM/rulefit). Python implementation of the rulefit algorithm
- [Interpretable Machine Learning in 10 Minutes with RuleFit and Scikit Learn](https://towardsdatascience.com/interpretable-machine-learning-in-10-minutes-with-rulefit-and-scikit-learn-da9ebb925795)
- [Difference between rulefit & skope-rules Python Packages](https://datascience.stackexchange.com/questions/90262/difference-between-rulefit-skope-rules-python-packages)

# 30.05.2022
- [Peeking and backtracking Python generators](https://ricardoanderegg.com/posts/peeking-backtracking-python-generator/)

# 27.05.2022
- [Multi Index Sorting in Pandas](https://stackoverflow.com/questions/14733871/multi-index-sorting-in-pandas)
- [Python Virtual Environments: A Primer](https://realpython.com/python-virtual-environments-a-primer/)
- [rounding errors in Python floor division](https://stackoverflow.com/questions/38588815/rounding-errors-in-python-floor-division)
- [pipetools](https://0101.github.io/pipetools/doc/) enables function composition similar to using Unix pipes.

# 23.05.2022
- [How can a class that inherits from a NumPy array change its own values?](https://stackoverflow.com/questions/27910013/how-can-a-class-that-inherits-from-a-numpy-array-change-its-own-values)
- [How to create a reprex containing Python code from R/RStudio?](https://community.rstudio.com/t/how-to-create-a-reprex-containing-python-code-from-r-rstudio/95348)

# 20.05.2022
- [What’s in which Python](https://nedbatchelder.com/text/which-py.html). This is a summary of what features appeared in which versions of Python. Items with a star were introduced with a __future__ import.
- [Overview of Pandas Data Types](https://pbpython.com/pandas_dtypes.html)

# 17.05.2022
- COOL! [Python decorator patterns](https://bytepawn.com/python-decorator-patterns.html)
- [Fundamentals of Matrix Algebra with Python | Part 1](https://towardsdatascience.com/fundamentals-of-matrix-algebra-with-python-part-1-85aaa17e3632)
- [Using the Python match statement](https://tonybaloney.github.io/posts/python-match-statement.html)
- [Linear Regression in Python](https://realpython.com/linear-regression-in-python/)

# 13.05.2022
- [what is the difference between series/dataframe and ndarray?](https://stackoverflow.com/questions/44236661/what-is-the-difference-between-series-dataframe-and-ndarray).
After some research I found the answer to my question I asked above. For anyone who needs, here it is from [pandas docs](https://pandas.pydata.org/pandas-docs/stable/dsintro.html#vectorized-operations-and-label-alignment-with-series):
_A key difference between Series and ndarray is that operations between Series automatically align the data based on the label. Thus, you can write computations without giving consideration to whether the Series involved have the same labels._
- [NumPy Arrays vs. Pandas Series: A Performance Comparison](https://nickmccullum.com/numpy-arrays-pandas-series-performance-comparison/). Indexing NumPy Arrays is faster than Indexing Pandas Series Objects
- [I have 12000 known URLs, what is the fastest way to scrape them with Python?](https://stackoverflow.com/questions/63580445/i-have-12000-known-urls-what-is-the-fastest-way-to-scrape-them-with-python)

# 11.05.2022
- Форматный вывод. 
```
var = 15.734
print ("Variable as string = %06.2f" % (var))
```
- [Python String Formatting Best Practices](https://realpython.com/python-string-formatting/)
- [A Guide to the Newer Python String Format Techniques](https://realpython.com/python-formatted-output/)
- [string — Common string operations](https://docs.python.org/3/library/string.html#string-formatting)


# 08.05.2022
- Целая философская дискуссия. [Pandas dataframe get first row of each group](https://stackoverflow.com/questions/20067636/pandas-dataframe-get-first-row-of-each-group)
I'd suggest to use `.nth(0)` rather than `.first()` if you need to get the first row.
The difference between them is how they handle `NaN`s, so `.nth(0)` will return the first row of group no matter what are the values in this row, while `.first()` will eventually return the first not NaN value in each column.
- COOL! [Bitwise Operators in Python](https://realpython.com/python-bitwise-operators/)
- [Bitfields in Python using masks, properties, and closures](https://www.hactrn.net/blog/2020/03/21/bitfields-in-python-using-masks-properties-and-closures/)
- [Bitfield](A Python bitfield class for easier bit manipulation of integers

# 05.05.2022
- [Split (explode) pandas dataframe string entry to separate rows](https://stackoverflow.com/questions/12680754/split-explode-pandas-dataframe-string-entry-to-separate-rows)
- [jellyfish](https://pypi.org/project/jellyfish/) a library for doing approximate and phonetic matching of strings.
- [jaro-winkler](https://pypi.org/project/jaro-winkler/)
- [Jaro and Jaro-Winkler similarity](https://www.geeksforgeeks.org/jaro-and-jaro-winkler-similarity/)
- [jellyfish vs pyjarowinkler](https://stackoverflow.com/questions/48428810/jellyfish-vs-pyjarowinkler)
- [textdistance](https://pypi.org/project/textdistance/). Compute distance between the two texts.
- [Fuzzy matching string comparisons with Dask DataFrames](https://coiled.io/blog/dask-fuzzy-matching-string-comparison/)
- [Applying Jaro-Winkler distance to dataframe](https://stackoverflow.com/questions/57360343/applying-jaro-winkler-distance-to-dataframe)
- [How can I use the apply() function for a single column?](https://stackoverflow.com/questions/34962104/how-can-i-use-the-apply-function-for-a-single-column)
- [Super Fast String Matching in Python](https://bergvca.github.io/2017/10/14/super-fast-string-matching.html) Oct 14, 2017
- [Applying Jaro-Winkler distance to dataframe](https://stackoverflow.com/questions/57360343/applying-jaro-winkler-distance-to-dataframe)

# 01.05.2022
- [ImageHash](https://pypi.org/project/ImageHash/). An image hashing library written in Python. ImageHash supports.
- [Art3](https://johannesbuchner.github.io/imagehash/index3.html)
- [pHash](https://www.phash.org/). The open source perceptual hash library

# 28.04.2022
- [Top2Vec](https://github.com/ddangelov/Top2Vec) learns jointly embedded topic, document and word vectors. 
- article [Top2Vec: Distributed Representations of Topics](https://arxiv.org/abs/2008.09470)
- [leaftmap. 53 choropleth](https://leafmap.org/notebooks/53_choropleth/)

# 17.04.2022
- [plotly. Calculate sum totals data-table](https://community.plotly.com/t/calculate-sum-totals-data-table/45521)
- [Using Pandas on Ray (Modin)](https://docs.ray.io/en/latest/data/modin/index.html)
- [Scaling Pandas: Comparing Dask, Ray, Modin, Vaex, and RAPIDS](https://www.datarevenue.com/en-blog/pandas-vs-dask-vs-vaex-vs-modin-vs-rapids-vs-ray)
	- Dask: a low-level scheduler and a high-level partial Pandas replacement, geared toward running code on compute clusters.
	- Ray: a low-level framework for parallelizing Python code across processors or clusters.
	- Modin: a drop-in replacement for Pandas, powered by either Dask or Ray.
	- Vaex: a partial Pandas replacement that uses lazy evaluation and memory mapping to allow developers to work with large datasets on standard machines.
	- RAPIDS: a collection of data-science libraries that run on GPUs and include cuDF, a partial replacement for Pandas.
- [Comparison between Modin | Dask | Data.table | Pandas for parallel processing and out of memory csv files](https://stackoverflow.com/questions/56483996/comparison-between-modin-dask-data-table-pandas-for-parallel-processing-an)
- COOL! [How we parallelized 600+ pandas functions with Modin](https://ponder.io/how-do-we-parallelized-600-pandas-functions-with-modin/)

# 29.03.2022
- [The Essential Protobuf Guide for Python](https://www.datascienceblog.net/post/programming/essential-protobuf-guide-python/)
- [plotnine](https://plotnine.readthedocs.io/en/stable/#) A Grammar of Graphics for Python¶. 
plotnine is an implementation of a grammar of graphics in Python, it is based on ggplot2.

# 24.03.2022
- [Daily dose of Python](https://jerry-git.github.io/daily-dose-of-python/doses/1/)
- [Refactoring a Python Codebase with LibCST](https://engineering.instawork.com/refactoring-a-python-codebase-with-libcst-fc645ecc1f09)
- [Pandas Tutor visualizes how your Python code transforms dataframes](https://pandastutor.com/index.html)
- [Creating conditional columns on Pandas with Numpy `select()` and `where()` methods](https://towardsdatascience.com/creating-conditional-columns-on-pandas-with-numpy-select-and-where-methods-8ee6e2dbd5d5). Some of the most useful Pandas tricks

# 18.03.2022
- Вопрос. Удалил папку с виртуальным окружением, во время работы в этом окружении. Все сломалось.
Теперь при исполнении кода python в файле, интерпретатор ссылается на `/venv/bin/python3: No such file or directory`.
Как починить?

починить можно двумя путями/способами:
1. создать виртуальное окружение вручную, через терминал/командную строку.
2. создать новый проект в PyCharm. При создании проекта автоматически создаётся в/окружение. Перенести в проект все файлы, установить нужные библиотеки (`pip install requests, pandas, bs4`)
Команды для создания виртуального окружения можно легко найти.

Для создания в/окружения я использую библиотеку `pipenv` (нужно предварительно установить в системе, не в ВО), 
- команда `pipenv shell` создаст ВО и автоматически активирует его
- команда `pipenv install pandas, requests, bs4` установит внутри ВО библиотеки

Вы можете использовать другие библиотеки - `venv` или `virtualenv`
при запуске скрипта интерпретатор вернёт ошибки - так Вы поймёте каких библиотек не хватает
ну и для начала загляните в пространство имён - верхняя часть скрипта, где перечислены импорты
Valerii Mamontov, [18.03.2022 8:50]
при запуске скрипта интерпретатор вернёт ошибки - так Вы поймёте каких библиотек не хватает
ну и для начала загляните в пространство имён - верхняя часть скрипта, где перечислены импорты
я себе создал шпаргалку с двумя типами окружений
посмотри как их установить, глянь что за команды и используй на здоровье
```
pipenv shell- создать окружение
pipenv install package_name 
pipenv install --dev flake8 - окружения для разработки
pipenv uninstall 
pipenv update 
pipenv run pip freeze
pipenv install -r requirements.txt

conda create -n data_env
conda install pandas
conda activate data_env
conda deactivate
conda remove -n data_env --all
conda env export >data_env.yml
conda env create -f data_env.yml
conda list
conda update pandas
conda remove pandas
```

# 09.02.2022
- [How to use loc and iloc for Selecting Data in Pandas (with Python code!)](https://www.analyticsvidhya.com/blog/2020/02/loc-iloc-pandas/)
- Как удалить из df столбцы в котором все значения 0?
`df.loc[:, (df != 0).any(axis=0)]`

# 20.02.2022
- [Python for Excel](https://www.xlwings.org/)
- [Python Project Setup – Virtual Environments and Package Management](https://bas.codes/posts/python-virtualenv-venv-pip-pyenv-poetry)

# 10.02.2022
- [Ranking order per group in Pandas](https://stackoverflow.com/questions/33899369/ranking-order-per-group-in-pandas)

# 05.02.2022
- Не решено пока. [Conditional Join (merge) in pandas #7480 {Closed}](https://github.com/pandas-dev/pandas/issues/7480)
- [How to do/workaround a conditional join in python Pandas?](https://stackoverflow.com/questions/23508351/how-to-do-workaround-a-conditional-join-in-python-pandas)

# 18.01.2022
- [Python bytecode explained](https://github.com/MoserMichael/pyasmtool/blob/master/bytecode_disasm.md)
- [Why I Use Nim instead of Python for Data Processing](https://benjamindlee.com/posts/2021/why-i-use-nim-instead-of-python-for-data-processing/)
- COOL! [NIM. Efficient, expressive, elegant](https://nim-lang.org/)
Nim is a statically typed compiled systems programming language. It combines successful concepts from mature languages like Python, Ada and Modula.

# 10.01.2022
- [Три метода Pandas, о которых вы, возможно, не знали](https://habr.com/ru/company/ruvds/blog/479276/)
- COOL! Разобрана масса вариантов, сделан тайминг! [How do I select rows from a DataFrame based on column values?](https://stackoverflow.com/questions/17071871/how-do-i-select-rows-from-a-dataframe-based-on-column-values)
- [A Guide to Python Lambda Functions](https://adamj.eu/tech/2020/08/10/a-guide-to-python-lambda-functions/)
- COOL! [Write Clean Python Code Using Pipes](https://towardsdatascience.com/write-clean-python-code-using-pipes-1239a0f3abf5). A Short and Clean Approach to Processing Iterables
	- Перевод. [Пишем чистый код на Python с PIPES](https://uproger.com/pishem-chistyj-kod-na-python-s-pipes/)

# 06.12.2021
- COOL! [Pandas Tutor visualizes how your Python code transforms dataframes](https://pandastutor.com/index.html)
- [Pandas: pad series on top or bottom](https://stackoverflow.com/questions/38743064/pandas-pad-series-on-top-or-bottom)

# 30.11.2021
- COOL! Полная дичь. [3 ways to deal with `SettingWithCopyWarning` in Pandas](https://www.analyticsvidhya.com/blog/2021/11/3-ways-to-deal-with-settingwithcopywarning-in-pandas/)
- [100 data puzzles for pandas](https://github.com/ajcr/100-pandas-puzzles), ranging from short and simple to super tricky
- [101 Pandas Exercises for Data Analysis](https://www.machinelearningplus.com/python/101-pandas-exercises-python/)

# 17.11.2021
- COOL! [How to Use MultiIndex in Pandas to Level Up Your Analysis](https://towardsdatascience.com/how-to-use-multiindex-in-pandas-to-level-up-your-analysis-aeac7f451fce). An introduction to hierarchical indexing on DataFrames for sophisticated data analysis.
Важное замечание!!! The Pandas documentation has this note on it:
Indexing will work even if the data are not sorted, but will be rather inefficient (and show a PerformanceWarning). It will also return a copy of the data rather than a view.

# 15.11.2021
- COOL! [Are list-comprehensions and functional functions faster than "for loops"?](https://stackoverflow.com/questions/22108488/are-list-comprehensions-and-functional-functions-faster-than-for-loops/22108640#22108640)
- [Top 50 Important Python Libraries!
Every Pythonista Must Have A Glance At These Libraries](https://blog.octachart.com/top-50-important-python-libraries)

# 10.11.2021
- [A high-level app and dashboarding solution for Python](https://panel.holoviz.org/)
- [Common Python Data Structures (Guide)](https://realpython.com/python-data-structures/)

# 31.10.2021
## R
- [Beautiful decision tree visualizations with dtreeviz](https://towardsdatascience.com/beautiful-decision-tree-visualizations-with-dtreeviz-af1a66c1c180)

# 29.10.2021
## python
- [The Basics of Indexing and Slicing Python Lists](https://towardsdatascience.com/the-basics-of-indexing-and-slicing-python-lists-2d12c90a94cf). A guide for beginners, by a beginner.
Indexing, Slicing, Stepping.
В частности, Negative step values reverse the direction in which the slicer iterates through the original list: `my_list[::-1]`

# 26.10.2021
## python
- [The nature of pandas DataFrame](https://stackoverflow.com/questions/27374774/the-nature-of-pandas-dataframe)

# 25.10.2021
## python
- [gslides: Creating charts in Google slides](https://michael-gracie.github.io/gslides/index.html)
- COOL! [Understanding all of Python, through its builtins](https://sadh.life/post/builtins/#index)
- COOL! [9 первоклассных функций Pandas Python для работы с данными](https://nuancesprog.ru/p/14300/)
- [PySimpleGUI: The Simple Way to Create a GUI With Python](https://realpython.com/pysimplegui-python/)

# 21.10.2021
## python
- [Here’s How to Build a Pivot Table using Pandas in Python](https://www.analyticsvidhya.com/blog/2020/03/pivot-table-pandas-python/)
- COOL! [Is there any simple way to benchmark Python script?](https://stackoverflow.com/questions/1593019/is-there-any-simple-way-to-benchmark-python-script)
If you don't want to write boilerplate code for timeit and get easy to analyze results, take a look at [benchmarkit](https://github.com/vgrabovets/benchmarkit). Also it saves history of previous runs, so it is easy to compare the same function over the course of development.
	- Требует ставить Cython для сборки пандаса на этапе инсталляции. [Cython](https://pypi.org/project/Cython/)
	The Cython compiler for writing C extensions for the Python language. 
	`pip install Cython`
- [timeit — Измерение времени выполнения небольших фрагментов кода](https://digitology.tech/docs/python_3/library/timeit.html)
- [timeit — Measure execution time of small code snippets](https://docs.python.org/3/library/timeit.html)
- [Python Timeit() with Examples](https://www.guru99.com/timeit-python-examples.html). Triple quotes for long code
- [Python 101: An Intro to Benchmarking your code](https://www.blog.pythonlibrary.org/2016/05/24/python-101-an-intro-to-benchmarking-your-code/)
И вот он, трындец по скорости:
```
timeit.timeit("[{'a': i, 'b': 2 * i} for i in range(10000)]", number = 1000)
4.28375910000068s
```
Аналог на base R дает на порядок меньше
```
bench::mark(
  m = lapply(1:1000, function(x){1:10000 %>% data.frame(a = ., b = 2 * .); NULL}),
  iterations = 1
)
# A tibble: 1 x 13
  expression      min   median `itr/sec` mem_alloc 
  <bch:expr> <bch:tm> <bch:tm>     <dbl> <bch:byt> 
1 m             407ms    407ms      2.46     115MB 
```

- [Как получить список методов в классе Python?](https://coderoad.ru/1911281/%D0%9A%D0%B0%D0%BA-%D0%BF%D0%BE%D0%BB%D1%83%D1%87%D0%B8%D1%82%D1%8C-%D1%81%D0%BF%D0%B8%D1%81%D0%BE%D0%BA-%D0%BC%D0%B5%D1%82%D0%BE%D0%B4%D0%BE%D0%B2-%D0%B2-%D0%BA%D0%BB%D0%B0%D1%81%D1%81%D0%B5-Python). Вариантов масса, один из простых:
Допустим, вы хотите знать все методы, связанные с классом `list` Просто Введите следующее
```
print (dir(list))
```

# 19.10.2021
## python
- [What the f*ck Python!](https://github.com/satwikkansal/wtfpython). Exploring and understanding Python through surprising snippets
- [Pythonic way to create a long multi-line string](https://stackoverflow.com/questions/10660435/pythonic-way-to-create-a-long-multi-line-string)
- [Use pandas.shift() within a group](https://stackoverflow.com/questions/53335567/use-pandas-shift-within-a-group). Pandas' grouped objects have a `groupby.DataFrameGroupBy.shift` method,

# 14.10.2021
## python
- [Pandas Coalesce - How to Replace NaN values in a dataframe](https://kanoki.org/2019/08/17/pandas-coalesce-replace-value-from-another-column/)
- [12 Of My Favorite Python Practices For Better Functions](https://towardsdatascience.com/12-of-my-favorite-python-practices-for-better-functions-7a21d18cfb38). It is easy to write bad functions, much harder to write exemplary ones — here are some of the ways I improve mine

## profiling
- [Profiling and Timing Code](https://jakevdp.github.io/PythonDataScienceHandbook/01.07-timing-and-profiling.html)

# 11.10.2021
## python
- [Why you can’t switch to Python 3.10 just yet](https://pythonspeed.com/articles/switch-python-3.10/) by Itamar Turner-Trauring. Last updated 05 Oct 2021
- [MkDocs. Project documentation with Markdown.](https://www.mkdocs.org/)

# 07.10.2021
## python
- [COOL!] Inside a Jupyter notebook:
BAD:
```
!pip install somelib  # may install in the wrong environment!
or
!conda install somelib  # same problem
```
GOOD:
```
import sys
!{sys.executable} -m pip install somelib
or
!conda install --yes --prefix {sys.prefix} somelib
```
- [How to determine a Python variable's type?](https://stackoverflow.com/questions/402504/how-to-determine-a-python-variables-type). Use the `type()` builtin function
- [How to use enumerate inside a list comprehension in Python](https://www.kite.com/python/answers/how-to-use-enumerate-inside-a-list-comprehension-in-python)
- [Python enumerate(): Simplify Looping With Counters](https://realpython.com/python-enumerate/)
- [Convert a Pandas DataFrame to a dictionary](https://stackoverflow.com/questions/26716616/convert-a-pandas-dataframe-to-a-dictionary)
- [Python 3's f-Strings: An Improved String Formatting Syntax (Guide)](https://realpython.com/python-f-strings/)
- [Словари (dict) и работа с ними. Методы словарей](https://pythonworld.ru/tipy-dannyx-v-python/slovari-dict-funkcii-i-metody-slovarej.html)

# 27.09.2021
## python
- COOL! [All Algorithms implemented in Python the-algorithms.com](https://github.com/TheAlgorithms/Python)

# 20.09.2021
## python
- [A Python sandbox for decision making in dynamics](https://github.com/zykls/whynot)

# 30.08.2021
## python
- [A fancy and practical functional tools](https://github.com/suor/funcy)
- [Awesome Functional Python](https://github.com/sfermigier/awesome-functional-python) A curated list of awesome things related to functional programming in Python.

# 24.08.2021
- [В чем разница между 'coding = utf8' и '- * - coding: utf-8 - * -'?](https://overcoder.net/q/280098/%D0%B2-%D1%87%D0%B5%D0%BC-%D1%80%D0%B0%D0%B7%D0%BD%D0%B8%D1%86%D0%B0-%D0%BC%D0%B5%D0%B6%D0%B4%D1%83-coding-utf8-%D0%B8-coding-utf-8). Нет никакой разницы; Python распознает все 3. Он ищет шаблон: `coding[:=]\s*([-\w.]+)`
- [Where does this come from: -*- coding: utf-8 -*-](https://stackoverflow.com/questions/4872007/where-does-this-come-from-coding-utf-8)
In Python 3+, the default encoding of source files is already UTF-8 and that line is useless.
- [3 Python Packages That Make Data Science Simple](https://medium.com/trymito/3-python-packages-that-make-data-science-simple-25695dc565d). 1. Mito; 2. Pandas Profiling; 3. Lux
- [Python eval(): Evaluate Expressions Dynamically](https://realpython.com/python-eval-function/)

## Хорошие либы в python
- [FastAPI framework](https://fastapi.tiangolo.com/) -- high performance, easy to learn, fast to code, ready for production
- [Scale your pandas workflow by changing a single line of code](https://modin.readthedocs.io/en/latest/)
- [Fast multi-threaded DataFrame library in Rust and Python](https://github.com/pola-rs/polars)
- [OpenCV]()
- [Voilà](https://github.com/voila-dashboards/voila) turns Jupyter notebooks into standalone web applications

- [How to Speed Up Pandas with Modin](https://medium.com/distributed-computing-with-ray/how-to-speed-up-pandas-with-modin-84aa6a87bcdb)
- [Pandas Cheat Sheet — Python for Data Science](https://www.dataquest.io/blog/pandas-cheat-sheet/)
- [MyST - Markedly Structured Text](https://myst-parser.readthedocs.io/en/latest/). A fully-functional markdown flavor and parser for Sphinx. MyST allows you to write Sphinx documentation entirely in markdown.
- [MyST cheat sheet](https://jupyterbook.org/reference/cheatsheet.html)