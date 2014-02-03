# -*- coding: utf-8 -*-
'''
This script allows you to start production with multiple files
on your auphonic account.
It can be used to batch process many files at once.

It uses the Auphonic API for batch processing:
https://auphonic.com/developers

Author: Georg Holzmann, Andre Rattinger
Date: Sept 2012

'''

import sys
import getpass

try:
    import requests
    from requests.auth import HTTPBasicAuth

    if int(requests.__version__.split('.')[1]) < 12:
        print

except:
    print "Please install python requests!"
    print "Instructions can be found here:"
    print "http://docs.python-requests.org/en/latest/user/install/"


# Auphonic API url
API_URL = "https://auphonic.com/api/simple/productions.json"


def soundProcessWithAuphonic(f):
    """ Main function.
    """
    #files = sys.argv[1:]
    #if not files:
    #    print "Usage: batch-upload.py [file [file ...]]"
    #    return

    print "\nWelcome to the Auphonic upload script!"

    #print "\nPlease enter your Auphonic account information:"
    username = 'ashuven63@gmail.com'
    password = 'ashu177'
    #print "ATTENTION: use this function with care and don't spam our system!"
    #confirm = raw_input('(y/N): ')
    #if confirm != "y":
    #    return

    #print "\nOK, if you are sure, let's make new productions ..."
    #print
    preset = 'aPZCk3SVNZGPUfPGEgA76Q'

    data = {'preset': preset, 'action': 'start', }
    input_files = {}

    # iterate through all files and create a new production for each one
    #print "\nCreating new productions:"
    #print "files", files
    #f = 'tr.wav'
    #    print "- %s" % f
    input_files['input_file'] = open(f, 'r')
    print "opened file"
    requests.post(API_URL, data=data, files=input_files,
                              auth=HTTPBasicAuth(str(username), str(password)))

    print "\nFinished!"
    print "Please check your auphonic account or email for status updates!\n"


#if __name__ == "__main__":
#    main()
