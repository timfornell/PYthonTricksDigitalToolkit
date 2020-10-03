""" 
Lesson 1: List comprehensions
"""

values = [x * x
          for x in range(10)
          if x % 2 == 0]
print(values)