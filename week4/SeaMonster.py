from Monster import Monster
class SeaMonster(Monster):
    def __init__(self, strength, health, depth):
        super().__init__(strength, health)
        self.__depth = depth

    @property
    def depth(self):
        return self.__depth
    
    @depth.setter
    def depth(self, value):
        self.__depth = value

    def move(self, x, y):
        print(f"Swim to ({x}, {y}) position under {self.__depth} kilometers in the sea")
        self._Monster__position = (x, y) 
    def attack(self):
        print(f'Attack enemy {self.strength} damage')



# sea_monster = SeaMonster(strength=20, health=150, depth=8)
# sea_monster.move(6, 10)
# sea_monster.attack()
