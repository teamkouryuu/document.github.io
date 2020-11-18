from glob import glob
from os.path import basename
from os.path import splitext

from setuptools import setup
from setuptools import find_packages


def _requires_from_file(filename):
    return open(filename).read().splitlines()


setup(
    name="hironobunigo",
    version="0.2.0",
    license="MIT",
    description="パッケージの説明",
    author="nigo",
    url="GitHubなどURL",
    packages=["src"],
)