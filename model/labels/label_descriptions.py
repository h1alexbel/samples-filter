import pandas

csv_file = '../train.csv'
df = pandas.read_csv(csv_file)

keywords = ["example", "tutorial", "sample"]

df['description'] = df['description'].astype(str)
def matches(description):
    if pandas.notna(description):
        words = description.lower().split()
        return any(keyword in words for keyword in keywords)
    return False

df['label'] = df['description'].apply(matches).astype(int)
df.to_csv(csv_file, index=False)

print("CSV file updated with labels.")
