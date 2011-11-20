### bipy

*bipy* is a collection of python scripts to analyze and visualize two-mode (bipartite) networks, mostly aimed at ecological datasets

*bipy* is released under the terms of the GNU GPL <http://en.wikipedia.org/wiki/GNU_General_Public_License>

**Author** : Timothee Poisot <tpoisot@um2.fr>  
**Language** : Python  >= 2.6  
**Requires** : numpy, scipy, pyx, tempfile, urllib, pp 

### Some features are…

**null models** : based on connectance (*nullC*, *null1*) or marginal probabilities of interactions (*null2*)  
**measures of nestedness** : only the highly robust NODF measure is implemented  
**modularity detection** : LP-BRIM algorithm with asynchronous random propagation, uses Barber's modularity
**visualization of networks** : *plotWeb* function can draw networks as lines or matrices, according to nestedness or modularity  
**ability to read data from the web** : *readRemoteWeb* with the URL of a textfile  
**integration of bibliographical informations** : can associate a dataset with a DOI, PMID, or JSTOR stable identifier, and get a link or the full references of the paper  
**a feature-rich class** : defines the *bipartite* class to automate most of the calculations and gain time when using null models
**species-names integration** : the name of each species in the network is used in reporting functions and graphics  