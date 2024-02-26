# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Create class

class User:
  # Constructor
  def __init__(self, name, email, age):
    self.name = name
    self.email = email
    self.age = age

  def greeting(self):
   return f'My name is {self.name} and i am {self.age}'

# Init user object
brad = User('Brad Traversy', 'brad@gmail.com',31)
janet = User('Janet Williams', 'jain@gmail.com', 12)
brad.age= 38
# print(janet.age)

# print(janet.greeting())


# greet = greeting()

class User:
  def __init__(self,name,email,age):
    self.name = 'G Dev'
    self.email = "gdev@gmail.com"
    self.age = 20


# brad = User('Brad Traversy','brad@gmail.com',31)

# print(User(brad.age))


class User:
  # constructor
  def __init__(self,name,email,age):
    self.name = name
    self.email = email
    self.age = age

  def greeting(self):
    return f'My name is {self.name} and age is {self.age}'

  def has_birthday(self):
    self.age += 1


#Init user object
brad = User('Brad Traversy','brad@gmail.com',37)
janet = User('Jenet williams','jaten@gmail.com',21)

print(brad.greeting())
print(janet.greeting())
print(janet.age)
print(brad.name)
print(janet.email)
brad.age = 21
janet.email = 'janet1@gmail.com'
print(brad.email)
print(janet.email)
print(janet.age)
janet.has_birthday()
print(janet.greeting())

class Customer(User):
   def __init__(self,name,email,age):
    self.name = name
    self.email = email
    self.age = age
    self.balance = 0

   def report(self):
    return f'Your Balance is {self.balance}'

   def set_balance(self,balance):
    self.balance = balance


john = Customer('John Doe','john@gmail.com',21)

john.set_balance(500)

print(john.report())

