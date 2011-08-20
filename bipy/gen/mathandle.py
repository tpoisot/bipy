import scipy as sp
import numpy as np
from .gendesc import *
from ..spe import *

def fixmat(aW):
	W = aW
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
	W = aW
	# Transforms any matrix into an adjacency matrix
	ntop = len(W)
	nbot = len(W[0])
	for to in range(0,ntop):
		for bo in range(0,nbot):
			if W[to,bo] > 0:
				W[to,bo] = 1
	return W

def prettyprint(aW):
	W = aW
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

def sortbydegree(aW):
	W = aW
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
