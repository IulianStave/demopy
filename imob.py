from bs4 import BeautifulSoup
import pandas
import requests

r = requests.get("http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/", headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})

html_content = r.content

soup = BeautifulSoup(html_content, "html.parser")

#print(soup.prettify())
all = soup.find_all("div",{"class":"propertyRow"})
prop_list = []
for item in all:
    dict = {}
    price = item.find("h4",{"class":"propPrice"})
    prop_price = price.text.replace("\n","").replace(" ","")
    dict["Price"]=prop_price
    dict["Address"] = item.find_all("span",{"class":"propAddressCollapse"})[0].text
    dict["Locality"] = item.find_all("span",{"class":"propAddressCollapse"})[1].text
    #print(prop_details)
    try:
        dict["Beds"] = item.find("span",{"class":"infoBed"}).find("b").text
    except:
        dict["Beds"] = None
    for column_group in item.find_all("div",{"class":"columnGroup"}):
        for feature_group, feature_name in zip(
            column_group.find_all("span",{"class":"featureGroup"}),column_group.find_all("span",{"class":"featureName"})):
            #print (feature_group.text, feature_name.text)
            if "Lot size" in feature_group.text:
                dict["Lot size"] = feature_name.text

    
    #print()
    prop_list.append(dict)

#print(prop_list)
df = pandas.DataFrame(prop_list)
df.to_csv("Prop.csv")