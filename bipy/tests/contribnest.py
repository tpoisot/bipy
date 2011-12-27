from ..bipartite_class import *
from ..nes import *

def null_contrib(adj,idx,row=True):
    tint = np.prod(tem.shape)
    zeroes = tint-np.sum(tem)
    ## We only return a matrix with no non-interacting species
    hasNull = True
    trials = 0
    while hasNull:
        trials += 1
        mat = np.concatenate((np.ones(np.sum(tem)),np.zeros(zeroes)),1)
        np.random.shuffle(mat)
        mat = mat.reshape((len(tem),len(tem[0])))
        NI0 = np.sum(mat.sum(axis=0)==0)
        NI1 = np.sum(mat.sum(axis=1)==0)
        if (NI0 == 0)&(NI1 == 0):
            hasNull = False
    return mat

## Individual contribution to nestedness
def spContribNest(w,replicates=100,nodf_strict=True):
    """
    Contribution of each species to the nestedness of the overall matrix
    """

    return 0