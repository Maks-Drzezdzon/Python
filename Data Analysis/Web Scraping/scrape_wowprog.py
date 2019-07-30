import requests
from bs4 import BeautifulSoup

data = requests.get('https://www.wowprogress.com/')
soup = BeautifulSoup(data.text,'html.parser')
store=[]
'''for ele in soup.find_all('span', {'class':'innerLink ratingProgress'}):
    print(ele)'''
    
mythic_proggress = soup.find('div',{'class':'sortBy'}) # opens div with raid names
table = soup.find('table',{'class':'rating'}) # opens table with team data
data = table.find('a',{'class':'guild'}) # opens row with team data

name = data.find('nobr') # retrives name of team


realm = table.find('a',{'class':'realm'}) # retrives server team plays on
current_raid = mythic_proggress.find('span',{'class':'selected'}) # retrives current raid name
prog = table.find('span',{'class':'innerLink ratingProgress'}) # retrives current proggression 

teams=[]
team={}
print(name)
