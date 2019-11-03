from bs4 import BeautifulSoup
import pandas
import requests

r = requests.get("http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/", headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})

html_content = r.content

soup = BeautifulSoup(html_content, "html.parser")

#print(soup.prettify())
all = soup.find_all("div",{"class":"propertyRow"})
for item in all:
    price = item.find("h4",{"class":"propPrice"})
    prop_price = price.text.replace("\n","").replace(" ","")
    print(prop_price)
    prop_details = item.find_all("span",{"class":"propAddressCollapse"})[0].text

    print(prop_details)
    try:
        print(item.find("span",{"class":"infoBed"}).find("b").text)
    except:
        print(None)
    print()