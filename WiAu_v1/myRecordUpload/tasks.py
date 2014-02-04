from celery import Celery
import sys
import getpass
import requests
from requests.auth import HTTPBasicAuth
API_URL = "https://auphonic.com/api/simple/productions.json"
API_DETAILS_URL = "https://auphonic.com/api/production/{uuid}.json"

app = Celery('tasks', broker='redis://localhost')

#@app.task
#def add(x, y):
#    return x + y
@app.task(name='myRecordUpload.tasks.soundProcessingWithAuphonicTask')
def soundProcessingWithAuphonicTask(f):
	username = 'ashuven63@gmail.com'
	password = 'ashu177'
	preset = 'aPZCk3SVNZGPUfPGEgA76Q'
	data = {'preset': preset, 'action': 'start', }
	input_files = {}
	input_files['input_file'] = open(f, 'r')
	print "opened file"
	response_upload = requests.post(API_URL, data=data, files=input_files,auth=HTTPBasicAuth(str(username), str(password)))
	return 0
    
