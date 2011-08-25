from bipy import *

print "Reading a remote file on NCEAS server"
print ""

ResUrl = "http://www.nceas.ucsb.edu/interactionweb/data/host_parasite/text_matrices/aishihik_p.txt"

rw = readRemoteWeb(ResUrl,True,True)
prettyprint(sortbydegree(rw.web))

print ""
print "Reading a list of all networks available in the WebDB"
print ""
AllId = getListOfWebs('all')
print ""
print """The function `getListOfWebs` returns an array with the ID of
the webs matching the request, so that you can store and use this information
at a later time."""
print ""
print "Accessing and printing web number 2"
print ""

prettyprint(getWebById(AllId[1]).web)