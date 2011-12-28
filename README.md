# bipy

*bipy* is a collection of python scripts to analyze and visualize two-mode (bipartite) networks, mostly aimed at ecological datasets

*bipy* is released under the terms of the GNU GPL <http://en.wikipedia.org/wiki/GNU_General_Public_License>

**Author** : Timothee Poisot <timothee.poisot@uqar.ca>
**Language** : Python  2.7.2
**Requires** : numpy, scipy, pyx, tempfile, urllib

## Changes in this version (v1.0.1)

* Robustness analyses are now in a class of their own
* Improvements in the speed of the null models
* Strong improvements in the speed of tests for nestedness (nodf is calculated on raw matrices rather than coverted bipartite objects)
* Improvements in the speed of modularity analysis (labels are propagated as int rather than str)

## For a list of the features...

... see the [website](http://tpoisot.github.com/bipy/).