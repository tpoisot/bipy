---
layout: page
title: BIPY - Tutorial
---

# A step-by-step introduction

The goal of this tutorial is to cover the things that *bipy* is able to do. More extensive information can be found in the [reference]({{ site.url }}/reference/) pages, in which a detailed list of the built-in functionalities can be found.

This tutorial require that you have installed *bipy* in your local Python distribution. We will work on the data by [Fonseca & Ganade (1996) dataset]({{ site.url }}/tutorial/fonseca-ganade.web). To use another dataset, see the page about [loading data]({{ site.url }}/reference/data/reading/).

## Step 1 : loading the data and naming the species

To load the data and give name to the species, the following commands are used:

{% highlight python %}
# Loading bipy
from bipy import *
# Reading the network, and giving it a name
w = openWeb('fonseca-ganade.web',
	t=False,name='FonsecaGanade',
	species_names=False)
# Naming the upper trophic level species
w.upnames = ['Caba','Azal','Azis','Azaf','AlD','Alpr',
		'Alaf','SoA','Alau','CrB','AzHC','AzG','CrD',
		'AzCO','Phmi','CrA','AzTO','CrC','Azsc','Psni',
		'Psco','AzD','Azpo','CrE','AzQ']
# Naming the lower trophic level species
w.lonames = ['Cepu','Ceco','Cedi','Cefi','Pohe','Himy',
	'Hiph','Dusa','Cono','Coaf','Tobu','Magu','Mapo',
	'Tapo','Tamy','Amaf']
{% endhighlight %}

At the end of this step, we have a `rw` object, which is an instance of the [`bipartite` class]({{ site.url }}/reference/classes/bipartite/). This class is one of the core features of *bipy*, and when called, will calculate most of the informations you need to have about a network.

## Step 2 : printing informations about the species

Most of the informations about the species in the network can be accessed through the `specieslevel` method of `bipartite`. The following command:

{% highlight python %}
w.specieslevel(True,True)
{% endhighlight %}

will output both to the screen and to a file a table will all informations about the species in your network. Note that not all informations are available for all species (i.e. there is no value of specificity for the lower trophic level species). When new analyses like the one described below are done, their results are added to your `bipartite` object, and you may want to run `specieslevel` (and similarly for `networklevel`) as the last command in your script.

At this point, `bipy` has already calculated most of the metrics, expect the one that are computationally intensive (you may not need them, so they are only calculated on demand). More species-level metrics (e.g. different measures of centrality) will be added in future versions.

## Step 3 : printing informations about the network

Similarly to the `specieslevel` command, the `bipartite` class defines a `networklevel` method.

{% highlight python %}
w.networklevel()
{% endhighlight %}

It works slightly differently from the `specieslevel` command, in that successive calls of this command will be outputed to a single text file, to allow comparison between different networks, and/or test of the same network against different null models. For this reason, it is important the this command is called, for each network, at the same point of the analysis, as the header of the text file is only printed once.

## Step 4 : plotting the network

The simplest way to output a network is to print it to the console in text form. The `txt` method of `bipartite` is doing this, so that you can type

{% highlight python %}
w.txt()
{% endhighlight %}

You should see something like this:

{% highlight bash %}
█---------------
█---------------
████------------
█--█------------
----█-----------
------█---------
-----███--------
------██--------
-------█-█------
-------███------
---------█------
---------███----
---------██-----
---------█------
----------███---
------█---███---
----------█-----
----------█-█---
-------------██-
-------------██-
-------------██-
--------------█-
--------------█-
---------█----█-
---------------█
{% endhighlight %}

Full blocks correspond to interactions, and dashes correspond to no interactions.

Of course, *bipy* offers more pleasing ways to plot networks, using *PyX*. There are two broad categories of plots: as a matrix (like the text version above), and as beads connected by strings. Both of them are handled by the `plot` method of `bipartite`, which provides several options.

{% highlight python %}
# Plot as a matrix, to reflect nestedness
# with colors
w.plot(asNest=True,asBeads=False,color=True)
# Plot as a matrix, to reflect modularity
# with no colors
w.plot(asNest=False,asBeads=False,color=False)
# Plot as beads, to reflect modularity
w.plot(asNest=False,asBeads=True)
# Plot as beads, to reflect nestedness
w.plot(asNest=True,asBeads=True)
{% endhighlight %}

## Step 5 : checking robustness to extinction

Robustness to extinctions is done by removing species from either trophic level, and counting the number of species from the other trophic levels with no links remaining. When creating a `bipartite` object, a `robustness` class is created. This class has several methods, corresponding to different extinction scenarios. To perform the complete analysis, type:

{% highlight python %}
w.robustness.do_random(200)
w.robustness.do_stog(1)
w.robustness.do_gtos(1)
{% endhighlight %}

The `do_` commands correspond to the different extinction scenarios (resp. at random, from specialists to generalists, and from generalists to specialists). By convention, each of these function accept one argument, corresponding to the number of replicates to do. The `robustness` class has a `__str__` methodm so that you can view the results of the analysis with

{% highlight python %}
print w.robustness
{% endhighlight %}

In addition, there is a plot method associated to this class, so that you can have a visual output of the analysis using *PyX*.

{% highlight python %}
print w.robustness.plot()
{% endhighlight %}

This command will create a `pdf` file, with the name of the current network, in the current working directory.

## Step 6 : finding modularity

## Step 7 : testing the significancy of the patterns

## Step 8 : conclusion

<div class='ref'>Fonseca, C.R., and G. Ganade. 1996. Asymmetries, compartments and null interactions in an Amazonian ant-plant community. Journal of Animal Ecology 66: 339-347.</div>