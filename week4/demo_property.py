class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

#Traditional get/set method:
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        if name =="":
            print("Name cannot be empty")
        else:
            self.__name = name
        
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, age):
        if age < 0:
            print('Age cannot be negative')
        else: 
            self.__age = age


john = Student("John",20)
print(john.get_name(),john.age)



john.set_name('John Doe')
john.age = 21

print(john.get_name(), john.age)