---
layout: post
title: First release and dev branch
tag: [release]
---

The first release of `bipy` (v 1.0.0) was pushed a few days ago. As explained in the [versions notes]({{ site.url }}/changelog/), the stable releases will be tagged, and the current development version will be available through the `dev` branch. By default, the `master` branch on GitHub will have the latest stable release.

Starting from this version, `bipy` can be installed using setuptools:

{% highlight bash %}
sudo python setup.py install
{% endhighlight %}

At this time, the [tutorial]({{ site.url }}/tutorial/) and some of the already written [reference pages]({{ site.url }}/reference/) may not be entirely up to date, but I will work on fixing this in the next days.