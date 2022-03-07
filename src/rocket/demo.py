from sqlalchemy import table
from Web import *
from bookParser import *

webScraper = Web("Adventurous")
parser = bookParser(webScraper.bookUrl())
parser.reduceSoup()
parser.initList()
parser.printBook()