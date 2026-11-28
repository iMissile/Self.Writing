+++
title = "rustic_scheduler"
description = "rustic scheduler"
weight = 1
in_search_index = true
+++

<p>
<img class="content-logo" src="https://raw.githubusercontent.com/rustic-rs/assets/main/logos/readme_header_scheduler.png" />
</p>
<p><b>centrally schedule rustic backups</b></p>

<!-- <p>
<a href="https://crates.io/crates/rustic-rs"><img src="https://img.shields.io/crates/v/rustic-rs.svg" /></a>
<a href="https://docs.rs/rustic-rs/"><img src="https://img.shields.io/docsrs/rustic-rs?style=flat&amp;labelColor=1c1d42&amp;color=4f396a&amp;logo=Rust&amp;logoColor=white" /></a>
<a href="https://raw.githubusercontent.com/rustic-rs/rustic/main/"><img src="https://img.shields.io/badge/license-Apache2.0/MIT-blue.svg" /></a>
<a href="https://crates.io/crates/rustic-rs"><img src="https://img.shields.io/crates/d/rustic-rs.svg" /></a>
<p> -->

<p>
<a href="https://github.com/rustic-rs/rustic_scheduler/actions/workflows/nightly.yml"><img src="https://github.com/rustic-rs/rustic_scheduler/actions/workflows/nightly.yml/badge.svg" /></a>
</p>

# About

_rustic scheduler_ is a client/server application to schedule regular backups on
many clients to one identical repository controlled by a central scheduling
server.

It allows to define client groups which are all backed up the same way.

**Note**: _rustic scheduler_ is in an early development stage.

# Installation

## From binaries

_rustic-scheduler_ is in an early development stage. Please use the nightly builds from [here](https://rustic.cli.rs/docs/nightly_builds.html).

# Getting started

- Copy the _rustic-scheduler-server_ binary to your backup schedule server and
  the _rustic-scheduler-client_ binary to all your clients.
- Create a config file [rustic_schedulder.toml](https://raw.githubusercontent.com/rustic-rs/rustic_scheduler/main/config/rustic_scheduler.toml) on your backup schedule server.
- Run the _rustic-scheduler-server_ binary on your server in the dir containing
  the config.
- On each client, run

  ```
  rustic-scheduler-client <ADDR>
  ```

  where `<ADDR>` is the
  websocket address to connect, e.g.

  ```
  rustic-scheduler-client http://server.localdomain:3012/ws
  ```

- Backups on your clients are automatically started based on the configured
  schedule(s).

# License

Licensed under either of:

- [Apache License, Version 2.0](https://raw.githubusercontent.com/rustic-rs/rustic_scheduler/main/LICENSE-APACHE)
- [MIT license](https://raw.githubusercontent.com/rustic-rs/rustic_scheduler/main/LICENSE-MIT)

at your option.
