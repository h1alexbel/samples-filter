# samples-filter

[![EO principles respected here](https://www.elegantobjects.org/badge.svg)](https://www.elegantobjects.org)
[![DevOps By Rultor.com](http://www.rultor.com/b/h1alexbel/samples-filter)](http://www.rultor.com/p/h1alexbel/samples-filter)
[![We recommend IntelliJ IDEA](https://www.elegantobjects.org/intellij-idea.svg)](https://www.jetbrains.com/idea/)

[![py](https://github.com/h1alexbel/samples-filter/actions/workflows/py.yml/badge.svg)](https://github.com/h1alexbel/samples-filter/actions/workflows/py.yml)
[![PyPI - Version](https://img.shields.io/pypi/v/samples-filter)](https://pypi.org/project/samples-filter)
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

**Motivation**. During work on [cam](https://github.com/yegor256/cam) project,
where we're building datasets with open source Java programs,
we [discovered](https://github.com/yegor256/cam/issues/227)
the need for filtering repositories that contain
not a real code, but rather samples, tutorials or examples.
This repository is portable command-line tool that filters those
sample repositories.

## How to use

TBD..

## Filtering method

We take the input in the format of `repositories.csv`:

```csv
full_name,default_branch,stars,forks,created_at,size,open_issues_count,description,topics
heysupratim/material-daterange-picker,master,1328,269,2015-09-14T12:00:47Z,868,14,"A material Date Range Picker based on wdullaers MaterialDateTimePicker","["datepicker", "datetimepicker", "material", "picker", "range-selection", "timepicker"]"
Jude95/EasyRecyclerView,master,2029,458,2015-07-18T13:11:48Z,11336,110,"ArrayAdapter,pull to refresh,auto load more,Header/Footer,EmptyView,ProgressView,ErrorView","[]"
hanks-zyh/SmallBang,master,1005,158,2015-12-24T14:48:37Z,6379,6,"  twitter like animation for any view :heartbeat:","["animation", "heartbeat", "like-button", "twitter"]"
Gavin-ZYX/StickyDecoration,master,1033,165,2017-05-31T07:38:49Z,1018,3,"","[]"
...
```

?: format csv to Markdown

Then, for each repo in the dataset we fetch it's `README.md` file.
Then we extract `full_name`, `description`, `topics` columns' values from
dataset. At this point we TBD..

## How to contribute

Fork repository, make changes, send us a [pull request](https://www.yegor256.com/2014/04/15/github-guidelines.html).
We will review your changes and apply them to the `master` branch shortly,
provided they don't violate our quality standards. To avoid frustration,
before sending us your pull request please run full build:

```bash
..
```

To set up virtual environment use this set of commands:

```bash
python3 -m venv $(pwd)
source $(pwd)/venv/bin/activate
```

You will need [Python 3.9+](https://www.python.org/downloads/release/python-390)
and [pip](https://pypi.org/project/pip) installed.
