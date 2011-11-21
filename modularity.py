from bipy import *
import time

print "Reading the network file..."
print ""

w = bipartite(readweb('modular.web'),t=False)

# Parallel
# Uncomment to test
# Of course, you need to have a multi-core machine
#start_time = time.time()
#p_modules = p_findModules(w,reps=1000,ncpu=7)
#print "Time elapsed: ", time.time() - start_time, "s"
# Tests with the demo data : 1000 repls in 2.3 sec

print ""
print "The modular network was hand-made"
print "so that we expect 3 modules"
print ""
start_time = time.time()
w.modules = modules(w,reps=10)
print "Time elapsed: ", time.time() - start_time, "s"

print 'Null 2'
n2 = nullModel(w,null_2,replicates=300)

print 'Test for nestedness'
print getDevNest(w,n2)
print 'Test for QR'
print getDevQr(w,n2)
print 'Test for Q bip'
print getDevQbip(w,n2)
