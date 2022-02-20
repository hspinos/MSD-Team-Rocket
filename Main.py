from WebScraper import *
from bookParser import *

#create web scraper object with specified URL
webScraperHorror = WebScraper("https://www.booksamillion.com/horrorbooks#")
webScraperMythology = WebScraper("https://www.booksamillion.com/mythology")
webScraperThriller = WebScraper("https://www.booksamillion.com/thrillers")
webScraperRomance = WebScraper("https://www.booksamillion.com/romance")

#create book parser with Soup object returned from web scraper
bookParser = bookParser(webScraperRomance.getHTML())
bookParser.reduceSoup()
bookParser.initList()
for i in bookParser.bookList:
    print(i.title + "\n")
    print(i.author + "\n")
    print(i.price + "\n")

