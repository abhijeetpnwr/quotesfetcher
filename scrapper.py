import sys
import os


#Check for beauifull soup installation
try:
    import BeautifulSoup
except ImportError:
    sys.exit("""You need Beautiful Soup ! install it from http://pypi.python.org/pypi/foo or run pip install foo.""")

#Check for requests installation
try:
    import requests
except ImportError:
    sys.exit("""You need request package installd ! """)

#check for urllib2 installation
try:
    import urllib2
except ImportError:
    sys.exit("""You need urllib2 package installd ! """)

import urllib2
import requests
from BeautifulSoup import BeautifulSoup



#Class scrapper does all the work of scrapping quotes from url 
class scrapper:
	
	weburl = ""

	def __init__(self,url):
		print "Class scrapper initialized"
		self.weburl=url

	def  selector(self):

		response = requests.get(self.weburl)
		html = response.content
		soup = BeautifulSoup(html)
		header = soup.findAll('span', attrs={'class': 'bqQuoteLink'})
		fetchedstring = unicode.join(u'\n',map(unicode,header))

		print fetchedstring

		BS = BeautifulSoup(fetchedstring)

		print BS

		quote = BS.a.contents[0].strip()

		command = "notify-send  'Quote for today' \'"+quote+"\'"
		print command
		os.system(command)


scrapperobj = scrapper("http://www.brainyquote.com/quotes_of_the_day.html")

print "This scrapper object will scrappe :",scrapperobj.weburl

scrapperobj.selector()