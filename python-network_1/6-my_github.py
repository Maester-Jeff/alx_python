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
    user_name = sys.argv[1]
    user_password = sys.argv[2]
    url = "https://api.github.com/user"
    auth = requests.auth.HTTPBasicAuth(user_name, user_password)
    response = requests.get("https://api.github.com/user", auth = auth)
    
    if response.status_code == 200:
        user_info = response.json()
        user_id = user_info.get("id")
        print(user_id)
    else:
        print("Error code:", response.status_code)
