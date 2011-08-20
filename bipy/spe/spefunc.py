import scipy as sp
import numpy as np
from ..mainfuncs import *
from ..gen import *

def generality(aW):
	W = aW
	# Measure of generality
	#	Schoener, T. (1989) Ecology 70(6) 1559-1589
	gen = []
	for links in W:
		nl = 0
		for link in range(0,len(links)):
			if links[link] > 0:
				nl = nl + 1
		gen.append(nl)
	return gen

def vulnerability(aW):
	W = aW
	# Measure of generality
	#	Schoener, T. (1989) Ecology 70(6) 1559-1589
	vul = generality(W.T)
	return vul

def specificity(aW):
	W = aW
	# Measures the specialization using the Paired Differences Index
	#	Poisot, T, et al. (2011) Biol Lett 7(2) 201-204 10.1098/rsbl.2010.0774
	#	Poisot, T, et al. (in press) Proc R Soc Lon B 10.1098/rspb.2011.0826
	spe = []
	fit = 0
	for fit in W:
		tspe = 0
		fit = sorted(fit,reverse=True)
		i = 0
		ma = max(fit)
		while i < len(fit):
			fit[i] = fit[i]/float(ma)
			i = i+1
		i = 1
		while i < len(fit):
			tspe = tspe + ((fit[0]-fit[i])/(len(fit)-1))
			i = i+1
		spe.append(round(tspe,3))
	return spe	
