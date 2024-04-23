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

# examples = pandas.read_csv('data/examples.csv')
# samples = pandas.read_csv('data/samples.csv')
# tutorials = pandas.read_csv('data/tutorials.csv')
# combined = pandas.concat([examples, samples, tutorials], ignore_index=True)
# combined.to_csv('dataset.csv', index=False)

# @todo #41:45min Combine all the csv files into merge.csv.
#  We should combine all 4 files: default.csv, examples.csv, samples.csv,
#  and tutorials.csv (all should have readme, use input.py for this) into one
#  big file named merge.csv. Don't forget to remove this puzzle.
input = pandas.read_csv('data/input.csv')
dataset = pandas.read_csv('data/dataset.csv')
combined = pandas.concat([input, dataset], ignore_index=True)
combined.to_csv('train.csv', index=False)
