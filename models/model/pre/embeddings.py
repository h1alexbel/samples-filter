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
from transformers import BertTokenizer, BertModel
import torch

"""
Generate embeddings for a set of tokens.
"""


class Embeddings:
    def __init__(self, tokens, length, encoder="bert-base-uncased"):
        self.tokens = tokens
        self.length = length
        self.tokenizer = BertTokenizer.from_pretrained(encoder)
        self.model = BertModel.from_pretrained(encoder)

    def embed(self):
        print(f"Generating embeddings for {self.tokens}")
        print(f"Encoder: {self.tokenizer}, {self.model}, output length: {self.length}")
        inputs = []
        masks = []
        # @todo #143:30min We generate embeddings for each token instead of the whole unit.
        #   For now, we generate embeddings for each token. We probably should
        #   generate embeddings for joined tokens as one unit. In this case we
        #   can try to replace preprocessing steps with a huggingface tokenizers.
        #   Let's validate this assumption.
        for tokens in self.tokens:
            ids = self.tokenizer.encode_plus(
                tokens,
                add_special_tokens=True,
                return_tensors='pt',
                padding='max_length',
                truncation=True,
                max_length=self.length
            )
            inputs.append(ids["input_ids"])
            masks.append(ids["attention_mask"])
        inputs = torch.cat(inputs, dim=0)
        masks = torch.cat(masks, dim=0)
        with torch.no_grad():
            outputs = self.model(inputs, attention_mask=masks)
            states = outputs.last_hidden_state
        embeddings = states[0].numpy()
        print(f"Generated embeddings {embeddings}")
        return embeddings
