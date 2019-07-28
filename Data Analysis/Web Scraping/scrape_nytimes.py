# import sys
# sys.path.insert(1,'..//API')
# PublicAPI.query_public_api("random")
# from PublicAPI import *
from bs4 import BeautifulSoup
import requests
import pandas as pd
# loads a basic html article page
response = requests.get('https://www.nytimes.com/interactive/2017/06/23/opinion/trumps-lies.html')
soup = BeautifulSoup(response.text,'html.parser')
# finds pattern in html with tags span class short-desc
results = soup.find_all('span', attrs={'class' : 'short-desc'})
"""
# counting data len
#print(len(results))
# inspecting the first few rows
#print(results[0:3])
first_result = results[0]
date_stored = first_result.find('strong').text[0:-1]+', 2017'
# in order to get data out of this html page
# converting it to a list split by tags
# print(first_result.contents[1]) # returns a list
print(first_result.contents[1][1:-2]) # to get rid of the " "
# now to find another statment search for the tag
first_result.find('a').text[1:-1]
# now the url
# bs treats these as a key value pair ['href'] : url
first_result.find('a')['href']
"""
records =[]
for element in results:
    date = element.find('strong').text[0:-1] + ', 2017'
    assertion = element.contents[1][1:-2]
    oppinion = element.find('a').text[1:-1]
    url = element.find('a')['href']
    records.append((date, assertion, oppinion, url))   
#print(records[0:3])
df = pd.DataFrame(records, columns=['date','assertion','oppinion','url'])
# print(df.head())
# formatting date
df['date'] = pd.to_datetime(df['date'])
# index=False for not including index in csv
df.to_csv('nytimes.csv', index = False, encoding='utf-8')