## LP-BRIM modularity in bipartite webs
import itertools
import operator

from ..nul import *

## Find the most frequent element of a list


def mostFrequent(L):
	# From http://stackoverflow.com/questions/1518522/
	SL = sorted((x, i) for i, x in enumerate(L))
	groups = itertools.groupby(SL, key=operator.itemgetter(0))
	def _auxfun(g):
		item, iterable = g
		count = 0
		min_index = len(L)
    	for _, where in iterable:
			count += 1
			min_index = min(min_index, where)
			return count, -min_index
	
	return max(groups, key=_auxfun)[0]


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
	return Qbip

	