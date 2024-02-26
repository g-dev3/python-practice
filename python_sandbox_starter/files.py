# Python has functions for creating, reading, updating, and deleting files.

#open a file
myFile = open('myfile.txt','w')

# Get some info
print('Name: ', myFile.name)
print('is Closed: ', myFile.closed)
print('Oening Mode: ', myFile.mode)


# Write to file

myFile.write('I love Python')
myFile.write(' and Javascript')

myFile.close()

#  Append to file
myFile = open('myfile.txt', 'a')
myFile.write(' I also like PHP')
myFile.close()

#  Read from file
myFile = open('myfile.txt', 'r+')
text = myFile.read(50)
print(text)