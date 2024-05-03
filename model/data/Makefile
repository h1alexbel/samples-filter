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
.PHONY: install test check
.SILENT:

## The shell to use.
SHELL := bash

clean:
	rm -f dataset.csv repos.csv examples.csv samples.csv guides.csv repos.tex examples.tex samples.tex guides.tex

# Build new dataset.
dataset:
	@echo "Starting dataset build at $(shell date '+%Y-%m-%d %H:%M:%S')"
	ruby discover-repos.rb --total=750 --csv=repos.csv --tex=repos.tex
	ruby discover-repos.rb --total=84 --query-append=examples --min-stars=20 --csv=examples.csv --tex=examples.tex
	ruby discover-repos.rb --total=83 --query-append=samples --min-stars=20 --csv=samples.csv --tex=samples.tex
	ruby discover-repos.rb --total=83 --query-append=guides --min-stars=20 --csv=guides.csv --tex=guides.tex
	python3 combine.py
	@echo "Finished dataset build at $(shell date '+%Y-%m-%d %H:%M:%S')"
	@echo "Dataset build duration: $(shell date -u -d @$$(($(shell date -u +%s) - $(shell date -u +%s))))"
