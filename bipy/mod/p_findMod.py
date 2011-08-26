import pp
from collections import Counter
from ..nul import *
from ..mainfuncs import *
from .lpbrim import *

## Find modules
def p_findModules(W,ncpu=1):
	topmod = 0
	out = [0,0,0,0]
	if reps >= 100:
		print "Done	Best Q	Best M"
		print "----------------------"
	nstep = outstep
	for repl in range(reps):
		LPpart = LP(W)
		BRIMpart = BRIM(W,LPpart)
		Q = BRIMpart[0]
		Nmod = len(uniquify(BRIMpart[1]))
		TopPart = BRIMpart[1]
		BotPart = BRIMpart[2]
		if Q > topmod:
			topmod = Q
			out = [Q,Nmod,TopPart,BotPart]
		if reps >= 100:
			if (repl/float(reps))*100 >= nstep:
				print"{0}%	{1} 	{2}".format(str(nstep), str(out[0]), str(out[1]))
				nstep += outstep
#	print 'Found '+str(out[1])+' modules with Qbip of '+str(topmod)
	print "----------------------"
	print"{0}%	{1}	{2}".format(str(100),str(out[0]), str(out[1]))
	print "----------------------"
	return out
