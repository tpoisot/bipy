---
layout: reference
title: BIPY - Network level measures - Nestedness
---

# Nestedness

Nestedness is measured using the Nestedness based on Overlap and Decreasing Fill (NODF) algorithm.

{% highlight python linenos %}
import bipy
W = bipy.bipartite(readweb('data.web'),nodf_strict=True)
print W.nodf
print W.nodf_up
print W.nodf_low
{% endhighlight %}

The NODF algorithm (to be continued)

<div class='ref'>M. Almeida-Neto, P. Guimaraes, P.R. Guimaraes Jr, R.D. Loyola, W. Ulrich, A consistent metric for nestedness analysis in ecological systems: reconciling concept and measurement, Oikos. 117 (2008) 1227-1239.</div>