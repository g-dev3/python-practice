# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary

import json 

#  Sample JSON
userJSON = '{"first_name": "John", "last_name": "Doe", "age": 30}'

# Parse to dict
user = json.loads(userJSON)

print(user)
print(user['first_name'])
print(user['age'])
user['age'] += 1

print(user['age'])

user['first_name']= 'Gopal'
user['last_name'] = 'Kumawat'
user['age']= 21

# print(user)

admin = {'first_name': 'Gopal', 'last_name': 'Kumawat', 'age': 21}

adminJSON = json.dumps(admin)

print(adminJSON)
