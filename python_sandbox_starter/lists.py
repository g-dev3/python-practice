# A List is a collection which is ordered and changeable. Allows duplicate members.

numbers = [1,2,3,4,5]

numbers = list((1,2,3,4,5))

# print(type(numbers))
fruits = ['Apple', 'Oranges', 'Grapes', 'Pears']
# print(numbers)
# print(fruits[0])

# print(len(fruits))

fruits.append('Mangos')

# print(fruits)

fruits.remove('Oranges')

fruits.insert(2,'Strawberries')

fruits.pop(3)

fruits.reverse()

fruits.sort()
print(fruits)


