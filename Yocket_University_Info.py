#from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import re
import urllib.request

user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
ur = "https://yocket.in/universities/reviews/"
filename= "citynew.csv" #filename
f=open(filename, "w")
header= "UniversityCity, TypeOfUniversity, UniversityExpense , MaxTemp, MinTemp, UniversityName, \n"
f.write(header)
#s will traverse through all the webpages and extract the information
for s in (799 , 2587 , 2647 , 707 , 781 , 713 , 1101 , 702 , 2706 , 2716 , 861):
        #feel free to include below numbers in the above for loop and see the magic happen
         # 2652 , 745 , 782 , 2649 , 809 , 1480 , 703 , 2594 , 2632 , 2601 , 1094 , 
         #2566 , 794 , 808 , 1856 , 706 , 752 , 710 , 711 , 868 , 2638 , 701 , 795 ,
         # 712 , 2573 , 1813 , 748 , 704 , 801 , 763 , 802 , 737 , 2814 , 2577 , 2574 , 
         #801 , 704 , 814 , 763 , 802 , 864 , 709 , 2657 , 702 , 713 , 1813 , 1094 ,
         #712 , 703 , 2573 , 2587 , 745 , 711 , 2800 , 737 , 729 , 861 , 2566
    url=ur + str(s)
    headers={'User-Agent':user_agent,} 

    request=urllib.request.Request(url,None,headers) #The assembled request
    response = urllib.request.urlopen(request)
    data = response.read() # The data u need
    
    page_soup = soup(data,"lxml")
    #Extract information about the location of university
    UniversityCity = page_soup.findAll("div",{"class":"col-sm-11 col-sm-offset-1"})
    UniversityCity=str(re.sub(", United States",'', UniversityCity[0].h4.text ))
    print(UniversityCity)
    #Extract the name of university
    UniversityName=page_soup.h1.text
    print(UniversityName)
    #Extract the temperature information of the location from a HTML table
    temperature = page_soup.findAll("table",{"class":"table"})
    temp =temperature[0]
    temptable = temp.find_all('h3')
    temptable[0].small.decompose()
    temptable[0]=float(temptable[0].text.strip())
    temptable[1].small.decompose()
    temptable[1]=float(temptable[1].text.strip())
    temptable[2].small.decompose()
    temptable[2]=float(temptable[2].text.strip())
    temptable[3].small.decompose()
    temptable[3]=float(temptable[3].text.strip())
    MaxTemp=max(temptable)
    MinTemp=min(temptable)
    print(MaxTemp)
    print(MinTemp)
    #Extract the infromation about the type of university(Public or Private)
    containers = page_soup.findAll("div",{"class":"col-sm-3 col-xs-6"})
    TypeOfUniversity=containers[0]
    TypeOfUniversity.small.decompose()
    TypeOfUniversity= TypeOfUniversity.text.strip()
    print(TypeOfUniversity)
    #Extract the average expenses of all the programs in the universities
    uExpense=containers[3]
    uExpense.h2.small.decompose()
    uExpense.h2.small.decompose()
    inputTag=uExpense.h2.text.strip()
    UnivExpense = int(re.sub('\W+','', inputTag ))
    print(UnivExpense)
    #write the above information of each university into a csv file
    f.write(UniversityCity+ "," + TypeOfUniversity + "," + str(UnivExpense) + "," + str(MaxTemp) +"," + str(MinTemp) +","+ UniversityName.replace(",", "") + "\n")
f.close()