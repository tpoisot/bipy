from bipy import *

print "Reading the network file..."
print ""


w = bipartite(readweb('modular.web'),t=False)
prettyprint(w.web)

## These are the correct modules
og = [1,1,1,1,2,2,2,2,2,3,3,3,3,3]
oh = [1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,3]

print ""
print "The modular network was hand-made"
print "so that we expect 3 modules and Qbip: "+str(Qbip(w,og,oh))
print ""
findModules(w,10) # Needs a number of replicates