from bs4 import BeautifulSoup
from json import decoder
import pandas
import requests

output_file = "output.csv"
url = "http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/"
mozilla_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'
#url sample second page http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s=10.html
#based on url_pattern we compound the url for each results page by adding 0, 10, 20 etc and .html end
url_pattern = 'http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s='

r = requests.get(url, headers={'User-agent': mozilla_agent})
html_content = r.content
soup = BeautifulSoup(html_content, "html.parser")
# Search for a anchor elements of Class Page and get the last one from the list 
# the last page number in the list [-1] is the number of result pages  
page_nr = soup.find_all("a",{"class":"Page"})[-1].text
print("There are {} results pages.".format(page_nr))
#print(soup.prettify())
#all = soup.find_all("div",{"class":"propertyRow"})

properties_list = []
for i in range(0, int(page_nr)):
    page_url = url_pattern+str(i*10)+'.html'
    print(i, " " ,page_url)
    
    r = requests.get(page_url, headers={'User-agent': mozilla_agent})
    html_content = r.content
    soup = BeautifulSoup(html_content, "html.parser")

    all = soup.find_all("div",{"class":"propertyRow"})
    for item in all:
        dict = {}
        price = item.find("h4",{"class":"propPrice"})
        property_price = price.text.replace("\n","").replace(" ","")
        dict["Price"] = property_price
        dict["Address"] = item.find_all("span",{"class":"propAddressCollapse"})[0].text
        dict["Locality"] = item.find_all("span",{"class":"propAddressCollapse"})[1].text
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
        properties_list.append(dict)

#print(properties_list)
df = pandas.DataFrame(properties_list)
df.to_csv(output_file, index = False)
print ("The web scrapping output has been exported to the CSV file: {}".format(output_file))

print()

dataframe = pandas.read_csv(output_file, header = 0)
print ("This is how the CSV file, imported into a Pandas dataframe, looks like")
print(dataframe)
print("   {} results found".format(dataframe.shape[0]))