'''
Created on Sep 14, 2015

@author: Philip Schulz
'''
# It is good practice to only import the features that you really need
from people import Human
from people import Student

# Here we build our first Human
bart = Human(32)

# This shows that the method have_birthday really works
bart.have_birthday()
print bart.age

# Now we create a Student object
elisa = Student('Elisa', 30, 8.2)

print elisa.haircolour

elisa.change_haircolour('green')

print elisa.haircolour

print elisa.name

print elisa.tell_age()

# Notice that although Students have names, Humans still do not.
# print bart.name