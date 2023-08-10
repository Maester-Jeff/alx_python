#!/usr/bin/python3
'''Python scripts that take a URL and sends a request.'''
import sys
'''Importing sys module.'''
import requests
'''Impporting requests package.'''
if __name__ == "__main__":
    '''Code should not be executed when imported.'''
    url = sys.argv[1]
    req = requests.get(url)
    print(req.headers['X-Request-Id'])
