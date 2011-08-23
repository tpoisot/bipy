## MAIN PACKAGE

__version__ = "0.3"

print "BIPY (bipartite network analysis using python) v. "+__version__+" loaded"
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
from mainfuncs import *
from bipartite_class import *
from getref import *


print "Done, you're good to go!"
print " "
print " "
print " "
