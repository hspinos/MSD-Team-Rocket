
def test_reduceSoupProducesFiveElements(bpFixture):
    assert len(bpFixture.soupList) is 0
    bpFixture.reduceSoup()
    assert len(bpFixture.soupList) is 5

def test_initListCallsInitBook(bpFixture):
    bpFixture.initList()
    assert len(bpFixture.bookList) is 5

def test_printBook(bpFixture, capsys):
    bpFixture.printBook()
    captured = capsys.readouterr()
    assert captured.out != ""