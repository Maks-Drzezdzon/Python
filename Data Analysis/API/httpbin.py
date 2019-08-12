import requests
from requests import Session, Request
import json
from requests.exceptions import HTTPError
import pprint


url = 'https://httpbin.org'
# session = requests.Session()
# session.auth('user','pass')


res = requests.get(url+'/get', params = json.dumps({'key1':'data1'}))
#print(res.json())
d = {'key2': ['data2','data3','data4']}

res = requests.post(url+'/post', params = json.dumps(d))

# print(res.text)
patch_data = {'key2':['data1','data2',]}
j_data = {'key3':'data',
          'key4': ['data2','data3','data4']}

r = requests.post(url+'/post', params = patch_data)
f = requests.post(url+'/post', json = j_data)
a = requests.patch(url+'/patch', params = patch_data , data = d)
# pprint.pprint(res.json())
# pprint.pprint(r.headers)
# pprint.pprint(a.json())
# pprint.pprint(f.json())

data = 200
c = requests.get(url+'/status/'+ str(data) )
# print(c.headers)
a = requests.get(url+'/ip')
a.headers.update({'test':'testServer'})
rep = requests.get(url+'/headers')

s = Session()
n = Request('GET',url, data = d)
pprint.pprint(n)


