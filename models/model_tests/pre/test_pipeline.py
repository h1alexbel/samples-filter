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
import unittest

from model.pre.pipeline import Pipeline
from transformers import AutoTokenizer

"""
Test cases for Pipeline.
"""


class TestPipeline(unittest.TestCase):

    def test_vectorizes_repository(self):
        repository = {
            "name": "h1alexbel/fakehub",
            "readme": """
            # fakehub
            
            # How to use
            
            first, install it like this:
            
            ```bash
            brew install fakehub
            ```
            
            then, run it:
            
            ```bash
            fakehub start
            ```
            """,
            "description": "fakehub description",
            "topics": "rust,github,mock-api,testing",
            "cpd": 5.2,
            "rc": 0.04,
            "ic": 0.25
        }
        tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
        vector = Pipeline(repository, tokenizer).apply().tolist()
        size = len(vector)
        cpd = repository["cpd"]
        has_cpd = cpd in vector
        rc = repository["rc"]
        has_rc = rc in vector
        ic = repository["ic"]
        has_ic = ic in vector
        expected = 78
        self.assertEqual(
            size,
            expected,
            f"received vector size {size} for vector {vector} does not match with expected {expected}"
        )
        self.assertTrue(
            has_cpd,
            f"received vector {vector} does not have CPD value: {cpd}, but should"
        )
        self.assertTrue(
            has_rc,
            f"received vector {vector} does not have RC value: {rc}, but should"
        )
        self.assertTrue(
            has_ic,
            f"received vector {vector} does not have IC value: {ic}, but should"
        )
