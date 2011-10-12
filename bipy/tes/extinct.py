from .tests import *

def extinctRobustness(w,method='random',removelower=True,tofile=False,nreps=100):
	######
	#
	# method
	# Must be one of
	#	random : random removal
	#	stog : specialists to generalists
	#	gtos : generalists to specialists
	#
	# removelower
	#	tells if the upper or lower level is removed
	#
	# nreps
	#	Number of extinction sequences to perform
	#
	######
	return 0