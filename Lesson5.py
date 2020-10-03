""" 
Comparing objects
"""

# is vs ==
# Two cat analogy
# == checks if two objects are equal, are these cats similar? => Yes, they look the same
# is checks if two objects are identical, are these two cats the same cat? => No, there are two cats

# Example
a = [1, 2, 3]
b = a

print(a == b) # => True since they contain the same elements
print(a is b) # => True since b and a both point to the underlying object

a[0] = "hello"
print(a,b) # => Both a and b have changed
a[0] = 1
c = list(a) # Shallow copy
print(a, b, c) # They all look the same
print(a == c) # => Returns True since they contain the same elements
print(a is c) # => Returns False since they do not point to the same underlying object