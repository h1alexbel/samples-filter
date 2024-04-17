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
GitHub Readme.
"""
import base64

import requests


class Readme:
    def __init__(self, repo):
        self.repo = repo

    # @todo #19:45min Use raw.githubusercontent.com instead of api.github.com.
    #  We should use static GitHub content hosting instead of their API
    #  in order to prevent problems with rate limits.
    #  Don't forget to remove this puzzle.
    def asText(self):
        response = requests.get(
            f"https://api.github.com/repos/{self.repo}/readme",
            headers={"Accept": "application/vnd.github.v3+json"}
        )
        if response.status_code == 200:
            return base64.b64decode(response.json()["content"]).decode("utf-8")
        else:
            print(f"Failed to fetch README for {self.repo}")
