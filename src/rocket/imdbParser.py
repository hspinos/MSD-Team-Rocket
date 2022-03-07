

class imdbParser:

    def __init__(self, Soup):
        self.soup = Soup
        self.soupList = []
        self.imdbList = []

    def reduceSoup(self):
        self.soupList = self.soup.find_all(class_="lister-item-content", limit=5)

    def initIMDBList(self):
        for i in range(0, 5):
            self.imdbList.append(
                self.initIMDBItem(self.soupList[i])
            )

    def initIMDBItem(self, soupItem):
        imdbItem = IMDBItem()
        imdbItem.parseIMDB(soupItem)

        return imdbItem

class IMDBItem:

    def __init__(self):
        self.title = "Title: "
        self.rating = "Rating: "
        self.description = "Description: "
        self.star = "Star: "


    #TODO finish parsing logic
    def parseIMDB(self, soupItem):
        parsedTitle = soupItem.find_next()
        parsedRating = soupItem.find_next()
        parsedDescription = soupItem.find_next()
        parsedStar = soupItem.find_next()

        self.title = parsedTitle
        self.rating = parsedRating
        self.description = parsedDescription
        self.star = parsedStar

