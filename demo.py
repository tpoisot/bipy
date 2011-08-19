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
