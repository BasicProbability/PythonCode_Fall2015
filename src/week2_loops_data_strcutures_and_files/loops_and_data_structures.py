'''
Created on Sep 7, 2015

@author: Philip Schulz
'''

# Import all necessary packages and functions.
# Notice that you can use 'as' to assign shorter names to packages.
from random import randint
# import numpy as np
import string
import sys

# A little update on lists: you can actually sort them.
my_list = 'this is a sentence with a lot of words.'.split(' ')
print my_list
# The sort method can take arguments. If you are interested in them, check out the
# documentation.
my_list.sort()
print my_list

# Let us again define a hello world string, this time with more punctuation.
hello_world = "Hello, World!?;"
# We can split strings around white spaces.
print hello_world.split(' ')
# We can also split them around any other character or character sequence.
hello_split = hello_world.split('o')
print hello_split
# Finally, we can join a list of strings around a common character or sequence.
print 'a'.join(hello_split)

# The translation function helps us to delete characters. For this, we specify which
# characters to delete in the second argument. Check the documentation for the use of
# the first argument.
print hello_world.translate(None, string.punctuation)

# Basic comparison operators that yield boolean outcomes.
print 1 == 1
print 1 != 1

# We can also make some more involved boolean statements. Notice that each True and False here
# might itself be a boolean statement, e.g. a comparison.
print True and False
print True or (not False and not (not True))

# This just reminds us of how for-loops work. This time, we are looping over the characters
# in a string.
for char in hello_world:
    print char.upper()

# The while-loop executes while the boolean condition in its head is true.
# We can use the break statement to terminate a while-loop prematurely.
# If you put a break statement into a for-loop, it works the same way, i.e. it breaks the loop.
i = 0
while i < 10:
    i += 1
    if i == 5:
        break
    
    print i
    
# Sometimes it may make sense to start an infinite loop on purpose. In that case we need the
# break statement if we ever want to get out of the loop. This little loop counts how often
# we need to sample random numbers until we get one that is greater than 800.
count = 0
while True:
    new_number = randint(1,1000)
    count += 1
    if (new_number > 800):
        break
    
print 'It took ' + str(count) + ' samples to get a number > 800.'

# Sets work just like you would expect them to. They can be created in two ways, where the
# first statement creates an empty set.
my_first_set = set()
my_first_set = {1,2,3,4,5,6}

# Obviously, adding an element to a set that is already in the set, does not change the set.
my_first_set.add(3)
print my_first_set

# Standard set operations, like intersection and union are readily supported by Python.
my_second_set = {5,6,7,8}
print my_first_set.intersection(my_second_set)
print my_first_set.union(my_second_set)

# Dictionarires are a super-useful data structure for storing data in a principled way.
# They are Python's implementation of the general idea of a key-value-map.
my_first_dictionary = dict()
# This is how you assign a value to a key.
my_first_dictionary['a_key'] = 'a_value'

# If you want to create many key-value pairs, a for-loop often comes in handy.
for i in xrange(100):
    my_first_dictionary[i] = i**3
    
print my_first_dictionary
# You can check the value associated to a given key like this.
print my_first_dictionary[66]

# You can also change that value
my_first_dictionary[66] = 1
print my_first_dictionary[66]

# If a key is not yet in the dictionary, you will get a KeyError.
#my_first_dictionary[200]

# That's why you should always first check whether or not a key is present.
print my_first_dictionary.has_key(200)

# Sometimes, we will not care about the keys and just want to collect all values.
print my_first_dictionary.values()

# We can also iterate over all key-value pairs in a dictionary using a for-loop.
# Make sure to use the iteritems() function to get all key-value pairs.
for k,v in my_first_dictionary.iteritems():
    pass
 
# Likewise, we can iterate over all keys.
for key in my_first_dictionary.keys():
    pass
 
# And over all values
for value in my_first_dictionary.values():
    pass

# This is how you open up a stream to a file. For the time being, we will treat
# the try-except construct as a black box. Just notice that the file might not
# be present on your computer, in which case you'd get a FileNotFoundError. 
# The with open(...) statement automatically closes the stream for you after it has been
# used. This is very convenient and you should therefore always use with open(...) when
# you create a stream.
try:
    with open('/home/philip/Desktop/testfolder/sample.txt') as my_file:
        # You can iterate through your text file line by line.
        for line in my_file:
            print line 
except:
    print 'The specfied file was not found.'
    sys.exit(0)
    