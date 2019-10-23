# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

people = ['scott', 'nick', 'rob', 'andrew']

# simple loop
for person in people:
    print(f'current person: {person}')

# Break this stops at rob
for person in people:
    if person == 'rob':
        break
    print(f'current person: {person}')

# continue this skips rob
for person in people:
    if person == 'rob':
        continue
    print(f'current person: {person}')

# range
for i in range(len(people)):
    print(people[i])

for i in range(0, 11):
    print(f'Number: {i}')

# While loops execute a set of statements as long as a condition is true.
count = 0
while count <= 10:
    print(f'Count: {count}')
    count += 1
