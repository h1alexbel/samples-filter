build, pypi, puzzles,
loc, hoc, license

Samples-filter is a command-line filter
for GitHub repositories that contain `samples`,
instead of real project or framework or library.
E.g. [leeowenowen/rxjava-examples](https://github.com/leeowenowen/rxjava-examples),
[streaming-with-flink/examples-java](https://github.com/streaming-with-flink/examples-java), 
[redisson/redisson-examples](https://github.com/redisson/redisson-examples).

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
$ ..
```

You will need [Python 3.95+]() and [pip+]() installed.
