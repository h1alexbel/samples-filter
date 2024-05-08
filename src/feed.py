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
import csv

"""
Feed.
"""


class Feed:
    def __init__(self, file):
        self.file = file

    # @todo #105:60min Process all fields required as inputs.
    #  We should process all fields required as inputs: full_name, readme,
    #  created_at, last_commit. In case of transformer we should do it in a
    #  prompt way, like repository advanced description. Check
    #  <a href="https://github.com/h1alexbel/samples-filter/issues/75#issuecomment-2094153280">this</a>.
    def read(self):
        with open(self.file, "r") as input:
            csv.field_size_limit(2 * 1024 * 1024 * 1024)
            reader = csv.DictReader(input)
            feed = []
            for row in reader:
                name = row["full_name"]
                description = row["description"]
                lines = description
                feed.append(
                    {
                        "id": name,
                        "input": lines
                    }
                )
            return feed
