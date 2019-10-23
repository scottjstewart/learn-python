# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Create a class


class User:
    # constructor
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
    # method

    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'

    def has_birthday(self):
        self.age += 1

# extend class this greeting could also be accessed from the parent by calling rob.greeting() in a print


class Customer(User):
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def set_balance(self, balance):
        self.balance = balance

    def greeting(self):
        return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}'


# init customer
rob = Customer('rob', 'rob@rob.com', 27)

rob.set_balance(500)
print(rob.greeting())

# initialize user object
scott = User('Scott', 'scott@test.com', 25)
print(type(scott), scott.name)
scott.has_birthday()
print(scott.greeting())
