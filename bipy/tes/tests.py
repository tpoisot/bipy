## Tests of deviation from the null models

from ..nes import *
from ..mod import *

## excess modularity
def getDevNest(w,list):
	deviation = []
	for i in list:
		ni = i.nodf
		deviation.append(w.nodf-ni[0])
	return deviation

	
## excess modularity
def getDevMod(w,m,list):
	Qsim = []
	wQr = Qr(w,m)
	for i in list:
		ExcQ = wQr - Qr(i,m)
		Qsim.append(ExcQ)
	return Qsim
