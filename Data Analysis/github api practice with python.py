# importing the requests library 
import requests,json

#gets request from api  
r = requests.get('https://api.github.com/user', auth=('user', 'password'))
#stores data from api in data
data = r.json()
#converst data to element
json_text = json.dumps(data)
#converst it to string format
request_response = json.loads(json_text)
#store data in dict
dictionary ={"my_id": request_response['id'],"my_login":request_response['login']}

print(dictionary)

