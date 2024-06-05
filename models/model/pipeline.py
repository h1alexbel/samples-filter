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

from model.embeddings import Embeddings
from model.pre_description import PreDescription
from model.pre_name import PreName
from model.pre_readme import PreReadme
from model.pre_topics import PreTopics
from model.vector import Vector

"""
Pipeline.
Processing from repository in csv format to vector.
"""


class Pipeline:
    """
    Ctor.
    :param repository Repository to vectorize
    """

    def __init__(self, repository):
        self.repository = repository

    def apply(self):
        name = self.repository["name"]
        print(f"processing {name}")
        name = PreName(name).tokens()
        readme = PreReadme(self.repository["readme"]).tokens()
        description = PreDescription(self.repository["description"]).tokens()
        topics = PreTopics(self.repository["topics"]).tokens()
        e_name = Embeddings(name, 30).embed()
        e_readme = Embeddings(readme, 512).embed()
        e_description = Embeddings(description, 100).embed()
        e_topics = Embeddings(topics, 100).embed()
        return Vector(
            e_name,
            e_readme,
            e_description,
            e_topics,
            cpd=self.repository["cpd"],
            rc=self.repository["rc"],
            ic=self.repository["ic"]
        ).plain()
