class item:
    def __init__(self,id,name,price,quantity) :
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

    def show_item(self):
        print(f"Item ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Price: ${self.price:.2f}")
        print(f"Quantity: {self.quantity}")

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_quantity(self):
        return self.quantity

    def add_quantity(self, quantity_to_add):
        self.quantity += quantity_to_add
        print(f"{quantity_to_add} units added to the quantity. New quantity: {self.quantity}")


item1 = item(1, "Laptop", 999.99, 5)
item2 = item(2,"Iphone", 1000.00,4)
item1.show_item()
item2.show_item()
print(f"Item ID: {item1.get_id()}")
print(f"Item Name: {item1.get_name()}")
print(f"Item Price: ${item1.get_price():.2f}")
print(f"Item Quantity: {item1.get_quantity()}")
item1.add_quantity(3)


class inventory:
    def __init__(self,
