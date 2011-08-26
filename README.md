### bipy

*bipy* is a collection of python scripts to analyze and visualize two-mode (bipartite) networks, mostly aimed at ecological datasets

**Author** : Timothee Poisot <tpoisot@um2.fr>  
**Language** : Python  >= 2.6  
**Requires** : numpy, scipy, pyx, pymysql, tempfile, urllib, pp 

See the wiki at <http://bipy.timotheepoisot.fr/> for examples

### Some features are…

**null models** : based on connectance (*nullC*, *null1*) or marginal probabilities of interactions (*null2*)  
**measures of nestedness** : only the highly robust NODF measure is implemented  
**modularity detection** : LP-BRIM algorithm with asynchronous random propagation, uses Barber's modularity, including parallel version of it using *p_findModules*  
**visualization of networks** : *plotMatrix* and *plotModules*, with the possibility to color links according to their strength  
**ability to read data from the web** : *readRemoteWeb* with the URL of a textfile  
**integration with a database** : still heacily experimental, but allows to request webs and informations from a central database  
**integration of bibliographical informations** : can associate a dataset with a DOI, PMID, or JSTOR stable identifier, and get a link or the full references of the paper  
**a feature-rich class** : defines the *bipartite* class to automate most of the calculations and gain time when using null models