import scipy as sp
import numpy as np
from ..mainfuncs import *
from ..gen import *
from ..spe import *
from ..bipartite_class import *
import pp
from sys import stdout

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
	return mini_bipartite(fixmat(Wp))


## Null model 2 (constrained)
def null2(W):
	# Generate a random network based on the
	# probability that a row and a column
	# have an interaction in the overall
	# web
	g = []
	v = []
	for i in range(W.upsp):
		g.append(W.generality[i]/float(W.losp))
	for j in range(W.losp):
		v.append(W.vulnerability[j]/float(W.upsp))
	# Generate a random web
	Wp = np.zeros((W.upsp,W.losp))
	for i in range(W.upsp):
		for j in range(W.losp):
			IsInt = np.random.uniform(0,1,(1,))
			ProbInt = (g[i]+v[j])/2
			if ProbInt > IsInt:
				Wp[i][j] = 1
	return mini_bipartite(fixmat(Wp))
	


## Parallel wrapper for the null model 1
def p_null1(W,nreps=100,ncpu=2):
	# Generate a long replication of the web
	ListOfArgs = []
	for i in range(nreps):
		ListOfArgs.append(W)
	# Initiate parallel
	job_server = pp.Server(ncpu, ppservers=())
	print "Starting parallel generation of null models on", job_server.get_ncpus(), "CPU(s)"
	jobs = [(input, job_server.submit(null1, (input,), (fixmat, websize, generality, vulnerability, nullC, ), ())) for input in ListOfArgs]
	ListOfNulls = []
	for input, job in jobs:
		if (websize(job()) == W.size):
			ListOfNulls.append(job())
	return ListOfNulls


## Parallel wrapper for the null model 2
def p_null2(W,nreps=100,ncpu=2):
	# Generate a long replication of the web
	ListOfArgs = []
	for i in range(nreps):
		ListOfArgs.append(W)
	# Initiate parallel
	job_server = pp.Server(ncpu, ppservers=())
	print "Starting parallel generation of null models on", job_server.get_ncpus(), "CPU(s)"
	jobs = [(input, job_server.submit(null2, (input,), (fixmat, websize, generality, vulnerability, ), ())) for input in ListOfArgs]
	ListOfNulls = []
	for input, job in jobs:
		if (websize(job()) == W.size):
			ListOfNulls.append(job())
	return ListOfNulls


## Global wrapper around the null models
def nullModel(W,null=1,nreps=1,ncpus=1,maxiter=10000):
	out = []
	i = 0
	while (len(out) < nreps)&(i<maxiter):
		i += 1
		## Do the null web
		if null == 1:
			tnmod = null1(W)
		else:
			tnmod = null2(W)
		## Check it
		sha = tnmod.web.shape
		if (sha[0]==W.upsp)&(sha[1]==W.losp):
			out.append(null1(W))
		currentRep = round(100*(len(out)/float(nreps)),0)
		stdout.write("\r%g   " % currentRep)
		stdout.flush()
	stdout.write("\r    \r\n")
	print str(nreps)+' null webs generated in '+str(i)+' iterations\n'
	return out
