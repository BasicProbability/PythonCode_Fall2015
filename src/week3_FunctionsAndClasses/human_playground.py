'''
Created on Sep 14, 2015

@author: philip
'''
from people import Human
from people import Student

bart = Human(32)

bart.have_birthday()
print bart.age

elisa = Student('Elisa', 30, 8.2)

print elisa.haircolour

elisa.change_haircolour('green')

print elisa.haircolour

print elisa.name

print elisa.tell_age()
# print bart.name