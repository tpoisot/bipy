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

w = bipartite(readweb('demo.web').T)
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


## Comparison of class vs. non-class objects
import time

def time_it(f, *args):
       start = time.clock()
       f(*args)
       return (time.clock() - start)*1000

time_D = []
time_C = []
for i in range(50):
	time_D.append(time_it(null1,data))
	time_C.append(time_it(null1,w))

print ""
print ""
print "Mean time (in ms) for a null-model based on connectance"
print "class should be roughly 100 ms faster with a network"
print "size of "+str(w.size)+" interactions."
print("With the class object : "+str(mean(time_C)))
print("With the raw object   : "+str(mean(time_D)))

# EXAMPLE OF GRAPHICS
# If you have pyx installed, uncomment the following : 
# from pyx import *
# 
# text.set(mode="latex")
# text.preamble(r"\usepackage{fourier}")
# 
# g = graph.graphxy(width=8,
# 	x = graph.axis.linear(title='Degree',min=0,max=20),
# 	y = graph.axis.linear(title='Count',min=0,max=80))
# g.plot(graph.data.points(d2h(w.generality,'rice'),x=1,y=2), [graph.style.histogram()])
# g.writePDFfile("generality")
