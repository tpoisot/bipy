from .nes import *
from .mod import *
from .contrib import *
from .null import *
from .tests import *

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
        self.nodf_strict = nodf_strict
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
    def txt(self):
        """
        Prints a text version of the network to the console
        Can be used to view quickly the shape of a network
        """
        for line in self.adjacency:
            s = ''
            for char in line:
                if char > 0:
                    s += u'\u2588'
                else:
                    s += '-'
            print s
        return 0
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

## Sort by modules
def sortbymodule(W,g,h):
    sg = sorted(np.copy(g),reverse=True)
    sh = sorted(np.copy(h),reverse=True)
    # Step 1 : Sort a matrix by module
    ## VOID VECTORS FOR THE SORTED SPECIES NAMES
    oTnames = W.upnames
    oBnames = W.lonames
    vTnames = np.copy(oTnames)
    vBnames = np.copy(oBnames)
    ## Step 1a : sort TLO
    rG = rank(g)
    nW = np.zeros((W.upsp,W.losp))
    for ro in range(0,W.upsp):
        nW[rG[ro]] = W.web[ro]
        vTnames[rG[ro]] = oTnames[ro]
    ## Step 1b : sort BLO
    nW = nW.T
    dW = np.zeros((W.upsp,W.losp)).T
    rG = rank(h)
    for ro in range(0,W.losp):
        dW[rG[ro]] = nW[ro]
        vBnames[rG[ro]] = oBnames[ro]
    web = np.copy(dW.T)
    # New temp files for the names
    oBnames = np.copy(vBnames)
    oTnames = np.copy(vTnames)
    # Step 2 : Sort each module by degree
    uniqueMod = sorted(uniquify(sg),reverse=True)
    ## Step 2a : sort TLO
    totalMadeInt = 0
    tempIntCnt = 0
    tdeg = generality(web)
    nweb = np.zeros(np.shape(web))
    for module in uniqueMod:
        totalMadeInt += tempIntCnt
        tempIntCnt = 0
        cdeg = []
        for sp in range(len(tdeg)):
            if sg[sp] == module:
                cdeg.append(tdeg[sp])
        rnk = rank(cdeg)
        for ro in range(len(rnk)):
            nweb[totalMadeInt+rnk[ro]] = web[totalMadeInt+ro]
            vTnames[totalMadeInt+rnk[ro]] = oTnames[totalMadeInt+ro]
            tempIntCnt += 1
    web = np.copy(nweb.T)
    ## Step 2b : sort BLO
    totalMadeInt = 0
    tempIntCnt = 0
    tdeg = generality(web)
    nweb = np.zeros(np.shape(web))
    for module in uniqueMod:
        totalMadeInt += tempIntCnt
        tempIntCnt = 0
        cdeg = []
        for sp in range(len(tdeg)):
            if sh[sp] == module:
                cdeg.append(tdeg[sp])
        rnk = rank(cdeg)
        for ro in range(len(rnk)):
            nweb[totalMadeInt+rnk[ro]] = web[totalMadeInt+ro]
            vBnames[totalMadeInt+rnk[ro]] = oBnames[totalMadeInt+ro]
            tempIntCnt += 1
    Fweb = bipartite(np.copy(nweb.T))
    Fweb.upnames = vTnames
    Fweb.lonames = vBnames
    return Fweb

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