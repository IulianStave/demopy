# parse the source code of a html file
# and filter the content and show the paragraphs or div elements 
# adding a header to the requests.get() method allows the script to impersonate a browser

import requests
from bs4 import BeautifulSoup

r = requests.get("http://www.pyclass.com/example.html",
headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})


htmlcont = r.content
#print("The source code is \n %s"%c)

soup = BeautifulSoup(htmlcont,"html.parser")
# view the source code with prettify
#print (soup.prettify())

all = soup.find_all("div",{"class":"cities"})
#print (all)
for item in all:
        print(item.find_all("p")[0].text)