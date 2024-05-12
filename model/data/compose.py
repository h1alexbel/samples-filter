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
Compose text from train.csv in single 'text' column.
"""
import pandas

origin = "train.csv"
target = "text.csv"
print(f"Composing {origin} into text column...")
frame = pandas.read_csv(origin)
# @todo #104:90min Split README.md into important segments.
#  We should split README.md file into segments that are important for
#  processing. For now the problem is in the README.md size. If file is
#  reasonably big, than model will interpret it like negative, while README
#  is taken from example repository. Let's fix it by splitting README.md file
#  into segments and then picking the segment that represents this repository
#  in most accurate way. Let's find out techniques that will help us in README
#  splitting from this paper: https://www.researchgate.net/publication/317489055_Cataloging_GitHub_Repositories
frame["text"] = (
        "Repository: " + frame["full_name"] + '; ' +
        "Description: " + frame["description"].fillna('NULL') + '; ' +
        "README.md: " + frame["readme"]
).astype(str)
frame.drop(
    columns=[
        "full_name",
        "description",
        "readme",
        "created_at",
        "last_commit"
    ]
).to_csv(target, index=False)
print(f"Composed columns flushed to {target}")
