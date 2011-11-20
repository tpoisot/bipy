## LP-BRIM modularity in bipartite webs
from ..null import *
from ..mainfuncs import *

## Find the most frequent element of a list
def mostFrequent(L):
	uVal = uniquify(L)
	random.shuffle(uVal)
	cnt = {}
	for u in uVal:
		cnt[str(u)] = 0
	for l in L:
		cnt[str(l)] += 1
	MaxLab = max(cnt, key=cnt.get)
	return MaxLab


## Compute Barber's bipartite modularity
def Qbip(W,gg,gh):
	tQ = 0
	if type(gg) == int:
		gg = [gg]
	if type(gh) == int:
		gh = [gh]
	for i in range(W.upsp):
		for j in range(W.losp):
			if gg[i] == gh[j]:
				hasInt = W.adjacency[i][j]
				probInt = (W.generality[i]*W.vulnerability[j])/float(W.nlink)
				tQ += hasInt - probInt
	qbip = tQ / float(W.nlink)
	return round(qbip,4)


## LP method
def LP(W):
	import scipy as sp
	import numpy as np
	OptimStep = 0
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
	oriBip = -1
	# Then go on to optimize
	# The LP procedure stops whenever the modularity stops increasing
	while oriBip < refBip:
		oriBip = refBip
		# We propagate the UTL species labels
		# The order of the nodes being updated
		# is choosen at random
		jOrder = range(W.losp)
		random.shuffle(jOrder) 
		for j in jOrder:
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
		# The order of the nodes being updated
		# is choosen at random
		iOrder = range(W.upsp)
		random.shuffle(iOrder)
		for i in iOrder:
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
		OptimStep += 1
	# Once we are OUTSIDE the loop (the modularity is stabilized)
	# we return the current Qbip and the community partition
	out = [refBip,g,h]
	return out


## Create the R and T matrix from a partition
def getRTfp(tg,th):
	import numpy as np
	ug = uniquify(tg)
	uh = uniquify(th)
	c = len(ug)
	# Build matrices
	R = np.zeros((len(tg),c))
	T = np.zeros((len(th),c))
	# Fill matrices
	for comm in range(c):
		for row in range(len(tg)):
			if ug[comm] == tg[row]:
				R[row][comm] = 1
		for row in range(len(th)):
			if uh[comm] == th[row]:
				T[row][comm] = 1
	return [R,T]


## Gets a module vector from a module matrix
def getCVfromCM(cm):
	cv = []
	for i in range(len(cm)):
		for j in range(len(cm[0])):
			if cm[i][j] == 1:
				cv.append((j+1))
	return cv


## BRIM procedure
def BRIM(W,part):
	import numpy as np
	# part is an object returned by LP
	ig = part[1]
	ih = part[2]
	iQbip = part[0]
	initPart = getRTfp(ig,ih)
	R = initPart[0]
	T = initPart[1]
	nc = len(R[0])
	# do the B matrix
	B = np.copy(W.adjacency)
	for i in range(W.upsp):
		for j in range(W.losp):
				B[i][j] -= (W.generality[i]*W.vulnerability[j])/float(W.nlink)
	# begin BRIM optimization
	refQbip = -1
	while refQbip < iQbip:
		refQbip = iQbip
		# Step 1 : BT
		BT = np.dot(B,T)
		for i in range(len(BT)):
			for k in range(nc):
				if BT[i][k] == max(BT[i]):
					R[i][k] = 1
				else:
					R[i][k] = 0
		# Step 2 : BR
		BR = np.dot(B.T,R)
		for i in range(len(BR)):
			for k in range(nc):
				if BR[i][k] == max(BR[i]):
					T[i][k] = 1
				else:
					T[i][k] = 0
		ng = getCVfromCM(R)
		nh = getCVfromCM(T)
		iQbip = Qbip(W,ng,nh)
	return [iQbip,ng,nh]


## Single LPBRIM Run
def LPBRIM(W):
	import scipy as sp
	import numpy as np
	LPpart = LP(W)
	BRIMpart = BRIM(W,LPpart)
	Q = BRIMpart[0]
	Nmod = len(uniquify(BRIMpart[1]))
	TopPart = BRIMpart[1]
	BotPart = BRIMpart[2]
	out = [Q,Nmod,TopPart,BotPart]
	return out


## Find modules
def findModules(W,reps=10,outstep=5,step_print=False):
	topmod = 0
	out = [0,0,0,0]
	if (reps >= 100)&(step_print):
		print "Done	Best Q	Best M"
		print "----------------------"
	nstep = outstep
	for repl in range(reps):
		run = LPBRIM(W)
		if run[0] > topmod:
			topmod = run[0]
			out = run
		if reps >= 100:
			if ((repl/float(reps))*100 >= nstep)&(step_print):
				print"{0}%	{1} 	{2}".format(str(nstep), str(out[0]), str(out[1]))
				nstep += outstep
#	print 'Found '+str(out[1])+' modules with Qbip of '+str(topmod)
	if (reps >= 100)&(step_print):
		print "----------------------"
		print"{0}%	{1}	{2}".format(str(100),str(out[0]), str(out[1]))
		print "----------------------"
	return out


## Sort by modules
def sortbymodule(W,g,h):
	sg = sorted(np.copy(g),reverse=True)
	sh = sorted(np.copy(h),reverse=True)
	# Step 1 : Sort a matrix by module
	## VOID VECTORS FOR THE SORTED SPECIES NAMES
	oTnames = W.upnames
	oBnames = W.lonames
	vTnames = np.copy(oTnames)
	vBnames = np.copy(oBnames)
	## Step 1a : sort TLO
	rG = rank(g)
	nW = np.zeros((W.upsp,W.losp))
	for ro in range(0,W.upsp):
		nW[rG[ro]] = W.web[ro]
		vTnames[rG[ro]] = oTnames[ro]
	## Step 1b : sort BLO
	nW = nW.T
	dW = np.zeros((W.upsp,W.losp)).T
	rG = rank(h)
	for ro in range(0,W.losp):
		dW[rG[ro]] = nW[ro]
		vBnames[rG[ro]] = oBnames[ro]
	web = np.copy(dW.T)
	# New temp files for the names
	oBnames = np.copy(vBnames)
	oTnames = np.copy(vTnames)
	# Step 2 : Sort each module by degree
	uniqueMod = sorted(uniquify(sg),reverse=True)
	## Step 2a : sort TLO
	totalMadeInt = 0
	tempIntCnt = 0
	tdeg = generality(web)
	nweb = np.zeros(np.shape(web))
	for module in uniqueMod:
		totalMadeInt += tempIntCnt
		tempIntCnt = 0
		cdeg = []
		for sp in range(len(tdeg)):
			if sg[sp] == module:
				cdeg.append(tdeg[sp])
		rnk = rank(cdeg)
		for ro in range(len(rnk)):
			nweb[totalMadeInt+rnk[ro]] = web[totalMadeInt+ro]
			vTnames[totalMadeInt+rnk[ro]] = oTnames[totalMadeInt+ro]
			tempIntCnt += 1
	web = np.copy(nweb.T)
	## Step 2b : sort BLO
	totalMadeInt = 0
	tempIntCnt = 0
	tdeg = generality(web)
	nweb = np.zeros(np.shape(web))
	for module in uniqueMod:
		totalMadeInt += tempIntCnt
		tempIntCnt = 0
		cdeg = []
		for sp in range(len(tdeg)):
			if sh[sp] == module:
				cdeg.append(tdeg[sp])
		rnk = rank(cdeg)
		for ro in range(len(rnk)):
			nweb[totalMadeInt+rnk[ro]] = web[totalMadeInt+ro]
			vBnames[totalMadeInt+rnk[ro]] = oBnames[totalMadeInt+ro]
			tempIntCnt += 1
	Fweb = mini_bipartite(np.copy(nweb.T))
	Fweb.upnames = vTnames
	Fweb.lonames = vBnames
	return Fweb


## Realized modularity
## Which proportion of the interactions are made within modules ?
def Qr(w,mod):
	if mod[0] == 0:
		realized = 0
	else :
		g = mod[2]
		h = mod[3]
		Nint = 0
		for i in range(w.upsp):
			for j in range(w.losp):
				if w.adjacency[i][j] == 1:
					if g[i] == h[j]:
						Nint += 1
	 	realized = Nint/float(w.nlink)
	return realized


## Separate modules
def splitWeb(W,mod,path='.',prefix='web_',ext='web',minU=3,minL=3):
	if mod[1] == 0:
		np.savetxt(path+'/'+prefix+'full.'+ext,W.web,delimiter=' ')
	else:
		# We start with the modules
		g = mod[2]
		h = mod[3]
		uMod = uniquify(g)
		for mod in uMod:
			# For each module
			nUp = 0
			nLo = 0
			for i in g:
				if i == mod:
					nUp += 1
			for i in h:
				if i == mod:
					nLo += 1
			nWeb = np.zeros((nUp,nLo))
			cRow = -1
			for i in range(W.upsp):
				cCol = -1
				if g[i] == mod:
					cRow += 1
					for j in range(W.losp):
						if h[j] ==mod:
							cCol +=1
							nWeb[cRow][cCol] = W.web[i][j]
			if nUp >= minU:
				if nLo >= minL:
					np.savetxt(path+'/'+prefix+str(mod)+'.'+ext,nWeb,delimiter=' ')
	return 0


## All sub webs as mini_bipartite
def subWebs(W):
	ExtractedModules = []
	# We start with the modules
	g = W.modules.up_modules
	h = W.modules.low_modules
	uMod = uniquify(g)
	for mod in uMod:
		# For each module
		nUp = 0
		nLo = 0
		for i in g:
			if i == mod:
				nUp += 1
		for i in h:
			if i == mod:
				nLo += 1
		nWeb = np.zeros((nUp,nLo))
		cRow = -1
		for i in range(W.upsp):
			cCol = -1
			if g[i] == mod:
				cRow += 1
				for j in range(W.losp):
					if h[j] ==mod:
						cCol +=1
						nWeb[cRow][cCol] = W.web[i][j]
		ExtractedModules.append(nWeb)
	return ExtractedModules


## END OF FILE