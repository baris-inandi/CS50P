from plates import is_valid


def test_alphanumeric():
    # all alphanumeric
    assert is_valid("CS50") == True
    assert is_valid("||50") == False
    assert is_valid("CS") == True
    assert is_valid("C5") == False
    assert is_valid("2C") == False
    assert is_valid("50") == False
    assert is_valid(" 5") == False
    assert is_valid("C!") == False
    assert is_valid("!C") == False
    assert is_valid("!?!?!") == False
    assert is_valid("$$") == False
    assert is_valid("CS50!") == False


def test_lengths():
    # length between 2 and 6
    assert is_valid("NAMAST3") == False
    assert is_valid("P") == False
    assert is_valid("LWYRUP") == True
    assert is_valid("CS") == True


def test_first_two():
    # first two chars should be letters
    assert is_valid("50CS") == False
    assert is_valid("5CS") == False


def test_first():
    # first number shouldn't be 0
    assert is_valid("CS050") == False


def test_last():
    # should end with numbers or have no numbers at all
    assert is_valid("CS50P") == False
    assert is_valid("CPSC") == True
