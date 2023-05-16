from seasons import convert


def test_date():
    assert convert(365) == "Five hundred twenty-five thousand, six hundred minutes"
