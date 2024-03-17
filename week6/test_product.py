from itertools import product
from product import Product

def test_product_init():
    p = Product('apple', 10,2)
    assert p.name == 'apple'
    assert p.price == 10
    assert p.quantity == 2


def test_product_name_setter01():
    p = Product('apple',10,2)
    p.name = 'banana'
    assert p.name == 'banana'

def test_product_price_setter01():
    p = Product('apple',10,2)
    p.price = 20
    assert p.price == 20

def test_product_quantity_setter01():
    p = Product('apple',10,2)
    p.quantity = 10
    assert p.quantity == 10

def test_product_name_setter02():
    p = Product('apple',10,2)
    try:
        p.name =""
        assert False
    except ValueError as e:
        assert str(e) == 'Name cannot be empty'


def test_product_price_setter02():
    p = Product('apple',10,2)
    try:
        if p.price < 0:
            assert False
    except ValueError as e:
        assert str(e) == 'Price cannot be negative'



def test_product_quantity_setter02():
    p = Product('apple',10,2)
    try:
        if p.quantity < 0:
            assert False
    except ValueError as e:
        assert str(e) == 'Quantity cannot be negative'


def test_product_show(capsys):
    p = Product('apple', 10, 2)
    p.show()
    captured = capsys.readouterr()
    assert captured.out == "Name: apple | price: $10 | quantity: 2\n"