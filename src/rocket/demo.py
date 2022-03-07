from src.rocket.Web import *
from src.rocket.bookParser import *

webScraper = Web("Love")
parser = bookParser(webScraper.bookUrl())
parser.reduceSoup()
parser.initList()

for i in parser.bookList:
    print(i.title + "\n")
    print(i.author + "\n")
    print(i.price + "\n")