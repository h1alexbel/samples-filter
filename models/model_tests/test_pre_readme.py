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

from model.pre_readme import PreReadme

"""
Test cases for PreReadme.
"""


class TestPreReadme(unittest.TestCase):

    def test_preprocesses_readme_in_tokens(self):
        tokens = PreReadme("""
            ## Java Examples for Stream Processing with Apache Flink

            This repository hosts Java code examples for
            ["Stream Processing with Apache Flink"](//link).

            **Note:** The Java examples are not complete yet. <br>
            The [Scala examples](#scala) placed here.
            """).tokens()
        expected = [
            "java", "examples", "stream", "process",
            "apache", "flink", "repository", "host",
            "java", "code", "examples", "stream",
            "process", "apache", "flinklink", "note",
            "java", "examples", "complete", "yet",
            "scala", "examplesscala", "place"
        ]
        self.assertEqual(
            tokens,
            expected,
            f"received tokens {tokens} do not match with expected {expected}"
        )