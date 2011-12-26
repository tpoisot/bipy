---
layout: reference
title: BIPY - Reference - Classes - tests
---

# The test class

This class is used to assess the significancy of the nested or modular pattern of a bipartite network, against a sample of random networks obtained through one of the four currently implemented [null models]({{ site.url }}/reference/nulls/wrapper/). The references to the methods used are described in the relevant pages.

The general principle behing the analyses is as follows. Given a network for which we know the value of one metric (e.g. nestedness), $N$, we want to know if this value is significantly different than what whould be expected at random. We generate a series of pseudo-random networks under certain rules, and for each of them, calculate the same metric, so that we have a pseudo-random distribution $N'$. If the value of this metric in the original network is obtained by chance, the mean of the distribution of $N-N'$ will not be different from 0. This is assessed by doing a two-tailed one sample t-test, and checking that 0 falls within the [95 % confidence interval predicted through a Bayesian method](http://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.bayes_mvs.html).

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

By itself, the `test` class is only generating a list of null models. The tests are taken care of by the `nestedness` and `modularity` methods described thereafter. It should be noted that it is possible to perform one test but not the other (e.g. nestedness but not modularity). After creating a new instance of a `test` class, it will have a `null` object, which is an array of length `replicates`, with each element being a null interaction matrix.

## Test for modularity

The test for modularity will likely be the longest thing that *bipy* will do, as it requires optimizing the community partition for each of the null replicates. Use of the `q_c = True` option is therefore strongly recommended. This test is done through the `modularity()` method of the `test` class, and takes one mandatory argument `repl`, giving the number of replicates of the [LP-BRIM]({{ site.url}}/reference/networklevel/modularity/) algorithm to perform, for each random network.

{% highlight python linenos %}
test_web.modularity(500)
{% endhighlight %}

Doing this will add two objects (`devqr` and `devqb`), corresponding to the output of the [`getDevMod`]({{ site.url }}/reference/tests/modularity/) function.

If the `bipartite` object on which the analysis is done has no information in its module object, i.e. no detection of modularity was previously conducted, the `modularity` method will perform it, and issue a warning if `verbose = True`.

## Test for nestedness

## Results output

<div class='ref'>Ref. coming soon.</div>