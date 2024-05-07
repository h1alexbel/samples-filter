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
import requests

"""
Dump remote asset from GitHub branch locally.
"""


class RemoteAsset:
    def __init__(self, ref):
        self.ref = ref

    def dump(self):
        print(f"Downloading {self.ref} ...")
        response = requests.get(
            f"https://raw.githubusercontent.com/h1alexbel/samples-filter/random-forest/{self.ref}"
        )
        if response.status_code == 200:
            with open(f"{self.ref}", "wb") as vfile:
                print(f"Dumping {self.ref} locally...")
                vfile.write(response.content)
                return vfile.name
        else:
            raise FileNotFoundError(f"Failed to fetch ref: {self.ref}")
