# Bipy functions for the web

from ..gen import *
from ..bipartite_class import *

import urllib
import tempfile
import os

##### OTHER WEB FUNCTIONS

def readRemoteWeb(url,t=False):
	f = tempfile.NamedTemporaryFile(delete=False)
	webFile = urllib.urlopen(url)
	f.write(webFile.read())
	webFile.close()
	f.close()
	web = readweb(f.name)
	web = bipartite(web,t)
	os.unlink(f.name)
	return web	
