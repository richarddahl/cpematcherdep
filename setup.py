from codecs import open
from os import path

from setuptools import setup, find_packages

__version__ = "0.0.8"

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

# get the dependencies and installs
with open(path.join(here, "requirements.txt"), encoding="utf-8") as f:
    all_reqs = f.read().split("\n")

install_requires = [x.strip() for x in all_reqs if "git+" not in x]
dependency_links = [
    x.strip().replace("git+", "") for x in all_reqs if x.startswith("git+")
]

setup(
    name="cpematcherdep",
    version=__version__,
    description="Fork of alertot/cpematcher: Matches CPE Names and any Deprecated CPE Names.",
    long_description=long_description,
    url="https://github.com/richarddahl/cpematcherdep",
    download_url="https://github.com/richarddahl/cpematcherdep/tarball/" + __version__,
    license="BSD",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.10",
    ],
    keywords="",
    packages=find_packages(exclude=["docs", "tests*"]),
    include_package_data=True,
    author="cmplid:// Inc.",
    install_requires=install_requires,
    dependency_links=dependency_links,
)
