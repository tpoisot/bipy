from bipy import *

print "Reading the network file..."
print "Ant-plant data from Fonseca & Ganade"
print "Species names for Genus species is Gesp"
print ""
rw = bipartite(readweb('fonseca.web'))
rw.upnames = ['Caba','Azal','Azis','Azaf','AlD','Alpr','Alaf','SoA','Alau','CrB','AzHC','AzG','CrD','AzCO','Phmi','CrA','AzTO','CrC','Azsc','Psni','Psco','AzD','Azpo','CrE','AzQ']
rw.lonames = ['Cepu','Ceco','Cedi','Cefi','Pohe','Himy','Hiph','Dusa','Cono','Coaf','Tobu','Magu','Mapo','Tapo','Tamy','Amaf']
modules = findModules(rw,10)

print "Some statistics for the upper trophic level species"
print ""
print "--------------------------------"
print "SPECIES\tGENER.\tSPECIF.\tMOD. #"
print "--------------------------------"
for i in range(rw.upsp):
	print rw.upnames[i]+'\t'+str(rw.generality[i])+'\t'+str(round(rw.specificity[i],2))+'\t'+str(modules[2][i])
print "--------------------------------"

#plotWeb(rw,modules,asbeads=True)
#plotWeb(rw,asnest=True,asbeads=True,filename='webN')