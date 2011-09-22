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
def remSpecies(w,sp=0,fromTop=True):
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
	# Returns a mini bipartite object
	return mini_bipartite(fixmat(RMat))


# Get the contribution of each species to modularity
def getContribMod(w,reps=1000):
	# Get modularity
	m = findModules(w,reps)
	Qbip = m[0]
	# Create two objects: up and low
	CMup = []
	CMlo = []
	# Loop
	for i in range(w.upsp):
		tMat = remSpecies(w,i,True)
		rQbip = findModules(tMat,reps)[0]
		tStat = np.abs(rQbip-Qbip)
		CMup.append(tStat)
	for i in range(w.losp):
		tMat = remSpecies(w,i,False)
		rQbip = findModules(tMat,reps)[0]
		tStat = np.abs(rQbip-Qbip)
		CMlo.append(tStat)
	# Return the data
	return [CMup,CMlo]


# Get the contribution of each species to nestedness
def getContribNes(w):
	# Create two objects: up and low
	CNup = []
	CNlo = []
	# Loop
	for i in range(w.upsp):
		tMat = remSpecies(w,i,True)
		tStat = np.abs(tMat.nodf-w.nodf)
		CNup.append(tStat)
	for i in range(w.losp):
		tMat = remSpecies(w,i,False)
		tStat = np.abs(tMat.nodf-w.nodf)
		CNlo.append(tStat)
	# Return the data
	return [CNup,CNlo]
