from .mini_bipartite_class import *
from .gen import *
from .nul import *
from .nes import *
from .spe import *
from .mod import *
from .tes import *

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
		self.nlink = linknum(self.web)
		self.connectance = self.nlink / float(self.size)
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
		
	## Species-level function
	def specieslevel(self,modreps=100):
		# Create a filename
		if self.name != '':
			filename = self.name+'_species.txt'
		else:
			filename = 'web_species.txt'
		# Check the modules
		if self.modules == '':
			self.modules = modules(self,reps=modreps)
		# Loop on the species
		f = open(filename, 'w')
		f.write('SPEC\tLEVEL\tDEGREE\tSPE\tSSI\tMOD\n')
		for i in range(self.upsp):
			f.write(str(self.upnames[i])+'\tTOP\t'+str(self.generality[i])+'\t'+str(self.specificity[i])+'\t'+str(self.ssi[i])+'\t'+str(self.modules.up_modules[i])+'\n')
		for i in range(self.losp):
			f.write(str(self.lonames[i])+'\tBOTTOM\t'+str(self.vulnerability[i])+'\tNA\tNA\t'+str(self.modules.low_modules[i])+'\n')
		f.close()
		# Return the data
		print 'Species-level data saved to '+filename
		return 0
	
	## Network-level function
	def networklevel(self,modreps=50,nullreps=100,fun=null2,maxiter=1000,robseq=300,robupper=True,robfile=False):
		# Create a filename
		if self.name != '':
			filename = self.name+'_network.txt'
		else:
			filename = 'web_network.txt'
		# Check the modules
		if self.modules == '':
			self.modules = modules(self,reps=modreps)
		# Do the null models
		NullList = nullModel(self,fun=fun,nreps=nullreps,maxiter=maxiter)
		# Check deviation of nestedness
		DevNest = getDevNest(self,NullList)
		MeanDev = mean(DevNest)
		StdDev = np.std(DevNest)
		SignifDev = sp.stats.ttest_1samp(DevNest,0)
		# Check deviation of modularity
		if self.modules.N > 1:
			DevMod = getDevQ(self,NullList)
			MeanDevMod = mean(DevMod)
			StdDevMod = np.std(DevMod)
			SignifDevMod = sp.stats.ttest_1samp(DevMod,0)
		else:
			MeanDevMod = 0
			StdDevMod = 0
			SignifDevMod = [0,1]
		# Perform robustness analysis
		Rrand = extinctRobustness(self,nreps=robseq,removelower=robupper,tofile=robfile)
		Rwors = extinctRobustness(self,method='gtos',nreps=1,removelower=robupper,tofile=robfile)
		Rbest = extinctRobustness(self,method='stog',nreps=1,removelower=robupper,tofile=robfile)
		###################################################
		# Print the data
		f = open(filename, 'w')
		## General informations
		f.write('NAME\t'+self.name+'\n')
		f.write('SIZE\t'+str(self.size)+'\n')
		f.write('UP_SP\t'+str(self.upsp)+'\n')
		f.write('LO_SP\t'+str(self.losp)+'\n')
		f.write('CONN\t'+str(self.connectance)+'\n')
		## Nestedness
		f.write('NODF\t'+str(self.nodf)+'\n')
		f.write('NODF_UP\t'+str(self.nodf_up)+'\n')
		f.write('NODF_LO\t'+str(self.nodf_low)+'\n')
		f.write('NODF_DEV\t'+str(round(MeanDev,3))+'\n')
		f.write('NODF_DEV_SD\t'+str(round(StdDev,3))+'\n')
		f.write('NODF_DEV_SIGNIF\t'+str(SignifDev[1])+'\n')
		## Modularity
		f.write('QBIP\t'+str(self.modules.Q)+'\n')
		f.write('NMOD\t'+str(self.modules.N)+'\n')
		f.write('QR\t'+str(self.modules.Qr)+'\n')
		f.write('MOD_DEV\t'+str(round(MeanDevMod,3))+'\n')
		f.write('MOD_DEV_SD\t'+str(round(StdDevMod,3))+'\n')
		f.write('MOD_DEV_SIGNIF\t'+str(SignifDevMod[1])+'\n')
		## Robustness
		f.write('ROB_RANDOM\t'+str(extinctionScore(Rrand))+'\n')
		f.write('ROB_GtoS\t'+str(extinctionScore(Rwors))+'\n')
		f.write('ROB_StoG\t'+str(extinctionScore(Rbest))+'\n')
		f.close()
		###################################################
		# Return the data
		print 'Network-level data saved to '+filename
		return 0
	
	## Module-level functions
	def modulelevel(self):
		# Create a filename
		if self.name != '':
			filename = self.name+'_modules.txt'
		else:
			filename = 'web_modules.txt'
		# Check the modules
		if self.modules == '':
			self.modules = modules(self,reps=modreps)
		# If modularity
		if self.modules.N > 1:
			f = open(filename, 'w')
			f.write('MOD\tUP SP\tLO SP\tNES\tCONN\n')
			mods = subWebs(self)
			cmod = 1
			for mo in mods:
				mod_stats = []
				# Is the network of size 2 or more?
				NUp = len(mo)
				NLo = len(mo[0])
				if (NUp > 1) & (NLo > 1):
					tnet = mini_bipartite(mo)
					f.write(str(cmod)+'\t'+str(tnet.upsp)+'\t'+str(tnet.losp)+'\t'+str(tnet.nodf)+'\t'+str(tnet.connectance)+'\n')
				else:
					f.write(str(cmod)+'\t'+str(NUp)+'\t'+str(NLo)+'\t'+'NA'+'\t'+'NA'+'\n')
				cmod += 1
			f.close()
		else:
			print 'There are no modules within this web'
		# Return 0
		print 'Module-level data saved to '+filename
		return 0
	


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
