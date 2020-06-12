from bs4 import BeautifulSoup
import requests
import pandas as pd

response = requests.get("https://library.teachyourself.com/id004325062")
soup = BeautifulSoup(response.text, 'html.parser')
results = soup.find_all('section')

print(results)
