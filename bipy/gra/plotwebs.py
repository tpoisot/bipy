import scipy as sp
import numpy as np
from pyx import *

from ..gen import *
from ..mod import *

def plotMatrix(w,filename='web',asnest=True):
	GS = 0.5
	c = canvas.canvas()
	if asnest:
		W = np.copy(sortbydegree(w.adjacency))
	else:
		W = np.copy(w.adjacency)
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
				c.stroke(path.rect(xc, yc, xd, yd),[deco.filled([color.gray.black])])
	c.writePDFfile(filename)
	return 0

def plotModules(w,mod,filename='web',col=True):
	GS = 0.5
	# Organise web by communities
	g = mod[2]
	cg = sorted(g)
	h = mod[3]
	ch = sorted(h)
	W = sortbymodule(w,g,h)
	ListOfColors = [color.cmyk.Gray,
		color.cmyk.RedOrange,
		color.cmyk.NavyBlue,
		color.cmyk.ForestGreen,
		color.cmyk.YellowOrange,
		color.cmyk.Black,
		color.cmyk.RedViolet,
		color.cmyk.ProcessBlue]
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
				if col:
					if cg[i] == ch[j]:
						CCol = ListOfColors[cg[i]]
					else:
						CCol = ListOfColors[0]
				else:
					CCol = color.gray.black
				c.stroke(path.rect(xc, yc, xd, yd),[deco.stroked.clear,deco.filled([CCol])])
	c.writePDFfile(filename)
	return 0
