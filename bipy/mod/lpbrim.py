## LP-BRIM modularity in bipartite webs
from collections import Counter

from ..nul import *

## Find the most frequent element of a list


def mostFrequent(L):
	l = L
	random.shuffle(l)
	c = Counter(l)
	return c.most_common(1)[0][0]


## Compute Barber's bipartite modularity
def Qbip(W,g,h):
	tQ = 0
	for i in range(W.upsp):
		for j in range(W.losp):
			if g[i] == h[j]:
				hasInt = W.adjacency[i][j]
				probInt = (W.generality[i]*W.vulnerability[j])/float(W.nlink)
				tQ += hasInt - probInt
	Qbip = tQ / float(W.nlink)
	return round(Qbip,4)

## LP method
def LP(W):
	print "LP: LP started"
	w = W.adjacency ## This version of modularity is BINARY
	# Community objects
	g = []
	# Each LTL species is assigned a random label
	h = np.arange(W.losp)
	np.random.shuffle(h)
	# First round of UTL species label propagation
	for i in range(W.upsp):
		# We get a void object to get neighboring labels
		vNL = []
		for j in range(W.losp):
			if w[i][j] == 1:
				# In case of interaction, the label of the interacting
				# LTL species is considered to be neighboring
				vNL.append(h[j])
		# We then add the most common label
		g.append(mostFrequent(vNL))
	# We calculate basal modularity
	refBip = Qbip(W,g,h)
	print "LP: initial Qbip "+str(refBip)
	oriBip = -1
	# Then go on to optimize
	# The LP procedure stops whenever the modularity stops increasing
	print "LP: LP in progress"
	while oriBip < refBip:
		oriBip = refBip
		# We propagate the UTL species labels
		for j in range(W.losp):
			# We get a void object to get neighboring labels
			vNL = []
			for i in range(W.upsp):
				if w[i][j] == 1:
					# In case of interaction, the label of the interacting
					# LTL species is considered to be neighboring
					vNL.append(g[i])
			# We then add the most common label
			h[j] = mostFrequent(vNL)
		# We propagate the LTL species labels
		for i in range(W.upsp):
			# We get a void object to get neighboring labels
			vNL = []
			for j in range(W.losp):
				if w[i][j] == 1:
					# In case of interaction, the label of the interacting
					# LTL species is considered to be neighboring
					vNL.append(h[j])
			# We then add the most common label
			g[i] = mostFrequent(vNL)
		# We then recalculate the modularity
		refBip = Qbip(W,g,h)
	# Once we are OUTSIDE the loop (the modularity is stabilized)
	# we return the current Qbip and the community partition
	print "LP: optimal found for Qbip "+str(refBip)
	out = [refBip,g,h]
	return out

