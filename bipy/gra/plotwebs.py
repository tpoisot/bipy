import scipy as sp
import numpy as np
from pyx import *

from ..gen import *

def plotMatrix(w,filename='web',asnest=True):
	GS = 0.5
	c = canvas.canvas()
	if asnest:
		W = sortbydegree(w.adjacency)
	else:
		W = w.adjacency
	for i in range(w.upsp):
		c.text(-0.1, GS*(i+0.7), str(i+1),[text.halign.boxcenter, text.halign.flushcenter])
		for j in range(w.losp):
			if i == 0:
				c.text(GS*(j+0.9), -0.1, str(j+1),[text.halign.boxcenter, text.halign.flushcenter])
			if W[i][j] == 1:
				xc = GS*j+(GS/2)
				yc = GS*i+(GS/2)
				xd = 0.8*GS
				yd = 0.8*GS
				c.stroke(path.rect(xc, yc, xd, yd),[deco.filled([color.gray.black])])
	c.writePDFfile(filename)
	return 0
