from tkinter import *
from tkinter import messagebox as msg
from tkinter import Listbox as lst
from tkinter import filedialog as fd

from sport_item import SportItem
from sport_store import Store

class StoreGUI:
    def __init__(self):
        try:
            self.store = Store()
        except FileNotFoundError:
            print('File not found')
            exit()
        self.window = self.create_window()
        self.create_widgets()
        self.load_name()

    def create_window(self):
        window = Tk()
        window.title('Store')
        window.geometry('500x400')
        return window
    
    def create_widgets(self):
        self.lbl_item = Label(self.window, text='All items')
        self.lbl_item.grid(row=0, column=0)

        self.list_items = lst(self.window, width=50, height=10, exportselection=False)
        self.list_items.grid(row=1, column=0, rowspan=5, sticky=W)
        self.list_items.bind('<<ListboxSelect>>', self.lst_items_clicked)

        self.lbl_id = Label(self.window, text='ID')
        self.lbl_id.grid(row=1, column=2, sticky=E)

        self.txt_id = Entry(self.window)
        self.txt_id.grid(row=1, column=3, columnspan=3, sticky=W)

        self.lbl_name = Label(self.window, text='Name')
        self.lbl_name.grid(row=2, column=2, sticky=E)

        self.txt_name = Entry(self.window)
        self.txt_name.grid(row=2, column=3, columnspan=3, sticky=W)

        self.lbl_brand = Label(self.window, text='Brand')
        self.lbl_brand.grid(row=3, column=2, sticky=E)

        self.txt_brand = Entry(self.window)
        self.txt_brand.grid(row=3, column=3, columnspan=3, sticky=W)

        self.lbl_price = Label(self.window, text='Price')
        self.lbl_price.grid(row=4, column=2, sticky=E)

        self.txt_price = Entry(self.window)
        self.txt_price.grid(row=4, column=3, columnspan=3, sticky=W)

        self.btn_add = Button(self.window, text='Add', command=self.btn_add_clicked)
        self.btn_add.grid(row=5, column=2, sticky=E)

        self.btn_update = Button(self.window, text='Update', command=self.btn_update_clicked)
        self.btn_update.grid(row=5, column=3, sticky=E)

        self.btn_delete = Button(self.window, text='Delete', command=self.btn_delete_clicked)
        self.btn_delete.grid(row=5, column=4, sticky=E)

        self.btn_load = Button(self.window, text='Load', command=self.btn_load_clicked)
        self.btn_load.grid(row=6, column=2, sticky=E)  # New button for loading

        self.btn_save = Button(self.window, text='Save', command=self.btn_save_clicked)
        self.btn_save.grid(row=6, column=3, sticky=E)  # New button for saving
        
    def load_name(self):
        for name in self.store.get_name():
            self.list_items.insert(END, name)

    def lst_items_clicked(self, event):
        index = self.list_items.curselection()[0]
        id, name, brand, price = self.store.get_item(index)

        self.txt_id.delete(0, END)
        self.txt_id.insert(END, id)

        self.txt_name.delete(0, END)
        self.txt_name.insert(END, name)

        self.txt_brand.delete(0, END)
        self.txt_brand.insert(END, brand)

        self.txt_price.delete(0, END)
        self.txt_price.insert(END, price)

    def btn_add_clicked(self):
        try:
            id = int(self.txt_id.get())
            name = self.txt_name.get()
            brand = self.txt_brand.get()
            price = float(self.txt_price.get())

            self.store.add_item(id, name, brand, price)
            self.list_items.insert(END, name)
            
        except ValueError as e:
            msg.showerror('Error', str(e)) 


    def btn_update_clicked(self):
        try:
            index = self.list_items.curselection()[0]
            name = self.txt_name.get()
            brand = self.txt_brand.get()
            price = float(self.txt_price.get())

            self.store.update_item(index, name, brand, price)
            self.list_items.delete(0, END)
            self.load_name()
        except ValueError as e:
            msg.showerror('Error', str(e))

    def btn_delete_clicked(self):
        try:
            index = self.list_items.curselection()[0]

            self.store.delete_item(index)
            self.list_items.delete(0, END)
            self.load_name()
        except IndexError:
            msg.showerror('Error', 'Please select an item')

    def btn_load_clicked(self):
        filename = fd.askopenfilename(
            
            title='Select file',
            filetypes=[('Sport Data Files', '*.csv')]  # Filter for ".sport" files
        )
        if filename:
            try:
                self.store.load_items(filename)
                self.list_items.delete(0, END)  # Clear existing items
                self.load_name()  # Reload items from loaded data
                msg.showinfo('Success', 'Data loaded successfully!')
            except FileNotFoundError:
                msg.showerror('Error', 'File not found!')
            except Exception as e:  # Catch other potential errors
                msg.showerror('Error', f'Error loading data: {e}')

    def btn_save_clicked(self):
        filename = fd.asksaveasfilename(
            title='Save file',
            filetypes=[('Sport Data Files', '*.csv')]  # Filter for ".sport" files
        )
        if filename:
            try:
                # Extract the filename from the listbox
                items_save = []
                for i in range(self.list_items.size()): #Interate through the listbox
                    item_text = self.list_items.get(i) # get item text from listbox
                    items_save.append(item_text)
                self.store.save_items(filename, items_save) # Save the items
                msg.showinfo('Success', 'Data saved successfully!')
            except Exception as e:
                msg.showerror('Error', f'Error saving data: {e}')

    def run(self):
        self.window.mainloop()

program = StoreGUI()
program.run()