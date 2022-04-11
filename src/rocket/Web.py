from bs4 import BeautifulSoup
import logging
import requests

'''
pip install google
pip install beautifulsoup4
pip install requests
'''

class Web:
    def __init__(self, keyword):
        self.keyword = keyword.lower()
        self.listForBooks = {"adventurous" : "https://www.booksamillion.com/summer-reading2?oxid=1162&oxname=summereadinglist&oxpage=summeradventure&oxpos=module2&oxdate=050621",
                             "happy" : "https://www.booksamillion.com/50bookstoreadbefore5",
                             "sad" : "https://www.booksamillion.com/personalgrowth?oxid=1777&oxname=personalgrowth&oxpage=consciousliving&oxpos=module3&oxdate=121420",
                             "love" : "https://www.booksamillion.com/romance",
                             "sci-Fi" : "https://www.booksamillion.com/scifi"}

    def bookUrl(self):
        try:
            webUrls = requests.get(self.listForBooks[self.keyword]).text
            Soup = BeautifulSoup(webUrls, 'lxml')
            return(Soup)

        except Exception as e:
            print(e)
        
if __name__ == "__main__":
    web = Web("sad")
    web.bookUrl()

