# Bipy functions for the web
# https://github.com/petehunt/PyMySQL is needed
# in replacement of MySQLdb

from ..gen import *
from ..bipartite_class import *

import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
import urllib
import tempfile
import os

def webAsStr(W):
	Wtr = ''	
	for row in W.web:
		for col in row:
			Wtr = Wtr+str(col)+' '
		Wtr = Wtr+'\n'
	return Wtr

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
	print 'ID	NAME		CATEGORY	UTL	LTL'
	for web in re:
		if len(str(web[2])) < 8:
			TabOrNot = '	'
		else:
			TabOrNot = ''
		OutStr = '{0}	{1}{2}	{3}	{4}	{5}'.format(str(web[1]),str(web[2]),TabOrNot,str(web[3]),str(web[9]),str(web[10]))
		if cat == 'all':
			print OutStr
			ListOfId.append(web[1])
		else:	
			if str(web[3]) == cat:
				print OutStr
				ListOfId.append(web[1])
	return ListOfId


def pushWebToDB(dbo,usrid,w,infos):
	# Connect to the DB
	cursor = dbo.cursor()
	cursor.execute('USE networks')
	
	# Info strings
	i = infos
	# Convert the web to a string to upload
	wstr = webAsStr(w)
	
	print i['utl']
	
	# DOI ?
	if hasattr(w.ref,'doi'):
		i['doi'] = w.ref.doi
	else:
		i['doi'] = ''
	
	# PMID ?
	if hasattr(w.ref,'pmid'):
		i['pmid'] = w.ref.pmid
	else:
		i['pmid'] = ''
		
	# JSTOR ?
	if hasattr(w.ref,'jstor'):
		i['jstor'] = w.ref.jstor
	else:
		i['jstor'] = ''
	
	InsertQRY = """INSERT INTO `webs` (`mat`, `name`, `category`,
	`doi`, `pmid`, `jstor`, `comment`, `contributor`, `utl`, `ltl`) 
	VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}', '{9}');""".format(wstr, i['name'], i['cat'], i['doi'], i['pmid'], i['jstor'], i['comment'], str(usrid), i['utl'], i['ltl'])
	
	cursor.execute(InsertQRY)
	
	websOnDB(dbo,cat=i['cat'])
	
	return 0


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
