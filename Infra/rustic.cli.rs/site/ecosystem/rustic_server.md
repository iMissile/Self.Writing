+++
title = "rustic_server"
description = "rustic server"
weight = 1
in_search_index = true
+++

<p>
<img class="content-logo" src="https://raw.githubusercontent.com/rustic-rs/assets/main/logos/readme_header_server.png" />
</p>
<p><b>REST server for rustic</b></p>

<!-- <p>
<a href="https://crates.io/crates/rustic-rs"><img src="https://img.shields.io/crates/v/rustic-rs.svg" /></a>
<a href="https://docs.rs/rustic-rs/"><img src="https://img.shields.io/docsrs/rustic-rs?style=flat&amp;labelColor=1c1d42&amp;color=4f396a&amp;logo=Rust&amp;logoColor=white" /></a>
<a href="https://raw.githubusercontent.com/rustic-rs/rustic/main/"><img src="https://img.shields.io/badge/license-Apache2.0/MIT-blue.svg" /></a>
<a href="https://crates.io/crates/rustic-rs"><img src="https://img.shields.io/crates/d/rustic-rs.svg" /></a>
<p> -->

<p>
<a href="https://github.com/rustic-rs/rustic_server/actions/workflows/nightly.yml"><img src="https://github.com/rustic-rs/rustic_server/actions/workflows/nightly.yml/badge.svg" /></a>
<a href="https://www.gnu.org/licenses/agpl.txt"><img src="https://www.gnu.org/graphics/agplv3-88x31.png" height="20"/></a>
</p>

# About

A REST server built in rust for use with rustic and restic.

Works pretty similar to [rest-server](https://github.com/restic/rest-server).
Most features are already implemented.

# Installation

## From binaries

_rustic-server_ is in an early development stage. Please use the nightly builds from [here](https://rustic.cli.rs/docs/nightly_builds.html).

# Features

Allows to give ACLs im TOML format, use option `--acl`

Example TOML file:

```toml
# default sets ACL for the repo without explicit path
# (and for the repo under path "default", if exists)
[default]
alex = "Read"
admin = "Modify"

[alex]
alex = "Modify"
bob = "Append"
```

# License

`rustic-server` is open-sourced software licensed under the
[GNU Affero General Public License v3.0 or later](https://raw.githubusercontent.com/rustic-rs/rustic_server/main/LICENSE).
