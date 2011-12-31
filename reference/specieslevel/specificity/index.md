---
layout: reference
title: BIPY - Species level measures - Specificity
---

# Specificity

The default measure of specificity is the (quantitative) Paired Difference Index (PDI). This measure works by sorting the link strength (interaction strenghts, i.e. the values in the matrix) of each organism of the upper trophic level, and measuring how fast they decay from the optimum (Poisot et al., in press). Alternative measures are the (quantitative) Species Specialization Index (Julliard et al., 2006), and the (binary) Resource Range (Poisot et al., in press).

{% highlight python %}
import bipy
# If the bipartite object is called W
spe = W.specificity
ssi = W.ssi
rr = W.rr
# If the network is not a bipartite object
# Not recommended, this is slower
spe = bipy.specificity(W)
ssi = bipy.ssi(W)
rr = bipy.rr(W)
{% endhighlight %}

The `spe` object, in both cases, will be an array with the specificity of each species in the network measured by PDI. The `ssi` array will have the Species specialization index, and the `rr` array will have the resource range.

The corrections of these measures explained in Poisot et al. (in press) are implemented in *bipy* so that a value of 1 correspond to a perfect specialist, and a value of 0 correspond to a perfect generalist.

<div class='ref'>T. Poisot, E. Canard, N. Mouquet, M.E. Hochberg, A comparative study of ecological specialization estimators, Methods in Ecology and Evolution. (in press).   
R. Julliard, J. Clavel, V. Devictor, F. Jiguet, D. Couvet, Spatial segregation of specialists and generalists in bird communities, Ecology Letters. 9 (2006) 1237-1244.</div>