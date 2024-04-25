import unittest

from text_out import TextOut


class TestTextOut(unittest.TestCase):

    def test_prints_as_real(self):
        prediction = [{'label': 'NEGATIVE', 'score': 1.0}]
        text = TextOut(prediction).as_text()
        expected = "real"
        self.assertEqual(
            text,
            expected,
            f"output '{text}' for '{prediction}' does not match with expected {expected}"
        )

    def test_prints_as_sample(self):
        prediction = [{'label': 'POSITIVE', 'score': 1.0}]
        text = TextOut(prediction).as_text()
        expected = "sample"
        self.assertEqual(
            text,
            expected,
            f"output '{text}' for '{prediction}' does not match with expected {expected}"
        )
