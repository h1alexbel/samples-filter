# Transformer Model

[![Model on HF](https://huggingface.co/datasets/huggingface/badges/resolve/main/model-on-hf-sm.svg)](https://huggingface.co/h1alexbel/github-samples-classifier)
[![Dataset on HF](https://huggingface.co/datasets/huggingface/badges/resolve/main/dataset-on-hf-sm.svg)](https://huggingface.co/datasets/h1alexbel/github-samples)

Directory `/model` contains ML model used for text classification
of GitHub repositories, that consist of `full_name`, `description`, `topics`,
and `readme`.

## How to use it?

You can use this _pre-trained model_ for predictions via `predictor.py`:

```python
from model.predictor import Predictor

prediction = Predictor("<input here>").predict()
print(prediction) # NEGATIVE or POSITIVE
```

`POSITIVE` prediction says that repository is not real, it contains
examples, tutorials or samples; while `NEGATIVE` signs that repository
is a real project/framework/library.

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

## How to build new dataset?

To build new dataset, follow these steps:

TBD..

## How to train it?

To train the model you should run this script:

```bash
export HF_TOKEN=<your hugging face API key>
python3 train.py
```

Pay attention to exported `HF_TOKEN`, it's needed for pushing trained model into
[Hugging Face Model Hub](https://huggingface.co/docs/diffusers/en/using-diffusers/push_to_hub).

Training consume approximately 30 minutes. After it successfully finished,
all output model files will be pushed to [h1alexbel/github-samples-classifier](https://huggingface.co/h1alexbel/github-samples-classifier).

You will need [Python 3.9+] installed.

[CSV]: https://en.wikipedia.org/wiki/Comma-separated_values
[Python 3.9+]: https://www.python.org/downloads/release/python-390
