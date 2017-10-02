# From your command line go to third_party folder skill
#
# cd /opt/mycroft/third_party
#
# python mycroft-gmail-skill --noauth_local_webserver
# 
# checking for cached credentials
#
# Go to the following link in your browser on computer with browser (this link may be different on each computer):
# 
# Enter verification code: 4/oxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx   (Please copy the code generated, and paste it there)
#

import httplib2
import os

from apiclient import discovery
from apiclient import errors
import oauth2client
from oauth2client import file
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from oauth2client.client import OAuth2WebServerFlow

import json
from json import JSONEncoder
from HTMLParser import HTMLParser
from datetime import datetime

__author__ = 'jcasoft'

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None


SCOPES = 'https://www.googleapis.com/auth/gmail.readonly'
CID = "992603803855-18na240ttgkgm4va2mvtiucqjreejvrm.apps.googleusercontent.com"
CIS = "bqde08mLgxG8JygoZjGENM-S"
APPLICATION_NAME = 'Mycroft GMail Skill'



def get_credentials():
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    print("checking for cached credentials")
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,'mycroft-gmail-skill.json')

    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        credentials = tools.run_flow(OAuth2WebServerFlow(client_id=CID,client_secret=CIS,scope=SCOPES,user_agent=APPLICATION_NAME),store)
        print 'Storing credentials to ' + credential_dir
	print 'Your GMail Skill is now authenticated '
    else:
	print 'Loaded credentials for Gmail Skill from ' + credential_dir
    return credentials


credentials = get_credentials()
http = credentials.authorize(httplib2.Http())
global service
service = discovery.build('gmail', 'v1', http=http)

try:
	user_id = "me"
	label_id = ["INBOX","IMPORTANT"]
        query = "is:unread"
	max_results = 4
	
	response = service.users().messages().list(userId=user_id,labelIds=label_id,maxResults=5,q=query).execute()

	messages = []
    	if 'messages' in response:
    		messages.extend(response['messages'])

    	while 'nextPageToken' in response:
		page_token = response['nextPageToken']
		response = service.users().messages().list(userId=user_id,labelIds=label_id,maxResults=5,q=query,pageToken=page_token).execute()
		messages.extend(response['messages'])

	print (json.dumps(messages[0], indent=4, sort_keys=True))


except errors.HttpError, error:
	print 'An error occurred: %s' % error

print 'Your Google Calendar Skill is now authenticated '
