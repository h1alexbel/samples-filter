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
import csv

from .feed import Feed
from .text_prediction import TextPrediction

"""
Filter pipe.
"""


class FilterPipe:
    def __init__(self, repos, output, mdl, typer):
        self.repos = repos
        self.output = output
        self.model = mdl
        self.typer = typer

    # @todo #18:60min Create integration test case for filter_pipe.py.
    #  We should create some sort of integration test that checks filtering
    #  together with model prediction, files creation and other things happening
    #  in #apply(). Don't forget to remove this puzzle.
    def apply(self):
        instance = self.model()
        self.typer.echo(f"Filtering {self.repos} with {instance.name()}...")
        feed = Feed(self.repos).read()
        with open("predictions.csv", "w") as predictions:
            writer = csv.DictWriter(
                predictions,
                fieldnames=["candidate", "input", "prediction", "model"]
            )
            writer.writeheader()
            samples = []
            self.typer.echo(
                f"Predicting... (all predictions will be saved into {predictions.name})"
            )
            for candidate in feed:
                identifier = candidate["id"]
                text = candidate["input"]
                prediction = instance.predict(text)
                log = {
                    "candidate": identifier,
                    "input": text,
                    "prediction": prediction,
                    "model": instance.name()
                }
                writer.writerow(log)
                answer = TextPrediction(prediction, instance.name()).as_text()
                self.typer.echo(f"{identifier} classified as {answer}")
                if answer == "sample":
                    samples.append(identifier)
        self.typer.echo(f"found {len(samples)} samples")
        with open(self.repos, "r") as source, open(self.output, "w") as target:
            reader = csv.DictReader(source)
            writer = csv.DictWriter(target, fieldnames=reader.fieldnames)
            writer.writeheader()
            for row in reader:
                identifier = row["full_name"]
                if identifier not in samples:
                    writer.writerow(row)
        self.typer.echo(f"Filtering completed. Output saved to {self.output}")
