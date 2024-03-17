class LightBulb:
    def __init__(self,name):
        self.__name = name
        self.__light = False #By default, light is off

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,value):
        self.__name = value

    @property
    def light(self):
        return self.__light
    
    def turn_on(self):
        self.__light = True

    def turn_off(self):
        self.__light = False

    def show(self):
        print(f"{self.name} is {'on' if self.__light else 'off'}")


# bedroom_light = LightBulb('Bedroom LIght')
# bedroom_light.show()
# bedroom_light.turn_on()
# bedroom_light.show()


class ColorLightBulb(LightBulb):  #ClassA(B): mean class A inherits from class B
    def __init__(self, name,color):
        super().__init__(name)   #Call the constructor from super class (LightBulb)
        self.__color = color

    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self,value):
        self.__color = value

    
    def show(self):
        super().show() #Call the method show from super class (LightBulb)
        #add a new code to  show color
        if self.light: #use the properity, cannot access self.__light directly because it private
            print(f'Color: {self.color}')
        else: 
            print('No color when light is off')
# bedroom_light = ColorLightBulb('Bedroom LIght', 'red')
# bedroom_light.show()
# bedroom_light.turn_on()
# bedroom_light.show()
# bedroom_light.turn_off()
# bedroom_light.show()

class MultiColorLightBulb(ColorLightBulb):
    def __init__(self, name):
        super().__init__(name, 'white') #Call the constructor from ColorLightBulb
        self.__current = 0 # index for current color

    def turn_on(self):
        colors = ['red', 'green', 'yellow']
        self.__current = (self.__current + 1) % 3
        self.color = colors[self.__current]
        super().turn_on()

bedroom_light = MultiColorLightBulb('Bedroom LIght')
bedroom_light.show()
bedroom_light.turn_on()
bedroom_light.show()
bedroom_light.turn_on()
bedroom_light.show()
bedroom_light.turn_on()
bedroom_light.show()
bedroom_light.turn_off()
bedroom_light.show()



