# Python has functions for creating, reading, updating, and deleting files.


# open a file
my_file = open('myfile.txt', 'w')

# get some info on this file
print('Name: ', my_file.name)
print('Is Closed: ', my_file.closed)
print('Opening Mode: ', my_file.mode)

# write to file
my_file.write('Whaddup dude')
my_file.write('how are you')
my_file.close()


# append to file
my_file = open('myFile.txt', 'a')
my_file.write(' its been awhile')
my_file.close()

# read from a file
my_file = open('myFile.txt', 'r+')
text = my_file.read(100)
print(text)
