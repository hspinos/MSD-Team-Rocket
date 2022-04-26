from rocket.Web import *
from rocket.bookParser import *

webScraper = Web("sad")

def test_printBookReturnsPrettyTable():
    bp = bookParser(webScraper.bookUrl())
    assert type(bp.printBook()) == PrettyTable

def test_reduceSoupReturns5SoupElements():
    bp = bookParser(webScraper.bookUrl())
    bp.reduceSoup()
    assert len(bp.soupList) == 5

def test_initListCreates5BookObjects():
    bp = bookParser(webScraper.bookUrl())
    bp.reduceSoup()
    bp.initList()
    assert len(bp.bookList) == 5
    for book in bp.bookList:
        assert type(book) == Book

def test_contentsOfBookListNotNull():
    bp = bookParser(webScraper.bookUrl())
    bp.reduceSoup()
    bp.initList()
    for book in bp.bookList:
        assert book.title is not None
        assert book.author is not None
        assert book.price is not None