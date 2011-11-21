from .base import *
from .null import *
from .nes import *
from .spe import *
from .mod import *
#from .tests import *

from getref import *
from mainfuncs import *

import scipy as sp
import numpy as np
from scipy import stats

import tempfile
import os
import tkFileDialog

def loadweb(file='',t=False,name=''):
	if file == '':
		filename = tkFileDialog.askopenfilename()
	else:
		filename = file
	# Read the web
	w = bipartite(readweb(filename),t=t)
	w.name = name
	return w


def loadwebNamed(file='',name=''):
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
	web = bipartite(readweb(f.name))
	os.unlink(f.name)
	web.name = name
	web.upnames=upnames
	web.lonames=lonames
	return web


class bipartite:
	## This class defines a bipartite object with all structural infos
	def __init__ (self,web,t=False):
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
		self.mperf = meanperf(web,novoid=True)
		self.bperf = HighLink(web)
		# Nestedness
		NODF = nodf(web)
		self.nodf = NODF[0]
		self.nodf_up = NODF[2]
		self.nodf_low = NODF[1]
		# Stability
		self.stability = mean(self.mperf) - np.sqrt(self.upsp*self.losp*self.connectance)
		# Placeholder for modularity
		self.modules = ''
		# Placeholder for references
		self.ref = []
		# Placeholder for species names
		self.upnames = range(self.upsp)
		self.lonames = range(self.losp)
		# For the name
		self.name = ''


class modules:
	## A class for the modules
	def __init__(self,w,reps=100):
		modinfos = findModules(w,reps=reps)
		self.Q = modinfos[0]
		if self.Q > 0:
			self.N = modinfos[1]
		else:
			self.N = 1
		self.up_modules = modinfos[2]
		self.low_modules = modinfos[3]
		if self.Q > 0:
			self.Qr = Qr(w,modinfos)
		else:
			self.Qr = 1
	


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
