from requests import delete
from sport_item import SportItem
import csv

class Store:
    def __init__(self):
        self.__items = []  # Initialize empty list for items

    def load_items(self, file_name):
        items = []
        if file_name:  # Check if a filename is provided
            try:
                with open(file_name, 'r') as f:
                    reader = csv.reader(f)
                    # Skip header
                    next(reader)
                    # Scan each row
                    for row in reader:
                        id = int(row[0])
                        name = row[1]
                        brand = row[2]
                        price = float(row[3])
                        s = SportItem(id, name, brand, price)
                        items.append(s)
            except FileNotFoundError:
                print('File not found!')
            except Exception as e:  # Catch other potential errors
                print(f'Error loading data: {e}')
        self.__items = items  # Update internal items after successful loading
        return items
    
    def save_items(self, file_name,items):
        with open(file_name, 'w', newline='') as f:
            writer = csv.writer(f)
            # write header
            writer.writerow(['ID', 'Name', 'Brand', 'Price'])
            # write items
            for s in self.__items:
                writer.writerow([s.id, s.name, s.brand, s.price])
    
    def get_name(self):
        return (s.name for s in self.__items)
    
    def get_item(self, index):
        # return self.__items[index] => not safe, expose items info outside
        s = self.__items[index] 
        # safe because we return a copy of item's info
        return s.id, s.name, s.brand, s.price
    
    def add_item(self, id, name, brand, price):
        self.__items.append(SportItem(id, name, brand, price))

    def update_item(self, index, name, brand, price):
        s= self.__items[index]
        s.name = name
        s.brand = brand
        s.price = price

    def delete_item(self, index):
        del self.__items[index]