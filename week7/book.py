class Book:
    def __init__(self,id, title, author, price):
        if not isinstance(id,int) or id < 0:
            raise ValueError('Id must me a number and not negative')
        if title == '':
            raise ValueError('Title cannot be empty')
        if author == '':
            raise ValueError('Author cannot be empty')
        if not isinstance(price, float) or price <= 0:
            raise ValueError('Price cannot be negative')
        self._id = id
        self._title = title
        self._author = author
        self._price = price

#Provide getter for id
#Provide getter, setter for tittle, author, price
    @property   
    def id(self):
        return self._id
    
    
    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, value):
        if value == '':
            raise ValueError('Title cannot be empty')
        self._title = value


    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        if value == '':
            raise ValueError('Author cannot be empty')
        self._author = value

    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, value):
        if not (isinstance(value, float) or isinstance(value, int)) or value <= 0:
            raise ValueError('Price cannot be negative')
        self._price = value
    
    
