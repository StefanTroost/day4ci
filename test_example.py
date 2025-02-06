import example as ex

def test_add():
    assert ex.add(1, 2) == 3
    assert ex.add(3, 2) == 5

def test_subtract():
    assert ex.subtract(2, 1) == 1
    assert ex.subtract(2, 3) == -1
