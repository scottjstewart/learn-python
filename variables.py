# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""


# x = 1 #casted by int as default
# y = 2.5 #casted as a float
# name = 'john' #casted as a string
# is_cool = True #casted as a boolean t or f should be capitalized

# Multiple Assignment Operator
x, y, name, is_cool = (1, 2.5, 'john', True)

# Basic math
a = x + y

# casting types
x = str(x)
y = int(y)
z = float(y)

# print types
print(type(z), z)
