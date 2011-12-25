---
layout: reference
title: BIPY - Species level measures - Specificity
---

# Specificity

Specificity is measured using the Paired Difference Index (PDI).

{% highlight python linenos %}
import bipy
# If the bipartite object is called W
spe = W.specificity
# If the network is not a bipartite object
spe = bipy.specificity(W)
{% endhighlight %}

The `spe` object, in both cases, will be an array with the specificity of each species in the network.

<div class='ref'>T. Poisot, E. Canard, N. Mouquet, M.E. Hochberg, A comparative study of ecological specialization estimators, Methods in Ecology and Evolution. (in press).</div>