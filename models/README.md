# Model

Directory `/models` contains ML models used for detecting sample
repositories (SR).

## How to use it?

You can use these models for detecting SRs:

* [Isolation forest model](#if-model)
* [Transformer model based on BERT](#transformer-bert-model)

## IF model

TBD..

## Transformer BERT model

TBD..

## How to train it?

To train models, run this:

```bash
docker run -e "GH_TOKEN=..." abialiauski/samples-filter-models model/<model-name>.py
```

For `<model-name>` you should provide a name of Python script for training, for
instance `isolation-forest` or `t_bert`. For `GH_TOKEN` you should provide a
GitHub PAT for pushing `isolation-forest` model files into `results` branch of
this `h1alexbel/samples-filter`. If you are training `t_bert` model, and you
want to export output model files, then pass `-e "HF_TOKEN=..."` to push them to the
[HuggingFace].

You will need [Docker] installed.

## How to build new dataset?

Dataset used for model training are located here:
[train.csv](https://github.com/h1alexbel/samples-filter/blob/dataset/train.csv)
To refresh it, run [srdataset] either on cloud VM or locally. The building
process can take a while. After it completed, you should have `dataset.csv`
file with all collected repositories with the following structure:

* `name`: repository full name, e.g. `redisson/redisson-examples`.
* `readme`: repository README.md file.
* `description`: repository description.
* `topics`: a set of repository topics, e.g. `[apache, streaming, kafka]`
* `CPD`: commits per day calculated metric.
* `RC`: published releases to commits ratio.
* `IC`: issues to commits ratio.

All features must be preprocessed and vectorized using [pipeline.py].
Once you have vectors, you can [feed](#how-to-train-it) them to the models.

[GitHub PAT]: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens
[HuggingFace]: https://huggingface.co/models
[Docker]: https://docs.docker.com/get-docker
[srdataset]: https://github.com/h1alexbel/srdataset
[pipeline.py]: https://github.com/h1alexbel/samples-filter/blob/master/models/model/pre/pipeline.py
