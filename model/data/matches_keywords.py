# MIT License
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
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
Dataset matchers.
"""
import pandas

keywords = [
    "example",
    "tutorial",
    "sample",
    "examples",
    "samples",
    "tutorials",
    "guide",
    "guides",
    "master-class",
    "masterclass"
]


def matches(input):
    if pandas.notna(input):
        words = input.lower().split()
        return any(keyword in words for keyword in keywords)
    return False


# @todo #75:30min Remove code duplication in matches_keywords.py.
#  Let's make it more generic or decorate the logic in #matches.
#  The only difference in both this functions is that we don't need extra
#  processing in case of repository name before put it #any matcher.
def matches_name(input):
    if pandas.notna(input):
        return any(keyword in input for keyword in keywords)
    return False
