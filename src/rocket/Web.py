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
                             "Happy" : "https://www.booksamillion.com/50bookstoreadbefore5",
                             "Sad" : "https://www.booksamillion.com/personalgrowth?oxid=1777&oxname=personalgrowth&oxpage=consciousliving&oxpos=module3&oxdate=121420",
                             "Love" : "https://www.booksamillion.com/romance",
                             "Sci-Fi" : "https://www.booksamillion.com/scifi"}

    def bookUrl(self):
        try:
            list_ = []
            webUrls = requests.get(self.listForBooks[self.keyword]).text
            Soup = BeautifulSoup(webUrls, 'lxml')
            #print(self.listForBooks[self.keyword], "\n")
            #title = Soup.findAll("span", class_="js-subbuzz__title-text")[1].text
            #print(title)

            '''for i in range(1,6):
                list_.append(title[i].findAll("a"))
                
            for i in range(len(list_)):
                print(list_[i][0].text, "\n")

            for i in range(1,6):
                print(title[i].text)'''

            #print(list_)
            return(Soup)

        except Exception as e:
            print(e)
        
if __name__ == "__main__":
    web = Web("Sad")
    web.bookUrl()

