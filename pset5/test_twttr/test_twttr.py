from twttr import shorten


def test_shorten():
    assert shorten("twitter") == "twttr"
    assert shorten("testing my twitter") == "tstng my twttr"
    assert shorten("TESTING MY TWITTER") == "TSTNG MY TWTTR"
    assert shorten("two 2") == "tw 2"
    assert shorten("punc .") == "pnc ."
