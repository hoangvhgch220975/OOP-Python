
from requests import delete
from book import Book
import csv

class Library:
    def __init__(self):
        self.__books = self.load_books('books.csv')

    def load_books(self, file_name):
        books =[]
        with open(file_name, 'r') as f:
            reader = csv.reader(f)
            # skip header
            next(reader)
            # scan each raw
            for row in reader:
                id = int(row[0])
                title = row[1]
                author = row[2]
                price = float(row[3])
                b = Book(id, title, author, price)
                books.append(b)
        return books
    
    def get_title(self):
        return (b.title for b in self.__books)
    
    def get_book(self, index):
        # return self.__books[index] => not safe, expose books info outside
        b = self.__books[index] 
        # safe because we return a copy of book's info
        return b.id, b.title, b.author, b.price
    
    def add_book(self, id, title, author, price):
        self.__books.append(Book(id, title, author, price))
    
    def update_book(self, index, title, author, price):
        b= self.__books[index]
        b.title = title
        b.author = author
        b.price = price

    def delete_book(self, index):
        del self.__books[index]

