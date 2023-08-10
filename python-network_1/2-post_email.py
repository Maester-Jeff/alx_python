#!/usr/bin/python3
'''
Python Python script that takes in a URL and an email address,
sends a POST request to the passed URL with the email as a 
parameter, and finally displays the body of the response.
'''
import requests
'''Importing requests module.'''
import sys
'''Impporting sys package.'''
if __name__ == "__main__":
    '''Code should not be executed when imported.'''
    url = sys.argv[1]
    email = sys.argv[2]
    email_address = {'email': email}
    req = requests.post(url, data = email_address)
    print(req.text)
