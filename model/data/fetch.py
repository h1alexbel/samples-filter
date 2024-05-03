import time

from last_commit import LastCommit
from src.readme import Readme
import pandas

raw = pandas.read_csv("dataset.csv")
raw["last_commit"] = None
raw["readme"] = None

processed = 0
for index, row in raw.iterrows():
    repo = row["full_name"]
    # last_commit = LastCommit("...", repo).when()
    # raw.at[index, "last_commit"] = last_commit
    # processed += 1
    # if processed % 10 == 0:
    #     cooldown = 100
    #     print(f"Let's sleep for {cooldown}s in order to cool off GitHub API...")
    #     time.sleep(cooldown)
    readme = Readme(repo, row["default_branch"]).asText()
    raw.at[index, "readme"] = readme

raw.to_csv("fetched.csv", index=False)
print("README information has been added to the dataset.")
