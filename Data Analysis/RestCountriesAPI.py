import requests
import json
import pprint
pprint = pprint.PrettyPrinter(indent=2)


def eu():

    request = requests.get('https://restcountries.eu/rest/v2/region/europe')
    json_text = json.dumps(request.json())
    request_response = json.loads(json_text)
    
    for element in request_response:
        try:
            pprint.pprint(request_response[0])
            # pprint.pprint(request_response[0][element]['name'])
        except:
            print("error retrieving data from region EU")

# API used for this is:
# https://restcountries.eu/#filter-response
def tag_to_name(country_dict) -> list:

    # fetches full country names from api
    country_tags = country_dict["bordering_countries"]
    list1 = []
    for tag in country_tags:
        request = requests.get('https://restcountries.eu/rest/v2/alpha/'+tag)
        json_text = json.dumps(request.json())
        request_response = json.loads(json_text)
        try:
            list1.append(request_response['name'])
        except:
            print("names of bordering countries were not found")
    return list1


def country_lookup(country: str) -> dict:
    # add functionallity so that a name like germany gets translated to a tag,
    # possibily with a try excpet finally to check if germany resolves to DE
    
    # country='pol'
    request = requests.get('https://restcountries.eu/rest/v2/alpha/'+country)
    # stores data from api in data
    # converst data to element
    json_text = json.dumps(request.json())
    # converst it to string format
    request_response = json.loads(json_text)
    try:
        country_tags = {"bordering_countries": request_response['borders']}
    except:
        print("No bordering countries")
    try:
        country_dict = {"country_name": request_response['name'],
                        # languages is a list of dictionaries
                        "bordering_countries": tag_to_name(country_tags),
                        "main_language": request_response['languages'][0]['name']}
        return pprint.pprint(country_dict)
    except:
        print("Country with name of " + "'" + country + "'" + " not found , please try another variation")


country_lookup("DE")