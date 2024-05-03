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
