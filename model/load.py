# The MIT License (MIT)
#
# Copyright (c) 2024 Aliaksei Bialiauski
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
Load and pre-process dataset.
"""
from sklearn.model_selection import train_test_split
from datasets import load_dataset

def load():
    frame = load_dataset(
        "h1alexbel/github-samples",
        data_files="data/train.csv"
    )["train"].to_pandas()
    frame = frame.dropna(subset=['label'])
    frame['label'] = frame['label'].apply(lambda x: 'positive' if x == 1.0 else 'negative')
    frame["repository"] = (
            frame["full_name"].astype(str) + " " +
            frame["description"].astype(str) + " " +
            frame["topics"].astype(str) + " " +
            frame["readme"].astype(str)
    )
    repos = frame["repository"].tolist()
    labels = frame["label"].tolist()
    train_repos, temp_repos, train_labels, temp_labels = (
        train_test_split(repos, labels, test_size=0.2, random_state=42)
    )
    label_mapping = {"positive": 1, "negative": 0}
    train_labels = [label_mapping[label] for label in train_labels]
    val_repos, test_repos, val_labels, test_labels = (
        train_test_split(temp_repos, temp_labels, test_size=0.5, random_state=42)
    )
    return train_repos, train_labels, val_repos, val_labels, test_repos, test_labels
