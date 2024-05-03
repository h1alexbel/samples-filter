import pandas

from matches_keywords import matches

origin = "no-branch.csv"
target = "labeled.csv"
unlabeled = pandas.read_csv(origin)
unlabeled["label"] = 0

labeled = 0
for index, row in unlabeled.iterrows():
    if row['label'] == 1:
        continue
    if matches(row["description"]):
        unlabeled.at[index, "label"] = 1
        labeled += 1

unlabeled.to_csv(target, index=False)
print(f"Dataset labeled in {target}")
print(f"Labeled rows: {labeled}")
