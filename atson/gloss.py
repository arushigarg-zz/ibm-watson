from urllib2 import Request, urlopen, URLError
from xml.etree.ElementTree import parse
import xmltodict, json
request = Request('http://www.dictionaryapi.com/api/v1/references/collegiate/xml/test?key=728dd5df-1f08-4509-95d7-e2ce9dc3b363')

try:
	response = urlopen(request)
	kittens = response.read()
	#print kittens[559:1000]
	#tree = parse(response)
	#root = tree.getroot()
	o = xmltodict.parse(kittens)
	print json.dumps(o) 
	# '{"e": {"a": ["text", "text"]}}'
	#for child in root:
	#	print(child.tag, child.attrib)

except URLError, e:
    print 'No kittez. Got an error code:', e