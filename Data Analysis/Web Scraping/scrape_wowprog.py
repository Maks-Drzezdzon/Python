import requests
from bs4 import BeautifulSoup

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

team_names = []
team_realm = []
current_prog = []

team={}
#print(name, realm, current_raid, prog)
for ele in names:
    for name in ele:
        #print (name)
        team_names.append(name)
        
for ele in realms:
    for realm in ele:
        #print (realm)
        team_realm.append(realm)   
        
for ele in prog:
    # full class
    for proggress in ele:
        # prog with tags
        for i in proggress:   
            # prog without tags
            print (i)
            current_prog.append(i)


for ele in team_names,team_realm,current_prog:
    print(team_names[0],team_realm[0],current_prog[0])