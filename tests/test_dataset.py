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
Test case for Dataset.
"""
import os
import unittest

from objects.dataset import Dataset
from objects.pre_filter import PreFilter

class TestDataset(unittest.TestCase):
    OUT = "out"

    def tearDown(self):
        os.remove("pipeline/dataset.csv")
        os.rmdir("pipeline")
        os.remove(self.OUT)

    def test_formulates_dataset(self):
        PreFilter(self.OUT).prepare()
        Dataset("tests/input.csv").formulate()
        with open("pipeline/dataset.csv", 'r') as formulated, open("tests/data.csv", 'r') as prepared:
            actual = formulated.read()
            expected = prepared.read()
        self.assertEqual(
            actual,
            expected,
            f"generated csv {actual} does not match with expected {expected}"
        )
