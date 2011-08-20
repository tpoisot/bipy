from bipy import *

print "Reading the network file..."
data = readweb('wBL.web')


print "Some general infos..."
print "Connectance           : "+str(connectance(data))+" "
print "Mean specificity      : "+str(mean(specificity(data)))+" "
print "Nestedness (NODF)     : "+str(nodf(data)[0])+" "

print ""
print "The network looks like this :"
prettyprint(nestadj(data))

print ""
print ""
print "Using the bipartite class..."
w = bipartite(readweb('wBL.web'))


print "Some general infos..."
print "Connectance           : "+str(w.connectance)+" "
print "Mean specificity      : "+str(mean(w.specificity))+" "
print "Nestedness (NODF)     : "+str(w.nodf)+" "

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
