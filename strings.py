# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods
name = 'Scott'
age = 24

# concatenate
print('Hello my name is ' + name + ' and I am ' + str(age) + ' years old')

# String Formatting

# Arguments by position
print('Hello my name is {name} and I am {age} years old'.format(
    name=name, age=age))

# F- Strings (only in python 3.6 and up)
print(f'Hello my name is {name} and I am {age} years old')

# String Methods
s = 'hello my name is Scott and I am 24 years old'

# capitalize string
# print(s.capitalize())

# all uppercase
# print(s.upper())

# all lower
# print(s.lower())

# Swap case
# print(s.swapcase())

# get length
# print(len(s))

# replace
# print(s.replace('world', 'everyone'))

# count
# sub = 'h'
# print(s.count(sub))

# starts with
# print(s.startswith('h'))

# ends with
# print(s.endswith('h'))

# split into list
# print(s.split())

# find position
# print(s.find('r'))

# is all alpha numeric spaces violate this
# print(s.isalnum())

# is all alphabetic spaces violate this
# print(s.isalpha())

# is all numeric
# print(s.isnumeric())
