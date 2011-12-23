## Tests of deviation from the null models

from ..nes import *
from ..mod import *
from ..bipartite_class import *
import scipy.stats as spp

class test:
    def __init__(self,web,model,replicates,verbose,q_c):
        """
        Initialize a test class and perform the tests
        """
        self.v = verbose
        self.web = web
        self.q_c = q_c
        if self.v:
            print "[INF] Creation of the null networks"
        self.nulls = nullModel(self.web,model,replicates=replicates)
        self.devnest = []
        self.devqb = []
        self.devqr = []
    def nestedness(self):
        if self.v:
            print "[INF] Begin testing nestedness"
        self.devnest = getDevNest(self.web,self.nulls)
        if self.v:
            print "[INF] Nestedness test completed"
    def modularity(self,repl):
        ## test if the bipartite object has modules
        if len(self.web.modules) == 0:
            if self.v:
                print '[WRN] Conducting the modularity analysis'
            self.web.modules = modules(self.web,reps=repl,q_c=self.q_c)
        ##
        if self.v:
            print '[INF] Beginning the test for modularity'
        d_mod = getDevMod(self.web,self.nulls,repl,self.q_c)
        self.devqr = d_mod[0]
        self.devqb = d_mod[1]
        if self.v:
            print '[INF] Test for modularity completed'
    def __str__(self):
        out = "Stat\tN0\t\tN'\t\tp\t\tIC-\t\tIC+\n"
        out +=  "---------------------------------------------\n"
        if len(self.devnest) > 0:
            p_nest = '---'
            if self.devnest[1] < 0.05:
                p_nest = '*    '
            if self.devnest[1] < 0.01:
                p_nest = '**   '
            if self.devnest[1] < 0.001:
                p_nest = '***  '
            if self.devnest[1] < 0.0001:
                p_nest = '**** '
            if self.devnest[1] < 0.00001:
                p_nest = '*****'
            out += "NODF\t"+str(round(self.devnest[0],2)).zfill(4)+"\t"+str(round(self.devnest[2],2)).zfill(4)+"\t"+p_nest+"\t"+str(round(self.devnest[3],2)).zfill(4)+"\t"+str(round(self.devnest[4],2)).zfill(4)+"\n"
        if len(self.devqr) > 0:
            p_qr = '  -  '
            if self.devqr[1] < 0.05:
                p_qr = '*    '
            if self.devqr[1] < 0.01:
                p_qr = '**   '
            if self.devqr[1] < 0.001:
                p_qr = '***  '
            if self.devqr[1] < 0.0001:
                p_qr = '**** '
            if self.devqr[1] < 0.00001:
                p_qr = '*****'
            out += "QR    \t"+str(round(self.devqr[0],2)).zfill(4)+"\t"+str(round(self.devqr[2],2)).zfill(4)+"\t"+p_qr+"\t"+str(round(self.devqr[3],2)).zfill(4)+"\t"+str(round(self.devqr[4],2)).zfill(4)+"\n"
        if len(self.devqb) > 0:
            p_qb = '---'
            if self.devqb[1] < 0.05:
                p_qb = '*    '
            if self.devqb[1] < 0.01:
                p_qb = '**   '
            if self.devqb[1] < 0.001:
                p_qb = '***  '
            if self.devqb[1] < 0.0001:
                p_qb = '**** '
            if self.devqb[1] < 0.00001:
                p_qb = '*****'
            out += "QB    \t"+str(round(self.devqb[0],2)).zfill(4)+"\t"+str(round(self.devqb[2],2)).zfill(4)+"\t"+p_qb+"\t"+str(round(self.devqb[3],2)).zfill(4)+"\t"+str(round(self.devqb[4],2)).zfill(4)+"\n"
        return out

def gMIC(distrib):
    """
    Bayesian estimates of mean, and standard deviation
    """
    estimates = spp.bayes_mvs(distrib,alpha=0.95)[0]
    return[estimates[0],estimates[1][0],estimates[1][1]]

## excess nestedness
def getDevNest(w,list):
    expect = []
    for i in list:
        expect.append(bipartite(i).nodf)
    testRes = stats.ttest_1samp(expect, w.nodf)
    OUT = [w.nodf,testRes[1]]
    est = gMIC(expect)
    for est_par in est:
        OUT.append(est_par)
    return OUT

## excess modularity
def getDevMod(w,nulls,rep,q_c):
    """
    Get the deviation from random expectation of modularity. Optimized so that
    the null webs are gone through only one time. Retunrs two arrays, one for
    Qr, the other for Qb.
    """
    m = [w.modules.Q,w.modules.N,w.modules.up_modules,w.modules.low_modules]
    Qbsim = []
    Qrsim = []
    wQr = Qr(w,m)
    wQb = w.modules.Q
    for c_null in nulls:
        mod = modules(bipartite(c_null),rep,q_c)
        Qrsim.append(mod.Qr)
        Qbsim.append(mod.Q)
    testResB = stats.ttest_1samp(Qbsim, wQb)
    testResR = stats.ttest_1samp(Qrsim, wQr)
    OUT_r = [wQr,testResR[1]]
    OUT_b = [wQb,testResB[1]]
    est_r = gMIC(Qrsim)
    est_b = gMIC(Qbsim)
    for est_par in est_r:
        OUT_r.append(est_par)
    for est_par in est_b:
        OUT_b.append(est_par)
    return [OUT_r,OUT_b]