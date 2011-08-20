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
print "Mean specificity      : "+str(mean(specificity(data)))+" "

print ""
print ""

w = bipartite(readweb('demo.web').T)
print "Some general infos (using the bipartite class):"
print "Connectance                   : "+str(w.connectance)+" "
print "Mean specificity              : "+str(mean(w.specificity))+" "
print "Mean number of hosts          : "+str(mean(w.generality))+" "
print "Mean number of parasites      : "+str(mean(w.vulnerability))+" "
print "Nestedness (NODF)             : "+str(w.nodf)+" "
print "Network size                  : "+str(w.size)+" "

## EXAMPLE OF GRAPHICS
## If you have pyx installed, uncomment the following : 
#from pyx import *
#
#text.set(mode="latex")
#text.preamble(r"\usepackage{fourier}")
#
#spedistrib = d2h(generality(data))
#
#g = graph.graphxy(width=8,
#	x = graph.axis.linear(title='Degree',min=0,max=12),
#	y = graph.axis.linear(title='Count',min=0,max=6))
#g.plot(graph.data.points(spedistrib,x=1,y=2), [graph.style.histogram()])
#g.writePDFfile("specificity")
