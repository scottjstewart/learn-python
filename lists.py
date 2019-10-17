# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create List
numbers = [1, 2, 3, 4]
fruits = ['apples', 'oranges', 'grapes', 'pears']

# use a contructor this is the less common way
# numbers2 = list((1, 2, 3, 4))

# print(numbers, numbers2)

# get value
print(fruits[1])

# get length
print(len(fruits))

#append or add
fruits.append('mangos')

# remove
fruits.remove('grapes')

# insert into position
fruits.insert(2, 'strawberries')

# change value
fruits[0] = 'blueberries'

# remove from position
fruits.pop(2)

# reverse the list
fruits.reverse()

# sort
fruits.sort()

# reverse sort
fruits.sort(reverse=True)

print(fruits)
