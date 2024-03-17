
from circle import Circle
from rectangle import Rectangle

s = Circle('A',5)
print(s.name, s.radius, s.area())
print(s, f' | Area: {s.area()}')


ss = Rectangle('ABCD', 3,4)
print(ss, f' | Area: {ss.area()}')