# проблемы python
- GIL:
    - [Как устроен GIL в Python](https://habr.com/ru/post/84629/)
    - [What Is the Python Global Interpreter Lock (GIL)?](https://realpython.com/python-gil/)
- Pandas BlockManager:
	- [Apache Arrow and the "10 Things I Hate About pandas"](https://wesmckinney.com/blog/apache-arrow-pandas-internals/)
	- [The one pandas internal I teach all my new colleagues: the BlockManager](https://uwekorn.com/2020/05/24/the-one-pandas-internal.html)
	- [What is BlockManager and why does it exist?](https://github.com/pydata/pandas-design/blob/a0f1d32094f5030cc06ec09c8582b5a7b7798065/source/internal-architecture.rst#what-is-blockmanager-and-why-does-it-exist)
	- [Block manager rewrite](https://pandas.pydata.org/docs/development/roadmap.html#block-manager-rewrite)
- Сборка
	- [What the f*ck Python!](https://github.com/satwikkansal/wtfpython). Exploring and understanding Python through surprising snippets
	- [python-code-disasters](https://github.com/sobolevn/python-code-disasters)
- pandas дичь
	- Полная дичь. [3 ways to deal with `SettingWithCopyWarning` in Pandas](https://www.analyticsvidhya.com/blog/2021/11/3-ways-to-deal-with-settingwithcopywarning-in-pandas/)
	- [How to Avoid a Pandas Pandemonium](https://towardsdatascience.com/how-to-avoid-a-pandas-pandemonium-e1bed456530)
	- [Pandas vectorization: faster code, slower code, bloated memory](https://pythonspeed.com/articles/pandas-vectorization/)
- Base Python:
- А вот еще сказочный треш от питона, все забывал его упомянуть.
пункт ["Method 2 Creating a 2-D list"](https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/), наивный способ инициализации массива

# недостатки python
- [Почему будущее не за Python](https://habr.com/ru/company/edison/blog/495610/)
- [Пока, Python. Привет, Julia❗](https://habr.com/ru/company/edison/blog/506656/)
- [Python — это медленно. Почему?](https://habr.com/ru/company/ruvds/blog/418823/)

# IDE & Installation
- [Spyder](https://www.spyder-ide.org/) is a free and open source scientific environment written in Python, for Python, and designed by and for scientists, engineers and data analysts. Our standalone installers for Windows and macOS are available from Spyder 4.2 onwards. [We recommend using this installation method](https://docs.spyder-ide.org/current/installation.html) on those platforms, but we offer several other options for Linux, advanced users and specific needs, so keep reading if that’s the case for you.
	- [Official repository for Spyder - The Scientific Python Development Environment](https://github.com/spyder-ide/spyder).
- [Using Python with the RStudio IDE](https://support.rstudio.com/hc/en-us/articles/1500007929061-Using-Python-with-the-RStudio-IDE)
- [How do I install pip on macOS or OS X?](https://stackoverflow.com/questions/17271319/how-do-i-install-pip-on-macos-or-os-x)
- COOL! [How to upgrade all Python packages with pip](https://stackoverflow.com/questions/2720014/how-to-upgrade-all-python-packages-with-pip)
	 - The shortest and easiest on Windows. Запускаем именно в классической командной строке:
`pip freeze > requirements.txt && pip install --upgrade -r requirements.txt && rm requirements.txt`
	- Еще решение (работает, запускаем под WT и бед не знаем). [And for python 3... pip3 install]
```
Use AWK update packages:
pip install -U $(pip freeze | awk -F'[=]' '{print $1}')

Windows PowerShell update
foreach($p in $(pip freeze)){ pip install -U $p.Split("=")[0]}
```
	- Еще решение (надо проверять): 
```
$ pip install pipupgrade
$ pipupgrade --verbose --latest --yes
```
- [How To Update All Python Packages](https://www.activestate.com/resources/quick-reads/how-to-update-all-python-packages/)
- [8 Best Ways to Check the Package Version in Python](https://blog.finxter.com/check-the-package-version-in-python)
`pip show my_package`
- [pip's dependency resolver does not currently take into account all the packages that are installed](https://bobbyhadz.com/blog/python-error-pips-dependency-resolver-does-not-currently-take)
	- Install and upgrade `wheel`, `setuptools`and `pip`.
	- Optionally create a virtual environment and install the package in it.
	- Make sure your Python version is supported by the package.
- [How to Update All of Your Python Packages With pip Using One Simple Command](https://dougie.io/answers/pip-update-all-packages/)
`pip freeze | cut -d'=' -f1 | xargs -n1 pip install -U`
- [How to find a Python package's dependencies](https://stackoverflow.com/questions/29751572/how-to-find-a-python-packages-dependencies)
- [IPython. Interactive Computing](https://ipython.org/). Он же Jupyter.
	- [Install](https://docs.jupyter.org/en/latest/install/notebook-classic.html) `pip3 install jupyter`
	- [Run](https://docs.jupyter.org/en/latest/running.html#running) `jupyter notebook`
	- [exit from ipython](https://stackoverflow.com/questions/1527689/exit-from-ipython). I like IPython a lot for working with the python interpreter. However, I continually find myself typing exit to exit, and get prompted "Type exit() to exit."
I know I can type Ctrl-D to exit, but is there a way I can type exit without parentheses and get IPython to exit?
- [JupyterLab computational environment.](https://github.com/jupyterlab/jupyterlab). 
	- [Install] `pip install jupyterlab`
	- Start up JupyterLab using: `jupyter lab`
	- [A visual debugger for Jupyter](https://blog.jupyter.org/a-visual-debugger-for-jupyter-914e61716559)
- [Orange](https://orangedatamining.com/). Open source machine learning and data visualization.
- MacOS. [Switching Python version installed by Homebrew](https://stackoverflow.com/questions/64362772/switching-python-version-installed-by-homebrew)
```
brew unlink python@3.9
brew unlink python@3.8
brew link --force python@3.9
```


## VScode
- [Setting Up Run by Line and Debugging for Notebooks](https://github.com/microsoft/vscode-jupyter/wiki/Setting-Up-Run-by-Line-and-Debugging-for-Notebooks)
Run `pip install -U ipykernel`
- [VSCode. Python Interactive window](https://code.visualstudio.com/docs/python/jupyter-support-py)
- [How to separate changed files from untracked files in vscode?](https://stackoverflow.com/questions/52410100/how-to-separate-changed-files-from-untracked-files-in-vscode)
`Settings/untracked`
- [EFFICIENTLY REMOVE UNTRACKED FILES FROM VISUAL STUDIO CODE REPOSITORY](https://whatismarkdown.com/efficiently-remove-untracked-files-from-visual-studio-code-repository/)
- [Refactoring](https://code.visualstudio.com/docs/editor/refactoring)
- COOL! [How can you export the Visual Studio Code extension list?](https://stackoverflow.com/questions/35773299/how-can-you-export-the-visual-studio-code-extension-list)
```
Dump extensions:
code --list-extensions > extensions.txt

Install extensions with Bash (Linux, OS X and WSL):
cat extensions.txt | xargs code --list-extensions {}

Install extensions on Windows with PowerShell:
cat extensions.txt |% { code --install-extension $_}
```
or
Generate a Windows command file (batch) for installing extensions:
```
for /F "tokens=*" %i in ('code --list-extensions')
   do @echo call code --install-extension %i >> install.cmd
```
- Мой список установленных расширений
```
1YiB.rust-bundle
bungcip.better-toml
dustypomerleau.rust-syntax
eamodio.gitlens
ms-azuretools.vscode-docker
MS-CEINTL.vscode-language-pack-ru
ms-python.isort
ms-python.pylint
ms-python.python
ms-python.vscode-pylance
ms-toolsai.jupyter
ms-toolsai.jupyter-keymap
ms-toolsai.jupyter-renderers
ms-toolsai.vscode-jupyter-cell-tags
ms-toolsai.vscode-jupyter-slideshow
ms-vscode-remote.remote-containers
ms-vscode-remote.remote-wsl
quarto.quarto
RDebugger.r-debugger
REditorSupport.r
rust-lang.rust-analyzer
serayuzgur.crates
Swellaby.rust-pack
```
- [SonarLint for Visual Studio Code](https://github.com/SonarSource/sonarlint-vscode)

# Internal object structure
- [How do I look inside a Python object?](https://stackoverflow.com/questions/1006169/how-do-i-look-inside-a-python-object)
	- If you're interested in a GUI for this, take a look at [objbrowser](https://pypi.org/project/objbrowser/). It uses the inspect module from the Python standard library for the object introspection underneath. First install [PyQt](https://www.riverbankcomputing.com/software/pyqt/download) or [PySide2](https://wiki.qt.io/Qt_for_Python). Важно соблюдать версии PyQT!!! 5-ый, значит 5-ый.
	- There is a very cool tool called [objexplore](https://github.com/kylepollina/objexplore). Here is a simple example on how to use its explore function on a pandas DataFrame.

# Memory management
- [Memory Management](https://docs.python.org/3/c-api/memory.html)
- COOL! [Memory Management in Python](https://realpython.com/python-memory-management/)
- [Memory Management in Python](https://www.honeybadger.io/blog/memory-management-in-python/)
Understanding memory management is a superpower that will help you design memory-efficient applications and make it easier to debug memory issues. Join Rupesh Mishra for a deep dive into the internals of CPython.
- [Python Memory Management: The Essential Guide](https://scoutapm.com/blog/python-memory-management)

# Profiling & benchmarking
- [Python 101: An Intro To Benchmarking Your Code](https://www.blog.pythonlibrary.org/2016/05/24/python-101-an-intro-to-benchmarking-your-code/)
- [4 Simple Libraries to Quickly Benchmark Python Code](https://medium.com/swlh/4-simple-libraries-to-quickly-benchmark-python-code-8d3dfd288d7a)
- [How to Benchmark (Python) Code](https://switowski.com/blog/how-to-benchmark-python-code/)
	- `python -m timeit`
	- `rich-bench`
	- `pyperf`
	- `hyperfine`
- [The Python Performance Benchmark Suite](https://pyperformance.readthedocs.io/)
- [Scalene](https://github.com/plasma-umass/scalene): a high-performance, high-precision CPU, GPU, and memory profiler for Python with AI-powered optimization proposals
	- [Scalene - CPU and Memory Profiler for Python Code](https://coderzcolumn.com/tutorials/python/scalene-cpu-and-memory-profiler-for-python-code)
- [cProfile – How to profile your python code](https://www.machinelearningplus.com/python/cprofile-how-to-profile-your-python-code/)
- [Profiling and Analyzing Performance of Python Programs](https://martinheinz.dev/blog/64)
	- `python -m cProfile -s cumulative some-code.py`
- [How should I understand the output of dis.dis?](https://stackoverflow.com/questions/12673074/how-should-i-understand-the-output-of-dis-dis/47529318#47529318). I would like to understand how to use dis (the dissembler of Python bytecode). Specifically, how should one interpret the output of dis.dis (or dis.disassemble)?

# Conferences
- [EuroPython Conference](https://www.youtube.com/c/EuroPythonConference/playlists)

# XPROM
- [clickhouse-driver](https://clickhouse-driver.readthedocs.io/en/latest/). Python driver for ClickHouse.
	- Ставим в конфигурации `pip install clickhouse-driver[lz4,zstd]`
	- [API](https://clickhouse-driver.readthedocs.io/en/latest/api.html). This part of the documentation covers basic classes of the driver: Client, Connection and others.
- [ClickHouse and Python: Getting to Know the Clickhouse-driver Client](https://altinity.com/blog/clickhouse-and-python-getting-to-know-the-clickhouse-driver-client)
- [Python Integration with ClickHouse Connect](https://clickhouse.com/docs/en/integrations/language-clients/python/intro/)
- [clickhouse client and clickhouse local](https://clickhouse.com/docs/en/integrations/sql-clients/clickhouse-client-local/)

- [Pola.rs](https://pola-rs.github.io/polars-book/user-guide/quickstart/intro.html)
	- Ставим `pip install polars`
- Polars. [Read from MySQL, Postgres, Sqlite, Redshift, Clickhouse](https://pola-rs.github.io/polars-book/user-guide/howcani/io/read_db.html)
- [ConnectorX: The fastest library for loading your Python data frame](https://towardsdatascience.com/connectorx-the-fastest-way-to-load-data-from-databases-a65d4d4062d5)
- [connectorx](https://pypi.org/project/connectorx/). ConnectorX enables you to load data from databases into Python in the fastest and most memory efficient way.
	- [Строки подключения](https://sfu-db.github.io/connector-x/databases.html)
	- Clickhouse (through mysql protocol). `text`: MySQL Text protocol, slower than binary, recommend to use only when binary protocol is not supported by the source (e.g. Clickhouse).
- [Polars Python API reference](https://pola-rs.github.io/polars/py-polars/html/reference/index.html)

# Pola.rs
- [Polars: Create column with fixed value from variable](https://stackoverflow.com/questions/71340260/polars-create-column-with-fixed-value-from-variable)
- [Polars. Adding Columns](https://calmcode.io/polars/with_columns.html).
In pandas you may be used to calling `.assign()` when you want to add a new column. In polars you'd use the `with_columns` method instead.
- [`With_columns`](https://pola-rs.github.io/polars-book/user-guide/quickstart/quick-exploration-guide.html?highlight=with_columns#with_columns]
- [Cheatsheet for Pandas to Polars](https://www.rhosignal.com/posts/polars-pandas-cheatsheet/)
- [Tips and Tricks for Working with Strings in Polars](https://towardsdatascience.com/tips-and-tricks-for-working-with-strings-in-polars-ec6bb74aeec2). From sorting column names to splitting columns
- [How to get row_count for a group in polars?](https://stackoverflow.com/questions/70044520/how-to-get-row-count-for-a-group-in-polars)
- [What is the recommended way for retrieving row numbers (index) for polars?](https://stackoverflow.com/questions/72474673/what-is-the-recommended-way-for-retrieving-row-numbers-index-for-polars). Use `with_row_count()`
- [python-polars split string column into many columns by delimiter](https://stackoverflow.com/questions/73699500/python-polars-split-string-column-into-many-columns-by-delimiter)
- COOL!!! This is a guest post by Vincent D. Warmerdam. [The Expressions API in Polars is Amazing](https://www.pola.rs/posts/the-expressions-api-in-polars-is-amazing/)
	- [A benchmark with Polars](https://gist.github.com/koaning/5a0f3f27164859c42da5f20148ef3856)
- COOL!!! [Window functions 🚀🚀](https://pola-rs.github.io/polars-book/user-guide/dsl/window_functions.html)
- [How to perform computations easily between every column in a polars DataFrame and the mean of that column](https://stackoverflow.com/questions/72539701/how-to-perform-computations-easily-between-every-column-in-a-polars-dataframe-an)

- [Replacing Pandas with Polars. A Practical Guide](https://www.confessionsofadataguy.com/replacing-pandas-with-polars-a-practical-guide/)
- [Pandas vs Polar - A look at performance](https://studioterabyte.nl/en/blog/polars-vs-pandas)
- [Pandas vs. Polars: A Syntax and Speed Comparison](https://towardsdatascience.com/pandas-vs-polars-a-syntax-and-speed-comparison-5aa54e27497e)
- polars literal
	- [Extract value of Polars literal](https://stackoverflow.com/questions/71721497/extract-value-of-polars-literal).
```
import polars as pl
expr = pl.lit(0.5)
val = pl.select(expr)[0, 0]
```
Explanation: a polars literal is an `Expr` object. An `Expr` object can be evaluated using `pl.select()`. That returns a DataFrame. To get the value in the first row and column of that DataFrame, use `[0, 0]`
- [window agg over one value, but return another via Polars](https://stackoverflow.com/questions/72019524/window-agg-over-one-value-but-return-another-via-polars).
- [Py Polars: How to filter using 'in' and 'not in' like in SQL](https://stackoverflow.com/questions/71850031/py-polars-how-to-filter-using-in-and-not-in-like-in-sql)
- [How to filter df by value list with Polars?](https://stackoverflow.com/questions/74856449/how-to-filter-df-by-value-list-with-polars)
- [Lightweight syntax for filtering a polars DataFrame on a multi-column key?](https://stackoverflow.com/questions/72546690/lightweight-syntax-for-filtering-a-polars-dataframe-on-a-multi-column-key)
- COOL! [polars equivalent to pandas groupby shift()](https://stackoverflow.com/questions/73101521/polars-equivalent-to-pandas-groupby-shift)
- [Grouping Rows in Polars](https://stackoverflow.com/questions/72520291/grouping-rows-in-polars)
- [polars equivalent to `groupby.last`](https://stackoverflow.com/questions/73113290/polars-equivalent-to-groupby-last)
```
    df
    .select(['index', 'value'])
    .unique(subset='index', keep="last")
```
- [Filter DataFrame using within-group expression](https://music.yandex.ru/album/9062303/track/59241827)
`df.filter((pl.col("y") == pl.max("y").over("x")))`
- [Set multiple values simultaneously #1160 {Closed}](https://github.com/pola-rs/polars/issues/1160)
- [Polars: how to add a column with numerical?](https://stackoverflow.com/questions/72245243/polars-how-to-add-a-column-with-numerical)
- [Py Polars: How to filter using 'in' and 'not in' like in SQL](https://stackoverflow.com/questions/71850031/py-polars-how-to-filter-using-in-and-not-in-like-in-sql).
You were close.
```
df.filter(~pl.col('fruits').is_in(exclude_fruit))
```
- [Removing null values on selected columns only in Polars dataframe](https://stackoverflow.com/questions/73933043/removing-null-values-on-selected-columns-only-in-polars-dataframe)
The `~` in front of the `pl.all` stands for negation. Notice that we didn't need the `col_list`.
- [In polars, can I create a categorical type with levels myself?](https://stackoverflow.com/questions/70934789/in-polars-can-i-create-a-categorical-type-with-levels-myself)
- [Apply function to all columns of a Polars-DataFrame](https://stackoverflow.com/questions/67834912/apply-function-to-all-columns-of-a-polars-dataframe)
```
df.select([
    np.log2(pl.all())
])
```
- [How to select columns by data type in Polars?](https://stackoverflow.com/questions/72359181/how-to-select-columns-by-data-type-in-polars). `print(df.select([pl.col(pl.Utf8), pl.col(pl.Int64)]))`
- [Add a method to extract a column as a series #1346 {Closed}](https://github.com/pola-rs/polars/issues/1346)
- [Get column as `pl.Series` not as `pl.Dataframe` in polars](https://stackoverflow.com/questions/69916200/get-column-as-pl-series-not-as-pl-dataframe-in-polars)
- [`polars.Series.to_list`](https://pola-rs.github.io/polars/py-polars/html/reference/series/api/polars.Series.to_list.html#polars.Series.to_list). Convert this Series to a Python List. This operation clones data.
- [Select all columns where column name starts with string](https://stackoverflow.com/questions/72920189/select-all-columns-where-column-name-starts-with-string)
`.select(pl.exclude('^prefix_.*$'))`
- [polars.LazyFrame.drop_nulls](https://pola-rs.github.io/polars/py-polars/html/reference/lazyframe/api/polars.LazyFrame.drop_nulls.html). Return a new LazyFrame where rows with null values are dropped.
- COOL! [In Polars how do I print all elements of a list column?](https://stackoverflow.com/questions/74301064/in-polars-how-do-i-print-all-elements-of-a-list-column)
 [Config options](https://pola-rs.github.io/polars/py-polars/html/reference/config.html) `pl.Config.set_tbl_rows(100)`
- [How can i concat in polars dataframes that have different columns vertically](https://stackoverflow.com/questions/72642575/how-can-i-concat-in-polars-dataframes-that-have-different-columns-vertically). If you want polars to add the columns, you can by setting the direction of the concatenation to `"diagonal"`.
- [Why is use_pyarrow in function pl.read_ipc set to default False?](https://stackoverflow.com/questions/72656470/why-is-use-pyarrow-in-function-pl-read-ipc-set-to-default-false)
- [Eager join multiple DataFrames on Categorical data](https://pola-rs.github.io/polars-book/user-guide/performance/strings.html)
- [polars.toggle_string_cache](https://pola-rs.github.io/polars/py-polars/html/reference/api/polars.toggle_string_cache.html)
- [how to limit number of threads in polars](https://stackoverflow.com/questions/71179317/how-to-limit-number-of-threads-in-polars)
- [Python Polars join on column with greater or equal](https://stackoverflow.com/questions/73176563/python-polars-join-on-column-with-greater-or-equal)
- COOL! Кастуем время [Casting from integer timestamps to pl.Datetime #3318 {Closed}](https://github.com/pola-rs/polars/issues/3318).
Смотрим в сторону `dt.with_time_unit`
- [Python Polars Parse Date from Epoch](https://stackoverflow.com/questions/71641045/python-polars-parse-date-from-epoch)
- [Python-Polars: How to filter categorical column with string list](https://stackoverflow.com/questions/73519899/python-polars-how-to-filter-categorical-column-with-string-list)
- [How to increase values of polars dataframe column by index](https://stackoverflow.com/questions/72352725/how-to-increase-values-of-polars-dataframe-column-by-index)
- [Enumerate each group](https://stackoverflow.com/questions/74981501/enumerate-each-group). You're looking to `.rank()` your data - in particular - a "dense" ranking.
- [Polars: assign existing category](https://stackoverflow.com/questions/73699982/polars-assign-existing-category)
- [Using Patito for DataFrame Validation](https://patito.readthedocs.io/en/latest/tutorial/dataframe-validation.html)
	- [kolonialno/patito](https://github.com/kolonialno/patito). A data modelling layer built on top of polars and pydantic
	- [Static Typing with Python](https://typing.readthedocs.io/en/latest/)
	- В файле [pydantic.py](https://github.com/kolonialno/patito/blob/main/src/patito/pydantic.py) живет описание допустимых типов в модели.
```
class tracesSchema(pt.Model):
    pattern: str = pt.Field(dtype = pl.Categorical)
    n: int
    cases: List[str] = pt.Field(dtype = pl.List)
    cum_n: int
    cum_ratio: float
```
- [The great Python dataframe showdown, part 3: Lightning-fast queries with Polars](https://www.orchest.io/blog/the-great-python-dataframe-showdown-part-3-lightning-fast-queries-with-polars)
- Polars [Missing data](https://pola-rs.github.io/polars-book/user-guide/howcani/missing_data.html)
- [Idiomatic replacement of empty string '' with pl.Null (null) in polars](https://stackoverflow.com/questions/72292048/idiomatic-replacement-of-empty-string-with-pl-null-null-in-polars)
- [Number of unique items in a group](https://stackoverflow.com/questions/74001954/number-of-unique-items-in-a-group)


# Python & R
- [How to use R and Python in the same notebook?](https://www.askpython.com/python/examples/use-r-and-python-in-the-same-notebook)
- [R and Python Together in Jupyter Notebooks](https://www.joveactuarial.com/r-and-python-working-together/)

# 29.03.2023
- COOL! [Tutorial: Why Functions Modify Lists and Dictionaries in Python](https://www.dataquest.io/blog/tutorial-functions-modify-lists-dictionaries-python/)
- [What is the difference between arguments and parameters?](https://docs.python.org/3.3/faq/programming.html#faq-argument-vs-parameter)

# 13.03.2023
- [Overhead of Python Asyncio tasks](https://textual.textualize.io/blog/2023/03/08/overhead-of-python-asyncio-tasks/)
- [Codon](https://github.com/exaloop/codon) is a high-performance Python compiler that compiles Python code to native machine code without any runtime overhead.
- [ETNA](https://etna-docs.netlify.app/) is the first python open source framework of Tinkoff.ru AI Center. It is designed to make working with time series simple, productive, and fun
- COOL! [Append values to a set in Python](https://stackoverflow.com/questions/3392354/append-values-to-a-set-in-python). 
Use `add` to append single values.
Use `update` to add elements from tuples, sets, lists or frozen-sets
You can also use the `|` operator to concatenate two sets (union in set theory) or a shorter form using |=:

## Pandas 2.0
- [pandas 2.0 and the Arrow revolution (part I)](https://datapythonista.me/blog/pandas-20-and-the-arrow-revolution-part-i)

# 03.03.2023
- [Process escape sequences in a string in Python](https://stackoverflow.com/questions/4020539/process-escape-sequences-in-a-string-in-python)
- [How to Make Python Statically Typed — The Essential Guide](https://betterdatascience.com/python-statically-typed/)
- [Best Python Data Validation Library : In 2022](https://www.datasciencelearner.com/top-5-python-data-validation-library/)
- [Pandas DataFrame Validation with Pydantic](https://www.inwt-statistics.com/read-blog/pandas-dataframe-validation-with-pydantic.html)
- [Validate Your pandas DataFrame with Pandera](https://towardsdatascience.com/validate-your-pandas-dataframe-with-pandera-2995910e564). Make Sure Your Data Matches Your Expectation
- [Pandera. DataFrame Schemas](https://pandera.readthedocs.io/en/stable/dataframe_schemas.html)

# 25.02.2023
- [Find the memory size of a NumPy array](https://www.geeksforgeeks.org/find-the-memory-size-of-a-numpy-array/)
	- `size`: This attribute gives the number of elements present in the NumPy array.
	- `itemsize`: This attribute gives the memory size of one element of NumPy array in bytes.
	- `nbytes`: This attribute gives the total bytes consumed by the elements of the NumPy array.
- [Python memory usage of numpy arrays](https://stackoverflow.com/questions/11784329/python-memory-usage-of-numpy-arrays)
- Любопытная статья, затрагивает вычислительные сложности алгоритмов в т.ч. [How to Find the Memory Size of a Numpy Array?](https://www.scaler.com/topics/how-to-find-the-memory-size-of-a-numpy-array/)
- [How to use Python `numpy.where()` Method](https://www.digitalocean.com/community/tutorials/python-numpy-where)
- [Numpy `Argwhere` With Examples In Python](https://www.pythonpool.com/numpy-argwhere/)
- В картинках. [Reshape numpy arrays in Python — a step-by-step pictorial tutorial](https://towardsdatascience.com/reshaping-numpy-arrays-in-python-a-step-by-step-pictorial-tutorial-aed5f471cf0b)
- [How to Get Size of Object in Python](https://fedingo.com/how-to-get-size-of-object-in-python/). If you want to get size of nested and complex objects, you can use asizeof function in `Pympler` package. `from pympler import asizeof`
- [How to Get the First Match From a Python List or Iterable](https://realpython.com/python-first-match/)
- [Python list comprehension using if-else](https://pythonguides.com/python-list-comprehension-using-if-else/)


# 20.02.2023
- [Subtract a value from every number in a list in Python?](https://stackoverflow.com/questions/4918425/subtract-a-value-from-every-number-in-a-list-in-python)
The list comprehension solution is much more pythonic. `a = [x - 13 for x in a]`
- [Python | Accessing all elements at given list of indexes](https://www.geeksforgeeks.org/python-accessing-all-elements-at-given-list-of-indexes/)
- [Python | Convert set into a list](https://www.geeksforgeeks.org/python-convert-set-into-a-list/)
- [How do I make a flat list out of a list of lists?](https://stackoverflow.com/questions/952914/how-do-i-make-a-flat-list-out-of-a-list-of-lists)

## от XPROM
- [Python 3's f-Strings: An Improved String Formatting Syntax (Guide)](https://realpython.com/python-f-strings/)
- [How to write a Python dictionary into a json file?](https://www.easytweaks.com/write-dictionary-json-file-python/). `json.dump(hr_data, j)`
- [How To Save A Python Dictionary As A JSON File](https://predictivehacks.com/?all-tips=how-to-save-a-python-dictionary-as-a-json-file)
- [Что такое venv и virtualenv в Python, и как их использовать](https://blog.sedicomm.com/2021/06/29/chto-takoe-venv-i-virtualenv-v-python-i-kak-ih-ispolzovat/)
- [Питон в коробке – venv в python 3.3](https://habr.com/ru/post/157287/). 5 ноя 2012
- [Using Virtual Environments in Jupyter Notebook and Python](https://janakiev.com/blog/jupyter-virtual-envs/#add-virtual-environment-to-jupyter-notebook)

# 13.02.2023
- [Modifying a list inside a function](https://stackoverflow.com/questions/22054698/modifying-a-list-inside-a-function)
- [How do I pass a variable by reference?](https://stackoverflow.com/questions/986006/how-do-i-pass-a-variable-by-reference)
- [Get the length of a 2D Array in Python](https://bobbyhadz.com/blog/python-get-length-of-2d-array)
- [Is there a short contains function for lists?](https://stackoverflow.com/questions/12934190/is-there-a-short-contains-function-for-lists)


# 08.02.2023
- [Difference Between Multithreading vs Multiprocessing in Python](https://www.geeksforgeeks.org/difference-between-multithreading-vs-multiprocessing-in-python/)
- [Асинхронное программирование для начинающих](https://python-scripts.com/async)
- [Асинхронное программирование в Python](https://tproger.ru/translations/asynchronous-programming-in-python/)
- [Unicode & Character Encodings in Python: A Painless Guide](https://realpython.com/python-encodings-guide/)

# 06.02.2023
- [Python | Using 2D arrays/lists the right way](https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/). Тут куча граблей указана!!!
- COOL! [printing a two dimensional array in python](https://stackoverflow.com/questions/17870612/printing-a-two-dimensional-array-in-python)
```
for i in A:
    print('\t'.join(map(str, i)))
```
or `print('\n'.join('\t'.join(map(str, row)) for row in A))`
- [Two-dimensional lists (arrays)](https://snakify.org/en/lessons/two_dimensional_lists_arrays/). Тут пошаговый разбор и исполнение.
- [Python – Flatten a list of lists to a single list](https://datascienceparichay.com/article/python-flatten-a-list-of-lists-to-a-single-list/)
- [6 Ways to Concatenate Lists in Python](https://www.digitalocean.com/community/tutorials/concatenate-lists-python).
Python’s `'*'` operator can be used to easily concatenate two lists in Python. The `‘*’` operator in Python basically unpacks the collection of items at the index arguments.

# 30.01.2023
- [Print lists in Python (5 Different Ways)](https://www.geeksforgeeks.org/print-lists-in-python-4-different-ways/)
	- Without using loops: `*` symbol is use to print the list elements in a single line with space. To print all elements in new lines or separated by comma use `sep=”\n”` or `sep=”, ”` respectively. `print(*a, sep = ", ")`
- Use List Comprehension and the `enumerate()` Function to Get the Indices of All Occurrences of an Item in A List
```
programming_languages = ["JavaScript","Python","Java","Python","C++","Python"]
python_indices  = [index for (index, item) in enumerate(programming_languages) if item == "Python"]
print(python_indices)
```
- COOL! [Check if element exists in list in Python](https://www.geeksforgeeks.org/check-if-element-exists-in-list-in-python/)

# 25.01.2023
- [How To Concatenate String and Int in Python](https://www.digitalocean.com/community/tutorials/python-concatenate-string-and-int)
- [Python Unicode HOWTO](https://docs.python.org/3/howto/unicode.html)
- [Python list comprehension using if-else](https://pythonguides.com/python-list-comprehension-using-if-else/)
- [Python ‘If…Else’ In A List Comprehension (Examples)](https://www.codingem.com/python-if-else-in-list-comprehension/)
- [How To Use Break, Continue, and Pass Statements when Working with Loops in Python 3](https://www.digitalocean.com/community/tutorials/how-to-use-break-continue-and-pass-statements-when-working-with-loops-in-python-3)
- [Break out of nested loops in Python](https://note.nkmk.me/en/python-break-nested-loops/). 5 ways

# 24.01.2023
webassembly
- [Shiny for Python](https://shiny.rstudio.com/py/)
- [Compile Python to WebAssembly (WASM)](https://pythondev.readthedocs.io/wasm.html)
- [Running Python in the Browser with WebAssembly](https://testdriven.io/blog/python-webassembly/)
- [Running Python in WebAssembly](https://www.fermyon.com/blog/python-wagi)

# 22.01.2023
- COOL! Подробный разбор [How do I count the occurrences of a list item?](https://stackoverflow.com/questions/2600191/how-do-i-count-the-occurrences-of-a-list-item)
- [Python | Get the Index of first element greater than K](https://www.geeksforgeeks.org/python-get-the-index-of-first-element-greater-than-k/)
- [Python | Get the Index of first element greater than K](https://www.geeksforgeeks.org/python-program-to-replace-list-elements-within-a-range-with-a-given-number/)
- [Python - change value of items within specific range](https://dirask.com/posts/Python-change-value-of-items-within-specific-range-jE6y91)

# 20.01.2023
- [Python Graph Libraries](https://wiki.python.org/moin/PythonGraphLibraries). These libraries are concerned with graphs and networks, not the plotting of numeric data in graphical form.
- COOL! [Performance of Python Types](https://bradfieldcs.com/algos/analysis/performance-of-python-types/)
- COOL! [Python List `append()` vs `extend()`](https://blog.finxter.com/python-list-append-vs-extend/)

# 18.01.2023
- [Read data from a pandas DataFrame and create a tree using anytree in python](https://stackoverflow.com/questions/64084786/read-data-from-a-pandas-dataframe-and-create-a-tree-using-anytree-in-python)
- [Select rows from table using tree order](https://stackoverflow.com/questions/3709292/select-rows-from-table-using-tree-order)
- [6 Ways To Get The Last Element Of A List In Python](https://thispointer.com/6-ways-to-get-the-last-element-of-a-list-in-python/)
- [Python: Get Index of Max Item in List](https://datagy.io/python-index-of-max-item-list/)
- [Remove an item from a list in Python (clear, pop, remove, del)](https://note.nkmk.me/en/python-list-clear-pop-remove-del/)
- [Python `del` statement](https://docs.python.org/3/reference/simple_stmts.html#the-del-statement)
- COOL! [Is there a simple way to delete a list element by value?](https://stackoverflow.com/questions/2793324/is-there-a-simple-way-to-delete-a-list-element-by-value)
- [Python List `insert()`](https://www.programiz.com/python-programming/methods/list/insert)
- [Python: Count Unique Values in a List (4 Ways)](https://datagy.io/python-count-unique-values-list/)

# 16.01.2023
- [Saxonica. XSLT and XQuery Processing](https://pypi.org/user/saxonica/)

# 09.01.23
- [Why Python uses 0-based indexing](http://python-history.blogspot.com/2013/10/why-python-uses-0-based-indexing.html). Thursday, October 24, 2013

# 03.01.23
- [How do I split a string into a list of characters?](https://stackoverflow.com/questions/4978787/how-do-i-split-a-string-into-a-list-of-characters)
- [Pandas Drop Rows From DataFrame Examples](https://sparkbyexamples.com/pandas/pandas-drop-rows-from-dataframe/)
- [Combine two columns of text in pandas dataframe](https://stackoverflow.com/questions/19377969/combine-two-columns-of-text-in-pandas-dataframe)

# 21.12.22
- [How to sum all the values in a dictionary?](https://stackoverflow.com/questions/4880960/how-to-sum-all-the-values-in-a-dictionary)
For python 3:
```
d = {'key1': 1,'key2': 14,'key3': 47}
sum(list(d.values()))
```

# 19.12.2022
- [Guido van Rossum on Types, Speed and the Future of Python ](https://thenewstack.io/guido-van-rossum-on-types-speed-and-the-future-of-python)
- [Sorting a Python Dictionary: Values, Keys, and More](https://realpython.com/sort-python-dictionary/)

# 11.12.2022
- [Run-length Encoding for PandasPermalink](https://tech.blueyonder.com/rle-array/)
- [Все доброго утра , каким инструментом пользуются data scientists для визуализации данных , достаточно ли знания power bi?](https://t.me/pydata_chat/40737)

```100500 вариантов
начинают с 
- https://matplotlib.org/
- https://seaborn.pydata.org/
- https://plotnine.readthedocs.io/en/stable/
- https://echarts.apache.org/en/index.html
- https://observablehq.com/
- [Vega-Altair: Declarative Visualization in Python](https://altair-viz.github.io/)
- [Bokeh](https://docs.bokeh.org/en/latest/)
- [Plotly Open Source Graphing Library for Python](https://plotly.com/python/)
```

## Мутная история с Python Integer & bitwise operations.
- [class `int`](https://docs.python.org/3/library/functions.html#int)
- [A Python Integer Is More Than Just an Integer](https://jakevdp.github.io/PythonDataScienceHandbook/02.01-understanding-data-types.html#A-Python-Integer-Is-More-Than-Just-an-Integer)
- [In Python 3, there is effectively no limit to how long an integer value can be.](https://realpython.com/python-data-types/#integers)
- [Bitwise Operations on Integer Types](https://docs.python.org/3/library/stdtypes.html#bitwise-operations-on-integer-types)

# 07.12.2022
- [Появляется установочная библиотека Python3 `pandas` Не удалось импортировать модуль `lzma`.](https://www.programmerclick.com/article/3650407895/)
- [Reshaping a DataFrame with Pandas `stack()` and `unstack()`](https://towardsdatascience.com/reshaping-a-dataframe-with-pandas-stack-and-unstack-925dc9ce1289). 7 tricks to effectively use the Pandas `stack()` and `unstack()`.
- Разбираются нюансы с группированными датафреймами. Какие методы работают с заполненными элементами, а какие учитывают и NaN. [5 Pandas Group By Tricks You Should Know in Python](https://towardsdatascience.com/5-pandas-group-by-tricks-you-should-know-in-python-f53246c92c94). All you need to know about Pandas DataFrame Group By to use it efficiently.

# 04.11.2022
- [“Quacks like a duck” — why you probably should use pydantic more in Python apps](https://polarpersonal.medium.com/quacks-like-a-duck-why-you-probably-should-use-pydantic-more-in-your-python-apps-197accf1fdfc)

# 27.10.2022
- [ENH: Create dataframes using every combination of given values, like R's `expand.grid()` {#7426}](https://github.com/pandas-dev/pandas/issues/7426)
- COOL! [`expand.grid` equivalent to get pandas data frame for prediction in Python](https://stackoverflow.com/questions/71116437/expand-grid-equivalent-to-get-pandas-data-frame-for-prediction-in-python)
- [How to merge dataframes to every row in a second dataframe?](https://stackoverflow.com/questions/71710731/how-to-merge-dataframes-to-every-row-in-a-second-dataframe)
- [R `expand.grid()` function in Python](https://stackoverflow.com/questions/12130883/r-expand-grid-function-in-python):
```
from sklearn.model_selection import ParameterGrid
param_grid = {'a': [1,2,3], 'b': [5,7,9]}
expanded_grid = ParameterGrid(param_grid)
```
or
```
import janitor as jn

jn.expand_grid(others = {
    'x': range(0, 4),
    'y': ['a', 'b', 'c'],
    'z': [False, True]
})
```
or
```
>>> from datar.base import c, expandgrid
>>> expandgrid(a = c(1,2,3), b = c(4,5))
```
и еще `itertools`
- [pyjanitor](https://pypi.org/project/pyjanitor/#history). Tools for cleaning pandas DataFrames
- Site: [pyjanitor](https://pyjanitor-devs.github.io/pyjanitor/) is a Python implementation of the R package janitor, and provides a clean API for cleaning data.
- [datar](https://pwwang.github.io/datar/). A Grammar of Data Manipulation in python

# 21.10.2022
- [Interesting Ways to Select Pandas DataFrame Columns](https://towardsdatascience.com/interesting-ways-to-select-pandas-dataframe-columns-b29b82bbfb33)
- [Pandas Select Columns by Name or Index](https://sparkbyexamples.com/pandas/pandas-select-columns-by-name-or-index/)
- [How to Rename Column by Index in pandas](https://sparkbyexamples.com/pandas/pandas-rename-column-by-index/)
- [Indexing and selecting data](https://pandas.pydata.org/docs/user_guide/indexing.html)

# 17.10.2022
- [Python – An Introduction to NumPy Arrays](https://www.askpython.com/python-modules/numpy/python-numpy-arrays)
- [numpy get index where value is true](https://stackoverflow.com/questions/16094563/numpy-get-index-where-value-is-true)
- Любопытно. [Fast lags calculation concept using numpy arrays](https://www.kaggle.com/code/nareyko/fast-lags-calculation-concept-using-numpy-arrays)

# 03.10.2022
- COOL! [A tidyverse R and polars Python side-by-side](https://robertmitchellv.com/blog/2022-07-r-python-side-by-side/r-python-side-by-side.html)
- [Lark](https://github.com/lark-parser/lark) is a parsing toolkit for Python, built with a focus on ergonomics, performance and modularity.

# 22.09.2022
- [How to Install Python 3.9 on Ubuntu 20.04](https://linuxize.com/post/how-to-install-python-3-9-on-ubuntu-20-04/)
```
sudo apt update
sudo apt install software-properties-common
sudo apt install python3.9
python3.9 --version
```
- COOL! [Typeclasses in Python](https://sobolevn.me/2021/06/typeclasses-in-python)
- [How to save a pandas DataFrame table as a png](https://stackoverflow.com/questions/35634238/how-to-save-a-pandas-dataframe-table-as-a-png). Много разных вариантов

# 17.09.2022
- [Coalesce values from 2 columns into a single column in a pandas dataframe](https://stackoverflow.com/questions/38152389/coalesce-values-from-2-columns-into-a-single-column-in-a-pandas-dataframe)

# 01.09.2022
- [Selecting multiple columns in a Pandas dataframe](https://stackoverflow.com/questions/11285613/selecting-multiple-columns-in-a-pandas-dataframe)
With Pandas,
with column names
```
dataframe[['column1','column2']]
```
to select by iloc and specific columns with index number:
```
dataframe.iloc[:,[1,2]]
```
with loc column names can be used like
```
dataframe.loc[:,['column1','column2']]
```

# 27.08.22
- COOL! [nbdev+Quarto: A new secret weapon for productivity](https://www.fast.ai/2022/07/28/nbdev-v2/)
- [nbdev](https://nbdev.fast.ai/). Create delightful software. with Jupyter Notebooks. Write, test, document, and distribute software packages and technical articles — all in one place, your notebook.
- COOL! [Reshaping a DataFrame with Pandas `stack()` and `unstack()`](https://towardsdatascience.com/reshaping-a-dataframe-with-pandas-stack-and-unstack-925dc9ce1289). 7 tricks to effectively use the Pandas `stack()` and `unstack()`
- Текущее время в микросекундах.
	- [How do I get the current time in milliseconds in Python?](https://stackoverflow.com/questions/5998245/how-do-i-get-the-current-time-in-milliseconds-in-python)
	- [How can I get millisecond and microsecond-resolution timestamps in Python? {duplicate}](https://stackoverflow.com/questions/38319606/how-can-i-get-millisecond-and-microsecond-resolution-timestamps-in-python)
	- [High-precision clock in Python](https://stackoverflow.com/questions/1938048/high-precision-clock-in-python). Python 3.7 introduces 6 new time functions with nanosecond resolution, for example instead of `time.time()` you can use `time.time_ns()` to avoid floating point imprecision issues.
- [Pandas And Multiprocessing Memory Management Splitting A Dataframe Into Multiple Chunks](https://www.faqcode4u.com/faq/176176/pandas-and-multiprocessing-memory-management-splitting-a-dataframe-into-multiple-chunks). Вопрос нетривиальный, касается передачи данных в дочерние потоки.


# 13.08.2022
- [Uncommon Uses of Python in Commonly Used Libraries](https://eugeneyan.com/writing/uncommon-python/). To learn how to build more maintainable and usable Python libraries, I’ve been reading some of the most widely used Python packages. Along the way, I learned some things about Python that are off the beaten path. Here are a few things I didn’t know before.

# 06.08.2022
- [How to create a Python package in 2022](https://mathspp.com/blog/how-to-create-a-python-package-in-2022)
- [How to Choose the Right Python Concurrency API](https://superfastpython.com/python-concurrency-choose-api/)

# 28.06.2022
- [Is there a sessionInfo() equivalent in Python?](https://stackoverflow.com/questions/20703975/is-there-a-sessioninfo-equivalent-in-python)
- [14 Must-Know pip Commands For Data Scientists and Engineers](https://towardsdatascience.com/14-must-know-pip-commands-for-data-scientists-and-engineers-a59ebbe0a439)
	- List installed packages: `python -m pip list`

# 23.06.2022
- [Исключения в Python теперь считаются анти-паттерном](https://habr.com/ru/company/oleg-bunin/blog/445234/)

# 21.06.2022
- [Understanding nested list comprehension syntax in Python](https://spapas.github.io/2016/04/27/python-nested-list-comprehensions/)
- [Nested list comprehension in python](https://www.tutorialspoint.com/nested-list-comprehension-in-python)
- [Python List Comprehension: single, multiple, nested, & more](https://www.learndatasci.com/solutions/python-list-comprehension/)
- [When to Use a List Comprehension in Python](https://realpython.com/list-comprehension-python/)

# 20.06.2022
- ebook. [Announcing the release of my e-book: Introduction to Empirical Bayes](http://varianceexplained.org/r/empirical-bayes-book/)
- [Introduction to Empirical Bayes using Baseball Statistics](https://dangeles.github.io/jupyter/BaseBall_Statistics_Part1.html)
This post draws extensively on material from the book Introduction to Empirical Bayes by David Robinson. I've found the book to be an excellent introduction to Empirical Bayes, and a great introduction to the Lahman Baseball dataset as well. You can find the book here. I strongly suggest it!
- ebook Repo. [Introduction to Empirical Bayes: Examples from Baseball Statistics](https://github.com/dgrtwo/empirical-bayes-book)
- [BAYESIAN REGRESSION](https://alistaire.rbind.io/blog/bayesian-regression/)


# 19.06.2022
- [What is the right way to debug in iPython notebook?](https://stackoverflow.com/questions/32409629/what-is-the-right-way-to-debug-in-ipython-notebook)
- [Jupyter Tips and Tricks](https://chrieke.medium.com/jupyter-tips-and-tricks-994fdddb2057)
- Message. [Setupterm could not find terminal, in Python program using curses](https://discuss.dizzycoding.com/setupterm-could-not-find-terminal-in-python-program-using-curses/). В частности, при использовании `from objexplore import explore`

# 16.06.2022
- COOL! [Pandas vectorization: faster code, slower code, bloated memory](https://pythonspeed.com/articles/pands-vectorization/)
- COOL! [](https://www.analyticsvidhya.com/blog/2021/11/3-ways-to-deal-with-settingwithcopywarning-in-pandas/)
- [How vectorization speeds up your Python code](https://pythonspeed.com/articles/vectorization-python/)
- [Numba](https://numba.pydata.org/) is an open source JIT compiler that translates a subset of Python and NumPy code into fast machine code.
- [How To Fix WARNING: There was an error checking the latest version of pip Error?](https://networkcult.com/fix-warning-there-was-an-error-checking-the-latest-version-of-pip-error-1520/). 
Just Upgrade Your PIP to Latest Version using Command `python -m pip install --upgrade pip`
If you are using the Python version 3 then use the below command to update pip version: `python3 -m pip install --upgrade pip`
- [How to find size of an object in Python?](https://www.geeksforgeeks.org/how-to-find-size-of-an-object-in-python/)
- [Measure the Real Size of Any Python Object](https://goshippo.com/blog/measure-real-size-any-python-object/)

# 14.06.2022
- [Calling R From Python With rpy2](https://rviews.rstudio.com/2022/05/25/calling-r-from-python-with-rpy2/), 2022-05-25
- [imodels](https://github.com/csinva/imodels). Interpretable ML package 🔍 for concise, transparent, and accurate predictive modeling (sklearn-compatible).
- [Are list-comprehensions and functional functions faster than "for loops"?](https://stackoverflow.com/questions/22108488/are-list-comprehensions-and-functional-functions-faster-than-for-loops/60254921)
- [Are list comprehensions syntactic sugar for `list(generator expression)` in Python 3?](https://stackoverflow.com/questions/30096351/are-list-comprehensions-syntactic-sugar-for-listgenerator-expression-in-pyth/30097520)
- [The Adventures of a Pythonista in Schemeland v0.1 documentation. Quoting and quasi-quoting](http://www.phyast.pitt.edu/~micheles/scheme/scheme8.html)
- [A Brief Look at Cpython String](https://www.heurekadevs.com/a-brief-look-at-cpython-string)

# 12.06.2022
## EDA
- [10 полезных расширений для дата-сайентистов](https://habr.com/ru/company/skillfactory/blog/542870/)
- [Детальный анализ данных с помощью всего нескольких строчек кода](https://zen.yandex.ru/media/machinelearning/detalnyi-analiz-dannyh-s-pomosciu-vsego-neskolkih-strochek-koda-623835b2b834125366e2af67)
- [SweetViz](https://pypi.org/project/sweetviz/). In-depth EDA (target analysis, comparison, feature analysis, correlation) in two lines of code!
- [pandas-profiling](https://github.com/ydataai/pandas-profiling). Create HTML profiling reports from pandas DataFrame objects
- [DTale](https://github.com/man-group/dtale). Visualizer for pandas data structures

# 10.06.2022
- [Memray](https://github.com/bloomberg/memray) is a memory profiler for Python.
- [Scalene](https://github.com/plasma-umass/scalene) is a high-performance CPU, GPU and memory profiler for Python that does a number of things that other Python profilers do not and cannot do
- [imodels](https://www.marktechpost.com/2022/02/10/uc-berkeley-researchers-introduce-imodels-a-python-package-for-fitting-interpretable-machine-learning-models/): A Python Package For Fitting Interpretable Machine Learning Models

# 08.06.2022
- [Python Standard Library changes in recent years](https://antonz.org/python-stdlib-changes/)
- [What to Expect from Python 3.11?](https://bas.codes/posts/new-features-python-3-11)
- [Lena](https://github.com/ynikitenko/lena) is an architectural framework for data analysis. It is written in Python and works with Python versions 2, 3 and PyPy.

# 07.06.2022
- [How do I look inside a Python object?](https://stackoverflow.com/questions/1006169/how-do-i-look-inside-a-python-object)
- [How to Inspect a Python Object](https://www.codingem.com/inspect-a-python-object/)
- [Is there a more effective way to generate this dataframe?](https://stackoverflow.com/questions/72523656/is-there-a-more-effective-way-to-generate-this-dataframe)

# 06.06.2022
- [Skope-rules](https://github.com/scikit-learn-contrib/skope-rules). Machine learning with logical rules in Python
- [RuleFit](https://github.com/christophM/rulefit). Python implementation of the rulefit algorithm
- [Interpretable Machine Learning in 10 Minutes with RuleFit and Scikit Learn](https://towardsdatascience.com/interpretable-machine-learning-in-10-minutes-with-rulefit-and-scikit-learn-da9ebb925795)
- [Difference between rulefit & skope-rules Python Packages](https://datascience.stackexchange.com/questions/90262/difference-between-rulefit-skope-rules-python-packages)

# 30.05.2022
- [Peeking and backtracking Python generators](https://ricardoanderegg.com/posts/peeking-backtracking-python-generator/)
- [How can I remove a key from a Python dictionary?](https://stackoverflow.com/questions/11277432/how-can-i-remove-a-key-from-a-python-dictionary/32616904#32616904)
- [Pydantic](https://pydantic-docs.helpmanual.io/). Data validation and settings management using python type annotations.
- [Python Date and Time Functions: The Complete Tutorial](https://codesolid.com/python-date-tutorial/)
- [How can I make a python numpy arange of datetime](https://stackoverflow.com/questions/12137277/how-can-i-make-a-python-numpy-arange-of-datetime)

# 27.05.2022
- [Multi Index Sorting in Pandas](https://stackoverflow.com/questions/14733871/multi-index-sorting-in-pandas)
- [Python Virtual Environments: A Primer](https://realpython.com/python-virtual-environments-a-primer/)
- [rounding errors in Python floor division](https://stackoverflow.com/questions/38588815/rounding-errors-in-python-floor-division)
- [pipetools](https://0101.github.io/pipetools/doc/) enables function composition similar to using Unix pipes.

# 23.05.2022
- [How can a class that inherits from a NumPy array change its own values?](https://stackoverflow.com/questions/27910013/how-can-a-class-that-inherits-from-a-numpy-array-change-its-own-values)
- [How to create a reprex containing Python code from R/RStudio?](https://community.rstudio.com/t/how-to-create-a-reprex-containing-python-code-from-r-rstudio/95348)

# 20.05.2022
- COOL! [What’s in which Python](https://nedbatchelder.com/text/which-py.html). This is a summary of what features appeared in which versions of Python. Items with a star were introduced with a __future__ import.
- [Overview of Pandas Data Types](https://pbpython.com/pandas_dtypes.html)

# 17.05.2022
- COOL! [Python decorator patterns](https://bytepawn.com/python-decorator-patterns.html)
- [Декораторы в Python: понять и полюбить](https://tproger.ru/translations/demystifying-decorators-in-python/)
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
## pandas дичь
- COOL! Полная дичь. [3 ways to deal with `SettingWithCopyWarning` in Pandas](https://www.analyticsvidhya.com/blog/2021/11/3-ways-to-deal-with-settingwithcopywarning-in-pandas/)
- COOL! [How to Avoid a Pandas Pandemonium](https://towardsdatascience.com/how-to-avoid-a-pandas-pandemonium-e1bed456530)
- COOL! [Pandas vectorization: faster code, slower code, bloated memory](https://pythonspeed.com/articles/pandas-vectorization/)
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
- COOL! [The Basics of Indexing and Slicing Python Lists](https://towardsdatascience.com/the-basics-of-indexing-and-slicing-python-lists-2d12c90a94cf). A guide for beginners, by a beginner. Indexing, Slicing, Stepping.
В частности, Negative step values reverse the direction in which the slicer iterates through the original list: `my_list[::-1]`

# 26.10.2021
- [The nature of pandas DataFrame](https://stackoverflow.com/questions/27374774/the-nature-of-pandas-dataframe)

# 25.10.2021
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