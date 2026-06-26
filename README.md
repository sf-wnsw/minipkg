# minipkg

[![ci](https://github.com/sf-wnsw/minipkg/workflows/ci/badge.svg)](https://github.com/sf-wnsw/minipkg/actions?query=workflow%3Aci)
[![documentation](https://img.shields.io/badge/docs-zensical-FF9100.svg?style=flat)](https://sf-wnsw.github.io/minipkg/)
[![pypi version](https://img.shields.io/pypi/v/minipkg.svg)](https://pypi.org/project/minipkg/)
[![gitter](https://img.shields.io/badge/matrix-chat-4DB798.svg?style=flat)](https://app.gitter.im/#/room/#minipkg:gitter.im)

Minimal packaging example with uv and pyproject.toml

## Installation

This is a template, or rather an example, for developers, not an end user product.  

This package was created from the template [copier-uv](https://pawamoy.github.io/copier-uv) which comes with opinionated aspects for the workflow of a package development. While opinionated for a good reason, the water mark is high to comply with expectations in terms of unit tests, syntax, etc.

This repository will gradually strip down some aspects to a lightweight template, while keeping the packaging working.

We will probably assume we keep [`uv`](https://docs.astral.sh/uv/) to at least build the package.

## Stripping things out successively

Various upcoming commits will strip down the following items, a priori. We will commit at changes that still build what remains.

- publishing to pypi
- generation of HTML documentation
- various code quality checks
- unit tests
- versioning and changelog

### Starting point

`minipkg` is actually available on pypi, but we do not want to polute pypi with spurious or idiosyncratic packages. `make release` would currently (with my pypi secret keys) create such an entry, so will not test this.

`make check` does not pass yet, but probably because the git repo is new and without a remote/history. The subsets:

* `make check-docs` pass
* `make check-quality` pass
* `make check-types` pass
* `make docs` pass

`make test` pass, but only if I do `make run zensical build --clean` first.

