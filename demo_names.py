from bipy import *

print "Reading the network file..."
ResUrl = "http://www.nceas.ucsb.edu/interactionweb/data/ant_plant/text_matrices/fonseca&ganade.txt"
print "Fonseca & Ganade, plant--ant network"

rw = readRemoteWeb(ResUrl,True,False)
rw.upnames = ['Caba','Azal','Azis','Azaf','AlD','Alpr','Alaf','SoA','Alau','CrB','AzHC','AzG','CrD','AzCO','Phmi','CrA','AzTO','CrC','Azsc','Psni','Psco','AzD','Azpo','CrE','AzQ']
rw.lonames = ['Cepu','Ceco','Cedi','Cefi','Pohe','Himy','Hiph','Dusa','Cono','Coaf','Tobu','Magu','Mapo','Tapo','Tamy','Amaf']

modules = findModules(rw,10)

plotWeb(rw,modules,asbeads=True)
plotWeb(rw,asnest=True,asbeads=True,filename='webN')