from Cat import Cat

class Owner: 
    def __init__(self,name,pet):
        self.name = name
        self.pet = pet
    
    def show(self):
        print(f'My name is {self.name}, my pet is {self.pet.name}')
    
Kitty = Cat('Kitty','John')
john = Owner('John', Kitty)

john.show()