# 25.12.2018
## R
- "Advancer R" 2-nd ed. [10 Function factories](https://adv-r.hadley.nz/function-operators.html)

# 24.12.2018
## R & DS
- COOL! [CUSTOM JAVASCRIPT, CSS AND HTML IN SHINY](https://www.listendata.com/2018/12/javascript-shiny-r.html)
- [SHINYPROXY CHRISTMAS RELEASE](https://www.openanalytics.eu/blog/2018/12/23/shinyproxy-2.1.0/)
- [Spinning Pins](https://fronkonstin.com/2018/12/19/spinning-pins/)
- COOL! [Spelling 2.0: Improved Markdown and RStudio Support](https://ropensci.org/technotes/2018/12/20/spelling-20/)
- [How to Scrape Data from a JavaScript Website with R](https://velaco.github.io/how-to-scrape-data-from-javascript-websites-with-R/)
- COOL! [Headless 'Chrome' Orchestration in R](https://github.com/hrbrmstr/decapitated)
- COOL! [5 amazing free tools that can help with publishing R results and blogging](https://jozefhajnala.gitlab.io/r/r907-christmas-praise/)
- COOL! [Create R Markdown reports and presentations even better with these 3 practical tips](https://jozefhajnala.gitlab.io/r/r909-rmarkdown-tips/)
- COOL! [Here's why 2019 is a great year to start with R: A story of 10 year old R code then and now](https://jozefhajnala.gitlab.io/r/r908-10-year-old-code/)
- Весьма прикольно! [BUBBLE PACKED CHART WITH R USING PACKCIRCLES PACKAGE](https://chichacha.netlify.com/2018/12/22/bubble-packed-chart-with-r-using-packcircles-package/)
- [November 2018: “Top 40” New Packages](https://rviews.rstudio.com/2018/12/21/november-2018-top-40-new-packages/)
	- COOL! [lobstr: Visualize R Data Structures with Trees](https://cran.r-project.org/web/packages/lobstr/index.html)
A set of tools for inspecting and understanding R data structures inspired by str(). Includes ast() for visualizing abstract syntax trees, ref() for showing shared references, cst() for showing call stack trees, and obj_size() for computing object sizes.
	- COOL! [dabestr: Data Analysis using Bootstrap-Coupled Estimation](https://cran.r-project.org/web/packages/dabestr/index.html). Offers an alternative to significance testing using bootstrap methods and estimation plots. See Ho et al (2018). There is a vignette on [Bootstrap Confidence Intervals](https://cran.r-project.org/web/packages/dabestr/vignettes/bootstrap-confidence-intervals.html), another on [Statistical Visualizations](https://cran.r-project.org/web/packages/dabestr/vignettes/robust-statistical-visualization.html), and a third on creating [Estimation Plots](https://cran.r-project.org/web/packages/dabestr/vignettes/using-dabestr.html).
	- COOL! [Robust and Beautiful Statistical Visualization](https://cran.r-project.org/web/packages/dabestr/vignettes/robust-statistical-visualization.html)
	- COOL! [Introduction to vtree 0.1.4](https://cran.r-project.org/web/packages/vtree/vignettes/vtree.html) by Nick Barrowmanvtree.
v0.1.4: Provides a function for drawing drawing variable trees plots that display information about hierarchical subsets of a data frame defined by values of categorical variables. The vignette offers an introduction.
- [Using the tidyverse for more than data manipulation: estimating pi with Monte Carlo methods](https://www.brodrigues.co/blog/2018-12-21-tidyverse_pi/)
- COOL! [t-КРИТЕРИЙ СТЬЮДЕНТА - МЕТОД ОЦЕНКИ ЗНАЧИМОСТИ РАЗЛИЧИЙ СРЕДНИХ ВЕЛИЧИН](http://medstatistic.ru/theory/t_cryteria.html)
- COOL! [Reintroducing tsibble: data tools that melt the clock](https://blog.earo.me/2018/12/20/reintro-tsibble/)
- [GEOCOMPUTATION WITH R - THE AFTERWORD](https://nowosad.github.io/post/geocomputation-with-r-the-afterword/)

# 21.12.2018
## A/B Testing
- [Understanding Bayesian A/B testing (using baseball statistics)](http://varianceexplained.org/r/bayesian_ab_baseball/)
- [Bayesian A/B Testing Made Easy](https://www.r-exercises.com/2017/08/21/bayesian_ab_testing_made_easy/)
- COOL! [dabestr: Data Analysis using Bootstrap-Coupled Estimation](https://cran.r-project.org/web/packages/dabestr/index.html). Offers an alternative to significance testing using bootstrap methods and estimation plots. See Ho et al (2018). There is a vignette on [Bootstrap Confidence Intervals](https://cran.r-project.org/web/packages/dabestr/vignettes/bootstrap-confidence-intervals.html), another on [Statistical Visualizations](https://cran.r-project.org/web/packages/dabestr/vignettes/robust-statistical-visualization.html), and a third on creating [Estimation Plots](https://cran.r-project.org/web/packages/dabestr/vignettes/using-dabestr.html).
	- COOL! [Robust and Beautiful Statistical Visualization](https://cran.r-project.org/web/packages/dabestr/vignettes/robust-statistical-visualization.html)
- A/B testing -- частный случай метода [Randomized controlled trial](https://en.wikipedia.org/wiki/Randomized_controlled_trial)
- [Формирование гипотез, запуск A/B-теста и анализ его результатов](https://vc.ru/flood/28728-formirovanie-gipotez-zapusk-a-b-testa-i-analiz-ego-rezultatov)
- [Как не надо анализировать A/B тесты. Проблема подглядывания](https://gopractice.ru/how-not-to-analyze-abtests/)
- [Ухудшающие A/B тесты – cамый недооцененный инструмент менеджера продукта](https://gopractice.ru/ab-test/)
- [A/B тест — это просто](https://habr.com/post/233911/)
Интересная статья. Но есть замечание. Т-критерий Стюдента требует нормальное распределение. Вы предлагаете биномиальное (конверсия). Нормальная аппроксимация справедлива когда pn>5 и n(1-p)>5. [Binomial_proportion_confidence_interval](en.wikipedia.org/wiki/Binomial_proportion_confidence_interval)
Т.е. если на сайте 1% конверсии, то выборка должна быть на 500 кликов минимум. Если мы изучаем клики по банеру c CTR 0.1%, то показов должно быть 5к минимум. Так что не совсем верно: «Этот тест хорошо зарекомендовал себя для небольших объемов данных».
P.S. Не совсем понятно что такое «Стандартное отклонение». Это «среднеквадратичное отклонение» или «стандартная ошибка»?
- [The Complete Guide to A/B Testing: Expert Tips from Google, HubSpot and More](https://www.shopify.com/blog/the-complete-guide-to-ab-testing)
- [Tips for A/B Testing with R](https://www.inwt-statistics.com/read-blog/ab-testing.html)
- COOL! [A/B Testing Example](https://rpubs.com/JanpuHou/280223)
- [A/B testing in Python or R](https://stats.stackexchange.com/questions/12739/a-b-testing-in-python-or-r)
- [Data science you need to know! A/B testing](https://towardsdatascience.com/data-science-you-need-to-know-a-b-testing-f2f12aff619a)
- [randomizeR: Randomization for Clinical Trials](https://cran.r-project.org/web/packages/randomizeR/)
This tool enables the user to choose a randomization procedure based on sound scientific criteria. It comprises the generation of randomization sequences as well the assessment of randomization procedures based on carefully selected criteria. Furthermore, 'randomizeR' provides a function for the comparison of randomization procedures.
- COOL! [Bayesian vs Frequentist A/B Testing – What’s the Difference?](https://conversionxl.com/blog/bayesian-frequentist-ab-testing/)
- COOL! [Bayesian and frequentist A/B split testing](https://github.com/dgrtwo/splittestr). Functions for Bayesian and frequentist A/B split testing. The main purpose of this package is to provide functions and support for [this blog post about Bayesian A/B testing](http://varianceexplained.org/r/bayesian-ab-testing/).
	- [A/B Testing Rigorously (without losing your job)](http://elem.com/~btilly/ab-testing-multiple-looks/part1-rigorous.html)
- COOL! [EvanMiller.org](https://www.evanmiller.org)
	- [How Not To Run an A/B Test](http://www.evanmiller.org/how-not-to-run-an-ab-test.html)
	- [Simple Sequential A/B Testing](https://www.evanmiller.org/sequential-ab-testing.html)
- [The Errors of A/B Testing: Your Conclusions Can Make Things Worse](https://grasshopper.com/blog/the-errors-of-ab-testing-your-conclusions-can-make-things-worse/)
- [A/B Testing Tech Note: determining sample size](https://signalvnoise.com/posts/3004-ab-testing-tech-note-determining-sample-size)
- COOL! [bayesAB](https://frankportman.github.io/bayesAB/). Fast Bayesian Methods for AB Testing
- COOL! [Quick Significance Calculations for A/B Tests in R](http://www.win-vector.com/blog/2018/10/quick-significance-calculations-for-a-b-tests-in-r/)
- [20-80% Faster A/B Tests? Is it real?](http://blog.analytics-toolkit.com/2018/20-80-percent-faster-a-b-tests-real/)
- EARL2017. [Fast and Efficient A/B Testing Analysis with Shiny and SQL](https://earlconf.com/2017/downloads/boston/presentations/EARL2017_-_Boston_-_Charlie_Thompson_-_%20Fast_and_efficient_A:B_testing_analysis.pdf)
- COOL! [Statistical Inference: A Tidy Approach](https://ismayc.github.io/talks/ness-infer/slide_deck.html#1)
- COOL! [An Introduction to Statistical and Data Sciences via R](https://moderndive.com/)
- [A/B Testguide calculator](https://abtestguide.com/calc/)
- COOL! [A/B Testing with Machine Learning - A Step-by-Step Tutorial](https://www.business-science.io/business/2019/03/11/ab-testing-machine-learning.html)

## R
- COOL! [How to rename a variable in R without copying the object?](https://stackoverflow.com/questions/22951811/how-to-rename-a-variable-in-r-without-copying-the-object)
- COOL! Guru99. [apply(), sapply(), tapply() in R with Examples](https://www.guru99.com/r-apply-sapply-tapply.html)

# 20.12.2018
## DS
- COOL! Sphinx. [Open Source Search Server](http://sphinxsearch.com/)
- Sphinx. [Система полнотекстового поиска](https://habr.com/hub/sphinx/)
- COOL! [Presentations from H2O meetups & conferences by the H2O.ai team https://www.meetup.com/pro/h2oai](https://github.com/h2oai/h2o-meetups)

# 17.12.2018
## R
- COOL! Request for comments on planned features for futile.logger 1.5](https://cartesianfaith.com/2018/12/15/request-for-comments-on-planned-features-for-futile-logger-1-5/)
- COOL! [Alternative approaches to scaling Shiny with RStudio Shiny Server, ShinyProxy or custom architecture](https://appsilon.com/alternatives-to-scaling-shiny/)
- [2018-13 Rendering HTML Content in R Graphics](https://stattech.wordpress.fos.auckland.ac.nz/2018/12/17/2018-13-rendering-html-content-in-r-graphics/)
	- Статья ['Rendering HTML Content in R Graphics'](https://www.stat.auckland.ac.nz/~paul/Reports/HTML/layoutengine/layoutengine.html) by Paul Murrell, http://orcid.org/0000-0002-3224-8858]
- [Six Sigma DMAIC Series in R – Part4](https://datascienceplus.com/six-sigma-dmaic-series-in-r-part4/)
- COOL! [linl 0.0.3: Micro release](http://dirk.eddelbuettel.com/blog/2018/12/15/#linl_0.0.3). Our linl package for writing LaTeX letter with (R)markdown had a fairly minor release today, following up on the previous release well over a year ago.

# 12.12.2018
## R & DS
- COOL! [NUMPY AXES EXPLAINED](https://www.sharpsightlabs.com/blog/numpy-axes-explained/)
- [The tidyverse style guide](https://style.tidyverse.org/) by Hadley Wickham
	- [oneliner - a new style guide for styler](https://lorenzwalthert.netlify.com/posts/oneliner/)
	- [strcode - structure your code better](https://lorenzwalthert.netlify.com/posts/strcode1/)
	- [styler - A non-invasive source code formatter for R](https://lorenzwalthert.netlify.com/posts/stylerpost/)
- COOL! [tidyselect: Select from a Set of Strings](https://cran.r-project.org/web/packages/tidyselect/index.html). A backend for the selecting functions of the 'tidyverse'. It makes it easy to implement select-like functions in your own packages in a way that is consistent with other 'tidyverse' interfaces for selection.
	- [dev версия](https://github.com/tidyverse/tidyselect)

## Web Scrapping
- COOL! [Rvest Navigation and Authentication](https://github.com/rstudio/webinars/blob/master/32-Web-Scraping/navigation-and-authentication.md)

# 07.12.2018
## H2O
- запускаем из командной строки с доступом извне: `java -jar h2o.jar -ip 10.0.0.238`
- COOL! [H2O GBM Tuning Tutorial for R](https://www.h2o.ai/blog/h2o-gbm-tuning-tutorial-for-r/)
- [Save and load all h2o cross-validation models in R](https://stackoverflow.com/questions/47696590/save-and-load-all-h2o-cross-validation-models-in-r)
- [An example of saving and loading H2O model in R](https://gist.github.com/woobe/a75ee98fe5cbbe3f9bd47e1acd9b007b)

## DS
- [What are some good error metrics for multi-class classification when you have many objects to classify?](https://www.quora.com/What-are-some-good-error-metrics-for-multi-class-classification-when-you-have-many-objects-to-classify)
- [Good performance metrics for multiclass classification problem besides accuracy?](https://datascience.stackexchange.com/questions/31315/good-performance-metrics-for-multiclass-classification-problem-besides-accuracy)
- [Multi-class Performance Measures](http://notesbyanerd.com/2014/12/17/multi-class-performance-measures/)
- [Can anybody tell about Multi-class Classification performance measures list?](https://www.researchgate.net/post/Can_anybody_tell_about_Multi-class_Classification_performance_measures_list)
- [How do you calculate precision and recall for multiclass classification using confusion matrix?](https://stats.stackexchange.com/questions/51296/how-do-you-calculate-precision-and-recall-for-multiclass-classification-using-co)
```
from sklearn.metrics import confusion_matrix
import numpy as np

labels = ...
predictions = ...

cm = confusion_matrix(labels, predictions)
recall = np.diag(cm) / np.sum(cm, axis = 1)
precision = np.diag(cm) / np.sum(cm, axis = 0)
```
- COOL [What is π?](https://www.quora.com/What-is-math-pi-math/answer/Alon-Amit?ch=10&share=23b7ed43&srid=BGtK)

## Python
- [nbviewer. A simple way to share Jupyter Notebooks](http://nbviewer.jupyter.org/)
- [A simple way to view ipython notebook](https://stackoverflow.com/questions/48481290/a-simple-way-to-view-ipython-notebook)
- [Jupyter Notebook Online in the Cloud, with NumPy, SciPy, matplotlib...](https://paiza.cloud/en/jupyter-notebook-online)
- [Google Collaboratory](https://colab.research.google.com/notebooks/welcome.ipynb). Welcome to Colaboratory! Colaboratory is a free Jupyter notebook environment that requires no setup and runs entirely in the cloud. See our FAQ for more info.

# 05.12.2018
## R
- [Single-node data aggregation benchmark](https://h2oai.github.io/db-benchmark/)
- [ggQC | ggplot Quality Control Charts – New Release](http://r-bar.net/ggqc-ggplot-quality-control-charts/)
- COOL - COOL! [Starspace for NLP #nlproc](http://www.bnosac.be/index.php/blog/84-starspace-for-nlp-nlproc)
- [Making a Profit with Henry Wan in Arkham Horror: The Card Game](https://ntguardian.wordpress.com/2018/12/03/making-profit-henry-wan-arkham-horror/)

## ggplot
- [ggplot2::facet_grid(); facet-specific features](https://rstudio-pubs-static.s3.amazonaws.com/389583_b0df56e5c0954dd6b6762c9f51c7c0b6.html)

## stat
- [«Правда, чистая правда и статистика» или «15 распределений вероятности на все случаи жизни»](https://habr.com/ru/post/311092/)

# 03.12.2018
## R
- [Install and Load Multiple R Packages](https://www.listendata.com/2018/12/install-load-multiple-r-packages.html)
- [Simulating dinosaur populations, with R](https://blog.revolutionanalytics.com/2018/11/jurassic-park.html)
- [Using R: the best thing I’ve changed about my code in years](https://onunicornsandgenes.blog/2018/12/01/using-r-the-best-thing-ive-changed-about-my-code-in-years/)
- [NYC buses: C5.0 classification with R; more than 20 minute delay?](https://datascienceplus.com/nyc-buses-c5-0-classification-with-r-more-than-20-minute-delay/)
- [What hyper-parameters are, and what to do with them; an illustration with ridge regression](https://www.brodrigues.co/blog/2018-12-02-hyper-parameters/)
- [Day 02 – little helper na_omitlist](https://www.statworx.com/de/blog/day-02-little-helper-na_omitlist/)
- COOL! [Why R for data science – and not Python?](http://blog.ephorie.de/why-r-for-data-science-and-not-python)
- COOL! [In Python, when should I use a function instead of a method?](https://stackoverflow.com/questions/8108688/in-python-when-should-i-use-a-function-instead-of-a-method)
- [Installing topicmodels - "fatal error: 'gsl/gsl_rng.h'"](http://tinyheero.github.io/2016/02/20/install-r-topicmodels.html). Также, под Ubuntu проблема возникает [Cannot find gsl header files when compiling {duplicate}](https://askubuntu.com/questions/914592/cannot-find-gsl-header-files-when-compiling). Решение:
	- CentOS: `sudo yum install gsl-devel`
	- Ubuntu: `sudo apt-get install libgsl-dev`
- R Deep Learning Cookbook. [Setting up a bidirectional RNN model](https://www.packtpub.com/mapt/book/big_data_and_business_intelligence/9781787121089/6/ch06lvl1sec69/setting-up-a-bidirectional-rnn-model)
- [How to Visualize Your Recurrent Neural Network with Attention in Keras. A technical discussion and tutorial](https://medium.com/datalogue/attention-in-keras-1892773a4f22)
- [Report on Text Classification using CNN, RNN & HAN](https://medium.com/jatana/report-on-text-classification-using-cnn-rnn-han-f0e887214d5f)
- [Add row in each group using dplyr and add_row()](https://stackoverflow.com/questions/43403282/add-row-in-each-group-using-dplyr-and-add-row)
- [How to remove more than 2 consecutive NA's in a column?](https://stackoverflow.com/questions/42668059/how-to-remove-more-than-2-consecutive-nas-in-a-column)
- [Remove/collapse consecutive duplicate values in sequence](https://stackoverflow.com/questions/27482712/remove-collapse-consecutive-duplicate-values-in-sequence)

## Text mining & R
- [Text Message Classification](https://datascienceplus.com/text-message-classification/)
- [Deep Learning for Text Classification with Keras](https://blogs.rstudio.com/tensorflow/posts/2017-12-07-text-classification-with-keras/)
- [Text classification](https://fasttext.cc/docs/en/supervised-tutorial.html). Library for efficient text classification and representation learning
- [Text Classification is Your New Secret Weapon. Natural Language Processing is Fun! Part 2](https://medium.com/@ageitgey/text-classification-is-your-new-secret-weapon-7ca4fad15788)
- COOL! [A Comprehensive Guide to Understand and Implement Text Classification in Python](https://www.analyticsvidhya.com/blog/2018/04/a-comprehensive-guide-to-understand-and-implement-text-classification-in-python/)
- [Multiclass text classification using R](https://stackoverflow.com/questions/48617076/multiclass-text-classification-using-r)
- COOL! Step-by-step [Multiclass classification for text data](https://rpubs.com/shanmukha_karthik/346007) и тут же вопрос о неработоспособности метода :): [Multiclass classification of text in R](https://stackoverflow.com/questions/48075256/multiclass-classification-of-text-in-r)
- [What are the best packages for multiclass classification in R?](https://www.quora.com/What-are-the-best-packages-for-multiclass-classification-in-R)
- [Collection of SVM Packages](https://github.com/pukkinming/Collection-of-SVM-Packages)
- [liquidSVM: A Fast and Versatile SVM Package](http://www.isa.uni-stuttgart.de/software/)
- [Multiclass classification using scikit-learn](https://www.geeksforgeeks.org/multiclass-classification-using-scikit-learn/)
- COOL! [Чудесный мир Word Embeddings: какие они бывают и зачем нужны?](https://habr.com/company/ods/blog/329410/)
- COOL! [Применение сверточных нейронных сетей для задач NLP](https://habr.com/company/ods/blog/353060/)
- COOL! [Text Classification Using LSTM and visualize Word Embeddings: Part-1](https://medium.com/@sabber/classifying-yelp-review-comments-using-lstm-and-word-embeddings-part-1-eb2275e4066b)
- COOL! [Немного про word2vec: полезная теория](http://nlpx.net/archives/179)
- COOL! [Tensorflow. Vector Representations of Words](https://www.tensorflow.org/tutorials/representation/word2vec)
- [H2O.ai gist. word2vec, transform sentences to vectors by averaging the word-vectors](https://github.com/h2oai/h2o-3/blob/master/h2o-r/demos/rdemo.word2vec.craigslistjobtitles.R)
- [Guide To Multi-Class Multi-Label Classification With Neural Networks In Python](https://www.depends-on-the-definition.com/guide-to-multi-label-classification-with-neural-networks/)
- [Poor multiclass classification using Caret in R {closed}](https://stats.stackexchange.com/questions/310889/poor-multiclass-classification-using-caret-in-r)
- [Multi-Class Classification Using XGBOOST](https://rpubs.com/zxs107020/368478)
- [Compare multiple classification models with caret](https://www.kaggle.com/tobikaggle/compare-multiple-classification-models-with-caret).
	- [7.0.51 Two Class Only](http://topepo.github.io/caret/Two_Class_Only.html)
- [package caret. 6 Available Models](https://topepo.github.io/caret/available-models.html). The models below are available in train. The code behind these protocols can be obtained using the function getModelInfo or by going to the github repository.
- [Weight Lifting Exercise - Multiclass Classification based on Random Forest](https://rstudio-pubs-static.s3.amazonaws.com/245066_f7b5962e8ab84594829b84f06ced39b6.html)
- [Multinomial Logistic Regression Essentials in R](http://www.sthda.com/english/articles/36-classification-methods-essentials/147-multinomial-logistic-regression-essentials-in-r/). The multinomial logistic regression is an extension of the logistic regression (Chapter @ref(logistic-regression)) for multiclass classification tasks. It is used when the outcome involves more than two classes.
- `tokenizers` & `stopwords` packages.

## DS
- COOL! [OpenRefine (formerly Google Refine)](http://openrefine.org/) is a powerful tool for working with messy data: cleaning it; transforming it from one format into another; and extending it with web services and external data.
- CH COOL! [Altinity Stable ClickHouse 18.14.15 Release Notice](https://www.altinity.com/blog/altinity-stable-clickhouse-181415-release)
- [Algorithms. What’s the process for implementing new algorithms in H2O?](http://docs.h2o.ai/h2o/latest-stable/h2o-docs/faq/algorithms.html)

# 30.11.2018 Learning
## R courses & learning
- Отличный курс по R. [UC Business Analytics R Programming Guide](http://uc-r.github.io/tibbles)
- COOL! [Hands-on with dplyr](https://github.com/dgrapov/TeachingDemos/blob/master/Demos/dplyr/hands_on_with_dplyr.md) by Dmitry Grapov
- [Tibbles](https://cran.r-project.org/web/packages/tibble/vignettes/tibble.html). There are three key differences between tibbles and data frames: printing, subsetting, and recycling rules.
- [Lecture 14: ggmap and lubridate packages. 95-868: Exploring and Visualizing Data](https://www.andrew.cmu.edu/user/davidch/95868/Lec14.pdf)
- COOL! [STAT 545. Cheatsheet for dplyr join functions](http://stat545.com/bit001_dplyr-cheatsheet.html) by Jenny Bryan
- [STAT 385: Statistics Programming Methods](http://stat385.thecoatlessprofessor.com/)
Statisticians must be savvy in programming methods useful to the wide variety of analysis that they will be expected to perform. This course provides the foundation for writing and packaging statistical algorithms through the creation of functions and object oriented programming. Fundamental programming techniques and considerations will be emphasized. Students will also create dynamic reports that encapsulate their implemented algorithms. Students must have access to a computer on which they can install software. Prerequisite: STAT 200 or STAT 212.
- Материалы и упражнения. [Index of /courses/RC0818](https://journalismcourses.org/courses/RC0818/)
- [Learn the tidyverse](https://www.tidyverse.org/learn/)
- [Data Manipulation in R by Steph Locke](https://itsalocke.com/). Covers data manipulation in a tidyverse way. [ebook](https://itsalocke.com/files/DataManipulationinR.pdf)
- Старый материал [stat405](http://stat405.had.co.nz/). Introduction to data analysis. Fall 2012. Rice University. Hadley Wickham. hadley@rice.edu
- COOL! purrr tutorial  by Jenny Bryan. [Introduction to map(): extract elements](https://jennybc.github.io/purrr-tutorial/ls01_map-name-position-shortcuts.html)
- COOL! [Rebecca Barter. Learn to purrr](http://www.rebeccabarter.com/blog/2019-08-19_purrr/)
- [Tidyverse for Beginners](https://slides.com/djnavarro/tidyverse-for-beginners#/)
- [Slides for teaching the tidyverse way to total beginners](https://community.rstudio.com/t/slides-for-teaching-the-tidyverse-way-to-total-beginners/3157)
- [teaching and learning materials for data visualization](https://kieranhealy.org/blog/archives/2018/12/12/teaching-and-learning-materials-for-data-visualization/)
- COOL! Ozan Jaquette, @ozanjaquette
Thinking about making switch to R? Here is a link to (10 week) R course I developed with amazing TA Patricia Martin https://ozanj.github.io/rclass/resources/ …. includes lectures, code, datasets, and problem sets .  Based on https://r4ds.had.co.nz/  textbook by @StatGarrett and @hadleywickham
- [R Workshop Series. A Computational Social Scientist Toolkit](https://wesslen.github.io/fall2017-rworkshops/index.html) by Ryan Wesslen
    - Свежайшая презентация!! [RStudio & tidyverse](https://rpubs.com/ryanwesslen/rviz-tutorial-tidy) by Ryan Wesslen, July 18, 2018
    - [tidyverse](https://rpubs.com/ryanwesslen/tidyverse) by Ryan Wesslen, September 27, 2017
- Хадли советует использовать курс Гаррета [rstudio/master-the-tidyverse](https://github.com/rstudio/master-the-tidyverse/tree/master/pdfs). Course contents for Master the Tidyverse. Contribute to rstudio/master-the-tidyverse development by creating an account on GitHub.
- COOL! отличная презентация по ggplot!!! Рассказывать надо будет именно по ней. [A Gentle Guide to the Grammar of Graphics with ggplot2](https://github.com/gadenbuie/gentle-ggplot2). The slides are available here: https://gadenbuie.github.io/gentle-ggplot2
- COOL! Текст, а не презентация, но много деталей и оригинальных картинок. [Introduction to ggplot2](https://rawgit.com/bioinformatics-core-shared-training/r-intermediate/master/ggplot2.html) by Thomas Carroll
MRC-CSC/Shared-bioinformatics-training
требуемые файлы данных здесь: https://github.com/bioinformatics-core-shared-training/r-intermediate
- COOL! [Code and slides for RStudio webinars https://resources.rstudio.com/webinars](https://github.com/rstudio/webinars)
- COOL! [Happy R Users Purrr by Charlotte Wickham](https://github.com/cwickham/purrr-tutorial)
	- [Purrr workshop materials](https://github.com/cwickham/purrr-tutorial)
- [reprex rstudio webinar](https://github.com/tidyverse/reprex/tree/master/slides/2018-09_reprex-rstudio-webinar)
- [Get out of Excel free](https://github.com/rsheets/jailbreakr)
- Похоже, что по материалам DataCamp сделан неплохой справочник [ugo_r_doc](https://ugoproto.github.io/ugo_r_doc/Data_Analysis_in_R,_the_data.table_Way/#mixing-it-together-lapply-sd-sdcols-and-n)
- Работа со строками
	- похоже, что сделан по мотивам datacamp курса Шарлотты [String Manipulation in R with stringr](https://rpubs.com/iPhuoc/stringr_manipulation) by Khac Phuoc Le
	- [Text Processing Presentation](https://robchavez.github.io/datascience_gallery/html_only/text_processing.html) by Stephanie Gluck & Pooya Razavi
	- [Strung Out On String Ops – A Brief Comparison of stringi and stringr](https://rud.is/b/2017/02/06/strung-out-on-string-ops-a-brief-comparison-of-stringi-and-stringr/)
	- [Regular Expressions Every R programmer Should Know](https://blog.jumpingrivers.com/posts/2018/top_regular_expressions_r_stringr/)
	- [Handling Strings with R](http://www.gastonsanchez.com/r4strings/) by Gaston Sanchez, 2018-04-19
	- [Handling and Processing Strings in R](http://gastonsanchez.com/Handling_and_Processing_Strings_in_R.pdf), Gaston Sanchez
	- [Marek Gagolewski, stringi Package for R](http://www.gagolewski.com/software/stringi/)
- [PH525x series - Biomedical Data Science](http://genomicsclass.github.io/book/)

## R exercises & Learning
- [Exercism](https://exercism.io/). Code practice and mentorship for everyone.
Level up your programming skills with 2,652 exercises across 48 languages, and insightful discussion with our dedicated team of welcoming mentors. Exercism is 100% free forever.
- [R for Data Science: Exercise Solutions](https://jrnold.github.io/r4ds-exercise-solutions/) by Jeffrey B. Arnold, January 17, 2019
- [R exercises](https://www.r-exercises.com/start-here-to-learn-r/). Start here to learn R!
- [R programming Exercises, Practice, Solution](https://www.w3resource.com/r-programming-exercises/)
- [Introduction to R workshop notes](https://tutorials.iq.harvard.edu/R/Rintro/Rintro.html)
- data:
	- [hadley/babynames](https://github.com/hadley/babynames). An R package containing US baby names from the SSA

## R presentations & learning
- [Visualisation with ggplot2](https://privefl.github.io/R-presentation/ggplot2.html#1)
- [R you ready to ggplot?](http://tonyfujs.github.io/ggplot2/)
	- [R you ready to ggplot2?](http://tonyfujs.github.io/ggplot_post/02_gg_basic) (Presentation) Basic Plots. October 15, 2014. Tony Fujs
- [R Graphics: Introduction to ggplot2](https://stats.idre.ucla.edu/stat/data/intro_ggplot2/ggplot2_intro_slidy.html#(1))
	- [Introduction to ggplot2 seminar](https://stats.idre.ucla.edu/r/seminars/ggplot2_intro/)
- [Lecture 4: R Graphics with ggplot2](http://www.statsoft.org/wp-content/uploads/2017/09/Lecture4_ggplot2.html#/). HKU STAT3622 Data Visualization by Dr. Aijun Zhang, 18 September 2017
- [R graphics with ggplot2 workshop notes](https://tutorials.iq.harvard.edu/R/Rgraphics/Rgraphics.html)
- [The Complete ggplot2 Tutorial - Part1 | Introduction To ggplot2 (Full R code)](http://r-statistics.co/Complete-Ggplot2-Tutorial-Part1-With-R-Code.html)
- [Lecture 3: Graphics in R. 95-868: Exploring and Visualizing Data](https://www.andrew.cmu.edu/user/davidch/95868/Lec3.pdf)
- [Lecture 9: An introduction to ggplot2](https://seananderson.ca/courses/12-ggplot2/ggplot2_notes.pdf) by Sean C. Anderson, November 21, 2012
- COOL! [Why xaringan / remark.js for HTML5 Presentations?](https://yihui.name/en/2017/08/why-xaringan-remark-js/)

## Text mining
- [textrank: Summarize Text by Ranking Sentences and Finding Keywords](https://cran.r-project.org/web/packages/textrank/index.html)
- COOL! [Изучаем синтаксические парсеры для русского языка](https://habr.com/company/sberbank/blog/418701/). Блог компании Сбербанк, Искусственный интеллект, Машинное обучение

# 29.11.2018
## R
- [Collection of most color palettes in a single R package](https://www.hvitfeldt.me/r/paletteer/)
- [The background to useR! 2018](http://dicook.org/2018/10/10/content/post/2018-10-10-user2018/)
- [Find the best locations for facilities using maxcovr](https://github.com/njtierney/user-2018-maxcovr-talk). A talk presented by Nick Tierney, presented at UseR!2018
- [fasster](https://mitchelloharawild.com/user2018/). Forecasting multiple seasonality with state switching
- R FAQ. [7.31 Why doesn’t R think these numbers are equal?](https://cran.r-project.org/doc/FAQ/R-FAQ.html#Why-doesn_0027t-R-think-these-numbers-are-equal_003f)
- Statistical Inference: A Tidy Approach. The infer R package
	- Slides available at [http://bit.ly/infer-useR](http://bit.ly/infer-useR)
	- Package webpage at [https://infer.netlify.com](https://infer.netlify.com)

# 28.11.2018
## R
- COOL! [Postman](https://www.getpostman.com/). Developers use Postman to build modern software for the API-first world.
- [tsibble 0.6.0](https://cran.rstudio.com/web/packages/tsibble/news/news.html)
- [Slack and Plumber, Part Two](https://rviews.rstudio.com/2018/11/27/slack-and-plumber-part-two/)
- COOL! [Using clustering to find points in an image](https://privefl.github.io/blog/using-clustering-to-find-points-in-an-image/)
- [styler 1.1.0](https://lorenzwalthert.netlify.com/posts/styler-v1.1/)
- r `sub()` vs `gsub()`:
	- [Difference between sub and gsub in R](http://www.datasciencemadesimple.com/sub-gsub-function-in-r/)
	- [sub, gsub](http://rfunction.com/archives/2354)
	- [Difference between sub and gsub in R](https://gist.github.com/soujanno/8464a2130e71737b56f7a543a373adf2)
- [flatxml package](http://www.zuckarelli.de/flatxml/index.html)
- The [xml2 package](http://xml2.r-lib.org/) is a binding to libxml2, making it easy to work with HTML and XML from R. The API is somewhat inspired by jQuery.
	- [Parse and process XML (and HTML) with xml2](https://blog.rstudio.com/2015/04/21/xml2/) by Hadley Wickham, 2015-04-21
- [Using xml schema and xslt in R](https://ropensci.org/blog/2017/01/10/xslt-release/)
- [This R Data Import Tutorial Is Everything You Need](https://www.datacamp.com/community/tutorials/r-data-import-tutorial)
- [Project-oriented workflow](https://www.tidyverse.org/articles/2017/12/workflow-vs-script/). What’s wrong with setwd()?

# 27.11.2018
## R
- А вот возможные корни проблемы с R notebook: [Output missing from notebook HTML, but not regular HTML](https://github.com/rstudio/rmarkdown/issues/1002). Слишком сложные зависимости.
- Оказалось все гораздо проще. Процесс инициализации пакетов включает всякие ненужные операции при выводе на экран. Надо их гасить опциями и все получается Ок!
```{r load packages, message=FALSE, warning=FALSE, include=FALSE}
```
- [BTYDplus: Probabilistic Models for Assessing and Predicting your Customer Base](https://cran.r-project.org/web/packages/BTYDplus/)
- [A Chrome Remote Interface written in R](https://github.com/RLesur/crrri)

# 26.11.2018
## R
- [RStudio Cheatsheets Source](https://github.com/rstudio/cheatsheets)
- [Interactive directory input in Shiny app (R)](https://stackoverflow.com/questions/39196743/interactive-directory-input-in-shiny-app-r)
- [An shiny input widget for selecting directories](https://github.com/wleepang/shiny-directory-input)
- [thomasp85/shinyFiles](https://github.com/thomasp85/shinyFiles). shinyFiles: A Server-Side File System Viewer for Shiny
Provides functionality for client-side navigation of the server side file system in shiny apps. In case the app is running locally this gives the user direct access to the file system without the need to "download" files to a temporary location. Both file and folder selection as well as file saving is available.
- [OneR – fascinating insights through simple rules](http://blog.ephorie.de/oner-fascinating-insights-through-simple-rules)


# 23.11.2018
## R
- [Creating List with Iterator](https://statcompute.wordpress.com/2018/11/22/creating-list-with-iterator/)


# 22.11.2018
## DS & R
- COOL! [Dealing with failed projects](https://edwinth.github.io/blog/failed-projects/)
- COOL! [So your data science project isn’t working](https://medium.com/@skyetetra/so-your-data-science-project-isnt-working-7bf57e3f12f1)
- COOL! [Slides from my talks about Demystifying Big Data and Deep Learning (and how to get started)](https://shirinsplayground.netlify.com/2018/11/slides_demystifying_dl/)
- COOL! [circlize: circular visualization in R](https://github.com/jokergoo/circlize)
- [ACHINE LEARNING. IN CONVERSATION WITH JELENA ILIC, SENIOR DATA SCIENTIST AT MANGO SOLUTIONS](https://www.mango-solutions.com/blog/machine-learning-in-conversation-with-jelena-ilic-senior-data-scientist-at-mango-solutions)
- [OpenCPU 2.1 Release: Scalable R Services](https://www.opencpu.org/posts/opencpu-201/), November 22, 2018
- [R > PYTHON: A CONCRETE EXAMPLE](https://matloff.wordpress.com/2018/11/20/r-python-a-concrete-example/)
- [Make your R code nicer with roperators](https://www.happylittlescripts.com/2018/09/make-your-r-code-nicer-with-roperators.html)

# 19.11.2018
- [The tidy caret interface in R](https://poissonisfish.wordpress.com/2018/11/16/the-all-new-caret-interface-in-r/)
- [Make Beautiful Tables with the Formattable Package](https://www.displayr.com/formattable/)
- COOL! [Convert Data Frame to Dictionary List in R](https://statcompute.wordpress.com/2018/11/16/convert-data-frame-to-dictionary-list-in-r/)
- [zero counts in dplyr](https://kieranhealy.org/blog/archives/2018/11/19/zero-counts-in-dplyr/)
- [RStudio 1.2 Preview: The Little Things](https://blog.rstudio.com/2018/11/19/rstudio-1-2-preview-the-little-things/) by Jonathan McPherson, 2018-11-19

# 16.11.2018
- [ggplot geom_bar with stat = “sum”](https://stackoverflow.com/questions/47818188/ggplot-geom-bar-with-stat-sum)
- [stat_sum and stat_identity give weird results](https://stackoverflow.com/questions/27965291/stat-sum-and-stat-identity-give-weird-results/27965637#27965637)

# 15.11.2018
## R
- [Shiny 1.2.0: Plot caching](https://blog.rstudio.com/2018/11/13/shiny-1-2-0/) by Joe Cheng, 2018-11-13
- OPEN SOURCE AUTOMATION. Automating everyday tasks with open source code. [THOSE “OTHER” APPLY FUNCTIONS…](http://theautomatic.net/2018/11/13/those-other-apply-functions/)
- [Windows Clipboard Access with R](http://r-bar.net/r-clipboard-data-copy-paste/)
- COOL! [Searching for the optimal hyper-parameters of an ARIMA model in parallel: the tidy gridsearch approach](https://www.brodrigues.co/blog/2018-11-15-tidy_gridsearch/)
- [Writing Data From R to Excel Files (xls|xlsx)](http://www.sthda.com/english/wiki/writing-data-from-r-to-excel-files-xls-xlsx)
- [Opposite of %in%](https://stackoverflow.com/questions/5831794/opposite-of-in)

# 13.11.2018
## R
- [gsubfn: Utilities for Strings and Function Arguments](https://cran.r-project.org/web/packages/gsubfn/index.html)
- COOL!! [Faster way to trim a long character vector in R {closed}](https://stackoverflow.com/questions/39152317/faster-way-to-trim-a-long-character-vector-in-r). !!! **It's just that `strtrim()` is fairly slow.** Answer: Use `(substr(x, 1, 3))`
- ряд полезных функций: `stringi::stri_trim_both`, `stringr::str_squish`, `stringr::str_trunc`, `rlang::squash_chr`
- [Recode values with character subsetting](https://tjmahr.github.io/recode-values-with-character-subsetting/)
- Разбивка на диапазоны. Ключевое слово -- "ДИСКРЕТИЗАЦИЯ". См. область из машинного обучения.
	- `discretize {arules}`, см. [Convert a Continuous Variable into a Categorical Variable](http://www.inside-r.org/packages/cran/arules/docs/discretize)
	- [Convert continuous numeric values to discrete categories defined by intervals](https://stackoverflow.com/questions/13559076/convert-continuous-numeric-values-to-discrete-categories-defined-by-intervals)
	- [Categorize continuous variable with dplyr {duplicate}](https://stackoverflow.com/questions/40380112/categorize-continuous-variable-with-dplyr)
	- [discretization in R with `arules` package](https://stackoverflow.com/questions/32100476/discretization-in-r-with-arules-package)

- как создать "тепловые" карты с надписями:
	- [Hello, Dorling! (Creating Dorling Cartograms from R Spatial Objects + Introducing Prism Skeleton)](https://rud.is/b/2018/06/03/hello-dorling-creating-dorling-cartograms-from-r-spatial-objects-introducing-prism-skeleton/)
	- [Wrangling Data Table Out Of the FBI 2017 IC3 Crime Report](https://rud.is/b/2018/05/08/wrangling-data-table-out-of-the-fbi-2017-ic3-crime-report/)
	- [Compute/Visualize Drive Space Consumption of Your Installed R Packages](https://rud.is/b/2018/04/01/compute-visualize-drive-space-consumption-of-your-installed-r-packages/)
	- [Statebins Reimagined](https://rud.is/b/2017/11/18/statebins-reimagined/)
	- COOL! [ggraph: An Implementation of Grammar of Graphics for Graphs and Networks](https://cran.r-project.org/web/packages/ggraph/index.html)
	- [A Very Palette-able Post](https://rud.is/b/2017/05/21/a-very-pallete-able-post/)
	- [Making Faceted Heatmaps with ggplot2](https://rud.is/b/2016/02/14/making-faceted-heatmaps-with-ggplot2/)



# 09.11.2018
## R & JSON with jqr

## parallel
- COOL! Как правильно сделать? [R foreach with .combine=rbindlist](https://stackoverflow.com/questions/17411223/r-foreach-with-combine-rbindlist)
- Проблема с NULL значениями при слиянии списков с помощью rbindlist: ["Is there a more efficient way to replace NULL with NA in a list?"](https://stackoverflow.com/questions/22870198/is-there-a-more-efficient-way-to-replace-null-with-na-in-a-list/22870450)
	- [rbinding a list of data frame R with NULL](https://stackoverflow.com/questions/48793099/rbinding-a-list-of-data-frame-r-with-null)
	- [rbindlist should deal with NULL values #1871 {Open}](https://github.com/Rdatatable/data.table/issues/1871)
- [foreach: Keep names](https://stackoverflow.com/questions/27276269/foreach-keep-names)
- COOL! [A Foreach Parallel Adaptor using Futures](https://cran.r-project.org/web/packages/doFuture/vignettes/doFuture.html). Introduction
- COOL! [R - parallel computing in 5 minutes (with foreach and doParallel)](http://blog.aicry.com/r-parallel-computing-in-5-minutes/index.html)
- COOL! [GNU Parallel Tutorial](https://www.gnu.org/software/parallel/parallel_tutorial.html): `sudo yum install parallel`

# 08.11.2018
## R JIT
- "Efficient R programming". [7.4 The byte compiler](https://csgillespie.github.io/efficientR/7-4-the-byte-compiler.html)
- [The new R compiler package in R 2.13.0: Some first experiments](http://dirk.eddelbuettel.com/blog/2011/04/12/)
- [How to make best use of the byte compiler in R](https://blog.revolutionanalytics.com/2017/08/take-advantage-compiler.html)

# 07.11.2018
## R
- COOL! [readtext: Import and Handling for Plain and Formatted Text Files](https://cran.r-project.org/web/packages/readtext/index.html)
Functions for importing and handling text files and formatted text files with additional meta-data, such including '.csv', '.tab', '.json', '.xml', '.html', '.pdf', '.doc', '.docx', '.xls', '.xlsx', and others.
- [Source and List: Organizing R Shiny Apps](http://r-bar.net/organize-r-shiny-list-source/)
- COOL! ['How do neural nets learn?' A step by step explanation using the H2O Deep Learning algorithm](https://shirinsplayground.netlify.com/2018/11/neural_nets_explained/)
- [Using httr to Detect HTTP(s) Redirects](https://petermeissner.de/blog/2018/11/07/using-httr-to-detect-redirects/)
- COOL! [httpbin.org. A simple HTTP Request & Response Service.](https://httpbin.org/)
- [ndjson Newline Delimited JSON](http://ndjson.org/)

## GCC
- При инсталляции пакета `ndjson` под CentOS получил ошибку "C++14 standard requested but CXX14 is not defined".
PostPosted: Tue Jun 19, 2018 5:30 pm    Post subject:	Reply with quote
Are you able to compile your example with g++? I can't seem to replicate your issue on machines that have a more recent version of libstdc++
From this page [https://gcc.gnu.org/projects/cxx-status.html#cxx14](https://gcc.gnu.org/projects/cxx-status.html#cxx14) it looks like 4.8.5 doesn't fully support C++14
```
$ lsb_release -id
Distributor ID:   CentOS
Description:   CentOS Linux release 7.5.1804 (Core)
$ which g++
/usr/bin/g++
$ g++ --version
g++ (GCC) 4.8.5 20150623 (Red Hat 4.8.5-28)
```

## yum
- Как поставить в CentOS пакет меньшей версии? Ответ: Командой `sudo yum downgrade <rpm>`

## R. Document similarity
- COOL! [Documents similarity](http://text2vec.org/similarity.html) by Dmitriy Selivanov, 2017-08-08
- [Document Similarity with R](http://fredgibbs.net/tutorials/document-similarity-with-r.html)
- COOL! [quanteda: Quantitative Analysis of Textual Data](https://quanteda.io/)
- COOL! Text2vec [Blog](http://dsnotes.com/tags/text2vec/):
	- COOL! [Analyzing texts with text2vec package](https://dsnotes.com/post/text2vec/)
- [tokenizers: Fast, Consistent Tokenization of Natural Language Text](https://cran.r-project.org/web/packages/tokenizers/index.html)
Convert natural language text into tokens. Includes tokenizers for shingled n-grams, skip n-grams, words, word stems, sentences, paragraphs, characters, shingled characters, lines, tweets, Penn Treebank, regular expressions, as well as functions for counting characters, words, and sentences, and a function for splitting longer texts into separate documents, each with the same number of words. The tokenizers have a consistent interface, and the package is built on the 'stringi' and 'Rcpp' packages for fast yet correct tokenization in 'UTF-8'.
- [Demystifying Text Analytics part 3 — Finding Similar Documents with Cosine Similarity in R](https://blog.exploratory.io/demystifying-text-analytics-finding-similar-documents-with-cosine-similarity-e7b9e5b8e515)
- [Pairwise comparisons for document similarity](https://cran.r-project.org/web/packages/textreuse/vignettes/textreuse-pairwise.html)
- [textrank: Summarize Text by Ranking Sentences and Finding Keywords](https://cran.r-project.org/web/packages/textrank/index.html)
- [udpipe: Tokenization, Parts of Speech Tagging, Lemmatization and Dependency Parsing with the 'UDPipe' 'NLP' Toolkit](https://cran.r-project.org/web/packages/udpipe/index.html)
- [Using String Distance {stringdist} To Handle Large Text Factors, Cluster Them Into Supersets](https://amunategui.github.io/stringdist/)

## LDA (Latent Dirichlet Allocation)
- COOL! [A gentle introduction to topic modeling using R](https://eight2late.wordpress.com/2015/09/29/a-gentle-introduction-to-topic-modeling-using-r/)
- [Введение для новичков: что такое Латентное размещение Дирихле (LDA)?](https://mebius.io/analysis/intro-to-LDA). Популярно о сложном — об известнейшем методе машинного обучения под названием «Латентное размещение Дирихле».
- [Bayesian and frequentist reasoning in plain English](http://stats.stackexchange.com/questions/22/bayesian-and-frequentist-reasoning-in-plain-english)
- Блестящий цикла материалов про LDA:
	- [Вероятностные модели: от наивного Байеса к LDA, часть 1](https://habrahabr.ru/company/surfingbird/blog/228249/)
	- [Вероятностные модели: LDA, часть 2](https://habrahabr.ru/company/surfingbird/blog/230103/)
- [Find out more about Themescape](http://ip-science.thomsonreuters.com/winningmove/secure/TI_Themescape_QT.html)
- [Консалтинговая контора по DataScience](https://projectbotticelli.com/). Взял с конференции Микрософт:[Putting Science into the Business of Data Science](https://channel9.msdn.com/Events/Machine-Learning-and-Data-Sciences-Conference/Data-Science-Summit-2016/MSDSS05), Date: September 26, 2016, Speakers: Rafal Lukawiecki
- [topicmodels: Topic Models](https://cran.r-project.org/web/packages/topicmodels/index.html)
Provides an interface to the C code for Latent Dirichlet Allocation (LDA) models and Correlated Topics Models (CTM) by David M. Blei and co-authors and the C++ code for fitting LDA models using Gibbs sampling by Xuan-Hieu Phan and co-authors

Новинки
- [Your Easy Guide to Latent Dirichlet Allocation](https://medium.com/@lettier/how-does-lda-work-ill-explain-using-emoji-108abf40fa7d)
- [Spark ML -- Latent Dirichlet Allocation](https://spark.rstudio.com/reference/ml_lda/)
- [Topic modeling with LDA: MLlib meets GraphX](https://databricks.com/blog/2015/03/25/topic-modeling-with-lda-mllib-meets-graphx.html)

# 06.11.2018
## R
- [Visualize the Business Value of your Predictive Models with `modelplotr`](https://modelplot.github.io/modelplotr.html) by Jurriaan Nagelkerke Pieter Marcus | 03 Nov 2018
- [R tip: Make Your Results Clear with sigr](http://www.win-vector.com/blog/2018/11/r-tip-make-your-results-clear-with-sigr/)
- [coalesce with wrapr](http://www.win-vector.com/blog/2018/11/coalesce-with-wrapr/)
- [NEW R CHEATSHEET: DATA SCIENCE WORKFLOW WITH R](https://www.business-science.io/learning-r/2018/11/04/data-science-r-cheatsheet.html)
- [Coding Gradient boosted machines in 100 lines of code](https://www.statworx.com/de/blog/coding-gradient-boosted-machines-in-100-lines-of-code/)
- COOL! Explore Your Dataset in R](https://www.littlemissdata.com/blog/simple-eda)
- [EARL HOUSTON: INTERVIEW WITH HADLEY WICKHAM](https://www.mango-solutions.com/blog/earl-houston-interview-with-hadley-wickham)
- [Interactive plots - advanced](https://shiny.rstudio.com/articles/plot-interaction-advanced.html), LAST UPDATED: 30 MAY 2017

## Sentiment Analysis
- [Twitter sentiment analysis with Machine Learning in R using doc2vec approach (part 1)](https://analyzecore.com/2017/02/08/twitter-sentiment-analysis-doc2vec/) by Sergey Bryl', Data Scientist @ MacPaw Inc
- [A gentle introduction to Doc2Vec](https://medium.com/scaleabout/a-gentle-introduction-to-doc2vec-db3e8c0cce5e)

# 03.11.2018
## R
- [What R version do you really need for a package?](https://www.jumpingrivers.com/blog/what-r-version-do-you-really-need-for-a-package/)
- [Master R shiny: One trick to build maintainable and scalable event chains](https://www.statworx.com/de/blog/master-r-shiny-one-trick-to-build-maintainable-and-scalable-event-chains/)
- [Normalize by Group](https://stackoverflow.com/questions/43680246/normalize-by-group)

# 31.10.2018
## R
- [R : CREATE SAMPLE / DUMMY DATA](https://www.listendata.com/2016/02/r-create-dummy-data.html)
- COOL! [trinker/wakefield](https://github.com/trinker/wakefield). Generate random data sets
- [How do I create a vector of random dates between two time points in R?](https://stackoverflow.com/questions/45381759/how-do-i-create-a-vector-of-random-dates-between-two-time-points-in-r)
- [R: Sample a vector with replacement multiple times](https://stackoverflow.com/questions/10264025/r-sample-a-vector-with-replacement-multiple-times)
- [Using the RcppArmadillo-based Implementation of R's sample()](http://gallery.rcpp.org/articles/using-the-Rcpp-based-sample-implementation/)


## R
- COOL! [Extracting Specific Lines from a Large (Compressed) Text File](https://statr.me/2018/05/extracting-lines-from-a-large-file/)
- [Getting started Stamen maps with ggmap](https://statisticaloddsandends.wordpress.com/2018/10/25/getting-started-stamen-maps-with-ggmap/)
- [How to perform merges (joins) on two or more data frames with base R, tidyverse and data.table](https://jozefhajnala.gitlab.io/r/r006-merge/)


## DS
- COOL! [Welcome to the 2018 edition of fast.ai's 7 week course, Practical Deep Learning For Coders, Part 1, taught by Jeremy Howard (Kaggle's #1 competitor 2 years running, and founder of Enlitic).](http://course.fast.ai/index.html)


# 25.10.2018
## R
- COOL! [benchplot {ggplot2}](https://ggplot2.tidyverse.org/reference/benchplot.html). Benchmark plot creation time. Broken down into construct, build, render and draw times.
- [Create a Glossary in R Markdown](https://liao961120.github.io/2018/10/24/glossary-maker.html)
- [“Demystifying Data Science” remote notes](http://research.libd.org/rstatsclub/2018/10/24/demystifying-data-science-remote-notes/)
- R & CRUD:
	- [DT 0.4: Editing Tables, Smart Filtering, and More](https://blog.rstudio.com/2018/03/29/dt-0-4/) by Yihui Xie, 2018-03-29
	- [Make it possible to edit values in table #480 {Merged}](https://github.com/rstudio/DT/pull/480) yihui merged 3 commits into master from feature/editor on 18 Jan
	- [barbara: Here’s a CRUD app I built in Shiny 295, using SQLite.](https://github.com/bborgesr/wsds2017/tree/master/app)
	- [rhandsontable](https://jrowen.github.io/rhandsontable/). Introduction. rhandsontable is a htmlwidget based on the handsontable.js library.
	- [Building CRUD with Shiny](https://community.rstudio.com/t/building-crud-with-shiny/2881/8)
- COOL! [Streamulus](http://iritkatriel.github.io/streamulus/). A C++ Embedded Language for Event Stream Processing
	- [RcppStreams](http://dirk.eddelbuettel.com/code/rcpp.streams.html)


# 24.10.2018
## Math. p-value
- [Three common misuses of P values](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5042133/)
- [What the P values really tell us](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5665734/)
- [Understanding p-value](https://stats.stackexchange.com/questions/44769/understanding-p-value)
- COOL! [What is the meaning of p values and t values in statistical tests?](https://stats.stackexchange.com/questions/31/what-is-the-meaning-of-p-values-and-t-values-in-statistical-tests)- - [Альтернатива p-value для проверки статистической гипотезы](https://medium.com/@denisgabaydulin/%D0%B0%D0%BB%D1%8C%D1%82%D0%B5%D1%80%D0%BD%D0%B0%D1%82%D0%B8%D0%B2%D0%B0-p-value-%D0%B4%D0%BB%D1%8F-%D0%BF%D1%80%D0%BE%D0%B2%D0%B5%D1%80%D0%BA%D0%B8-%D1%81%D1%82%D0%B0%D1%82%D0%B8%D1%81%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%BE%D0%B9-%D0%B3%D0%B8%D0%BF%D0%BE%D1%82%D0%B5%D0%B7%D1%8B-3235fcf93f1e)
- [There is still only one test](http://allendowney.blogspot.ru/2016/06/there-is-still-only-one-test.html)
- [There is only one test!](http://allendowney.blogspot.ru/2011/05/there-is-only-one-test.html)
- [Remember: p-values Are Not Effect Sizes](http://www.win-vector.com/blog/2017/09/remember-p-values-are-not-effect-sizes/)
- Неплохое обучающее видео. [Hypothesis testing and p-values](https://www.khanacademy.org/math/statistics-probability/significance-tests-one-sample/tests-about-population-mean/v/hypothesis-testing-and-p-values)
- [P-VALUES, SAMPLE SIZE AND DATA MINING](http://skranz.github.io//r/2018/04/09/Sample_Size_P-Values_and_Data_Mining.html)
- [P-VALUES FROM RANDOM EFFECTS LINEAR REGRESSION MODELS](http://www.datasurg.net/2018/01/13/p-values-from-random-effects-linear-regression-models/)
- COOL! R: Анализ и визуализация данных. [Классические методы статистики: критерий хи-квадрат](http://r-analytics.blogspot.ru/2012/08/blog-post.html)
- COOL! R: Анализ и визуализация данных. [Протокол разведочного анализа данных: проверка на нормальность распределения](https://r-analytics.blogspot.com/2012/06/blog-post_14.html)
- [Ещё раз про оценку научных данных и, наконец, про p-value](http://jescid.livejournal.com/481888.html)
- COOL [Scientific method: Statistical errors](http://www.nature.com/news/scientific-method-statistical-errors-1.14700). P values, the 'gold standard' of statistical validity, are not as reliable as many scientists assume.
- COOL! Statistics for Hackers
	- [Jake Vanderplas - Statistics for Hackers - PyCon 2016](https://www.youtube.com/watch?v=Iq9DzN6mvYA&t=4s). [Презентация "Statistics for Hackers"](https://speakerdeck.com/jakevdp/statistics-for-hackers)
	- [Statistics for Hackers](http://christopherroach.com/articles/statistics-for-hackers/)
	- [Jake VanderPlas](http://vanderplas.com/)
	- [“Resampling: The New Statistics”](http://onlinebooks.library.upenn.edu/webbin/book/lookupid?key=olbp28567) by Julian L. Simon, Second Edition published October 1997
	- [Probabilistic Programming & Bayesian Methods for Hackers](http://camdavidsonpilon.github.io/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers/)
	- [Statistical Thinking for Data Science SciPy2015](https://youtu.be/TGGGDpb04Yc)


## Math. SD vs SE
- [Standard deviations and standard errors](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1255808/)
- [Standard deviation vs standard error of sample mean](https://stats.stackexchange.com/questions/205338/standard-deviation-vs-standard-error-of-sample-mean).
Standard error refers to the standard deviation of the sampling distribution of a statistic.
- [Converting standard error to standard deviation?](https://stats.stackexchange.com/questions/15505/converting-standard-error-to-standard-deviation)
- [Standard Deviation vs Standard Error](https://math.stackexchange.com/questions/193045/standard-deviation-vs-standard-error)
- [Difference between standard error and standard deviation](https://stats.stackexchange.com/questions/32318/difference-between-standard-error-and-standard-deviation).
```
Here is a more practical (and not mathematical) answer:

The SD (standard deviation) quantifies scatter — how much the values vary from one another.
The SEM (standard error of the mean) quantifies how precisely you know the true mean of the population. It takes into account both the value of the SD and the sample size.
Both SD and SEM are in the same units -- the units of the data.
The SEM, by definition, is always smaller than the SD.
The SEM gets smaller as your samples get larger. This makes sense, because the mean of a large sample is likely to be closer to the true population mean than is the mean of a small sample. With a huge sample, you'll know the value of the mean with a lot of precision even if the data are very scattered.
The SD does not change predictably as you acquire more data. The SD you compute from a sample is the best possible estimate of the SD of the overall population. As you collect more data, you'll assess the SD of the population with more precision. But you can't predict whether the SD from a larger sample will be bigger or smaller than the SD from a small sample. (This is a simplification, not quite true. See comments below.)
Note that standard errors can be computed for almost any parameter you compute from data, not just the mean. The phrase "the standard error" is a bit ambiguous. The points above refer only to the standard error of the mean.
```
- Наглядный пример с собачками [Standard Deviation and Variance](https://www.mathsisfun.com/data/standard-deviation.html)

## R
- [Is plumber multithreading or single threading ? #170 {Closed}](https://github.com/trestletech/plumber/issues/170)
	- [Rplumber docs. Chapter 7 Hosting](https://www.rplumber.io/docs/hosting.html)

## R & web scrapping\SOAP
- COOL! [How I became a crolute i.e. an user of the crul package](http://www.masalmon.eu/2017/06/30/crolute/). Maëlle blog. (curl/httr)
A few months ago rOpenSci’s Scott Chamberlain asked me for feedback about a new package of his called crul, an http client like httr, so basically something you use for e.g. writing a package interfacing an API. He told me that a great thing about crul was that it supports asynchronous requests. I felt utterly uncool because I had no idea what this meant although I had already written quite a few API packages (for instance ropenaq, riem and opencage).
	- [crul: HTTP Client](https://cran.rstudio.com/web/packages/crul/). A simple HTTP client, with tools for making HTTP requests, and mocking HTTP requests. (curl/httr)
	- [R for cats and cat lovers. An intro to R for new programmers](https://rforcats.net/). This is an introduction to R. I promise this will be fun. Since you have never used a programming language before, or any language for that matter, you won’t be tainted by other programming languages with different ways of doing things. This is good - we can teach you the R way of doing things.
- COOL! [Introducing routr - Routing of HTTP and WebSocket in R](http://www.data-imaginist.com/2017/Introducing-routr/)



# 23.10.2018
## R
- COOL! [Back To The DT Package After Two Years. Why I disappeared for so long...](https://yihui.name/en/2018/01/back-to-dt/) by Yihui Xie, 2018-01-19
- COOL! [Knitr options. Chunk options and package options](https://yihui.name/knitr/options/)
- COOL! [One Little Thing: the knitr Chunk Option include=FALSE](https://yihui.name/en/2017/11/knitr-include-false/) by Yihui Xie, 2017-11-22
- Вопрос Генриха:
	- [which sampling function in R help to provide required schema of sampling?](https://stackoverflow.com/questions/52662055/which-sampling-function-in-r-help-to-provide-required-schema-of-sampling)
	- [AlgDesign: Algorithmic Experimental Design](https://cran.r-project.org/web/packages/AlgDesign/index.html). Algorithmic experimental designs. Calculates exact and approximate theory experimental designs for D,A, and I criteria. Very large designs may be created. Experimental designs may be blocked or blocked designs created from a candidate list, using several criteria. The blocking can be done when whole and within plot factors interact.
	- []()

# 22.10.2018
## R
- Проблемы с русским языком на графиках в RMarkdown. `In grid.Call(C_textBounds, as.graphicsAnnot(x$label), x$x, x$y,  : invalid input 'Дата' in 'utf8towcs'`
- [emojifont. use with RMarkdown #17 {Closed}](https://github.com/GuangchuangYu/emojifont/issues/17)

# 19.10.2018
## R
- [R Database Securing Credentials](https://db.rstudio.com/best-practices/managing-credentials/)
- COOL! [R PACKAGES SEARCH AND STATISTICS](https://www.rpackages.io/)
- [zumbov2/colorfindr](https://github.com/zumbov2/colorfindr). Extracts colors from various image types and plots treemaps and 3D scatterplots of color compositions.
- [Loops and Pizzas. An Introduction to Loops in R](https://msperlin.github.io/2018-10-19-R-and-loops/) by Marcelo S. Perlin
- [SOLVING THE CHINESE POSTMAN PROBLEM](https://freakonometrics.hypotheses.org/53694)
- [A Lazy Function](http://cillianmacaodh.blogspot.com/2018/10/a-lazy-function.html) by CillianMacAodh (Cillian McHugh)
- [automl package: part 1/2 why and how](https://r-posts.com/automl-package-part-1-2-why-and-how/)

## DS. Рекомендательные системы
- [Sergey Nikolenko](https://logic.pdmi.ras.ru/~sergey/talks.html)
- [Demonstrations related to Matrix Decompositions (Wolfram Demonstrations Project)](http://demonstrations.wolfram.com/search.html?query=symbols%3ACholeskyDecomposition+OR+Eigensystem+OR+HermiteDecomposition+OR+HessenbergDecomposition+OR+JordanDecomposition+OR+LatticeReduce+OR+LUDecomposition+OR+QRDecomposition+OR+SchurDecomposition+OR+SingularValueDecomposition)
- COOL! Дмитрий Селиванов
	- [Matrix factorization for recommender systems](http://dsnotes.com/post/2017-05-28-matrix-factorization-for-recommender-systems/)
	- [Matrix factorization for recommender systems (part 2)](http://dsnotes.com/post/2017-06-28-matrix-factorization-for-recommender-systems-part-2/)
	- [dselivanov/rsparse](https://github.com/dselivanov/rsparse). Fast and accurate machine learning on sparse matrices - matrix factorizations, regression, classification, top-N recommendations. https://www.slideshare.net/DmitriySel…
- [How do I speed up matrix factorization by sampling users (without losing precision)?](https://www.quora.com/How-do-I-speed-up-matrix-factorization-by-sampling-users-without-losing-precision)
- Блог Avito. [Многорукие бандиты в рекомендациях](https://habr.com/company/avito/blog/417571/)
- [Байесовские многорукие бандиты против A/B тестов](https://habr.com/company/ods/blog/325416/)
- COOL! [10 уроков рекомендательной системы Quora](https://habr.com/company/retailrocket/blog/341346/)
- COOL! [Netflix and Chill: Building a Recommendation System in Excel](https://towardsdatascience.com/netflix-and-chill-building-a-recommendation-system-in-excel-c69b33c914f4). Learn the Machine Learning “Magic” behind the Binge
- Как это все было. [Netflix Update: Try This at Home](), https://sifter.org/~simon/journal/20061211.htmlMonday, December 11, 2006
- COOL! [Building a Movie Recommendation System](https://rpubs.com/jeknov/movieRec) by Jekaterina Novikova, PhD, June, 2016
- [Building a Recommendation System in TensorFlow: Overview](https://cloud.google.com/solutions/machine-learning/recommendation-system-tensorflow-overview)
- [ALS Implicit Collaborative Filtering](https://medium.com/radon-dev/als-implicit-collaborative-filtering-5ed653ba39fe)
Вот вопрос:
Implicit vs explicit data
Explicit data is data where we have some sort of rating. Like the 1 to 5 ratings from the MovieLens or Netflix dataset. Here we know how much a user likes or dislikes an item which is great, but this data is hard to come by. Your users might not spend the time to rate items or your app might not work well with a rating approach in the first place.

Implicit data (the type of data we’re using here) is data we gather from the users behaviour, with no ratings or specific actions needed. It could be what items a user purchased, how many times they played a song or watched a movie, how long they’ve spent reading a specific article etc. The upside is that we have a lot more of this data, the downside is that it’s more noisy and not always apparent what it means.

For example, with star ratings we know that a 1 means the user did not like that item and a 5 that they really loved it. With song plays it might be that the user played a song and hated it, or loved it, or somewhere in-between. If they did not play a song it might be since they don’t like it or that they would love it if they just knew about.
- COOL! [mhahsler/recommenderlab](https://github.com/mhahsler/recommenderlab). recommenderlab - Lab for Developing and Testing Recommender Algorithms - R package
- [List of Recommender Systems](https://github.com/grahamjenson/list_of_recommender_systems)
- COOL! [Recommender Systems Comparison](https://rpubs.com/tarashnot/recommender_comparison) by Taras Hnot, 06.08.2016
- COOL! [recosystem: Recommender System Using Parallel Matrix Factorization](https://cran.r-project.org/web/packages/recosystem/vignettes/introduction.html) by Yixuan Qiu, 2017-09-01
	- [Recosystem. Matrix Factorization with Gradient Descend](https://rstudio-pubs-static.s3.amazonaws.com/288275_c115bc2ebc794d89a71b5654905beddc.html) by Ann Liu-Ferrara, June 29, 2017
	- Yixuan's Blog [recosystem: Recommender System Using Parallel Matrix Factorization](https://statr.me/2016/07/recommender-system-using-parallel-matrix-factorization/), July 15, 2016 in Programming, R, Statistics. A Quick View of Recommender System
	- COOL! [Fast matrix factorization in R](https://www.smartcat.io/blog/2017/fast-matrix-factorization-in-r/)
	- COOL! [Improved R implementation of collaborative filtering](https://www.smartcat.io/blog/2017/improved-r-implementation-of-collaborative-filtering/)
	- [smartcat-labs/collaboratory](https://github.com/smartcat-labs/collaboratory). Laboratory for collaborative filtering
- [The 4 Recommendation Engines That Can Predict Your Movie Tastes](https://medium.com/@james_aka_yale/the-4-recommendation-engines-that-can-predict-your-movie-tastes-bbec857b8223)
- [Как работают рекомендательные системы. Лекция в Яндексе](https://habr.com/company/yandex/blog/241455/)
- COOL! [Рекомендательные системы](https://vas3k.ru/blog/355/)
- [Recommender Systems 101 – a step by step practical example in R](http://bigdata-doctor.com/recommender-systems-101-practical-example-in-r/)
- [Recommender Systems in Python: Beginner Tutorial](https://www.datacamp.com/community/tutorials/recommender-systems-python)
- [Comprehensive Guide to build a Recommendation Engine from scratch (in Python)](https://www.analyticsvidhya.com/blog/2018/06/comprehensive-guide-recommendation-engine-python/)
- [Prototyping a Recommendation System](https://towardsdatascience.com/prototyping-a-recommendation-system-8e4dd4a50675). Hello World in R, Java, Scala, and SQL
- [Recommender Systems in Keras](https://nipunbatra.github.io/blog/2017/recommend-keras.html).
	- А вообще, в его [блоге](https://nipunbatra.github.io/blog/index.html) полно записей про матричную факторизацию.
- [Deep Learning for Recommendation with Keras and TensorRec](https://hackernoon.com/deep-learning-for-recommendation-with-keras-and-tensorrec-2b8935c795d0)
- COOL! [Prototyping a Recommender System for Binary Implicit Feedback Data With R and Keras](https://nanx.me/blog/post/recsys-binary-implicit-feedback-r-keras/)
- Netflix. [Goodbye Stars, Hello Thumbs](https://media.netflix.com/en/company-blog/goodbye-stars-hello-thumbs)
- [Understanding ROC curves](http://www.navan.name/roc/)
- [List of Recommender Systems](https://github.com/grahamjenson/list_of_recommender_systems)
- H2O meetup. [Recommender Systems, Basics and Different Use Cases](https://github.com/h2oai/h2o-meetups/tree/master/2016_11_16_ODSC_Recommenders_H2O)

## Recommendation video lectures
- [Lecture 55 — Latent Factor Recommender System | Stanford University](https://www.youtube.com/watch?v=E8aMcwmqsTg)
- [How does Netflix recommend movies? Matrix Factorization](https://www.youtube.com/watch?v=ZspR5PZemcs)

## Datasets
- [Retail Sector Datasets and Competitions on Kaggle](https://blogs.msdn.microsoft.com/shishirs/2017/02/07/retail-sector-datasets-and-competitions-on-kaggle/)
- [Online Retail Data Set](https://archive.ics.uci.edu/ml/datasets/online+retail)
- [BigML datasets](https://bigml.com/gallery/datasets/consumer_and_retail)



# 18.10.2018
## R
- [hclust() in R on large datasets](https://stackoverflow.com/questions/40989003/hclust-in-r-on-large-datasets)
- COOL! [fastcluster: Fast Hierarchical Clustering Routines for R and 'Python'](https://cran.r-project.org/web/packages/fastcluster/)
This is a two-in-one package which provides interfaces to both R and 'Python'. It implements fast hierarchical, agglomerative clustering routines. Part of the functionality is designed as drop-in replacement for existing routines: linkage() in the 'SciPy' package 'scipy.cluster.hierarchy', hclust() in R's 'stats' package, and the 'flashClust' package. It provides the same functionality with the benefit of a much faster implementation. Moreover, there are memory-saving routines for clustering of vector data, which go beyond what the existing packages provide. For information on how to install the 'Python' files, see the file INSTALL in the source distribution. Based on the present package, Christoph Dalitz also wrote a pure 'C++' interface to 'fastcluster': <http://informatik.hsnr.de/~dalitz/data/hclust>.
- [Cluster Analysis with R](https://rstudio-pubs-static.s3.amazonaws.com/33876_1d7794d9a86647ca90c4f182df93f0e8.html)

## parallel R
- COOL! [A guide to parallelism in R](https://privefl.github.io/blog/a-guide-to-parallelism-in-r/) Written on September 5, 2017 by Florian Privé, R(cpp) enthusiast
- [Parallel process in chunks giving no performance benefits](https://stackoverflow.com/questions/45479105/parallel-process-in-chunks-giving-no-performance-benefits)
- [Parallel computing with R](http://pablobarbera.com/POIR613/code/06-parallel-computing.html) by Pablo Barbera, September 12, 2017
- [Using foreach and iterators for manual parallel execution](https://docs.microsoft.com/en-us/machine-learning-server/r/how-to-revoscaler-distributed-computing-foreach)
- [data.table and parallel computing](https://stackoverflow.com/questions/14759905/data-table-and-parallel-computing)
- COOL e-book [Efficient R programming](https://csgillespie.github.io/efficientR/), Colin Gillespie, Robin Lovelace, 2017-04-10
- [Parallelization with data.table](https://stackoverflow.com/questions/50049780/parallelization-with-data-table)



# 17.10.2018
## R
- [iotools: I/O Tools for Streaming](https://cran.r-project.org/web/packages/iotools/). Basic I/O tools for streaming and data parsing.
- [pubchunks: extract parts of scholarly XML articles](https://ropensci.org/technotes/2018/10/16/pubchunks/)
- Отличные лекции. [Lesson 5. Convert R Markdown to PDF or HTML](https://www.earthdatascience.org/courses/earth-analytics/document-your-science/knit-rmarkdown-document-to-pdf/)
- [Running rmarkdown from the command line without the need for X11 capability #1100 {Closed}](https://github.com/rstudio/rmarkdown/issues/1100)
- [Compiling Reports from R Scripts](https://rmarkdown.rstudio.com/articles_report_from_r_script.html)
- [Render reports directly from R scripts](http://brooksandrew.github.io/simpleblog/articles/render-reports-directly-from-R-scripts/)
- COOL! Macro Substitution in R](https://github.com/WinVector/wrapr/blob/master/extras/MacrosInR.md) by John Mount 2018-09-14
- [Even more images as x-axis labels](https://jcarroll.com.au/2018/10/16/even-more-images-as-x-axis-labels/)
- [Modifying Excel Files using openxlsx](https://webbedfeet.netlify.com/post/modifying-excel-files-using-openxlsx/)
- [Exploring college major and income: a live data analysis in R](http://varianceexplained.org/r/tidy-tuesday-college-major/)
- [I would like do a zip compression with password in R](https://stackoverflow.com/questions/40112701/i-would-like-do-a-zip-compression-with-password-in-r)
- COOL! Профилировка Rmarkdown!
```
# НУЖНО ЗАПУСКАТЬ В ЧИСТОЙ СЕССИИ
# profvis::profvis({rmarkdown::render("validation_proc.Rmd", "html_document", encoding = 'UTF-8')}, interval = 0.1, prof_output = "manual.rprof")
```

## Ищем тормоза при генерации репорта для МСП
Одним из самых тормозных элементов оказалась функция `lower_tri` в функции `stringdist::stringdistmatrix`. [Ссылка на определение функции](https://github.com/markvanderloo/stringdist/blob/03cec8adad87d572cd2671789c4fe9e6910dedfa/pkg/R/stringdist.R#L331).
Эта фукция использует [RCpp код]: [`SEXP R_lower_tri(`](https://github.com/markvanderloo/stringdist/blob/03cec8adad87d572cd2671789c4fe9e6910dedfa/pkg/src/Rstringdist.c#L235)



# 15.10.2018
## R
- [Running R scripts within in-database SQL Server Machine Learning](https://tomaztsql.wordpress.com/2018/10/14/running-r-scripts-within-in-database-sql-server-machine-learning/)
- Красиво. [VISUAL ART WITH PI USING GGPLOT2 & CIRCLIZE](https://chichacha.netlify.com/2018/10/13/visual-art-with-pi-using-ggplot2-circlize/)
	- Упоминается пакет [`circlize`]
- Форматирование таблиц в R:
	- [Total of a column in DT dataTables in shiny](https://stackoverflow.com/questions/49135787/total-of-a-column-in-dt-datatables-in-shiny)
	- [Huxtable is an R package to create styled tables in multiple output formats, with a friendly, modern interface.](https://hughjonesd.github.io/huxtable/)
	- [The flextable package provides a framework for easily create tables for reporting.](https://davidgohel.github.io/flextable/)
	- [Create Awesome HTML Table with knitr::kable and kableExtra](https://cran.r-project.org/web/packages/kableExtra/vignettes/awesome_table_in_html.html)
	- [Create stylish tables in R using formattable](https://www.littlemissdata.com/blog/prettytables)
- data.table. Учат мужика правильно открывать тикеты:
	- [fread from v.1.11.0+ no longer reads the .csv correctly, which was read perfectly in v.1.10.4-3 {#2857} Open](https://github.com/Rdatatable/data.table/issues/2857)
- В т.ч. и для data.table [Changing column names of a data frame](https://stackoverflow.com/questions/6081439/changing-column-names-of-a-data-frame/34202613#34202613)
- [Is possible to use fwrite from `data.table` with gzfile?](https://stackoverflow.com/questions/42788401/is-possible-to-use-fwrite-from-data-table-with-gzfile)


# 12.10.2018
## R
- COOL! [The R Infrastructure. How we build stuff](https://jeroen.github.io/uros2018/#1) by Jeroen Ooms, 2018/09/14
- [Optimize your R Code using Memoization](https://www.inwt-statistics.com/read-blog/optimize-your-r-code-using-memoization.html)
- [Some R Guides: tidyverse and data.table Versions](http://www.win-vector.com/blog/2018/10/some-r-guides-tidyverse-and-data-table-versions/)
- COOL! [Getting Started in R. An eight-page pdf guide for "Getting Started in R".](https://github.com/eddelbuettel/gsir-te)
1. По предварительным изысканиям `data.table` [поддерживает](https://jangorecki.gitlab.io/data.table/library/data.table/html/setops.html) `bit64::integer64`
2. Поддержка int64 в RClickhouse под вопросом.
    - [RClickhouse. Integer64 support #31 {Open}](https://github.com/IMSMWU/RClickhouse/issues/31)
    - Ведутся активности [64 bit integer support for reading and writing #35 {Open}](https://github.com/IMSMWU/RClickhouse/pull/35)
Но в первой ссылке RClickhouse есть хорошая проверка следующего утверждения: numeric can keep precise values up to 2**53
- [Libraries from third-party developers for working with ClickHouse](https://clickhouse-m.readthedocs.io/ru/latest/en/interfaces/third-party_client_libraries/)

## UPS
- [Настройка UPS Powercom BNT-600AP usb NUT на Debian](http://sonboga.ru/article/nastroika-ups-powercom-bnt-600ap-usb-nut-na-debian)
- [powercom - UPS driver for serial Powercom/Trust/Advice UPS equipment](https://networkupstools.org/docs/man/powercom.html)
- [Мониторинг APC UPS \ установка и настройка в Linux](http://netlly.ru/monitoring-apc-ups/)

# 11.10.2018
## R
- [Extending DT child rows example](http://www.reigo.eu/2018/04/extending-dt-child-row-example/)

# 10.10.2018
## R
- [Partially additive (generalized) linear model trees](https://eeecon.uibk.ac.at/~zeileis/news/palmtree/)

# 08.10.2018
## R
- [Introduction to DataExplorer](https://cran.r-project.org/web/packages/DataExplorer/vignettes/dataexplorer-intro.html)
- [DataExplorer: Fast Data Exploration With Minimum Code](http://blog.revolutionanalytics.com/2018/02/dataexplorer.html)
- MergeTree
	- [SSTable and Log Structured Storage: LevelDB](https://www.igvita.com/2012/02/06/sstable-and-log-structured-storage-leveldb/)
	- [The Log-Structured Merge-Tree (LSM Tree)](https://blog.acolyer.org/2014/11/26/the-log-structured-merge-tree-lsm-tree/)
	- [How does the log-structured merge-tree work?](https://www.quora.com/How-does-the-log-structured-merge-tree-work)
- [The “Gold Standard” for Data Science Project Management](https://towardsdatascience.com/the-gold-standard-of-data-science-project-management-13d68c9e85d6)
- COOL! [Project-oriented workflow](https://www.tidyverse.org/articles/2017/12/workflow-vs-script/). В частности, пункт "Use projects and the `here` package".
- COOL! [here. part of the tidyverse](https://here.r-lib.org/)
- COOL! [rprojroot. part of the tidyverse](https://rprojroot.r-lib.org/)



# 05.10.2018
## R
- COOL! [docxtractr](https://github.com/hrbrmstr/docxtractr). Extract Data Tables and Comments from ‘Microsoft’ ‘Word’ Documents
	- [Using R To Get Data *Out Of* Word Docs](https://rud.is/b/2015/08/23/using-r-to-get-data-out-of-word-docs/)
- radrachart in R
	- [radarchart: Radar Chart from 'Chart.js'](https://cran.r-project.org/web/packages/radarchart/index.html)
	- [radarchart: Drawing radar chart (a.k.a. spider plot)](https://rdrr.io/cran/fmsb/man/radarchart.html). In fmsb: Functions for Medical Statistics Book with some Demographic Data
	- [The R Graph Gallery's Top 5 Most Visited Graph Themes](https://www.datacamp.com/community/tutorials/top-5-r-graphics)
	- [Generate radar charts with ggplot2](https://stackoverflow.com/questions/50353923/generate-radar-charts-with-ggplot2)
	- [SPIDER OR RADAR CHART](https://www.r-graph-gallery.com/spider-or-radar-chart/)

## CH\DS
- [Dump/Import data from clickhouse](https://groups.google.com/forum/#!topic/clickhouse/Dx0CsFGbk7c)
- [Machine Learning for Visualization](https://medium.com/@enjalot/machine-learning-for-visualization-927a9dff1cab). Let’s Explore the Cutest Big Dataset


# 04.10.2018
## R
- COOL! [A Tale of Two Shiny Apps: Google Auth & ShinyProxy](https://rtask.thinkr.fr/blog/a-tale-of-two-shiny-apps-google-auth-shinyproxy/)
- [Apps / Unicode character inspector](https://apps.timwhitlock.info/unicode/inspect)
- COOL! Очень полезные способы работы с RStudio . [JhR blog](https://jozefhajnala.gitlab.io/r/)

# 02.10.2018
# R
- COOL! [bs4Dash](https://divadnojnarg.github.io/bs4Dash/index.html). Bootstrap 4 shinydashboard using AdminLTE3
- Ошибка с памятью, что замучала c валидатором МСП: [pandoc document conversion failed with error 127](https://stackoverflow.com/questions/34687030/pandoc-document-conversion-failed-with-error-127)
- [8 Useful Commands to Monitor Swap Space Usage in Linux](https://www.tecmint.com/commands-to-monitor-swap-space-usage-in-linux/)
	- [Glances – An Advanced Real Time System Monitoring Tool for Linux](https://www.tecmint.com/glances-an-advanced-real-time-system-monitoring-tool-for-linux/)
- [Useful R functions you might not know](https://www.computerworld.com/article/3184778/data-analytics/6-useful-r-functions-you-might-not-know.html) by Sharon Machlis, Executive Editor, Data & Analytics, Computerworld | MAY 4, 2018 11:08 AM PT


# 01.10.2018
## R
- [4 ways to be more productive, using RStudio's terminal](https://jozefhajnala.gitlab.io/r/r905-rstudio-terminal/)
- [XKCD "Curve Fitting", in R](http://blog.revolutionanalytics.com/2018/09/curve-fitting.html)
	- [Code and graphs for the xkcd2048 comic](https://gitlab.com/b-rowlingson/xkcd2048)
- [Visualize your Portfolio’s Performance and Generate a Nice Report with R](https://datascienceplus.com/visualize-your-portfolios-performance-and-generate-a-nice-report-with-r/)
- [Discover and install useful RStudio addins](https://github.com/daattali/addinslist)
- COOL! [smouksassi/ggquickeda](https://github.com/smouksassi/ggquickeda). ggplot and summary statistics quick exploration of data
- COOL! [esquisse](https://github.com/dreamRs/esquisse)
The purpose of this add-in is to let you explore your data quickly to extract the information they hold. You can only create simple plots, you won't be able to use custom scales and all the power of ggplot2. This is just the start!
- COOL! [ggplot2 explorer](http://databall.co/shiny/shinyggplot/). I created this website to help all R learners to undestand how to plot beautiful/useful charts using the most popular vizualization package ggplot2. It won't teach you how to write a code, but definitely will show you how ggplot2 geoms look like, and how manipulating their arguments changes visualization. Few scrolls below you can find list of covered geoms and example of what they plot.
	- [Исходники ggplot2 visual explorer](https://github.com/AlienDeg/shinyexplorer)
- COOL! [A new RStudio addin to facilitate inserting tables in Rmarkdown documents](https://lbusett.netlify.com/post/a-new-rstudio-addin-to-facilitate-inserting-tables-in-rmarkdown-documents/)
- COOL! [Radiant – Business analytics using R and Shiny](https://radiant-rstats.github.io/docs/)
- COOL! [ryantimpe/rspivot](https://github.com/ryantimpe/rspivot). RStudio addin to view data frames as pivot tables. View data as values, growth rates, and shares.
	- [Introduction to rspivot](https://ryantimpe.github.io/rspivot/articles/rspivot.html) by Ryan Timpe, 2018-01-25
- [multi-computer makePSOCKcluster on Windows: Building a step-by-step guide](https://stackoverflow.com/questions/32571996/multi-computer-makepsockcluster-on-windows-building-a-step-by-step-guide)
- [Does ifelse really calculate both of its vectors every time? Is it slow?](https://stackoverflow.com/questions/16275149/does-ifelse-really-calculate-both-of-its-vectors-every-time-is-it-slow)


# 28.09.2018
## R
- [August 2018: Top 40 New Packages](https://rviews.rstudio.com/2018/09/26/august-2018-top-40-new-packages/). Очень интересные подборки свежих пакетов, особенно в части time-series


# 27.09.2018
## DS
- [The Perl for MS Windows, free of charge!](http://strawberryperl.com/). Strawberry Perl is a perl environment for MS Windows containing all you need to run and develop perl applications. It is designed to be as close as possible to perl environment on UNIX systems.

## R
- shinyloadtest
- shinyloadtest. Ошибки, которые встретил сразу
-
```
> df0 <- shinyloadtest::load_runs("16 workers" = "./shinyloadtest/run_16", verbose = TRUE)
16 workers [===========================================================] 20/20 eta: 0s
Error in FUN(X[[i]], ...) :
  only defined on a data frame with all numeric variables
```
-
```
> shinyloadtest::shinyloadtest_report(df, "run.html")
run - Saving HTML [=================================================>] 126/127 eta: 0spandoc.exe: Cannot decode byte '\x92': Data.Text.Internal.Encoding.decodeUtf8: Invalid UTF-8 stream
```
	- Завал происходит в строке `df_filtered <- filter_df(df_run)`. Почему-то весь датафрейм зануляется

- [Shinycannon IllegalStateException #21 {Closed}](https://github.com/rstudio/shinyloadtest/issues/21)

# 26.09.2018
## R
- COOL! [Label line ends in time series with ggplot2](https://drsimonj.svbtle.com/label-line-ends-in-time-series-with-ggplot2)
- COOL! [Create stylish tables in R using formattable](https://www.littlemissdata.com/blog/prettytables)
- [Klipfolio](https://www.klipfolio.com/). The top rated dashboard on Earth.

## Excel
- [не удаётся разорвать связи в Excel](https://www.planetaexcel.ru/forum/index.php?PAGE_NAME=read&FID=8&TID=33341)
- [ Excel не разрывает связь с внешней книгой ](http://www.excelworld.ru/forum/2-12911-1). решение через распаковку
```
на листе Catalog
в ячейках:
C48:C49,E49,E52,C52,C54:C55,E54:E55,E58,C58,E74,C74,C66,E66

выставлена проверка данных, которая и держит связь.
очищаем условие проверки, сохраняем, перезагружаем книгу, связь пропала.

как быстро найдено:
1. открываем копию книгу винраром
2. находим и удаляем папку "externalLinks"
3. закрываем архиватор
4. открываем файл в Excel
5. Excel ругается, но потом восстанавливает данные, выдавая следующее:
Удаленное свойство: Проверка данных из части /xl/worksheets/sheet7.xml
```


# 25.09.2018
## R
- COOL! [Tuning a data preprocessing pipeline with recipes and modelgrid](http://smaakage85.netlify.com/2018/09/24/tuning-a-data-preprocessing-pipeline-with-recipes-and-modelgrid/)
- [modelgrid: A Framework for Creating, Managing and Training Multiple Caret Models](https://cran.r-project.org/web/packages/modelgrid/index.html)
A minimalistic but flexible framework that facilitates the creation, management and training of multiple 'caret' models. A model grid consists of two components: (1) a set of settings that is shared by all models by default, and (2) specifications that apply only to the individual models. When the model grid is trained, model and training specifications are first consolidated from the shared and the model specific settings into complete 'caret' model configurations. These models are then trained with the 'train' function from the 'caret' package.
- COOL! [Tol Color Schemes](https://owi.usgs.gov/blog/tolcolors/)
	- COOL! [Colour Schemes](https://personal.sron.nl/~pault/data/colourschemes.pdf), Prepared by: Paul Tol
	- [THE PAUL TOL 21-COLOR SALUTE](https://tradeblotter.wordpress.com/2013/02/28/the-paul-tol-21-color-salute/)
- Для быстрый конвертации R `data.frame` в JSON: https://github.com/SymbolixAU/jsonify
- COOL! [mschart](https://ardata-fr.github.io/mschart/). The mschart package provides a framework for easily create charts for ‘Microsoft PowerPoint’ documents. It has to be used with package officer that will produce the charts in new or existing PowerPoint or Word documents.
- COOL! [Crosstalk is an add-on to the htmlwidgets package](https://rstudio.github.io/crosstalk/)


# 24.09.2018
## R
- [A Performance Benchmark of Different AutoML Frameworks](https://www.statworx.com/de/blog/a-performance-benchmark-of-different-automl-frameworks/)
- [Shiny application in production with ShinyProxy, Docker and Debian](https://rtask.thinkr.fr/blog/shiny-application-in-production-with-shinyproxy-docker-and-debian/)
- [Where am I?](https://www.johnmackintosh.com/2018-09-23-Where-am-I/). Notes on the here package
- [Union Multiple Data.Frames with Different Column Names](https://statcompute.wordpress.com/2018/09/22/union-multiple-data-frames-with-different-column-names/)
- [By-Group Summary with SparkR – Follow-up for A Reader Comment](https://statcompute.wordpress.com/2018/09/23/by-group-summary-with-sparkr-follow-up-for-a-reader-comment/)
- [Simple Steps to Create Treemap in R](https://r-posts.com/simple-steps-to-create-treemap-in-r/)
 -[Timing Column Indexing in R](http://www.win-vector.com/blog/2018/09/timing-column-indexing-in-r/)
- [yihui/servr. servr: A Simple HTTP Server to Serve Static Files or Dynamic Documents](https://cran.r-project.org/web/packages/servr/index.html)
- COOL! [Heatmaps in R] by Jeff Oliver, 12 July, 2018. A worked example of making heatmaps in R with the ggplot package, as well as some data wrangling to easily format the data needed for the plot.
- [Time Based Heatmaps in R](https://www.littlemissdata.com/blog/heatmaps). R на IBM Watson
- [heatmap-esque plot for mouse clicking data](https://stackoverflow.com/questions/22442478/heatmap-esque-plot-for-mouse-clicking-data)
- [edzer/hexbin. Hexagonal binning routines and plotting methods](https://github.com/edzer/hexbin)
- [Be Awesome in ggplot2: A Practical Guide to be Highly Effective - R software and data visualization](http://www.sthda.com/english/wiki/be-awesome-in-ggplot2-a-practical-guide-to-be-highly-effective-r-software-and-data-visualization)
- [RShiny mouse-click does not work with facet_grid #1539 {Closed}](https://github.com/tidyverse/ggplot2/issues/1539)
- [shiny - Click on a map](http://playshiny.com/2016/10/17/shiny-click-on-a-map/)
- [Applications of R presented at EARL London 2018](https://www.r-bloggers.com/applications-of-r-presented-at-earl-london-2018/amp/)
- Надо уточнить, что подразумевалось под фразой: ["Rescaling Update
In preparing the data for the above plot all the variables were rescaled so that they were between 0 and 1.
Jim rightly pointed out in the comments (and I did not initally get it) that the heatmap-function uses a different scaling method and therefore the plots are not identical. Below is an updated version of the heatmap which looks much more similar to the original."](https://learnr.wordpress.com/2010/01/26/ggplot2-quick-heatmap-plotting/)

# 21.09.2018
## R Profiling
- [Profiling in R](http://ipub.com/r-profiling/). R has a built in performance and memory profiling facility: Rprof. Type  ?Rprof into your console to learn more. The way the profiler works is as follows:
    		* you start the profiler by calling Rprof, providing a filename where the profiling data should be stored
    		* you call the R functions that you want to analyse
    		* you call Rprof(NULL) to stop the profiler
    		* you analyse the file created by Rprof, typically using  summaryRprof
- [Profiling with RStudio and profvis](https://blog.rstudio.org/2016/05/23/profiling-with-rstudio-and-profvis/). RStudio Blog
- COOL! Презентация с Rconf 2018. [Make Shiny Fast …by doing as little work as possible](https://tailrecursion.com/slides/fast-shiny/#/cran-explorer) by Alan Dipert (@alandipert), February 2, 2018
- COOL! [Introduction to profvis](https://rstudio-pubs-static.s3.amazonaws.com/275741_41a9db67c79f4bcb9bf0933b7f268c5a.html) by Winston Chang, 2017-05-12
- [How can I profile a full R flexdashboard app to see what might be taking the most time/memory?](https://stackoverflow.com/questions/49677598/how-can-i-profile-a-full-r-flexdashboard-app-to-see-what-might-be-taking-the-mos): `profvis::profvis(rmarkdown::run("flexdashboard.Rmd"))`
- [Shiny (R) Web App Performance - Profiling](https://lukesingham.com/shiny-r-performance-profiling/).
```
# Load library
library(profvis)

# Run profiler on shiny app with optional arg to save output
profvis({ runApp('Projects/path_of_app') }
        , prof_output = '/path_to_save_output')
```
- Профилировка rmarkdown
   # НУЖНО ЗАПУСКАТЬ В ЧИСТОЙ СЕССИИ
   # profvis::profvis({rmarkdown::render("validation_proc.Rmd", "html_document", encoding = 'UTF-8')}, interval = 0.1, prof_output = "manual.rprof")

## R Streaming
- [Streaming in R](https://plot.ly/r/streaming/)
- [Plotly's Real-Time Streaming API](https://github.com/plotly/Streaming-Demos)
- [htmlwidgets for R - gallery](http://gallery.htmlwidgets.org/)
- [Introduction to the streamgraph htmlwidgtet R Package](https://hrbrmstr.github.io/streamgraph/) streamgraph is an htmlwidget JavaScript/D3 chart library.
- [THE R GRAPH GALLERY. STREAMGRAPH](https://www.r-graph-gallery.com/streamgraph/) A Stream graph is really close from a stacked area chart. It displays the evolution of a numerical value (Y axis) in function of another numerical value (X axis).
- [From Data to Viz](https://www.data-to-viz.com/). From Data to Viz leads you to the most appropriate graph for your data. It links to the code to build it and lists common caveats you should avoid.
- [JohnCoene/echarts. echarts for R - htmlwidget http://echarts4r.john-coene.com](https://github.com/JohnCoene/echarts)
- [ECHARTS](https://ecomfe.github.io/echarts-doc/public/en/index.html)
- COOL! [Interactive plots in Shiny](https://rviews.rstudio.com/2018/09/20/shiny-r2d3/). With r2d3 there is more work, but the gains in customization and interactivity make it by far the best choice, in my opinion.

## R
- [Make your R code faster: part 1](https://phdstatsphys.wordpress.com/2017/12/20/make-your-r-code-runs-faster/)
- [Make your R code faster: part 2](https://phdstatsphys.wordpress.com/2018/01/09/make-your-r-code-faster-part-2/)

## Elastic
- [Machine Learning for Nginx Logs - Identifying Operational Issues with Your Website](https://www.elastic.co/blog/machine-learning-for-nginx-logs)


# 19.09.2018
## Twitter
- [Apps of a Feather… Stick Together](http://apps-of-a-feather.com/)
- [The best Twitter client for Windows 2018: schedule and manage your tweets](https://www.techradar.com/news/the-best-twitter-client)

## Resilio
- [If Your Device Is Stolen](https://help.resilio.com/hc/en-us/articles/204644049-If-your-device-is-stolen)
If one of your devices used for sharing data via Sync has been stolen, the thief's chances to gain access to the contents of the shared folders depend on your operating system security. If the drive on the stolen device was encrypted, there’s nothing to worry about: no one will access your data unless they have a decryption key. If the drive wasn’t encrypted, the thief can potentially run Sync on the stolen device and, consequently, view, modify or remove data on other linked devices. If that is the case, the following steps should be considered:
- Back up the data in the folders added to Sync.
- Remove the synced data from the storage folder.
- Uninstall Sync. While uninstalling on Windows select ‘Remove settings’.
- Re-generate your identity and link your devices anew. For the guide on how to create an identity and link devices, click here
- Re-add the folders.
The above steps will remove the previous instance of Sync and break the connection with the stolen device. If you have a PRO version, you should activate your license again (click here to see how). The owner of the license is the peer who activated it most recently, therefore re-adding the license to Sync will override the previous activation. If the thief runs Sync on the stolen device and goes online, that instance of Sync will automatically be reverted to the FREE version.


## R
- [«smooth» package for R. Intermittent state-space model. Part I. Introducing the model](https://forecasting.svetunkov.ru/en/2018/09/18/smooth-package-for-r-intermittent-state-space-model-part-i-introducing-the-model/)
- [caching plots in R/Shiny](https://stackoverflow.com/questions/24192570/caching-plots-in-r-shiny)
- [rstudio/shinyloadtest. Tools for load testing Shiny applications - WIP!](https://github.com/rstudio/shinyloadtest)
- [rstudio/shiny. Caching ETA #2132 {Closed}](https://github.com/rstudio/shiny/issues/2132)
- [Official release of shiny.router and its new features](https://appsilon.com/shiny-router-package/)

# 17.09.2018
## R
- [Welcome to DARTISTICS!](http://www.dartistics.com/index.html). Digital Analytics: R and staTISTICS
This site is intended to be a resource for digital analysts who are interested in learning or expanding their knowledge of R and statistics. That’s from whence the semi-silly name came from:
	- [Fast R code](http://www.dartistics.com/fast-r-code.html)
- COOL! [readxl Workflows](https://readxl.tidyverse.org/articles/articles/readxl-workflows.html)
- [Why are concurrent writes not allowed on an SQLite database?](https://softwareengineering.stackexchange.com/questions/340550/why-are-concurrent-writes-not-allowed-on-an-sqlite-database)
- [Multiple simultaneous threads using SQLite in R {closed}](https://stackoverflow.com/questions/34026884/multiple-simultaneous-threads-using-sqlite-in-r)
- [Four different ways to handle SQLite concurrency](https://medium.com/@gwendal.roue/four-different-ways-to-handle-sqlite-concurrency-db3bcc74d00e)
- COOL! [Data visualisation pitfalls: how to avoid barbarplots ?](https://rtask.thinkr.fr/blog/data-visualisation-pitfalls-how-to-avoid-barbarplots/)
- Неплохой анализ! [Why Vectorize?](https://statcompute.wordpress.com/2018/09/16/why-vectorize/)
- [Break Down: model explanations with interactions and DALEX in the BayArea](http://smarterpoland.pl/index.php/2018/09/break-down-model-explanations-with-interactions-and-dalex-in-the-bayarea/)
- COOL! [Create anatograms using ggplot2](https://github.com/jespermaag/gganatogram)
- новые поступления от ropensci:
	- [ropensci/charlatan](https://github.com/ropensci/charlatan). Create fake data in R
	- [jqr -- R interface to jq, a JSON processor http://stedolan.github.io/jq/](https://github.com/ropensci/jqr). jqr makes it easy to process large amounts of json without having to convert from json to R, or without using regular expressions. This means that the eventual loading into R can be quicker.
- [Hyperpolyglot. JSON Tools: Jq](http://hyperpolyglot.org/json)
- ML. [cattonum](https://github.com/bfgray3/cattonum). cattonum (cat to num) provides different ways to encode categorical features as numerics.
- [Synchronization for R with the flock Package](http://www.quintuitive.com/2014/11/20/synchronization-for-r-with-the-flock-package/)


# 13.09.2018
## R
- [If not Notebooks, then what? Look to Literate Programming](http://blog.revolutionanalytics.com/2018/09/notebooks-literate-programming.html). Author and research engineer Joel Grus kicked off an important conversation about Jupyter Notebooks in his [recent presentation at JupyterCon](https://docs.google.com/presentation/d/1n2RlMdmv1p25Xy5thJUhkKGvjtV-dkAIsUXP-AL4ffI/edit#slide=id.g362da58057_0_1)
- [The First Notebook War](https://yihui.name/en/2018/09/notebook-war/). So Joel Grus doesn't like Jupyter notebooks. Here are some of my thoughts on notebooks, IDE, and R Markdown. Yihui Xie / 2018-09-10
- COOL! [future 1.9.0 - Output from The Future](https://www.jottr.org/2018/07/23/output-from-the-future/)
- COOL! [Comparison of breakDown, lime and shapleyR](https://rawgit.com/pbiecek/DALEX_docs/master/vignettes/Comparison_between_breakdown%2C_lime%2C_shapley.html) by Aleksandra Grudziąż, 15 czerwca 2018
In the vignette below we will see how methods implemented in three R packages focuses on variables in selected model. For our model we consider breakDown, lime and shapleyr.
- Отличные пакеты:
	- [SHINRA](https://shinra-dev.github.io/) is a collection of packages, or meta-package, for R. The primary purpose for the packages is to help programmers access, measure, visualize, and understand hardware resources. В частности, пакет [shinra-dev/memuse](https://github.com/shinra-dev/memuse)
	- [bench](https://github.com/r-lib/bench) -- "убийца" microbenchmark. High Precision Timing of R Expressions http://bench.r-lib.org/
	- [carbonate](https://yonicd.github.io/carbonate/). “carbon.js is the easiest way to create beautiful images of your source code.”
This package uses an R6 api to interact with carbon.js and create directly from the console carbon images.
- [MonetDBLite](https://github.com/hannesmuehleisen/MonetDBLite)
MonetDBLite is an embedded analytical SQL database that runs a variety of environments and does not require the installation of any external software. MonetDBLite is derived from free and open-source MonetDB, a product of the Centrum Wiskunde & Informatica.
- [Installing older versions of packages](https://support.rstudio.com/hc/en-us/articles/219949047-Installing-older-versions-of-packages)
- [maptools: Tools for Reading and Handling Spatial Objects](https://cran.r-project.org/web/packages/maptools/index.html)
- [capitalone/dataCompareR](https://github.com/capitalone/dataCompareR) dataCompareR is an R package that allows users to compare two datasets and view a report on the similarities and differences.
- COOL! tsibble ecosystem:
	- COOL! [The tsibble package](https://pkg.earo.me/tsibble/articles/intro-tsibble.html) extends the tidyverse to temporal-context data. Built on top of the tibble, a tsibble (or tbl_ts) is a data-centric format, following the tidy data principle (Wickham 2014).
	- [hts](http://pkg.earo.me/hts/). The R package hts presents functions to create, plot and forecast hierarchical and grouped time series.
	- COOL! [sugrrants](https://pkg.earo.me/sugrrants/).  The goal of sugrrants is to provide supporting graphs with R for analysing time series data. It aims to fit into the tidyverse and grammar of graphics framework for handling temporal data.
	- COOL! [tidyverts/fasster](https://github.com/tidyverts/fasster). Forecasting with Additive Switching of Seasonality, Trend and Exogenous Regressors. Очень хорошая [презентация](https://www.mitchelloharawild.com/user2018/#1)
	- The R package [fable](https://github.com/tidyverts/fable) provides methods and tools for displaying and analysing univariate time series forecasts including exponential smoothing via state space models and automatic ARIMA modelling. Data, model and forecast objects are all stored in a tidy format.

## Git
- [How can I undo the last commit?](https://www.git-tower.com/learn/git/faq/undo-last-commit). Ответ: `$ git reset --soft HEAD~1`
- [On undoing, fixing, or removing commits in git](https://sethrobertson.github.io/GitFixUm/fixup.html)
- [dnGrep](http://dngrep.github.io/) allows you to search across files with easy-to-read results. Search through text files, Word documents, PDFs, and archives using text, regular expression, XPath, and phonetic queries. dnGrep includes search-and-replace, whole-file preview, right-click search in File Explorer, and much more.
- [Free alternative(s) to PowerGREP](https://stackoverflow.com/questions/1086198/free-alternatives-to-powergrep/7858518)

# 12.09.2018
## Gitlab
- [GitLab and SSH keys](https://docs.gitlab.com/ee/ssh/)
- [How to create your SSH Keys](https://docs.gitlab.com/ee/gitlab-basics/create-your-ssh-keys.html)
- [Gitlab : How To Switch Remote Repository URL From Ssh To Http](https://www.linuxhelp.com/questions/gitlab-how-to-switch-remote-repository-url-from-ssh-to-http/)
first verify the existing remote url status using `git remote -v`... then refer below example to modify URL ssh to http
```
git remote set-url origin http://git@mp.trainee.co/trainee/user1.git
```
- [How do I tell Git for Windows where to find my private RSA key?](https://serverfault.com/questions/194567/how-do-i-tell-git-for-windows-where-to-find-my-private-rsa-key)

## DS
- COOL! [Towards Data Science. Sharing concepts, ideas, and codes]()https://towardsdatascience.com/)
	- [Understanding Feature Engineering (Part 1) — Continuous Numeric Data](https://towardsdatascience.com/understanding-feature-engineering-part-1-continuous-numeric-data-da4e47099a7b)
	- [Understanding Feature Engineering (Part 2) — Categorical Data](https://towardsdatascience.com/understanding-feature-engineering-part-2-categorical-data-f54324193e63)
	- [Understanding Feature Engineering (Part 3) — Traditional Methods for Text Data](https://towardsdatascience.com/understanding-feature-engineering-part-3-traditional-methods-for-text-data-f6f7d70acd41)
	- [Automated Feature Engineering in Python](https://towardsdatascience.com/automated-feature-engineering-in-python-99baf11cc219). How to automatically create machine learning features
- [Feature Lab](https://www.featurelabs.com/product/). Automated Feature Engineering for the Enterprise
Feature Labs accelerates the error prone, time intensive, and costly process of intelligently transforming raw data for machine learning algorithms
- [A Hands-On Guide to Automated Feature Engineering using Featuretools in Python](https://www.analyticsvidhya.com/blog/2018/08/guide-automated-feature-engineering-featuretools-python/)
- [Featuretools](https://www.featuretools.com/). An open source python framework for automated feature engineering
- [Automated Text Feature Engineering using textfeatures in R](https://datascienceplus.com/automated-text-feature-engineering-using-textfeatures-in-r/)
- [Automated Feature Selection using bounceR](https://www.statworx.com/de/blog/data-science/automated-feature-selection-using-bouncer/)
	- [STATWORX/bounceR. Automated Feature Selection](https://github.com/STATWORX/bounceR)


# 11.09.2018
## R
- [Difference in preprocessing using recipes and caret's preProcess](https://stackoverflow.com/questions/50339298/difference-in-preprocessing-using-recipes-and-carets-preprocess)
- COOL! Обсуждение [Future of caret?](https://community.rstudio.com/t/future-of-caret/612)
- COOL [greta. simple and scalable statistical modelling in R](https://goldingn.github.io/greta/)
- [Lattice or GGplot2. 2018](https://community.rstudio.com/t/lattice-or-ggplot2/6240). Ссылки на отличные ресурсы:
People definitely still use both packages.
	- You can visually see some of the differences in Tufte in R:
http://motioninsocial.com/tufte/
	- Here's another post: Plotting in R: Intro to base, lattice and ggplot2 by Joseph V. Casillas
http://www.jvcasillas.com/base_lattice_ggplot/
	- And another side-by-side comparison from STAT545, below:
https://www.stat.ubc.ca/~jenny/STAT545A/block18_gapminderGgplot2VsLattice.html


# 10.09.2018
## R
- COOL! [Diagnosing RStudio Startup Issues](https://datawookie.netlify.com/blog/2018/09/diagnosing-rstudio-startup-issues/). !! If you have problems running RStudio, give `--run-diagnostics` a try.
- [Playing Map() and Reduce() in R – Subsetting](https://statcompute.wordpress.com/2018/09/08/playing-map-and-reduce-in-r-subsetting/)
- [Driving Drill Dynamically with Docker and Updating Storage Configurations On-the-fly with sergeant](https://rud.is/b/2018/09/09/driving-drill-dynamically-with-docker-and-updating-storage-configurations-on-the-fly-with-sergeant/)
- [WVU Log Viewer](www.wvulogviewer.org/). WVU Well log viewer is a web enabled application to quickly visualize and interpret well log data. User can upload a LAS file and visualize logs in different ...
- Проблемка с read_csv, выявленная на экспериментах с нефтянкой: [Print column specification whenever there is guessing? #522 {Open}](https://github.com/tidyverse/readr/issues/522)/ Наблюдаются проблемы с разбором целевой колонки 'Нефть, т'. Там числа, завернутые в строки, а десятичным разделителем выступает запятая, а не точка
- Как поставить файл с гитхаба из локального архива?
	- Вроде прошло `install.packages("C:/Users/Ilya/Downloads/multidplyr-master.zip", repos=NULL)`, с обязательным указанием `repos`/
	- Прошло `devtools::install_local("C:/Users/Ilya/Downloads/multidplyr-master/")`. Читаем здесь: [Install R packages from github downloading master.zip](https://stackoverflow.com/questions/17366772/install-r-packages-from-github-downloading-master-zip)
- [An introduction to multidplyr](https://github.com/hadley/multidplyr/blob/master/vignettes/multidplyr.md) by Hadley Wickham
`multidplyr` is a new backend for `dplyr`. You continue to use the dplyr verbs that you're familiar with, but instead of the computation happening on one core it's spread across multiple cores. You effectively create a local cluster on your computer, and then multidplyr takes care of telling each node what to do.


# 07.09.2018
## R
- COOL! [From Data to Viz](https://www.data-to-viz.com/). From Data to Viz leads you to the most appropriate graph for your data. It links to the code to build it and lists common caveats you should avoid.
- [Diffusion/Wiener Model Analysis with brms – Part III: Hypothesis Tests of Parameter Estimates](http://singmann.org/wiener-model-analysis-with-brms-part-iii/)
- [Is there an R function for finding the index of an element in a vector?](https://stackoverflow.com/questions/5577727/is-there-an-r-function-for-finding-the-index-of-an-element-in-a-vector)

## ML
- [h2o.varimp_plot: Plot Variable Importances](https://rdrr.io/cran/h2o/man/h2o.varimp_plot.html)
- [h2o.varimp: Retrieve the variable importance](https://rdrr.io/cran/h2o/man/h2o.varimp.html)
- [Метрики в задачах машинного обучения](https://habr.com/company/ods/blog/328372/)
- [Understanding ROC curves](http://www.navan.name/roc/)
- [Задачки про AUC (ROC)](https://alexanderdyakonov.wordpress.com/2015/10/09/%D0%B7%D0%B0%D0%B4%D0%B0%D1%87%D0%BA%D0%B8-%D0%BF%D1%80%D0%BE-auc-roc/)
- [Логистическая функция ошибки](https://alexanderdyakonov.wordpress.com/2018/03/12/%D0%BB%D0%BE%D0%B3%D0%B8%D1%81%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B0%D1%8F-%D1%84%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D1%8F-%D0%BE%D1%88%D0%B8%D0%B1%D0%BA%D0%B8/#more-6139)

# 06.09.2018
## R
- [In praise of Commonmark: wrangle (R)Markdown files without regex](https://ropensci.org/technotes/2018/09/05/commonmark/)
- [Get Started with R (For Free) in IBM Watson Studio](https://www.littlemissdata.com/blog/watsonstudio)

# 05.09.2018
## R
- [Regular-Expression-in-R](https://github.com/ritagior/Regular-Expression-in-R), presentation for SatRday Amsterdam 01/09/2018
- [Optimization Methods for Tuning Predictive Models](https://github.com/topepo/Optimization-Methods-for-Tuning-Predictive-Models/blob/master/Kuhn_NLP_Tune.pdf), CRUG 2016, Max Kuhn Pfizer R&D
- [dplyr::mutate_if fails when column names contain spaces](https://stackoverflow.com/questions/44781389/dplyrmutate-if-fails-when-column-names-contain-spaces?rq=1)
- [Using group_by with mutate_if by column name](https://stackoverflow.com/questions/46607352/using-group-by-with-mutate-if-by-column-name)
- Как проверить, что тип принадлежит Date:
	- [Is there a way to check if a column is a Date in R?](https://stackoverflow.com/questions/18178451/is-there-a-way-to-check-if-a-column-is-a-date-in-r). Один из ответов: `lubridate::is.Date(x)`
	- [DescTools::IsDate](https://www.rdocumentation.org/packages/DescTools/versions/0.99.19/topics/IsDate). Check If An Object Is Of Type Date

## ML
- Missing Data Imputation.
Mice just provide a way to overcome issues with NAs. Some of the models do not accept NAs. So you have 3 approaches - (1) Leave the data as is and go for a model which can handle missing data (XGBoost, RF etc.) (2) Drop the NAs. This might lead to a significant loss of signal detection as you are letting go of some data portion (3) Opt for a data imputation methodology. Mice is one such library which would do it for you very easily. It allows for imputation using a variety of rules ranging from 'meanvalue' imputation to deriving relationship between variables to predict 'missing' value of target variable using a variety of models.
- [Impute Housing Data](https://www.kaggle.com/captcalculator/imputing-missing-data-with-the-mice-package-in-r)
- [Methods for Multiple Imputing Analysis with R](https://www.andrew.cmu.edu/user/aurorat/MIA_r.html) by Aurora Tsai, Carnegie Mellon University, December 22, 2017
- [A Solution to Missing Data: Imputation Using R](https://www.kdnuggets.com/2017/09/missing-data-imputation-using-r.html)
- [Uncertainty in random forest imputations from R missForest package](https://stats.stackexchange.com/questions/178699/uncertainty-in-random-forest-imputations-from-r-missforest-package)
- [How to use the data after missing values imputation (using mice)?](https://stats.stackexchange.com/questions/274176/how-to-use-the-data-after-missing-values-imputation-using-mice)
- [Dealing with Missing Data using R](https://medium.com/coinmonks/dealing-with-missing-data-using-r-3ae428da2d17)


- COOL! [Feature Selection in R with the Boruta R Package](https://www.datacamp.com/community/tutorials/feature-selection-R-boruta)
	- `install.packages(c("Boruta", "missForest", "Amelia"))`
- COOL! [Amelia II: A Program for Missing Data](https://gking.harvard.edu/amelia)
- [Tutorial on 5 Powerful R Packages used for imputing missing values](https://www.analyticsvidhya.com/blog/2016/03/tutorial-powerful-packages-imputing-missing-values/)
- A nominal variable is another name for a categorical variable. См. [Nominal Variable: Definition and Examples](http://www.statisticshowto.com/nominal-variable/)
- [How to perform feature selection (i.e. pick important variables) using Boruta Package in R ?](https://www.analyticsvidhya.com/blog/2016/03/select-important-variables-boruta-package/)
- [FEATURE SELECTION TECHNIQUES WITH R](http://dataaspirant.com/2018/01/15/feature-selection-techniques-r/)
- [The caret Package. Chapter 18. Feature Selection Overview](https://topepo.github.io/caret/feature-selection-overview.html)

# 04.09.2018
## R
- Random forrest
	- [Titanic: Getting Started With R - Part 5: Random Forests](http://trevorstephens.com/kaggle-titanic-tutorial/r-part-5-random-forests/)
	- [How to implement Random Forests in R](https://r-posts.com/how-to-implement-random-forests-in-r/)
- [Заметки по R: Случайный лес (random forest)](https://bdemeshev.github.io/r_cycle/cycle_files/22_forest.html). Да и вообще, сам сайт ["Заметки по R"](http://bdemeshev.github.io/r_cycle/) неплох.
- COOL! [Internationalization of shiny apps has never been easier!](https://appsilondatascience.com/internationalization-of-shiny-apps-i18n/)
- [Playing Map() and Reduce() in R – By-Group Calculation](https://statcompute.wordpress.com/2018/09/03/playing-map-and-reduce-in-r-by-group-calculation/)
- Video [Creating and Preprocessing a Design Matrix with Recipes](https://www.rstudio.com/resources/webinars/creating-and-preprocessing-a-design-matrix-with-recipes/)
- COOL! [Tutorial on the R Apply Family](https://www.datacamp.com/community/tutorials/r-tutorial-apply-family)
- COOL! [For loop functionals: friends of lapply()](http://adv-r.had.co.nz/Functionals.html)

# 03.09.2018
## R
- [Spectrograms in R – a gallery](https://walczak.org/2018/09/spectrograms-in-r-a-gallery/)
- COOL! rollRegress v0.1.0: Implements methods for fast-rolling and expanding linear regression models. The methods use rank-one updates and downdates of the upper triangular matrix from a QR decomposition. See Dongarra et al.(1979). The [vignette](https://rviews.rstudio.com/2018/08/27/july-2018-top-40-new-packages/) provides some details.
- [ceterisParibus: Ceteris Paribus Profiles](https://cran.r-project.org/web/packages/ceterisParibus/index.html).
Ceteris Paribus Profiles (What-If Plots) are designed to present model responses around selected points in a feature space. For example around a single prediction for an interesting observation. Plots are designed to work in a model-agnostic fashion, they are working for any predictive Machine Learning model and allow for model comparisons. Ceteris Paribus Plots supplement the Break Down Plots from 'breakDown' package.
- [makeParallel: Transform Serial R Code into Parallel R Code](https://cran.r-project.org/web/packages/makeParallel/)
- [R move column to last using dplyr](https://stackoverflow.com/questions/43897844/r-move-column-to-last-using-dplyr): `data%>%select(-b,everything())`, [Explained by Hadley himself](https://github.com/tidyverse/dplyr/issues/2838)
- COOL! [datapasta](https://github.com/MilesMcBain/datapasta) is about reducing resistance associated with copying and pasting data to and from R. It is a response to the realisation that I often found myself using intermediate programs like Sublime to munge text into suitable formats. Addins and functions in datapasta support a wide variety of input and output situations, so it (probably) "just works". Hopefully tools in this package will remove such intermediate steps and associated frustrations from our data slinging workflows.
	- [Datapasta review by Andrew Ba Tran, 1/28/2017](https://andrewbtran.github.io/r-journalism-case-studies/week2-hamilton-data/datapasta.html)
	- [Functions with R and rvest: A Laymen’s Guide](https://towardsdatascience.com/functions-with-r-and-rvest-a-laymens-guide-acda42325a77)
	- [Does datapasta work with RStudio Server? #73 {Open}](https://github.com/MilesMcBain/datapasta/issues/73). Yeah this problem arises since RStudio server is trying to access the
clipboard of the remote machine, not your local terminal where the data
resides.
- [install sqlite3 dev and other packages in centos](https://stackoverflow.com/questions/42669368/install-sqlite3-dev-and-other-packages-in-centos)
```
$ yum list | grep sqlite
libsqlite3x-devel.x86_6
```
- [Rstudio SQLite](http://db.rstudio.com/databases/sqlite/)
- [Querying SQLite Databases From R](http://tiffanytimbers.com/querying-sqlite-databases-from-r/)
- DALEX. [Use case: Regression. Apartment prices in Warsaw](https://pbiecek.github.io/DALEX_docs/2-2-useCaseApartmetns.html)
- [Model Interpretability with DALEX](http://uc-r.github.io/dalex)

# 31.08.2018
## Visualization
- COOL! [RAW Graphs](https://rawgraphs.io/). The missing link between spreadsheets and data visualization.
- [Falcon plotly. Can this App connect clickhouse database ? #431 {Open}](https://github.com/plotly/falcon/issues/431)
- [Test-driving Apache Superset](https://www.smartcat.io/blog/2018/test-driving-apache-superset/)
- [Superset: benefits and limitations of the open source data visualization tool by Airbnb](https://medium.com/@InDataLabs/superset-benefits-and-limitations-of-the-open-source-data-visualization-tool-by-airbnb-8dc8ac81efa9)
	- Исходник: [Superset: benefits and limitations of the open source data visualization tool by Airbnb](https://indatalabs.com/blog/data-strategy/open-source-data-visualization-tool-superset)
- [Почему я не использую реляционные СУБД](https://dou.ua/lenta/columns/dont-use-rdbms/)
- [Сравнение Pentaho Enterprise & Community](http://www.aplanadc.ru/partners/pentaho/pentahoeevsce.html)
- GeoMaps
	- [MapShaper](http://mapshaper.org/)
- [GeoJSON](http://geojson.io/)

## R
- COOL! [Making Graphs Look Easy with ggplot2 and Tidy Evaluation](https://crunch.io/dev/blog/autoplot-with-tidyeval/)
- COOL! [An Example Usage of ggplot_add()](https://yutani.rbind.io/post/2017-11-07-ggplot-add/)
- [Build your first web app dashboard using Shiny and R](https://medium.freecodecamp.org/build-your-first-web-app-dashboard-using-shiny-and-r-ec433c9f3f6c)
- [Building a simple Sales Revenue Dashboard with R Shiny & ShinyDashboard](https://datascienceplus.com/building-a-simple-sales-revenue-dashboard-with-r-shiny-shinydashboard/)
- [Designing Gadget UI](https://shiny.rstudio.com/articles/gadget-ui.html)
- [Shiny Chart Builder - Explore your database with a point-and-click interface](https://blog.datascienceheroes.com/shiny-chart-builder-explore-your-database-with-a-point-and-click-interface/)
- [daattali/advanced-shiny](https://github.com/daattali/advanced-shiny). Shiny tips & tricks for improving your apps and solving common problems https://deanattali.com/blog/advanced-…
- COOL! [Discover and install useful RStudio addins](https://github.com/daattali/addinslist)




# 30.08.2018
## R
- COOL! [Five steps for missing data with Finalfit](http://www.datasurg.net/2018/08/29/five-steps-for-missing-data-with-finalfit/)
- [finalfit: Quickly Create Elegant Regression Results Tables and Plots when Modelling](https://cran.r-project.org/web/packages/finalfit/index.html)
- COOL! [naniar](http://naniar.njtierney.com/). naniar provides principled, tidy ways to summarise, visualise, and manipulate missing data with minimal deviations from the workflows in ggplot2 and tidy data.
- [Transfer data from R to Python with PyRserve and Bio7](https://bio7.org/transfer-data-from-r-to-python-with-pyrserve-and-bio7/)
- [Fitting removal models with the detect R package](http://peter.solymos.org/code/2018/08/30/fitting-removal-models-with-the-detect-r-package.html)
- [How to self-publish a book: Customizing Bookdown](https://blog.datascienceheroes.com/how-to-self-publish-a-book-customizing-bookdown/)
- [shinyFeedback 0.1.0 on CRAN](https://www.tychobra.com/posts/2018_08_21_shinfeedback_release/?platform=hootsuite) by Andy Merlino, 2018/08/21

## NES
- [NES Graphics – Part 1](http://www.dustmop.io/blog/2015/04/28/nes-graphics-part-1/)
- [Проект wideNES — выходим на границы экрана NES](https://habr.com/post/421555/). [Оригинал на английском](http://prilik.com/blog/wideNES)

# 27.08.2018
## R
- COOL! [Select first and last row from grouped data](https://stackoverflow.com/questions/31528981/select-first-and-last-row-from-grouped-data)
- [MOVING BEYOND PATTERN-BASED ANALYSIS: ADDITIONAL APPLICATIONS OF GEOPAT 2](https://nowosad.github.io/post/geopat-2-extend/)
- [Simplifying World Tile Grid Creation with geom_wtg()](https://rud.is/b/2018/08/27/simplifying-world-tile-grid-creation-with-geom_wtg/)
- [littler 0.3.4: More updated examples](http://dirk.eddelbuettel.com/blog/2018/08/24/#littler-0.3.4)
- [MPT trees published in BRM](https://eeecon.uibk.ac.at/~zeileis/news/mpttree/)
- COOL! [Statistics Sunday: Visualizing Regression](http://www.deeplytrivial.com/2018/08/statistics-sunday-visualizing-regression.html). Now the fun part: let's plot our regression tree.
- COOL! [The power of stepped-wedge designs](https://www.rdatagen.net/post/alternatives-to-stepped-wedge-designs/)

# 21.08.2018
## R
- [Why build a recommender system?](https://www.mango-solutions.com/blog/introduction-to-recommender-systems)
- [BooST series I: Advantage in Smooth Functions](https://insightr.wordpress.com/2018/08/20/boost-series-i-advantage-in-smooth-functions/)
- [Missing deprecation warning when setting row names on tibble](https://community.rstudio.com/t/missing-deprecation-warning-when-setting-row-names-on-tibble/2004)
- `get_os` для опредления MacOS:
```
get_os <- function() {
  if (.Platform$OS.type == "windows") {
    "win"
  } else if (Sys.info()["sysname"] == "Darwin") {
    "mac"
  } else if (.Platform$OS.type == "unix") {
    "unix"
  } else {
    stop("Unknown OS")
  }
}
```
- [MS Access export table as .CSV file](https://answers.microsoft.com/en-us/msoffice/forum/msoffice_access-mso_other-msoversion_other/ms-access-export-table-as-csv-file/2df3f848-1560-4eeb-ba69-ee0be8f4b9db)
- Нашлись грабли с логическими операциями для множественных колонок. [Logical “and” for multiple logical vectors](https://stackoverflow.com/questions/40145025/logical-and-for-multiple-logical-vectors)


# 20.08.2018
## R
- [R:case4base - code profiling with base R](https://jozefhajnala.gitlab.io/r/r004-profiling/)
- [How to Create Sankey Diagrams From Tables (Data Frames) Using R](https://www.displayr.com/how-to-create-sankey-diagrams-from-tables-using-r)
- [An R package to create NEWS.md files](https://www.statworx.com/de/blog/an-r-package-to-create-news-md-files/)
- [Statistics Sunday: Using Text Analysis to Become a Better Writer](http://www.deeplytrivial.com/2018/08/statistics-sunday-using-text-analysis.html)
- [MANY REPORTS FROM 1 RMARKDOWN FILE](https://scottishsnow.wordpress.com/2018/08/17/many-reports-from-1-rmarkdown-file/)
- [Updates to the sergeant (Apache Drill connector) Package & a look at Apache Drill 1.14.0 release](https://rud.is/b/2018/08/16/updates-to-the-sergeant-apache-drill-connector-package-apache-drill-1-14-0-release/)


# 13.08.2018
## R
- Как добавить NA к факторам. `base::addNA()` или `forcats::fct_explicit_na(f, na_level = "(Missing)")` [Make missing values explicit](https://forcats.tidyverse.org/reference/fct_explicit_na.html). This gives missing value an explicit factor level, ensuring that they appear in summaries and on plots.



- COOL! Операция `naniar::replace_to_na`, обратная `tidyr::replace_na`: [Replacing selected values as NA #76 {Closed}](https://github.com/njtierney/naniar/issues/76)
- [tjmahr/fillgaze](https://github.com/tjmahr/fillgaze). Helper functions for interpolating missing eyetracking data
- COOL! [set_na_where(): a nonstandard evaluation use case](https://www.tjmahr.com/set-na-where-nonstandard-evaluation-use-case/). Bottling up magic spells
- [In dplyr, what are the intrinsic differences between setdiff and anti_join?](https://stackoverflow.com/questions/46854072/in-dplyr-what-are-the-intrinsic-differences-between-setdiff-and-anti-join)
- COOL! [dplyrpart of the tidyverse: Flexible equality comparison for data frames](https://dplyr.tidyverse.org/reference/all_equal.html). `all_equal` function
- COOL! [can dplyr package be used for conditional mutating?](https://stackoverflow.com/questions/24459752/can-dplyr-package-be-used-for-conditional-mutating). Масса ответов и бенчмарков.
- COOL! [Text clustering with Levenshtein distances](https://stackoverflow.com/questions/21511801/text-clustering-with-levenshtein-distances)

## Unsupervised learning
- COOL! [Unsupervised Learning in R](https://rpubs.com/williamsurles/310847) by William Surles, 2017-09-21
- [Articles - Partitioning Clustering Essentials](http://www.sthda.com/english/articles/27-partitioning-clustering-essentials/)
	- [Articles - Cluster Analysis in R: Practical Guide](http://www.sthda.com/english/articles/25-cluster-analysis-in-r-practical-guide/111-types-of-clustering-methods-overview-and-quick-start-r-code/). Types of Clustering Methods: Overview and Quick Start R Code
- [Beautiful dendrogram visualizations in R: 5+ must known methods - Unsupervised Machine Learning](http://www.sthda.com/english/wiki/beautiful-dendrogram-visualizations-in-r-5-must-known-methods-unsupervised-machine-learning)
- [Hierarchical cluster analysis on famous data sets - enhanced with the dendextend package](https://cran.r-project.org/web/packages/dendextend/vignettes/Cluster_Analysis.html)
- [Cluster Analysis in R](http://girke.bioinformatics.ucr.edu/GEN242/pages/mydoc/Rclustering.html) by First/last name (first.last@ucr.edu), Last update: 11 May, 2018
- [matloff/parcoordtutorial](https://github.com/matloff/parcoordtutorial). Tutorial on the parallel coordinates visualization method. Examples, interpretation, data, links and more.
- [cdparcoord: Categorical and Discrete Parallel Coordinates](https://cran.r-project.org/web/packages/cdparcoord/vignettes/cdparcoord.html)
- [PARALLEL COORDINATE PLOTS FOR DISCRETE AND CATEGORICAL DATA IN R — A COMPARISON](https://datascience.blog.wzb.eu/2016/09/27/parallel-coordinate-plots-for-discrete-and-categorical-data-in-r-a-comparison/)
- [An easy explanation for the parallel coordinates plot](https://stats.stackexchange.com/questions/2846/an-easy-explanation-for-the-parallel-coordinates-plot)
- [Parallel Coordinate Plots](https://homepage.divms.uiowa.edu/~luke/classes/STAT4580/parcor.html)

# 07.08.2018
## Excel
- [Отличие *.xlsx и *.xlsb - Планета Excel](https://www.planetaexcel.ru/forum/?PAGE_NAME=read&FID=1&TID=49986)
- [Importing a big xlsx file into R?](https://stackoverflow.com/questions/19147884/importing-a-big-xlsx-file-into-r)

## R
- Проблемка!! R.3.5 readr не может найти русский файлик под виндой. Похожая проблема: [`read_csv` can't recognize chinese file path on R 3.5.0 #834](https://github.com/tidyverse/readr/issues/834). Проблема с новым поведением `base::normalizePath()`
	- [CP1251 char set in file name #476](https://github.com/tidyverse/readxl/issues/476)
	- [convert path to the native locale before passing to boost::interprocess::file_mapping() #838](https://github.com/tidyverse/readr/pull/838)
	- [read_*() mangles file paths by converting them to UTF-8 and fails to read the resulting paths #868](https://github.com/tidyverse/readr/issues/868)
- COOL! [Why use purrr::map instead of lapply?](https://stackoverflow.com/questions/45101045/why-use-purrrmap-instead-of-lapply)
- [Mapping the stock market using self-organizing maps](https://databasedinvesting.blogspot.com/2018/08/mapping-stock-market-using-self.html)
- COOL! [MilesMcBain/friendlyeval](https://github.com/MilesMcBain/friendlyeval). A friendly interface to tidyeval/rlang that will excuse itself when you're done.
	- [Solving the Challenge of Tidyeval](https://milesmcbain.xyz/solving-the-challenge-of-tidyeval/) by Miles McBain | 23 May 2018
	- [The Roots of Quotation](https://milesmcbain.xyz/the-roots-of-quotation/) by Miles McBain | 26 Jul 2018
- [jennybc/code-smells-and-feels](https://github.com/jennybc/code-smells-and-feels#readme). Talk on code smells and feels and how to change that via refactoring https://rstd.io/code-smells
- [skimr for useful and tidy summary statistics](https://ropensci.org/blog/2017/07/11/skimr/)


# 01.08.2018
## R
- [Stages in the Evolution of S](http://ect.bell-labs.com/sl/S/history.html). Here is a summary of how S has evolved over its long history.
- COOL! [Teaching R to New Users - From tapply to the Tidyverse](https://simplystatistics.org/2018/07/12/use-r-keynote-2018/)
- [No worries! Afterthoughts from UseR 2018](http://smarterpoland.pl/index.php/2018/07/no-worries-afterthoughts-from-user-2018/)
- [Long Running Tasks With Shiny: Challenges and Solutions](http://blog.fellstat.com/?p=407)
- [Tidy evaluation in ggplot2](https://www.tidyverse.org/articles/2018/07/ggplot2-tidy-evaluation/)
- [EARL CONFERENCE 2018 – THE BEST YET!](https://www.mango-solutions.com/blog/earl-conference-2018-the-best-yet)
- [Singularity as a software distribution / deployment tool](https://mlampros.github.io/mlampros.github.io/2018/07/26/singularity_containers/)
- [How to use Covariates to Improve your MaxDiff Model](https://www.displayr.com/how-to-use-covariates-to-improve-your-maxdiff-model/?utm_medium=Feed&utm_source=Syndication)
- COOL! [But can ravens forecast? Why forecast sales?](https://thinkr.biz/2018/07/29/sales-forecast/)
- [Source code chapter added to “Evidence-based software engineering using R”](http://shape-of-code.coding-guidelines.com/2018/07/31/source-code-chapter-added-to-evidence-based-software-engineering-using-r/)
- COOL! [A package for dimensionality reduction of large data](https://ropensci.org/blog/2018/08/01/umapr/)
- COOL! [Understanding Titanic Dataset with H2O’s AutoML, DALEX, and lares library](https://datascienceplus.com/understanding-titanic-dataset-with-h2os-automl-dalex-and-lares-library/)

# 24.07.2018
## R
- COOL! сравнение прогнозов с реальными ценами. [Playing with Prophet on financial time series (again)](https://quantdare.com/playing-with-prophet-again/)

# 23.07.2018
## ML
- COOL e-book! [Interpretable Machine Learning. A Guide for Making Black Box Models Explainable.](https://christophm.github.io/interpretable-ml-book/)
- COOL! [What is the role of the activation function in a neural network? How does this function in a human neural network system?](https://www.quora.com/What-is-the-role-of-the-activation-function-in-a-neural-network-How-does-this-function-in-a-human-neural-network-system)
- [Activation Function](https://quickkt.com/tutorials/artificial-intelligence/deep-learning/activation-function/)

## R
- [Real-time data visualization using R and data extracting from SQL Server](https://tomaztsql.wordpress.com/2018/07/23/real-time-data-visualization-using-r-and-data-extracting-from-sql-server/)
- [RStudio:addins part 4 - Unit testing coverage investigation and improvement, made easy](https://jozefhajnala.gitlab.io/r/r104-unit-testing-coverage/)
- COOL! [R.devices - Into the Void](https://www.jottr.org/2018/07/21/suppressgraphics/)
- [A new ‘boto3’ Amazon Athena client wrapper with dplyr async query support](https://rud.is/b/2018/07/20/a-new-boto3-amazon-athena-client-wrapper-with-dplyr-async-query-support/)
- [Benchmarking Feature Selection Algorithms with Xy()](https://www.statworx.com/de/blog/benchmarking-feature-selection-algorithms-with-xy/)

# 20.07.2018
## R
- [Using leaflet, just because](https://nsaunders.wordpress.com/2018/07/17/using-leaflet-just-because/)
- [DEPLOYING R MODELS IN SQL SERVER](https://www.mango-solutions.com/blog/deploying-r-models-in-sql-server)
- [Machine Learning Results in R: one plot to rule them all!](https://datascienceplus.com/machine-learning-results-one-plot-to-rule-them-all/)
- [Call Centre Workforce Planning Using Erlang C in R language](https://lucidmanager.org/call-centre-workforce-planning-erlang-c-in-r/)
- BlackBox
	- COOL! [Explaining Black-Box Machine Learning Models - Code Part 1: tabular data + caret + iml](https://shirinsplayground.netlify.com/2018/07/explaining_ml_models_code_caret_iml/)
	- [Explaining Keras image classification models with lime](https://shirinsplayground.netlify.com/2018/06/keras_fruits_lime/)
- COOL! [ggthemes 4.0.0](https://jrnold.github.io/ggthemes/). Some extra geoms, scales, and themes for ggplot, including:


## Shiny
- [R-Shiny webserver on a local server](https://stackoverflow.com/questions/25858196/r-shiny-webserver-on-a-local-server)
- COOL! Shiny. If the log file is not preserved add the following line to the top of you `shiny-server.conf` file in `/etc/shiny-server/`: preserve_logs true`;. Once the log files are preserved, you should be able to identify the error causing the application to exit. Взял [отсюда](https://community.rstudio.com/t/shiny-webserver-deployment-in-windows-operating-system/9349)

# 19.07.2018
## R & Docker
- [How to Dockerize an R Shiny App — Part 1](https://towardsdatascience.com/how-to-dockerize-an-r-shiny-app-part-1-d4267659312a)
- [How do I Dockerize an R Shiny app on my local machine using Shiny server?](https://stackoverflow.com/questions/49736393/how-do-i-dockerize-an-r-shiny-app-on-my-local-machine-using-shiny-server)
- [Use Docker to distribute and run Shiny apps](https://wabi-wiki.scilifelab.se/display/KB/Use+Docker+to+distribute+and+run+Shiny+apps)
- COOL! [Best practices for writing Dockerfiles](https://docs.docker.com/v17.09/engine/userguide/eng-image/dockerfile_best-practices/)
- COOL! [cole-brokamp/rize](https://github.com/cole-brokamp/rize) dockerize R shiny apps
- [QuantumObject/docker-shiny](https://github.com/QuantumObject/docker-shiny). Dockerfile to be use to build image for docker container with Shiny https://shiny.quantumobject.org/
- Docker error!!! [/var/lib/docker/tmp/docker-builderXXXXXXX/... no such file or directory {#1922}](https://github.com/docker/for-mac/issues/1922#issuecomment-355364451)
	- [.dockerignore file](https://docs.docker.com/engine/reference/builder/#dockerignore-file)
	- [Docker build ignoring .dockerignore](https://forums.docker.com/t/docker-build-ignoring-dockerignore/11991)
- [Shiny Server on Docker: CentOS 7 Edition](https://www.datascienceriot.com/r/shiny-docker/)
        - COOL! [A Dockerfile to initialize Shiny-Server and RStudio Server on CentOS7](https://github.com/keberwein/docker_shiny-server_centos7)


# 17.07.2018
## R
- [Smoothing Time Series Data](https://www.displayr.com/smoothing-time-series-data/)
- [Customizing styler - the quick way](https://lorenzwalthert.netlify.com/posts/customizing-styler-the-quick-way/)
- COOL! [Create a reactive trigger](https://github.com/daattali/advanced-shiny/tree/master/reactive-trigger)

# 16.07.2018
## R
- COOL! [From Data to Viz](https://www.data-to-viz.com/) leads you to the most appropriate graph for your data. It links to the code to build it and lists common caveats you should avoid.
- [Stan®](http://mc-stan.org/) is a state-of-the-art platform for statistical modeling and high-performance statistical computation. Thousands of users rely on Stan for statistical modeling, data analysis, and prediction in the social, biological, and physical sciences, engineering, and business.
- [Using Machine Learning for Causal Inference](https://www.statworx.com/de/blog/using-machine-learning-for-causal-inference/)
- [Seasonal decomposition of short time series](https://robjhyndman.com/hyndsight/tslm-decomposition/)
- COOL! [Why I rarely use apply](https://privefl.github.io/blog/why-i-rarely-use-apply/)

# 12.07.2018
## R
- [{ggplot2} Welcome viridis !](https://rtask.thinkr.fr/blog/ggplot2-welcome-viridis/)
- [Our Package template to design a prod-ready Shiny application](https://rtask.thinkr.fr/blog/our-shiny-template-to-design-a-prod-ready-app/)
- [{How-to} Share content between several R6 instances](https://rtask.thinkr.fr/blog/share-content-between-several-r6-instances/)
- [Dockerise and deploy your own R Archive Repo](https://rtask.thinkr.fr/blog/dockerise-and-deploy-your-own-r-archive-repo/)
- liftr. [A Quick Introduction to liftr](https://cran.r-project.org/web/packages/liftr/vignettes/liftr-intro.html)
- [Handling Strings with R](http://www.gastonsanchez.com/r4strings/) by Gaston Sanchez, 2018-04-19
- [rocker](http://dirk.eddelbuettel.com/blog/code/rocker/)
- COOL! [dockerfiler is now on CRAN](https://colinfay.me/dockerfiler-cran/)


# 11.07.2018
## R
- COOL! [drake: A Pipeline Toolkit for Reproducible Computation at Scale](https://cran.r-project.org/web/packages/drake/index.html)
- COOL! [r2d3: Interface to 'D3' Visualizations](https://cran.r-project.org/web/packages/r2d3/index.html)
- COOL! [A paging input for R/Shiny applications](https://github.com/wleepang/shiny-pager-ui)
- [shiny reimagined with bootstrap 4 https://nteetor.github.io/dull](https://github.com/nteetor/dull)
- COOL! [merlinoa/shinyFeedback](https://github.com/merlinoa/shinyFeedback). R package for displaying user feedback next to Shiny inputs
- [Advantages of Using R Notebooks For Data Analysis Instead of Jupyter Notebooks](http://minimaxir.com/2017/06/r-notebooks/)
- [Top 5 Alternatives to Jupyter Notebook](https://analyticsindiamag.com/top-5-alternatives-jupyter-notebook/)
- [packagefinder: Comfortable Search for R Packages on CRAN](https://cloud.r-project.org/web/packages/packagefinder/index.html)
- COOL! [Build awesome dashboards with shiny](https://divadnojnarg.github.io/blog/awesomedashboards/)
- [Gentelella Shiny](http://code.markedmondson.me/gentelellaShiny/). This is an R Shiny HTML Template version of the gentelella bootstrap theme.
- [Discussion: when is Shiny a good choice vs when is it not the right tool for the job?](https://community.rstudio.com/t/discussion-when-is-shiny-a-good-choice-vs-when-is-it-not-the-right-tool-for-the-job/707)
- COOL [Comparison with R / R libraries](https://pandas.pydata.org/pandas-docs/stable/comparison_with_r.html)
- [ficonsulting/RInno](https://github.com/ficonsulting/RInno). How to install local shiny apps
- [Coloured output in the R console](https://aghaynes.wordpress.com/2018/07/12/coloured-output-in-the-r-console/)

## DS
- [Regex was taking 5 days to run. So I built a tool that did it in 15 minutes.](https://medium.freecodecamp.org/regex-was-taking-5-days-flashtext-does-it-in-15-minutes-55f04411025f)
- COOL! [RethinkDB. The open-source database for the realtime web](https://www.rethinkdb.com/)
- COOL! [22 Free and Open Source Data Visualization Tools to Grow Your Business](https://blog.capterra.com/free-and-open-source-data-visualization-tools/)
	- COOL! [RAW Graphs](https://rawgraphs.io/). The missing link between spreadsheets and data visualization.
- Отличное русскоязычное сообщество: [Big Data Russia](https://vk.com/big_data_russia)
- [Stack Overflow: Kotlin, R and TypeScript among least disliked programming languages](https://jaxenter.com/kotlin-among-least-disliked-languages-138544.html)
- [Язык программирования R для статистических вычислений](https://vk.com/rstatistics)

# 09.07.2018
## R
- [Speed up your R Work](http://www.win-vector.com/blog/2018/07/speed-up-your-r-work/)
- [Dealing with heteroskedasticity; regression with robust standard errors using R](http://www.brodrigues.co/blog/2018-07-08-rob_stderr/)
- [Connecting R to PostgreSQL on Linux](https://www.nielsenmark.us/2018/07/07/connecting-r-to-postgresql-on-linux/)
- [New package 'packagefinder' - Search for packages from the R console](https://topics-in-r.blogspot.com/2018/07/new-package-packagefinder.html)
- [CONVEX REGRESSION MODEL](https://freakonometrics.hypotheses.org/53384)
- [Survey your audience and visualise the results with R and Google forms](http://www.seascapemodels.org/rstats/2018/07/05/survey-your-audience.html)
- [New rWind release on CRAN! (v1.0.2)](https://allthiswasfield.blogspot.com/2018/07/new-rwind-v102-release-on-cran.html)
- COOL! [infer R Package](http://infer.netlify.com/). The objective of this package is to perform statistical inference using an expressive statistical grammar that coheres with the tidyverse design framework.
- [CRISP-DM – a Standard Methodology to Ensure a Good Outcome](https://www.datasciencecentral.com/profiles/blogs/crisp-dm-a-standard-methodology-to-ensure-a-good-outcome)


# 02.07.2018
## R
- [modelDown: a website generator for your predictive models](http://smarterpoland.pl/index.php/2018/06/modeldown-a-website-generator-for-your-predictive-models/)
- [A Comparative Review of the Rattle GUI for R](http://r4stats.com/2018/07/02/a-comparative-review-of-the-rattle-gui-for-r/)
- COOL! [Factfulness: Building Gapminder Income Mountains](http://staff.math.su.se/hoehle/blog/2018/07/02/factfulness.html)
- [Handling Outliers with R](https://madstatbr.wordpress.com/2018/07/02/handling-outliers-with-r/)


# 27.06.2018
## R, визуальный анализ датасетов
- [Caret package e-book](http://topepo.github.io/caret/index.html). The caret package (short for _C_lassification _A_nd _RE_gression _T_raining) is a set of functions that attempt to streamline the process for creating predictive models.
- COOL! [A primer on visual overview of data frame](https://towardsdatascience.com/visual-overview-of-the-data-frame-4c6186a69697)
- [GGpairs, correlation values are not aligned](https://stackoverflow.com/questions/40540363/ggpairs-correlation-values-are-not-aligned)
- COOL! [My favourite R package for: summarising data](https://dabblingwithdata.wordpress.com/2018/01/02/my-favourite-r-package-for-summarising-data/)
	- `base::summary`
	- `Hmisc::describe`
	- `pastecs::stat.desc`
	- `psych::describe` & `psych::describeBy`
	- `skimr::skim`
	- `summarytools::descr` & `summarytools::dfSummary`
	- я нашел еще inspectdf & DataExplorer
- COOL! [alastairrushworth/inspectdf](https://github.com/alastairrushworth/inspectdf). Tools for Exploring and Comparing Data Frames

## R
- [Running Python inside the RStudio Server IDE](https://www.mango-solutions.com/blog/running-python-inside-the-rstudio-server-ide)
- [Re-referencing factor levels to estimate standard errors when there is interaction turns out to be a really simple solution](https://www.rdatagen.net/post/re-referencing-to-estimate-effects-when-there-is-interaction/)
- COOL! [Package roomba](https://ropensci.org/blog/2018/06/26/roomba/). A package for tidying nested lists
- [New R package flatxml: working with XML files as R dataframes](https://topics-in-r.blogspot.com/2018/06/new-r-package-flatxml-working-with-xml.html)
- COOL! [package later. Schedule R Code to Be Executed Periodically in the Current R Session](https://yihui.name/en/2017/10/later-recursion/)
- [Shiny 1.1.0: Scaling Shiny with async](https://blog.rstudio.com/2018/06/26/shiny-1-1-0/)
 -[Combinations and permutations in R](https://davetang.org/muse/2013/09/09/combinations-and-permutations-in-r/)

# 26.06.2018
## DS
- COOL! Весьма воодушевляющий пост (Andrej Karpathy, Director of AI at Tesla) [Software 2.0](https://medium.com/@karpathy/software-2-0-a64152b37c35)
- [Using H2O Powered Machine Learning Algorithms in R & Exploratory](https://blog.exploratory.io/using-h2o-powered-machine-learning-algorithms-in-r-exploratory-9c514fddca8d)
- COOL! [Spark ML to H2O Migration for Machine Learning in iyzico](https://iyzico.engineering/spark-ml-to-h2o-migration-for-machine-learning-in-iyzico-dcba86b8eab2)
- [Understanding and Implementing CycleGAN in TensorFlow](https://hardikbansal.github.io/CycleGANBlog/)
- Datacamp. [New Course: Marketing Analytics in R](https://www.datacamp.com/community/blog/marketing-analytics-r)
- [Using LSTMs to forecast time-series](https://towardsdatascience.com/using-lstms-to-forecast-time-series-4ab688386b1f)

## Кухня
- http://chernovic.ru/, https://cookbooks.ru/

# 25.06.2018
## R
- [Switching to blogdown, Netlify and Travis](https://lorenzwalthert.netlify.com/posts/getting-up-and-running-with-blogdown-netlify-and-travis/)
- [Idle thoughts lead to R internals: how to count function arguments](https://nsaunders.wordpress.com/2018/06/22/idle-thoughts-lead-to-r-internals-how-to-count-function-arguments/)
- [Creating Slopegraphs with R](https://datascienceplus.com/creating-slopegraphs-with-r/)
- [A guide to working with character data in R](http://blog.revolutionanalytics.com/2018/06/handling-strings-with-r.html)
- [future.apply - Parallelize Any Base R Apply Function](https://www.jottr.org/2018/06/23/future.apply_1.0.0/)
- [A forecast ensemble benchmark](https://robjhyndman.com/hyndsight/benchmark-combination/)
- [Forecasting my weight with R](http://www.brodrigues.co/blog/2018-06-24-fun_ts/)
- [Extracting a Reference Grid of your Data for Machine Learning Models Visualization](https://neuropsychology.github.io/psycho.R//2018/06/25/refdata.html)
- [Tidy forecasting in R](https://robjhyndman.com/seminars/isf-fable/). 19 June 2018. Presentation at the International Symposium on Forecasting, Boulder USA.
- [r-lib/keyring](https://github.com/r-lib/keyring). Access the system credential store from R

## Data Imputation
- [Tutorial on 5 Powerful R Packages used for imputing missing values](https://www.analyticsvidhya.com/blog/2016/03/tutorial-powerful-packages-imputing-missing-values/)
	- MICE
	- Amelia
	- missForest
	- Hmisc
	- mi
	- imputeTS
- [Imputation methods for time series data](https://stats.stackexchange.com/questions/261271/imputation-methods-for-time-series-data)
- [CRAN Task View: Time Series Analysis](https://cran.r-project.org/web/views/TimeSeries.html). Maintainer: Rob J Hyndman

# 20.06.2018
## DS
- COOL! [Gradient Boosting from scratch](https://medium.com/mlreview/gradient-boosting-from-scratch-1e317ae4587d)
- COOL! [Understanding LSTM and its diagrams](https://medium.com/mlreview/understanding-lstm-and-its-diagrams-37e2f46f1714). LSTM = "Long Short Term Memory"
- COOL! [What is the difference between Bagging and Boosting?](https://quantdare.com/what-is-the-difference-between-bagging-and-boosting/)
- COOL! [What is the difference between test set and validation set?](https://stats.stackexchange.com/questions/19048/what-is-the-difference-between-test-set-and-validation-set)
- [About Train, Validation and Test Sets in Machine Learning](https://towardsdatascience.com/train-validation-and-test-sets-72cb40cba9e7)
- [How to split data into training/testing sets using sample function](https://stackoverflow.com/questions/17200114/how-to-split-data-into-training-testing-sets-using-sample-function)
- COOL! Очень хорошие комментарии про применение различных методов "в бою". [АНАЛИЗ МАЛЫХ ДАННЫХ, КвазиНаучный блог Александра Дьяконова. Python: категориальные признаки](https://alexanderdyakonov.wordpress.com/2016/08/03/python-%D0%BA%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B5-%D0%BF%D1%80%D0%B8%D0%B7%D0%BD%D0%B0%D0%BA%D0%B8/)
- [10 типов регрессии – какой выбрать?](http://datareview.info/article/10-tipov-regressii-kakoy-vyibrat/)
- [Предсказываем будущее с помощью библиотеки Facebook Prophet](https://habr.com/company/ods/blog/323730/)
- [Нестандартная кластеризация, часть 3: приёмы и метрики для кластеризации временных рядов](https://habr.com/post/334220/)
- [Анализ временных рядов с помощью python](https://habr.com/post/207160/)
- COOL! [How to choose Last-layer activation and loss function](https://www.dlology.com/blog/how-to-choose-last-layer-activation-and-loss-function/)
- COOL! [The Keras Functional API: Five simple examples](http://www.puzzlr.org/the-keras-functional-api-five-simple-examples/)
- [How to Use the Keras Functional API for Deep Learning](https://machinelearningmastery.com/keras-functional-api-deep-learning/)

- [Predicting the price of wine with the Keras Functional API and TensorFlow](https://medium.com/tensorflow/predicting-the-price-of-wine-with-the-keras-functional-api-and-tensorflow-a95d1c2c1b03)

# 19.06.2018
## R
- !! [Not only LIME. DALEX package](http://smarterpoland.pl/index.php/2018/06/not-only-lime/)
- !! [iml: interpretable machine learning](https://github.com/christophM/iml)
- [bounceR 0.1.2: Automated Feature Selection](https://www.statworx.com/de/blog/data-science/bouncer-0-1-2-automated-feature-selection/)
- [Most Starred R Packages on GitHub](https://stevenmortimer.com/most-starred-r-packages-on-github/). Published June 18, 2018
	- [r2d3: Interface to 'D3' Visualizations](https://cran.r-project.org/web/packages/r2d3/index.html)
	- [goodpractice: Advice on R Package Building](https://cran.r-project.org/web/packages/goodpractice/index.html)
	- [workflowr: A Framework for Reproducible and Collaborative Data Science](https://cran.r-project.org/web/packages/workflowr/)
	- [furrr: Apply Mapping Functions in Parallel using Futures](https://cran.r-project.org/web/packages/furrr/index.html)
	- [scico: Colour Palettes Based on the Scientific Colour-Maps](https://cran.r-project.org/web/packages/scico/index.html)
	- [xtensor: Headers for the 'xtensor' Library](https://cran.r-project.org/web/packages/xtensor/index.html)
	- [rtika: R Interface to 'Apache Tika'](https://cran.r-project.org/web/packages/rtika/index.html)
	- [mindr: Convert Files Between Markdown or Rmarkdown Files and Mindmaps](https://cran.r-project.org/web/packages/mindr/index.html)
	- [rngtools: Utility Functions for Working with Random Number Generators](https://cran.r-project.org/web/packages/rngtools/index.html)
	- [gsubfn: Utilities for Strings and Function Arguments](https://cran.r-project.org/web/packages/gsubfn/index.html)
	- [munsell: Utilities for Using Munsell Colours](https://github.com/cwickham/munsell/)
- [smooth: Forecasting Using State Space Models](https://cran.r-project.org/web/packages/smooth/index.html)
- [Prediction Interval, the wider sister of Confidence Interval](https://datascienceplus.com/prediction-interval-the-wider-sister-of-confidence-interval/)
- [Removing attributes of columns in data.frames on multilevel lists in R](https://stackoverflow.com/questions/28873323/removing-attributes-of-columns-in-data-frames-on-multilevel-lists-in-r)

## Time-series
- [ts function in R {closed}](https://stats.stackexchange.com/questions/259979/ts-function-in-r)
- [Saving ts objects as csv files](https://robjhyndman.com/hyndsight/ts2csv/). Occasionally R might not be the tool you want to use (hard to believe, but apparently that happens). Then you may need to export some data from R via a csv file. When the data is stored as a ts object, the time index can easily get lost. So I wrote a little function to make this easier, using the tsibble package to do most of the work in looking after the time index.
- [Time Series Analysis in R Part 1: The Time Series Object](https://datascienceplus.com/time-series-analysis-in-r-part-1-the-time-series-object/)
- [Time Series Analysis in R Part 2: Time Series Transformations](https://datascienceplus.com/time-series-analysis-in-r-part-2-time-series-transformations/)
- [Time Series Analysis in R Part 3: Getting Data from Quandl](https://datascienceplus.com/time-series-analysis-in-r-part-3-getting-data-from-quandl/)
- [Manipulating Time Series Data in R with xts & zoo](https://rpubs.com/mohammadshadan/288218)
- [Is it possible to merge two time series in one?](https://stackoverflow.com/questions/23944092/is-it-possible-to-merge-two-time-series-in-one)
- [could not convert index to appropriate type while attempting to plot weekly ts object in dygraphs](https://stackoverflow.com/questions/29261855/could-not-convert-index-to-appropriate-type-while-attempting-to-plot-weekly-ts-o)
```
> head(index(dfts))
[1] 2012.346 2012.365 2012.385 2012.404 2012.423 2012.442
The index is numeric, while xts requires some type of date object, so you'll need to convert it.
```

# 18.06.2018
## DS
- АНАЛИЗ МАЛЫХ ДАННЫХ КвазиНаучный блог Александра Дьяконова. [Cтекинг (Stacking) и блендинг (Blending)](https://alexanderdyakonov.wordpress.com/2017/03/10/c%D1%82%D0%B5%D0%BA%D0%B8%D0%BD%D0%B3-stacking-%D0%B8-%D0%B1%D0%BB%D0%B5%D0%BD%D0%B4%D0%B8%D0%BD%D0%B3-blending/)
- [Andrej Karpathy](https://medium.com/@karpathy). Director of AI at Tesla. Previously Research Scientist at OpenAI and PhD student at Stanford. I like to train deep neural nets on large datasets.
- The Asimov Institute. [THE NEURAL NETWORK ZOO](http://www.asimovinstitute.org/neural-network-zoo/)
- COOL! [10 steps to bootstrap your machine learning project (part 1)](https://blog.metaflow.fr/10-steps-to-bootstrap-your-machine-learning-project-part-1-aa7e1031f5b1)
Just split your dataset into three groups: the training set, the dev (or cross validation) set and the test set. A classic split is 70%, 15% and 15% of your whole dataset.
- [10 steps to bootstrap your machine learning project (part 2)](https://blog.metaflow.fr/10-steps-to-bootstrap-your-machine-learning-project-part-2-b6be78444c70)
- [Bootstrapping in R – Bootstrap Resampling and Examples](https://data-flair.training/blogs/bootstrapping-in-r/)

- [Kaggle: История о том как мы учились предсказывать релевантность поисковых запросов и заняли 3-е место](https://habr.com/post/305026/)
- [Как победить в соревновании на Kaggle. Советы Data Scientist-a](https://dev.by/lenta/indata-labs/kak-pobedit-v-sorevnovanii-na-kaggle-sovety-data-scientist-a)

## ЕГАИС
- [Поддельный алкоголь. Как не испортить праздник](https://journal.tinkoff.ru/kutezh/)
- [ЕГАИС. Информационный портал](http://egais2016.ru/)
- [Код алкогольной продукции в ЕГАИС. Классификатор видов алкогольной продукции](https://businessman.ru/kod-alkogolnoy-produktsii-v-egais-klassifikator-vidov-alkogolnoy-produktsii.html)
- [ЕГАИС: код алкогольной продукции из штрихкода акцизной марки](https://infostart.ru/public/456403/)
- [Приказ № 33н от 12 мая 2010 г. "Об утверждении перечня сведений о маркируемой алкогольной продукции, наносимых на федеральные специальные марки и считываемых с использованием технических средств..."](http://www.fsrar.ru/legalacts/base/orders/prikaz--n-ot--maya--g--ob-utverzhdenii-perechnya-s)
- [Проверка алкоголя по акцизной марке онлайн через ЕГАИС](http://znaybiz.ru/licenzirovanie/otdelnye-vidy-deatelnosti/akcizy/proverka-alkogolya-po-akciznoj-marke-onlajn-egais.html)
- [ЕГАИС - узнать информацию о товаре](https://www.forum.mista.ru/topic.php?id=788655)
- [Base-36 converter](http://extraconversion.com/base-number/base-36)
Base 36 or hexatridecimal is a positional numeral system using 36 as the radix. The choice of 36 is convenient in that the digits can be represented using the Arabic numerals 0-9 and the Latin letters A-Z. Plural name is base-36.
```
А давайте обсудим детали...
И так, имеем Приказ № 33н от 12 мая 2010 года (http://www.fsrar.ru/legalacts/base/orders/prikaz--n-ot--maya--g--ob-utverzhdenii-perechnya-s)
в котором сказано что:
Символы   Сведения
2   Версия ПС ЕГАИС
17  специальный идентификатор (тот самый алкокод только в формате base36)
12  Номер и дата заявки
6   Номер марки в заявке
31  Контрольная группа


с этим всё понятно. в итоге мы можем получить от 15-и до 19-и знаков (строку) АлкоКода
теоретически длина добивается нулями спереди до 19 знаков, если тот меньше получился
но вот лично для меня стало неожиданностью когда я увидел в базе ЕГАИС (через ЛК смотрел)
именно 15, 17, 18, 19-значные АлкоКоды у продукции (т.е. без добавления нулей спереди)
мне интересен алгоритм получения такого кода из считанной марки с бутылки.
вся соль заключается в том что где та граница, где стоит добавлять нули спереди, а где нет.
```

# 17.06.2018
## R & DS
- [Jake VanderPlas](http://vanderplas.com/speaking.html)
	- COOL! [Statistics for Hackers](http://christopherroach.com/articles/statistics-for-hackers/)
- [“Resampling: The New Statistics”](http://www.resample.com/intro-text-online/) by Julian L. Simon
- COOL! Вторая редакция книги Хадли. [Advanced R](https://adv-r.hadley.nz/evaluation.html)
- [Build httr Functions Automagically from Manual Browser Requests with the middlechild Package](https://rud.is/b/2018/06/15/build-httr-functions-automagically-from-manual-browser-requests-with-the-middlechild-package/)
- COOL! [mitmproxy is a free and open source interactive HTTPS proxy.](https://mitmproxy.org/)
	- [ropenscilabs/middlechild. R interface to MITM](https://github.com/ropenscilabs/middlechild)
	- [How To: Use mitmproxy to read and modify HTTPS traffic](https://blog.heckel.xyz/2013/07/01/how-to-use-mitmproxy-to-read-and-modify-https-traffic-of-your-phone/)
	- [Debugging Mobile Apps with mitmproxy](https://medium.com/sean3z/debugging-mobile-apps-with-mitmproxy-4596e56b3da2)
- [Prediction Interval, the wider sister of Confidence Interval](https://datascienceplus.com/prediction-interval-the-wider-sister-of-confidence-interval/)
- [Version 0.6-11 of NIMBLE released](https://r-nimble.org/version-0-6-11-of-nimble-released)
- [It's that easy! Image classification with keras in roughly 100 lines of code](https://shirinsplayground.netlify.com/2018/06/keras_fruits/)
- [The Statistical Bootstrap and Other Resampling Methods](http://www.burns-stat.com/documents/tutorials/the-statistical-bootstrap-and-other-resampling-methods-2/)

# 15.06.2018
## R
- ряд полезных функций: `stringi::stri_trim_both`, `stringr::str_squish`, `stringr::str_trunc`, `rlang::squash_chr`
- ["Busy..." / "Done!" / "Error" feedback after pressing a button](https://github.com/daattali/advanced-shiny/tree/master/busy-indicator)
- Infosec. [toolsmith #133 - Anomaly Detection & Threat Hunting with Anomalize](https://holisticinfosec.blogspot.com/2018/06/toolsmith-133-anomaly-detection-threat.html)
- [Generate a set of random unique integers from an interval](https://stackoverflow.com/questions/17773080/generate-a-set-of-random-unique-integers-from-an-interval)

# 14.06.2018
## R
- [Anomaly Detection for Business Metrics with R](https://analyzecore.com/2018/06/13/anomaly-detection-for-business-metrics-with-r/)
- [rstudio/DT. async support {#543} Open](https://github.com/rstudio/DT/issues/543)
- [Mixed Models with Adaptive Gaussian Quadrature](https://iprogn.blogspot.com/2018/06/mixed-models-with-adaptive-gaussian.html)
- [reticulate – another step towards a multilingual and collaborative way of working](https://blog.eoda.de/2018/06/14/reticulate-another-step-towards-a-multilingual-and-collaborative-way-of-working/)

## DS
- [Практические аспекты машинного обучения](https://www.osp.ru/os/2016/01/13048648/)
- [Introduction to Local Interpretable Model-Agnostic Explanations (LIME)](https://www.oreilly.com/learning/introduction-to-local-interpretable-model-agnostic-explanations-lime)

# 13.06.2018
## Apache Kafka, Tarantool, etc.
- [Apache Kafka и миллионы сообщений в секунду](https://habr.com/company/tinkoff/blog/342892/)
	1. Нет потребителей — скорость падает.
Если новые сообщения тут же никто не забирает, они сохраняются на диск. А это очень дорогая операция. Поэтому если потребители внезапно отключились или “залагали”, пропускная скорость упадет.
	2. Чем больше размер сообщения, тем выше пропускная способность
- [Инструментарий специалиста по большим данным: Apache Kafka](http://datareview.info/article/instrumentariy-spetsialista-po-bolshim-dannyim-apache-kafka/)
- [Tarantool: как сэкономить миллион долларов на базе данных на высоконагруженном проекте](https://habr.com/company/oleg-bunin/blog/310690/). Материал старый, но подробно объясняет идеологию решения.
- [Building a Kafka and Spark Streaming pipeline - Part I](https://tlfvincent.github.io//2016/09/25/kafka-spark-pipeline-part-1/)
- [Для чего нужен Apache Ignite / GridGain, на примере .NET & C#](https://habr.com/company/gridgain/blog/325830/). Что это такое и зачем?
Самый простой и ёмкий ответ — это база данных. В основе которой — хранилище "ключ-значение"; грубо говоря, ConcurrentDictionary, в котором данные расположены на нескольких машинах.
- Раньше объясняли подробно. [Второе рождение гридов](https://www.osp.ru/os/2013/08/13037859/)
- [On Apache Ignite, Apache Spark and MySQL. Interview with Nikita Ivanov](http://www.odbms.org/blog/2017/06/on-apache-ignite-apache-spark-and-mysql-interview-with-nikita-ivanov/). Nikita Ivanov, CTO of GridGain
- Очень хорошее объяснение. [Apache® Ignite™ and Apache® Spark™: Complementary In-Memory Computing Solutions](https://insidebigdata.com/2016/06/20/apache-ignite-and-apache-spark-complementary-in-memory-computing-solutions/)
- [Недопонимание CAP-теоремы](https://habr.com/post/136305/).
- [К чему относится Ignite исходя из CAP теоремы, к CP или CA?](https://habr.com/company/gridgain/blog/325830/). Ответ -- CP

## R
- [The Popularity of Point-and-Click GUIs for R](http://r4stats.com/2018/06/12/gui-popularity/)
	- [Rattle](https://rattle.togaware.com/)
	- [R commander (Rcmdr)](http://www.rcommander.com/)
	- [BlueSky](http://www.blueskystatistics.com/). Fully featured Statistics application and development framework built on the open source R project
- [The ssh Package: Secure Shell (SSH) Client for R](https://ropensci.org/technotes/2018/06/12/ssh-02/)
- [Merging spatial buffers in R](https://aghaynes.wordpress.com/2018/06/11/merging-spatial-buffers-in-r/)
- [Anomaly Detection in R](https://r-posts.com/anomaly-detection-in-r/)
- [MODIStsp v. 1.3.4 is out ! Now allowing interactive definition of processing extent!](https://lbusett.netlify.com/post/modistsp-v-1-3-4-is-out-now-allowing-interactive-definition-of-processing-extent/). MODIStsp is a “R” package devoted to automatizing the creation of time series of raster images derived from MODIS Land Products data. MODIStsp allows to perform several preprocessing steps (e.g., download, mosaicing, reprojection, resize, data extraction) on MODIS data available within a given time period. Users have the ability to select which specific layers of the original MODIS HDF files they want to process. They also can select which additional Quality Indicators should be extracted from the aggregated MODIS Quality Assurance layers and, in the case of Surface Reflectance products, which Spectral Indexes should be computed from the original reflectance bands.
- [Create outstanding dashboards with the new semantic.dashboard package](https://appsilondatascience.com/blog/rstats/2018/06/11/dashboard-tutorial.html)
- Весьма наглядно. [Why loops are slow in R](https://privefl.github.io/blog/why-loops-are-slow-in-r/)
- [Customizing time and date scales in ggplot2](https://www.statworx.com/de/blog/customizing-time-and-date-scales-in-ggplot2/)
- [Top Tip: Don't keep your data prep in the same project as your Shiny app](https://www.mango-solutions.com/blog/top-tip-don-t-keep-your-data-prep-in-the-same-project-as-your-shiny-app)
- Clustering
	- [K-Means Clustering in R Tutorial](https://www.datacamp.com/community/tutorials/k-means-clustering-r)
	- [Articles - Partitioning Clustering Essentials. K-Means Clustering Essentials](http://www.sthda.com/english/articles/27-partitioning-clustering-essentials/87-k-means-clustering-essentials/)
	- [Articles - Cluster Analysis in R: Practical Guide. Clustering Example: 4 Steps You Should Know](http://www.sthda.com/english/articles/25-cluster-analysis-in-r-practical-guide/108-clustering-example-4-steps-you-should-know/)
	- [How to produce a pretty plot of the results of k-means cluster analysis?](https://stats.stackexchange.com/questions/31083/how-to-produce-a-pretty-plot-of-the-results-of-k-means-cluster-analysis)

# 09.06.2018
## General
- [Commandline](http://www.commandline.co.uk/). Free open source software. Cmdow/Mtee/Batch Function Library.
- [zarunbal/LogExpert](https://github.com/zarunbal/LogExpert). Windows tail program and log file analyzer.

## R
- COOL! [Interactive Linking of Text and Visualizations](http://vti-example.fbeck.com/). [Статья](https://www.vis.wiwi.uni-due.de/uploads/tx_itochairt3/publications/vti_euvis2018.pdf)
- [Mara Averick Twitter](https://twitter.com/dataandme)
- [Custom snippets in RStudio: ⚡ faster tweet chunks for all](https://maraaverick.rbind.io/2017/09/custom-snippets-in-rstudio-faster-tweet-chunks-for-all/)
- [Designing the nteract Data Explorer](https://blog.nteract.io/designing-the-nteract-data-explorer-f4476d53f897)
- COOL! [Open  Access VIS](http://oavis.steveharoz.com/). A collection of open access visualization research at the VIS 2017 conference. Info about the symbols and open access. To edit the data, see GitHub.
- COOL! [An introduction to data cleaning with R](https://cran.r-project.org/doc/contrib/de_Jonge+van_der_Loo-Introduction_to_data_cleaning_with_R.pdf)
- [How to get the name of the calling function inside the called routine?](https://stackoverflow.com/questions/15595478/how-to-get-the-name-of-the-calling-function-inside-the-called-routine)
For the record, as Hadley has suggested, you can use `sys.call()`. For example:
```
funx = function(...) {
    callingFun = as.list(sys.call(-1))[[1]]
    calledFun = as.list(sys.call())[[1]]
    message(paste(callingFun, " is calling ", calledFun, sep=""))
}
```
Важное продолжение: [Converting language type to string in R using infix notation](https://stackoverflow.com/questions/33496319/converting-language-type-to-string-in-r-using-infix-notation)
```
typeof(someExpr[[3]])
[1] "language"
```
!!!!! You can use `deparse`:
```
someExpr <- substitute(a+2*b)
result<-deparse(someExpr[[3]])
result
[1] "2 * b"

str(result)
chr "2 * b"
```
По умолчанию длина выдаваемой `deparse` строки ограничена 60-ю символами, но это правится в параметрах.

# 06.06.2018
## R
- [In R, how to get an object's name after it is sent to a function?](https://stackoverflow.com/questions/10520772/in-r-how-to-get-an-objects-name-after-it-is-sent-to-a-function)
- [Creating zip file from folders in R](https://stackoverflow.com/questions/23668395/creating-zip-file-from-folders-in-r)
- COOL! [Database bulk update and inline editing in a Shiny Application](https://www.mango-solutions.com/blog/database-bulk-update-and-inline-editing-in-shiny-application)

## DS
- [An introduction to machine learning with Keras in R](https://theoreticalecology.wordpress.com/2018/06/06/an-introduction-to-machine-learning-with-keras-in-r/)
- CLASSIFICATION FROM SCRATCH]
	- [OVERVIEW 0/8](https://freakonometrics.hypotheses.org/52731)
	- [LOGISTIC REGRESSION 1/8](https://freakonometrics.hypotheses.org/52747)
	- [LOGISTIC WITH SPLINES 2/8](https://freakonometrics.hypotheses.org/52771)
	- [LOGISTIC WITH KERNELS 3/8](https://freakonometrics.hypotheses.org/52815)
	- [PENALIZED RIDGE LOGISTIC 4/8](https://freakonometrics.hypotheses.org/52773)
	- [PENALIZED LASSO LOGISTIC 5/8](https://freakonometrics.hypotheses.org/52894)
	- [NEURAL NETS 6/8](https://freakonometrics.hypotheses.org/52774)
	- [SVM 7/8](https://freakonometrics.hypotheses.org/52775)
	- [LINEAR DISCRIMINATION 8/8](https://freakonometrics.hypotheses.org/53021)
	- [TREES 9/8](https://freakonometrics.hypotheses.org/52776)
	- [BAGGING AND FORESTS 10/8](https://freakonometrics.hypotheses.org/52777)

# 04.06.2018
## R
- [Even Simpler SQL](https://www.johnmackintosh.com/2018-06-03-even-simpler-sql/)
- [rqdatatable: rquery Powered by data.table](http://www.win-vector.com/blog/2018/06/rqdatatable-rquery-powered-by-data-table/)
- [Coloring Sudokus](https://fronkonstin.com/2018/06/01/coloring-sudokus/)
- [New R package xplain: Providing interactive interpretations and explanations of statistical results](https://topics-in-r.blogspot.com/2018/05/new-r-package-xplain-providing.html)
- [Deep Catalan roots: playing with stringdist](https://ikashnitsky.github.io/2018/deep-catalan-roots/)
- COOL! [What's the fastest way to determine the number of rows of a CSV in R?](https://gist.github.com/peterhurford/0d62f49fd43b6cf078168c043412f70a)
- COOL! [Advanced R. 21 Quasiquotation](https://adv-r.hadley.nz/quasiquotation.html)

# 31.05.2018
## R
- [User authentication in R Shiny - sneak peek of shiny.users and shiny.admin packages](https://appsilondatascience.com/blog/rstats/2018/05/30/user-authentication-in-r-shiny.html)
- [Regulex JavaScript Regular Expression Visualizer](https://jex.im/regulex)
- [Demystifying life expectancy calculations](http://freerangestats.info/blog/2018/05/31/life-expectancy)
- [Defining Marketing with the Rvest and Tidytext Packages](https://r.prevos.net/rvest-and-tidytext/)


## MS
- Otlook. [сообщение "невозможно выполнить эту операцию так как сообщение было изменено"](https://answers.microsoft.com/ru-ru/msoffice/forum/msoffice_outlook-mso_windows8/%D1%81%D0%BE%D0%BE%D0%B1%D1%89%D0%B5%D0%BD%D0%B8/485a84be-c1a1-48d8-874f-81aa178d7a3f)

## Ответ Кате v3. RE: X5 FW: Бизнес-отчетность (дополнения выделены зеленым)
Касательно темы референс визитов тоже есть важное уточнение.
Переход от закрытых вендорских продуктов к опенсорс решениям понятие референс визита практически потеряло свою актуальность.
 - ПО бесплатно;
 - исходники все доступны;
 - развивают компоненты «всем миром»;
 - множество людей и компаний ведут блоги по задачам,  технологиям и решениям;
 - регулярно проводят конференции, материалы которых полностью доступны, включая видеозаписи.

Если говорить о компонентах предлагаемого нами решения R, то весьма занимательно проглядеть материалы европейской конференции EARL, в частности [EARL 2017 London](https://earlconf.com/2017/london/), а также логотипы участников и спонсоров, большое количество грандов принимает [активное участие](https://earlconf.com/2017/downloads/london/EARL-London-2017-Agenda.pdf).

Очень много кейсов по применению указанного фреймворка для бизнес задач.
Например, крайне интересны:
 - кейс с мониторингом системы городского транспорта Лондона – [«Every Journey Matters Use of R at TfL»](https://earlconf.com/2017/downloads/london/presentations/EARL2017_-_London_-_Ashley_Turner_-_Every_journey_matters.pdf)
 - кейс с мониторингом канализации Великобритании – [«USING R TO MONITOR SEWER NETWORK PERFORMANCE FOR THE WATER INDUSTRY»](https://earlconf.com/2017/downloads/london/presentations/EARL2017_-_London_-_Joy%20McKenny_-_Using_R_to_monitor_sewer_network_performance.pdf);
сложно найти более жизненные варианты.


# 01.06.2018
## R
- COOL! [THREE WAYS OF VISUALIZING A GRAPH ON A MAP](https://datascience.blog.wzb.eu/2018/05/31/three-ways-of-visualizing-a-graph-on-a-map/)
- [choroplethr](https://github.com/arilamstein/choroplethr) simplifies the creation of choropleths (thematic maps) in R
	- choroplethr. [New Version of ggplot2](https://arilamstein.com/blog/2018/05/30/new-version-of-ggplot2/)
	- [A Shiny app to demonstrate the datasets that ship with choroplethr v3.1.0](https://github.com/arilamstein/choroplethr-3-1-0-shiny-app)
- COOL! COOL! [A comprehensive survey of the types of things in R. 'mode' and 'class' and 'typeof' are insufficient](https://stackoverflow.com/questions/8855589/a-comprehensive-survey-of-the-types-of-things-in-r-mode-and-class-and-type)
- COOL! [How to repeat a String N times in R?](How to repeat a String N times in R?)


# 30.05.2018
## R
- [Daily Streamflow Trend Analysis](https://owi.usgs.gov/blog/Quantile-Kendall/)
- COOL! [A recipe for recipes](https://edwinth.github.io/blog/recipes_blog/)
- [Native scoring in SQL Server 2017 using R](https://tomaztsql.wordpress.com/2018/05/28/native-scoring-in-sql-server-2017-using-r/)
- COOL! [TAKE SCREENSHOT OF WEBPAGE USING R](https://www.listendata.com/2018/05/take-screenshot-of-webpage-using-r.html)
- [SHINYPROXY 1.1.1 RELEASED!](https://www.openanalytics.eu/blog/2018/05/28/shinyproxy-1.1.1/)
- COOL! [Performance: captureOutput() is Much Faster than capture.output()](https://www.jottr.org/2014/05/26/captureoutput/)

# 28.05.2018
## R
- [Interprocess data sharing between R sessions](https://github.com/renkun-ken/sharedata)
- [RStudio:addins part 3 - View objects, files, functions and more with 1 keypress](https://jozefhajnala.gitlab.io/r/r103-keypress-viewer/)


# 25.05.2018
## R
- [sample_n_of(): a useful helper function](https://www.tjmahr.com/sample-n-groups/)
- [panelView: Visualizing Panel Data with Dichotomous Treatments](http://yiqingxu.org/software/panelView/panelView.html)
- [How Many Factors to Retain in Factor Analysis](https://neuropsychology.github.io/psycho.R//2018/05/24/n_factors.html)
- [Selective Raster Graphics](https://www.stat.auckland.ac.nz/~paul/Reports/rasterize/rasterize.html)
- Важные нюансы по `testthat`:
	- [Setup and teardown](https://www.tidyverse.org/articles/2017/12/testthat-2-0-0/): tests/testthat/setup-xyz.R files are run before the first test file is executed. They are similar to the existing helpers-xyz.R files, but are not run by devtools::load_all(). Similarly, test/teststhat/teardown-xyz.R files are run after all tests are complete; use these to clean up any global changes made by the setup files.
	- Из документации "• Helper files start with helper and are executed before tests are run and from `devtools::load_all()`"
- [Merge Multiple spaces to single space; remove trailing/leading spaces
](https://stackoverflow.com/questions/25707647/merge-multiple-spaces-to-single-space-remove-trailing-leading-spaces).
`stringr::str_squish(string)` or `qdap::Trim(qdap::clean(string))

# 24.05.2018
## ELK & nix
- [Installing the ELK Stack on Windows](https://logz.io/blog/installing-the-elk-stack-on-windows/)
- [Памятка пользователям ssh](https://habr.com/post/122445/)

# 23.05.2018
## R
- COOL! [A perfect RStudio layout](https://ikashnitsky.github.io/2018/perfect-rstudio-layout/)

# 22.05.2018
## R & Shiny
- Смотрим запущенные процессы. Различные команды, например `top` + кнопка `1` или `htop`. [Команда top в Linux](https://vps.ua/wiki/beginners/top-command/)
- Смотрим запущенные процессы R (из под shiny server): `ps -aux | grep "exec/R --no-save"`
- [RStudio Shiny Pro Pricing guide](https://shiny-server.chargifypay.com/h/3384909/subscriptions/new). Сервера просто работают в параллель.
- [RStudio Connect Admin Guide](http://docs.rstudio.com/connect/admin/#). Для расширения требуется Execution Server
	- [pdf версия](http://docs.rstudio.com/connect/admin/index.pdf)
- [Подробно про Connect Execution Server](https://blog.rstudio.com/2017/12/01/rstudio-connect-v1-5-10/)
- [И еще](https://blog.rstudio.com/2018/04/12/rstudio-connect-1-6-0-a-year-in-the-making/). В Админ гайде это проходит под пунктом [6 High Availability and Load Balancing](http://docs.rstudio.com/connect/admin/high-availability.html)
- [RStudio Configuration and sizing recommendations](https://support.rstudio.com/hc/en-us/articles/115002344588-Configuration-and-sizing-recommendations)


# 21.05.2018
## R
- [Pivotal | R](https://pivotalsoftware.github.io/gp-r/) A place for all things Pivotal & R
- COOL! [Create Code Metrics with cloc](https://rud.is/b/2018/05/19/create-code-metrics-with-cloc/)
- COOL! [Wrangling Data Table Out Of the FBI 2017 IC3 Crime Report](https://rud.is/b/2018/05/08/wrangling-data-table-out-of-the-fbi-2017-ic3-crime-report/)
- [Beautiful and Powerful Correlation Tables in R(https://neuropsychology.github.io/psycho.R//2018/05/20/correlation.html)
- [openrouteservice – geodata!](https://aghaynes.wordpress.com/2018/05/19/openrouteservice-geodata/)

# 18.05.2018
## R
- COOL `group_by_at` [dplyr group by colnames described as vector of strings](https://stackoverflow.com/questions/47912107/dplyr-group-by-colnames-described-as-vector-of-strings)
- COOL [Update Programming with dpyr article to reference group_by_at ? {#3114}](https://github.com/tidyverse/dplyr/issues/3114)
- [19.6.2 Writing pipeable functions](http://r4ds.had.co.nz/functions.html)


# 16.05.2018
## R
- COOL! [icon: web icons for rmarkdown](https://ropensci.org/technotes/2018/05/15/icon/)
- [Workaround for tidyr::spread with duplicate row identifiers](https://www.daeconomist.com/post/2018-05-15-spread/)

# 15.05.2018
## R
- COOL! [RStudio:addins part 2 - roxygen documentation formatting made easy](https://jozefhajnala.gitlab.io/r/r102-addin-roxytags/)
- [Tips for Ellipse Summary Plot](https://tomizonor.wordpress.com/2018/05/13/tips-for-ellipse-summary-plot/)
- [VISUALIZING GRAPHS WITH OVERLAPPING NODE GROUPS](https://datascience.blog.wzb.eu/2018/05/11/visualizing-graphs-with-overlapping-node-groups/)
- [Mimicking SQLDF with MonetDBLite](https://statcompute.wordpress.com/2018/05/09/mimicking-sqldf-with-monetdblite/)
- [sparklyr 0.8](https://blog.rstudio.com/2018/05/14/sparklyr-0-8/)
- [rquery: Relational Query Generator for Data Manipulation at Scale](https://cran.r-project.org/web/packages/rquery/index.html)
A 'SQL' query generator based on Edgar F. Codd's relational algebra and experience using 'SQL' and 'dplyr' at big data scale. The design represents an attempt to make 'SQL' more teachable by denoting composition by a sequential pipeline notation instead of nested queries or functions. The implementation delivers reliable high performance data processing on large data systems such as ‘Spark' and databases. Package features include: data processing trees or pipelines as observable objects (able to report both columns produced and columns used), optimized ’SQL' generation as an explicit user visible modeling step, and convenience methods for applying query trees to in-memory 'data.frame's.
- [ArgumentCheck: Improved Communication to Users with Respect to Problems in Function Arguments](https://cran.r-project.org/web/packages/ArgumentCheck/)
- COOL! [Programming with R. Creating Functions](https://swcarpentry.github.io/r-novice-inflammation/02-func-R/)

# 10.05.2018
## R
- COOL! [Creating new data with max values for each subject](https://webbedfeet.netlify.com/post/creating-new-data-with-max-values-for-each-subject-2/)
- COOL! [Tidying messy Excel data (tidyxl)](https://webbedfeet.netlify.com/post/tidying-messy-excel-data-tidyxl/)
	- [unpivotr](https://nacnudus.github.io/unpivotr/index.html). unpivotr deals with non-tabular data, especially from spreadsheets.
	- [tidyxl](https://nacnudus.github.io/tidyxl/). tidyxl imports non-tabular data from Excel files into R.
- [Going from a human readable Excel file to a machine-readable csv with {tidyxl}](http://www.brodrigues.co/blog/2018-09-11-human_to_machine/)
- Как поставить пакеты в R, если есть проблемы с https сертификатами. Выдает ошибку:
```
Warning messages:
1: In download.file(url, destfile = f, quiet = TRUE) :
 URL 'https://cran.r-project.org/CRAN_mirrors.csv': status was 'Peer certificate cannot be authenticated with given CA certificates'
2: package ‘httr’ is not available (for R version 3.4.4)
```
решил вопрос путем обхода секьюрности флагами: `install.packages("httr", method="wget", extra="--no-check-certificate")`

# 07.05.2018
## R
- [Checking (G)LM model assumptions in R](https://biologyforfun.wordpress.com/2014/04/16/checking-glm-model-assumptions-in-r/)
- [Calculating optimal number of bins in a histogram](https://stats.stackexchange.com/questions/798/calculating-optimal-number-of-bins-in-a-histogram)
- COOL! [Data Binning and Plotting](http://www.jdatalab.com/data_science_and_data_mining/2017/01/30/data-binning-plot.html)
- [Remove password protection from Excel sheets using R](https://ryouready.wordpress.com/2018/05/06/remove-password-protection-from-excel-sheets-using-r/)
- COOL! [Coordinate systems in ggplot2: easily overlooked and rather underrated](https://www.statworx.com/de/blog/coordinate-systems-in-ggplot2-easily-overlooked-and-rather-underrated/)

## Statistics
- COOL! [Understanding the basis of GLM Regression (Logistic, Gaussian, Gamma, etc)](https://tsmatz.wordpress.com/2017/08/30/glm-regression-logistic-poisson-gaussian-gamma-tutorial-with-r/)
- [Is there any difference between lm and glm for the gaussian family of glm?](https://stats.stackexchange.com/questions/181113/is-there-any-difference-between-lm-and-glm-for-the-gaussian-family-of-glm)
- The Analysis Factor. [Generalized Linear Models (GLMs) in R, Part 4: Options, Link Functions, and Interpretation](https://www.theanalysisfactor.com/generalized-linear-models-glm-r-part4/)

# 04.05.2018
## RStudio
- [Difference between R MarkDown and R NoteBook](https://stackoverflow.com/questions/43820483/difference-between-r-markdown-and-r-notebook)

## Retail
- [Price look-up code {PLU}](https://en.wikipedia.org/wiki/Price_look-up_code)
- [What’s the Difference between a UPC and EAN?](https://www.nationwidebarcode.com/whats-the-difference-between-a-upc-and-ean/)
- [Retail Numbering Systems](http://www.himatix.com/resources/manage/retail_numbering.html)

# 03.05.2018
## R
- [Done “Establishing DBI”!?](https://www.r-dbi.org/blog/dbi-2-final/) The “Establishing DBI” project, funded by the R consortium, started about a year ago. It includes the completion of two new backends, RPostgres and RMariaDB, and a quite a few interface extensions and specifications.
- Re-exporting the magrittr pipe operator
	- COOL! отвечают знаменитости. [Magrittr %>% inside a package](https://community.rstudio.com/t/magrittr-inside-a-package/2033/7).
		- jennybryanRStudio EmployeeOct '17
The solution from @alistaire basically summarizes how this is handled within tidyverse packages, which often import and re-export the %>% for the user’s convenience. They are less likely to actually use the pipe internally.
`usethis::use_pipe()` does the necessary mechanics (caveat: usethis isn’t on CRAN yet, but will be). That’s about as close as you’ll get to an “official” solution.
		- alistaireOct '17
In practice, `%>%` tends to be re-exported, which can be done in a couple ways, e.g. `dplyr/R/utils.r` 7's concise
```
#' @importFrom magrittr %>%
#' @export
```
	- [R: use magrittr pipe operator in self written package](https://stackoverflow.com/questions/27947344/r-use-magrittr-pipe-operator-in-self-written-package/27979637#27979637)
- [Read Random Rows from A Huge CSV File](https://statcompute.wordpress.com/2018/04/28/read-random-rows-from-a-huge-csv-file/). pure R & python in R solutions.
- [Using Shiny Dashboards for Financial Analysis](https://r-posts.com/using-shiny-dashboards-for-financial-analysis/)
- [Extreme Makeover: R Graphics Edition](https://www.stat.auckland.ac.nz/~paul/Reports/deviceloc/deviceloc.html)
- [How To: LEGO mosaics from photos using R & the tidyverse](http://www.ryantimpe.com/2018/04/23/lego-mosaic1/)
- [Get your tracks from the Strava API and plot them on Leaflet maps](https://rcrastinate.blogspot.ru/2018/05/get-your-tracks-from-strava-api-and.html)
- [Simulating animal movements and habitat use](https://allthiswasfield.blogspot.ru/2018/05/simulating-animal-movements-and-habitat.html)
- [purrr Like a Kitten till the Lake Pipes RoaR](https://www.finex.co/purrr-like-a-kitten-till-the-lake-pipes-roar/)
- [March 2018: "Top 40" New Package Picks](https://rviews.rstudio.com/2018/04/30/march-2018-top-40-new-package-picks/)
	- [tsfknn v0.1.0](https://cran.r-project.org/package=tsfknn): Provides a function to forecast time series using nearest neighbors regression. See Martinez et al. (2017) and the vignette for details. [Time Series Forecasting with KNN in R: the tsfknn Package](https://cran.r-project.org/web/packages/tsfknn/vignettes/tsfknn.html)

## Time-Series anomaly Detection & Forecasting
- [Detecting Correlation Among Multiple Time Series](https://anomaly.io/detect-correlation-time-series/)
- [Anomaly Detection Using K-Means Clustering](https://anomaly.io/anomaly-detection-clustering/)
- [Understanding Cross-Correlation, Auto-Correlation, Normalization and Time Shift](https://anomaly.io/understand-auto-cross-correlation-normalized-shift/)
- [An Introduction to Time Series Forecasting with Prophet Package in Exploratory](https://blog.exploratory.io/an-introduction-to-time-series-forecasting-with-prophet-package-in-exploratory-129ed0c12112)
- [Time Series Forecasting with KNN in R: the tsfknn Package](https://cran.r-project.org/web/packages/tsfknn/vignettes/tsfknn.html)

# 25.04.2018
## R
- [Using glue_sql()](https://db.rstudio.com/best-practices/run-queries-safely/#using-glue_sql)
Parameterized queries are generally the safest and most efficient way to pass user defined values in a query, however not every database driver supports them. The function glue_sql(), part of the the glue package, is able to handle the SQL quoting and variable placement.
- [Командная строка EmEditor](http://www.emeditor.org/en/howto_file_file_commandline.html) (нужна для настройки AstroGrep)
- Проблема с tibbletime. По умолчанию он считает, что индекс в UTC. Однако есть внутренние атрибуты индекса! См. [Create tbl_time objects](https://business-science.github.io/tibbletime/reference/tbl_time.html). The information stored about `tbl_time` objects are the `index_quo` and the `index_time_zone`. These are stored as attributes, with the `index_quo` as a `rlang::quosure()` and the `time_zone` as a string.

# 24.04.2018
## R
- COOL! [Semantic dashboard - new open source R Shiny package](https://appsilondatascience.com/blog/rstats/2018/04/23/semanticdashboard.html)
- COOL! [An Introduction to Greta](https://rviews.rstudio.com/2018/04/23/on-first-meeting-greta/). I had assumed that the tensorflow and reticulate packages would eventually enable R developers to look beyond deep learning applications and exploit the TensorFlow platform to create all manner of production-grade statistical applications. BUT greta lets users write TensorFlow-based Bayesian models directly in R! What could be more charming?
- [Big changes behind the scenes in R 3.5.0](http://blog.revolutionanalytics.com/2018/04/r-350.html)
 	- [Preview: ALTREP promises to bring major performance improvements to R](http://blog.revolutionanalytics.com/2017/09/altrep-preview.html). Тут есть ссылки на презентации.
	- [WHAT'S IN A VECTOR?](https://gmbecker.github.io/jsm2017/jsm2017.html) by GABRIEL BECKER, LUKE TIERNEY, TOMAS KALIBERA
	- [ALTREP: Alternative Representations for R Objects](https://svn.r-project.org/R/branches/ALTREP/ALTREP.html)
	- [Big vectors coming to R](http://blog.revolutionanalytics.com/2012/07/big-vectors-coming-to-r.html)
- hrbrthemes 0.5
	- [Titillium Web-based font](https://fonts.google.com/specimen/Titillium+Web)
- COOL Shiny Tweak. [Adding text (or inputs) to the navigation bar in a navbarPage](https://github.com/daattali/advanced-shiny/tree/master/navbar-add-text)

# 23.04.2018
## R
- [Packaging Shiny applications: A deep dive](https://www.mango-solutions.com/blog/packaging-shiny-applications-a-deep-dive)

# 20.04.2018
## DS
- ODS блог. [Ассоциативные правила, или пиво с подгузниками](https://habrahabr.ru/company/ods/blog/353502/)
- [Почему расчет перцентилей работает не так как вы ожидаете?](https://habrahabr.ru/post/274303/)
- [yahoo/kafka-manager](https://github.com/yahoo/kafka-manager) A tool for managing Apache Kafka.

# 18.04.2018
## R
- [How to save and load environment objects in R](https://www.techcoil.com/blog/how-to-save-and-load-environment-objects-in-r/).
`save.image(file='myEnvironment.RData')` & load('myEnvironment.RData')
- [A better way of saving and loading objects in R](https://www.fromthebottomoftheheap.net/2012/04/01/saving-and-loading-r-objects/)
- [Convert comma separated numbers in a character string to numeric vector {duplicate}](https://stackoverflow.com/questions/44521042/convert-comma-separated-numbers-in-a-character-string-to-numeric-vector?rq=1)
- Как схлопнуть все уровни в списках? `flatten` не способен, надо брать `rlang::squash()` --  Flatten or squash a list of lists into a simpler vector
- [`strrep`: Repeat the Elements of a Character Vector](https://rdrr.io/r/base/strrep.html)

# 17.04.2018
## R
- [Maximum Likelihood Estimation For Regression](https://medium.com/quick-code/maximum-likelihood-estimation-for-regression-65f9c99f815d)
- [loo 2.0 is loose](http://andrewgelman.com/2018/04/16/loo-2-0-loose/). We’re happy to announce the release of v2.0.0 of the loo R package for efficient approximate leave-one-out cross-validation (and more). For anyone unfamiliar with the package, the original motivation for its development is in our paper:
- GIS. [ORDNANCE SURVEY TERRAIN 50: MERGING IN R](https://scottishsnow.wordpress.com/2018/04/16/ordnance-survey-terrain-50-merging-in-r/):
```
library(rgdal)
library(gdalUtils)
f = list.files("~/Downloads/temp", pattern=".asc", full.names=T)
mosaic_rasters(f, paste0(normalizePath("~"), "/GIS/OS/Terrain50.tif"))
```
- COOL! [Adding Intel MKL easily via a simple script](http://dirk.eddelbuettel.com/blog/2018/04/15/#018_mkl_for_debian_ubuntu)
- Join
	- COOL! [STAT 545. Cheatsheet for dplyr join functions](http://stat545.com/bit001_dplyr-cheatsheet.html) by Jenny Bryan
	- COOL! [Joining Data in R with dplyr](http://www.rpubs.com/williamsurles/293454) by William Surles, 2017-07-20

- COOL! [How to group by all but one columns?](https://stackoverflow.com/questions/39181208/how-to-group-by-all-but-one-columns): Building on the @eipi10's dplyr 0.7.0 edit, `group_by_at` appears to be the right function for this job.

# 16.04.2018
## R
- [{pmice}, an experimental package for missing data imputation in parallel using {mice} and {furrr}](http://www.brodrigues.co/blog/2018-04-15-announcing_pmice/)
- [Imputing missing values in parallel using {furrr}](http://www.brodrigues.co/blog/2018-04-14-playing_with_furrr/)
- COOL [Supercharge your R code with wrapr](http://www.win-vector.com/blog/2018/01/supercharge-your-r-code-with-wrapr/)
- COOL! lubridate. Как подхватить месяц, написанный словами? [Handling dates in R](https://skgrange.github.io/date_handling.html) by Stuart Grange, 2016-08-22.
С определенной натяжкой получается конструкцией `stri_datetime_parse("19 декабрь 2015", "dd-LLLL-yyyy", tz="Europe/Moscow", locale="ru_RU")`

# 13.04.2108
## R
- [Convert epub to Text for Processing in R](https://rud.is/b/2018/04/12/convert-epub-to-text-for-processing-in-r/)
- COOL! [PIMP MY RMD: A FEW TIPS FOR R MARKDOWN](https://www.r-graph-gallery.com/pimp-my-rmd-a-few-tips-for-r-markdown/)
	- Сам документ. [Pimp my RMD: a few tips for R Markdown](https://holtzy.github.io/Pimp-my-rmd/) by Yan Holtz - 11 April 2018
- [Regular Expressions Every R programmer Should Know](https://blog.jumpingrivers.com/posts/2018/top_regular_expressions_r_stringr/)
- [future 1.8.0: Preparing for a Shiny Future](https://www.jottr.org/2018/04/12/future-results/)
- [readtext: Import and Handling for Plain and Formatted Text Files](https://cran.r-project.org/web/packages/readtext/)
- [R: assign() inside nested functions](https://emilkirkegaard.dk/en/?p=5718). The call that does the trick is the last one, namely the one using `assign()`. Here we modify an object outside the function’s own environment. How do we know which one to modify? Well, we take one step back (`pos = 1`). Alternatively, one could have used `<<-`.

## SQL
- [10 Easy Steps to a Complete Understanding of SQL](https://blog.jooq.org/2016/03/17/10-easy-steps-to-a-complete-understanding-of-sql/)
- [Parameterized queries](https://db.rstudio.com/best-practices/run-queries-safely#parameterized-queries)
- [odbc](https://db.rstudio.com/odbc/). The goal of the odbc package is to provide a DBI-compliant interface to Open Database Connectivity (ODBC) drivers. This allows for an efficient, easy to setup connection to any database with ODBC drivers available, including SQL Server, Oracle, MySQL, PostgreSQL, SQLite and others. The implementation builds on the nanodbc C++ library.



# 12.04.2018
## R
- COOL! [Neglected R Super Functions](http://www.win-vector.com/blog/2018/04/neglected-r-super-functions/)
- COOL! [Assign multiple new variables on LHS in a single line in R](https://stackoverflow.com/questions/7519790/assign-multiple-new-variables-on-lhs-in-a-single-line-in-r)
	- [zeallot: Multiple, Unpacking, and Destructuring Assignment](https://cran.r-project.org/web/packages/zeallot/index.html)
Provides a %<-% operator to perform multiple, unpacking, and destructuring assignment in R. The operator unpacks the right-hand side of an assignment into multiple values and assigns these values to variables on the left-hand side of the assignment.
	- [Matlab-style multiple assignment in R](https://strugglingthroughproblems.wordpress.com/2010/08/27/matlab-style-multiple-assignment-in%C2%A0r/). Posted on August 27, 2010
- [Comparison of String Distance Algorithms](https://www.joyofdata.de/blog/comparison-of-string-distance-algorithms/). Posted on 2013/08/21
- применимо и к selectizeInput [reactive radioButtons with tooltipBS in shiny](https://stackoverflow.com/questions/36132204/reactive-radiobuttons-with-tooltipbs-in-shiny)
- COOL! [Essential Shiny packages](https://divadnojnarg.github.io/blog/bestofshiny/). October 2017 · 5 minute read
- [ijlyttle/bsplus](https://github.com/ijlyttle/bsplus). Shiny and R Markdown addons to Bootstrap 3 http://ijlyttle.github.io/bsplus/
- [RODBC odbcDriverConnect() Connection Error](https://stackoverflow.com/questions/15420999/rodbc-odbcdriverconnect-connection-error)



# 10.04.2018
## R
- [Dissecting R Package “Utility Belts”](https://rud.is/b/2018/04/08/dissecting-r-package-utility-belts/)
- [ANOMALIZE: TIDY ANOMALY DETECTION](http://www.business-science.io/code-tools/2018/04/08/introducing-anomalize.html)
- [magrittr and wrapr Pipes in R, an Examination](http://www.win-vector.com/blog/2018/04/magrittr-and-wrapr-pipes-in-r-an-examination/)
- [Writing better R functions part one -- April 6, 2018](https://ibecav.github.io/betterfunctions/)
- [How to use dplyr's mutate in R without a vectorized function](https://deanattali.com/blog/mutate-non-vectorized/)
- [A New Package (hhi) for Quick Calculation of Herfindahl-Hirschman Index scores](https://r-posts.com/a-new-package-hhi-for-calculation-of-herfindahl-hirschman-index-scores/)
- [How to visualize data with Highcharter: exercises](https://www.r-exercises.com/2018/04/09/how-to-visualize-data-with-highcharter-exercises/)
- [dplyr. Adding a new SQL backend (перевод)](http://biostat-r.blogspot.ru/2015/08/dplyr-dplyr.html)
- [A dummy DBI connector that simulates ANSI-SQL compliance](https://dbi.r-dbi.org/reference/ansi). `ANSI()`
- [dplyr backend for any DBI-compatible database — src_dbi • dbplyr](http://dbplyr.tidyverse.org/reference/src_dbi.html)
- [Квантиль - что это?](http://www.reshim.su/blog/kvantil/2015-09-09-626)

# 09.04.2018
## R
- R & SQL exploits
	- [Exploits of a Mom](https://xkcd.com/327/)
	- `dplyr::sql_escape_string(NULL, "s');")`

# 06.04.2018
## R
- [Appsilon/shiny.collections](https://github.com/Appsilon/shiny.collections). shiny.collections adds persistent reactive collections that can be effortlessly integrated with components like Shiny inputs, DT::dataTable or rhandsontable. The package makes it easy to build collaborative Shiny applications with persistent data.
- [My Data Science Tool Box](http://people.fas.harvard.edu/~izahn/posts/my-toolbox/), Ista Zahn 2018-04-03 14:00 Source
- [UserR! 2017 Brussel](https://user2017.brussels. масса интересных докладов. в т.ч. и по применению shiny для массового коммерческого применения
	- [Доклады](https://user2017.brussels/schedule)
	- [Видеозапись](https://channel9.msdn.com/Events/useR-international-R-User-conferences/useR-International-R-User-2017-Conference)
- [Daff: diff, patch and merge for data.frames](https://cran.r-project.org/web/packages/daff/)
daff is an R package that can find difference in values between data.frames, store this difference, render it and apply this difference to patch a data.frame. It can also merge two versions of a data.frame having a common parent. It wraps the daff.js library using the V8 package.
- [compareDF](https://cran.r-project.org/web/packages/compareDF/index.html): Do a Git Style Diff of the Rows Between Two Dataframes with Similar Structure

## Forecast
- [Is Prophet Really Better than ARIMA for Forecasting Time Series Data?](https://blog.exploratory.io/is-prophet-better-than-arima-for-forecasting-time-series-fa9ae08a5851)
- [Imputing missing values using ARIMA model](https://stackoverflow.com/questions/30584423/imputing-missing-values-using-arima-model)
- [Tutorial on 5 Powerful R Packages used for imputing missing values](https://www.analyticsvidhya.com/blog/2016/03/tutorial-powerful-packages-imputing-missing-values/)
- [A brief history of time series forecasting competitions](https://robjhyndman.com/hyndsight/forecasting-competitions/)

# 04.04.2018
## R
- [5 Most Practically Useful Window (Table) Calculations in R - Exploratory](https://blog.exploratory.io/5-most-practically-useful-window-table-calculations-in-r-7e2c7ca431d9)
- [Roll apply to return moving average](https://stackoverflow.com/questions/32614554/roll-apply-to-return-moving-average)
- [kevinushey/RcppRoll](https://github.com/kevinushey/RcppRoll). Fast rolling functions through Rcpp
- Отвечает Dirk Eddelbuettel. [Number of months between two dates](https://stackoverflow.com/questions/1995933/number-of-months-between-two-dates/1996404)
- Продолжение: [Get the difference between dates in terms of weeks, months, quarters, and years](https://stackoverflow.com/questions/14454476/get-the-difference-between-dates-in-terms-of-weeks-months-quarters-and-years)
- [R: Filtering by two columns using “is not equal” operator dplyr/subset](https://stackoverflow.com/questions/47191727/r-filtering-by-two-columns-using-is-not-equal-operator-dplyr-subset)
- COOL! non standard evaluation [What is tidy eval and why should I care?](https://www.mango-solutions.com/blog/what-is-tidy-eval-and-why-should-i-care)

# 03.04.2018
## R
- COOL! Чем занято пространство диска (treemap)? [Compute/Visualize Drive Space Consumption of Your Installed R Packages](https://rud.is/b/2018/04/01/compute-visualize-drive-space-consumption-of-your-installed-r-packages/)
- [RStudio GPU Workstations in the Cloud with Paperspace](https://tensorflow.rstudio.com/blog/rstudio-gpu-paperspace.html)
- [oneliner - a new style guide for styler](https://lorenzwalthert.github.io/oneliner/)
- COOL! [Bump Chart. Track performance over time](https://dominikkoch.github.io/Bump-Chart/)
- COOL! [Flexible equality comparison for data frames](http://dplyr.tidyverse.org/reference/all_equal.html). You can use `all_equal()` with any data frame, and `dplyr` also provides `tbl_df` methods for `all.equal()`.

# 02.04.2018
## R
- tidyeval. Пытаюсь использовать в dplyr значение переменной из внешнего окружения. Понятно, что если такой переменной нет в data.frame, то автоматом уйдем выше. Но, тем не менее:
	- [Use variable names in functions of dplyr](https://stackoverflow.com/questions/24569154/use-variable-names-in-functions-of-dplyr). In the devel version of dplyr and soon to be released as 0.6.0 (April 2017), we can create the variables as quoted and then unquote (`UQ` or `!!`) for evaluation. Из документации 2018 г. следует: "`UQ()` and `UQS()` were soft-deprecated in rlang 0.2.0 in order to make the syntax of quasiquotation more consistent. The prefix forms are now `!!`() and `!!!`() which is consistent with other R operators (e.g. `+`(a, b) is the prefix form of a + b)."

# 30.03.2018
## R
- [LEARN TO R BLOG SERIES - R AND RSTUDIO](https://itsalocke.com/blog/learn-to-r-blog-series---r-and-rstudio/)
- [Cats are great and so is the forcats R package](https://sw23993.wordpress.com/2018/03/28/cats-are-great-and-so-is-the-forcats-r-package/)
- COOL! [DT 0.4: Editing Tables, Smart Filtering, and More](https://blog.rstudio.com/2018/03/29/dt-0-4/)
- [BotRNot: An R app to detect Twitter bots](http://blog.revolutionanalytics.com/2018/03/twitter-bot-or-not.html)
- COOL! [Feb 2018: "Top 40" New Package Picks](https://rviews.rstudio.com/2018/03/29/feb-2018-top-40-new-package-picks/)
	- [geozoning: Zoning Methods for Spatial Data](https://cran.r-project.org/web/packages/geozoning/index.html)
	- [NetLogoR: A Port of 'NetLogo' Functions and Language to R](https://cran.r-project.org/web/packages/NetLogoR/index.html). Easily create agent-based models in R following the 'NetLogo' framework (Wilensky, 1999; <http://ccl.northwestern.edu/netlogo/>).
	- [riskyr: Rendering Risk Literacy more Transparent](https://cran.r-project.org/web/packages/riskyr/index.html)
Risk-related information can be expressed in terms of probabilities or frequencies. By providing a toolbox of methods and metrics, we compute, translate, and represent risk-related information in a variety of ways. By offering different, but complementary perspectives on the interplay between key parameters, 'riskyr' renders teaching and training of risk literacy more transparent. [riskyr User Guide](https://cran.r-project.org/web/packages/riskyr/vignettes/A_user_guide.html)
	- [knitrProgressBar: Provides Progress Bars in 'knitr'](https://cran.r-project.org/web/packages/knitrProgressBar/index.html)
Provides a progress bar similar to 'dplyr' that can write progress out to a variety of locations, including stdout(), stderr(), or from file(). Useful when using 'knitr' or 'rmarkdown', and you still want to see progress of calculations in the terminal.
	- [trackr: Semantic Annotation and Discoverability System for R-Based Artifacts](https://cran.r-project.org/web/packages/trackr/index.html)
Automatically annotates R-based artifacts with relevant descriptive and provenance-related and provides a backend-agnostic storage and discoverability system for organizing, retrieving, and interrogating such artifacts.

## R & Excel
- [ДАТАЗНАЧ (функция ДАТАЗНАЧ)](https://support.office.com/ru-ru/article/%D0%94%D0%90%D0%A2%D0%90%D0%97%D0%9D%D0%90%D0%A7-%D1%84%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D1%8F-%D0%94%D0%90%D0%A2%D0%90%D0%97%D0%9D%D0%90%D0%A7-df8b07d4-7761-4a93-bc33-b7471bbff252)
- [Date Formats in R](https://www.r-bloggers.com/date-formats-in-r/). If you are importing data from Excel, you may have dates that are in a numeric format. We can still use as.Date to import these, we simply need to know the origin date that Excel starts counting from, and provide that to as.Date.
For Excel on Windows, the origin date is December 30, 1899 for dates after 1900. (Excel’s designer thought 1900 was a leap year, but it was not.) For Excel on Mac, the origin date is January 1, 1904.
- [tidyxl: Read Untidy Excel Files](https://github.com/nacnudus/tidyxl).
Imports non-tabular from Excel files into R. Exposes cell content, position and formatting in a tidy structure for further manipulation. Tokenizes Excel formulas. Supports '.xlsx' and '.xlsm' via the embedded 'RapidXML' C++ library <http://rapidxml.sourceforge.net>. Does not support '.xlsb' or '.xls'.

# 29.03.2018
## R
- COOL! [Quoting version of c() array concatinator](https://winvector.github.io/wrapr/reference/qc.html)
- COOL! [Test Driven Development in R](https://rpubs.com/pparacch/278724) by Pier Lorenzo Paracchini, 18 mai, 2017
- [HOW I LEARNED TO STOP WORRYING AND LOVE R CMD CHECK](https://juliasilge.com/blog/how-i-stopped/)
- knitr:
	- [R knitr markown: Setting HTML page width](https://stackoverflow.com/questions/28480625/r-knitr-markown-setting-html-page-width)
	- [Long lines of text output](https://yihui.name/knitr/demo/output/). Normally R respects the option width (set via `options(width = ??)`) when printing text output, e.g. rnorm(100). The default value for width is set to 75
	- [R console width for output #764 {Closed}](https://github.com/yihui/knitr/issues/764). I have added the new chunk option `R.options`. Thanks!
	- [# a list of options attributes for RStudio](https://github.com/yihui/knitr/blob/master/R/defaults.R)
- Полезно [How to suppress warnings globally in an R Script](https://stackoverflow.com/questions/16194212/how-to-suppress-warnings-globally-in-an-r-script). `suppressWarnings(expr)`
- [HOW TO PLAY WITH ATTRIBUTES IN R](http://www.dummies.com/programming/r/how-to-play-with-attributes-in-r/)


# 27.03.2018
## R
- Формулы в R Markdown. [An Example R Markdown](http://www.statpower.net/Content/310/R%20Stuff/SampleMarkdown.html).
	- [Equation Examples in R Markdown](http://www.montana.edu/rotella/documents/502/MarkdownEqnExamples.Rmd)
- [Power analysis for longitudinal multilevel models: powerlmm 0.2.0 is now out on CRAN](http://rpsychologist.com/powerlmm-0-2-0)
- COOL! Интересный разбор фич ggplot. [ggplot2: How Geoms & Aesthetics ≈ Whipped Cream](https://trinkerrstuff.wordpress.com/2018/03/21/ggplot2-how-geoms-aesthetics-%E2%89%88-whipped-cream/)
- [Regression Analysis Essentials For Machine Learning](http://www.sthda.com/english/wiki/regression-analysis-essentials-for-machine-learning)
- [15 TYPES OF REGRESSION YOU SHOULD KNOW](https://www.listendata.com/2018/03/regression-analysis.html)
- [Machine Learning Modelling in R :: Cheat Sheet](http://www.thertrader.com/2018/03/22/machine-learning-modelling-in-r-cheat-sheet/)
- [Should I learn sf or sp for spatial R programming?](http://www.seascapemodels.org/rstats/2018/03/23/should-I-learn-sp-or-sf.html)
- COOL! Очень интересное объяснение математики на примере R. [Exploring the underlying theory of the chi-square test through simulation - part 2](https://www.rdatagen.net/post/a-little-intuition-and-simulation-behind-the-chi-square-test-of-independence-part-2/)
- [SHINYPROXY 1.1.0 RELEASED!](https://www.openanalytics.eu/blog/2018/03/25/shinyproxy-1.1.0/)
- [R package for M4 Forecasting Competition](https://robjhyndman.com/hyndsight/m4comp2018/)
- [reticulate: R interface to Python](https://blog.rstudio.com/2018/03/26/reticulate-r-interface-to-python/)
- [Guide to tidy git analysis](https://drsimonj.svbtle.com/embarking-on-a-tidy-git-analysis)
- [remoter: Remote R: Control a Remote R Session from a Local One](https://cran.r-project.org/web/packages/remoter/index.html)
- [Automate R processes](http://www.bnosac.be/index.php/blog/76-automate-r-processes)
- plumber: [Cannot POST in UTF-8 under windows #153 {Open}](https://github.com/trestletech/plumber/issues/153)
- [RUN PYTHON FROM R](https://www.listendata.com/2018/03/run-python-from-r.html)
- [Generate image captions with the Computer Vision API](http://blog.revolutionanalytics.com/2018/03/computer-vision-api.html)
- [Discriminant Analysis: Statistics All The Way](https://r-posts.com/discriminant-analysis-statistics-all-the-way/)

## R nub
- [Using R to ‘drive’ MS Excel -- 3/27/2018](https://ibecav.github.io/RtoExcel/)
- [Using functions to be more efficient – March 28, 2018](https://ibecav.github.io/Functionalize/)


## Microsoft
- [The olapR library](https://docs.microsoft.com/en-us/machine-learning-server/r-reference/olapr/olapr) provides R functions for importing data from OLAP cubes stored in SQL Server Analysis Services into a data frame. This package is available on premises, on Windows only.
- [Установка Microsoft ODBC Driver for SQL Server на Linux и macOS](https://docs.microsoft.com/ru-ru/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server)
- [Драйвер Microsoft ODBC для SQL Server в Windows](https://docs.microsoft.com/ru-ru/sql/connect/odbc/windows/microsoft-odbc-driver-for-sql-server-on-windows)
- [Run a (R) script as a service {server 2012R2}](https://serverfault.com/questions/867549/run-a-r-script-as-a-service-server-2012r2)
- [ASStoredProcedures. Analysis Services Stored Procedure Project](https://archive.codeplex.com/?p=asstoredprocedures)
- [<запрос источника данных> -OPENROWSET](https://docs.microsoft.com/ru-ru/sql/dmx/source-data-query-openrowset)
- [Отличие DAX и MDX](https://habrahabr.ru/post/341478/)


# 21.03.2018
## R
- [R and Docker](http://blog.revolutionanalytics.com/2018/03/r-and-docker.html)
- [The Rocker Project. Docker Containers for the R Environment](https://www.rocker-project.org/)
- Тащим вебкасты с RStudio. [Tube Ninja](https://www.tubeninja.net/)
- COOL! [Some shinyjs functions not working in shiny module #50 {Closed}](https://github.com/daattali/shinyjs/issues/50)

# 20.03.2018
## R
- [How to create file execute mode permissions in Git on Windows?](https://stackoverflow.com/questions/21691202/how-to-create-file-execute-mode-permissions-in-git-on-windows)
- [`theme_ipsum_ps`: A precise & pristine ggplot2 theme with opinionated defaults...](https://rdrr.io/github/hrbrmstr/hrbrthemes/man/theme_ipsum_ps.html)
- [hrbrthemes : Additional Themes and Theme Components for ‘ggplot2’](https://github.com/hrbrmstr/hrbrthemes)
- [New IBM Plex Sans Support in hrbrthemes + Automating Axis Text Justification](https://rud.is/b/2017/11/16/new-ibm-plex-sans-support-in-hrbrthemes-automating-axis-text-justification/)
- [The package of IBM’s typeface, IBM Plex.](https://github.com/IBM/plex)
- [IBM Plex. Font Squirrel](https://www.fontsquirrel.com/fonts/ibm-plex)

# 17.03.2018
## R
- [Take Care If Trying the RPostgres Package](http://www.win-vector.com/blog/2018/03/take-care-if-trying-the-rpostgres-package/)
- Полезный вводный материал. [Getting Started with tidyverse in R](http://www.storybench.org/getting-started-with-tidyverse-in-r/)
- [Cleaning Big Data: Most Time-Consuming, Least Enjoyable Data Science Task, Survey Says](https://www.forbes.com/sites/gilpress/2016/03/23/data-preparation-most-time-consuming-least-enjoyable-data-science-task-survey-says/#5b01407a6f63)
- [ClickTail Introduction](https://www.altinity.com/blog/2018/3/12/clicktail-introduction)


# 16.03.2018
## R
- [Phaedra is an open source platform for data capture and analysis of high-content screening data.](https://www.phaedra.io/)
- COOL! [Empty R environment becomes large file when saved](https://stackoverflow.com/questions/13912867/empty-r-environment-becomes-large-file-when-saved)

# 15.03.2018
## R
- [DataExplorer: Fast Data Exploration With Minimum Code](http://blog.revolutionanalytics.com/2018/02/dataexplorer.html)
- [Math Notation for R Plot Titles: expression and bquote](https://trinkerrstuff.wordpress.com/2018/03/15/2246/)

# 14.03.2018
## R
- COOL! [Alternative Design for Shiny](https://rviews.rstudio.com/2018/03/13/alternative-design-for-shiny/)
- COOL! [Excel is obsolete. Here are the Top 2 alternatives from R and Python](https://appsilondatascience.com/blog/rstats/2018/03/13/excel-is-obsolete.html)
- [An Ode to Testing, my first review](https://ropensci.org/blog/2018/03/13/ode-to-testing/)
- [The RedMonk Programming Language Rankings: January 2018](http://redmonk.com/sogrady/2018/03/07/language-rankings-1-18/)
- [Effortlessly Read Rectangular Data: R Package `readit` 1.0.0 Released on CRAN](https://anotherblogaboutr.blogspot.ru/2018/03/effortlessly-read-rectangular-data-r.html)
- COOL! [Material design in Shiny apps](https://ericrayanderson.github.io/shinymaterial/)
- Decision Trees
	- [Estimating Decision Tree Models](https://docs.microsoft.com/en-us/machine-learning-server/r/how-to-revoscaler-decision-tree)
	- [Draw nicer Classification and Regression Trees with the rpart.plot package](http://blog.revolutionanalytics.com/2013/06/plotting-classification-and-regression-trees-with-plotrpart.html)
	- [Visualizing C5.0 Decision Tree? {closed}](https://stats.stackexchange.com/questions/198134/visualizing-c5-0-decision-tree)
	- [R Decision Trees – A Tutorial to Tree Based Modeling in R](https://data-flair.training/blogs/r-decision-trees/)
	- [How to edit the rule sets of decision tree in R](https://gisday.wordpress.com/2014/06/06/how-to-edit-the-rule-sets-of-decision-tree-in-r/)
- COOL! [Inconsistent parsing failure "no trailing characters e3" #645 {Closed}](https://github.com/tidyverse/readr/issues/645)
- [How to fork/parallelize process in `purrr::pmap`](https://stackoverflow.com/questions/47552930/how-to-fork-parallelize-process-in-purrrpmap)
- [Rstudio addin to help you with your regexes (in progress)](https://github.com/gadenbuie/regexplain)
	- [RegExplain](https://www.garrickadenbuie.com/project/regexplain/) is an RStudio addin slash utility belt for regular expressions. Interactively build your regexp, check the output of common string matching functions, consult the interactive help pages, or use the included resources to learn regular expressions. And more.
- [RStudio:addins part 5 - Profile your code on keypress in the background, with no dependencies.](https://jozefhajnala.gitlab.io/r/r105-async-profiler/)
- `lubridate::now()` > 1.7.0 падает без указание tzone:
	- [How to change the default time zone in R?](https://stackoverflow.com/questions/6374874/how-to-change-the-default-time-zone-in-r). See `?timezone`. Another way to do it, without changing the whole computer time is using the setenv command like this: `Sys.setenv(TZ='GMT')`. После переезда на гугловые библиотеки необходимо добавлять в код установку переменных (либо делать это в системе): `Sys.setenv(TZ="Europe/Moscow")`

## R по мотивам Сибинтека
- COOL! GIS [Visualising your hiking trails and photos with My Tracks, R and Leaflet](http://mhermans.net/hiking-gpx-r-leaflet.html)
- EXIF:
	- [exifr: EXIF Image Data in R](https://cran.r-project.org/web/packages/exifr/)
	- [Read and Write 'Exif' Image/Media Tags with R](https://github.com/hrbrmstr/exiv)
- COOL! [Gantt chart using R](https://davetang.org/muse/2017/02/03/gantt-chart-using-r/)
- [Adding Curved Flight path using R's Leaflet Package](https://stackoverflow.com/questions/34499212/adding-curved-flight-path-using-rs-leaflet-package)
- [Strava маршутры на leaflet](http://www.wolferonline.de/uploads/llmap.positr.html)



# 13.03.2018
## R
- [Tidy Resampling Redux with Agricultural Economics Data](http://appliedpredictivemodeling.com/blog/2018/3/12/2s3j82ctkrhxugq7hf3myoeeb49k8u)
- [Exploratory Analysis – When to Choose R, Python, Tableau or a Combination](https://www.stoltzmaniac.com/tool-selection-python-tableau-r/)
- COOL! [Shiny slider examples with the intrval R package](http://peter.solymos.org/code/2018/03/08/shiny-slider-examples-with-the-intrval-r-package.html)

# 12.03.2018
## R
- [An introduction to styler](http://styler.r-lib.org/articles/introducing_styler.html) by Lorenz Walthert, 2018-03-09
- [styler 1.0.1](https://lorenzwalthert.github.io/stylerpost2/) is now awailable on CRAN. It’s mainly a maintenance release and contains bug fixes and speed improvements.
- [lime v0.4: The kitten picture edition](https://tensorflow.rstudio.com/blog/lime-v0.4-the-kitten-picture-edition.html)
- [R: simple for complex tasks, complex for simple tasks](https://ekonometrics.blogspot.ru/2018/03/r-simple-for-complex-tasks-complex-for.html)
- [Compare outlier detection methods with the OutliersO3 package](http://blog.revolutionanalytics.com/2018/03/outliers.html)
- useR! 2017 [When is an Outlier an Outlier? The O3 plot](https://channel9.msdn.com/Events/useR-international-R-User-conferences/useR-International-R-User-2017-Conference/When-is-an-Outlier-an-Outlier-The-O3-plot)
- [Find duplicated elements with dplyr](https://stackoverflow.com/questions/28244123/find-duplicated-elements-with-dplyr)
- Shiny tweaks
	- COOL! [SOME TOOLS FOR WRITING SHINY APPS](http://skranz.github.io//r/2018/03/08/Tools_for_Writing_Shiny_Apps.html)
	- [shinyEvents](https://github.com/skranz/shinyEvents). Use shiny with event handlers instead of reactivity
	- [Shiny slider examples with the intrval R package](http://peter.solymos.org/code/2018/03/08/shiny-slider-examples-with-the-intrval-r-package.html)
- [`bind_rows()` warning with columns of unknown classes #2688 {Closed}](https://github.com/tidyverse/dplyr/issues/2688)


## SAS
- [Хочу все знать. Язык SAS](https://geekbrains.ru/posts/sas_lang)
- [Step-by-Step Programming with Base SAS® Software](https://support.sas.com/documentation/onlinedoc/91pdf/sasdoc_913/base_step_10071.pdf)


# 06.03.2018
## R
- COOL! [smoothScatter with ggplot2](https://www.inwt-statistics.com/read-blog/smoothscatter-with-ggplot2-513.html)
- [R package for controlling Minecraft via API](https://github.com/ropenscilabs/miner)
- COOL [Nice presentation about NSE and metaprogramming](https://r-oxford.github.io/slides/2018_03.pdf)
- [Mining CRAN DESCRIPTION Files](https://juliasilge.com/blog/mining-cran-description/) by Julia Silge
	- [JC and the Vignettes](https://jcarroll.com.au/2018/03/06/jc-and-the-vignettes/)
- COOL! [Tao of Tidygraph](http://www.questionflow.org/2018/03/06/tao-of-tidygraph/)
- [Using R in SQL Server Reporting Services (SSRS)](https://tomaztsql.wordpress.com/2018/03/04/using-r-in-sql-server-reporting-services-ssrs/)
- [Another reason to be careful about what you control for](https://www.rdatagen.net/post/another-reason-to-be-careful-about-what-you-control-for/)
- COOL! [Implementing DT Reload within Shiny #168 {Closed}](https://github.com/rstudio/DT/issues/168)


# 05.03.2018
## R
- COOL! [covr](https://github.com/r-lib/covr). Test coverage reports for R
- COOL! [How to add code coverage (codecov) to your R package?](https://walczak.org/2017/06/how-to-add-code-coverage-codecov-to-your-r-package/)

- COOL! Python. [dplyr-style Data Manipulation with Pipes in Python](https://towardsdatascience.com/dplyr-style-data-manipulation-with-pipes-in-python-380dcb137000)
- COOL! [Generating codebooks in R](http://sandsynligvis.dk/articles/18/codebook.html). A codebook is a technical document that provides an overview of and information about the variables in a dataset.
- [Getting {sparklyr}, {h2o}, {rsparkling} to work together and some fun with bash](http://www.brodrigues.co/blog/2018-03-03-sparklyr_h2o_rsparkling/)
- [How To Learn R, Part 1: Learn From A Master Data Scientist's Code](http://www.business-science.io/learning-r/2018/03/03/how_to_learn_R_pt1.html)
- [hrbrpkgs: list Bob Rudis' packages](http://www.masalmon.eu/2018/03/04/hrbrpkgs/)
- [Exercise dashboard](http://www.nathanchaney.com/2018/03/04/exercise-dashboard/)

# R tidyverse
- [R: Names and Symbols](https://stat.ethz.ch/R-manual/R-devel/library/base/html/name.html). A ‘name’ (also known as a ‘symbol’) is a way to refer to R objects by name (rather than the value of the object, if any, bound to that name).

# 02.03.2018
## R
- COOL! [Annotating phylogenetic tree with images using ggtree and ggimage](https://guangchuangyu.github.io/2018/03/annotating-phylogenetic-tree-with-images-using-ggtree-and-ggimage/)
- COOL! [Craft httr calls cleverly with curlconverter](https://rud.is/b/2016/02/10/craft-httr-calls-cleverly-with-curlconverter/)
- COOL! [pillar. part of the tidyverse](pillar provides tools for styling columns of data, artfully using colour and unicode characters to guide the eye.)
- [Using mutate_at() with negated select helpers e.g (not `one_of()`)](https://stackoverflow.com/questions/45875697/using-mutate-at-with-negated-select-helpers-e-gnot-one-of)

# 01.03.2018
## R
- COOL! [Criminal goings-on in a random forest](https://thinkr.biz/2018/03/01/crime-random-forest/)
- [#17: Dependencies](http://dirk.eddelbuettel.com/blog/2018/02/28/#017_dependencies). February 28, 2018, By Thinking inside the box
- COOL!! [Faster way to trim a long character vector in R {closed}](https://stackoverflow.com/questions/39152317/faster-way-to-trim-a-long-character-vector-in-r). !!! **It's just that `strtrim()` is fairly slow.** Answer: Use `(substr(x, 1, 3))`


# 28.02.2018
## R
- [Parallel Processing Baseball Data with R and mlbgameday](http://www.datascienceriot.com//r/mlbgameday-basics/)
- [Effective data analytics in Manufacturing](https://www.mango-solutions.com/blog/effective-data-analytics-in-manufacturing)

## R & SAP
- [Working with R integration in HANA 2.0 SPS02](https://blogs.sap.com/2017/09/18/working-with-r-integration-in-hana-2.0-sps02/)
- [R Integration with SAP HANA](https://blogs.sap.com/2016/12/23/r-integration-with-sap-hana/)
- [SAP NW RFC connector for R](https://github.com/piersharding/RSAP)

# 27.02.2018
## R
- [Installing Package Dependencies without external http(s) requests](http://www.peteredewitt.com/2018/installing-dependencies/)
- COOL! [qdap: Bridging the Gap Between Qualitative Data and Quantitative Analysis](https://cran.r-project.org/web/packages/qdap/index.html). Весьма интересный пакет. Я нашел в сопутствующем пакете [`qdapTools`](http://trinker.github.io/qdapTools/) функцию `list2df`
- А вот еще более классный ответ Хадли: [turning a named list into a dataframe using dplyr](https://gist.github.com/aammd/9ae2f5cce9afd799bafb)
```
list_to_df <- function(listfordf){
  if(!is.list(named.list)) stop("it should be a list")

  df <- list(list.element = listfordf)
  class(df) <- c("tbl_df", "data.frame")
  attr(df, "row.names") <- .set_row_names(length(listfordf))

  if (!is.null(names(listfordf))) {
    df$name <- names(listfordf)
  }

  df
}
```
- А в пакете `tibble` для этого есть функция `enframe`
- [R: removing NULL elements from a list](https://stackoverflow.com/questions/33004238/r-removing-null-elements-from-a-list)
- [Creating corporate colour palettes for ggplot2](https://drsimonj.svbtle.com/creating-corporate-colour-palettes-for-ggplot2)
- Shiny async. [Promises with async shiny on shiny server open source](https://community.rstudio.com/t/promises-with-async-shiny-on-shiny-server-open-source/5076). Found an answer on my own! Thankfully it does work on open source! The issue was with ubuntu and the httpuv package, which needs to be updated with a special linux dependency [before installing the async shiny dev package from github](https://github.com/beakerbrowser/beaker/issues/54).


# 26.02.2018
## R
- [MLE in R](https://statcompute.wordpress.com/2018/02/25/mle-in-r/). When I learned and experimented a new model, I always like to start with its likelihood function in order to gain a better understanding about the statistical nature. That’s why I extensively used the SAS/NLMIXED procedure that gives me more flexibility.
- [How to set up a sparklyr cluster in 5 minutes](http://blog.revolutionanalytics.com/2018/02/aztk-sparklyr.html). You can get up and running in about 5 minutes using the guide SparklyR on Azure with AZTK, and you don't even have to install anything yourself.
- [Edinbr: Text Mining with R](https://blog.jumpingrivers.com/posts/2018/tidytext_edinbr_2018/)
- [Is R base::subset() really that bad?](http://www.win-vector.com/blog/2018/02/is-r-basesubset-really-that-bad/)
- COOL! [My Early Career Crisis (2014 - 2015), Yihui Xie / 2018-02-16](https://yihui.name/en/2018/02/career-crisis/). A painful transition of a fresh PhD from academia to industry, and from selfish open-source to product-oriented open-source
- [R's S3 generic-function object-oriented system](https://jasdumas.github.io/2018-02-23-s3-generic-function-oo/)
- Survival. [An introduction to joint modeling in R](https://talesofr.wordpress.com/2018/02/23/an-introduction-to-joint-modeling-in-r/)
- COOL! [Analyzing accelerometer data with R](http://blog.revolutionanalytics.com/2018/02/accelerometers.html). Исходник здесь: [Making Magic with Keras and Shiny. An exploration of Shiny’s position in the data science pipeline](http://nickstrayer.me/dataDayTexas/#1)
- [Whys and Hows of Apply Family of Functions in R. Introduction to Looping system](https://r-posts.com/whys-and-hows-of-apply-family-of-functions-in-r/)
- [Minimal, Explicit, Python Style Package Loading for R](https://trinkerrstuff.wordpress.com/2018/02/22/minimal-explicit-python-style-package-loading-for-r/)
- COOL! [Jan 2018: "Top 40" New Package Picks](https://rviews.rstudio.com/2018/02/22/jan-2018-top-40-new-package-picks/)
- [TSstudio v0.1.1](https://cran.rstudio.com/web/packages/TSstudio/vignettes/TSstudio_Intro.html): Provides a set of interactive visualization tools for time series analysis supporting ts, mts, zoo and xts objects including visualization functions for forecasting model performance (forecasted vs. actual), time series interactive plots (single and multiple series), and seasonality plots.
	- [Introduction for the TSstudio Package](https://cran.rstudio.com/web/packages/TSstudio/vignettes/TSstudio_Intro.html)
- COOL! [Combine your hex stickers with magic(k)](http://www.masalmon.eu/2018/02/22/hexcombine/)


# 23.02.2018
## R
- [R Lists](https://www.datamentor.io/r-programming/list)
In this article, you will learn to work with lists in R programming. You will learn to create, access, modify and delete list components.
- [R dyplr: Get index of column by its name](https://stackoverflow.com/questions/35768451/r-dyplr-get-index-of-column-by-its-name/35768651)
- COOL! [How would I hide the action button until all selections are made?](https://stackoverflow.com/questions/23893756/how-would-i-hide-the-action-button-until-all-selections-are-made)


# 21.02.2018
## R
- COOL! [callr package](). Call R from R. It is sometimes useful to perform a computation in a separate R process, without affecting the current R process at all. This packages does exactly that.
- [Blog about something you just learned](https://edwinth.github.io/blog-new-things/)
- COOL! [webmockr: mock HTTP requests](https://ropensci.org/technotes/2018/02/20/webmockr-intro/)
- [Deep Learning Image Classification with Keras and Shiny](https://jasdumas.github.io/2018-02-20-deep-learning-img-classifier/)
- [Speeding up spatial analyses by integrating `sf` and `data.table`: a test case](https://lbusettspatialr.blogspot.ru/2018/02/speeding-up-spatial-analyses-by.html)
- [MARKDOWN BASED WEB ANALYTICS? RECTANGLE YOUR BLOG](https://itsalocke.com/blog/markdown-based-web-analytics-rectangle-your-blog/)

- [How do I transpose a tibble() in R](https://stackoverflow.com/questions/42790219/how-do-i-transpose-a-tibble-in-r)
- [How to find out which package version is loaded in R?](https://stackoverflow.com/questions/11103189/how-to-find-out-which-package-version-is-loaded-in-r) `packageVersion("snow")`
- [R: use magrittr pipe operator in self written package](https://stackoverflow.com/questions/27947344/r-use-magrittr-pipe-operator-in-self-written-package)


# 20.02.2018
## R
- [DALEX: understand a black box model – conditional responses for a single variable](http://smarterpoland.pl/index.php/2018/02/dalex-conditional-single-variable-response-of-your-black-box-model/)
- [DALEX: how would you explain this prediction?](http://smarterpoland.pl/index.php/2018/02/dalex-which-variables-influence-this-single-prediction/)
- [DALEX website](https://pbiecek.github.io/DALEX/)
- COOL! [imputeTS: Time Series Missing Value Imputation](https://github.com/SteffenMoritz/imputeTS/blob/master/README.md)
The imputeTS package specializes on (univariate) time series imputation. It offers several different imputation algorithm implementations. Beyond the imputation algorithms the package also provides plotting and printing functions of time series missing data statistics. Additionally three time series datasets for imputation experiments are included.
- COOL! [RestRserve](http://dsnotes.com/RestRserve/) is an R web API framework for building high-performance microservices and app backends. The main difference to other frameworks (plumber, jug) is that it is parallel by design (thanks to Rserve).
YES - it means it will handle all the incomming requests in parallel - each request in a separate fork.
- [Integrating R with production systems using an HTTP API](http://blog.revolutionanalytics.com/2014/08/using-r-inside-the-enterprise-integration-with-existing-systems.html). August 19, 2014. читаю тут в интернетах какие best practice для деплоя микросервисов с R-бэкэндом. Все такие plumber, opencpu и тд отдыхают. Ниболее production-ready это Rserve + http сервер на ваш вкус.
- COOL! bit64 package
- [R package: future: Unified Parallel and Distributed Processing in R for Everyone](https://github.com/HenrikBengtsson/future)
- COOL! [A guide to parallelism in R](https://privefl.github.io/blog/a-guide-to-parallelism-in-r/)
- [An example of how to use the new R promises package](https://appsilondatascience.com/blog/rstats/2017/11/01/r-promises-hands-on.html)
- [A Future for R: Slides from useR 2016](https://www.jottr.org/2016/07/02/future-user2016-slides/)

# 19.02.2018
## R
- [Use unique() instead of levels() to find the possible values of a factor in R](https://chemicalstatistician.wordpress.com/2018/03/10/use-unique-instead-of-levels-to-find-the-possible-values-of-a-character-variable-in-r/)
- [R tip: Make Your Results Clear with sigr](http://www.win-vector.com/blog/2018/11/r-tip-make-your-results-clear-with-sigr/)
- [R Tip: Think in Terms of Values](http://www.win-vector.com/blog/2018/04/r-tip-think-in-terms-of-values/)
- [R Tip: Use Named Vectors to Re-Map Values](http://www.win-vector.com/blog/2018/03/r-tip-use-named-vectors-to-re-map-values/)
- [R Tip: Use let() to Re-Map Names](http://www.win-vector.com/blog/2018/03/r-tip-use-let-to-re-map-names/)
- [R Tip: Break up Function Nesting for Legibility](http://www.win-vector.com/blog/2018/03/r-tip-break-up-function-nesting-for-legibility/)
- [R Tip: Use stringsAsFactors = FALSE](http://www.win-vector.com/blog/2018/03/r-tip-use-stringsasfactors-false/)
- [R Tip: Use vector(mode = "list") to Pre-Allocate Lists](http://www.win-vector.com/blog/2018/03/r-tip-use-vectormode-list-to-pre-allocate-lists/)
- [R Tip: Get Out of the Habit of Calling View() Directly](http://www.win-vector.com/blog/2018/03/r-tip-get-out-of-the-habit-of-calling-view-directly/)
- [R Tip: Make Arguments Explicit in magrittr/dplyr Pipelines](http://www.win-vector.com/blog/2018/03/r-tip-make-arguments-explicit-in-magrittr-dplyr-pipelines/)
- [R Tip: Use drop = FALSE with data.frames](http://www.win-vector.com/blog/2018/02/r-tip-use-drop-false-with-data-frames/)
- [R Tip: Force Named Arguments](http://www.win-vector.com/blog/2018/02/r-tip-force-named-arguments/)
- [R Tip: Use `[[ ]]` Wherever You Can](http://www.win-vector.com/blog/2018/02/r-tip-use-wherever-you-can/)
- [R Tip: Use qc() For Fast Legible Quoting](http://www.win-vector.com/blog/2018/02/r-tip-use-qc-for-fast-legible-quoting/)
- [R Tip: Use seq_len() to Avoid The Backwards Sequence Bug](http://www.win-vector.com/blog/2018/02/r-tip-use-seq_len-to-avoid-the-backwards-sequence-bug/)
- [R Tip: Use Inline Operators For Legibility](http://www.win-vector.com/blog/2019/01/r-tip-use-inline-operators-for-legibility/)
- [R Tip: Use seqi() For Indexes](http://www.win-vector.com/blog/2019/01/r-tip-use-seqi-for-indexes/)
- [DPLYR, (MC)LAPPLY, FOR-LOOP AND SPEED](https://scottishsnow.wordpress.com/2018/02/18/dplyr-lapply-for-loop/)
- [R markdown blog template](http://lcolladotor.github.io/2018/02/17/r-markdown-blog-template)
- [Mix ggplot2 graphs with your favorite memes. memery 0.4.2 released.](https://blog.snap.uaf.edu/2018/02/15/mix-ggplot2-graphs-with-your-favorite-memes-memery/)
- [Packages for Getting Started with Time Series Analysis in R](https://mathewanalytics.com/2018/02/18/packages-for-getting-started-with-time-series-analysis-in-r/)

## Ubuntu
- [На разделе "boot" осталось всего 0 байт свободного места](https://raboj.su/%D0%B1%D0%BB%D0%BE%D0%B3/ubuntu/53-%D0%BD%D0%B0-%D1%80%D0%B0%D0%B7%D0%B4%D0%B5%D0%BB%D0%B5-boot-%D0%BE%D1%81%D1%82%D0%B0%D0%BB%D0%BE%D1%81%D1%8C-%D0%BC%D0%B0%D0%BB%D0%BE-%D1%81%D0%B2%D0%BE%D0%B1%D0%BE%D0%B4%D0%BD%D0%BE%D0%B3%D0%BE-%D0%BC%D0%B5%D1%81%D1%82%D0%B0.html). Для нетерпеливых, сразу лечение:
```
sudo apt-get autoremove
```

# 15.02.2018
## R
- [fastqcr: Quality Control of Sequencing Data](http://www.sthda.com/english/rpkgs/fastqcr/)
The FastQC, written by Simon Andrews at the Babraham Institute, is the most widely used sequence quality assessment tool for evaluating the raw reads from high throughput sequencing data.
- [Easily Make Multi-tabbed .xlsx Files with openxlsx](https://trinkerrstuff.wordpress.com/2018/02/14/easily-make-multi-tabbed-xlsx-files-with-openxlsx/)
- [Sentiment Analysis of 5 popular romantic comedies](https://appsilondatascience.com/blog/rstats/2018/02/14/valentines.html)

# 14.02.2018
## R
- [jamovi for R: Easy but Controversial](http://r4stats.com/2018/02/13/jamovi-for-r-easy-but-controversial/). jamovi is software that aims to simplify two aspects of using R. It offers a point-and-click graphical user interface (GUI). It also provides functions that combines the capabilities of many others, bringing a more SPSS- or SAS-like method of programming to R.
- [What does Microsoft do with R?](http://blog.revolutionanalytics.com/2018/02/what-does-microsoft-do-with-r.html)
- COOL! [shinyalert: Easily create pretty popup messages (modals) in Shiny](https://deanattali.com/blog/shinyalert-package/)
- [tfestimators - Package: Embeddings for Categorical Variables](https://flovv.github.io/Embeddings_with_tf/)
- [tidygraph 1.1 – A tidy hope](https://www.data-imaginist.com/2018/tidygraph-1-1-a-tidy-hope/). I am very pleased to tell you that the next version of tidygraph (1.1) is now available on CRAN. This is not a bug-fix release, nor a change-it-all release, but rather a more-of-it-all release, and in this post I’m going to tell you all about it.
- [«smooth» package for R. Common ground. Part IV. Exogenous variables. Advanced stuff](https://forecasting.svetunkov.ru/en/2018/02/10/smooth-package-for-r-common-ground-part-iv-exogenous-variables-advanced-stuff/)

# 12.02.2018
## R
- [Yet Another Blog in Statistical Computing. R Interfaces to Python Keras Package](https://statcompute.wordpress.com/2018/02/11/r-interfaces-to-python-keras-package/)
- COOL! [Applying a function over rows of a data frame](https://rpubs.com/wch/200398) by Winston Chang. Подробнейший разбор нескольких методов итерации по строкам.
- COOL! Как подхватывать функцию с произвольным списком переменных: [Advanced R by Hadley Wickham. chap Functions](http://adv-r.had.co.nz/Functions.html). Глава `...`. [capturing unevaluated dots](http://adv-r.had.co.nz/Computing-on-the-language.html#capturing-dots)
- COOL! [TestThat. Reference version 2.0.0](http://testthat.r-lib.org/reference/index.html)
- COOL! [rlangpart. Reference version 0.0.0.9019](http://rlang.tidyverse.org/reference/)
- [R package primer. Writing tests](http://kbroman.org/pkg_primer/pages/tests.html)
- [Printing custom diagnostic information if `testthat` test fails in `R`](https://stackoverflow.com/questions/26928253/printing-custom-diagnostic-information-if-testthat-test-fails-in-r)
- [Split uneven length vectors to columns with tidyr](https://community.rstudio.com/t/split-uneven-length-vectors-to-columns-with-tidyr/2704)
- [A new R trick ... for me at least](https://oddhypothesis.blogspot.ru/2013/08/a-new-r-trick-for-me-at-least.html)



# 09.02.2018
## R
- COOL! [DataExplorer: Fast Data Exploration With Minimum Code](http://blog.revolutionanalytics.com/2018/02/dataexplorer.html)
	- [Introduction to DataExplorer](https://cran.r-project.org/web/packages/DataExplorer/vignettes/dataexplorer-intro.html)
- COOL! [Test chunks for R Markdown](https://github.com/ropenscilabs/testrmd)
- COOL! [Intro to unit testing in R](https://katherinemwood.github.io/post/testthat/)
- При перемещении тестов в папку`./tests` команда `test_file` рушится следующим образом:
```
== Results =====================================================================
OK:       0
Failed:   2
Warnings: 1
Skipped:  0
> test_dir("./tests/")
√ | OK F W S | Context
Error in x[[method]](...) : attempt to apply non-function
```
Убрав `source` из файла, видно, что путь запуска идет от файла автотеста, а не от корня. Надо править относительные ссылки к подгружаемым файлам.

# 08.02.2018
## R
- [Data transformation in #tidyverse style: package sjmisc updated #rstats](https://strengejacke.wordpress.com/2018/02/06/data-transformation-in-tidyverse-style-package-sjmisc-updated-rstats/)
- [In case you missed it: January 2018 roundup](http://blog.revolutionanalytics.com/2018/02/in-case-you-missed-it-january-2018-roundup.html)
- [The plots thicken. Every story needs a good plot](https://thinkr.biz/2018/02/07/plots-thicken/)
	- Code. [The plots thicken. Daily Wikipedia page views of ‘Statistical Charts & Diagrams’](https://thinkr.biz/wp-content/uploads/2018/02/app.html)
- [Continuous integration for your private R projects with CircleCI](https://appsilondatascience.com/blog/rstats/2018/02/07/circleci.html)
- Hadley Wickham. [Automated checking](http://r-pkgs.had.co.nz/check.html)
- COOL! [CircleCI](https://circleci.com/). Build faster. Test more. Fail less. Automate the software development process using continuous integration and continuous delivery so you can focus on what matters: building great things, not waiting for great things to build.
- COOL! [IMSMWU/RClickhouse](https://github.com/IMSMWU/RClickhouse). A 'DBI' Interface to the Yandex Clickhouse Database Providing Basic 'dplyr' Support
- [httpuv: HTTP and WebSocket Server Library](https://cran.r-project.org/web/packages/httpuv/index.html)
- [Using future with plumber to set up asynchronous api calls](https://github.com/FvD/futureplumber)

# 07.02.2018
## R
- COOL! [Setting up a version controlled shiny-server](http://rmhogervorst.nl/cleancode/blog/2018/02/06/setting-up-a-version-controlled-shiny-server.html)
- [The prequel to the drake R package](https://ropensci.org/blog/2018/02/06/drake/)
- [An R-focused pipeline toolkit for reproducibility and high-performance computing](https://ropensci.github.io/drake)

## Python & Excel
- [Excel VBA Save Workbook: Easily Save Excel Files With These 3 Macro Examples](https://powerspreadsheets.com/vba-save-workbook/)
- [Программное копирование листа в программе Excel вызывает ошибку времени выполнения 1004](https://support.microsoft.com/ru-ru/help/210684/copying-worksheet-programmatically-causes-run-time-error-1004-in-excel)
- [Office VBA Reference Excel VBA](https://msdn.microsoft.com/vba/vba-excel)
	- [Workbooks.Open Method (Excel)](https://msdn.microsoft.com/en-us/vba/excel-vba/articles/workbooks-open-method-excel)
	- [Worksheet.Activate Method (Excel)](https://msdn.microsoft.com/en-us/vba/excel-vba/articles/worksheet-activate-method-excel)
	- [Свойство Application.ActiveSheet (Excel)](https://msdn.microsoft.com/ru-ru/vba/excel-vba/articles/application-activesheet-property-excel)
	- [Метод Workbook.SaveAs (Excel)](https://msdn.microsoft.com/ru-ru/vba/excel-vba/articles/workbook-saveas-method-excel)
	- [Workbook.BeforeSave Event (Excel)](https://msdn.microsoft.com/en-us/vba/excel-vba/articles/workbook-beforesave-event-excel)
	- [Метод Workbook.Close (Excel)](https://msdn.microsoft.com/ru-ru/vba/excel-vba/articles/workbook-close-method-excel)
- [How to enable events so Workbook_BeforeSave gets called](https://stackoverflow.com/questions/26296597/how-to-enable-events-so-workbook-beforesave-gets-called)
- [ошибка 1004 "Метод select из класса Range завершен неверно"](http://www.excel-vba.ru/forum/index.php?topic=2878.0)
- Как работать с константами win32 в python:
	- [error xlPrimary not defined in Python win32com](https://stackoverflow.com/questions/23290216/error-xlprimary-not-defined-in-python-win32com/23306850#23306850)
	- [How to use win32com.client.constants with MS Word?](https://stackoverflow.com/questions/28264548/how-to-use-win32com-client-constants-with-ms-word)
	- [Use VBA predefined constants in python win32com package](https://yiruiscool.wordpress.com/2015/03/19/use-vba-predefined-constants-in-python-win32com-package/)
	- [win32com.client.constants](http://nullege.com/codes/search/win32com.client.constants)
- COOL! [PYTHON FOR EXCEL. FREE & OPEN SOURCE](https://www.xlwings.org/)
- [pyxll=python("in excel")](https://www.pyxll.com/)
- [Creating Advanced Excel Workbooks with Python](http://pbpython.com/advanced-excel-workbooks.html)
- [Tutorial lesson using pywin32 module to handle excel by python.](https://github.com/sukuba/howto-pywin32-excel)
- [Python Excel Tutorial: The Definitive Guide](https://www.datacamp.com/community/tutorials/python-excel-tutorial)
- [How to control Excel with Python](https://kyleellefsen.com/blog/2017_10_28_python_excel/)
- [vinta/awesome-python](https://github.com/vinta/awesome-python). A curated list of awesome Python frameworks, libraries, software and resources http://awesome-python.com/
- [ПИТОНТЬЮТОР](http://pythontutor.ru/). УЧИТЕ ПИТОН. Бесплатный курс по программированию с нуля. Работает прямо в браузере.

# 06.02.2018
## map & ggplot
- [Mapping in R using the ggplot2 package](http://zevross.com/blog/2014/07/16/mapping-in-r-using-the-ggplot2-package/)
- [Making Maps with R](http://eriqande.github.io/rep-res-web/lectures/making-maps-with-R.html). Reproducible Research Course by Eric C. Anderson for (NOAA/SWFSC)
- [Mapping with R. by Andrew Ba Tran NICAR 2017](https://andrewbtran.github.io/NICAR/2017/maps/mapping-census-data.html)
- [Leaflet. Lines and Shapes](https://rstudio.github.io/leaflet/shapes.html). Leaflet makes it easy to take spatial lines and shapes from R and add them to maps.
- [Introduction to leaflet.minicharts](https://cran.r-project.org/web/packages/leaflet.minicharts/vignettes/introduction.html)
- [Making maps in R](https://cengel.github.io/rspatial/4_Mapping.nb.html) by claudia a engel. Last updated: May 17, 2017
- [Administrative regions map of a country with ggmap and ggplot2](https://stackoverflow.com/questions/17723822/administrative-regions-map-of-a-country-with-ggmap-and-ggplot2)
- [Map visualizations with external shapefile. Сбербанковский kaggle](https://www.kaggle.com/amclean/map-visualizations-with-external-shapefile?scriptVersionId=1180150)
- [How to create an intensive map of Russia using QGIS or any other software?](https://gis.stackexchange.com/questions/40921/how-to-create-an-intensive-map-of-russia-using-qgis-or-any-other-software)
- [Global Administrative Areas. Boundaries without limits](http://www.gadm.org/)
- [Leaflet offline map without map tiles](https://stackoverflow.com/questions/27472383/leaflet-offline-map-without-map-tiles?rq=1)
- [Загрузка файлов из GADM вручную](http://www.gadm.org/country)
- Depricated [A shapefile of the TZ timezones of the world](http://efele.net/maps/tz/world/). Переехало сюда:
["A tool to extract data from Open Street Map (OSM) to build the boundaries of the world's timezones that includes territorial waters."](https://github.com/evansiroky/timezone-boundary-builder)
- [Map Shaper](http://mapshaper.org/)
- Сглаживание полигонов:
	- [problem with polygon smoothing in R](https://gis.stackexchange.com/questions/117965/problem-with-polygon-smoothing-in-r)
	- [Smoothing polygons in contour map?](https://gis.stackexchange.com/questions/24827/smoothing-polygons-in-contour-map/24929#24929)
	- [Create polygon from set of points distributed](https://stackoverflow.com/questions/26087772/create-polygon-from-set-of-points-distributed/26089377#26089377)
	- [Tools, shapefiles & data to work with an "AlbersUSA" composite projection in R](https://github.com/hrbrmstr/albersusa)
	- [Simplifying complex polygons/polylines](https://rstudio.github.io/leaflet/shapes.html)
	- [rmapshaper Basics](https://cran.r-project.org/web/packages/rmapshaper/vignettes/rmapshaper.html)
- [Технология импорта пространственных данных из OpenStreetMap](https://gisinfo.ru/techno/osm.htm)

# 05.02.2018
## Tools
- [GoAccess](https://goaccess.io/) is an open source real-time web log analyzer and interactive viewer that runs in a terminal in *nix systems or through your browser. It provides fast and valuable HTTP statistics for system administrators that require a visual server report on the fly.

## R
- [Documenting R packages: roxygen2 vs. direct Rd input](https://www.enchufa2.es/archives/documenting-r-packages-roxygen2-vs-direct-rd-input.html)
- COOL! [Reproducible Research: Write your Clinical Chemistry paper using R Markdown](http://labrtorian.com/2018/02/05/reproducible-research-write-your-clinical-chemistry-paper-using-r/)
- [Concatenate Embeddings for Categorical Variables with Keras](https://flovv.github.io/Embeddings_with_keras_part2/)
- [A tidy API for graph manipulation](https://github.com/thomasp85/tidygraph)
- COOL! [RStudio rconf 2018](https://github.com/rstudio/rstudio-conf/tree/master/2018)
- [In between a rock and a conditional join](https://www.mango-solutions.com/blog/in-between-a-rock-and-a-conditional-join). Тут как раз про "Fuzzy wuzzy join".

# 01.02.2018
## R
- [An R-focused pipeline toolkit for reproducibility and high-performance computing](https://ropensci.github.io/drake)
- [Native SSH client in R](https://github.com/ropensci/ssh)
- [RCurl: General Network (HTTP/FTP/...) Client Interface for R](https://cran.r-project.org/web/packages/RCurl/index.html)
- Как достать файл по scp, имея пароль? Параметр `password`, который явно в документации не прописан.
```
scp("10.0.0.246", path="/var/log/squid/access.log", binary=FALSE, password="pass", user="root")
```
При этом ключик надо делать на клиентской машине, командой `ssh-keygen -t rsa -b 2048`
- COOL [Scrape a page in R using rvest or RCurl or httr](https://stackoverflow.com/questions/46318348/scrape-a-page-in-r-using-rvest-or-rcurl-or-httr)
- COOL [Scales, axes and legends](http://www.hafro.is/~einarhj/education/ggplot2/scales.html)
- COOL [compareGroups: Descriptive Analysis by Groups](https://cran.r-project.org/web/packages/compareGroups/index.html)
Create data summaries for quality control, extensive reports for exploring data, as well as publication-ready univariate or bivariate tables in several formats (plain text, HTML,LaTeX, PDF, Word or Excel. Create figures to quickly visualise the distribution of your data (boxplots, barplots, normality-plots, etc.). Display statistics (mean, median, frequencies, incidences, etc.). Perform the appropriate tests (t-test, Analysis of variance, Kruskal-Wallis, Fisher, log-rank, ...) depending on the nature of the described variable (normal, non-normal or qualitative). Summarize genetic data (Single Nucleotide Polymorphisms) data displaying Allele Frequencies and performing Hardy-Weinberg Equilibrium tests among other typical statistics and tests for these kind of data.


# 31.01.2018
## R
- [Using the R Software for Log File Analysis - Usenix](https://www.usenix.org/system/.../1403_11-15_tsoukalos.pdf)
- [Introduction to webreadr](https://cran.r-project.org/web/packages/webreadr/vignettes/Introduction.html). Reading web access logs
- [Scraping Wikipedia Tables from Lists for Visualisation](https://www.gokhanciflikli.com/post/scraping-wikipedia/)
- COOL! [fastrtext](https://pommedeterresautee.github.io/fastrtext/). R wrapper for fastText C++ code from Facebook. fastText is a library for efficient learning of word representations and sentence classification.
- `readr` questions:
	- [Load from file delimited by multiple spaces? #605 {Closed}](https://github.com/tidyverse/readr/issues/605)


# 30.01.2018
## R
- [Display all values in a Shiny selectInput box (1000+)](https://stackoverflow.com/questions/40710947/display-all-values-in-a-shiny-selectinput-box-1000)
- [Selectize.js options](https://github.com/selectize/selectize.js/blob/master/docs/usage.md)
- [The “cluster of six”. Unsupervised machine learning](https://thinkr.biz/2018/01/29/cluster-of-six/)
- [sparklyr 0.7](https://blog.rstudio.com/2018/01/29/sparklyr-0-7/). We are excited to share that sparklyr 0.7 is now available on CRAN!
- [Moving parts of a country over a map](http://rmhogervorst.nl/cleancode/blog/2018/01/29/moving-parts-of-a-map-in-a-gif.html)
- [A SMOOTH TRANSITION BETWEEN CHLOROPLETH AND CARTOGRAM](https://www.r-graph-gallery.com/a-smooth-transition-between-chloropleth-and-cartogram/)

# 29.01.2018
## R
- [Exploring Embeddings for Categorical Variables with Keras](https://flovv.github.io/Embeddings_with_keras/)
- [Type I error rates in two-sample t-test by simulation](https://heuristicandrew.blogspot.ru/2018/01/type-i-error-rates-in-two-sample-t-test.html)
- [Log shiny app visitors and R usage to Google Analytics](http://www.bnosac.be/index.php/blog/73-log-shiny-app-visitors-r-events-and-r-usage-to-google-analytics)
- [rte-antares-rpackage/manipulateWidget](https://github.com/rte-antares-rpackage/manipulateWidget). Add More Interactivity to htmlWidgets
- Shiny. Ручная эмуляция выбора из списка. [Chooser demo](https://shiny.rstudio.com/gallery/custom-input-control.html). Demonstrates creating a custom Shiny input binding for a simple JavaScript-enabled "dueling select box" input widget.
- [R or Python? Python or R? The ongoing debate.](https://tomaztsql.wordpress.com/2018/01/28/r-or-python-python-or-r-the-ongoing-debate/)
- [Have you ever asked yourself, "how should I approach the classic pre-post analysis?"](https://www.rdatagen.net/post/thinking-about-the-run-of-the-mill-pre-post-analysis/)
- ebook [Getting started with mdatools for R](http://mdatools.com/mdatools/index.html). This is a user guide for mdatools — R package for preprocessing, exploring and analysis of multivariate data


# 26.01.2018
## R. Импорт из Word, Text mining
- Bob Rudis. [docxtractr: Extract Data Tables and Comments from Microsoft Word Documents](https://cran.r-project.org/web/packages/docxtractr/)
	- [Using R To Get Data *Out Of* Word Docs](https://rud.is/b/2015/08/23/using-r-to-get-data-out-of-word-docs/)
	- [New Pacakge “docxtractr” – Easily Extract Tables From Microsoft Word Docs](https://rud.is/b/2015/08/24/new-pacakge-docxtractr-easily-extract-tables-from-microsoft-word-docs/)
- [textreadr](https://www.rdocumentation.org/packages/textreadr/versions/0.7.0) is a small collection of convenience tools for reading text documents into R. This is not meant to be an exhaustive collection; for more see the tm package.
- COOL! [CRAN Task View: Natural Language Processing](https://cran.r-project.org/web/views/NaturalLanguageProcessing.html)
- [tm: Text Mining Package](https://cran.r-project.org/web/packages/tm/index.html). A framework for text mining applications within R.
- Очень концептуальные вопросы и отсылки, хоть и 2013 год. [how do I create a corpus of *.docx files with tm?](https://stackoverflow.com/questions/16065952/how-do-i-create-a-corpus-of-docx-files-with-tm)
- [textreg: n-Gram Text Regression, aka Concise Comparative Summarization](https://cran.r-project.org/web/packages/textreg/index.html)
- [Text Processing in R](http://www.mjdenny.com/Text_Processing_In_R.html)
- [Text mining and word cloud fundamentals in R : 5 simple steps you should know](http://www.sthda.com/english/wiki/text-mining-and-word-cloud-fundamentals-in-r-5-simple-steps-you-should-know)
- [Wordcloud2 introduction](https://cran.r-project.org/web/packages/wordcloud2/vignettes/wordcloud.html). This is an introduction to wordcloud2 package. This package provides an HTML5 interface to wordcloud for data visualization. Timdream’s wordcloud2.js is used in this package.
- [Change font in Wordcloud package R](https://stackoverflow.com/questions/43460652/change-font-in-wordcloud-package-r)
- [Демки на wordcloud](http://www.r-graph-gallery.com/102-text-mining-and-wordcloud/)
- COOL! [Hardwired..for tidy text](https://www.johnmackintosh.com/2018-01-30-hardwired-for-tidy-text/)

# 25.01.2018
## R
- [Scraping a website with 5 lines of R code](http://blog.revolutionanalytics.com/2018/01/scraping-with-5-lines-r.html)
- [Exploring lime on the house prices dataset](http://blog.haunschmid.name/lime-on-regression-model-house-prices/)
- COOL! [Exploratory Data Analysis & Data Preparation with 'funModeling'](https://blog.datascienceheroes.com/exploratory-data-analysis-data-preparation-with-funmodeling/)
- [Predicting Fraud with Autoencoders and Keras](https://tensorflow.rstudio.com/blog/keras-fraud-autoencoder.html)
- [Styling Base R Graphics. Publication quality base R graphics](http://blog.jumpingrivers.com/posts/2018/2018-01-24-base-r-graphics/)
- COOL! [nodbi: the NoSQL Database Connector](https://ropensci.org/technotes/2018/01/25/nodbi/)
- [XLCONNECT 0.2-14](http://mirai-solutions.ch/news/2018/01/25/XLConnect-0.2-14/)
- [Dec 2017: "Top 40" New Package Picks](https://rviews.rstudio.com/2018/01/25/dec-2017-new-package-picks/)
- Может пригодиться при подготовке курсов. [INWT's guidelines for R code](https://www.inwt-statistics.com/read-blog/inwts-guidelines-for-r-code.html)


## Git
- [Какая разница между 'git pull' и 'git fetch'?](https://ru.stackoverflow.com/questions/641013/%D0%9A%D0%B0%D0%BA%D0%B0%D1%8F-%D1%80%D0%B0%D0%B7%D0%BD%D0%B8%D1%86%D0%B0-%D0%BC%D0%B5%D0%B6%D0%B4%D1%83-git-pull-%D0%B8-git-fetch).
`git pull` — это, по сути, команда `git fetch`, после которой сразу же следует `git merge`.

`git fetch` получает изменения с сервера и сохраняет их в каталог `refs/remotes/`.
Это никак не влияет на локальные ветки и текущие изменения. А `git merge` уже вливает все эти изменения в локальную копию.

# 24.01.2018
## R
- [Tidyverse and data.table, sitting side by side… and then base R walks in](https://www.enchufa2.es/archives/tidyverse-and-data-table-sitting-side-by-side-and-then-base-r-walks-in.html)
- [Visualize your Strava routes with R](http://blog.revolutionanalytics.com/2018/01/strava-visualization.html)
- [The progress bar just got a lot cheaper](http://peter.solymos.org/code/2018/01/23/the-progress-bar-just-got-a-lot-cheaper.html)

# DS
- [Чудесный мир Word Embeddings: какие они бывают и зачем нужны?](https://habrahabr.ru/company/ods/blog/329410/)
- [Обзор исследований в области глубокого обучения: обработка естественных языков](https://habrahabr.ru/company/wunderfund/blog/330194/)


# 22.01.2018
- [fs 1.0.0 is now available on CRAN!](https://www.tidyverse.org/articles/2018/01/fs-1.0.0/) fs provides a cross-platform, uniform interface to file system operations. fs uses libuv under the hood, which gives a rock solid cross-platform interface to the filesystem.
- COOL! [ggplot2 Time Series Heatmaps: revisited in the tidyverse](https://margintale.blogspot.ru/2018/01/ggplot2-time-series-heatmaps-revisited.html)
- [Wrapping Access to Web-Services in R-functions](https://flovv.github.io/Accessing_a_web_api/)
- [Exploring handwritten digit classification: a tidy analysis of the MNIST dataset](http://varianceexplained.org/r/digit-eda/)


# 19.01.2018
## R
- [Extract a single dplyr tbl_df row as a vector](https://stackoverflow.com/questions/35617785/extract-a-single-dplyr-tbl-df-row-as-a-vector)
- [Extract a dplyr tbl column as a vector](https://stackoverflow.com/questions/21618423/extract-a-dplyr-tbl-column-as-a-vector)
- [Using column index in dplyr's rename](https://stackoverflow.com/questions/42769650/using-column-index-in-dplyrs-rename)

# 18.01.2018
## R
- COOL! [While you wait for that to finish, can I interest you in parallel processing?](http://appliedpredictivemodeling.com/blog/2018/1/17/parallel-processing)
- [Importance sampling adds an interesting twist to Monte Carlo simulation](https://www.rdatagen.net/post/importance-sampling-adds-a-little-excitement-to-monte-carlo-simulation/)
- [January meeting: Getting started with spatial data and writing R packages from scratch](http://edinbr.org/edinbr/2018/01/08/january-meeting.html)
- COOL! [Slides or talk notes from EdinbR meetings](https://github.com/EdinbR/edinbr-talks)

# 17.01.2018
## R
- COOL! Практическое разпознавание кораблей на изображении с применением сверточных сетей. [A guide to GPU-accelerated ship recognition in satellite imagery using Keras and R (part I)](https://appsilondatascience.com/blog/rstats/2018/01/16/keras.html)
- [A guide to GPU-accelerated ships recognition in satellite imagery using Keras and R (part II)](https://appsilondatascience.com/blog/rstats/2018/01/23/keras.html)
- COOL! Пошаговое руководство по созданию R API с помощью plumber [How to make your machine learning model available as an API with the plumber package](https://shirinsplayground.netlify.com/2018/01/plumber/)
- [5 Things I Learned Making a Package to Work with Hydrometric Data in R](https://ropensci.org/blog/2018/01/16/tidyhydat/)

## RPA
- [Roro](https://github.com/arviedelgado/Roro) is a free open-source Robotic Process Automation software.
- [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/)
- [Workfusion](https://www.workfusion.com/). Intelligent Automation. (RPA)
- [Blue Prism vs Automation Anywhere vs Uipath](http://asha24.com/blog/blue-prism-vs-automation-anywhere-vs-uipath)


# 16.01.2018
## R
- [Base R can be Fast](http://www.win-vector.com/blog/2018/01/base-r-can-be-fast/)
- [Natural Language Processing for non-English languages with udpipe](http://www.bnosac.be/index.php/blog/72-natural-language-processing-for-non-english-languages-with-udpipe)
- [A comparison between spaCy and UDPipe for Natural Language Processing for R users](http://www.bnosac.be/index.php/blog/75-a-comparison-between-spacy-and-udpipe-for-natural-language-processing-for-r-users)
- [NLP with R and UDPipe](https://bnosac.github.io/udpipe/en/). Tokenization, Parts of Speech Tagging, Lemmatization, Dependency Parsing and NLP flows
- [Синтаксически размеченный корпус русского языка: информация для пользователей](http://www.ruscorpora.ru/instruction-syntax.html)
- [Online Udpipe Service](http://lindat.mff.cuni.cz/services/udpipe/)
- [UDPipe User's Manual](https://ufal.mff.cuni.cz/udpipe/users-manual)
	- А вот и описание полученного фрейма с разметкой:  [CoNLL-U Format](http://universaldependencies.org/format.html)
	- [Universal part-of-speech (POS) tags](http://universaldependencies.org/u/pos/index.html)
	- А тут описывается классификация тега XPOS [Alphabetical list of part-of-speech tags used in the Penn Treebank Project:](http://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html)
- Baseline results: [CoNLL 2017 Shared Task](http://universaldependencies.org/conll17/baseline.html). Two open-source systems have been run on the development data under comparable conditions to provide baseline results: UDPipe and SyntaxNet.
- [Главные достижения в области обработки естественного языка в 2017 году](https://habrahabr.ru/company/ods/blog/347524/)


# 15.01.2018
## R
- [Services and tools for building intelligent R applications in the cloud](http://blog.revolutionanalytics.com/2018/01/r-cloud-tools.html)
- Живые Shiny приложения. [Top interactive visualizations of movie scripts](http://smarterpoland.pl/index.php/2018/01/top-interactive-visualizations-of-movie-scripts/)


# 12.01.2018
## DS
- Лучшая статья по наивному байесу, которую я видел [Суровая реальность. Наивный байесовский классификатор]
- [6 простых шагов для освоения наивного байесовского алгоритма (с примером кода на Python)](http://datareview.info/article/6-prostyih-shagov-dlya-osvoeniya-naivnogo-bayesovskogo-algoritma-s-primerom-koda-na-python/)

# 11.01.2018
## Общее
- СOOL! объяснение "на котиках" [Git снизу вверх](https://habrahabr.ru/company/intel/blog/344962/)

## R
- Возможно ли средствами R сделать транслитерацию столбца с данными на русском языке на латиницу? Смотрим [блог в LiveJournal](тут, в комментах есть: http://r-statistics.livejournal.com/48247.html). Я предложил так: `stringi::stri_trans_general(c("Здесь фабула объять не может всех эмоций — шепелявый скороход в юбке тащит горячий мёд.", "Друг мой эльф! Яшке б свёз птиц южных чащ!"), "Russian-Latin/BGN")`
- [Palettes and graphics matching your RStudio editor](https://github.com/fkeck/editheme)

## ML
- [How to implement neural networks in R](http://blog.revolutionanalytics.com/2018/01/neural-networks-r6.html)
- COOL! [Building a neural network from scratch in R](http://selbydavid.com/2018/01/09/neural-network/)
- COOL! Дубль с business-science.io [Deep Learning With Keras To Predict Customer Churn](https://tensorflow.rstudio.com/blog/keras-customer-churn.html)
- [Сверточная сеть на python. Часть 3. Применение модели](https://habrahabr.ru/company/ods/blog/344888/). Распознавание циферок... подход может использоваться для здоровья ИТ сервисов!
- COOL! Про LIME [Looking beyond accuracy to improve trust in machine learning](https://blog.codecentric.de/en/2018/01/look-beyond-accuracy-improve-trust-machine-learning/)
- [TIDYTEXT 0.1.6](https://juliasilge.com/blog/tidytext-0-1-6/) by JULIA SILGE
- [How to implement Random Forests in R](https://r-posts.com/how-to-implement-random-forests-in-r/)
- [R Work Areas. Standardize and Automate](https://somerealnumbers.wordpress.com/2018/01/10/r-work-areas-standardize-and-automate/)
- [Direct forecast X Recursive forecast](https://insightr.wordpress.com/2018/01/10/direct-forecast-x-recursive-forecast/)

# 09.01.2018
## R
- [What's the difference between data science, machine learning, and artificial intelligence?](http://varianceexplained.org/r/ds-ml-ai/)
- [Semantic Question Matching with Deep Learning](https://engineering.quora.com/Semantic-Question-Matching-with-Deep-Learning)
- COOL! [Higher Order Functions](https://tjmahr.github.io)
	- COOL! [Using nonstandard evaluation to simulate a register machine](https://tjmahr.github.io/nonstandard-eval-register-machines/)
	- [Recode values with character subsetting](https://tjmahr.github.io/recode-values-with-character-subsetting/)
- [How to perform Logistic Regression, LDA, & QDA in R](https://datascienceplus.com/how-to-perform-logistic-regression-lda-qda-in-r/)
- [Discontinuing maintenance of jug](http://fishyoperations.com/2018/01/07/discontinuing-maintenance-jug.html)
- [prrd 0.0.1: Parallel Running [of] Reverse Depends](http://dirk.eddelbuettel.com/blog/2018/01/07/#prrd_0.0.1)
- [The Trouble with Tibbles](http://blog.jumpingrivers.com/posts/2018/trouble_with_tibbles/)

## DS
- [Wise.io](https://wise.io/) is a well-resourced, rapidly growing team inside of GE Digital whose charter is to build machine learning powered applications on top of GE’s treasure trove of data assets.
- Article. ["Siamese recurrent architectures for learning sentence similarity"](https://dl.acm.org/citation.cfm?id=3016291)
- [Бизнес-требования к проекту «Прогнозирование инфраструктурных сбоев»](https://sk.ru/foundation/events/july2017/gazpromneft/)


# 04.01.2018
## R
- [Deep Learning from first principles in Python, R and Octave – Part 1](https://gigadom.wordpress.com/2018/01/04/deep-learning-from-basic-principles-in-python-r-and-octave-part-1/)
- [Deep Learning from first principles in Python, R and Octave – Part 2](https://gigadom.wordpress.com/2018/01/11/deep-learning-from-first-principles-in-python-r-and-octave-part-2/)
- [Deep Learning from first principles in Python, R and Octave – Part 3](https://gigadom.wordpress.com/2018/01/30/deep-learning-from-first-principles-in-python-r-and-octave-part-3/)
- Deep Learning from first principles in Python, R and Octave – Part 4](https://gigadom.wordpress.com/2018/02/26/deep-learning-from-first-principles-in-python-r-and-octave-part-4/)
- [billboarder](https://cran.rstudio.com/web/packages/billboarder/vignettes/billboarder-intro.html). This package allow you to use billboard.js, a re-usable easy interface JavaScript chart library, based on D3 v4+.
- [esviz](https://github.com/DJAnderson07/esvis). R Package for effect size visualizations.
- [missRanger: Fast Imputation of Missing Values](https://cran.r-project.org/web/packages/missRanger/index.html)
- COOL! [Introduction to Huxtable](https://hughjonesd.github.io/huxtable/huxtable.html)
- [Divide and parallelize large data problems with Rcpp](http://blog.revolutionanalytics.com/2018/01/parallelize-rcpp.html)

# 02.01.2018
## R
- [Five tips to improve your R code](https://drsimonj.svbtle.com/five-simple-tricks-to-improve-your-r-code)
- [Making R Code Faster: A Case Study](https://robinsones.github.io/Making-R-Code-Faster-A-Case-Study/)
- [Forecasting time series with neural networks in R](http://kourentzes.com/forecasting/2017/02/10/forecasting-time-series-with-neural-networks-in-r/)
- [smooth functions in 2017](http://forecasting.svetunkov.ru/en/2018/01/01/smooth-functions-in-2017/)
- [Interpolating Statistical Tables](https://davegiles.blogspot.ru/2018/01/interpolating-statistical-tables.html)
- [Helpful Data Science Reads](https://somerealnumbers.wordpress.com/2018/01/03/helpful-data-science-reads/)
- GETTING DATA [The Mcomp Package](https://datascienceplus.com/the-mcomp-package/)
- COOL! [Заметки по R: Гетероскедастичность](https://bdemeshev.github.io/r_cycle/cycle_files/12_hetero.html)
- Отличный блог. Неплохо бы сконтактировать с автором. [R: Анализ и визуализация данных](http://r-analytics.blogspot.ru)
- COOL! [desctable usage vignette](https://cran.r-project.org/web/packages/desctable/vignettes/desctable.html). Desctable is a comprehensive descriptive and comparative tables generator for R.
- COOL! Классика! [Vectorization in R: Why?](http://www.noamross.net/blog/2014/4/16/vectorization-in-r--why.html) by Noam Ross, 16 April 2014
