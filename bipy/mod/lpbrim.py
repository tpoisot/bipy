## LP-BRIM modularity in bipartite webs
import itertools
import operator

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
