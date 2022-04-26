from rocket.Web import *

webScraper = Web("SAD")

def test_bookUrlReturnsTypeSoup():
    assert type(webScraper.bookUrl()) == BeautifulSoup

def test_imdbUrlReturnsTypeSoup():
    assert type(webScraper.imdbUrl()) == BeautifulSoup

def test_passedInKeywordIsSetToLowerCase():
    assert webScraper.keyword == "sad"
