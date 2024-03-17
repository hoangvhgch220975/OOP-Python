from animal import Animal
class Pet(Animal):
    def __init__(self,name, age,onwer):
        super().__init__(name,age)
        self.__owner = onwer
        
    def show(self):
        super().show()
        print(f'Owner: {self.__owner}')

cat = Pet('Cat', 2, 'John')
cat.show()