from library_item import LibraryItem
from video_library import library

# Create LibraryItem
def test_1():
    item = LibraryItem("The Godfather", "Francis Ford Coppola", 5)
    assert item.name == "The Godfather"
    assert item.director == "Francis Ford Coppola"
    assert item.rating == 5
    assert item.play_count == 0
# Call info() method
def test_2():
    item = LibraryItem("The Godfather", "Francis Ford Coppola", 5)
    assert item.info() == "The Godfather - Francis Ford Coppola *****"
# Call stars() method
def test_3():
    item = LibraryItem("The Godfather", "Francis Ford Coppola", 5)
    assert item.stars() == "*****"
# Test for empty name
def test_4():
    try:
        item = LibraryItem("", "Francis Ford Coppola", 5)
        assert False
    except ValueError as e:
        assert str(e) == "Name cannot be empty"

# Test for empty director
def test_5():
    try:
        item = LibraryItem("The Godfather", "", 5)
        assert False
    except ValueError as e:
        assert str(e) == "Director can not be empty"
# Test for rating not an integer
def test_6():
    try:
        item = LibraryItem("The Godfather", "Francis Ford Coppola", "hello")
        assert False
    except ValueError as e:
        assert str(e) == "Rating must be an integer"