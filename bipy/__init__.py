## MAIN PACKAGE

__version__ = "0.2"

print "BIPY (bipartite network analysis using python) v. "+__version__+" loaded"
print "Loading functions"

# Load the null models utilities
from .gen import *
from .nul import *
from .nes import *
from .spe import *

from mainfuncs import *
from bipartite_class import *


print "Done, you're good to go!"
print " "
print " "
print " "
