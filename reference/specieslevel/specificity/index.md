---
layout: reference
title: BIPY - Species level measures - Specificity
---

# Specificity

Specificity is measured using the Paired Difference Index (PDI).

{% highlight python linenos %}
import bipy
# If the bipartite object is called W
W.specificity
# If the network is not a bipartite object
bipy.specificity(W)
{% endhighlight %}

<div class='ref'>T. Poisot, E. Canard, N. Mouquet, M.E. Hochberg, A comparative study of ecological specialization estimators, Methods in Ecology and Evolution. (in press).</div>