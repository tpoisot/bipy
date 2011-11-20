import scipy as sp
import numpy as np

def linknum(W):
	# Number of established links within the web
	nl = 0
	for links in W:
		for link in range(0,len(links)):
			if links[link] > 0:
				nl = nl + 1
#	nl = W.sum()
	return nl

def websize(W):
	# Size of a web
	ntop = len(W)
	nbot = len(W[0])
	wsize = nbot * ntop
	return wsize


def connectance(W):
	# Connectance (as L/S^2)
	nl = linknum(W)
	ws = websize(W)
	connec = float(nl)/ws
	return connec
