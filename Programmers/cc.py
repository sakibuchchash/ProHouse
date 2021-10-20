import requests
from bs4 import BeautifulSoup

def CC(title):
        head = "https://wwww.codechef.com/users/"
        var = title
        URL = head + var
        page  = requests.get(URL)
        soup = BeautifulSoup(page.content,'html.parser')

        listRating = list(soup.findAll('div',class_="rating-number"))
        rating = list(listRating[0].children)
        rating = rating[0]
        #print (rating)
        return rating
        """
        listGCR = []  #Global and country ranking.
        listRanking = list(soup.findAll('div',class_="rating-ranks"))
        rankingSoup = listRanking[0] 
        for item in rankingSoup.findAll('a'):
                listGCR.append(item.get_text()) #Extracting the text from all anchor tags
        print ("Global Ranking: "+listGCR[0])
        print ("Country Ranking: "+listGCR[1])
        """

