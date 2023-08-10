#!/usr/bin/python3
'''
Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id.
'''
import requests
'''Importing requests module.'''
import sys
'''Impporting sys package.'''
if __name__ == "__main__":
    '''Code should not be executed when imported.'''
    username = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/user"
    response = requests.get(url, auth = (username, password))
    if response.status_code == 200:
        '''If statement to help display the id.'''
        user_id = response.json()["id"]
        print(user_id)
    else:
        print(None)
