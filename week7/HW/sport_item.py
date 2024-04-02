class SportItem:
    def __init__(self,id, name, brand, price):
        if not isinstance(id,int) or id < 0:
            raise ValueError('Id must me a number and not negative')
        if name == '':
            raise ValueError('Name cannot be empty')
        if brand == '':
            raise ValueError('Brand cannot be empty')
        if not isinstance(price, float) or price <= 0:
            raise ValueError('Price cannot be negative')
        self._id = id
        self._name = name
        self._brand = brand
        self._price = price


# Provide getter for id
    @property
    def id(self):
        return self._id
# provide getter, setter for name, brand, price
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if value == '':
            raise ValueError('Name cannot be empty')
        self._name = value

    @property
    def brand(self):
        return self._brand
    @brand.setter
    def brand(self, value):
        if value == '':
            raise ValueError('Brand cannot be empty')
        self._brand = value

    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, value):
        if not (isinstance(value, float) or isinstance(value, int)) or value <= 0:
            raise ValueError('Price cannot be negative')
        self._price = value