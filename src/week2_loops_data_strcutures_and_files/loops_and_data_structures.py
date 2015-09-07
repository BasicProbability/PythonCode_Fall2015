'''
Created on Sep 7, 2015

@author: Philip Schulz
'''

from random import randint
# import numpy as np
import string
import sys


hello_world = "Hello, World!?;"
print hello_world.split(' ')
hello_split = hello_world.split('o')
print hello_split
print 'a'.join(hello_split)

print hello_world.translate(None, string.punctuation)

print 1 == 1
print 1 != 1

print True and False
print True or (not False and not (not True))

for char in hello_world:
    print char.upper()
    
i = 0
while i < 10:
    i += 1
    if i == 5:
        break
    
    print i
    
count = 0
while True:
    new_number = randint(1,1000)
    count += 1
    if (new_number > 800):
        break
    
print 'It took ' + str(count) + ' samples to get a number > 800.'

my_first_set = set()
my_first_set = {1,2,3,4,5,6}

my_first_set.add(3)
print my_first_set

my_second_set = {5,6,7,8}
print my_first_set.intersection(my_second_set)
print my_first_set.union(my_second_set)

my_first_dictionary = dict()
my_first_dictionary['a_key'] = 'a_value'

for i in xrange(100):
    my_first_dictionary[i] = i**3
    
# print my_first_dictionary
print my_first_dictionary[66]

my_first_dictionary[66] = 1
print my_first_dictionary[66]

#my_first_dictionary[200]

print my_first_dictionary.has_key(200)
print my_first_dictionary.values()

# for k,v in my_first_dictionary:
#     pass
# 
# for key in my_first_dictionary.keys():
#     pass
# 
# for value in my_first_dictionary.values():
#     pass

try:
    with open('/home/philip/Desktop/testfolder/sample.txt') as my_file:
        for line in my_file:
            print line 
except:
    print 'The specfied file was not found.'
    sys.exit(0)
    