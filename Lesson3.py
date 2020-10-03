"""
Lesson 3: Emulating "switch/case" statements

if cond == "cond_a":
    handle_a()
elif cond == "cond_b":
    handle_b()
    .
    .
    .
else:
    handle_default()
"""

def myfunc(a, b):
    return a + b

# Possible to save and access funcitons in lists
funcs = [myfunc]
print(funcs[0](2, 3))

""" 
The idea:
Declare a dict as

func_dict = {
    "cond_a": handle_a,
    "cond_b": handle_b,
}

Get the correct condition handle by calling
func_dict[cond]()

Will however return KeyError if the "cond" is not in func_dict, can be solved by

func_dict.get(cond, handle_default)()

where handle_default will be called if cond is not in func_dict. The dict containing all the 
functions should be saved somehwhere so that it doesn't have to be created each time.
"""

# Example 1
def handle_a():
    print("a")

def handle_b():
    print("b")

def handle_default():
    print("Condition not found")

func_dict = {
    "a": handle_a,
    "b": handle_b,
}

func_dict.get("b", handle_default)()
func_dict.get("c", handle_default)()

# Example 2
def dispatch_dict(operator, x, y):
    return {
        "add": lambda: x + y,
        "sub": lambda: x - y,
        "mul": lambda: x * y,
        "div": lambda: x / y,
    }.get(operator, lambda: None)()

print(dispatch_dict("add", 2, 3))
print(dispatch_dict("avs", 2, 3))
print(dispatch_dict("div", 2, 3))