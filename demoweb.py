from bipy import *


print "Reading a remote file on NCEAS server"
print ""

ResUrl = "http://www.nceas.ucsb.edu/interactionweb/data/host_parasite/text_matrices/aishihik_p.txt"

rw = readRemoteWeb(ResUrl,True,True)
prettyprint(sortbydegree(rw.web))

#infs = {'name':'up_test','cat':'test','utl':'insects','ltl':'plants','comment':'Example network to show the possibility to upload to the database'}
#pushWebToDB(db,1,rw,infs)

print ""
print "Reading a list of all networks available in the WebDB"
print ""
AllId = getWebsFromDB(cat='all')
print ""
