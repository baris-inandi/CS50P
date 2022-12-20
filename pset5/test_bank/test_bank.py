from bank import value


def test_value():
    assert value("hello, sir") == 0
    assert value("HELLO!!!!") == 0
    assert value("hello") == 0
    assert value("hey") == 20
    assert value("hi") == 20
    assert value("what?") == 100
