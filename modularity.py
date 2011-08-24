from bipy import *

print "Reading the network file..."
print ""

w = bipartite(readweb('modular.web'),t=False)
prettyprint(w.web)

print ""
print "The modular network was hand-made"
print "so that we expect 3 modules"
print ""
#w = bipartite(readweb('demo.web'),t=True)
modulinfo = findModules(w,10,5) # Needs a number of replicates

#splitWeb(w,modulinfo)

rw = readRemoteWeb('http://www.nceas.ucsb.edu/interactionweb/data/host_parasite/text_matrices/aishihik_p.txt')
prettyprint(rw.web)

# The following line prints a web grouped by modules
plotModules(w,modulinfo,filename='web_by_modules',col=True)
# compare with the result of the function printing it by degree
plotMatrix(w,filename='web_by_degree',asnest=True)