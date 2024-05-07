
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

## fixed interception
- [Regression with fixed intercept](https://stats.stackexchange.com/questions/393414/regression-with-fixed-intercept)
- [Linear Regression with a known fixed intercept in R](https://stackoverflow.com/questions/7333203/linear-regression-with-a-known-fixed-intercept-in-r)

## viz
- [ggside: Plot Linear Regression using Marginal Distributions (ggplot2 extension)](https://www.business-science.io/code-tools/2021/05/18/marginal_distributions.html)


# 18.09.2023
- [mixedup](https://m-clark.github.io/mixedup/index.html). a package for extracting clean results from mixed models
- [LME4 Tutorial: Popularity Data](https://www.rensvandeschoot.com/tutorials/lme4/)
- COOL! Тут всякие новомодные концепты разбираются в глаголах tidyverse. [How to perform group-wise linear regression for a data frame in R](https://community.rstudio.com/t/how-to-perform-group-wise-linear-regression-for-a-data-frame-in-r/158783)
- [Multiple linear regression made simple](https://statsandr.com/blog/multiple-linear-regression-made-simple/)
- [visreg: Visualization of Regression Models](https://cran.r-project.org/web/packages/visreg/index.html)
- [Standard error of the regression](https://statisticsbyjim.com/glossary/standard-error-regression/) by Jim Frost. Approximately 95% of the observations should fall within plus/minus 2*standard error of the regression from the regression line, which is also a quick approximation of a 95% prediction interval.
- [Regression Analysis: How to Interpret S, the Standard Error of the Regression](https://blog.minitab.com/en/adventures-in-statistics-2/regression-analysis-how-to-interpret-s-the-standard-error-of-the-regression)

# 17.09.2023
- COOL! сделана отличная анимация на react-е для пояснения принципов. [An Introduction to Hierarchical Modeling](https://mfviz.com/hierarchical-models/).
This visual explanation introduces the statistical concept of Hierarchical Modeling, also known as _Mixed Effects Modeling_ or by these other terms. This is an approach for modeling nested data. Keep reading to learn how to translate an understanding of your data into a hierarchical model specification.
	- Hierarchical Models. [Исходный код для расчетов](https://github.com/mkfreeman/hierarchical-models/)


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


