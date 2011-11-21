from bipy import *

print "Reading the network file..."
print "Ant-plant data from Fonseca & Ganade"
print "Species names for Genus species is Gesp"
print ""

rw = loadweb('fonseca.web',name='FonsecaGanade')
# We assign species level
rw.upnames = ['Caba','Azal','Azis','Azaf','AlD','Alpr','Alaf','SoA','Alau','CrB','AzHC','AzG','CrD','AzCO','Phmi','CrA','AzTO','CrC','Azsc','Psni','Psco','AzD','Azpo','CrE','AzQ']
rw.lonames = ['Cepu','Ceco','Cedi','Cefi','Pohe','Himy','Hiph','Dusa','Cono','Coaf','Tobu','Magu','Mapo','Tapo','Tamy','Amaf']
# We compute the modularity
rw.modules = modules(rw,reps=50)

print 'Null 2'
n2 = nullModel(rw,null_2,replicates=4)

print 'Test for nestedness'
print testDeviation(getDevNest(rw,n2))
print 'Test for QR'
print testDeviation(getDevQr(rw,n2))
print 'Test for Q bip'
print testDeviation(getDevQbip(rw,n2))