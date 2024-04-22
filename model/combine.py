import pandas

# examples = pandas.read_csv('data/examples.csv')
# samples = pandas.read_csv('data/samples.csv')
# tutorials = pandas.read_csv('data/tutorials.csv')
# combined = pandas.concat([examples, samples, tutorials], ignore_index=True)
# combined.to_csv('dataset.csv', index=False)

input = pandas.read_csv('data/input.csv')
dataset = pandas.read_csv('data/dataset.csv')
combined = pandas.concat([input, dataset], ignore_index=True)
combined.to_csv('train.csv', index=False)
