from rocket.Web import *

def test_CorrectKeywordAssignment(webScraperFixtureCorrect):
    assert webScraperFixtureCorrect.keyword == "Love"

def test_bookUrlReturnsSoupObject(webScraperFixtureCorrect):
    assert type(webScraperFixtureCorrect.bookUrl()) is BeautifulSoup

def test_bookUrlThrowsErrorOnIncorrectKeyword(webScraperFixtureIncorrect, capsys):
    webScraperFixtureIncorrect.bookUrl()
    captured = capsys.readouterr()
    assert captured.out == "'Wrong'\n"
