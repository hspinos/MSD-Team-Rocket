
class bookParser:

    def __init__(self, Soup):
        self.soup = Soup
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
        book = Book()
        book.parseBook(soupItem)

        return book


class Book:

    def __init__(self):
        self.title = ""
        self.author = ""
        self.price = ""

    def parseBook(self, soupItem):
        authorMarker = soupItem.find(class_="item-title")
        parsedTitle = soupItem.find_next(class_="item-title").text
        parsedAuthor = authorMarker.find_next(style="font-size: 11px;").text
        parsedPrice = soupItem.find_next(class_="item-price").text

        self.title = parsedTitle
        self.author = parsedAuthor
        self.price = parsedPrice
        

