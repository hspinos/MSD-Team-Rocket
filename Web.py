from ast import keyword
from googlesearch import search
from time import sleep
from bs4 import BeautifulSoup
import requests

'''
pip install google
pip install beautifulsoup4
pip install requests
'''

class Web:

    def __init__(self, keyword):
        self.keyword = keyword
        self.listForBooks = {"Adventurous" : "https://www.booksamillion.com/summer-reading2?oxid=1162&oxname=summereadinglist&oxpage=summeradventure&oxpos=module2&oxdate=050621",
                             "Happy" : "https://www.booksamillion.com/search?filter=book_categories%3ASEL-016-000%7Cdate%3Apast_90%7Cavailable_in_stores%3Atrue",
                             "Sad" : "https://www.booksamillion.com/search?filter=book_categories%3ASEL-011-000%7Cavailable_in_stores%3Atrue",
                             "Love" : "https://www.booksamillion.com/romance5?oxid=1487&oxname=favromance&oxpage=romance&oxpos=module5&oxdate=012920"}

    def bookUrl(self):
        try:
            webUrls = requests.get(self.listForBooks[self.keyword]).text
            Soup = BeautifulSoup(webUrls, 'lxml')
            print(self.listForBooks[self.keyword], "\n")
            return(Soup)

        except Exception as e:
            print(e)
        
if __name__ == "__main__":
    web = Web("Adventurous")
    web.bookUrl()

