from Monster import Monster

class AirMonster(Monster):
    def __init__(self, strength, health, height):
        super().__init__(strength, health)
        self.__height = height

    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, value):
        self.__height = value

    def move(self, x, y):
        print(f"Fly to ({x}, {y}) position above {self.__height} kilometers in the air")
        self._Monster__position = (x, y)  
    def attack(self): 
        print(f"Attack enemy with {self.strength} damage from the sky")

air_monster = AirMonster(strength=25, health=180, height=10)
air_monster.move(8, 15)
air_monster.attack()
