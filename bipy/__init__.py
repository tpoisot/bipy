## MAIN PACKAGE

__name__ = "bipy"

from bipartite_class import * # General class for bipartite webs
from .null import * # Null models
from .base import * # General functions
from .nes import * # Nestedness related functions
from .spe import * # Specificity
from .mod import * # Modularity detection
from .graphs import * # Graphic utilities
from .web import * # Web functions
from .tests import * # Test of deviation from null models
from mainfuncs import * # Other functions
from getref import * # Functions to get the bibliographical infos
