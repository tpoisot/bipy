import numpy as np
import copy
from numpy.random import shuffle
from .tests import *

def extinctRobustness(w,method='random',removelower=True,tofile=False,nreps=100):
	######
	#
	# method
	# Must be one of
	#	random : random removal
	#	stog : specialists to generalists
	#	gtos : generalists to specialists
	#
	# removelower
	#	tells if the upper or lower level is removed
	#
	# nreps
	#	Number of extinction sequences to perform
	#
	######
	
	if method == 'random':
		print 'Starting '+str(nreps)+' random extinction sequences'
	if method == 'stog':
		print 'Starting '+str(nreps)+' increasing degree (best case) extinction sequences'
	if method == 'gtos':
		print 'Starting '+str(nreps)+' decreasing degree (worst case) extinction sequences'
	
	# Keep the data somewhere
	# and make sure that the extreme points are accounted for
	NSP_REMV = [0,1]
	NSP_SURV = [1,0]
	
	# Actual simulations
	currentRep = 0
	
	# Loop for the extinction sequence
	while currentRep < nreps:
		# Number of links for stog/gtos sequences
		if removelower:
			Links = w.vulnerability
			Range = np.array(range(0,w.losp))
			fTop = False
		else:
			Links = w.generality
			Range = np.array(range(0,w.upsp))
			fTop = True
	
		inds = np.argsort(np.copy(Links))
		Range = np.take(Range, inds)
	
		if method == 'gtos':
				Range = Range[::-1]
		
		# Increase the sequence counter
		currentRep += 1
		# Randomize if needed
		if method == 'random':
			shuffle(Range)
		# Begin extinctions
		mat = np.copy(w.adjacency)
		for i in range(0,(len(Range)-1)):
			if fTop:
				for j in range(0,w.losp):
					mat[Range[i],j] = 0
			else:
				for j in range(0,w.upsp):
					mat[j,Range[i]] = 0
			if removelower:
				NSP_REMV.append((i+1)/float(w.losp))
				NSP_SURV.append(np.sum(mat.sum(axis=1)>0)/float(w.upsp))
			else:
				NSP_REMV.append((i+1)/float(w.upsp))
				NSP_SURV.append(np.sum(mat.sum(axis=0)>0)/float(w.upsp))
			
	# Finally...
	out = zip(NSP_REMV,NSP_SURV)
	if tofile:
		fname = w.name+'_ext_'+method+'.txt'
		f = open(fname, 'w')
		for row in out:
			f.write(" ".join(map(str,row)))
			f.write('\n')
		f.close()
	return zip(NSP_REMV,NSP_SURV)


def int_rect(x,y):
	# Numerical integration using rectangles method
	AUC = 0
	LastLowerBound = 0
	LastUpperBound = 0
	for i in range(len(x)):
		# Find span and bounds
		if LastUpperBound == LastLowerBound:
			Span = x[(i+1)]-x[i]
			LastUpperBound = x[i]+Span/float(2)
			LastLowerBound = x[i]-Span/float(2)
		else:
			LastLowerBound = LastUpperBound
			HSpan = (x[i]-LastLowerBound)
			Span = HSpan  *2
			LastUpperBound = LastLowerBound + Span
		AUC += y[i]*Span
	return AUC

def extinctionScore(ext,integrator=int_rect):
	# Gives the area under the curve for an extinction robustness analysis
	
	# Step 1 : aggregate
	NRem = list(zip(*ext)[0])
	NSur = list(zip(*ext)[1])
	
	MSur = []
	LRem = uniquify(NRem)
	
	for lrem in LRem:
		tsum = 0
		tcnt = 0
		for i in range(len(NSur)):
			if NRem[i] == lrem:
				tsum += NSur[i]
				tcnt += 1
		MSur.append(tsum/float(tcnt))
	
	# Step 2 : perform integration
	AUC = integrator(LRem,MSur)
	
	return [AUC,LRem,MSur]

