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

.SHELLFLAGS: -e -o pipefail -c
.ONESHELL:
.PHONY: clean dataset trainrf transformer
.SILENT:

## The shell to use.
SHELL := bash

# Data folder.
DATA_FOLDER := data

# Clean .csv and .tex files.
$(DATA_FOLDER)/clean:
	cd $(DATA_FOLDER) && \
	rm -f *.csv *.tex

# Build new dataset.
$(DATA_FOLDER)/dataset:
	cd $(DATA_FOLDER) && \
	ruby discover-repos.rb --total=750 --csv=repos.csv --tex=repos.tex
	ruby discover-repos.rb --total=84 --query-append=examples --min-stars=20 --csv=examples.csv --tex=examples.tex
	ruby discover-repos.rb --total=83 --query-append=samples --min-stars=20 --csv=samples.csv --tex=samples.tex
	ruby discover-repos.rb --total=83 --query-append=guides --min-stars=20 --csv=guides.csv --tex=guides.tex
	python3 combine.py
	python3 fetch.py
	python3 remove_branch.py
	python3 label.py

# Train model with Random-Forest algorithm.
trainrf:
	python3 random-forest.py
# upload to huggingface

# Train text transformer.
transformer:
	python3 transformer.py
