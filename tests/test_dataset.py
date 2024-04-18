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
        Dataset("input.csv").formulate()
        with open("pipeline/dataset.csv", 'r') as formulated, open("data.csv", 'r') as prepared:
            actual = formulated.read()
            expected = prepared.read()
        self.assertEqual(
            actual,
            expected,
            f"generated csv {actual} does not match with expected {expected}"
        )
