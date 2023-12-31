#!/usr/bin/python3
'''Python scripts that take a URL and sends a request.'''
import requests
'''Importing requests module.'''
import sys
'''Impporting sys package.'''
if __name__ == "__main__":
    '''Code should not be executed when imported.'''
    url = sys.argv[1]
    req = requests.get(url)
    response = req.headers.get('X-Request-Id')
    print(response)
