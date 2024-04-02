
from tkinter import *
from tkinter import Listbox as lst
from tkinter import messagebox as msg
from turtle import title

from setuptools import Command
from book import Book
from library import Library

class LibraryGUI():
    def __init__(self):
        try:
            self.library = Library()
        except FileNotFoundError:
            print('File not found')
            exit()
        self.window = self.create_window()
        self.create_widgets()  
        self.load_title()

    
    def create_window(self):
        window = Tk()  
        window.title('Library')
        window.geometry('500x400')
        return window  
        
    def create_widgets(self):
        self.lbl_book = Label(self.window, text='All books')
        self.lbl_book.grid(row=0, column=0)

        self.list_books = lst(self.window, width=50, height=10, exportselection=False)
        self.list_books.grid(row=1, column=0, rowspan=5, sticky=W)
        self.list_books.bind('<<ListboxSelect>>', self.lst_books_clicked)

        self.lbl_id = Label(self.window, text='ID')
        self.lbl_id.grid(row=1, column=2, sticky=E)

        self.txt_id = Entry(self.window)
        self.txt_id.grid(row=1, column=3, columnspan=3, sticky=W)

        self.lbl_title = Label(self.window, text='Title')
        self.lbl_title.grid(row=2, column=2, sticky=E)

        self.txt_title = Entry(self.window)
        self.txt_title.grid(row=2, column=3, columnspan=3, sticky=W)

        self.lbl_author = Label(self.window, text='Author')
        self.lbl_author.grid(row=3, column=2, sticky=E)

        self.txt_author = Entry(self.window)
        self.txt_author.grid(row=3, column=3, columnspan=3, sticky=W)

        self.lbl_price = Label(self.window, text='Price')
        self.lbl_price.grid(row=4, column=2, sticky=E)

        self.txt_price = Entry(self.window)
        self.txt_price.grid(row=4, column=3, columnspan=3, sticky=W)


        self.btn_add = Button(self.window, text='Add', width=5, command=self.add_book)
        self.btn_add.grid(row=5, column=3, sticky=W)

        self.btn_update = Button(self.window, text='Update', width=5, command=self.update_book)
        self.btn_update.grid(row=5, column=4, sticky=W)

        self.btn_delete = Button(self.window, text='Delete', width=5, command=self.delete_book)
        self.btn_delete.grid(row=5, column=5, sticky=W)


    def load_title(self):
        title = self.library.get_title()
        # Clear listbox
        self.list_books.delete(0, END)
        # Insert titles
        for t in title:
            self.list_books.insert(END, t)

    def lst_books_clicked(self, event):
        index = self.list_books.curselection()[0]
        id, title, author, price = self.library.get_book(index)

        self.txt_id.delete(0, END)
        self.txt_id.insert(END, id)

        self.txt_title.delete(0, END)
        self.txt_title.insert(END, title)

        self.txt_author.delete(0, END)
        self.txt_author.insert(END, author)

        self.txt_price.delete(0, END)
        self.txt_price.insert(END, price)

    def add_book(self):
        #get book's info from textboxes
        id = int(self.txt_id.get())
        title = self.txt_title.get()
        author = self.txt_author.get()
        price = float(self.txt_price.get())

        self.library.add_book(id, title, author, price)
        self.list_books.insert(END, title)

        msg.showinfo('Add Book', 'Book added successfully')


    def update_book(self):
        index = self.list_books.curselection()[0]
        title = self.txt_title.get()
        author = self.txt_author.get()
        price = float(self.txt_price.get())
        # Update library
        self.library.update_book(index, title, author, price)
        self.load_title()

        msg.showinfo('Update Book', 'Book updated successfully')

    def delete_book(self):

        index = self.list_books.curselection()[0]
        self.library.delete_book(index)
        self.list_books.delete(index)
        self.load_title()

        msg.showinfo('Delete Book', 'Book deleted successfully')
    
            
    def run(self):
        self.window.mainloop()

program = LibraryGUI()
program.run()
