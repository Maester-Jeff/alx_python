#!/usr/bin/python3
'''
Python script that takes in a URL, sends a request
to the URL and displays the body of the response.
'''
import requests
'''Importing requests module.'''
import sys
'''Impporting sys package.'''
if __name__ == "__main__":
    '''Code should not be executed when imported.'''
    url = sys.argv[1]
    req = requests.get(url)
    response = req.status_code
    if response >= 400:
        '''If statement chcking whether a specific status_code arises.'''
        print("Error code: {}".format(response))
    else:
        print(req.text)
