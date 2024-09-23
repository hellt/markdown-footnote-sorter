# Contributing

🎉 Thank you for your interest in contributing to this project! 🎉

A couple of quick items:

1. To avoid duplicate issues and PRs, [please search open issue and pull requests](https://docs.github.com/en/issues/tracking-your-work-with-issues/filtering-and-searching-issues-and-pull-requests) before submitting a new one.
1. The general expectation is to [submit a GitHub issue](https://help.github.com/en/github/managing-your-work-on-github/creating-an-issue) to receive feedback before submitting a pull request (PR) with changes.
    * _This will help ensure ideas align with the project scope._
1. Unit tests should accompany [Pull Requests (PRs)](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests) **whenever possible**. :point_left:
    * This could mean adding additional tests to an existing unit test file or creating a new one.

## Ways to Contribute

(in no particular order)

* Code
* Documentation
* Expanding Unit Test coverage (where needed)
* Helping others (ex: with [issue tickets](https://github.com/hellt/markdown-footnote-sorter/issues))

## Testing Framework

For minimal dependencies, the "batteries included" [Python `unittest` framework](https://docs.python.org/3/library/unittest.html) is utilized. (Other testing frameworks could be considered should additional testing features be needed.)

## Development Process
>
> This section consists of suggestions.

It is recommended to verify tests are successful before making any code changes. From there make your changes and run the unit tests to validate there is not code regression.

* [Create a fork of this project](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo)
  * If you have an existing fork of this project be sure [to synchronize it](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/syncing-a-fork)!
* From the `main` branch of your fork, [create a feature branch](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-and-deleting-branches-within-your-repository)
* Validate [test cases run successfully](#running-unit-tests) before any changes are made
* Make modifications
* Re-test with the existing unit tests against the modified codebase
* Add any additional unit tests to improve testing coverage
* Re-run the unit tests to confirm they run successfully
* When you are satisfied with the changes and it is ready for review, [submit a Pull Request (PR)](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request)

## Running Unit Tests

Choose one of the below testing commands methods that suits your needs.

> [!IMPORTANT]
> The commands below are to be run from the top level of the project.

1. Discover and run unit tests
    * `python -m unittest discover`

1. Verbose version of unit test discovery
    * `python -m unittest discover -v`

1. Discover unit tests in specific directory (in this case, `tests`) with verbosity
    * `python -m unittest discover -s tests -v`

💡 For additional `unittest` command line options, refer to the [official Python unittest documentation](https://docs.python.org/3/library/unittest.html#command-line-interface).
