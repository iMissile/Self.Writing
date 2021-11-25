

# IDE
- [Julia lang](https://julialang.org/downloads/)
- [Juno IDE](http://docs.junolab.org/latest/man/installation/#Installation-Instructions)
- [Atom Editor](https://atom.io/)
- [Julia can not start inside Atom](https://discourse.julialang.org/t/julia-can-not-start-inside-atom/18923)

## Julia
- [Is Julia Really Fast?](https://medium.com/codex/is-julia-really-fast-12cd7caef96b) An overview of what you can and cannot expect from Julia performance. A guide to the fence sitters pondering whether to use Julia for high performance computing.
	- [ACCU 2020 SCHEDULE](https://accu.org/conf-previous/2021/schedule/)
- Exit Julia Terminal. Press `Ctrl + D`
- [Pluto's built-in package management](https://github.com/fonsp/Pluto.jl/wiki/%F0%9F%8E%81-Package-management)

## articles
- [Number one JuliaLang beginner tip: Do not delay the active learning](https://juliaifrank.com/active-learning-in-programming/)
- [Simple multi-layer perceptron](https://fluxml.ai/tutorials/2021/01/26/mlp.html)


# 23.11.2021
- [Julia: A Fresh Approach to Computing](https://computationalthinking.mit.edu/Spring21/)
This class uses revolutionary programmable interactivity to combine material from three fields creating an engaging, efficient learning solution to prepare students to be sophisticated and intuitive thinkers, programmers, and solution providers for the modern interconnected online world.
Three fields, one courseю Computer Science; Mathematics; Applications

# 09.11.2021
## Graph
- [JuliaGraphs - Graph analysis in Julia](https://juliagraphs.org/)

# 06.11.2021
- [The JuliaConnectoR. A Functionally Oriented Interface for Integrating Julia in R](https://arxiv.org/ftp/arxiv/papers/2005/2005.06334.pdf)
- [stefan-m-lenz/JuliaConnectoR](https://github.com/stefan-m-lenz/JuliaConnectoR). A functionally oriented interface for calling Julia from R
- [Julia beginner's corner: mastering comparison operators](https://bkamins.github.io/julialang/2021/10/08/comparisons.html). Oct 8, 2021
- [Tutorial on precompilation](https://julialang.org/blog/2021/01/precompile_tutorial/). 5 January 2021 | Tim Holy
- Performance Tips. [Be aware of when Julia avoids specializing](https://docs.julialang.org/en/v1/manual/performance-tips/#Be-aware-of-when-Julia-avoids-specializing)

# 31.10.2021
Нашел в телеграм канале массу ссылок
What should I read in order to / Что мне почитать, чтобы:


1. Understand basics of Julia / Понять основы языка Julia ?
	1.1 ThinkJulia: https://benlauwens.github.io/ThinkJulia.jl/latest/book.html
	1.2 QuantEcon parts: https://julia.quantecon.org/
	1.3 Zero2Hero Julia: https://www.youtube.com/watch?v=Fi7Pf2NveH0
	1.4 Julia wiki: https://en.wikibooks.org/wiki/Introducing_Julia
	1.5 From zero to Julia: https://techytok.com/from-zero-to-julia/
	1.6 Jane Herriman intro to Julia: https://www.youtube.com/watch?v=8h8rQyEpiZA
	1.7  Introduction to Computational Thinking with Julia, with applications to modelling the COVID-19 pandemic: https://github.com/mitmath/6S083
2. Understand Julia more deeply / Лучше понять некоторые тонкие аспекты Julia?
	2.1 Chris Rachauckas tutorial: https://ucidatascienceinitiative.github.io/IntroToJulia/
	2.2 Tom Kwong. Hands-on Design Patterns and Best Practices with Julia. 
	2.3 Malcolm Sherrington. Mastering Julia.
	2.4 Julia workshop 2019 (Finland): https://github.com/crstnbr/JuliaOulu20
	2.5 D.P.Sanders workshop: https://github.com/dpsanders/hands_on_julia
	2.6 Metaprogramming workshop: https://youtu.be/SeqAQHKLNj4
3. Learn some applications to specific branches of mathematics / Узнать больше о
приложениях к некоторым областям математики?
	3.1 Linear algebra / Линейная алгебра:
		3.1.1 Introduction to applied linear algebra: vectors, matrices and least squares http://vmls-book.stanford.edu/
		3.1.2 Folkmar Bornemann: Numerical Linear Algebra. A Concise Introduction  with MATLAB and Julia
		3.1.3 MODERN APPLICATIONS OF NUMERICAL LINEAR ALGEBRA METHODS: https://github.com/ivanslapnicar/GIAN-Applied-NLA-Course
	3.2 Differential equations, dynamical systems / Дифуры и динамич. системы:
		3.2.1 DynamicalSystems.jl tutorial: https://www.youtube.com/watch?v=13hqE_1a158
		3.2.2 DifferentialEquations tutorial: https://www.youtube.com/watch?v=13hqE_1a158
		3.2.3 Partial Differential Equations tutorial: https://www.youtube.com/watch?v=13hqE_1a158
	3.3 Optimization / Оптимизация:
		3.3.1 Kochenderfer, Wheeler : Algorithms for Optimization
		3.3.2 Kwong: Julia Programming for Operations Research, 2nd Edition
	3.4 Data science / Наука о данных:
		3.4.1 Data science workshop: https://youtu.be/SLE0vz85Rqo
		3.4.2 Queryverse workshop: https://www.youtube.com/watch?v=OFPNph-WxLM
	3.5 Statistics, bayesian, etc / Статистика, байесовский подход и др.:
		3.5.1 Statistics with julia: https://github.com/h-Klok/StatsWithJuliaBook
		3.5.2 Turing language tutorials: https://turing.ml/dev/tutorials/
		3.5.3 Statistical rethinking in Julia: https://github.com/StatisticalRethinkingJulia/StatisticalRethinking.jl
	3.6 Calculus, symbolic computations, ... / Анализ, символьные вычисления:
		3.6.1 Calculus with julia : http://calculuswithjulia.github.io/
4. Ecosystem, packages, etc / Экосистема, пакеты и иное:
	4.1 How to write a package (Rackauckas) https://youtu.be/QVmU29rCjaA
	4.2 How to install https://youtu.be/oyx8M1yoboY

# 30.08.2021
- [How to upgrade Julia to a new release?](https://newbedev.com/how-to-upgrade-julia-to-a-new-release)
```
julia> using Pkg # Pkg.init() if needed
copy REQUIRE file from package directory of the old version to the new one (in this example from .julia/v0.5 to .julia/v0.6) overwriting the existing file
julia> Pkg.resolve() # or Pkg.update()
```
- [Pkg](https://docs.julialang.org/en/v1/stdlib/Pkg/) is Julia's builtin package manager, and handles operations such as installing, updating and removing packages.
- [Welcome to the documentation for Pkg, Julia's package manager.](https://pkgdocs.julialang.org/v1/)

# 13.08.2021
## Julia
- [Benchmarking push! in DataFrames.jl](https://bkamins.github.io/julialang/2021/06/25/push.html)

# 19.07.2021
## Julia
- COOL! [JuliaCall: Integrating R and Julia](https://hwborchers.github.io/)
- [FIRST IMPRESSIONS OF JULIA FROM AN R USER](https://mdneuzerling.com/post/first-impressions-of-julia-from-an-r-user/)
- [Pluto's built-in package management](https://github.com/fonsp/Pluto.jl/wiki/%F0%9F%8E%81-Package-management)

