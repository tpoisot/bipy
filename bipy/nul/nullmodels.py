import scipy as sp
import numpy as np
from ..mainfuncs import *
from ..gen import *
from ..spe import *
import pp

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
	if hasattr(W,'connectance'):
		C = W.connectance
		Wp = nullC(len(W.web),len(W.web[0]),C)
	else:
		C = connectance(W)
		Wp = nullC(len(W),len(W[0]),C)
	return fixmat(Wp)


## Null model 2 (constrained)
def null2(W):
	# Generate a random network based on the
	# probability that a row and a column
	# have an interaction in the overall
	# web
	import numpy as np
	if hasattr(W,'connectance'):
		adj = W.adjacency
		g = W.generality
		v = W.vulnerability
		upsp = W.upsp
		losp = W.losp
	else:
		adj = adjacency(W)
		g = generality(W)
		v = vulnerability(W)
		upsp = len(adj)
		losp = len(adj[0])
		
	for i in range(upsp):
		g[i] = g[i]/float(losp)
	for j in range(losp):
		v[j] = v[j]/float(upsp)
	# Generate a random web
	Wp = np.zeros((upsp,losp))
	for i in range(upsp):
		for j in range(losp):
			IsInt = np.random.uniform(0,1,(1,))
			ProbInt = (g[i]+v[j])/2
			if ProbInt > IsInt:
				Wp[i][j] = 1
	return fixmat(Wp)
	


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
		ListOfNulls.append(job())
	return ListOfNulls


## Global wrapper around the null models
def nullModel(W,null=1,nreps=1,ncpus=1):
	if ncpus == 1:
		out = []
		if null == 1:
			for i in range(nreps):
				out.append(null1(W))
		else:
			for i in range(nreps):
				out.append(null2(W))
	else:
		if null == 1:
			out = p_null1(W,nreps=nreps,ncpu=ncpus)
		else:
			out = p_null2(W,nreps=nreps,ncpu=ncpus)
	return out