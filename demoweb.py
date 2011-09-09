from bipy import *


print "Reading a remote file on NCEAS server"
print ""

ResUrl = "http://www.nceas.ucsb.edu/interactionweb/data/host_parasite/text_matrices/aishihik_p.txt"

rw = readRemoteWeb(ResUrl,True)
prettyprint(sortbydegree(rw.web))

print ""
print "Reading a list of all networks available in the WebDB"
print ""
AllId = getWebsFromDB(cat='all')
print ""

W = getWebById(2)

print W.ref.fulltext
print W.name