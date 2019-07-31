import requests
from bs4 import BeautifulSoup
import pprint

data = requests.get('https://www.wowprogress.com/')
soup = BeautifulSoup(data.text,'html.parser')
store=[]
'''for ele in soup.find_all('span', {'class':'innerLink ratingProgress'}):
    print(ele)'''
    
mythic_proggress = soup.find('div',{'class':'sortBy'}) # opens div with raid names
table = soup.find('table',{'class':'rating'}) # opens table with team data
#data = table.find('a',{'class':'guild'}) # opens row with team data
    
current_raid = mythic_proggress.find('span',{'class':'selected'}) # retrives current raid name

names = table.find_all('nobr') # retrives name of team
realms = table.find_all('a',{'class':'realm'}) # retrives server team plays on
prog = table.find_all('span',{'class':'innerLink ratingProgress'}) # retrives current proggression 

team_names = [name for element in names for name in element if name !=' ']
team_realm = [realm for element in realms for realm in element if realm !=' ']
current_prog = [progress for element in prog for data in element for progress in data if progress !=' ']

team_scored = dict(zip(team_names,current_prog))
team_servers = dict(zip(team_names,team_realm))
pprint.pprint (team_servers)
pprint.pprint (team_scored)


#print(len(team_names))
#print(current_prog)
