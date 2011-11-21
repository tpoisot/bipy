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
#rw.modules = modules(rw,reps=50)

Dnodf1 = []
Dnodf2 = []
Dnodf3r = []
Dnodf3c = []

print 'Null 1'
n1 = nullModel(rw,null_1,replicates=10)
print 'Null 2'
n2 = nullModel(rw,null_2,replicates=10)
print 'Null 3 rows'
n3r = nullModel(rw,null_3row,replicates=10)
print 'Null 3 cols'
n3c = nullModel(rw,null_3col,replicates=10)

for r1 in n1:
	Dnodf1.append(rw.nodf-bipartite(r1).nodf)

for r2 in n2:
	Dnodf2.append(rw.nodf-bipartite(r2).nodf)

for r3r in n3r:
	Dnodf3r.append(rw.nodf-bipartite(r3r).nodf)

for r3c in n3c:
	Dnodf3c.append(rw.nodf-bipartite(r3c).nodf)

print stats.ttest_1samp(Dnodf1, 0)
print stats.ttest_1samp(Dnodf2, 0)
print stats.ttest_1samp(Dnodf3r, 0)
print stats.ttest_1samp(Dnodf3c, 0)