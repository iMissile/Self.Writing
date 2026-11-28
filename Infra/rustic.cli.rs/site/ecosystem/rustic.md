+++
title = "rustic"
description = "rustic"
weight = 1
in_search_index = true
+++

![rustic logo](https://raw.githubusercontent.com/rustic-rs/assets/main/logos/readme_header.png)

fast, encrypted, and deduplicated backups

<p>
<a href="https://crates.io/crates/rustic-rs"><img src="https://img.shields.io/crates/v/rustic-rs.svg" /></a>
<a href="https://docs.rs/rustic-rs/"><img src="https://img.shields.io/docsrs/rustic-rs?style=flat&amp;labelColor=1c1d42&amp;color=4f396a&amp;logo=Rust&amp;logoColor=white" /></a>
<a href="https://raw.githubusercontent.com/rustic-rs/rustic/main/"><img src="https://img.shields.io/badge/license-Apache2.0/MIT-blue.svg" /></a>
<a href="https://crates.io/crates/rustic-rs"><img src="https://img.shields.io/crates/d/rustic-rs.svg" /></a>
<a href="https://github.com/rustic-rs/rustic/actions/workflows/nightly.yml"><img src="https://github.com/rustic-rs/rustic/actions/workflows/nightly.yml/badge.svg" /></a>
<p>

# About

_rustic_ is a backup tool that provides fast, encrypted, deduplicated backups.

It reads and writes the [restic][1] repo format described in the
[design document][2] and can be used as a _restic_ replacement in most cases.

It is implemented in [Rust](https://www.rust-lang.org/), a performant,
memory-efficient, and reliable cross-platform systems programming language.

Hence _rustic_ supports all major operating systems (Linux, MacOs, *BSD), with
Windows support still being experimental.

# Features

- Backup data is **deduplicated** and **encrypted**.
- Backup storage can be local or cloud storages, including cold storages.
- Allows multiple clients to **concurrently** access a backup repository using
  lock-free operations.
- Backups by default are append-only on the repository.
- The operations are robustly designed and can be **safely aborted** and
  **efficiently resumed**.
- Snapshot organization is possible by hostname, backup paths, label and tags.
  Also a rich set of metadata is saved with each snapshot.
- Retention policies and cleaning of old backups can be **highly customized**.
- Follow-up backups only process changed files, but still create a complete
  backup snapshot.
- In-place restore only modifies files which are changed.
- Uses config files for easy configuration of all every-day commands, see
  [example config files](https://github.com/rustic-rs/rustic/tree/main/config).

# Differences to _restic_

We have collected some improvements of _rustic_ over _restic_
[here](https://rustic.cli.rs/docs/comparison-restic.html).

# Installation

## From binaries

### [cargo-binstall](https://crates.io/crates/cargo-binstall)

```bash
cargo binstall rustic-rs
```

### Windows

#### [Scoop](https://scoop.sh/)

```bash
scoop install rustic
```

Or you can check out the
[releases](https://github.com/rustic-rs/rustic/releases).

Nightly binaries are available
[here](https://rustic.cli.rs/docs/nightly_builds.html).

## From source

**Beware**: This installs the latest development version, which might be
unstable.

```bash
cargo install --git https://github.com/rustic-rs/rustic.git rustic-rs
```

### crates.io

```bash
cargo install rustic-rs
```

# Getting started

Please check our
[documentation](https://rustic.cli.rs/docs/getting_started.html) for more
information on how to get started.

# Minimum Rust version policy

This crate's minimum supported `rustc` version is `1.70.0`.

The current policy is that the minimum Rust version required to use this crate
can be increased in minor version updates. For example, if `crate 1.0` requires
Rust 1.20.0, then `crate 1.0.z` for all values of `z` will also require Rust
1.20.0 or newer. However, `crate 1.y` for `y > 0` may require a newer minimum
version of Rust.

In general, this crate will be conservative with respect to the minimum
supported version of Rust.

# License

Licensed under either of:

- [Apache License, Version 2.0](https://raw.githubusercontent.com/rustic-rs/rustic/main/LICENSE-APACHE)
- [MIT license](https://raw.githubusercontent.com/rustic-rs/rustic/main/LICENSE-MIT)

at your option.

[1]: https://github.com/restic/restic
[2]: https://github.com/restic/restic/blob/master/doc/design.rst
