---
layout: reference
title: BIPY - Reference - Classes - tests
---

# The test class

This class is used to assess the significancy of the nested or modular pattern of a bipartite network, against a sample of random networks obtained through one of the four currently implemented [null models]({{ site.url }}/reference/nulls/wrapper/).

## Starting a test

The `__init__` method of the `test` class requires the following arguments:

* `web`: a bipartite object
* `model`: the name of one of the [null models]({{ site.url }}/reference/nulls/wrapper/) generating functions
* `replicates`: the number of null networks to generate
* `verbose`: the `test` class can output some messages about the progress of the analysis (boolean).
* `q_c`: boolean, whether to use the optimized C function for Qbip (`True`) or not (`False`); the `q_c` argument is passed to the [`modules`]({{ site.url }}/reference/classes/modules/) class

The following snippet illustrates how to initialize a test with 10 replicates of the [null model 2]({{ site.url }}/reference/nulls/null2/), with no verbose output and the optimized C function.

{% highlight python linenos %}
from bipy import *
w = bipartite(readweb('my_web.web'),t=False)
test_web = test(w,null_2,10,verbose=False,q_c=True)
{% endhighlight %}

By itself, the `test` class is only generating a list of null models. The tests are taken care of by the `nestedness` and `modularity` methods described thereafter. It should be noted that it is possible to perform one test but not the other (e.g. nestedness but not modularity).

## Test for modularity

## Test for nestedness

## Results output

<div class='ref'>Ref. coming soon.</div>