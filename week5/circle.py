from shape import Shape

class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)  #initiate abtract class Shape
        self.__radius = radius  #private class
        self._type = 'Circle'   #protect class

    @property
    def radius(self):
        return self.__radius
    
    @radius.setter
    def radius(self, value):
        self.__radius = value

    #overwrite the abstract method from abstract class
    def area(self):
        return 3.14 * self.__radius**2
    
    def __str__(self):
        return super().__str__() + f' | Radius: {self.radius}'
    