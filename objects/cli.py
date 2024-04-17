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

"""
Cli runner.
"""
from typing import Optional

import typer

from objects import NAME, VERSION
from .pre_filter import PreFilter
from .input import Input

app = typer.Typer()


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{VERSION}")
        raise typer.Exit()


@app.command()
def filter(
        repositories: str = typer.Option(
            ..., "--repositories", help="Path to the repositories CSV file."
        ),
        out: str = typer.Option(
            ..., "--out", help="Path to the output CSV file."
        )
):
    """
    Filter repositories.
    """
    typer.echo(f"Filtering {repositories}...")
    # @todo #10:45min Filter the repositories using general-like interface.
    #  We should execute filtering here using some general interface, so
    #  it would easy to use either LLM or ML filters.
    # @todo #19:45 Implement chain of csv transformation.
    #  We should implement a transformation chain of csv files.
    #  For now we are just adding separate objects to this script.
    #  Let's create a class (let's call it `train` or `pipeline`) that would
    #  execute all transformation one by one.
    PreFilter(out).prepare()
    Input(repositories).copy()
    typer.echo(f"Filtering completed. Saving output to {out}...")


# Run it.
@app.callback()
def main(
        # pylint: disable=unused-argument
        version: Optional[bool] = typer.Option(
            None,
            "--version",
            help="Show the application's version and exit.",
            callback=_version_callback,
            is_eager=True,
        )
) -> None:
    f"""
    {NAME}
    """
    return
