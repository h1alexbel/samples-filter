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
Last commit for GitHub repository.
@todo #75:45min Find a way to fetch date of last commit without using API.
 GitHub API usage has quite soft rate limits. Even with authentication, it
 can't process whole dataset (approx 1k) rows. Moreover, we can't let to pass
 the credentials in the CLI package. Let's investigate the ways to parse last
 commit date without API.
"""
import json

import requests


class LastCommit:
    def __init__(self, auth, repo):
        self.auth = auth
        self.repo = repo

    def when(self):
        response = requests.get(
            f"https://api.github.com/repos/{self.repo}/commits",
            headers={
                "Authorization": self.auth
            }
        )
        date = json.loads(response.content)[0]["commit"]["author"]["date"]
        print(f"For {self.repo} last commit was at {date}")
        return date
