from WebScraper import *
from bookParser import *
from Web import *

eliza = Eliza()

keyword = KeyWord(Eliza.getReply())
web = Web(keyword.getSyn())
bp = bookParser(Web.bookUrl())

prettyTable.print(bp.bookList)

for i in bookParser.bookList:
    print(i.title + "\n")
    print(i.author + "\n")
    print(i.price + "\n")



