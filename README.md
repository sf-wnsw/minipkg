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

After pushing the repo to [sf-wnsw/minipkg](https://github.com/sf-wnsw/minipkg), the CI workflow run. The release workflow is skipped, perhaps a good thing but not sure why anymore. I always release from my machine. 

The main CI takes a [bit of time to run](https://github.com/sf-wnsw/minipkg/actions/runs/28218942794), but this is because the default `ci.yml` file covers quite a matrix of versions and OS-es to run on. I typically pair it back to a subset in practice, uless I have very good reasons to check various versions. Note to self: pandas/numpy versions...

I thought the `make` commands were mostly working on Unix systems, but the CI log suggests this works fine on windows, which I never tried first hand.

At this point the docs are not yet deployed as a HTML github pages site. `make docs` runs fine with:

```text
Serving /home/per202/src/minipkg/site on http://127.0.0.1:8000
Build started
No issues found
```

and is browsable.

`. .venv/bin/activate` then `uv pip list | less` confirms that `make setup` has installed the package in the locale env in "debug" mode:

```text
minipkg             0.1.dev2+g38cd3c7 /home/xxxxxx/src/minipkg
```

#### Version

A neat if opinionated feature is the automatic version numbering and changelog management. We have changed a few things, let's uptick the version/changelog.
