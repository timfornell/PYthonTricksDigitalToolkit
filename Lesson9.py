"""
*args and **kwargs
"""

"""
This function required the 'required' arguments but it can also accept 
extra positional and keyword arguments.
"""
def foo(required, *args, **kwargs):
    print(required)
    if args:
        print("args{}".format(args))
    if kwargs:
        print("kwargs{}".format(kwargs))

# foo() => Will fail since required was not provided
foo("hello") # => prints 'hello'
foo("hello", 1, 2, 3) # => prints 'hello' and args(1,2,3) ((1,2,3) is a tuple)
foo("hello", 1, 2, 3, key1="value", key2=999) # => The kwargs are saved in a dictionary

# Can be useful when wrapping other functions
def bar_wrapper(x, *args, **kwargs):
    kwargs["name"] = "Alice"
    new_args = args + ("extra",)
    bar(x, *new_args, **kwargs)

# Class example
class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

class AlwaysBlueCar(Car):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.color = "blue"