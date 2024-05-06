# rename to rf.py
import numpy
import pandas
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report

nltk.download("punkt")
nltk.download("stopwords")
# upload dataset to HuggingFace and fetch it from there.
frame = pandas.read_csv("../data/train.csv")


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

