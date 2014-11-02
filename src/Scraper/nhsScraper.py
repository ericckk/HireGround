#@author - Eric Kingori
#this scraper is extract health care related skills from nhs.uk website.
#input designed for demo and testing purposes intergration into full sytem will not require user input
#output is data written to the "result.txt" file

import urllib2
import urllib
import mechanize
from bs4 import BeautifulSoup

#set up the browser 
def browser():

	br = mechanize.Browser();
	br.set_handle_robots(False) 
	# spoof some headers so the request appears to be coming from a browser, not a bot
	headers = [("user-agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5)")]
	br.addheaders = headers
	return br

#creating the url link 
def url(selection):
	categories = ['allied-health-professions','ambulance-service-team','Dental Team','Doctors','Health Informatics','healthcare-science','nursing']
	query = str(categories[selection]).lower()
	query = query.replace(" ","-")
	url = "http://www.nhscareers.nhs.uk/explore-by-career/"+ query +"/skills-required/"
	return str(url)



def get(br, url):
	#sending the request and storing the info
	try:	
		rawData =  br.open(url).read()
		soup = BeautifulSoup(rawData)
		return soup
	except urllib2.HTTPError, e:
		print "HTTP Error code: " + str(e.code)
		if (e.code == 404):
			print "Page not found"
		return False
	#print rawData
	
	

def parse(soup):
	#print (soup.prettify().encode('utf-8'))
	info =soup.findAll('strong')
	#print (str(results).encode('utf-8'))
	for paragraph in info:
		print (paragraph.text).encode('utf-8')
	specialCases = [2,4,5]

	if selection in specialCases:
		info =soup.findAll('li')
		#print (str(results).encode('utf-8'))
		for paragraph in info:
			print (paragraph.text).encode('utf-8')
	
		

br = browser()
selection = int(input("Choose skills from the following options: \n1. Allied Health Proffessions \n2. Ambulance Service Teams\n3. Dental Teams\n4. Doctors\n5. Health Informatics\n6. Health Care science  \n7. Nursing\n "))
url=url(selection-1)
soup = get(br, url)
if (soup != False):
	parse(soup)

