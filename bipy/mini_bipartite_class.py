from .gen import *
from .nes import *
from mainfuncs import *

class mini_bipartite:
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
		self.nlink = linknum(self.web)
		self.connectance = self.nlink / float(self.size)
		# Specificity and all
		self.generality = generality(web)
		self.vulnerability = vulnerability(web)
		# Perf
		self.mperf = meanperf(web,novoid=True)
		self.bperf = HighLink(web)
		# Nestedness
		NODF = nodf(web)
		self.nodf = NODF[0]
		self.nodf_up = NODF[2]
		self.nodf_low = NODF[1]
		# Stability
		self.mperf = meanperf(web,novoid=True)
		self.stability = mean(self.mperf) - np.sqrt(self.upsp*self.losp*self.connectance)
	

