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

test_web = test(w,null_2,100,verbose=False)

test_web.nestedness()
test_web.modularity(10)

print test_web