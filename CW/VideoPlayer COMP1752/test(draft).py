import tkinter as tk
from tkinter import simpledialog

class LibraryItem:
    def __init__(self, title, director, rating):
        self.title = title
        self.director = director
        self.rating = rating

class LibraryGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Library Management System")

        self.library = {}
        self.library["01"] = LibraryItem("Tom and Jerry", "Fred Quimby", 4)
        self.library["02"] = LibraryItem("Breakfast at Tiffany's", "Blake Edwards", 5)
        self.library["03"] = LibraryItem("Casablanca", "Michael Curtiz", 2)
        self.library["04"] = LibraryItem("The Sound of Music", "Robert Wise", 1)
        self.library["05"] = LibraryItem("Gone with the Wind", "Victor Fleming", 3)

        self.listbox = tk.Listbox(self.master, width=50)
        self.listbox.pack(padx=10, pady=10)
        self.update_listbox()

        add_button = tk.Button(self.master, text="Add", command=self.add_item)
        add_button.pack(side=tk.LEFT, padx=5)

        edit_button = tk.Button(self.master, text="Edit", command=self.edit_item)
        edit_button.pack(side=tk.LEFT, padx=5)

        delete_button = tk.Button(self.master, text="Delete", command=self.delete_item)
        delete_button.pack(side=tk.LEFT, padx=5)

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for key in self.library:
            item = self.library[key]
            self.listbox.insert(tk.END, f"{key}: {item.title} by {item.director} (rating: {item.rating})")

    def add_item(self):
        title = simpledialog.askstring("Add Item", "Enter title:")
        if title:
            director = simpledialog.askstring("Add Item", "Enter director:")
            if director:
                rating = simpledialog.askinteger("Add Item", "Enter rating:", initialvalue=0)
                if rating is not None:
                    key = self.generate_key()
                    self.library[key] = LibraryItem(title, director, rating)
                    self.update_listbox()

    def edit_item(self):
        index = self.listbox.curselection()
        if index:
            key = self.listbox.get(index)[0:2]
            item = self.library[key]
            title = simpledialog.askstring("Edit Item", "Enter title:", initialvalue=item.title)
            if title:
                director = simpledialog.askstring("Edit Item", "Enter director:", initialvalue=item.director)
                if director:
                    rating = simpledialog.askinteger("Edit Item", "Enter rating:", initialvalue=item.rating)
                    if rating is not None:
                        self.library[key] = LibraryItem(title, director, rating)
                        self.update_listbox()

    def delete_item(self):
        index = self.listbox.curselection()
        if index:
            key = self.listbox.get(index)[0:2]
            del self.library[key]
            self.update_listbox()

    def generate_key(self):
        keys = [int(k) for k in self.library.keys()]
        new_key = max(keys) + 1 if keys else 1
        return f"{new_key:02d}"

def main():
    root = tk.Tk()
    app = LibraryGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
