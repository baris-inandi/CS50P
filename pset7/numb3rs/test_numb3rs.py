from numb3rs import validate


def test_ipranges():
    assert validate("cs50") == False
    assert validate("192.168.1.2") == True
    assert validate("255.255.255.255") == True
    assert validate("192.333.333.333") == False
    assert validate("0.0.0.0") == True
    assert validate("192.168") == False
    assert validate("192.168.1") == False
    assert validate("192.168.1.1.1") == False
    assert validate("10000000.0.0") == False
    assert validate("256") == False
    assert validate("255") == False
