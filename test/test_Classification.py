from rocket.classification import *

classifier = keyword()

def test_emotionArraysArePopulated():
    assert len(classifier.sad) > 1
    assert len(classifier.happy) > 1
    assert len(classifier.fear) > 1
    assert len(classifier.disgust) > 1
    assert len(classifier.anger) > 1
    assert len(classifier.surprise) > 1
    assert len(classifier.adventurous) == 1

def test_detectFoundMatchInput():
    classifier.input = "sad"
    result = classifier.compareInput()
    assert result == "sad"

def test_detectNoFoundMatchInput():
    classifier.input = "beaver"
    result = classifier.compareInput()
    assert result is None

