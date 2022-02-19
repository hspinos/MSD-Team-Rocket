from googlesearch import search
from time import sleep
import urllib.request
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
        self.result = []
        self.headingTags = ['h1', 'h2', 'h3']

    def topSearches(self):
        query = self.keyword
        for j in search(query, tld="co.in", stop=1):
            self.result.append(j)

    def url(self):
        self.topSearches()
        for i in range(len(self.result)):
            try:
                webUrls = requests.get(self.result[i]).text
                Soup = BeautifulSoup(webUrls, 'lxml')
                print(self.result[i] + "\n")
                return(Soup)

            except Exception as e:
                print(e)
        
if __name__ == "__main__":
    web = Web("books")
    print(str(web.url().title.text))

