import pytest
from jar import Jar


def test_init():
    jar = Jar(capacity=10)
    assert jar.capacity == 10
    assert jar.size == 0


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(2)
    assert str(jar) == "🍪🍪"
    jar.deposit(4)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪"
    jar.withdraw(2)
    assert str(jar) == "🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(2)
    jar.deposit(3)
    assert jar.size == 5
    with pytest.raises(ValueError):
        jar.deposit(9999)


def test_withdraw():
    jar = Jar()
    jar.deposit(10)
    jar.withdraw(1)
    jar.withdraw(1)
    assert jar.size == 8
    with pytest.raises(ValueError):
        jar.withdraw(9999)
