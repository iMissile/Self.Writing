
# Linear Regression
## blogs
- COOL! e-book [The Truth About Linear Regression](https://www.stat.cmu.edu/~cshalizi/TALR/)
- [Learn by Marketing. Linear Regression in R](https://www.learnbymarketing.com/tutorials/linear-regression-in-r/)

- Запускаем `lm` для кучи колонок:
	- COOL! [Creating new Functions with Linear Regression in R](https://stackoverflow.com/questions/38175775/creating-new-functions-with-linear-regression-in-r)
	- COOL! [Linear Regression in R without names of column](https://stackoverflow.com/questions/43004888/linear-regression-in-r-without-names-of-column)
`debugonce(lm.fit)`

- [Fitting & Interpreting Linear Models in R](http://blog.yhat.com/posts/r-lm-summary.html)
- [Slides from my talk on the broom package](http://varianceexplained.org/r/broom-slides/)
- [broom: a package for tidying statistical models into data frames](http://varianceexplained.org/r/broom-intro/)
- [Estimated Simple Regression Equation](http://www.r-tutor.com/elementary-statistics/simple-linear-regression/estimated-simple-regression-equation)
- [PARALLELIZING LINEAR REGRESSION OR USING MULTIPLE SOURCES](https://freakonometrics.hypotheses.org/53283)
- [Machine Learning with R: A Complete Guide to Linear Regression](https://appsilon.com/r-linear-regression/)
- COOL! Ответ Хадли. [Extract Slopes by group, Broom? Dplyr?](https://community.rstudio.com/t/extract-slopes-by-group-broom-dplyr/2751)
```
library(tidyverse) #for purrr, tidyr and dplyr
library(broom)

Orange %>%
  split(.$Tree) %>%
  map(~lm(age ~ 1 + circumference, data = .x)) %>%
  map_df(tidy) %>%
  filter(term == 'circumference')
```
- [broom: a package for tidying statistical models into data frames](http://varianceexplained.org/r/broom-intro/)
- [QUICK GUIDE: INTERPRETING SIMPLE LINEAR MODEL OUTPUT IN R](https://feliperego.github.io/blog/2015/10/23/Interpreting-Model-Output-In-R)
- [Interpret R Linear/Multiple Regression output (lm output point by point), also with Python](https://medium.com/@vineetjaiswal/interpret-r-linear-multiple-regression-output-lm-output-point-by-point-also-with-python-8e53b2ee2a40)
- COOL! [Using Linear Regression for Predictive Modeling in R](https://www.dataquest.io/blog/statistical-learning-for-predictive-modeling-r/)
- [Fitting & Interpreting Linear Models in R](http://blog.yhat.com/posts/r-lm-summary.html) by yhat | May 18, 2013
- COOL! [How do I interpret the summary of a linear model in R?](https://www.quora.com/How-do-I-interpret-the-summary-of-a-linear-model-in-R)
```
In general, to interpret a (linear) model involves the following steps.

1. Assess the assumptions of the model. In a linear model, we’d like to check whether there severe violations of linearity, normality, and homoskedasticity. In addition, we may want to check whether the predictors are not too severely intercorrelated (look at multicollinearity-measures such as tolerances, VIFs, or condition indices), and whether there are influential cases or outliers that unduly distort the model (look at standardized residuals, Cook’s distances, etc.)
2. Assess the fit and significance of the model as a whole. In a linear model, we’d inspect the amount of variance explained, that is the R2 or the adjusted R2, and the ANOVA-test on the model’s significance.
3. Assess the direction, magnitude, and significance of the individual predictors that comprise the model. In a linear model, we’d interpret the direction and magnitude of the predictors directly via the b-coefficients, that is: “a one unit increase on X1 predicts an increase of b1 on Y”, etc. Note that in non-linear models such as models that contain quadratic terms or interaction effects, the interpretation of effects is trickier. Finally, for any term, it’s significance can be interpreted via p-values reported in the output.
```
- [R Tensorflow Multiple Linear Regression](https://blog.alpha-analysis.com/2019/08/r-tensorflow-multiple-linear-regression.html)
- [Many ways to do the same thing: linear regression](https://statisticaloddsandends.wordpress.com/2019/04/08/many-ways-to-do-the-same-thing-linear-regression/)
- [Pushing Ordinary Least Squares to the limit with Xy()](https://www.statworx.com/de/blog/pushing-ordinary-least-squares-to-the-limit-with-xy/)
- COOL! [Forecast double seasonal time series with multiple linear regression in R](https://petolau.github.io/Forecast-double-seasonal-time-series-with-multiple-linear-regression-in-R/)

## ols
- [Are linear regression and least squares regression necessarily the same thing?](https://stats.stackexchange.com/questions/523708/are-linear-regression-and-least-squares-regression-necessarily-the-same-thing)
- [Understanding Ordinary Least Squares (OLS) Regression](https://builtin.com/data-science/ols-regression)
Linear regression is employed in supervised machine learning tasks. OLS regression can be used to obtain a straight line as close as possible to your data points.

## fixed slope
- [Linear regression with specified slope](https://stackoverflow.com/questions/33292969/linear-regression-with-specified-slope)
- [set slope to 1 in linear regression in r {closed}](https://stats.stackexchange.com/questions/158821/set-slope-to-1-in-linear-regression-in-r)
- [Linear fit with a previously known slope {duplicate}](https://stackoverflow.com/questions/20709432/linear-fit-with-a-previously-known-slope)
- [Set one or more of coefficients to a specific integer](https://stackoverflow.com/questions/10027664/set-one-or-more-of-coefficients-to-a-specific-integer)
```
df<-data.frame(aa=1:6,bb=2:7,cc=c(4,2,7,5,8,3))
lm(cc ~ aa + offset(647*bb), data = df)
```

## fixed interception
- [Regression with fixed intercept](https://stats.stackexchange.com/questions/393414/regression-with-fixed-intercept)
- [Linear Regression with a known fixed intercept in R](https://stackoverflow.com/questions/7333203/linear-regression-with-a-known-fixed-intercept-in-r)

## Linear Regression With Errors in Both Variables

Статьи
- [Linear Regression With Errors in Both Variables](https://vp.phys.ethz.ch/DataAnalysis/pdf/14Nov2016.pdf)
- [Least Squares Methods for Treating Problems with Uncertainty in xand y](https://pubs.acs.org/doi/epdf/10.1021/acs.analchem.0c02178)

Размышления на тему
- [Regression when x and y each have uncertainties](https://stats.stackexchange.com/questions/422566/regression-when-x-and-y-each-have-uncertainties)
- [Introduction to the pls Package](https://cran.r-project.org/web/packages/pls/vignettes/pls-manual.pdf)
- [Матрица Якоби и якобиан](http://vmath.ru/vf5/algebra2/dets/jacobian)
- [Linear model where the data has uncertainty, using R](https://stats.stackexchange.com/questions/235693/linear-model-where-the-data-has-uncertainty-using-r)
- [The `metafor` Package: A Meta-Analysis Package for R](https://www.metafor-project.org/doku.php/metafor). `rma` method

!!! Отличный мини-учебник по статистике с масой примеров на R
https://mgimond.github.io/Stats-in-R/regression.html

### «Fit» or «chi-squared»
https://www.scribbr.com/frequently-asked-questions/how-do-i-perform-a-chi-square-goodness-of-fit-test-in-r/
https://stats.stackexchange.com/questions/235693/linear-model-where-the-data-has-uncertainty-using-r
https://vp.phys.ethz.ch/DataAnalysis/DataAnalysisToolbox/Lecture_5.pdf
https://cran.r-project.org/web/packages/discretefit/vignettes/package_introduction.html
https://cran.r-project.org/doc/contrib/Ricci-distributions-en.pdf
https://lbbe-software.github.io/fitdistrplus/
https://github.com/JorisChau/gslnls
- [GSL - GNU Scientific Library](https://www.gnu.org/software/gsl/)
	- [RcppGSL](https://cran.r-project.org/web/packages/RcppGSL/index.html): 'Rcpp' Integration for 'GNU GSL' Vectors and Matrices
	- [gsl](https://cran.r-project.org/web/packages/gsl/index.html): Wrapper for the Gnu Scientific Library
	- [RcppZiggurat](https://cran.r-project.org/web/packages/RcppZiggurat/index.html): 'Rcpp' Integration of Different "Ziggurat" Normal RNG Implementations
- [In Scipy how and why does curve_fit calculate the covariance of the parameter estimates](https://stackoverflow.com/questions/14854339/in-scipy-how-and-why-does-curve-fit-calculate-the-covariance-of-the-parameter-es/14857441#14857441)
https://www2.ph.ed.ac.uk/~mim/least_squares_poster.pdf
- [How do you weight a chi square for uncertainties in x and y (different units)?](https://physics.stackexchange.com/questions/681680/how-do-you-weight-a-chi-square-for-uncertainties-in-x-and-y-different-units)
https://www.astro.umd.edu/~miller/teaching/astr288a/lecture12.pdf
https://faculty1.coloradocollege.edu/~sburns/LinearFitting/SimpleDataFittingWithError.html

### York
- [Regression when each point has its own uncertainty in both $x$ and $y$](https://stats.stackexchange.com/questions/201859/regression-when-each-point-has-its-own-uncertainty-in-both-x-and-y) Функция `yorkfit`.
- Пакетик R package `bfsl`: Best-fit Straight Line (York algo) https://cran.r-project.org/web/packages/bfsl/readme/README.html
- Perform linear regression fit using the algorithm presented by York et al. (2004), [`fit_bivariate.py` ](https://gist.github.com/mikkopitkanen/ce9cd22645a9e93b6ca48ba32a3c85d0)
- OriginLab 15.2.6 Algorithms (Fit Linear with X Error) https://www.originlab.com/doc/en/Origin-Help/Ref-Linear-XErr
- york {geostats} R Documentation
Linear regression of X,Y-variables with correlated errors
https://search.r-project.org/CRAN/refmans/geostats/html/york.html
Тут все на R реализовано, любопытно почитать.

https://cran.r-project.org/web/packages/IsoplotR/index.html
https://www.ucl.ac.uk/~ucfbpve/isoplotr/home/
`IsoplotR::york`

Почитать
https://github.com/JENScoding/yorkregression
https://stats.stackexchange.com/questions/574027/chi-square-fit-fitting-data-to-a-straight-line-incomplete-gamma-function-as-go
https://www.physicsforums.com/threads/chi-squared-fit-with-errors-on-both-x-and-y.980490/


## viz
- [ggside: Plot Linear Regression using Marginal Distributions (ggplot2 extension)](https://www.business-science.io/code-tools/2021/05/18/marginal_distributions.html)


## Splines
- [Spline Regression in R](https://medium.com/analytics-vidhya/spline-regression-in-r-960ca82aa62c)
- [2 Piecewise Regression and Splines](https://bookdown.org/tpinto_home/Beyond-Linearity/piecewise-regression-and-splines.html)
- [How to Perform Piecewise Regression in R (Step-by-Step)](https://www.statology.org/piecewise-regression-in-r/)


# 18.09.2023
- [LME4 Tutorial: Popularity Data](https://www.rensvandeschoot.com/tutorials/lme4/)
- COOL! Тут всякие новомодные концепты разбираются в глаголах tidyverse. [How to perform group-wise linear regression for a data frame in R](https://community.rstudio.com/t/how-to-perform-group-wise-linear-regression-for-a-data-frame-in-r/158783)
- [Multiple linear regression made simple](https://statsandr.com/blog/multiple-linear-regression-made-simple/)
- [visreg: Visualization of Regression Models](https://cran.r-project.org/web/packages/visreg/index.html)
- [Standard error of the regression](https://statisticsbyjim.com/glossary/standard-error-regression/) by Jim Frost. Approximately 95% of the observations should fall within plus/minus 2*standard error of the regression from the regression line, which is also a quick approximation of a 95% prediction interval.
- [Regression Analysis: How to Interpret S, the Standard Error of the Regression](https://blog.minitab.com/en/adventures-in-statistics-2/regression-analysis-how-to-interpret-s-the-standard-error-of-the-regression)

## Logistic distribution
- [The Logistic Distribution](https://stat.ethz.ch/R-manual/R-devel/library/stats/html/Logistic.html)
- [Logistic Distribution in R (4 Examples) | dlogis, plogis, qlogis & rlogis Functions](https://statisticsglobe.com/logistic-distribution-in-r-dlogis-plogis-qlogis-rlogis)


## Linear Mixed Effect Model (aka Hierarchical Modeling)
- COOL! сделана отличная анимация на react-е для пояснения принципов. [An Introduction to Hierarchical Modeling](https://mfviz.com/hierarchical-models/).
This visual explanation introduces the statistical concept of Hierarchical Modeling, also known as _Mixed Effects Modeling_ or by these other terms. This is an approach for modeling nested data. Keep reading to learn how to translate an understanding of your data into a hierarchical model specification.
	- Hierarchical Models. [Исходный код для расчетов](https://github.com/mkfreeman/hierarchical-models/)
- [Mixed Models with R](https://m-clark.github.io/mixed-models-with-R/) by Michael Clark
- [mixedup](https://m-clark.github.io/mixedup/index.html). a package for extracting clean results from mixed models
- [INTRODUCTION TO LINEAR MIXED MODELS](https://ourcodingclub.github.io/tutorials/mixed-models/)
- [Using random effects in GAMs with mgcv](https://fromthebottomoftheheap.net/2021/02/02/random-effects-in-gams/)


## R formulae
- [formula {stats}](https://stat.ethz.ch/R-manual/R-devel/library/stats/html/formula.html). The generic function formula and its specific methods provide a way of extracting formulae which have been included in other objects.
- COOL! [Formulae in R - ANOVA and other models, mixed and fixed](https://conjugateprior.org/2013/01/formulae-in-r-anova/)
- [The R Formula Method: The Good Parts](https://rviews.rstudio.com/2017/02/01/the-r-formula-method-the-good-parts/). 2017-02-01 by Max Kuhn
- [The R Formula Method: The Bad Parts](https://rviews.rstudio.com/2017/03/01/the-r-formula-method-the-bad-parts/).  2017-03-01 by Max Kuhn
- [Asterisk (*) vs. colon (:) in R formulas {closed}](https://stackoverflow.com/questions/40567421/asterisk-vs-colon-in-r-formulas)
- [Condition ( | ) in R formula](https://stackoverflow.com/questions/42417963/condition-in-r-formula)
- [Changing the variable inside an R formula](https://statisticaloddsandends.wordpress.com/2019/08/24/changing-the-variable-inside-an-r-formula/)
- COOL! [Formulas in R Tutorial](https://www.datacamp.com/community/tutorials/r-formula-tutorial)
- [Advanced R. 20.3.4 Under the hood](https://adv-r.hadley.nz/evaluation.html#quosure-impl) Quosures were inspired by R’s formulas, because formulas capture an expression and an environment
- [Formula: Extended Model Formulas](https://cran.r-project.org/web/packages/Formula/index.html)
- [Expressing design formula in R](http://genomicsclass.github.io/book/pages/expressing_design_formula.html)
- [How to write a linear model formula with 100 variables in R](https://stats.stackexchange.com/questions/29477/how-to-write-a-linear-model-formula-with-100-variables-in-r)
- [anova test fails on lme fits created with pasted formula](https://stackoverflow.com/questions/7666807/anova-test-fails-on-lme-fits-created-with-pasted-formula/7668846#7668846)
- [Use of ~ (tilde) in R programming Language](https://stackoverflow.com/questions/14976331/use-of-tilde-in-r-programming-language)
	- [The 'formulas' section of the lazyeval vignette gives a good introduction to what a formula is](https://cran.r-project.org/web/packages/lazyeval/vignettes/lazyeval.html)
- [formula From stats v3.5.2](https://www.rdocumentation.org/packages/stats/versions/3.5.2/topics/formula) Model Formulae
- Повтор. [Use quick formula functions in purrr::map (+ base vs tidtyverse idiom comparisons/examples)](https://rud.is/b/2016/07/26/use-quick-formula-functions-in-purrrmap-base-vs-tidtyverse-idiom-comparisonsexamples/)
- Применение формул. Навеяно из документации tmaptools.pdf: `sp::coordinates(five_cities_geocode) <- ~lon+lat`
	- [The R Formula Method: The Good Parts](https://rviews.rstudio.com/2017/02/01/the-r-formula-method-the-good-parts/)
	- [The R Formula Method: The Bad Parts](https://rviews.rstudio.com/2017/03/01/the-r-formula-method-the-bad-parts/)
	- [What does the R formula y~1 mean?](https://stackoverflow.com/questions/13366755/what-does-the-r-formula-y1-mean)
- [Building formulae](http://www.brodrigues.co/blog/2017-12-27-build_formulae/)
- [Using a variable in update() in R to update formula](https://stackoverflow.com/questions/38980066/using-a-variable-in-update-in-r-to-update-formula)

# A/B
- COOL! [a/b testing](https://bytepawn.com/tag/ab-testing.html)
- [Online Experiments Tricks — Variance Reduction](https://towardsdatascience.com/online-experiments-tricks-variance-reduction-291b6032dcd7)
Stratification, CUPED, Variance-Weighted Estimators, and ML-based methods CUPAC and MLRATE
- COOL! [From Power Calculations to P-Values: A/B Testing at Stack Overflow](https://juliasilge.com/blog/ab-testing/)
## A/B as a form of regression
- e-book [Causal Inference for The Brave and True](https://matheusfacure.github.io/python-causality-handbook/landing-page.html)
- [50 оттенков линейной регрессии, или почему всё, что вы знаете об A/B тестах, помещается в одно уравнение](https://habr.com/ru/companies/X5Tech/articles/846298/)
- [Variance reduction with CUPED/CUPAC#](https://tea-tasting.e10v.me/user-guide/#variance-reduction-with-cupedcupac)
