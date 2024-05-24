# Model

Directory `/model` contains ML models used for detecting sample
repositories (SR).

## How to use it?

You can use these models for detecting SRs:

* [Random-Forest model](#random-forest-model)
* [Isolation forest model](#isolation-forest-model)
* [Transformer model](#transformer-model)

## Random-Forest model

In order to use trained model with [Random-Forest] learning algorithm:

```python
from src.rf_model import RfModel

rating = RfModel().predict("<input here>")
print(rating) # probability that repository is a SR
```

## Isolation forest model

TBD..

## Transformer model

You can use this transformer model for detecting SRs too:

```python
from src.transformer_model import TransformerModel

rating = TransformerModel().predict("<input here>")
print(rating) # probability that repository is a SR
```

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

To do it remotely, trigger [transformer.yml](https://github.com/h1alexbel/samples-filter/actions/workflows/transformer.yml)
workflow.

You will need [Python 3.9+] installed.

## How to build new dataset?

Dataset used for model training are located here:
[train.csv](https://github.com/h1alexbel/samples-filter/blob/dataset/train.csv)
To refresh it, run this either on cloud VM or locally:

```bash
docker run --detach --name=dataset --rm --volume "$(pwd):/dataset" \
  -e "DEPLOY_KEY=XXX" \
  -e "DEPLOY_DESTINATION=h1alexbel/samples-filter" \
  -e "DEPLOY_BRANCH=dataset" \
  -e "SEARCH_QUERY=<query>" \
  -e "START_DATE=2019-01-01" \
  -e "END_DATE=2024-05-01" \
  -e "PATS=pats.txt" \
  --oom-kill-disable \
  h1alexbel/srdataset:0.0.1 "make -e >/dataset/make.log 2>&1"
```

Where `XXX` is a [GitHub PAT] with WRITE permissions to
`h1alexbel/samples-filter`, `dataset` branch, which is place, where all output
files will be delivered, `<query>` is the [search query] to the GitHub API,
`2019-01-01` is a start date to search the repositories those were created at
this date, `2024-05-01` is an end to search the repositories those were created
at this date, `pats.txt` is file contains a number of [GitHub PATs].

The building process can take a while. After it completed, you should have
`dataset.csv` file with all collected repositories.

You will need [Python 3.9+] and [Docker] installed.

[Random-Forest]: https://en.wikipedia.org/wiki/Random_forest
[search query]: https://docs.github.com/en/search-github/searching-on-github/searching-for-repositories
[GitHub PATs]: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens
[Python 3.9+]: https://www.python.org/downloads/release/python-390
[Docker]: https://www.docker.com
