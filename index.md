---
title: BIPY -- analysis of bipartite interactions in python
---

# BIPY

*bipy* is a python module geared towards the analysis of bipartite networks of ecological interactions. It is designed to be used by people with little to no background in network analysis, as most of the analyses are automated and rely on the best possible set of published methods.

## Requirements

* Python 2.7.x
* numpy **and** scipy
* any reasonably recent version of GCC (optional, but increases the speed of some analyses)
* PyX and LaTeX if

## How to load *bipy* ?

{% highlight python %}
import bipy as bp
{% endhighlight %}