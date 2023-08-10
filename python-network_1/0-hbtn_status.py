#!/usr/bin/python3
'''Script that fetches a URL.'''
import requests
'''Importing requests package.'''
if __name__ == "__main__":
    '''Code should not be executed when imported.'''
    req = requests.get('https://alu-intranet.hbtn.io/status')
    print("Body response:\n\t- type: {}\n\t- content: {}".format(type(req.text), req.text))
