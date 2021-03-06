## Contributions
from ..nes import *
import numpy as np

class contrib:
    def __init__(self,web):
        self.w = web
        self.done = False
        self.up_whole = []
        self.up_up = []
        self.up_low = []
        self.low_whole = []
        self.low_up = []
        self.low_low = []
    def calculate(self,replicates=100,nodf_strict=True,model=2):
        self.done = True
        out = spContribNest(self.w,replicates,nodf_strict,model)
        self.up_whole = out[0][0]
        self.up_up = out[0][1]
        self.up_low = out[0][2]
        self.low_whole = out[1][0]
        self.low_up = out[1][1]
        self.low_low = out[1][2]


def null_contrib(adj,idx,upper=True,model=1):
    """
    Randomization of the interactions of one species in the adjacency matrix
    """
    hasNull = True
    trials = 0
    while hasNull:
        trials += 1
        M = np.copy(adj)
        if not upper:
            M = M.T
        if model == 1:
            np.random.shuffle(M[idx])
        elif model == 2:
            Ci = np.sum(M,axis=0) / float(len(M))
            Ri = np.sum(M,axis=1) / float(len(M[0]))
            Pi = (Ri[idx]+Ci)/float(2)
            M[idx] = np.random.binomial(1,Pi)
        NI0 = np.sum(M.sum(axis=0)==0)
        NI1 = np.sum(M.sum(axis=1)==0)
        if (NI0 == 0)&(NI1 == 0):
            hasNull = False
    if not upper:
        M = M.T
    return M

## Individual contribution to nestedness
def spContribNest(w,replicates=100,nodf_strict=True,model=1):
    """
    Contribution of each species to the nestedness of the overall matrix
    """
    C_UP_NODF = []
    C_UP_NODF_up = []
    C_UP_NODF_low = []
    C_LOW_NODF = []
    C_LOW_NODF_up = []
    C_LOW_NODF_low = []
    for tls in xrange(w.upsp):
        tRep = []
        tRep_up = []
        tRep_low = []
        for reps in xrange(replicates):
            NoRepl = nodf(null_contrib(w.adjacency,tls,True,model),nodf_strict)
            tRep.append(w.nodf-NoRepl[0])
            tRep_up.append(w.nodf_up-NoRepl[2])
            tRep_low.append(w.nodf_low-NoRepl[1])
        C_UP_NODF.append((w.nodf-np.mean(tRep))/np.std(tRep))
        C_UP_NODF_up.append((w.nodf_up-np.mean(tRep_up))/np.std(tRep_up))
        C_UP_NODF_low.append((w.nodf_low-np.mean(tRep_low))/np.std(tRep_low))
    for lls in xrange(w.losp):
        tRep = []
        tRep_up = []
        tRep_low = []
        for reps in xrange(replicates):
            NoRepl = nodf(null_contrib(w.adjacency,lls,False,model),nodf_strict)
            tRep.append(w.nodf-NoRepl[0])
            tRep_up.append(w.nodf_up-NoRepl[2])
            tRep_low.append(w.nodf_low-NoRepl[1])
        C_LOW_NODF.append((w.nodf-np.mean(tRep))/np.std(tRep))
        C_LOW_NODF_up.append((w.nodf_up-np.mean(tRep_up))/np.std(tRep_up))
        C_LOW_NODF_low.append((w.nodf_low-np.mean(tRep_low))/np.std(tRep_low))
    return [[C_UP_NODF,C_UP_NODF_up,C_UP_NODF_low],[C_LOW_NODF,C_LOW_NODF_up,C_LOW_NODF_low]]