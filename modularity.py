from bipy import *

print "Reading the network file..."
print ""

w = bipartite(readweb('modular.web'),t=False)
prettyprint(w.web)

# Parallel

start_time = time.time()
print p_findModules(w,reps=10,ncpu=1)
print "Time elapsed: ", time.time() - start_time, "s"

start_time = time.time()
print findModules(w,reps=10)
print "Time elapsed: ", time.time() - start_time, "s"

print ""
print "The modular network was hand-made"
print "so that we expect 3 modules"
print ""
#w = bipartite(readweb('demo.web'),t=True)
#modulinfo = findModules(w,100,5) # Needs a number of replicates

# The following line prints a web grouped by modules
#plotModules(w,modulinfo,filename='web_by_modules',col=True)
# compare with the result of the function printing it by degree
#plotMatrix(w,filename='web_by_degree',asnest=True)