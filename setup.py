# MIT License
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
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
setup.py
"""
import os
from setuptools import setup

def version():
    """
    Fetch version from version.txt.
    :return: version
    """
    version_file = 'version.txt'
    if os.path.exists(version_file):
        with open(version_file, 'r', encoding='utf-8') as file:
            return file.read().strip()
    else:
        return '0.0.0'

actual = version()

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='samples-filter',
    version=actual,
    packages=['src'],
    install_requires=[
        "typer",
        "pyarrow",
        "joblib",
        "requests",
        "transformers",
        "torch"
    ],
    entry_points={
        'console_scripts': [
            'samples-filter=src.__main__:main',
        ],
    },
    author='Aliaksei Bialiauski',
    author_email='aliaksei.bialiauski@hey.com',
    description=
    'Command-line filter for GitHub repositories that contain "samples",'
    ' instead of real project or framework or library',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/h1alexbel/samples-filter',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)
