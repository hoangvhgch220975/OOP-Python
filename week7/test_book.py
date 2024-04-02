from book import Book

def test_book1():
    b = Book(1, 'Python', 'Doan Trung Tung', 100.0)
    assert b.id == 1
    assert b.title == 'Python'
    assert b.author == 'Doan Trung Tung'
    assert b.price == 100.0

def test_book2():
    try:
        b = Book(1,'','Doan Trung Tung',100.0)
        assert False
    except ValueError as e:
        assert str(e) == 'Title cannot be empty'