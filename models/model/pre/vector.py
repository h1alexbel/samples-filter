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
import numpy as np

"""
Vectorizes the embedding matrixes with a scalar values into single vector.
"""


class Vector:
    def __init__(self, *matrixes, **scalars):
        self.matrixes = [np.array(mat) for mat in matrixes]
        self.scalars = {key: val for key, val in scalars.items()}

    def plain(self):
        flattened = []
        for matrix in self.matrixes:
            flattened.append(matrix.flatten())
        vector = np.concatenate(flattened)
        scals = []
        for scalar in self.scalars.values():
            scals.append(np.reshape(scalar, (-1,)).astype(float))
        values = np.concatenate(scals)
        return np.concatenate((vector, values))
