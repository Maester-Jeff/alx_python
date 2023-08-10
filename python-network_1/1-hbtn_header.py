#!/usr/bin/python3
'''Python scripts that take a URL and sends a request.'''
import requests
'''Importing sys module.'''
import sys
'''Impporting requests package.'''
if __name__ == "__main__":
    '''Code should not be executed when imported.'''
    url = sys.argv
    req = requests.get(url)
    response = req.headers['X-Request-Id']
    print(response)
