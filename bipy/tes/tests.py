## Tests of deviation from the null models

from ..nes import *

## excess modularity
def getDevNest(w,list):
	print w.upsp
	print w.losp
	deviation = []
	for i in list:
		ni = nodf(i)
		deviation.append(w.nodf-ni[0])
	return deviation
	
## excess modularity
def getDevMod(w,m,list):
	Qsim = []
	wQr = Qr(w,m)
	for i in list:
		ExcQ = wQr - Qr(bipartite(i),m)
		Qsim.append(ExcQ)
	return Qsim