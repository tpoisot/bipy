import scipy as sp
import numpy as np

from ..mainfuncs import *
from ..base import *
from ..spe import *

## Null model C (needs the size and connectance)
def nullC(ntop=30,nbottom=30,conn=0.5):
	import numpy as np
	Nsize = ntop * nbottom
	Wp = np.zeros((ntop,nbottom))
	for i in range(ntop):
		for j in range(nbottom):
			IsInt = np.random.uniform(0,1,(1,))
			if conn > IsInt:
				Wp[i][j] = 1
	return fixmat(Wp)


## Null model 1 (connectance based)
def null1(W):
	# Generate a random network based on the
	# overall connectance of the web
	Wp = nullC(W.upsp,W.losp,W.connectance)
	fmw = fixmat(Wp)
	if (len(fmw.shape) == 2):
		if (fmw.shape[0] == W.upsp)&(fmw.shape[1] == W.losp):
			fmw = mini_bipartite(fmw)
		else:
			fmw = np.zeros((0,0))
	else:
		fmw = np.zeros((0,0))
	return fmw


## Null model 2 (constrained)
def null2(W):
	# Generate a random network based on the
	# probability that a row and a column
	# have an interaction in the overall
	# web
	# Random matrix of probabilities
	IsInt = np.random.uniform(0,1,(W.upsp,W.losp))
	# Generate a random web
	Wp = np.zeros((W.upsp,W.losp))
	for i in range(W.upsp):
		for j in range(W.losp):
			ProbInt = (W.upsp*W.generality[i]+W.losp*W.vulnerability[j])/float(2*W.size)
			if ProbInt > IsInt[i][j]:
				Wp[i][j] = 1
	fmw = fixmat(Wp)
	if (len(fmw.shape) == 2):
		if (fmw.shape[0] == W.upsp)&(fmw.shape[1] == W.losp):
			fmw = mini_bipartite(fmw)
		else:
			fmw = np.zeros((0,0))
	else:
		fmw = np.zeros((0,0))
	return fmw


## Global wrapper around the null models
def nullModel(W,fun=null1,nreps=1,ncpus=1,maxiter=10000):
	out = []
	i = 0
	while (len(out) < nreps)&(i<maxiter):
		i += 1
		## Do the null web
		tnmod = fun(W)
		## Check it
		if hasattr(tnmod,'upsp'):
			out.append(tnmod)
	print str(len(out))+' null webs generated in '+str(i)+' iterations'
	return out
