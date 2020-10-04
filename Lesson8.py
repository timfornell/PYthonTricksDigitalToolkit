"""
Lesson 8: OOPmethod types comparison
@classmethod vs @staticmethod vs 'plain' methods
"""
import math

class MyClass:
    """
    Plain method, instance method:
    Can modify object instance state
    Can modify class state
    """
    def method(self):
        return 'instance method called', self

    """ 
    Class method: 
    Cant modify object instance state, i.e. not properties of the 'self' object
    Can modify class state, i.e. it can access attributes in the class
    """
    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    """
    Static method:
    Cant modify either the class or the instance (self)
    """
    @staticmethod
    def staticmethod():
        return 'static method called'

obj = MyClass()
print(obj.method()) # 'self' points to obj
print(obj.classmethod()) # 'cls' points to MyClass
print(obj.staticmethod())

# The static and class methods can be accessed directly through MyClass
print(MyClass.classmethod())
print(MyClass.staticmethod())

class Pizza:
    def __init__(self, radius, ingredients):
        self.radius = radius
        self.ingredients = ingredients

    def __repr__(self):
        return f'Pizza({self.ingredients})'

    def area(self):
        return self._circle_area(self.radius)

    @classmethod
    def margherita(cls):
        return cls(10, ["cheese", "tomatoes"])

    @classmethod
    def prosciutto(cls):
        return cls(10, ["cheese", "tomatoes", "ham"])

    @staticmethod
    def _circle_area(r):
        return r ** 2 * math.pi

# In this case the classmethod can be used to create specific 'pizzas'
# withouth having to manually typing the ingredrients
print(Pizza(10, ["cheese", "tomatoes"]))
print(Pizza.margherita())
print(Pizza.prosciutto())

# Static methods often used for helper functions since they can not modify
# the class or class instance, kinda like a namespace
print(Pizza.margherita().area())
print(Pizza._circle_area(10))