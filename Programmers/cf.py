import requests
from bs4 import BeautifulSoup


def C(title):
    var = title
    head = 'https://www.codeforces.com/profile/'
    URL = "{0}{1}".format(head,var)
    page = requests.get(URL)
    soup = BeautifulSoup(page.content,'html.parser')
    listRating = list(soup.findAll('div',class_="user-rank"))
    CheckRating = listRating[0].get_text()
    if str(CheckRating) == '\nUnrated \n':
        out = 0
        return out
    else:
        listinfo = list((soup.find('div',class_="info")).findAll('li'))
        string = (listinfo[0].get_text())
        string = string.replace(" ","")
        str1,str2 = string.split('(') 
        str3,str4 = str1.split(':') 
        out = int((str4.strip()))
        print(out)
        return out



















"""import requests
import urllib.request
from bs4 import BeautifulSoup

def C(title):   
    var = title
    head = 'https://www.codeforces.com/profile/'
    #var = "tourist"
    #URL = head + var
    URL = "{0}{1}".format(head,var)
      
    page = requests.get(URL, verify=False, timeout=240)
    soup = BeautifulSoup(page.content,'html.parser')
   
    listRating = list(soup.findAll('div',class_="user-rank"))
    CheckRating = listRating[0].get_text()  #Check for rated or unrated
    if str(CheckRating) == '\nUnrated \n':
        #print('Not rated')
        out = 'unrated'
        return out
    else:
        #print('rated')
        listinfo = list((soup.find('div',class_="info")).findAll('li'))
        string = (listinfo[0].get_text())
        string = string.replace(" ","")
        str1,str2 = string.split('(')   # Well,.. don't judge me
        str3,str4 = str1.split(':') 
        out = int((str4.strip()))
        print(out)
        #return out
        #return render(request, 'registration/profile.html',{'out':out}) 
"""

    
