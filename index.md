---
layout: page
title: BIPY - analyses of bipartite interactions in Python
---

# BIPY

*bipy* is a python module geared towards the analysis of bipartite networks of ecological interactions. It is designed to be used by people with little to no background in network analysis, as most of the analyses are automated and rely on the best possible set of published methods.

## Requirements

* [Python 2.7.x](http://www.python.org/getit/releases/2.7/) (*bipy* was developped and tested under 2.7.2)
* [numpy](http://numpy.scipy.org/) **and** [scipy](http://www.scipy.org/)
* any reasonably recent version of GCC (optional, but increases the speed of some analyses)
* [PyX](http://pyx.sourceforge.net/) (and LaTeX) if you want to do any visual output (optional)

## How to load *bipy* ?

{% highlight python linenos %}
import bipy as bp
{% endhighlight %}