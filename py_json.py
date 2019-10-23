# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary this file was named py_json because it cant be named the same as an import
import json

# sample json
userJSON = '{"first_name": "Scott", "last_name":"Stewart", "age":25}'

# parse to dict
user = json.loads(userJSON)
print(user)
print(user['first_name'])

# turn dictionary into json
car = {'make': 'bmw', 'model': '328xi', 'year': 2007}

carJSON = json.dumps(car)

print(carJSON)
