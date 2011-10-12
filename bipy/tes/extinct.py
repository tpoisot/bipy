import numpy as np
import copy
from numpy.random import shuffle
from .tests import *

def extinctRobustness(w,method='random',removelower=True,tofile=False,nreps=50):
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
	
	# Number of links for stog/gtos sequences
	if removelower:
		Links = np.copy(w.vulnerability)
		Range = np.array(range(0,w.losp))
		fTop = False
	else:
		Links = np.copy(w.generality)
		Range = np.array(range(0,w.upsp))
		fTop = True
	
	inds = np.argsort(Links)
	Range = np.take(Range, inds)
	
	if method == 'gtos':
			Range = Range[::-1]
	
	# Keep the data somewhere
	NSP_REMV = []
	NSP_SURV = []
	
	# Actual simulations
	currentRep = 0
	
	# Loop for the extinction sequence
	while currentRep < nreps:
		print currentRep
		sW = copy.deepcopy(w)
		# Increase the sequence counter
		currentRep += 1
		# Randomize if needed
		if method == 'random':
			shuffle(Range)
		# Begin extinctions
		for i in range(0,(len(Range)-1)):
			sW = remSpecies(sW,sp=Range[i],fromTop=fTop)
			if sW.__class__.__name__ == 'ndarray':
				break
			cRange = Range[i]
			for j in range((i+1),(len(Range)-1)):
				if Range[j] > cRange:
					Range[j] -= 1
			if removelower:
				NSP_SURV.append(sW.upsp)
			else:
				NSP_SURV.append(sW.losp)
			NSP_REMV.append(i)
			
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