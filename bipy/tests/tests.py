## Tests of deviation from the null models

from ..nes import *
from ..mod import *
from ..bipartite_class import *

import scipy.stats as spp

def gMIC(distrib):
	estimates = spp.bayes_mvs(distrib)[0]
	return[estimates[0],estimates[1][0],estimates[1][1]]

## excess modularity
def getDevNest(w,list):
	expect = []
	for i in list:
		expect.append(bipartite(i).nodf)
	testRes = stats.ttest_1samp(expect, w.nodf)
	OUT = [w.nodf,testRes[1]]
	est = gMIC(expect)
	for est_par in est:
		OUT.append(est_par)
	return OUT


## excess modularity
def getDevQr(w,list):
	m = [w.modules.Q,w.modules.N,w.modules.up_modules,w.modules.low_modules]
	Qsim = []
	wQr = Qr(w,m)
	for i in list:
		Qsim.append(Qr(bipartite(i),m))
	testRes = stats.ttest_1samp(Qsim, wQr)
	OUT = [wQr,testRes[1]]
	est = gMIC(Qsim)
	for est_par in est:
		OUT.append(est_par)
	return OUT


## excess bipartite modularity
def getDevQbip(w,list):
	Qsim = []
	wQ = w.modules.Q
	for i in list:
		Qsim.append(Qbip(bipartite(i),w.modules.up_modules,w.modules.low_modules))
	testRes = stats.ttest_1samp(Qsim, wQ)
	OUT = [wQ,testRes[1]]
	est = gMIC(Qsim)
	for est_par in est:
		OUT.append(est_par)
	return OUT
