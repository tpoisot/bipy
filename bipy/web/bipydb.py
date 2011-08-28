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


def registerAsContributor(infos,outfile='./WDB_contribinfos.txt'):
	f = open(outfile, 'w')
	url = 'http://bipy.alwaysdata.net/adduser.py?'+urllib.urlencode(infos)
	infos = urllib.urlopen(url).read()
	xml = minidom.parseString(infos)
	i = xml.getElementsByTagName('contrib')[0]
	#
	print "Thank you "+valNode(i,'rname')+" "+valNode(i,'rsname')+", "
	print "your registration was successful. Please keep all these informations."
	print "They are written in the file "+str(outfile)
	print ""
	if len(valNode(i,'msg')) > 0:
		print valNode(i,'msg')
	print "USERNAME: "+valNode(i,'user')
	f.write("USERNAME: "+valNode(i,'user')+'\n')
	print "PASSWORD: "+valNode(i,'pwd')
	f.write("PASSWORD: "+valNode(i,'pwd')+'\n')
	print "API KEY : "+valNode(i,'apikey')
	f.write("API KEY : "+valNode(i,'apikey')+'\n')
	print "EMAIL   : "+valNode(i,'eml')
	f.write("EMAIL   : "+valNode(i,'eml')+'\n')
	
	return web


def contributeNetwork(bpobj,addinfos,apikey='')
	
	getWebsFromDB(cat=addinfos['cat'])
	return 0