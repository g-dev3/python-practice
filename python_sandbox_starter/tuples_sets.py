# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
# fruit_tuple= ('Apple','Orange','Mango')

fruit_tuple= tuple(('Apple','Orange','Mango'))


print(fruit_tuple[1])

# print(fruit_tuple[1]= 'Grape')
# print(fruit_tuple) 

fruit_tuple_2  = ('Apple',)

# print(type(fruit_tuple_2))

fruit_set = {'Apple','Orange','Mango'}

# print('Apple' in fruit_set)

fruit_set.add('Grape')

fruit_set.remove('Apple')

fruit_set.clear()

print(fruit_set)


# A Set is a collection which is unordered and unindexed. No duplicate members.
