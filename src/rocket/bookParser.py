from turtle import title
from Web import *
from prettytable import PrettyTable


class bookParser:

    def __init__(self, Soup):
        self.soup = Soup
        self.table = PrettyTable(["Title", "Author", "Price"])
        self.soupList = []
        self.bookList = []

    def reduceSoup(self):
        self.soupList = self.soup.find_all(class_="product-image-text", limit=5)

    def initList(self):
        for i in range(0, 5):
            self.bookList.append(
                self.initBook(self.soupList[i])
            )

    def initBook(self, soupItem):
        book = Book(soupItem)
        return book

    def printBook(self):
        for i in self.bookList:
            if("$" in i.author):
                i.author = i.author.split("$")[0]
                self.table.add_row([i.title, i.author, i.price])
            else:
                self.table.add_row([i.title, i.author, i.price])
        print(self.table)



class Book:

    def __init__(self, soupItem):
        self.title = soupItem.find_next(class_="item-title").text

        try:
            self.author = soupItem.find_next(style="font-size: 11px;").text
        except:
            self.author = soupItem.find_next(style="min-width: 110px").text

                
        self.price = soupItem.find_next(class_="item-price").text


