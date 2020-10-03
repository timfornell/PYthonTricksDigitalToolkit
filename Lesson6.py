"""
Lesson 6: A mysterious dictionary expression
"""
print({True: "yes", 1: "no", 1.0: "maybe"})

# Explanation
xs = dict()
xs[True] = "yes"
xs[1] = "no"
xs[1.0] = "maybe"
# Each key here are 'equal' so that the first row sets the value to "yes", the second
# sets it to "no" and the third sets it to maybe
print("True == 1 == 1.0: {}".format(True == 1 == 1.0))