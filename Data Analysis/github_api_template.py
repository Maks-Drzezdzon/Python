# importing the requests library 
import requests
import json
import pprint

with open("C:/Users/Grim/Desktop/github_key.txt") as keys_file:
    text = keys_file.readlines()

user = text[0].strip().split(' ')[-1]
password = text[1].strip().split(' ')[-1]

# r = requests.get('https://api.github.com/user', auth=(user, password))


r = requests.get('https://api.github.com/user/repos', auth=(user, password))

json_text = json.dumps(r.json())
request_response = json.loads(json_text)

# dictionary ={"my_id": request_response['id'],"my_login": request_response['login']}

# pprint.pprint(request_response[0], indent = 4)


value = request_response[0] # for reuse                
github_api_links = {key : value[key] for key in value if "url" in key if value[key] != None}
pprint.pprint(github_api_links)