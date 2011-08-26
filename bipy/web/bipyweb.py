# Bipy functions for the web
# https://github.com/petehunt/PyMySQL is needed
# in replacement of MySQLdb

from ..gen import *
from ..bipartite_class import *

import urllib
import tempfile
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
import os

def connectToDB(h='SQL09.FREEMYSQL.NET',u='tpoisot',p='wDB1312bp'):
	db = MySQLdb.connect(host=h, user=u, passwd=p, db="networks")
	print "Connection to the database established"
	return db


def closeDBconnect(dbo):
	dbo.close()
	print "Connection to the database closed"
	return 0


def websOnDB(dbo,cat='all'):
	ListOfId = []
	cursor = dbo.cursor()
	cursor.execute('USE networks')
	# Fetch webs
	cursor.execute("SELECT * FROM `webs` LIMIT 30")
	re = cursor.fetchall()
	print 'ID	NAME		CATEGORY'
	for web in re:
		if len(str(web[2])) < 10:
			TabOrNot = '	'
		else:
			TabOrNot = ''
		OutStr = '{0}	{1}{2}	{3}'.format(str(web[1]),str(web[2]),TabOrNot,str(web[3]))
		if cat == 'all':
			print OutStr
			ListOfId.append(web[1])
		else:	
			if str(web[3]) == cat:
				print OutStr
				ListOfId.append(web[1])
	return ListOfId



def getWebById(dbo,id=0):
	cursor = dbo.cursor()
	cursor.execute('USE networks')
	# Fetch webs
	cursor.execute("SELECT * FROM webs WHERE id = "+str(id)+" LIMIT 30")
	re = cursor.fetchall()
	# Write the web to a temp file
	f = tempfile.NamedTemporaryFile(delete=False)
	f.write(re[0][0])
	f.close()
	web = bipartite(readweb(f.name))
	if len(re[0][4]) > 0:
		bib = {'doi':re[0][4]}
		web.ref = ref(bib)
	else:
		if len(re[0][5]) > 0:
			bib = {'pmid':re[0][4]}
			web.ref = ref(bib)
	os.unlink(f.name)
	return web


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
