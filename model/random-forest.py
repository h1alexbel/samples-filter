# MIT License
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
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import numpy
import pandas
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report
from joblib import dump

nltk.download("punkt")
nltk.download("stopwords")
frame = pandas.read_csv(
    "https://raw.githubusercontent.com/h1alexbel/samples-filter/dataset/train.csv"
)


def preprocess(text):
    if isinstance(text, str):
        tokens = word_tokenize(text)
        tokens = [token for token in tokens if token not in stopwords.words("english")]
        tokens = [token.lower() for token in tokens]
        return ' '.join(tokens)
    elif isinstance(text, float):
        return str(text)
    elif numpy.isnan(text):
        return ""


frame["description"] = frame["description"].apply(preprocess)
frame["readme"] = frame["readme"].apply(preprocess)
frame["text"] = frame["description"] + ' ' + frame["readme"]
features = frame["text"]
labels = frame["label"]
print(features)
print(labels)
print("Dataset preprocessed.")

f_train, f_test, l_train, l_test = train_test_split(
    features, labels, test_size=0.2, random_state=42
)
print("Dataset split.")

print("Training the model...")
vectorizer = TfidfVectorizer()
ftf = vectorizer.fit_transform(f_train)
ttf = vectorizer.transform(f_test)
model = RandomForestClassifier()
model.fit(ftf, l_train)

print("Evaluating the model...")
predicted = model.predict(ttf)
print(classification_report(l_test, predicted))

target = "rf-classifier.joblib"
print(f"Saving the model to... {target}")
dump(model, target)
dump(vectorizer, "rf-vec.joblib")
