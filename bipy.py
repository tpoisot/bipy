##########
# bipy
##########
# A set of python functions to work on bipartite interaction networks
# Timothee Poisot - Universite Montpellier 2
# August 12, 2011
# Contact : tpoisot@um2.fr
##########
# Version using scipy / numpy
# Be sure to have them installed
import scipy as sp
import numpy as np
##########

def readweb(fname):
	# Read a web from a text matrix with top trophic level organisms as rows
	data = np.loadtxt(fname)
	return data

def linknum(W):
	# Number of established links within the web
	nl = 0;
	for links in W:
		for link in range(0,len(links)):
			if links[link] > 0:
				nl = nl + 1
	return nl

def websize(W):
	# Size of a web
	ntop = len(W)
	nbot= len(W[0])
	wsize = nbot * ntop
	return wsize

def connectance(W):
	# Connectance (as L/S^2)
	nl = linknum(W)
	ws = websize(W)
	connec = float(nl)/ws
	return connec

def generality(W):
	# Measure of generality
	#	Schoener, T. (1989) Ecology 70(6) 1559-1589
	gen = []
	for links in W:
		nl = 0
		for link in range(0,len(links)):
			if links[link] > 0:
				nl = nl + 1
		gen.append(nl)
	return gen

def vulnerability(W):
	# Measure of generality
	#	Schoener, T. (1989) Ecology 70(6) 1559-1589
	vul = generality(W.T)
	return vul

def specificity(W):
	# Measures the specialization using the Paired Differences Index
	#	Poisot, T, et al. (2011) Biol Lett 7(2) 201-204 10.1098/rsbl.2010.0774
	#	Poisot, T, et al. (in press) Proc R Soc Lon B 10.1098/rspb.2011.0826
	spe = []
	fit = 0
	for fit in W:
		tspe = 0
		fit = sorted(fit,reverse=True)
		i = 0
		ma = max(fit)
		while i < len(fit):
			fit[i] = fit[i]/float(ma)
			i = i+1
		i = 1
		while i < len(fit):
			tspe = tspe + ((fit[0]-fit[i])/(len(fit)-1))
			i = i+1
		spe.append(round(tspe,3))
	return spe	

def meanperf(W):
	# Mean performance of all TL species
	perf = []
	fit = 0
	for fit in W:
		tspe = 0
		i = 0
		while i < len(fit):
			tspe = tspe + fit[i]
			i = i+1
		tspe = tspe / len(fit)
		perf.append(round(tspe,3))
	return perf

def adjacency(W):
	# Transforms any matrix into an adjacency matrix
	ntop = len(W)
	nbot = len(W[0])
	for to in range(0,ntop):
		for bo in range(0,nbot):
			if W[to,bo] > 0:
				W[to,bo] = 1
	return W

def prettyprint(W):
	# Outputs a text version of the matrix
	# that can be viewed within the console
	W = adjacency(W)
	for tl in range(0,len(W)):
	    tLine = ''
	    for bl in range(0,len(W[0])):
	        if W[tl,bl] > 0:
	            tLine = tLine+'# '
	        else :
	            tLine = tLine+'- '
	    print tLine
	return 0

def rank(V):
	# Returns the rank of a vector
	# with no ties
	rn = np.zeros(len(V),dtype=np.int8)
	crnk = 0
	while crnk < len(V):
		for j in xrange(0,len(V)):
			cMax = max(V)
			if V[j] == cMax:
				rn[j] = crnk
				crnk += 1
				V[j] = min(V)-1
				break
	return rn

def sortbydegree(W):
	# Sort a matrix by degree
	# Better for visualization
	# Required for nestedness
	## Step 1 : sort TLO
	rG = rank(generality(W))
	nW = np.zeros((len(W),len(W[0])))
	for ro in range(0,len(W)):
		nW[rG[ro]] = W[ro]
	## Step 2 : sort BLO
	nW = nW.T
	dW = np.zeros((len(W),len(W[0]))).T
	rG = rank(generality(nW))
	for ro in range(0,len(W[0])):
		dW[rG[ro]] = nW[ro]
	return dW.T

def nestadj(W):
	# Returns as sorted binary matrix
	return sortbydegree(adjacency(W))
	
def compareones(w1,w2,tn):
	# Compare the identity of ONES
	id = 0.0
	for i in range(0,len(w1)):
		if (int(w1[i]) == 1)&(int(w2[i]) == 1):
			id = id + 1
	prop = (100*id)/tn
	return round(prop,2)

def nodf(W):
	# Measures NODF
	#	Almeida-Neto, M, et al. (2008) Oikos 117(8) 1227-1239
	
	# Step 1 : reorganize the adjacency matrix
	W = nestadj(W)
	# Np values
	NProw = []
	NPcol = []
	# Computation for the ROWS
	gen = generality(W)
	for i in range(0,(len(W)-1)):
		for j in range((i+1),len(W)):
			if gen[i]>gen[j]:
				NProw.append(compareones(W[i],W[j],gen[j]))
			else :
				NProw.append(0)
	# same on the COLUMNS
	W = W.T
	vul = generality(W)
	for i in range(0,(len(W)-1)):
		for j in range((i+1),len(W)):
			if vul[i]>vul[j]:
				NPcol.append(compareones(W[i],W[j],vul[j]))
			else :
				NPcol.append(0)
	#
	W = W.T
	# Output the NODF value
	ColCor = (len(W[0])*(len(W[0])-1))/2
	RowCor = (len(W)*(len(W)-1))/2
	NrowSum = 0
	for p in range(0,len(NProw)):
		NrowSum += NProw[p]
	NcolSum = 0
	for p in range(0,len(NPcol)):
		NcolSum += NPcol[p]
	WholeNest = round((NcolSum+NrowSum)/(ColCor + RowCor),2)
	ColNest = round(NcolSum/ColCor,2)
	RowNest = round(NrowSum/RowCor,2)
	NEST = [WholeNest, ColNest, RowNest]
	return NEST