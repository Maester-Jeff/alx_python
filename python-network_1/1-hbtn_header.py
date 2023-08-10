'''
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
    response = req.headers['X-Request-Id']
    print(response)
'''
import requests
import sys
# Get the URL from the command line arguments.
url = sys.argv[1]
# Create a request object using the requests.get() function.
request = requests.get(url)
# Send the request and get the response.
response = request.content
# Get the value of the X-Request-Id variable from the response header.
x_request_id = response.headers.get('X-Request-Id')
# Print the value of the X-Request-Id variable.
print(x_request_id)