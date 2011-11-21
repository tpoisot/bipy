## Tests of deviation from the null models

from ..nes import *
from ..mod import *
from ..bipartite_class import *

## excess modularity
def getDevNest(w,list):
	deviation = []
	for i in list:
		deviation.append(w.nodf-bipartite(i).nodf)
	testRes = stats.ttest_1samp(deviation, 0)
	return [w.nodf,np.mean(deviation),testRes[1],deviation]


## excess modularity
def getDevQr(w,list):
	m = [w.modules.Q,w.modules.N,w.modules.up_modules,w.modules.low_modules]
	Qsim = []
	wQr = Qr(w,m)
	for i in list:
		Qsim.append(wQr - Qr(bipartite(i),m))
	testRes = stats.ttest_1samp(Qsim, 0)
	return [wQr,np.mean(Qsim),testRes[1],Qsim]


## excess bipartite modularity
def getDevQbip(w,list):
	Qsim = []
	wQ = w.modules.Q
	for i in list:
		Qsim.append(wQ - Qbip(bipartite(i),w.modules.up_modules,w.modules.low_modules))
	testRes = stats.ttest_1samp(Qsim, 0)
	return [wQ,np.mean(Qsim),testRes[1],Qsim]
