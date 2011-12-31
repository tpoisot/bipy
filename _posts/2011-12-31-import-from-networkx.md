---
layout: post
title: Import from NetworkX
author: Tim
abstract: A new function, allowing to import data from the NetworkX package
tag:
- feature
- networkx
---

The 1.0.2 version, currently in development, will allow to import data from the [NetworkX](http://networkx.lanl.gov/) software, and convert it to a `bipartite` object usable by `bipy`. The procedure is actually quite simple, and will allow a better interoperability betweem the two modules.

Start by creating a networkx bipartite graph:

{% highlight python %}
import networkx as nx
top_nodes=[1,1,2,3,3]
bottom_nodes=['a','b','b','b','c']
edges=zip(top_nodes,bottom_nodes) # create 2-tuples of edges
B=nx.Graph(edges)
{% endhighlight %}

Then simply convert it to a bipartite object using:

{% highlight python %}
aa = nxImport(B)
aa.txt()
{% endhighlight %}

You should have the following output:

{% highlight bash %}
█-█
--█
-██
{% endhighlight %}

The function will take care of assigning the correct species names, and you can use an optional `name` argument in `nxImport` to give a name to your network.

**Note that for some reason**, using the `easy_install networkx` command on my Mac installed the 0.3 version, instead of the current 1.6. If the same happens to you, just download the [sources](http://pypi.python.org/pypi/networkx/) and use `python setupy.py install`.