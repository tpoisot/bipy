from .gen import *
from .nul import *
from .nes import *
from .spe import *

from mainfuncs import *

class bipartite:
	## This class defines a bipartite object with all structural infos
	def __init__ (self,web):
		self.web = web
		self.connectance = connectance(web)
		self.size = websize(web)		
		self.generality = generality(web)
		self.vulnerability = vulnerability(web)
		NODF = nodf(web)
		self.nodf = NODF[0]
		self.nodf_up = NODF[2]
		self.nodf_low = NODF[1]
		self.specificity = specificity(web)
		self.ref = []

class ref:
	## This class defines references for a dataset
	## Fallback order is
	##		1 DOI
	##		2 PMID
	##		3 JSTOR stable url
	def __init__ (self,infos):
		self.link = ''
		if infos.has_key('pmid'):
			self.pmid = infos['pmid']
			self.link_pubmed = "http://www.ncbi.nlm.nih.gov/pubmed/"+str(self.pmid)
			self.link = self.link_pubmed
		if infos.has_key('jstor'):
			self.jstor = infos['jstor']
			self.link_jstor = "http://www.jstor.org/pss/"+str(self.jstor)
			self.link = self.link_jstor
		if infos.has_key('doi'):
			self.doi = infos['doi']
			self.link_doi = "http://dx.doi.org/"+str(self.doi)
			self.link = self.link_doi
		if self.link == '':
			self.link = 'No references for this dataset'
