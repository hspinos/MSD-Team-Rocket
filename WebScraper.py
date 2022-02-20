from bs4 import BeautifulSoup
import requests

class WebScraper:

    def __init__(self, pageUrl):
        self.pageUrl = pageUrl

    def getHTML(self):
        try:
            webUrl = requests.get(self.pageUrl).text
            Soup = BeautifulSoup(webUrl, 'lxml')
            
            return(Soup)

        except Exception as e:
            print(e)

