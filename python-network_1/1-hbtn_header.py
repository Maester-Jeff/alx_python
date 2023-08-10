#!/usr/bin/python3
'''Python scripts that take a URL and sends a request.'''
import os
'''Importing os module.'''
import requests
'''Impporting requests package.'''
if __name__ == "__main__":
    '''Code should not be executed when imported.'''
    req = requests.get('')
    print(req.headers['X-Request-Id'])
