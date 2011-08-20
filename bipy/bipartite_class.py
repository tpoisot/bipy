from .gen import *
from .nul import *
from .nes import *
from .spe import *

from mainfuncs import *

class bipartite:
	## This class defines a bipartite object with all structural infos
	def __init__ (self,web):
		self.web = web
		self.specificity = specificity(web)
		self.connectance = connectance(web)
		self.size = websize(web)		
		self.generality = generality(web)
		self.vulnerability = vulnerability(web)
		NODF = nodf(web)
		self.nodf = NODF[0]
		self.nodf_up = NODF[2]
		self.nodf_low = NODF[1]
