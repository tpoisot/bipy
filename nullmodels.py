##########
# bipy
# nullmodels
##########
# A set of python functions to work on bipartite interaction networks
# These functions implement several null models
# Timothee Poisot - Universite Montpellier 2
# August 12, 2011
# Contact : tpoisot@um2.fr
##########


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
	C = connectance(W)
	Wp = nullC(len(W),len(W[0]),C)
	return fixmat(Wp)

def null2(W):
	# Generate a random network based on the
	# probability that a row and a column
	# have an interaction in the overall
	# web
	W = adjacency(W)
	g = generality(W)
	v = vulnerability(W)
	for i in range(len(W)):
		g[i] = g[i]/float(len(W[0]))
	for j in range(len(W[0])):
		v[j] = v[j]/float(len(W))
	# Generate a random web
	Wp = np.zeros((len(W),len(W[0])))
	for i in range(len(W)):
		for j in range(len(W[0])):
			IsInt = np.random.uniform(0,1,(1,))
			ProbInt = (g[i]+v[j])/2
			if ProbInt > IsInt:
				Wp[i][j] = 1
	return fixmat(Wp)
