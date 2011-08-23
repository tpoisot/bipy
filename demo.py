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


## Comparison of class vs. non-class objects
import time

toN3D(w)

def time_it(f, *args):
       start = time.clock()
       f(*args)
       return (time.clock() - start)*1000

time_D  = []
time_C  = []
time_D2 = []
time_C2 = []
time_sD = []
time_sC = []
for i in range(10):
	time_D.append(time_it(null1,data))
	time_C.append(time_it(null1,w))
	time_D2.append(time_it(null2,data))
	time_C2.append(time_it(null2,w))
	time_sD.append(time_it(sortbydegree,data))
	time_sC.append(time_it(sortbydegree,w))

print ""
print ""
print "Mean time (in ms) for a null-model based on connectance"
print "class should be 10ms faster with the demo data"
print("With the class object : "+str(mean(time_C)))
print("With the raw object   : "+str(mean(time_D)))
print ""
print "Mean time (in ms) for a null-model based on marginal sums"
print "class should be 40 % faster with the demo data"
print("With the class object : "+str(mean(time_C2)))
print("With the raw object   : "+str(mean(time_D2)))
print ""
print "Mean time (in ms) to sort a matrix by degree"
print "class should be 40 % faster with the demo data"
print("With the class object : "+str(mean(time_sC)))
print("With the raw object   : "+str(mean(time_sD)))

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
