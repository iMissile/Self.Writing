# 09.01.2023
- [ANTLR4 parser generator runtime for Rust programming laguage](https://github.com/rrevenantt/antlr4rust)
- [Polars](https://www.pola.rs/). Lightning-fast DataFrame library for Rust and Python
- [Machine Learning and Rust (Part 3): Smartcore, Dataframe, and Linear Regression](https://levelup.gitconnected.com/machine-learning-and-rust-part-3-smartcore-dataframe-and-linear-regression-10451fdc2e60)

# 06.01.2023
- [How check type of variable](https://users.rust-lang.org/t/how-check-type-of-variable/33845)
	- Also, you can use an IDE for this. A free solution that works exceptionally well is VSCode + rust-analyzer
- [Get Type Name of Variables in Rust](http://www.legendu.net/misc/blog/get-type-name-of-variables-in-rust/).
	- Tips & Traps
```#![feature(type_name_of_val)]
use std::any::type_name_of_val;

let x = 1;
println!("{}", type_name_of_val(&x));
let y = 1.0;
println!("{}", type_name_of_val(&y));
```
	- Use the typename crate. [typename v0.1.2](https://crates.io/crates/typename). Stable alternative to Rust's type_name intrinsic.
	Однако! DEPRECATION NOTICE: This crate has been deprecated. The `type_name` intrinsic has been stablized in Rust 1.38. Users of this crate are asked to migrate to `std::any::type_name`.
	- [Tracking issue for any::type_name_of_val #66359 {Open}](https://github.com/rust-lang/rust/issues/66359)