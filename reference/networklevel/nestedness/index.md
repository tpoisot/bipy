---
layout: reference
title: BIPY - Network level measures - Nestedness
---

# Nestedness

Nestedness is measured using the Nestedness based on Overlap and Decreasing Fill (NODF, Almeida-Neto et al., 2008) algorithm. This measure is not sensitive to the matrix shape and size, and increases almost linearly with increased connectance.

{% highlight python linenos %}
import bipy
W = bipy.bipartite(readweb('data.web'),nodf_strict=True)
print W.nodf
print W.nodf_up
print W.nodf_low
{% endhighlight %}

The NODF algorithm calculates the nestedness for the whole network (`.nodf`), for the upper trophic level (`.nodf_up`), and the lower trophic level (`.nodf_low`). The original version described by Almeida-Neto et al. (2008) measures nestedness between two organisms only if one has more links than the other. This can be changed (the measure of nestedness between two organisms is calculated even for two organisms with the same number of links) by setting the `nodf_strict` option of `bipartite` to `False`.

<div class='ref'>M. Almeida-Neto, P. Guimaraes, P.R. Guimaraes Jr, R.D. Loyola, W. Ulrich, A consistent metric for nestedness analysis in ecological systems: reconciling concept and measurement, Oikos. 117 (2008) 1227-1239.</div>