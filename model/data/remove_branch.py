import pandas

origin = "fetched.csv"
target = "no-branch.csv"
frame = pandas.read_csv(origin)
print(f"Removing `default_branch` column from {origin}...")
frame.drop(columns=["default_branch"]).to_csv(target, index=False)
print(f"Created {target} without `default_branch` column.")
