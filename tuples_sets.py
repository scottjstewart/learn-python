# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# create a tuple single value needs trailing comma
fruits = ('apples', 'oranges', 'grapes')
fruits2 = ('apples',)
# with a constructor this is normally not used
# fruits2 = tuple(('apples', 'oranges', 'grapes'))

# single value same as list
print(fruits[1])
# tuples cant be changed
# fruits[0] = 'pears'
# delete tuple
del fruits2
# length is same as list
# print(fruits, type(fruits2))


# A Set is a collection which is unordered and unindexed. No duplicate members.
# create a set
fruits_set = {'apples', 'oranges', 'grapes'}

# check if in set
print('apples' in fruits_set)

# add to set
fruits_set.add('mango')

# remove something
fruits_set.remove('grapes')

# clear set entirely delete is different than deleting with del keyword
fruits_set.clear()

print(fruits_set)
