import pytest

from rocket.Web import Web
from rocket.bookParser import bookParser

@pytest.fixture(scope="module")
def webScraperFixtureCorrect():
    return Web("Love")

@pytest.fixture(scope="module")
def webScraperFixtureIncorrect():
    return Web("Wrong")

@pytest.fixture(scope="module")
def bpFixture(webScraperFixtureCorrect):
    return bookParser(webScraperFixtureCorrect.bookUrl())
