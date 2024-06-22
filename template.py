import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re
#from docx import Document

global sitemap
sitemap = """insert your sitemap here"""

def fetch_page(url):
    response = requests.get(url, headers = { 'Accept-Language' : 'en-US,en;q=0.5',
            'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:126.0) Gecko/20100101 Firefox/126.0'})
    return BeautifulSoup(response.text, 'html.parser')

num = 1

with open('blogscraperoutput.txt', 'w') as out:
    for line in sitemap.splitlines():
        date = [int(n) for n in re.findall("\d\d\d\d-\d\d-\d\d", line)[0].split("-")]
        #add a condition here if needed and do as many times as needed
        #if
           #continue

                print(p.text, file=out)

        print(num)
        print('\n\n\n\n\n', file=out)
        num += 1
