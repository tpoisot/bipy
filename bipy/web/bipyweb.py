# Bipy functions for the web

from ..gen import *
from ..bipartite_class import *

import urllib
import tempfile
import os

##### OTHER WEB FUNCTIONS

def readRemoteWeb(url,as_bip=True,t=False):
	f = tempfile.NamedTemporaryFile(delete=False)
	webFile = urllib.urlopen(url)
	f.write(webFile.read())
	webFile.close()
	f.close()
	web = readweb(f.name)
	if as_bip:
		web = bipartite(web,t)
	os.unlink(f.name)
	return web	
