from .nes import *
from .mod import *
from .contrib import *
from .null import *
from .tests import *
import scipy.stats as spp


from getref import *

import numpy as np

import tempfile
import os
import tkFileDialog

class bipartite:
    ## This class defines a bipartite object with all structural infos
    def __init__ (self,web,t=False,nodf_strict=True,q_c=True):
        self.q_c = q_c
        # Read the matrix
        if t:
            web = web.T
        self.web = fixmat(web)
        # General infos
        self.upsp = len(self.web)
        self.losp = len(self.web[0])
        self.size = self.upsp * self.losp
        # Connectance
        self.adjacency = adjacency(self.web)
        self.nlink = np.sum(self.adjacency)
        self.connectance = connectance(web)
        # Specificity and all
        self.generality = generality(web)
        self.vulnerability = vulnerability(web)
        self.specificity = specificity(web)
        self.rr = RR(web)
        self.ssi = ssi(web)
        self.bperf = web.max(1)
        # Nestedness
        NODF = nodf(web,strict=nodf_strict)
        self.nodf = NODF[0]
        self.nodf_up = NODF[2]
        self.nodf_low = NODF[1]
        # Placeholder for modularity
        self.modules = modules(self)
        # Placeholder for contributions
        self.contrib = contrib(self)
        # Placeholder for tests
        self.tests = test(self)
        # Placeholder for extinctions
        self.robustness = robustness(self)
        # Placeholder for references
        self.ref = []
        # Placeholder for species names
        self.upnames = range(self.upsp)
        self.lonames = range(self.losp)
        # For the name
        self.name = ''
    def __str__(self):
        s = 'Network '+self.name
        s+= '\t['+str(self.losp)+'x'+str(self.upsp)+'] Co = '+str(self.connectance)+'\n'
        return s
    def specieslevel(self,toScreen=True,toFile=True):
        """
        Write the species level informations
        """
        if toFile:
            f = open(self.name+'-sp.txt','w')
        Header = 'sp\tlev\tdeg\tspe\tssi\trr'
        if self.contrib.done:
            Header+= '\t'
            Header+= 'CN_w\tCN_u\tCN_l'
        if self.modules.done:
            Header+= '\t'
            Header+= 'MOD'
        if toScreen:
            print Header
        if toFile:
            f.write(Header+'\n')
        for tls in xrange(self.upsp):
            SpInfo = str(self.upnames[tls])+'\t'
            SpInfo+= 'top'+'\t'
            SpInfo+= str(self.generality[tls])+'\t'
            SpInfo+= str(self.specificity[tls])+'\t'
            SpInfo+= str(self.ssi[tls])+'\t'
            SpInfo+= str(self.rr[tls])
            if self.contrib.done:
                SpInfo+= '\t'
                SpInfo+= str(self.contrib.up_whole[tls])+'\t'
                SpInfo+= str(self.contrib.up_up[tls])+'\t'
                SpInfo+= str(self.contrib.up_low[tls])
            if self.modules.done:
                SpInfo+= '\t'
                SpInfo+= str(self.modules.up_modules[tls])
            if toScreen:
                print SpInfo
            if toFile:
                f.write(SpInfo+'\n')
        for lls in xrange(self.losp):
            SpInfo = str(self.lonames[lls])+'\t'
            SpInfo+= 'bottom'+'\t'
            SpInfo+= str(self.vulnerability[lls])+'\t'
            SpInfo+= '-----'+'\t'
            SpInfo+= '-----'+'\t'
            SpInfo+= '-----'
            if self.contrib.done:
                SpInfo+= '\t'
                SpInfo+= str(self.contrib.low_whole[lls])+'\t'
                SpInfo+= str(self.contrib.low_up[lls])+'\t'
                SpInfo+= str(self.contrib.low_low[lls])
            if self.modules.done:
                SpInfo+= '\t'
                SpInfo+= str(self.modules.low_modules[lls])
            if toScreen:
                print SpInfo
            if toFile:
                f.write(SpInfo+'\n')
        if toFile:
            f.close()
            print 'Species-level infos for the dataset '+self.name+' were written to '+self.name+'-sp.txt\n'
        return 0
    def networklevel(self,toScreen=True,toFile=True):
        """
        Outputs the network level informations
        """
        Header = 'Name'
        return 0

def openWeb(file='',t=False,name='',species_names=False):
    if species_names:
        web = oNW(file,t,name)
    else:
        web = oUW(file,t,name)
    return web

def oUW(file='',t=False,name=''):
    if file == '':
        filename = tkFileDialog.askopenfilename()
    else:
        filename = file
    # Read the web
    w = bipartite(readweb(filename),t=t)
    w.name = name
    return w


def oNW(file='',t=False,name=''):
    if file == '':
        filename = tkFileDialog.askopenfilename()
    else:
        filename = file
    upnames = []
    lonames = []
    f = tempfile.NamedTemporaryFile(delete=False)
    # Read the web
    fweb = open(filename,'r')
    cline = 0
    for line in fweb:
        if cline == 0:
            lonames = line.split()
        else:
            spl_line = line.split()
            upnames.append(spl_line[0])
            tintmat= []
            for i in range(1,len(spl_line)):
                f.write(str(float(spl_line[i]))+' ')
            f.write('\n')
        cline += 1
    f.close()
    web = oUW(f.name,t,name)
    os.unlink(f.name)
    web.upnames=upnames
    web.lonames=lonames
    return web


class modules:
    ## A class for the modules
    def __init__(self,w):
        self.w = w
        self.done = False
        self.Q = 0
        self.N = 1
        self.Qr = 1
        self.up_modules = []
        self.low_modules = []
    def detect(self,reps=100,q_c=False):
        self.done = True
        modinfos = findModules(self.w,reps=reps,q_c=q_c)
        self.Q = modinfos[0]
        if self.Q > 0:
            self.N = modinfos[1]
        self.up_modules = modinfos[2]
        self.low_modules = modinfos[3]
        if self.Q > 0:
            self.Qr = Qr(self.w,modinfos)
        else:
            self.Qr = 1
    def __str__(self):
        """
        Return the description of the modularity state
        """
        if self.done:
            s = 'Number of modules: '+str(self.N)+"\n"
            s+= 'Modularity (Qqip): '+str(round(self.Q,3)).zfill(5)+"\n"
            s+= 'Modularity (Qr)  : '+str(round(self.Qr,3)).zfill(5)+"\n"
        else:
            s = 'The detection of modularity has not been performed yet\n'
        return s

class ref:
    ## This class defines references for a dataset
    ## Fallback order is
    ##		1 DOI
    ##		2 PMID
    ##		3 JSTOR stable url
    def __init__ (self,infos):
        self.link = ''
        self.fulltext = 'Unable to retrieve citation info'
        if infos.has_key('doi'):
            self.doi = infos['doi']
            self.link_doi = "http://dx.doi.org/"+str(self.doi)
            self.fulltext = text_citation(get_citation(self.doi))
            self.link = self.link_doi
        if infos.has_key('pmid'):
            self.pmid = infos['pmid']
            self.link_pubmed = "http://www.ncbi.nlm.nih.gov/pubmed/"+str(self.pmid)
            self.fulltext = text_citation(get_citation(self.pmid))
            self.link = self.link_pubmed
        if infos.has_key('jstor'):
            self.jstor = infos['jstor']
            self.link_jstor = "http://www.jstor.org/pss/"+str(self.jstor)
            self.link = self.link_jstor
        if self.link == '':
            self.link = ' (no link available)'


def PValToText(pv):
    ptxt = ' --- '
    if pv < 0.05:
        ptxt = '  *  '
    if pv < 0.01:
        ptxt = '  ** '
    if pv < 0.001:
        ptxt= ' *** '
    if pv < 0.0001:
        ptxt = '**** '
    if pv < 0.00001:
        ptxt = '*****'
    return ptxt

class test:
    def __init__(self,web):
        """
        Initialize a test class and perform the tests
        """
        self.web = web
        self.nulls = []
        self.devnest = []
        self.devnest_lo = []
        self.devnest_up = []
        self.devqb = []
        self.devqr = []
    def donulls(self,model=null_1,replicates=100):
        self.nulls = nullModel(self.web,model,replicates)
    def nestedness(self):
        if len(self.nulls) == 0:
            self.donulls()
        d_nest = getDevNest(self.web,self.nulls)
        self.devnest = d_nest[0]
        self.devnest_lo = d_nest[1]
        self.devnest_up = d_nest[2]
    def modularity(self,repl):
        if len(self.nulls) == 0:
            self.donulls()
        ## test if the bipartite object has modules
        if not self.web.modules.done:
            self.web.modules.detect(reps=repl,q_c=self.web.q_c)
            ##
        d_mod = getDevMod(self.web,self.nulls,repl,self.web.q_c)
        self.devqr = d_mod[0]
        self.devqb = d_mod[1]
    def __str__(self):
        out = "Stat\tN0\t\tN'\t\tp\t\tIC-\t\tIC+\n"
        out +=  "---------------------------------------------\n"
        if len(self.devnest) > 0:
            out += " NODF\t"+str(round(self.devnest[0],2)).zfill(4)+"\t"+str(round(self.devnest[2],2)).zfill(4)+"\t"+PValToText(self.devnest[1])+"\t"+str(round(self.devnest[3],2)).zfill(4)+"\t"+str(round(self.devnest[4],2)).zfill(4)+"\n"
        if len(self.devnest_lo) > 0:
            out += "bNODF\t"+str(round(self.devnest_lo[0],2)).zfill(4)+"\t"+str(round(self.devnest_lo[2],2)).zfill(4)+"\t"+PValToText(self.devnest_lo[1])+"\t"+str(round(self.devnest_lo[3],2)).zfill(4)+"\t"+str(round(self.devnest_lo[4],2)).zfill(4)+"\n"
        if len(self.devnest_up) > 0:
            out += "tNODF\t"+str(round(self.devnest_up[0],2)).zfill(4)+"\t"+str(round(self.devnest_up[2],2)).zfill(4)+"\t"+PValToText(self.devnest_up[1])+"\t"+str(round(self.devnest_up[3],2)).zfill(4)+"\t"+str(round(self.devnest_up[4],2)).zfill(4)+"\n"
        if len(self.devqr) > 0:
            out += " QR    \t"+str(round(self.devqr[0],2)).zfill(4)+"\t"+str(round(self.devqr[2],2)).zfill(4)+"\t"+PValToText(self.devqr[1])+"\t"+str(round(self.devqr[3],2)).zfill(4)+"\t"+str(round(self.devqr[4],2)).zfill(4)+"\n"
        if len(self.devqb) > 0:
            out += " QB    \t"+str(round(self.devqb[0],2)).zfill(4)+"\t"+str(round(self.devqb[2],2)).zfill(4)+"\t"+PValToText(self.devqb[1])+"\t"+str(round(self.devqb[3],2)).zfill(4)+"\t"+str(round(self.devqb[4],2)).zfill(4)+"\n"
        return out

def gMIC(distrib):
    """
    Bayesian estimates of mean, and standard deviation
    """
    estimates = spp.bayes_mvs(distrib,alpha=0.95)[0]
    return[estimates[0],estimates[1][0],estimates[1][1]]

def getDevNest(w,list):
    expect = []
    expect_up = []
    expect_lo = []
    for i in list:
        Nodf = nodf(i)
        expect.append(Nodf[0])
        expect_up.append(Nodf[2])
        expect_lo.append(Nodf[1])
    testRes = spp.ttest_1samp(expect, w.nodf)
    testRes_up = spp.ttest_1samp(expect_up, w.nodf_up)
    testRes_lo = spp.ttest_1samp(expect_lo, w.nodf_low)
    OUT = [w.nodf,testRes[1]]
    OUT_up = [w.nodf_up,testRes_up[1]]
    OUT_lo = [w.nodf_low,testRes_lo[1]]
    est = gMIC(expect)
    est_lo = gMIC(expect_lo)
    est_up = gMIC(expect_up)
    for est_par in est:
        OUT.append(est_par)
    for est_par in est_lo:
        OUT_lo.append(est_par)
    for est_par in est_up:
        OUT_up.append(est_par)
    return [OUT, OUT_lo, OUT_up]

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
        tw = bipartite(c_null)
        tw.modules.detect(rep,q_c)
        Qrsim.append(tw.modules.Qr)
        Qbsim.append(tw.modules.Q)
    testResB = spp.ttest_1samp(Qbsim, wQb)
    testResR = spp.ttest_1samp(Qrsim, wQr)
    OUT_r = [wQr,testResR[1]]
    OUT_b = [wQb,testResB[1]]
    est_r = gMIC(Qrsim)
    est_b = gMIC(Qbsim)
    for est_par in est_r:
        OUT_r.append(est_par)
    for est_par in est_b:
        OUT_b.append(est_par)
    return [OUT_r,OUT_b]