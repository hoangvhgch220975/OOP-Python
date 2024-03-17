class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def show(self):
        print(f'Name: {self.__name} | Age: {self.__age}')



