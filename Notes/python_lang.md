
# проблемы python
- GIL:
    - [Как устроен GIL в Python](https://habr.com/ru/post/84629/)
    - [What Is the Python Global Interpreter Lock (GIL)?](https://realpython.com/python-gil/)
- Pandas BlockManager:
	- [Apache Arrow and the "10 Things I Hate About pandas"](https://wesmckinney.com/blog/apache-arrow-pandas-internals/)
	- [The one pandas internal I teach all my new colleagues: the BlockManager](https://uwekorn.com/2020/05/24/the-one-pandas-internal.html)
	- [What is BlockManager and why does it exist?](https://github.com/pydata/pandas-design/blob/a0f1d32094f5030cc06ec09c8582b5a7b7798065/source/internal-architecture.rst#what-is-blockmanager-and-why-does-it-exist)
	- [Block manager rewrite](https://pandas.pydata.org/docs/development/roadmap.html#block-manager-rewrite)

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
- Полная дичь. [3 ways to deal with `SettingWithCopyWarning` in Pandas](https://www.analyticsvidhya.com/blog/2021/11/3-ways-to-deal-with-settingwithcopywarning-in-pandas/)
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
- [timeit — Измерение времени выполнения небольших фрагментов кода](https://digitology.tech/docs/python_3/library/timeit.html)
- [timeit — Measure execution time of small code snippets](https://docs.python.org/3/library/timeit.html)
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