# If/ Else conditions are used to decide to do something based on something being true or false

x= 10
y=6

# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values
if x== y: 
  print(f'{x} is equal to {y}')


if x>y:
  print(f'{x} is greater than {y}')
else:
    print(f'{x} is less than {y}')


if x>y:
  print(f'{x} is greater than {y}')
elif x==y:
    print(f'{x} is equal to {y}')
else: 
  print(f'{x} is less than {y}')


if x > 2:
  if x<=10:
    print('helo')
  else:
    print('Bye')
else:
  print('noloy ')

# Logical operators (and, or, not) - Used to combine conditional statements

# if x > 2 or x<=10:
  print(f'{x} is less than 2 or greater than 10')

# if x> 2 and x <=10:
  print('yes its working')

# if not(x== y):
  print('its wront but i am using not oprator')


# Membership Operators (not, not in) - Membership operators are used to test if a sequence is presented in an object
m=10
numbers = [1,2,3,4,5,6]


if m in numbers:
  print(x in numbers)



# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
