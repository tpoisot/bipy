from bipy import *

print "Reading the network file..."

rw = bipartite(readweb('fonseca.web'))
rw.upnames = ['Caba','Azal','Azis','Azaf','AlD','Alpr','Alaf','SoA','Alau','CrB','AzHC','AzG','CrD','AzCO','Phmi','CrA','AzTO','CrC','Azsc','Psni','Psco','AzD','Azpo','CrE','AzQ']
rw.lonames = ['Cepu','Ceco','Cedi','Cefi','Pohe','Himy','Hiph','Dusa','Cono','Coaf','Tobu','Magu','Mapo','Tapo','Tamy','Amaf']

modules = findModules(rw,10)

plotWeb(rw,modules,asbeads=True)
plotWeb(rw,asnest=True,asbeads=True,filename='webN')