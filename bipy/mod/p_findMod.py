import pp
from ..nul import *
from ..mainfuncs import *
from .lpbrim import *

import time

def LPBRIM(W):
	import scipy as sp
	import numpy as np
	LPpart = LP(W)
	BRIMpart = BRIM(W,LPpart)
	return BRIMpart

## Find modules
def p_findModules(W,reps=10,ncpu=1):
	maxMod = 0
	LPBRIM(W)
	ListOfArgs = []
	for i in range(reps):
		ListOfArgs.append(W)
	# Start parallel server
	job_server = pp.Server(ncpu, ppservers=())
	print "Starting parallel optimization of modularity on", job_server.get_ncpus(), "CPU(s)"
	jobs = [(input, job_server.submit(LPBRIM, (input,), (LP, BRIM, mostFrequent, Qbip, getRTfp, uniquify, getCVfromCM, ), ("random",))) for input in ListOfArgs]
	for input, job in jobs:
		if job()[0] > maxMod:
			maxMod = job()[0]
			out = job()
	return out
