---
layout: reference
title: BIPY - Species level measures - Degree distribution
---

# Degree distribution

*bipy* can count the number of links established by species of the upper (generality) and lower (vulnerability) trophic levels, following Schoener (1989). These informations are calculated whenever a `bipartite` class is created, and can be accessed with

{% highlight python %}
w.generality()
w.vulnerability()
{% endhighlight %}

<div class='ref'>T.W. Schoener, Food webs from the small to the large, Ecology. 70 (1989) 1559-1589.</div>