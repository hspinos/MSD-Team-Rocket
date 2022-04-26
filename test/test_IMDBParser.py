from rocket.Web import *
from rocket.imdbParser import *

webScraper = Web("sad")

def test_printBookReturnsPrettyTable():
    imdbP = imdbParser(webScraper.imdbUrl())
    assert type(imdbP.printIMDBItem()) == PrettyTable

def test_reduceSoupReturns5SoupElements():
    imdbP = imdbParser(webScraper.imdbUrl())
    imdbP.reduceSoup()
    assert len(imdbP.soupList) == 5

def test_initListCreates5BookObjects():
    imdbP = imdbParser(webScraper.imdbUrl())
    imdbP.reduceSoup()
    imdbP.initIMDBList()
    assert len(imdbP.imdbList) == 5
    for item in imdbP.imdbList:
        assert type(item) == IMDBItem

def test_contentsOfBookListNotNull():
    imdbP = imdbParser(webScraper.imdbUrl())
    imdbP.reduceSoup()
    imdbP.initIMDBList()
    for item in imdbP.imdbList:
        assert item.title is not None
        assert item.rating is not None
        assert item.description is not None