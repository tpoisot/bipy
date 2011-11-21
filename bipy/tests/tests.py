## Tests of deviation from the null models

from ..nes import *
from ..mod import *
from ..bipartite_class import *

def testDeviation(vec):
	testRes = stats.ttest_1samp(vec, 0)
	return [np.mean(vec),testRes[1],testRes[0]]


## excess modularity
def getDevNest(w,list):
	deviation = []
	for i in list:
		deviation.append(w.nodf-bipartite(i).nodf)
	return deviation


## excess modularity
def getDevQr(w,list):
	m = [w.modules.Q,w.modules.N,w.modules.up_modules,w.modules.low_modules]
	Qsim = []
	wQr = Qr(w,m)
	for i in list:
		Qsim.append(wQr - Qr(bipartite(i),m))
	return Qsim


## excess bipartite modularity
def getDevQbip(w,list):
	Qsim = []
	wQ = w.modules.Q
	for i in list:
		Qsim.append(wQ - Qbip(bipartite(i),w.modules.up_modules,w.modules.low_modules))
	return Qsim


## remove a species from a matrix
def remSpecies(w,sp=0,fromTop=True,superMini=False):
	if fromTop:
		Mat = np.copy(w.web)
	else:
		Mat = np.copy(w.web.T)
	# Matrix with one less species
	RMat = np.zeros((len(Mat)-1,len(Mat[1])))
	ci = 0
	for i in range(len(Mat)):
		if not i == sp:
			for j in range(len(Mat[1])):
				RMat[ci][j] = Mat[i][j]
			ci = ci + 1
	if not fromTop:
		RMat = RMat.T
	# Check the dimensions
	mat = RMat
	if (len(mat.shape) == 2)&(len(mat)>=1)&(len(mat[0])>=1):
		if superMini:
			mat = super_mini_bipartite(mat)
		else:
			mat = mini_bipartite(mat)
	else:
		mat = np.zeros((0,0))
	# Returns a mini bipartite object
	return mat
