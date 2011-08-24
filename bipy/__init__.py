## MAIN PACKAGE

__name__ = "bipy"

print "BIPY (bipartite network analysis using python) loaded"
print "---"
print "Timothee Poisot - Universite Montpellier 2 - Contact : tpoisot@um2.fr"
print "---"
print "Loading functions"

# Load the null models utilities
from .gen import *
from .nul import *
from .nes import *
from .spe import *
from .mod import *
from .gra import *
from .web import * # Web functions
from mainfuncs import *
from bipartite_class import *
from getref import *


print "Done, you're good to go!"
print " "
print " "
print " "
