from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import re
import urllib.request
import requests
import unicodedata
from unicodedata import category
#url = 'https://www.usnews.com/best-graduate-schools/top-business-schools/mba-rankings'
#url = 'https://www.usnews.com/best-graduate-schools/top-business-schools/information-systems-rankings'
#url = 'https://www.usnews.com/best-graduate-schools/top-business-schools/mba-rankings'
#url = 'https://www.usnews.com/best-graduate-schools/top-business-schools/mba-rankings/page+2'
#url = 'https://www.usnews.com/best-graduate-schools/top-business-schools/accounting-rankings'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
result = requests.get(url, headers=headers)
data=result.content.decode()
page_soup = soup(data,"lxml")
#University rank is scraped
University_rank = page_soup.findAll("span",{"class":"rankscore-bronze"})
#University name is scraped
Name_University = page_soup.findAll("a",{"class":"school-name"})
#University location is scraped
University_location = page_soup.findAll("p",{"class":"location"})

filename= "msbalatest1.csv"
f=open(filename, "w")
headers= "Rank, UniversityName, UniversityLocation \n"
f.write(headers)
def remove_control_characters(s):
    return "".join(ch for ch in s if unicodedata.category(ch)[0]!="C")
Name_Universitynew=[11]
for a in range(0,11):
    #Formatting the text
    University_rank[a]=str(re.sub('[a-z,A-Z,\#]','', University_rank[a].text))
    Name_University[a]=Name_University[a].text
    Name_University[a]=str(remove_control_characters(Name_University[a]))
    Name_University[a]=str(re.sub('\(([A-Za-z0-9_]+)\)','', Name_University[a]))
    Name_University[a]=str(re.sub('\â€”',' ', Name_University[a]))
    Name_University[a]=str(re.sub('\—',' ', Name_University[a]))
    University_location[a]=str(University_location[a].text)
    f.write(University_rank[a] + "," + Name_University[a] + "," + University_location[a].replace(",", "") + "\n")
f.close()
print(University_rank)
print(Name_University)
print(University_location)