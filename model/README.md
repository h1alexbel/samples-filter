# Model

Directory `/model` contains ML models used for classification
of GitHub repositories.

## How to use it?

You can use these models for repository classification:

* [Random-Forest model](#random-forest-model)
* [Text Transformer model](#transformer-model)

## Random-Forest model

In order to use trained model with [Random-Forest] learning algorithm:

```python
from src.rf_model import RfModel

prediction = RfModel().predict("<input here>")
print(prediction) # 0 or 1
```

`0` means that repository is real, while `1` means that repository is sample.

## Transformer model

You can use this _pre-trained model_ for predictions like that:

```python
from src.transformer_model import TransformerModel

prediction = TransformerModel().predict("<input here>")
print(prediction) # POSITIVE or NEGATIVE
```

`POSITIVE` prediction says that repository is not real, since it contains
examples, tutorials or samples; while `NEGATIVE` signs that repository
is a real project/framework/library.

## How to train it?

To train Random-Forest model, run this script:

```bash
make random-forest
```

After training successfully ended, you should have `.joblib` files for both,
vectorizer and model. Latest model version is [here](https://github.com/h1alexbel/samples-filter/tree/random-forest).
To publish a new, trigger [random-forest.yml](https://github.com/h1alexbel/samples-filter/actions/workflows/random-forest.yml)
workflow.

If you want to train transformer model, you should run this script:

```bash
export HF_TOKEN=<your hugging face API key>
make transformer
```

Pay attention to the exported `HF_TOKEN`, it's needed for [pushing](https://huggingface.co/docs/transformers/v4.15.0/en/model_sharing)
trained model into Hugging Face Model Hub.

Training will take approximately 10 minutes. After it successfully finished,
all output model files will be pushed to [h1alexbel/github-samples-tclassifier](https://huggingface.co/h1alexbel/github-samples-tclassifier).

To do it remote, trigger [transformer.yml](https://github.com/h1alexbel/samples-filter/actions/workflows/transformer.yml)
workflow.

You will need [Python 3.9+] installed.

## How to build new dataset?

To build new dataset, run this:

```bash
make data/dataset
```

The building process will take you approximately 7 minutes.
Now, you should have `train.csv` containing all the repos together.

Training dataset is a [CSV] file with the following columns:

* `full_name` for repository name, e.g. `yegor256/takes`
* `description` for repository description
* `readme` for repository's README.md
* `created_at` for when repository was created, e.g. `2015-07-14T12:58:49Z`
* `last_commit` for date of last commit in repository, e.g. `2017-07-14T13:14:24Z`
* `commits` for number of commits in the repository
* `label` for labeling repositories as real (`0`) and sample (`1`)

Full dataset used for model training is located [here](https://github.com/h1alexbel/samples-filter/blob/dataset/train.csv).
To refresh it, trigger [dataset.yml](https://github.com/h1alexbel/samples-filter/actions/workflows/dataset.yml)
workflow.

You will need [Python 3.9+] and [Ruby 3.3+] installed.

[Random-Forest]: https://en.wikipedia.org/wiki/Random_forest
[CSV]: https://en.wikipedia.org/wiki/Comma-separated_values
[Python 3.9+]: https://www.python.org/downloads/release/python-390
[Ruby 3.3+]: https://www.ruby-lang.org/en/documentation/installation
