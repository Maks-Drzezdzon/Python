import json
import requests
import os
import sys
import pprint

#  https://api.publicapis.org/
# /entries for a list of apis
# /random for one random api response
# /categories for a list of categories

def query_api(data: str) -> dict:
    if data != 'entries' or data != 'random' or data != 'categories':
        pass
    
    response = requests.get('https://api.publicapis.org/' + data.strip())
    
    if response.status_code == 200:
        response_in = json.dumps(response.json())
        response_data = json.loads(response_in)
        query_data(response_data)
    else:
        print("Error querying  https://api.publicapis.org/ "+ response.status_code)
        
def open_html_page(data: str) -> None:
    #response = requests.get(data)

    
    response = requests.get(data.strip())
    
    if response.status_code == 200:
        response_in = json.dumps(response.text)
        response_data = json.loads(response_in)
        return response_data
    else:
        print("Error querying  "+ data +" "+ response.status_code) 
        
def query_data(data: dict) -> None:
    # pprint.pprint(data)
    pprint.pprint(data['entries'][0]['Link'])
    store_response = str(data['entries'][0]['Link'])
    print("value of a " + store_response)
    open_html_page(store_response)
     # pprint.pprint(response_data)




query_api("random")








'''response = requests.get('https://api.publicapis.org/random')
idk = json.dumps(response.json())
response_data = json.loads(idk)



pprint.pprint(response_data)'''