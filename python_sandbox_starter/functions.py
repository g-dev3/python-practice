# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces

def hello (num1 , num2):
  total = num1 + num2
  print(total)

# hello(12,12)

def count(name):
  print(f'helo {name}')

# count('Gopal')

def value(num1, num2):
  total = num1+num2
  return total

total = value(10,10)

print(total)

def id(name='G dev'):
  print(f'Hello {name}')

id('G')


# A lambda function is a small anonymous function.

duff = lambda num1, num2 :num1 +num2

print(duff(9,2))
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

