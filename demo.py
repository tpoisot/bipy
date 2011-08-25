from bipy import *

print "Reading the network file..."

print "Demo data were obtained from "
print "Bangham, R. V. 1955. American Midland Naturalist 53:184-194."

print ""
print ""

data = readweb('demo.web').T

print "Some general infos:"
print "Connectance           : "+str(connectance(data))+" "
print "Mean specificity      : "+str(mean(specificity(data)))+" "
print "Nestedness (NODF)     : "+str(nodf(data)[0])+" "

print ""
print ""

# The bipartite class is able to transpose the matrix
w = bipartite(readweb('demo.web'),t=True)
demo_ref = {"jstor":2422308}
w.ref = ref(demo_ref)
print "Some general infos (using the bipartite class):"
print "Connectance                   : "+str(w.connectance)+" "
print "Mean specificity              : "+str(mean(w.specificity))+" "
print "Mean number of hosts          : "+str(mean(w.generality))+" "
print "Mean number of parasites      : "+str(mean(w.vulnerability))+" "
print "Nestedness (NODF)             : "+str(w.nodf)+" "
print "Network size                  : "+str(w.size)+" "
output_citinfo(w)