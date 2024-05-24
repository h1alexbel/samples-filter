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
To refresh it, run either on cloud VM or locally this container:

```bash
docker run --detach --name=dataset --rm --volume "$(pwd):/dataset" \
  -e "DEPLOY_KEY=XXX" \
  --oom-kill-disable \
  h1alexbel/srdataset:0.0.1 "make -e >/dataset/make.log 2>&1"
```

The building process can take a while. After it completed, you should have
`dataset.csv` file with all collected repositories.

You will need [Python 3.9+] and [Docker] installed.

[Random-Forest]: https://en.wikipedia.org/wiki/Random_forest
[CSV]: https://en.wikipedia.org/wiki/Comma-separated_values
[Python 3.9+]: https://www.python.org/downloads/release/python-390
[Docker]: https://www.docker.com
