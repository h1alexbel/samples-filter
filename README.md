# samples-filter

[![EO principles respected here](https://www.elegantobjects.org/badge.svg)](https://www.elegantobjects.org)
[![DevOps By Rultor.com](http://www.rultor.com/b/h1alexbel/samples-filter)](http://www.rultor.com/p/h1alexbel/samples-filter)
[![We recommend IntelliJ IDEA](https://www.elegantobjects.org/intellij-idea.svg)](https://www.jetbrains.com/idea/)

[![py](https://github.com/h1alexbel/samples-filter/actions/workflows/py.yml/badge.svg)](https://github.com/h1alexbel/samples-filter/actions/workflows/py.yml)
[![PyPI - Version](https://img.shields.io/pypi/v/samples-filter)](https://pypi.org/project/samples-filter)
[![codecov](https://codecov.io/gh/h1alexbel/samples-filter/graph/badge.svg?token=lVkWRVIqfE)](https://codecov.io/gh/h1alexbel/samples-filter)
[![PDD status](http://www.0pdd.com/svg?name=h1alexbel/samples-filter)](http://www.0pdd.com/p?name=h1alexbel/samples-filter)
[![Hits-of-Code](https://hitsofcode.com/github/h1alexbel/samples-filter)](https://hitsofcode.com/view/github/h1alexbel/samples-filter)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/h1alexbel/samples-filter/blob/master/LICENSE.txt)
[![Known Vulnerabilities](https://snyk.io/test/github/h1alexbel/samples-filter/badge.svg)](https://snyk.io/test/github/h1alexbel/samples-filter)

Samples-filter is a command-line filter
for GitHub repositories that contain `samples`,
instead of real project or framework or library.
E.g. [leeowenowen/rxjava-examples](https://github.com/leeowenowen/rxjava-examples),
[streaming-with-flink/examples-java](https://github.com/streaming-with-flink/examples-java),
[redisson/redisson-examples](https://github.com/redisson/redisson-examples).

**Motivation**. During the work on [CaM] project,
where we're building datasets with open source Java programs,
we [discovered](https://github.com/yegor256/cam/issues/227)
the need for filtering repositories that contain
not a real code, but rather samples, tutorials or examples.
This repository is portable command-line tool that filters those
sample repositories.

## How to use

First, install it from [PyPI](https://pypi.org/project/samples-filter) like that:

```bash
pip install samples-filter
```

then, execute:

```bash
samples-filter filter --repositories=repos.csv --out=filtered.csv
```

For `--repositories` you should provide a name of **existing** [CSV] dataset
with GitHub repositories, and name for the output file in `--out`
(it will be created automatically). If you feel missed, try `--help` and tool
will explain to you what you should do.

Optionally, you can decide which [model](/model/README.md) to use for
filtering via `--model`. You can pass either `rf` (the default one), or
`transformer`.

## How to contribute

Fork repository, make changes, send us a [pull request](https://www.yegor256.com/2014/04/15/github-guidelines.html).
We will review your changes and apply them to the `master` branch shortly,
provided they don't violate our quality standards. To avoid frustration,
before sending us your pull request please run full build:

```bash
make install cov check
```

To set up virtual environment use this set of commands:

```bash
python3 -m venv venv
source $(pwd)/venv/bin/activate
```

You will need [Python 3.11+]
installed.

[CaM]: https://github.com/yegor256/cam
[CSV]: https://en.wikipedia.org/wiki/Comma-separated_values
[Python 3.11+]: https://www.python.org/downloads/release/python-3110
