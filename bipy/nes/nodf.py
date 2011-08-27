import scipy as sp
import numpy as np
from ..mainfuncs import *
from ..nul import *
from ..spe import *
from ..gen import *

def Ncal(W,reps=99,null=1):
	Ntot = []
	Nlow = []
	Ntop = []
	if hasattr(W,'nodf'):
		Nes [W.nodf,W.nodf_low,W.nodf_up]
	else:
		Nes = nodf(W)
	## Iteration
	for i in range(reps):
		if null == 1:
			Nprime = nodf(null1(W))
		if null == 2:
			Nprime = nodf(null2(W))
		Ntot.append(Nes[0]-Nprime[0])
		Nlow.append(Nes[1]-Nprime[1])
		Ntop.append(Nes[2]-Nprime[2])
	return [round(mean(Ntot),2),round(mean(Nlow),2),round(mean(Ntop),2)]

	
def nestadj(aW):
	W = aW
	# Returns as sorted binary matrix
	return adjacency(sortbydegree(W))

	
def compareones(w1,w2,tn):
	# Compare the identity of ONES
	id = 0.0
	for i in range(0,len(w1)):
		if (int(w1[i]) == 1)&(int(w2[i]) == 1):
			id = id + 1
	prop = (100*id)/tn
	return round(prop,2)		


def getNpaired(W):
	# Required for NODF calculation
	# Get the N paired value of a web
	Npaired = []
	gen = generality(W)
	for i in range(0,(len(W)-1)):
		for j in range((i+1),len(W)):
			if gen[i]>gen[j]:
				Npaired.append(compareones(W[i],W[j],gen[j]))
			else :
				Npaired.append(0)
	return Npaired			


def nodf(aW):
	W = nestadj(aW)
	# Measures NODF
	#	Almeida-Neto, M, et al. (2008) Oikos 117(8) 1227-1239
	# Step 1 : reorganize the adjacency matrix
	# Np values
	NProw = getNpaired(W)
	NPcol = getNpaired(W.T)
	# Output the NODF value
	ColCor = (len(W[0])*(len(W[0])-1))/2
	RowCor = (len(W)*(len(W)-1))/2
	NrowSum = 0
	for p in range(0,len(NProw)):
		NrowSum += NProw[p]
	NcolSum = 0
	for p in range(0,len(NPcol)):
		NcolSum += NPcol[p]
	WholeNest = round((NcolSum+NrowSum)/(ColCor + RowCor),2)
	ColNest = round(NcolSum/ColCor,2)
	RowNest = round(NrowSum/RowCor,2)
	NEST = [WholeNest, ColNest, RowNest]
	return NEST
