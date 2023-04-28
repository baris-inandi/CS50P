from um import count


def test_input():
    assert count("um") == 1
    assert count("UM!") == 1
    assert count("Um, no") == 1
    assert count("Um, yeess, um..") == 2
    assert count("Cogito, ergo sum") == 0
