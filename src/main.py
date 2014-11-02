'''
Created on Oct 23, 2014

@author: Cory
@author: Matt
'''

import pprint
from apiclient.discovery import build


api_key = "Enter API key"
search_Engine_ID = "Enter CSE Key"
query = "Jobs in Information Technolgy Domain"

if(len(api_key) != 13 or len(search_Engine_ID)!= 13 ):
	service = build("customsearch", "v1", developerKey=api_key)

	#file that will hold the output
	#will create the file if it does not exist (w+)
	output = open('output/output.txt', 'w+')

	response = service.cse().list(q = query, cx = search_Engine_ID).execute()
	#pprint.pprint(response, output)

	#iterate through the keys in the query response (dictionary)
	for key in response.keys():
	    #items key holds the link information
	    if key == "items":
		#iterate over the items dictionary
		for itemValue in response[key]:
		    #iterate over the keys in that dictionary
		    for itemKey in itemValue.keys():
		        #print if it is a link
		        if itemKey == "link":
		            output.write(itemValue[itemKey])
		            output.write("\n")
else:
	print ("Please enter an API key and CSE key into the source main.py and run script again")
	

