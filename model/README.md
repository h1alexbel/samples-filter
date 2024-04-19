# Transformer Model

Directory `/model` contains ML model used for text classification
on GitHub repositories, that consist of `full_name`, `description`, `topics`,
and `readme`.

## Datasets

Training dataset is a [CSV] file with the following columns:

* `full_name` for repository name, e.g. `yegor256/takes`
* `description` for repository description
* `topics` for repository topics
* `readme` with repository's README.md content

All these columns will be combined into single text frame called `repository`.
Besides all above, dataset has `label` column too.
It used for repository classification, by assigning `0` we are saying that repository
is `real`, while `1` means that repository is `sample` one.

Full dataset used for model training is located [here](https://huggingface.co/datasets/h1alexbel/github-samples).

## How to train it?

To train the model run `train.py` script:

```bash
python3 train.py
```

You will need [Python 3.9+] installed.

[CSV]: https://en.wikipedia.org/wiki/Comma-separated_values
[Python 3.9+]: https://www.python.org/downloads/release/python-390
