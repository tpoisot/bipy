import scipy as sp
import numpy as np
from .gendesc import *
from ..spe import *
from ..mainfuncs import *

def fixmat(aW):
	import numpy as np
	W = np.copy(aW)
	# Fix a matrix so that there are no empty row
	# or empty columns, issues a message is some rows
	# were removed
	OrigSize = websize(W)
	g = generality(W)
	v = vulnerability(W)
	emptyRows = 0
	emptyCols = 0
	for i in range(len(g)):
		if g[i]==0:
			emptyRows += 1
	for j in range(len(v)):
		if v[j]==0:
			emptyCols += 1
	if (emptyRows+emptyCols)==0:
		return W
	else :
		# Create a new matrix with the correct dimensions
		nW = np.zeros(((len(W)-emptyRows),(len(W[0])-emptyCols)),float)
		# For each row and each column
		# copy the correct values in the new matrix
		cRow = 0
		for i in range(len(g)):
			# If the species i is not interacting, we can skip
			if g[i] == 0:
				continue
			else:
				cCol = 0
				# Else we go throug the species j
				for j in range(len(v)):
					if v[j] > 0:
						nW[cRow][cCol] = W[i][j]
						cCol += 1
				cRow += 1
		# Finally...
		return nW


def readweb(fname):
	# Read a web from a text matrix with top trophic level organisms as rows
	data = np.loadtxt(fname)
	return fixmat(data)

	
def adjacency(aW):
	# Output the adjacency matrix
	ntop = len(aW)
	nbot = len(aW[0])
	W = np.zeros(((ntop),(nbot)))
	for to in range(0,ntop):
		for bo in range(0,nbot):
			if aW[to,bo] > 0:
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


def sortbydegree(W):
	# Sort a matrix by degree
	# Better for visualization
	# Required for nestedness
	
	if hasattr(W,'connectance'):
		g = W.generality
		v = W.vulnerability
		upsp = W.upsp
		losp = W.losp
		web = W.web
	else:
		g = generality(W)
		v = vulnerability(W)
		upsp = len(W)
		losp = len(W[0])
		web = W
		
	## Step 1 : sort TLO
	rG = rank(g)
	nW = np.zeros((upsp,losp))
	for ro in range(0,upsp):
		nW[rG[ro]] = web[ro]
	## Step 2 : sort BLO
	nW = nW.T
	dW = np.zeros((upsp,losp)).T
	rG = rank(v)
	for ro in range(0,losp):
		dW[rG[ro]] = nW[ro]
	return dW.T


def toN3D(bip,filename='w3b.web'):
	# This allows the user to export an interaction dataset
	# in a way that Network3D can read
	# 
	# Works for bipartite objects ONLY
	
	if not hasattr(bip,'web'):
		bip = bipartite(bip)
	
	f = open(filename, 'w')
	for up in range(bip.upsp):
		for lo in range(bip.losp):
			if bip.web[up][lo] > 0:
				f.write('{0} {1} {2}\n'.format('T'+str(up), 'B'+str(lo), str(bip.web[up][lo])))
	f.close()
	return 0

