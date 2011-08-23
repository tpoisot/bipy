import scipy as sp
import numpy as np
from pyx import *

from ..gen import *

def plotMatrix(w,filename='web',asnest=True):
	c = canvas.canvas()
	if asnest:
		W = sortbydegree(w.adjacency)
	else:
		W = w.adjacency
	for i in range(w.upsp):
		c.text(0, i+0.8, str(i+1),[text.halign.boxcenter, text.halign.flushcenter])
		for j in range(w.losp):
			if i == 0:
				c.text(j+0.8, 0, str(j+1),[text.halign.boxcenter, text.halign.flushcenter])
			if W[i][j] == 1:
				xc = j+0.5
				yc = i+0.5
				xd = 0.85
				yd = 0.85
				c.stroke(path.rect(xc, yc, xd, yd),[deco.filled([color.gray.black])])
	c.writePDFfile(filename)
	return 0
