#!/usr/bin/python3
'''
Python script that takes in a letter and sends
a POST request to http://0.0.0.0:5000/search_user 
with the letter as a parameter.
'''
import requests
'''Importing requests module.'''
import sys
'''Impporting sys package.'''
if __name__ == "__main__":
    '''Code should not be executed when imported.'''
    if len(sys.argv) == 2:
        '''Checking if argument is given.'''
        q = sys.argv[1]
    else:
        q = ""
    url = "http://0.0.0.0:5000/search_user"
    letter_parameter = {"q": q}
    response = requests.post(url, data = letter_parameter)
    try:
        '''Checking if repsonse is JSON formatted.'''
        json_response = response.json()
        if isinstance(json_response, dict) and json_response:
            user_id = json_response.get("id")
            user_name = json_response.get("name")
            print("[{}] {}".format(user_id, user_name))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
