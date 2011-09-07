## Tests of deviation from the null models

from ..nes import *

def getDevNest(w,list):
	print w.upsp
	print w.losp
	deviation = []
	for i in list:
		ni = nodf(i)
		deviation.append(w.nodf-ni[0])
	return deviation