---
layout: reference
title: BIPY - Nulls models - Null model 1
---

# Null model 1

The `null1` model is the simplest possible randomization of an adjacency matrix (see Fortuna & Bascompte, 2006). Essentially, it shuffles all of the interaction in the network and returns the resulting random matrix. As for all other null models implemented in `bipy`, `null1` will only return a network once all organisms have a degree of at least 1 (no organisms are left without interactions). That way, the size does not vary across the random replicates, and only changes in the organization of links have an impact.

{% highlight python %}
w.generality()
w.vulnerability()
{% endhighlight %}

<div class='ref'>Fortuna, M.A. and Bascompte, J. (2006). Habitat loss and the structure of plant-animal mutualistic networks. Ecology Letters, 9, 281-286.</div>