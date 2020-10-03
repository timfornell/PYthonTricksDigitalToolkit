"""
Lesson 2: String conversion "__repr__" vs "__str__"
"""

class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage
    
    def __str__(self):
        return "a {self.color} car".format(self=self)

    def __repr__(self):
        return "__repr__ for Car"

my_car = Car("red", 37281)

# Running 'my_car' print something like <__main__.Car object at 0x0000024A056076D8>
# While running 'print(my_car)' or 'str(my_car)' calls the __str__ function
print(my_car)
print(str(my_car))
print("{}".format(my_car))

# Running 'repr(my_car)' or 'my_car' will call the __repr__ function
print(repr(my_car))

import datetime
today = datetime.date.today()
# This prints the actual date
print(str(today))
# This prints the class representation of today
print(repr(today))

# Conclusion:
# __str__ => easy to read, for human consumtion
# __repr__ => unambigiuous, more meant for developers

# Implementation tip, always implement __repr__ somewhat like this
class Car2:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __repr__(self):
        return "{self.__class__.__name__}({self.color}, {self.mileage})".format(self=self)

my_car = Car2("red", 37281)
print(repr(my_car))
print(my_car)
