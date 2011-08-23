import scipy as sp
import numpy as np
from ..mainfuncs import *
from ..gen import *

def generality(W):
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

def vulnerability(W):
	# Measure of generality
	#	Schoener, T. (1989) Ecology 70(6) 1559-1589
	vul = generality(W.T)
	return vul

def specificity(W):
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

def ssi(W):
	# Measures the Species Specialization Index
	# usefull to discriminate among highly specialized organisms
	#	Julliard, R, et al. (2006) Ecol Lett 9(11) 1237-1244 10.1111/j.1461-0248.2006.00977.x
	spe = []
	n = len(W[0]) # Number of resources
	normfac = n * np.sqrt((n-1)/float(n))
	for fit in W:
		# For each species in the web
		tspe = 0
		Pbar = mean(fit)
		tnfac = normfac * Pbar
		for sp in fit:
			tspe += (sp-Pbar) ** 2
		spe.append(np.sqrt(tspe)/tnfac)
	return spe

