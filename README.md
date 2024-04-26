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

**Motivation**. During the work on [cam](https://github.com/yegor256/cam) project,
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

For `--repositories` you should provide a name of **existing** [CSV](https://en.wikipedia.org/wiki/Comma-separated_values)
dataset with GitHub repositories, and name for the output file in `--out`
(it will be created automatically).

## Filtering method

We take the input in the format of `repositories.csv`:

```csv
full_name,default_branch,stars,forks,created_at,size,open_issues_count,description,topics
apache/kafka,trunk,27266,13448,2011-08-15T18:06:16Z,182971,1085,"Mirror of Apache Kafka",kafka scala
apache/flink,master,23128,12938,2014-06-07T07:00:10Z,489079,1169,"Apache Flink",big-data flink java python scala sql
apache/cassandra,trunk,8506,3537,2009-05-21T02:10:09Z,427867,474,"Mirror of Apache Cassandra",cassandra database java
joyoyao/superCleanMaster,master,1898,884,2015-02-12T03:37:41Z,12302,18,"[DEPRECATED] ",
manifold-systems/manifold,master,2209,120,2017-06-07T02:37:23Z,126336,64,"Manifold is a Java compiler plugin, its features include Metaprogramming, Properties, Extension Methods, Operator Overloading, Templates, a Preprocessor, and more.",android-studio delegation duck-typing extension-methods graphql graphql-java intellij java java-development java-sql java-tooling js-java-interoperability json manifold metaprogramming preprocessor reflection-framework structural-typing template-engine type-providers
datageartech/datagear,master,1322,316,2020-02-22T04:06:51Z,87397,2,"数据可视化分析平台，自由制作任何您想要的数据看板",bi business-intelligence chart data-analysis data-analytics data-visualization echarts
CodingDocs/springboot-guide,master,5063,1390,2018-11-28T01:05:07Z,5354,16,"SpringBoot2.0+从入门到实战！",asynchronous dubbo mybatis rabbitmq spring-data-jpa springboot
hanks-zyh/SmallBang,master,1005,158,2015-12-24T14:48:37Z,6379,6,"  twitter like animation for any view :heartbeat:",animation heartbeat like-button twitter
...
```

this data in Markdown format looks like this:

| full_name                   | default_branch | stars | forks | created_at           | size   | open_issues_count | description                                                                                                                                                         | topics                                                                                                                                                                                                                                                                      |
|-----------------------------|----------------|-------|-------|----------------------|--------|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| apache/kafka                | trunk          | 27266 | 13448 | 2011-08-15T18:06:16Z | 182971 | 1085              | Mirror of Apache Kafka                                                                                                                                              | kafka scala                                                                                                                                                                                                                                                                 |
| apache/flink                | master         | 23128 | 12938 | 2014-06-07T07:00:10Z | 489079 | 1169              | Apache Flink                                                                                                                                                        | big-data flink java python scala sql                                                                                                                                                                                                                                        |
| apache/cassandra            | trunk          | 8506  | 3537  | 2009-05-21T02:10:09Z | 427867 | 474               | Mirror of Apache Cassandra                                                                                                                                          | cassandra database java                                                                                                                                                                                                                                                     |
| joyoyao/superCleanMaster    | master         | 1898  | 884   | 2015-02-12T03:37:41Z | 12302  | 18                | [DEPRECATED]                                                                                                                                                        |                                                                                                                                                                                                                                                                             |
| manifold-systems/manifold   | master         | 2209  | 120   | 2017-06-07T02:37:23Z | 126336 | 64                | Manifold is a Java compiler plugin, its features include Metaprogramming, Properties, Extension Methods, Operator Overloading, Templates, a Preprocessor, and more. | android-studio delegation duck-typing extension-methods graphql graphql-java intellij java java-development java-sql java-tooling js-java-interoperability json manifold metaprogramming preprocessor reflection-framework structural-typing template-engine type-providers |
| datageartech/datagear       | master         | 1322  | 316   | 2020-02-22T04:06:51Z | 87397  | 2                 | 数据可视化分析平台，自由制作任何您想要的数据看板                                                                                                                                            | bi business-intelligence chart data-analysis data-analytics data-visualization echarts                                                                                                                                                                                      |
| CodingDocs/springboot-guide | master         | 5063  | 1390  | 2018-11-28T01:05:07Z | 5354   | 16                | SpringBoot2.0+从入门到实战！                                                                                                                                               | asynchronous dubbo mybatis rabbitmq spring-data-jpa springboot                                                                                                                                                                                                              |
| hanks-zyh/SmallBang         | master         | 1005  | 158   | 2015-12-24T14:48:37Z | 6379   | 6                 | twitter like animation for any view :heartbeat:                                                                                                                     | animation heartbeat like-button twitter                                                                                                                                                                                                                                     |

For each repo (identified by `full_name` column) in the dataset we fetch it's
`README.md` file from GitHub. Then we copy all existing columns and add
new `readme` column. Then we extract `full_name`, `description`,
`topics`, and `readme` columns' values from dataset and prepare this data
for further analysis.

TBD..

## How to contribute

Fork repository, make changes, send us a [pull request](https://www.yegor256.com/2014/04/15/github-guidelines.html).
We will review your changes and apply them to the `master` branch shortly,
provided they don't violate our quality standards. To avoid frustration,
before sending us your pull request please run full build:

```bash
make install test check
```

To set up virtual environment use this set of commands:

```bash
python3 -m venv venv
source $(pwd)/venv/bin/activate
```

You will need [Python 3.9+](https://www.python.org/downloads/release/python-390)
installed.
