import scipy as sp
import numpy as np
from ..mainfuncs import *
from ..gen import *
from ..spe import *

def nullC(ntop=30,nbottom=30,conn=0.5):
	Nsize = ntop * nbottom
	Wp = np.zeros((ntop,nbottom))
	for i in range(ntop):
		for j in range(nbottom):
			IsInt = np.random.uniform(0,1,(1,))
			if conn > IsInt:
				Wp[i][j] = 1
	return fixmat(Wp)

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

def null2(W):
	# Generate a random network based on the
	# probability that a row and a column
	# have an interaction in the overall
	# web
	
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
	
