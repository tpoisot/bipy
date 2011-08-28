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


def getWebById(id=0):
	url = 'http://bipy.alwaysdata.net/getdatabyid.py?id='+str(id)
	infos = urllib.urlopen(url).read()	
	xml = minidom.parseString(infos)
	ids = xml.getElementsByTagName('web')[0]
	#
	f = tempfile.NamedTemporaryFile(delete=False)
	f.write(valNode(ids,'int'))
	f.close()
	web = bipartite(readweb(f.name))
	if len(valNode(ids,'doi')) > 0:
		bib = {'doi':valNode(ids,'doi')}
		web.ref = ref(bib)
	else:
		if len(valNode(ids,'pmid')) > 0:
			bib = {'pmid':valNode(ids,'pmid')}
			web.ref = ref(bib)
	os.unlink(f.name)
	
	return web
