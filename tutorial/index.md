---
layout: page
title: BIPY - Tutorial
---

# A step-by-step introduction

The goal of this tutorial is to cover the things that *bipy* is able to do. More extensive information can be found in the [reference]({{ site.url }}/reference/) pages, in which a detailed list of the built-in functionalities can be found.

This tutorial require that you have installed *bipy* in your local Python distribution. We will work on the data by [Fonseca & Ganade (1996) dataset]({{ site.url }}/tutorial/fonseca-ganade.web). To use another dataset, see the page about [loading data]({{ site.url }}/reference/data/reading/).

## Step 1 : loading the data and naming the species

To load the data and give name to the species, the following commands are used:

{% highlight python linenos %}
# Loading bipy
from bipy import *
# Reading the network, and giving it a name
rw = openWeb('fonseca-ganade.web',t=False,name='FonsecaGanade',species_names=False)
# Naming the upper trophic level species
rw.upnames = ['Caba','Azal','Azis','Azaf','AlD','Alpr','Alaf','SoA','Alau','CrB','AzHC',
'AzG','CrD','AzCO','Phmi','CrA','AzTO','CrC','Azsc','Psni','Psco','AzD','Azpo',
'CrE','AzQ']
# Naming the lower trophic level species
rw.lonames = ['Cepu','Ceco','Cedi','Cefi','Pohe','Himy','Hiph','Dusa','Cono','Coaf','Tobu',
'Magu','Mapo','Tapo','Tamy','Amaf']
{% endhighlight %}

At the end of this step, we have a `rw` object, which is an instance of the [`bipartite` class]({{ site.url }}/reference/classes/bipartite/). This class is one of the core features of *bipy*, and when called, will calculate most of the informations you need to have about a network.

## Step 2 : printing informations about the species

## Step 3 : printing informations about the network

## Step 4 : plotting the network

## Step 5 : checking robustness to extinction

Robustness to extinctions is done by removing species from either trophic level, and counting the number of species from the other trophic levels with no links remaining. When creating a `bipartite` object, a `robustness` class is created. This class has several methods, corresponding to different extinction scenarios. To perform the complete analysis, type:

{% highlight pyhon linenos %}
w.robustness.do_random(200)
w.robustness.do_stog(1)
w.robustness.do_gtos(1)
{% endhighlight %}

The `do_` commands correspond to the different extinction scenarios (resp. at random, from specialists to generalists, and from generalists to specialists). By convention, each of these function accept one argument, corresponding to the number of replicates to do. The `robustness` class has a `__str__` methodm so that you can view the results of the analysis with

{% highlight python linenos %}
print w.robustness
{% endhighlight %}

In addition, there is a plot method associated to this class, so that you can have a visual output of the analysis using *PyX*.

## Step 6 : assessing the significancy of the patterns

## Step 7 : conclusion

<div class='ref'>Fonseca, C.R., and G. Ganade. 1996. Asymmetries, compartments and null interactions in an Amazonian ant-plant community. Journal of Animal Ecology 66: 339-347.</div>