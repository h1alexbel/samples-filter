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

from model.pre.embeddings import Embeddings
from model.pre.vector import Vector

"""
Pipeline.
Processing from repository in csv format to vector.
"""


class Pipeline:
    """
    Ctor.
    :param repository Repository to vectorize
    """

    def __init__(self, repository, tokenizer):
        self.repository = repository
        self.tokenizer = tokenizer

    def apply(self):
        name = self.repository["name"]
        print(f"processing {name}")
        return Vector(
            Embeddings(name, 30, self.tokenizer).embed()["input_ids"],
            Embeddings(
                self.repository["readme"],
                512,
                self.tokenizer
            ).embed()["input_ids"],
            Embeddings(
                self.repository["description"],
                100,
                self.tokenizer
            ).embed()["input_ids"],
            Embeddings(
                self.repository["topics"], 100, self.tokenizer
            ).embed()["input_ids"],
            cpd=self.repository["cpd"],
            rc=self.repository["rc"],
            ic=self.repository["ic"]
        ).plain()
