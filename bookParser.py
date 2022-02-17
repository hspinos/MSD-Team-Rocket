

class bookParser:

    def __init__(self):
        #document refers to the html page that is passed from Web.py
        self.document = ""
        #bookList will hold 5 book
        self.bookList = []

    def initList(self):
        for i in range(4):
            self.bookList[i] = initBook(i)

    def initBook(self, index):
        book = Book()
        book.parseBook(index)

        return book


class Book:

    def __init__(self):
        self.title = ""
        self.author = ""
        self.price = ""

    def parseBook(self, index):
        parsedTitle = #parse title from returned web page
        parsedAuthor = #parse author from returned web page
        parsedPrice = #parse price from returned web page

        self.title = parsedTitle
        self.author = parsedAuthor
        self.price = parsedPrice
