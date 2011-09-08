import scipy as sp
import numpy as np
from pyx import *

from ..gen import *
from ..mod import *

# Generic function for plotting
def plotWeb(w,minfo='',filename='web',asnest=True,asbeads=False,colors=True):
	if minfo=='':
		# If the modules infos are void...
		if asnest:
			# If we want the web to be nested
			W = np.copy(sortbydegree(w.web))
		else:
			# Else
			W = np.copy(w.web)
		# We plot the web as a matrix
		plotMatrix(W,filename=filename,withcolors=colors)
	else:
		# If we give modules as an argument...
		g = np.copy(minfo[2])
		h = np.copy(minfo[3])
		W = np.copy(sortbymodule(w,g,h))
		# And... the plot
		plotModules(W,minfo,filename=filename,withcolors=colors)
	# In the end, we output the web sorted as in the plot
	# This may be useful
	return W


def plotMatrix(w,filename='web',withcolors=True):
	GS = 0.5
	W = np.copy(w)
	w = bipartite(w)
	c = canvas.canvas()
	if withcolors:
		MLink = max(w.bperf)
		for i in range(w.upsp):
			for j in range(w.losp):
				W[i][j] = round((W[i][j]/float(MLink))*100,0)
		# Define the color gradient
		ListOfColors = [color.gradient.Gray.select(i, 101) for i in range(101)]
	for i in range(w.upsp):
		c.text(-0.1, GS*(i+0.7), str(i+1),[text.halign.boxcenter, text.halign.flushcenter])
		for j in range(w.losp):
			if i == 0:
				c.text(GS*(j+0.9), -0.1, str(j+1),[text.halign.boxcenter, text.halign.flushcenter])
			if W[i][j] > 0:
				xc = GS*j+(GS/2)
				yc = GS*i+(GS/2)
				xd = 0.8*GS
				yd = 0.8*GS
				if withcolors:
					c.stroke(path.rect(xc, yc, xd, yd),[deco.stroked.clear,deco.filled([ListOfColors[int(W[i][j])]])])
				else:
					c.stroke(path.rect(xc, yc, xd, yd),[deco.stroked.clear,deco.filled([color.gray.black])])
	c.writePDFfile(filename)
	return 0


def plotModules(w,mod,filename='web',withcolors=True):
	GS = 0.5
	# Organise web by communities
	W = np.copy(w)
	g = np.copy(mod[2])
	cg = sorted(g,reverse=True)
	h = np.copy(mod[3])
	ch = sorted(h,reverse=True)
	w = mini_bipartite(w)
	ListOfColors = [color.gradient.Hue.select(i, (mod[1]+1)) for i in range(mod[1]+1)]
	# Plot
	c = canvas.canvas()
	for i in range(w.upsp):
		c.text(-0.1, GS*(i+0.7), str(i+1),[text.halign.boxcenter, text.halign.flushcenter])
		for j in range(w.losp):
			if i == 0:
				c.text(GS*(j+0.9), -0.1, str(j+1),[text.halign.boxcenter, text.halign.flushcenter])
			if W[i][j] > 0:
				xc = GS*j+(GS/2)
				yc = GS*i+(GS/2)
				xd = 0.8*GS
				yd = 0.8*GS
				if cg[i] == ch[j]:
					if withcolors:
						CCol = ListOfColors[(cg[i]-1)]
					else:
						CCol = color.gray.black
				else:
					CCol = color.cmyk.Gray
				c.stroke(path.rect(xc, yc, xd, yd),[deco.stroked.clear,deco.filled([CCol])])
	c.writePDFfile(filename)
	return 0
