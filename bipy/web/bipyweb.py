# Bipy functions for the web

from ..gen import *
from ..bipartite_class import *

import urllib
import tempfile
import MySQLdb
import os

def readRemoteWeb(url,as_bip=True,t=False):
	"""Copy the contents of a file from a given URL
	to a local file.
	"""
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


#def readFromSql(i):
#	Host = SQL09.FREEMYSQL.NET
#	User = tpoisot
#	Pass = wDB1312bp
#	db = MySQLdb.connect(host=Host, user=User, passwd=Pass, db="networks")
#	return 0
