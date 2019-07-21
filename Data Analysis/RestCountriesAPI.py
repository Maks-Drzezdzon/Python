import requests
import json
import pprint
import pyodbc as db
import logging
import time

# TODO use db , use logger more 

# class Country_lookup(country):
def look_up_api(country: str) -> json:
    """shorthand look up for api"""
    request = requests.get('https://restcountries.eu/rest/v2/alpha/'+country)
    # stores data from api in data
    # converst data to element
    json_text = json.dumps(request.json())
    # converst it to string format
    request_response = json.loads(json_text)
    return request_response
    

pprint = pprint.PrettyPrinter(indent=2)
'''conn = db.connect("Driver={SQL Server Native Client 11.0};"
                  "Server=;"
                  "Database=;"
                  "Trusted_Connection=yes;")'''    
    # API used for this is:
    # https://restcountries.eu/#filter-response
    
def tag_to_name(country_dict) -> list:
    """returns full country name from json dict, DE = germany"""
    # fetches full country names from api
    country_tags = country_dict["bordering_countries"]
    list_of_countries = list()
    for tag in country_tags:
        # requests data from api for each tag
        request_response = look_up_api(tag)
        try:
            # translates tag to full name using api and stores in list
            list_of_countries.append(request_response['name'])
        except Exception as err:
            print(err)
            print("name/s of bordering countrie/s were not found")
    return list_of_countries
    
    
def country_lookup(country: str) -> dict:
    # add functionallity so that a name like germany gets translated to a tag,
    # possibily with a try excpet finally to check if germany resolves to DE
    
    start_time = time.time()
    
    # logging.basicConfig(filename = "path", level = logging.DEBUG, format = LOG_FORMAT, filemode = 'w')
    # logger = logging.getLogger()
    
    request_response = look_up_api(country)
    
    try:
        country_tags = {"bordering_countries": request_response['borders']}
    except Exception as err:
        print("No bordering countries")
        print(err)
        raise
    try:
        country_dict = {"country_name": request_response['name'],
                        # languages is a list of dictionaries
                        "bordering_countries": tag_to_name(country_tags),
                        "main_language": request_response['languages'][0]['name']}
        return pprint.pprint(country_dict)
    except Exception as err:
        print("Country with name of " + "'" + country + "'" + " not found , please try another variation")
        print(err)
        raise
    finally:
        stop_time = time.time()
        time_stamp = stop_time - start_time
        # limit to x decimal places
        print("run time %.5f" % time_stamp + " seconds")
        

    

def eu() -> print:

    request = requests.get('https://restcountries.eu/rest/v2/region/europe')
    json_text = json.dumps(request.json())
    request_response = json.loads(json_text)
    
    for element in request_response:
        try:
            pprint.pprint(request_response[0])
            # pprint.pprint(request_response[0][element]['name'])
        except:
            print("error retrieving data from region EU")

country_lookup("de")

