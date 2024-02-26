# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.


person = {
  'first_name':'G dev',
  'last_name': 'group'
}


# person = dict(first_name='G dev', last_name='group')

print(person['first_name'])
print(person.get('last_name'))
person['age']=21

print(person.keys())
print(person.items())

person2 = person.copy()

person2['city']= 'Boston'

del(person['age'])
person.pop('first_name')

person.clear()

# print(person)
print(len(person2))