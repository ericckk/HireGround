#@author - Eric Kingori
#this scraper is extract all text from most websites
#input designed for demo and testing purposes intergration into full sytem will not require user input
#output will also be modified from print statements to data written to a file


import urllib
import urllib2
import mechanize
from bs4 import BeautifulSoup

#set up the browser 
def browser():
	br = mechanize.Browser();
	br.set_handle_robots(False)
	headers = [("user-agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5)")]
	br.addheaders = headers
	return br


#sending the request and storing the info
def openLink(br,url):	
	try:	
		rawData =  br.open(url).read()
		soup = BeautifulSoup(rawData)
		return soup
	except urllib2.HTTPError, e:
		print "HTTP Error code: " + str(e.code)
		if (e.code == 404):
			print "Page not found"
		return False

#extract data from link and save it to file
def extractText(soup):
	f = open('result.txt', 'w')
	f.write(soup.get_text().encode('UTF-8'))
	f.close()
	print("Done")


#calling the defined functions
br = browser()
url = str(raw_input("enter or paste url to be opened: \n"))
soup = openLink(br, url)
if (soup != False):
	extractText(soup)

