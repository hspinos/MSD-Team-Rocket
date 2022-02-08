from googlesearch import search
import urllib.request
from time import sleep
from bs4 import BeautifulSoup
import requests

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
                webUrls = urllib.request.urlopen(str(self.result[i])).read()
                Soup = BeautifulSoup(webUrls, 'lxml')
                print(Soup.prettify())
            except:
                print(self.result[i])
        
    
if __name__ == "__main__":
    web = Web("books")
    web.url()

