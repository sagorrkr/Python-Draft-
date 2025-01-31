from Hello import hello


def test_default():
    assert hello() == "Hello , world"

def test_arguments():
    assert hello("Roy") == "Hello , Roy"
