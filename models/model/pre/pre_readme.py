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
import re
from nltk import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

"""
Repository README preprocessing.
"""


class PreReadme:
    def __init__(self, content):
        self.content = content

    def tokens(self):
        lower = self.content.lower()
        no_tags = re.sub(r'<.*?>', '', lower)
        no_puncts = re.sub(r'[^\w\s]', '', no_tags)
        tokens = word_tokenize(no_puncts)
        stops = set(stopwords.words('english'))
        stops.update(['b', 'bash'])
        filtered = [word for word in tokens if word not in stops]
        lemmatizer = WordNetLemmatizer()
        ready = [lemmatizer.lemmatize(word, pos='v') for word in filtered]
        print(f"Preprocessed {self.content} to: {ready}")
        return ready
