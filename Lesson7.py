"""
Lesson 7: Funciton argument unpacking

'*': List unpack operater
'**': Dict unpack operator
"""

def print_vector(x, y, z):
    print("<%s, %s, %s>" % (x, y, z))

print_vector(0, 1, 0)

# print_vector works fine unless the values are store in tuples or vectors
tuple_vec = (0, 1, 0)
list_vec = [1, 0, 1]

print_vector(tuple_vec[0], tuple_vec[1], tuple_vec[2]) # => Lot of manual writing

# Solution argument unpacking, using '*' will generate the same result as above
print_vector(*tuple_vec)

gen_expr = (x * x for x in range(3))
print_vector(*gen_expr) # The length of input has to be 3

dict_vec = {"x": 1, "y": 2, "z": 3} # Cant be passed with the '*' => use '**' 
print_vector(**dict_vec) # This works since the keys in the dict and the variable names match