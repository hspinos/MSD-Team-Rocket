
from bs4 import BeautifulSoup

class bookParser:

    def __init__(self, Soup):
        #soup object being passed in from web scraper
        self.soup = Soup
        #the broken down soup objects
        self.soupList = []
        #bookList will hold 5 books
        self.bookList = []

    def reduceSoup(self):
        #for i in range (1, 1):
            bookIdTag = "splide01-splide01" #+ i
            
            #debug print
            print(bookIdTag)
            #debug print

            self.soupList.append(self.soup.find(id=bookIdTag))

    def initList(self):
        #for i in range(1, 1):
            self.bookList.append(self.initBook(self.soupList[0]))

    def initBook(self, soupItem):
        book = Book()
        book.parseBook(soupItem)

        return book


class Book:

    def __init__(self):
        self.title = ""
        self.author = ""
        self.price = ""

    def parseBook(self, soupItem):
        #authorMarker = soupItem.find_next(class_="item-title")
        parsedTitle = soupItem.find_next(class_="item-title").text
        #parsedAuthor = authorMarker.next_element().text
        parsedPrice = soupItem.find_next(class_="item-price").text

        self.title = parsedTitle
        self.author = parsedAuthor
        self.price = parsedPrice
        

