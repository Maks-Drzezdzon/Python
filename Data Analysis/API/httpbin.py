import requests
import json
from requests.exceptions import HTTPError
import pprint

res = requests.get('https://httpbin.org/get', params = json.dumps({'key1':'data1'}))
#print(res.json())
d = {'key2': ['data2','data3','data4']}

res = requests.post('https://httpbin.org/post', params = json.dumps(d))

# print(res.text)
patch_data = {'key2':['data1','data2',]}
j_data = {'key3':'data',
          'key4': ['data2','data3','data4']}

r = requests.post('https://httpbin.org/post', params = patch_data)
f = requests.post('https://httpbin.org/post', json = j_data)
a = requests.patch('https://httpbin.org/patch', params = patch_data , data = d)
# pprint.pprint(res.json())
# pprint.pprint(r.headers)
# pprint.pprint(a.json())
# pprint.pprint(f.json())

data = 200
c = requests.get('https://httpbin.org/status/'+ str(data) )
print(c.headers)





