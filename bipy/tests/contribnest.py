from ..bipartite_class import *
from ..nes import *
import numpy as np

def null_contrib(adj,idx,upper=True):
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
        np.random.shuffle(M[idx])
        NI0 = np.sum(M.sum(axis=0)==0)
        NI1 = np.sum(M.sum(axis=1)==0)
        if (NI0 == 0)&(NI1 == 0):
            hasNull = False
        if not upper:
            M = M.T
    return M

## Individual contribution to nestedness
def spContribNest(w,replicates=100,nodf_strict=True):
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
            NoRepl = nodf(null_contrib(w.adjacency,tls,True),nodf_strict)
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
            NoRepl = nodf(null_contrib(w.adjacency,lls,False),nodf_strict)
            tRep.append(w.nodf-NoRepl[0])
            tRep_up.append(w.nodf_up-NoRepl[2])
            tRep_low.append(w.nodf_low-NoRepl[1])
        C_LOW_NODF.append((w.nodf-np.mean(tRep))/np.std(tRep))
        C_LOW_NODF_up.append((w.nodf_up-np.mean(tRep_up))/np.std(tRep_up))
        C_LOW_NODF_low.append((w.nodf_low-np.mean(tRep_low))/np.std(tRep_low))
    return [[C_UP_NODF,C_UP_NODF_up,C_UP_NODF_low],[C_LOW_NODF,C_LOW_NODF_up,C_LOW_NODF_low]]