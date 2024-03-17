from audioop import mul
from operator import truediv
from pickle import TRUE
from demo_function import multiply

def test_1():
    n = 4
    kq = multiply(n)
    assert kq == 24

def test_2():
    n = 1
    kq = multiply(n)
    assert kq == 1

def test_3():
    n = 0
    kq = multiply(n)
    assert kq == 1

def test_4():
    n = -1
    try:
        kq = multiply(n)
        assert False

    except ValueError as e:
        assert str(e) == 'No factorial for negative number'