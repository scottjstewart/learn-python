# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

# core imports
import datetime
from datetime import date
import time
from time import time

# pip module
from camelcase import CamelCase

# import custom module this comes from our created validator module
from validator import validate_email

# today = datetime.date.today() these will both be the same
today = date.today()
timestamp = time()
c = CamelCase()
email = 'test@test.com'
if validate_email(email):
    print(f'{email} is a valid email')
else:
    print(f'{email} is an invalid email')

print(c.hump('hello good sir'))
print(today, timestamp)
