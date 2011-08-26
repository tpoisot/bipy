from bipy import *

# Open the database connection
db = connectToDB()

print "Reading a remote file on NCEAS server"
print ""

ResUrl = "http://www.nceas.ucsb.edu/interactionweb/data/host_parasite/text_matrices/aishihik_p.txt"

rw = readRemoteWeb(ResUrl,True,True)
prettyprint(sortbydegree(rw.web))

print ""
print "Reading a list of all networks available in the WebDB"
print ""
AllId = websOnDB(db,cat='all')
print ""
print """The function `getListOfWebs` returns an array with the ID of
the webs matching the request, so that you can store and use this information
at a later time."""
print ""
print "Accessing and printing web number 2"
print ""

DBw = getWebById(db,AllId[1])
prettyprint(DBw.web)
plotMatrix(DBw)

# Close the database connection !
# Do not forget to do it, or else ...
closeDBconnect(db)