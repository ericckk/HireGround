'''
Created on Oct 23, 2014

@author: cory

'''

import pprint
from apiclient.discovery import build


api_key = "Enter Api key"
search_Engine_ID = "Enter CSE key"


query = "IT professionals such as"

if(len(api_key) != 13 or len(search_Engine_ID)!= 13 ):

	service = build("customsearch", "v1", developerKey=api_key)

	response = service.cse().list(q = query, cx = search_Engine_ID).execute()
	pprint.pprint(response)
else:
	print ("Please enter an API key and CSE key into the source main.py and run script again")



