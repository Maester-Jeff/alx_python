#!/usr/bin/python3
'''Script that fetches a URL.'''
import requests
'''Importing requests package.'''
req = requests.get('https://alu-intranet.hbtn.io/status')
print("Body response:       \n -type: {} \n -content: {}".format(type(req.text), req.text))
