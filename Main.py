from WebScraper import *
from bookParser import *

#create web scraper object with specified URL
webScraper = WebScraper("https://www.booksamillion.com/horrorbooks#")

#create book parser with Soup object returned from web scraper
bookParser = bookParser(webScraper.getHTML())
bookParser.reduceSoup()
bookParser.initList()
for i in bookParser.bookList:
    print(i.title + "\n")
    print(i.author + "\n")
    print(i.price + "\n")

