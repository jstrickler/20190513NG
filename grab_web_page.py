#!/usr/bin/env python
import requests
import bs4


NG_URL = "https://www.nationalgridus.com/RI-Home/Default"

response = requests.get(NG_URL)

if response.status_code == requests.codes.OK:
    content = response.content.decode()

    soup = bs4.BeautifulSoup(content, 'lxml')

    for input_tag in soup.findAll('a'):
        url = input_tag.get('href')
        if 'http' in url:
           print(input_tag.text)
           print(url)
           print('=' * 10)


