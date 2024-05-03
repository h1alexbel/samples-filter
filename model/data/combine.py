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
Combine csv files into one.
"""
import pandas

print("Combining datasets into single one...")
built = pandas.concat(
    [
        pandas.read_csv("repos.csv", on_bad_lines='skip'),
        pandas.read_csv("examples.csv", on_bad_lines='skip'),
        pandas.read_csv("samples.csv", on_bad_lines='skip'),
        pandas.read_csv("guides.csv", on_bad_lines='skip')
    ],
    ignore_index=True
)
print(f"Number of rows in the built dataset: {len(built)}")
target = "dataset.csv"
print(f"Flushing combined csv to {target}")
built.to_csv(target, index=False)
