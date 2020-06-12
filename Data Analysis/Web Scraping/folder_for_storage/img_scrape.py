from bs4 import BeautifulSoup
from requests import get
from PIL import Image
from io import BytesIO
import os


def img(url):
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    # the tag
    # and class
    data = html_soup.find_all('img', class_='img-back lasyload')

    # find the data that you want and pass it to write
    for ele in data:
        extracted_link = str(ele).split('"')[-2]
        extracted_file_name = str(ele).split('/')[-2].replace('"', '')
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


def img_f(url):
    response = get(url)
    html_soup = BeautifulSoup(response.content, 'html5lib')
    print(html_soup)
    # the tag
    # and class
    data = html_soup.find_all('div', class_='thumb_square')
    print(data[:500])

    # find the data that you want and pass it to write
    for ele in data:
        extracted_link = str(ele).split('"')[-2]
        extracted_file_name = str(ele).split('/')[-2].replace('"', '')
        print(extracted_link)
        print(extracted_file_name)
        break
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


img_f("link here")
