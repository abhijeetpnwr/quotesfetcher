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

		quotearr = []

		for elem in headerarr:
			headerelem = elem[0:len(elem)-8]
			if len(headerelem)>0:
				BS = BeautifulSoup(headerelem.strip())
				quote = BS.a.contents[0].strip()
				quotearr.append(quote)

		quotefornow = quotearr[randint(0,len(quotearr))]
			
		command = "/usr/bin/notify-send -t 10000 'Quote for today' \'"+quotefornow+"\'"
		print command
		
		os.system(command)



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
"http://www.brainyquote.com/quotes/topics/topic_work.html",
"http://www.brainyquote.com/quotes/authors/s/steve_jobs.html",
"http://www.brainyquote.com/quotes/authors/b/bill_gates.html",
"http://www.brainyquote.com/quotes/authors/p/peter_drucker.html",
"http://www.brainyquote.com/quotes/authors/a/a_p_j_abdul_kalam.html",
"http://www.brainyquote.com/quotes/authors/a/albert_einstein.html",
"http://www.brainyquote.com/quotes/authors/n/napoleon_bonaparte.html",
"http://www.brainyquote.com/quotes/authors/m/muhammad_ali.html",
"http://www.brainyquote.com/quotes/authors/w/will_smith.html",
"http://www.brainyquote.com/quotes/authors/w/william_shakespeare.html",
"http://www.brainyquote.com/quotes/authors/w/winston_churchill.html",
"http://www.brainyquote.com/quotes/authors/j/jim_morrison.html",
"http://www.brainyquote.com/quotes/authors/j/john_lennon.html",
"http://www.brainyquote.com/quotes/authors/j/john_lennon.html",
"http://www.brainyquote.com/quotes/authors/m/mark_twain.html",
"http://www.brainyquote.com/quotes/authors/n/nelson_mandela.html",
"http://www.brainyquote.com/quotes/authors/g/george_bernard_shaw.html",
"http://www.brainyquote.com/quotes/authors/b/bob_marley.html",
"http://www.brainyquote.com/quotes/authors/m/muhammad_ali.html"]

scrapperobj = scrapper(urlstofetch[randint(0,len(urlstofetch))])

print "This scrapper object will scrappe :",scrapperobj.weburl

scrapperobj.selector()
