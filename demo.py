#from bipy import *
import bipy as bp
import numpy as np

print "Reading the network file..."

print "Demo data were obtained from "
print "Bangham, R. V. 1955. American Midland Naturalist 53:184-194."

print ""
print ""

data = bp.readweb('demo.web').T

print "Some general infos:"
print "Connectance           : "+str(bp.connectance(data))+" "
print "Mean specificity      : "+str(np.mean(bp.specificity(data)))+" "
print "Nestedness (NODF)     : "+str(bp.nodf(data)[0])+" "

print ""
print ""

# The bipartite class is able to transpose the matrix
w = bp.bipartite(bp.readweb('demo.web'),t=True)
demo_ref = {"jstor":2422308}
w.ref = bp.ref(demo_ref)
print "Some general infos (using the bipartite class):"
print "Connectance                   : "+str(w.connectance)+" "
print "Mean specificity              : "+str(np.mean(w.specificity))+" "
print "Mean number of hosts          : "+str(np.mean(w.generality))+" "
print "Mean number of parasites      : "+str(np.mean(w.vulnerability))+" "
print "Nestedness (NODF)             : "+str(w.nodf)+" "
print "Network size                  : "+str(w.size)+" "
bp.output_citinfo(w)