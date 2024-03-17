from demo_function import add

def test_add_1():
    a = 4
    b = 0
    c = add(a,b)
    assert c == 4  #Expected output


def test_add_2():
    a = 0
    b = 0
    c = add(a,b)
    assert c == 0

def test_add_3():
    a = 0
    b = 4
    c = add(a, b)
    assert c == 4
    