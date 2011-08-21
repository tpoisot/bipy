## Adapted from
## http://simon.net.nz/articles/query-pubmed-for-citation-information-using-a-doi-and-python/

import urllib
from xml.dom import minidom

def get_citation(q,tool="bipy",email="mail_addr"):
	search = {
		'db':'pubmed',
		'tool':tool,
		'email':email,
		'usehistory':'y',
		'retmax':1,
		'term':q
	}
	url = 'http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?' + urllib.urlencode(search)
	infos = urllib.urlopen(url).read()
	xml = minidom.parseString(infos)
	ids = xml.getElementsByTagName('Id')
	
	if len(ids) == 0:
		raise 'No corresponding identifier'
	
	id = ids[0].childNodes[0].data
	search.pop('term')
	search.pop('usehistory')
	search.pop('retmax')
	search['id'] = id
	search['retmode'] = 'xml'
	url = 'http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?' + urllib.urlencode(search)
	data = urllib.urlopen(url).read()
	return data
	
def text_citation(xml,shortAuth=True):
	xmldoc = minidom.parseString(xml)
	
	## Title
	title = xmldoc.getElementsByTagName('ArticleTitle')[0].childNodes[0].data
	
	## Authors
	authors = xmldoc.getElementsByTagName('AuthorList')[0]
	authors = authors.getElementsByTagName('Author')
	authorlist = []
	authorcount = 0
	for author in authors:
		LastName = author.getElementsByTagName('LastName')[0].childNodes[0].data
		Initials = author.getElementsByTagName('Initials')[0].childNodes[0].data
		author = '%s, %s' % (LastName, Initials)
		authorlist.append(author)
		authorcount += 1
	if shortAuth:
		if authorcount == 1:
			authorlist = authorlist[0]
		if authorcount == 2:
			authorlist = authorlist[0]+str(' & ')+authorlist[1]
		if authorcount > 2:
			authorlist = authorlist[0]+str(' et al.')
		
	## Journal infos
	journalinfo = xmldoc.getElementsByTagName('Journal')[0]
	journal = journalinfo.getElementsByTagName('Title')[0].childNodes[0].data
	journalinfo = journalinfo.getElementsByTagName('JournalIssue')[0]
	volume = journalinfo.getElementsByTagName('Volume')[0].childNodes[0].data
	issue = journalinfo.getElementsByTagName('Issue')[0].childNodes[0].data
	year = journalinfo.getElementsByTagName('Year')[0].childNodes[0].data
	pages = xmldoc.getElementsByTagName('MedlinePgn')[0].childNodes[0].data
	
	## Output
	output = authorlist+' ('+year+') '+title+' '+journal+' '+volume+'('+issue+') '+pages+'.'
	
	return output
