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

from src.feed import Feed

"""
Test case for feed.py.
"""


class TestFeed(unittest.TestCase):

    def test_reads_feed(self):
        feed = Feed("test-feed.csv").read()
        expected = [
            {
                'id': 'totond/TextPathView',
                'input': 'A View with text path animation!'
            },
            {
                'id': 'square/mortar',
                'input': 'A simple library that makes it easy to pair thin views with dedicated controllers, isolated from most of the vagaries of the Activity life cycle.'
            },
            {
                'id': 'joyoyao/superCleanMaster',
                'input': '[DEPRECATED] '
            }
        ]
        self.assertEqual(
            feed,
            expected,
            f"Received feed {feed} does not match with expected {expected}"
        )
