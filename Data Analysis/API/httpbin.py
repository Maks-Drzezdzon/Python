import requests
import json
from requests.exceptions import HTTPError
import pprint

res = requests.get('https://httpbin.org/get', params = json.dumps({'key1':'data1'}))
#print(res.json())

res = requests.post('https://httpbin.org/post', params = json.dumps({'key2': ['data2','data3','data4']}))
print(res.text)