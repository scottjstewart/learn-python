# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# create dictionary
person = {
    'first_name': 'Scott',
    'last_name': 'Stewart',
    'age': 24
}

# constructor
# person2 = dict(first_name='James', last_name='Williams')
# print(person2, type(person2))

# get value
print(person['first_name'])
print(person.get('last_name'))

# add key value
person['phone'] = '1234567'

# get dictionary keys
print(person.keys())

# get items
print(person.items())

# copy dictionary
person2 = person.copy()
person2['city'] = 'Indianapolis'
print(person2)

# remove an item
del(person['age'])
person.pop('phone')

# clear
person.clear()

# length
print(len(person2))

# list of dictionaries
people = [
    {'name': 'Scott', 'age': 24},
    {'name': 'Nick', 'age': 22}
]
print(people[1]['name'])


print(person, type(person))
