from bs4 import BeautifulSoup
from requests import get
from PIL import Image
from io import BytesIO
import os


def educate_plus(url):
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    data = html_soup.find_all('a', class_ = 'odd')
    
    
    return data

print(educate_plus('https://educateplus.ie/markingscheme/junior-cert-german-higher-level'))


def img(url):
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    data = html_soup.find_all('a', class_ = 'image-list-link')
    
    # find the data that you want and pass it to write
    for ele in data:
        extracted_link = "https:" + str(ele).split('"')[-2]
        extracted_file_name = str(extracted_link).split('/')[-1]
        r = get(extracted_link)
        if r.status_code == 200:
            try:
                i = Image.open(BytesIO(r.content))
                print("[*] Downloaded " + extracted_file_name)
                # ./ save in current folder
                # ../ one level above
                i.save(os.path.join('./', extracted_file_name))
            except Exception as e:
                print(e)
        else:
            print("Error with get request")
            
