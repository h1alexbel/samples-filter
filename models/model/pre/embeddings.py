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
from transformers import BertTokenizer, BertModel, AutoTokenizer
import torch

"""
Generate embeddings for a set of tokens.
"""


# text -> numerical representations -> vector
# 768, defined by the BERT architecture
class Embeddings:
    def __init__(self, raw, length, tokenizer):
        self.raw = raw
        self.length = length
        self.tokenizer = tokenizer

    def embed(self):
        tokens = self.tokenizer.tokenize(
            self.raw,
            padding=True,
            truncation=True,
            return_tensors='pt'
        )
        ids = self.tokenizer.convert_tokens_to_ids(tokens)
        final = self.tokenizer.prepare_for_model(ids)
        return final
