# Contributing

:tada: Thank you for your interest in contributing to this project! :tada:

A couple of quick items:

1. To avoid duplicate issues and PRs, [please search open issue and pull requests](https://docs.github.com/en/issues/tracking-your-work-with-issues/filtering-and-searching-issues-and-pull-requests)
   before submitting a new one.

1. The general expectation is to [submit a GitHub issue](https://help.github.com/en/github/managing-your-work-on-github/creating-an-issue)
   to receive feedback before submitting a pull request (PR) with changes.

    * _This will help ensure ideas align with the project scope._

1. Unit tests should accompany [Pull Requests (PRs)](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests)
   **whenever possible**. :point_left:

    * This could mean adding additional tests to an existing unit test file or
      creating a new one.

## Ways to Contribute

(in no particular order)

* Code
* Documentation
* Expanding Unit Test coverage (where needed)
* Helping others (ex: with [issue tickets](https://github.com/hellt/markdown-footnote-sorter/issues))

## Testing Framework

For minimal dependencies, the "batteries included" [Python `unittest` framework](https://docs.python.org/3/library/unittest.html)
is utilized. (Other testing frameworks could be considered should additional
testing features be needed.)

Testing can be invoked via [`make test` (more information below)](#run-python-unit-tests)

## Development Requirements

* Python 3
* GNU Make
* Docker (Engine)

> [!IMPORTANT]
> If your development workstation has a security access control (ex: SELinux)
> enabled, you will need to put it in a permissive mode for the Docker bind
> mounts to function.

## Development Process

> This section consists of suggestions.

It is recommended to verify tests are successful before making any code changes.
From there make your changes and run the unit tests to validate there is not
code regression.

1. [Create a fork of this project](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo)

    * If you have an existing fork of this project be sure [to synchronize it](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/syncing-a-fork)!

1. From the `main` branch of your fork, [create a feature branch](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-and-deleting-branches-within-your-repository)

1. Validate [test cases run successfully](#run-python-unit-tests) before any
  changes are made

1. Verify [linting and formatting checks run successfully](#run-all-linters-in-one-shot)
  before making any changes

1. Make modifications

1. Re-test with the existing unit tests against the modified codebase

1. Add any additional unit tests to improve testing coverage

1. Re-run the unit tests to confirm they run successfully

1. Re-run linting and formatting checks

1. Fix up any linting or formatting errors

1. When you are satisfied with the changes and it is ready for review,
  [submit a Pull Request (PR)](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request)

## Using `make` to streamline linting and testing

This project uses GNU `make` to simplify the action of interacting with several
linters and performing unit testing.
Project dependencies and Python virtual environment are managed with `uv`.

## Prequisites

* Install GNU [`make`](https://www.gnu.org/software/make/) for your operating
  system
* Install Docker (Engine)

## General

### Default (all)

* lint and test

```bash
make all

# or simply
make
```

### Clean

* Removes the Docker images this Makefile utilizes

`make clean`

## Linting

### Run all linters in one shot

`make lint`

### Run markdownlint-cli2 for Markdown linting

`make mdlint`

### Run ruff for Python linting

`make ruff`

### Run yamllint for Markdown linting

`make yamllint`

## Testing

### Run Python unit tests

`make test`

## But I want to run linting locally

> [!NOTE]
> This project uses Docker images to avoid shipping or depending on other
> projects, package managers, or languages (Node.js, Ruby).
>
> Non-Dockerized local testing is not supported by the repo owner.
>
> There are extra `make` targets in the Makefile in case you'd prefer local
> linting and formatting.

* Install GNU Make (same requirement as the main development pattern)
* [Install `uv` for Python package management](https://docs.astral.sh/uv/#getting-started)
* Install `npm` for Node.js package management

```bash
make localclean
make localinit
make localmdl
make localruff
make localyaml
```

## Running Unit Tests Manually

> [!NOTE]
> This information is somewhat historical since incorporating the Makefile,
> but could prove useful.

Choose one of the below testing command options that suits your needs.

> [!IMPORTANT]
> The commands below are to be run from the top level of the project.

1. Discover and run unit tests

    * `python -m unittest discover`

1. Verbose version of unit test discovery

    * `python -m unittest discover -v`

1. Discover unit tests in specific directory (in this case, `tests`) with verbosity

    * `python -m unittest discover -s tests -v`

:bulb: For additional `unittest` command line options, refer to the
[official Python unittest documentation](https://docs.python.org/3/library/unittest.html#command-line-interface).
