# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces


# create a function default value can be set and will work without receiving a parameter on function call
def sayHello(name='sam'):
    print(f'Hello {name}')


sayHello()


# Return Values
def getSum(num1, num2):
    total = num1 + num2
    return total


num = getSum(1, 2)
print(num)

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

# prettier reformatted the lambda function
# getSum = lambda num1, num2 : num1 + num2


def getSum(num1, num2): return num1 + num2


print(getSum(10, 3))
