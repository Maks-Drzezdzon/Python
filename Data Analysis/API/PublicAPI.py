import json
import requests
import pprint
#  https://api.publicapis.org/
# /entries for a list of apis
# /random for one random api response
# /categories for a list of categories
class PublicAPI():

    
    def query_public_api(data: str) -> dict:
        ''' pass in one of 3 args below in str form to query api 
                entries , random or categories '''
        try:
            if data != 'entries' or data != 'random' or data != 'categories':
                pass
            
            response = requests.get('https://api.publicapis.org/' + data.strip())
            
            if response.status_code == 200:
                response_in = json.dumps(response.json())
                response_data = json.loads(response_in)
                return response_data
            if data == 'random':
                PublicAPI.query_data(response_data)
            else:
                print("Error querying  https://api.publicapis.org/ "+ response.status_code)
        except Exception as err:
            print("query_public_api err in PublicAPI " + err)
    
    
    def open_html_page(data: str) -> None:
        try:
            #response = requests.get(data)
            response = requests.get(data.strip())
            # check response
            if response.status_code == 200:
                response_in = json.dumps(response.text)
                response_data = json.loads(response_in)
                return response_data
        except Exception as err:
            print("open_html_page error in PublicAPI " + err)
       
        
    def query_data(data: dict) -> None:
        # pprint.pprint(data)
        try:
            pprint.pprint(data['entries'][0]['Link'])
            store_response = str(data['entries'][0]['Link'])
            print("value " + store_response)
            #page_data = PublicAPI.open_html_page(store_response)
            # limit to first x chars
            #print(page_data[0:1000])
        except Exception as err:
            print("query_data error in PublicAPI "+err)


pprint.pprint(PublicAPI.query_public_api('entries')['entries'][0])