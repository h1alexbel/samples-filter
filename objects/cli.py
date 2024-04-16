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
from typing import Optional

import typer

from objects import name, version

app = typer.Typer()


# @todo #1:45min Add support for --repositories and --out parameter.
#  We should add support to our cli to handle two options: --repositories,
#  and --out. Both indicate the name of the file to read/create.
# @todo #1:25min Clean parameters that we don't need.
#  Let's remove parameters that we don't really need in this cli.
#  Less parameters we will have, the better.
#  Don't forget to remove this puzzle.
def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{name} v{version}")
        raise typer.Exit()


@app.callback()
def main(
        version: Optional[bool] = typer.Option(
            None,
            "--version",
            "-v",
            help="Show the application's version and exit.",
            callback=_version_callback,
            is_eager=True,
        )
) -> None:
    return
