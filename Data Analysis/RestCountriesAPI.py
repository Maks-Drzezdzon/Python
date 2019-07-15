import requests,json,pprint
pretty = pprint.PrettyPrinter(indent = 2)

def eu():
    request = requests.get('https://restcountries.eu/rest/v2/region/europe')
    json_text = json.dumps(request.json())
    request_response = json.loads(json_text)
    #pretty.pprint(request_response)
    for element in request_response:
        pretty.pprint(request_response[element])

eu()


#API used for this is:
#https://restcountries.eu/#filter-response
def tag_to_name(country_dict) -> list:
    #fetches full country names from api
    country_tags = country_dict["bordering_countries"]
    list1=[]
    
    for tag in country_tags:
        request = requests.get('https://restcountries.eu/rest/v2/alpha/'+tag)
        json_text = json.dumps(request.json())
        request_response = json.loads(json_text)
        list1.append(request_response['name'])
        
    return list1

def country_lookup(country:str) -> dict:
    #request = requests.get('https://restcountries.eu/rest/v2/region/europe')
    #country='pol'
    request = requests.get('https://restcountries.eu/rest/v2/alpha/'+country)
    #stores data from api in data
    #converst data to element
    json_text = json.dumps(request.json())
    #converst it to string format
    request_response = json.loads(json_text)

    country_tags = {"bordering_countries":request_response['borders']}
    
    country_dict = { "country_name":request_response['name'],
                  #languages used retrives a list of dictionaries hence the [0] to get the first dictionary object and access the name key
                  "bordering_countries":tag_to_name(country_tags),
                  "national_language":request_response['languages'][0]['name']}
    
    return country_dict


print(country_lookup("pol"))
    


    


