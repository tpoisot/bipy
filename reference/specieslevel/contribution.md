---
layout: reference
title: BIPY - Species level measures - Contribution to nestedness
---

# Contribution to nestedness

Saavedra et al. (2011) proposed a null-model based approach to the measurement of how individual species contribute to nestedness. In *bipy*, this measure is quite easily done using the [`contrib`]({{ site.url }}/reference/classes/contrib/) class and associated methods.

{% highlight python %}
import bipy
# If the bipartite object is called W
contr = bipy.spContribNest(W,replicates=100,nodf_strict=True,model=2)
{% endhighlight %}

`W` is the bipartite object for which we want to know the species contributions. `replicates` is the number of iterations of the null model described in Saavedra et al. (2011), `nodf_strict` is a boolean to perform a strict or relaxed measure of NODF, and `model` is an integer (either `1` or `2`), which tells if the measure of contribution should be performed using a null1-like or null2-like randomization.

This function will output an array of two arrays (focal and distal species). Each array (for each trophic level) be made of three arrays: contribution of each species to the overall nestedness, to the upper trophic level nestedness, and to the lower trophic level nestedness. For ease of use, it is recommanded to use the [`contrib`]({{ site.url }}/reference/classes/contrib/) class (the options of `spContribNest` are passed to the `calculate` method):

{% highlight python %}
import bipy
# If the bipartite object is called W
W.contrib = contrib(W)
# This above is rather awful, and will likely be fixed
# in a future release
W.contrib.calculate()
{% endhighlight %}

<div class='ref'>S. Saavedra, D.B. Stouffer, B. Uzzi, J. Bascompte, Strong contributors to network persistence are the most vulnerable to extinction, Nature. 478 (2011) 233-235.</div>