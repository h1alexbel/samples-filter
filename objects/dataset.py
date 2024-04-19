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
Dataset.
"""
import csv


class Dataset:
    DESTINATION = "pipeline/dataset.csv"

    def __init__(self, where):
        self.where = where

    """
    Formulate dataset.
    """
    def formulate(self):
        with open(self.where, "r") as input, open(self.DESTINATION, "w", newline="") as pipe:
            reader = csv.DictReader(input)
            writer = csv.DictWriter(
                pipe,
                fieldnames=[
                    "full_name",
                    "description",
                    "topics",
                    "readme"
                ]
            )
            writer.writeheader()
            # @todo #34:60min CSV column 'readme' is too big to read with reader.
            #  Column that contains readme in some cases is over the limit,
            #  which is `131072`. It this problem causes exception and
            #  terminates next row processing. Let's try to compress +
            #  decompress readme when writing/reading it. Another option can
            #  be to present the whole dataset in other format, for instance
            #  JSON. Don't forget to remove this puzzle.
            for row in reader:
                repo = row["full_name"]
                description = row["description"]
                topics = row["topics"]
                readme = row["readme"]
                out = {
                    "full_name": repo,
                    "description": description,
                    "topics": topics,
                    "readme": readme
                }
                writer.writerow(out)
                print(f"Prepared dataset for {repo}")
