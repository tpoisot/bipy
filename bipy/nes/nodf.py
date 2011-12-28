import scipy as sp
import numpy as np
from ..mainfuncs import *
from ..spe import *
from ..base import *

def nestadj(aW):
    return adjacency(sortbydegree(aW))


def compareones(w1,w2,tn):
    #TODO: This is a posssible bottleneck, maybe port to C
    return (100 * np.sum( (w1 == np.ones(len(w1))) * (w2 == np.ones(len(w2)))) )/tn


def getNpaired(W,strict):
    # Required for NODF calculation
    # Get the N paired value of a web
    Npaired = []
    gen = generality(W)
    for i in xrange(0,(len(W)-1)):
        for j in xrange((i+1),len(W)):
            if strict:
                if gen[i] > gen[j]:
                    Npaired.append(compareones(W[i],W[j],gen[j]))
                else :
                    Npaired.append(0)
            else:
                if gen[i] >= gen[j]:
                    Npaired.append(compareones(W[i],W[j],gen[j]))
                else :
                    Npaired.append(0)
    return Npaired


def nodf(aW,strict=True):
    """
    The strict boolean tells if the condition for overlap needs to be
    strictly enforced or not. If srict = False, this can somehow increase the NODF
    values.
    """
    if (len(aW[0])==1)|(len(aW)==1):
        return [0,0,0]
    W = nestadj(aW)
    NProw = getNpaired(W,strict)
    NPcol = getNpaired(W.T,strict)
    # Output the NODF value
    ColCor = (len(W[0])*(len(W[0])-1))/2
    RowCor = (len(W)*(len(W)-1))/2
    NrowSum = 0
    for p in xrange(0,len(NProw)):
        NrowSum += NProw[p]
    NcolSum = 0
    for p in xrange(0,len(NPcol)):
        NcolSum += NPcol[p]
    WholeNest = np.round((NcolSum+NrowSum)/(ColCor + RowCor),2)
    ColNest = np.round(NcolSum/ColCor,2)
    RowNest = np.round(NrowSum/RowCor,2)
    NEST = [WholeNest, ColNest, RowNest]
    return NEST
