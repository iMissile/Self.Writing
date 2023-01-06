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
	- Use the typename crate. [typename v0.1.2](https://crates.io/crates/typename). Stable alternative to Rust's type_name intrinsic