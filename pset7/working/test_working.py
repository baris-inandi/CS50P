import pytest
from working import convert


def test_convert():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("11:30 PM to 9:50 AM") == "23:30 to 09:50"
    assert convert("11 PM to 9 AM") == "23:00 to 09:00"
    assert convert("9 AM to 5:50 PM") == "09:00 to 17:50"


def test_value_error():
    with pytest.raises(ValueError):
        convert("9AM - 5PM")
    with pytest.raises(ValueError):
        convert("99:00 AM to 30:00 PM")
    with pytest.raises(ValueError):
        convert("9:99 AM to 5:99 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM to 5:00 PM to 8:00 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM to 17:00")
