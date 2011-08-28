# Bipy functions for the web
# https://github.com/petehunt/PyMySQL is needed
# in replacement of MySQLdb

from ..gen import *
from ..bipartite_class import *

import urllib
from xml.dom import minidom
import tempfile
import os

def webAsStr(W):
	Wtr = ''	
	for row in W.web:
		for col in row:
			Wtr = Wtr+str(col)+' '
		Wtr = Wtr+'\n'
	return Wtr


def valNode(obj,name):
	content = obj.getElementsByTagName(name)[0].childNodes[0].data
	return content


def getWebsFromDB(cat='all'):
	ListOfId = []
	url = 'http://bipy.alwaysdata.net/getdatabycat.py?cat='+cat
	infos = urllib.urlopen(url).read()
		
	xml = minidom.parseString(infos)
	ids = xml.getElementsByTagName('web')
	
	if len(ids) == 0:
		raise 'No corresponding identifier'
	
	print "Printing data for "+str(len(ids))+" matching record(s)"
	
	print 'ID	NAME		CATEGORY	UTL	LTL'
	for i in ids:
		ListOfId.append(valNode(i,'id'))
		if len(str(valNode(i,'name'))) < 8:
			TabOrNot = '	'
		else:
			TabOrNot = ''
		OutStr = '{0}	{1}{2}	{3}	{4}	{5}'.format(str(valNode(i,'id')),str(valNode(i,'name')),TabOrNot,str(valNode(i,'cat')),str(valNode(i,'utl')),str(valNode(i,'ltl')))
		print OutStr
	
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
