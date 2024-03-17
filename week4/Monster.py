
class Monster:
    def __init__(self, strength, health):
        self.__strength = strength
        self.__health = health
        self.__position = (0,0)

    @property
    def strength(self):
        return self.__strength
    
    @strength.setter
    def strength(self, value):
        self.__strength = value

    @property
    def health(self):
        return self.__health
    
    @health.setter
    def health(self, value):
        self.__health = value
        
    
    def move(self,x,y):
        self.__position = (x,y)
        print(f'Move to ({x}, {y} position)')

    def attack(self):
        print(f'Attack enemy {self.__strength} damage')


# monster = Monster(strength=10, health=100)
# monster.move(2, 3)
# monster.attack()
