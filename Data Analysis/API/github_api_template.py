# importing the requests library 
import requests
import json
import pprint
from requests.exceptions import HTTPError

with open("C:/Users/Grim/Desktop/github_key.txt") as keys_file:
    text = keys_file.readlines()

user = text[0].strip().split(' ')[-1]
password = text[1].strip().split(' ')[-1]

# r = requests.get('https://api.github.com/user', auth=(user, password))

def search_user(user,password):
    r = requests.get('https://api.github.com/user/repos', auth=(user, password))
    json_text = json.dumps(r.json())
    request_response = json.loads(json_text)
    # dictionary ={"my_id": request_response['id'],"my_login": request_response['login']}
    # pprint.pprint(request_response, indent = 4)
    github_data = request_response
    value = request_response[0]
    
    repository_names = [name['full_name'] for name in github_data]                
    github_api_links = {key : value[key] for key in value if "url" in key if value[key] != None}
    link = [value[key] for key in value if "url" in key if value[key] != None]
    
    return link
    
links = search_user(user,password)
'''for link in links:
    break
    try:
        response = requests.get(link)
        response.raise_for_status()
    # 
    except HTTPError as http_err:
        print(http_err)
    except Exception as err:
        print(err)
    else:
        print("connection made")'''
        
resp = requests.delete('https://api.github.com/user/repos/Hello-World', auth=(user, password))
#pprint.pprint(json.dumps(resp.json()))
pprint.pprint(resp)

'''data = {
  "name": "test-repo",
  "description": "This is your first repository",
  "homepage": "https://github.com",
  "private": False,
  "has_issues": True,
  "has_projects": True,
  "has_wiki": True
}

payload={"name":"test"}
r = requests.get('https://api.github.com/user/repos?visibility=private', auth=(user, password))
r = requests.post('https://api.github.com/user/repos',data=json.dumps(data), auth=(user, password))
data = json.dumps(r.json())
pprint.pprint(data)'''



