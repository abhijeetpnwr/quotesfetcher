import sys
import os
import time

from random import randint

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

		headerarr = fetchedstring.split("<span class=\"bqQuoteLink\">")

		for elem in headerarr:
			headerelem = elem[0:len(elem)-8]
			print "-----------"
			print headerelem
			print "---------****** ----------"
			if len(headerelem)>0:
				BS = BeautifulSoup(headerelem.strip())
				quote = BS.a.contents[0].strip()
				command = "notify-send  'Quote for today' \'"+quote+"\'"
				print command
				os.system(command)
			time.sleep(5)


#scrapperobj = scrapper("http://www.brainyquote.com/quotes/topics/topic_motivational.html")


urlstofetch = ["http://www.brainyquote.com/quotes_of_the_day.html","http://www.brainyquote.com/quotes/topics/topic_motivational.html",
"http://www.brainyquote.com/quotes/authors/m/mark_zuckerberg.html","http://www.brainyquote.com/quotes/topics/topic_motivational.html",
"http://www.brainyquote.com/quotes/topics/topic_inspirational.html",
"http://www.brainyquote.com/quotes/topics/topic_life.html",
"http://www.brainyquote.com/quotes/topics/topic_funny.html",
"http://www.brainyquote.com/quotes/topics/topic_positive.html",
"http://www.brainyquote.com/quotes/topics/topic_success.html",
"http://www.brainyquote.com/quotes/topics/topic_education.html",
"http://www.brainyquote.com/quotes/topics/topic_leadership.html",
"http://www.brainyquote.com/quotes/topics/topic_smile.html",
"http://www.brainyquote.com/quotes/topics/topic_work.html"]

scrapperobj = scrapper(urlstofetch[randint(0,len(urlstofetch))])

print "This scrapper object will scrappe :",scrapperobj.weburl

scrapperobj.selector()