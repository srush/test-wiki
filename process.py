import requests
import urllib.request
import time
from bs4 import BeautifulSoup

from urllib.request import urlopen
url = 'https://en.wikipedia.org/wiki/Joseph_Duffey'
html = urlopen(url) 
top_soup = BeautifulSoup(html, 'html.parser')


current_header = ""
in_p = False
def navigate(soup):
    global current_header, in_p
    if not hasattr(soup, "contents"):
        return 
    for tag in soup.contents:
        if tag.name == "h2":
            current_header = tag.contents[0].string
            # print(tag.contents[0].string)
            navigate(tag)
        elif tag.name == "p":
            in_p = True
            navigate(tag)
            in_p = False

        elif tag.string and in_p:
            print(tag.string)
            # new_tag = top_soup.new_tag("span")
            # new_tag.attrs["class"] = "tooltiptext"
            # new_tag.string = current_header
            # tag.append(new_tag)
            # tag.string = tag.string
        else:
            navigate(tag)
        
navigate(top_soup)
# print(soup)
