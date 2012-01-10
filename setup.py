import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "bipy",
    version = "1.0.3",
    author = "Timothee Poisot",
    author_email = "timothee.poisot@uqar.ca",
    description = ("A Python module to work on bipartite networks"
                   "of ecological interactions."),
    license = "GNU GPL",
    keywords = "ecology bipartite networks bioinformatics",
    url = "http://tpoisot.github.com/bipy/",
    packages=['bipy','bipy.contrib','bipy.base','bipy.null','bipy.nes','bipy.mod','bipy.graphs','bipy.web','bipy.tests','bipy.spe','bipy.dataIO'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Intended Audience :: Science/Research",
        "Environment :: Console",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Topic :: Scientific/Engineering :: Visualization"
        ],
    )
