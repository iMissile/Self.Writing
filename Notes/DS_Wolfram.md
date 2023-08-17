
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
[solve 5x =2 (mod 3)](https://www.wolframalpha.com/input/?i=solve+5x+%3D2+(mod+3)&lk=3)
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

