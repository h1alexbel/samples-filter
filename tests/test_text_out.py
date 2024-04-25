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
Test case for TextOut.
"""
import unittest

from objects.text_out import TextOut


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

    def test_raises_error_on_invalid_input(self):
        with self.assertRaises(
                TypeError,
        ):
            TextOut("<invalid input>").as_text()
