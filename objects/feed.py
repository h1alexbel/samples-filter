import csv


class Feed:
    def __init__(self, file):
        self.file = file

    def read(self):
        with open(self.file, "r") as input:
            reader = csv.DictReader(input)
            feed = []
            for row in reader:
                name = row["full_name"]
                feed.append(name)
            return feed
