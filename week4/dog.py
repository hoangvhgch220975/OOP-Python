
from pet import Pet

class Dog(Pet):
    def __init__(self, name, age, onwer):
        super().__init__(name, age, onwer)

    def woof(self):
        print('Woof!  Woof!  Woof!')


dog = Dog('Kiki',3,'Sarah')
dog.show()
dog.woof()