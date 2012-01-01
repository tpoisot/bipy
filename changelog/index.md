---
layout: page
title: BIPY - Changelog
---

This page lists the most notable changes between the stable releases. The current development snapshot can be found on the [dev](https://github.com/tpoisot/bipy/tree/dev) branch (which is often unstable, but can offer some interesting new features).

## Version 1.0

### 1.0.2 ([zip](https://github.com/tpoisot/bipy/zipball/sr_v1.0.2))

Minor release

* Faster measures of nestedness and modularity
* `q_c` replaced by `use_c`, also used by nestedness
* import from and export to NetworkX
* method `save` in bipartite using `pickle` to keep a bipartite object
* function `load` to import a previously saved object
* `networklevel` method to output summary statistics

### 1.0.1 ([zip](https://github.com/tpoisot/bipy/zipball/sr_v1.0.1))

Minor release

* Robustness analyses are now in a class of their own
* Improvements in the speed of modularity analysis, nestedness testing, null models, and specificity measures
* Modification of the `mod` sub-module (now takes a raw rather bipartite network)
* `plot` method in the `robustness` class of `bipartite`
* `bipartite` class gains the `txt` and `plot` methods

### 1.0.0 ([zip](https://github.com/tpoisot/bipy/zipball/sr_v1.0.0))

* First stable release
