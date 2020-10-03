"""
Lesson 4: Implicit returns

"""

# Python will automatically return None, all following functions will return the same value
def foo1(value):
    if value:
        return value
    else:
        return None

def foo2(value):
    """ Bare return statement implies 'return None'"""
    if value:
        return value
    else:
        return

def foo3(value):
    """ Missing return statement implies 'return None'"""
    if value:
        return value

print(foo1(False))
print(foo2(False))
print(foo3(False))

