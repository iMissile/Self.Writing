# 20.10.2024
- [Removing Abs from Abs\[a + Exp\[I*c\]b\]^2](https://mathematica.stackexchange.com/questions/31485/removing-abs-from-absa-expicb2)

# 18.10.2024
- [How to do substitution of a function in mathematica](https://stackoverflow.com/questions/4975136/how-to-do-substitution-of-a-function-in-mathematica)
I have the expression `D[f[x, y], x]`, and I want to substitute `f[x,y]` with `x*y`
- [Substitution of an expression into another expression](https://mathematica.stackexchange.com/questions/195396/substitution-of-an-expression-into-another-expression)
- [What is a Gröbner Basis](https://math.berkeley.edu/~bernd/what-is.pdf)
- [Gröbner basis](https://en.wikipedia.org/wiki/Gr%C3%B6bner_basis)

# 21.09.2024
- [Assign the results from a Solve to variable(s)](https://mathematica.stackexchange.com/questions/6669/assign-the-results-from-a-solve-to-variables)
Version 10 built-in function `Values` does value extraction conveniently for rules appearing in lists of arbitrary lengths and depths:
Here's a painless solution:
`s = Solve[y^2 == 13 x + 17 && y == 193 x + 29, {x, y}];`
Assign the four results of the solution s above to a variable each, in sequence
`{X1, Y1, X2, Y2} = s // Values // Flatten;`


# 27.08.2024
А как же работать в Wolfram с размерными величинами?
- [Units & Quantities](https://reference.wolfram.com/language/guide/Units.html)
- [Units Overview](https://reference.wolfram.com/language/tutorial/UnitsOverview.html)
- [MixedUnit](https://reference.wolfram.com/language/ref/MixedUnit.html). represents a mixed-unit expression consisting of units unit_1 through unit_n.
- [Degree](https://reference.wolfram.com/language/ref/Degree.html). Degree can be entered as deg: `Esc deg Esc`
- [Convert Radian to Degree?](https://community.wolfram.com/groups/-/m/t/1260622)

# 15.05.2024
Разбираемся как из системы уравнений получать одно, развертывая подстановки.
- [Substitution of an expression into another expression](https://mathematica.stackexchange.com/questions/195396/substitution-of-an-expression-into-another-expression)
- [Eliminate [{x = 2cos(t)/(1+a sin(t)), y = 2sin(t)/(1+a sin(t))},t]](https://www.wolframalpha.com/input?i=Eliminate+%5B%7Bx+%3D+2cos%28t%29%2F%281%2Ba+sin%28t%29%29%2C+y+%3D+2sin%28t%29%2F%281%2Ba+sin%28t%29%29%7D%2Ct%5D)

# 14.03.2024
- Хитро же рисуют модуль в Математике! [Absolute value's vertical bar symbol in Text cell formula](https://mathematica.stackexchange.com/questions/171753/absolute-values-vertical-bar-symbol-in-text-cell-formula)
If you want to type the expression into a cell, use `Esc l | Esc` instead of just `|` for the left side of the absolute value expression, and similarly `Esc r | Esc` instead of `|` for the right side. 

# 13.12.2023
- [Mathematica: Determine if all integers in a list are less than a number?](https://stackoverflow.com/questions/1184995/mathematica-determine-if-all-integers-in-a-list-are-less-than-a-number)
- [Alternatives to procedural loops and iterating over lists in Mathematica](https://mathematica.stackexchange.com/questions/7924/alternatives-to-procedural-loops-and-iterating-over-lists-in-mathematica)
- [Another way to avoid nested loops is with Tuples, as discussed [here](https://mathematica.stackexchange.com/questions/7915/assigning-a-particular-value-to-array-elements/7919#7919). This nested For loop Can be rewritten faster as:
`Xarray = A @@@ Tuples[Range[0, 9], 3];`
- [How to generate flattened tables?](https://mathematica.stackexchange.com/questions/170756/how-to-generate-flattened-tables)
e.g. `f @@@ Tuples[{Range[10], Range[5], Range[2]}]`
- [Polynomial Degree](https://mathworld.wolfram.com/PolynomialDegree.html). А еще есть тут: [PolynomialDegree. Compute the degree of a polynomial in any number of variables](https://resources.wolframcloud.com/FunctionRepository/resources/PolynomialDegree/)
- [Extract variable and coefficient from equation elegantly](https://mathematica.stackexchange.com/questions/126553/extract-variable-and-coefficient-from-equation-elegantly)

## Code conventions
- [General strategies to write big code in Mathematica?](https://mathematica.stackexchange.com/questions/109888/general-strategies-to-write-big-code-in-mathematica)
- [How to write a long function in Mathematica? Using Notebook as function?](https://stackoverflow.com/questions/8377750/how-to-write-a-long-function-in-mathematica-using-notebook-as-function)

# 15.11.2023
- [How to | Compute a Limit](https://reference.wolfram.com/language/howto/ComputeALimit.html)
- Полиномы, стартовая страница. [Algebraic Manipulation](https://reference.wolfram.com/language/tutorial/AlgebraicManipulation.html)
- Стартовая страница. [Manipulating Equations and Inequalities](https://reference.wolfram.com/language/tutorial/ManipulatingEquationsAndInequalities.html)


# 08.11.2023
## Немного аналитической геометрии
- [`FullSimplify` with assumptions](https://mathematica.stackexchange.com/questions/54931/fullsimplify-with-assumptions)
`... //FullSimplify[#, ...]&`
- Несколько различных способов решения. [Another way to write equation of the line passing through two points? {closed}](https://mathematica.stackexchange.com/questions/186285/another-way-to-write-equation-of-the-line-passing-through-two-points)
- [Triangle—Wolfram Language Documentation](https://reference.wolfram.com/language/ref/Triangle.html)
- [How to get a perpendicular segment inside of a triangle](https://mathematica.stackexchange.com/questions/124933/how-to-get-a-perpendicular-segment-inside-of-a-triangle)
- [Orthogonal vector in two dimensions](https://mathematica.stackexchange.com/questions/60739/orthogonal-vector-in-two-dimensions)
It's already built-in. It's called `Cross`.
```
Cross[{1, 2}]
```
- [Orthogonal Vectors](https://mathworld.wolfram.com/OrthogonalVectors.html)

# 11.10.2023
- [Решение линейных диофантовых уравнений с любым числом неизвестных](https://habr.com/ru/articles/330632/)

# 02.10.2023
- [`Rationalize`](https://reference.wolfram.com/language/ref/Rationalize.html?q=Rationalize) converts an approximate number x to a nearby rational with small denominator.

# 27.09.2023
- [Calculate the value of a number as if it were represented in binary](https://mathematica.stackexchange.com/questions/275304/calculate-the-value-of-a-number-as-if-it-were-represented-in-binary)
`BinaryToDecimal[num_] := FromDigits[RealDigits[num, 10], 2]`
- [Doing arithmetic with binary numbers](https://mathematica.stackexchange.com/questions/44908/doing-arithmetic-with-binary-numbers)
- [Представление чисел суммой двух квадратов и эллиптические кривые](https://habr.com/ru/articles/189618/)

# 22.09.2023
- [Rules](https://reference.wolfram.com/language/guide/Rules.html)
- [How to filter list of list of rules on certain condition?](https://mathematica.stackexchange.com/questions/86821/how-to-filter-list-of-list-of-rules-on-certain-condition)
- [Condition /;](https://reference.wolfram.com/language/ref/Condition.html)
- И вот, вразумительные ответы: [Constraints on Solve results](https://mathematica.stackexchange.com/questions/98525/constraints-on-solve-results/98527#98527)

https://beta.theb.ai/home 
PROMPT: `How to filter in Wolfram Mathematica from Solve function rules based on additional criteria`
PROMPT: `I have a function of two variables and want to filter Solve rules`
`Cases[solutions, {x -> n_ /; n > 0}]` подходит только для одного правила.
To filter out the solutions that do not satisfy the requirements, you can use the Select function with a function that returns True only for the solutions that satisfy all the requirements:
`Select[solutions, Function[{rule}, rule[[2]] > 0 && rule[[1, 2]]^2 + rule[[2, 2]]^2 \lt 1]]`
Но если попытать chatbot-а, то можно получить такой ответ:
`Cases[solutions, {x_ /; x > 2, y_ /; y \lt 6}]`, но так не работает!!!

# 19.09.2023
- Ищем коэффициенты при степенях полинома. 
	- [`Coefficient`](https://reference.wolfram.com/language/ref/Coefficient.html?q=Coefficient) gives the coefficient of form in the polynomial expr.
```
Coefficient[(x + y + z)^10, x^5 y^2 z^3]
CoefficientRules[(x + y + z)^10]
(x + y + z)^10 // Expand
```
	- [`CoefficientList`](https://reference.wolfram.com/language/ref/CoefficientList.html)
	- Много написано, надо разбираться: [Easiest way to extract the coefficient of a polynomial](https://mathematica.stackexchange.com/questions/115006/easiest-way-to-extract-the-coefficient-of-a-polynomial)
	- [Examples for Polynomials](https://www.wolframalpha.com/examples/mathematics/algebra/polynomials)
	- [Extracting coefficients from `g=a*x+b*y+c*x*y`](https://mathematica.stackexchange.com/questions/39088/extracting-coefficients-from-g-axbycxy)
	`{1, 0} /. CoefficientRules[g, {x, y}]`

# 18.09.2023
- [total differential for x*y/(x+y) - Wolfram|Alpha](https://www.wolframalpha.com/input?i=total+differential+for+x*y%2F%28x%2By%29)

# 30.08.2023
- [Векторный анализ и визуализация](https://www.wolfram.com/language/fast-introduction-for-math-students/ru/vector-analysis-and-visualization/). В Языке Wolfram n-мерные вектора представляются в виде списков длиной n.
Вычислим скалярное произведение двух векторов:
```
In[1]:=	{1, 2, 3}.{a, b, c}
Out[1]=	2 + 2b + 3c
```
- Решение в целых числах (диофантовы уравнения)
	- [Diophantine Equations](https://reference.wolfram.com/language/guide/DiophantineEquations.html)
	- [Getting actual integer solutions to an equation in Mathematica?](https://stackoverflow.com/questions/26411763/getting-actual-integer-solutions-to-an-equation-in-mathematica)
	I'm trying to solve an equation using Mathematica but I can't seem to get any actual answers.
`Solve[(5*d) + (216*b) == 1, {d, b}, Integers]`
	Solve gives you **the** solution. If you want **a** solution, change that to FindInstance:
`FindInstance[(5*d) + (216*b) == 1, {d, b}, Integers]`
which would be:
`{{d -> 173, b -> -4}}`
	- Нелинейный случай. [How to find integer solutions?](https://mathematica.stackexchange.com/questions/42359/how-to-find-integer-solutions)
	См. `Reduce`, `ToRules`

## Считаем площадь плоской фигуры
- [Triangle Area](https://mathworld.wolfram.com/TriangleArea.html)
- [Polygon Area](https://mathworld.wolfram.com/PolygonArea.html
- [Calculate area of a triangle](https://mathematica.stackexchange.com/questions/172871/calculate-area-of-a-triangle)
- [How do I calculate the area of a polygon given its coordinates?](https://mathematica.stackexchange.com/questions/31241/how-do-i-calculate-the-area-of-a-polygon-given-its-coordinates)
In version 10, many graphics primitives, including `Polygon`, can be treated as geometric regions. Use `RegionMeasure`:
```
poly=Polygon[{{0, 200 }, {200, 100}, {500, 300}, {100, 700}}];

RegionMeasure[poly]
(* 155000 *)
```
- [How do I calculate area in polygon from x and y points in R?](https://stackoverflow.com/questions/61975159/how-do-i-calculate-area-in-polygon-from-x-and-y-points-in-r)
- [Площадь простого многоульника](http://contester.ddns.is74.ru:82/gribennik/)

# 17.08.2023
- [Implement a recursive formula with internal sum](https://mathematica.stackexchange.com/questions/207288/implement-a-recursive-formula-with-internal-sum)
- [Examples for Recurrences](https://www.wolframalpha.com/examples/mathematics/discrete-mathematics/recurrences)

# 10.05.2023
- [Examples for Combinatorics](https://www.wolframalpha.com/examples/mathematics/discrete-mathematics/combinatorics/)
Combinatorics is a branch of mathematics dealing primarily with combinations, permutations and enumerations of elements of sets. It has practical applications ranging widely from studies of card games to studies of discrete structures. Wolfram|Alpha is well equipped for use analyzing counting problems of various kinds that are central to the field.
- Wolfram [Combinatorial Functions](https://reference.wolfram.com/language/guide/CombinatorialFunctions.html)
- [Permutations](https://reference.wolfram.com/language/guide/Permutations.html)
- [Combination](https://mathworld.wolfram.com/Combination.html). The number of combinations (n; k) can be computed in the Wolfram Language using Binomial[n, k], and the combinations themselves can be enumerated in the Wolfram Language using Subsets[Range[n],{k}].

# 27.04.2023
- Ищем обратные элементы в кольце вычетов.
	- [WolframAlpha](https://www.wolframalpha.com/input?i=5%5E-1+mod13)
	- Wolfram [ModularInverse](https://reference.wolfram.com/language/ref/ModularInverse.html)
	- Пример [виджета](https://planetcalc.ru/3311/)

# 26.04.2023
- COOL! [Where can I find examples of good Mathematica programming practice?](https://mathematica.stackexchange.com/questions/18/where-can-i-find-examples-of-good-mathematica-programming-practice)

# 25.04.2023
- [How to solve Mod equation with mathematica {closed}](https://mathematica.stackexchange.com/questions/71438/how-to-solve-mod-equation-with-mathematica)
- [Modulus](https://reference.wolfram.com/language/ref/Modulus.html). `Modulus -> n` is an option that can be given in certain algebraic functions to specify that integers should be treated modulo n.
- [Solving a system of linear equations modulo n](https://mathematica.stackexchange.com/questions/31696/solving-a-system-of-linear-equations-modulo-n)
Один из вариантов `Reduce[{a + b + c == 31, 4 a + 2 b + c == 3, 9 a + 3 b + c == 11}, {a, b, c},   Modulus -> 54]`
- Тут даже с интерактивом. [Linear Solve with Modular Arithmetic](https://mathematica.stackexchange.com/questions/11580/linear-solve-with-modular-arithmetic)
- [How to solve this system of Modular equations?](https://mathematica.stackexchange.com/questions/165523/how-to-solve-this-system-of-modular-equations)
- [Solving/Reducing equations in ℤ/𝑝ℤ](https://mathematica.stackexchange.com/questions/16001/solving-reducing-equations-in-mathbbz-p-mathbbz/16003#16003)
I was trying to find all the numbers 𝑛 for which  2𝑛=𝑛
Instead of solving it as a modular equation, convert it to an explicit Diophantine equation:
```
Solve[ 2^n - n - q 10^k == 0 && 1 <= k <= 3 && 0 <= n < If[ k == 1, 2, 1] 10^k,
       {k, n, q}, Integers]
```
- COOL! Масса примеров. [Equation Solving](https://www.wolframalpha.com/examples/EquationSolving-content.html)
- [Examples for Equation Solving](https://www.wolframalpha.com/examples/mathematics/algebra/equation-solving/)

### Systems of Congruences
- Solve a single congruence equation:
[solve 5x = 2 (mod 3)](https://www.wolframalpha.com/input/?i=solve+5x+%3D2+(mod+3)&lk=3)
- Solve systems of congruences:
[solve 2x = 10 (mod 12), 3x = 9 (mod 12)](https://www.wolframalpha.com/input/?i=solve+2x+%3D+10+(mod+12)%2C+3x+%3D+9+(mod+12)&lk=3)
- Check if values are equivalent under a given modulus:
(17 = 7 mod 10)[https://www.wolframalpha.com/input/?i=17+%3D+7+mod+10&lk=3]
- Solve a congruence involving variables in the modulus:
[solve 22 = 10 mod n](https://www.wolframalpha.com/input/?i=solve+22+%3D+10+mod+n&lk=3)
- Solve systems with each equation under a different modulus:
[x = 1 mod 2, x=3 mod 6, x=3 mod 7](https://www.wolframalpha.com/input/?i=x+%3D+1+mod+2%2C+x%3D3+mod+6%2C+x%3D3+mod+7&lk=3)
- Solve multivariate systems of congruences:
[x^2 = y^3 mod 2, x=3 mod 7, y=4 mod 7](https://www.wolframalpha.com/input/?i=x%5E2+%3D+y%5E3+mod+2%2C+x%3D3+mod+7%2C+y%3D4+mod+7&lk=3)

# 05.04.2023
- [Diophantine Equations](https://reference.wolfram.com/language/guide/DiophantineEquations.html)
- [FrobeniusSolve[{a1,…,an},b]](https://reference.wolfram.com/language/ref/FrobeniusSolve.html) gives a list of all solutions of the Frobenius equation .

# 31.03.2023
- [Function to view N-th digit of large number?](https://community.wolfram.com/groups/-/m/t/1700638)
`IntegerLength`, `9^(9^9) // IntegerDigits // Last`, `NumberDigit[x,n]` returns the digit corresponding to 10n in the real-valued number x.


# 09.01.2023
- [Polynomial Factoring & Decomposition](https://reference.wolfram.com/language/guide/PolynomialFactoring.html)
- [How to | Factor a Polynomial](https://reference.wolfram.com/language/howto/FactorAPolynomial.html)
- [Substituting a Value into an Expression](https://mathematica.stackexchange.com/questions/109127/substituting-a-value-into-an-expression)


# 30.12.2022
- [What is the simplest way to plot a decomposition tree in Mathematica?](https://stackoverflow.com/questions/5647268/what-is-the-simplest-way-to-plot-a-decomposition-tree-in-mathematica)
- [The inverse of moving from a map to a network topology](https://community.wolfram.com/groups/-/m/t/1358396?sortMsg=Flat)
- [Nested list to graph](https://mathematica.stackexchange.com/questions/43930/nested-list-to-graph)
- COOL! [Краеугольные камни уничтожения медленного кода в Wolfram Language: ускоряем код в десятки, сотни и тысячи раз](https://habr.com/ru/company/wolfram/blog/473220/)
- [Postfix with two arguments](https://mathematica.stackexchange.com/questions/56882/postfix-with-two-arguments)
- [Substituting a Value into an Expression](https://mathematica.stackexchange.com/questions/109127/substituting-a-value-into-an-expression)
`g /. y -> 1`
- [Preventing evaluation of Mathematica expressions](https://stackoverflow.com/questions/4856177/preventing-evaluation-of-mathematica-expressions)
- [Mathematica: Unevaluated vs Defer vs Hold vs HoldForm vs HoldAllComplete vs etc etc](https://stackoverflow.com/questions/1616592/mathematica-unevaluated-vs-defer-vs-hold-vs-holdform-vs-holdallcomplete-vs-etc)
- [How to invert Expand](https://mathematica.stackexchange.com/questions/211762/how-to-invert-expand). `HornerForm`
- [How to | Rearrange the Terms of a Polynomial](https://reference.wolfram.com/language/howto/RearrangeTheTermsOfAPolynomial.html)
- [TruncatedDistribution](https://reference.wolfram.com/language/ref/TruncatedDistribution.html)
- [Most Efficient Way to Calculate the Product of All Items in a List?](https://mathematica.stackexchange.com/questions/1352/most-efficient-way-to-calculate-the-product-of-all-items-in-a-list). `Apply[Times, list]`

# 25.08.2019
- [How to make use of Associations?](https://mathematica.stackexchange.com/questions/52393/how-to-make-use-of-associations)
- [Create a Dataset object, Association or SparesArray from a matrix {closed}](https://mathematica.stackexchange.com/questions/114081/create-a-dataset-object-association-or-sparesarray-from-a-matrix)
- [Does anybody know the meaning of the operator & /@?](https://community.wolfram.com/groups/-/m/t/132905?sortMsg=Flat)
- [Convert association to Matrix / List](https://mathematica.stackexchange.com/questions/176895/convert-association-to-matrix-list)
- [Changing Values in an Association using Map](https://mathematica.stackexchange.com/questions/55494/changing-values-in-an-association-using-map?rq=1)
- [How can I add a column into a existing Dataset?](https://mathematica.stackexchange.com/questions/51472/how-can-i-add-a-column-into-a-existing-dataset/51473#51473)
- [Pattern Matching with Associations](https://www.wolfram.com/language/11/core-language/pattern-matching-with-associations.html)
- [An Elementary Introduction to the Wolfram Language. 45. Datasets](https://www.wolfram.com/language/elementary-introduction/2nd-ed/45-datasets.html)
- [Select Elements in a Dataset](https://reference.wolfram.com/language/workflow/SelectElementsInADataset.html)
- [Assigning new value in association](https://mathematica.stackexchange.com/questions/72747/assigning-new-value-in-association)
- [«Игра престолов»: строим инфографику об убийствах, сексе, путешествиях по Вестеросу и многое другое](https://habr.com/ru/company/wolfram/blog/451640/)
- [Log Normal Distribution](http://mathworld.wolfram.com/LogNormalDistribution.html)

