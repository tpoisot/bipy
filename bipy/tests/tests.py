## Tests of deviation from the null models

from ..nes import *
from ..mod import *

## excess modularity
def getDevNest(w,list):
	deviation = []
	for i in list:
		deviation.append(w.nodf-i.nodf)
	return deviation


## excess modularity
def getDevMod(w,list):
	m = [w.modules.Q,w.modules.N,w.modules.up_modules,w.modules.low_modules]
	Qsim = []
	wQr = Qr(w,m)
	for i in list:
		ExcQ = wQr - Qr(i,m)
		Qsim.append(ExcQ)
	return Qsim


## excess bipartite modularity
def getDevQ(w,list):
	Qsim = []
	wQ = w.modules.Q
	for i in list:
		ExcQ = wQ - Qbip(i,w.modules.up_modules,w.modules.low_modules)
		Qsim.append(ExcQ)
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
	# Check the dimensionality
#	mat = fixmat(RMat)
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
