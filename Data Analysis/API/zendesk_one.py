import requests
import pprint
import json


with open("C:/Users/Grim/Desktop/github_key.txt") as keys_file:
    text = keys_file.readlines()
    
# Set the request parameters
url = 'https://your_subdomain.zendesk.com/api/v2/groups.json'
user = text[0].strip().split(' ')[-1]
pwd = text[1].strip().split(' ')[-1]

response = requests.get(url, auth=(user, pwd))

# Check for HTTP codes other than 200
if response.status_code != 200:
    print('Status:', response.status_code, 'Problem with the request. Exiting.')
    exit()

# Decode the JSON response into a dictionary and use the data
data = response.json()
pprint.pprint(data)
'''print( 'First group = ', data['groups'][0]['name'] )

group_list = data['groups']
for group in group_list:
    print(group['name'])'''