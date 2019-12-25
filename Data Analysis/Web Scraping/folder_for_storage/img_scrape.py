from bs4 import BeautifulSoup
from requests import get
import urllib.request
from PIL import Image
from io import BytesIO
import os

url = 'link here'
response = get(url)
html_soup = BeautifulSoup(response.text, 'html.parser')
# the tag
# and class
data = html_soup.find_all('img', class_ = 'img-back lasyload')

# find the data that you want and pass it to write
for ele in data:
    extracted_link = str(ele).split('"')[-2]
    extracted_file_name = str(ele).split('/')[-2].replace('"','')
    r = get(extracted_link)
    
    i = Image.open(BytesIO(r.content))
    print(extracted_file_name)
    # ./ save in current folder
    # ../ one level above
    i.save(os.path.join('./', extracted_file_name))
    
    