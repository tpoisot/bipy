from bipy import *

print "Reading the network file..."
print ""


w = bipartite(readweb('modular.web'),t=False)
prettyprint(w.web)

## These are the correct modules
g = [1,1,1,1,2,2,2,2,2,3,3,3,3,3]
h = [1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,3]

print ""
print "The modular network was hand-made"
print "so that we expect Qbip: "+str(Qbip(w,g,h))
print ""
LP(w)