'''
Created on Aug 31, 2015

@author: Philip Schulz
'''

import datetime

# Python can do addition
print 8+9

# Instead of doing addition, this statement just
# prints whatever is inside the quotes
print "8+9"

# The reason for this behaviour are the differences in type.
# The first statement gives you an integer while the second
# statement gives you a string.
print type(8+9)
print type("8+9")

# The plus sign is defined as concatenation for strings
print "8+9" + "=17"
# We cannot use plus for to concatenate different types. This
# will give us a type error. In order to prevent the error from
# occurring I commented out the line below.
# print 8*9 + "=17"

# This will print hello world. Notice that in Python we can use
# double or single quotes to create strings.
print 'Hello world!'

# If we use double quotes, we can use single quotes as apostrophes
# inside a string.
print "Sam's town"

# Python cann also do multiplication. For strings multiplication just
# repeats the string a specified number of times.
print 60*32
print 'Hello world!'*3

# Exponentiation is done by the double star.
print 5**2

# We can do also modulo arithmetic. What we will get here is the remainder
# of the division
print 10%3

# Apart from integers, we have also the type float for floating point numbers.
print type(13.2)

# DO NOT DO THIS! Your variables should always have informative names. Otherwise
# you won't be able to understand their meaning the next time you read your code.
a = 8*9
b = 5*12


# DO THIS! Give your variables sensible and informative names.
first_number = 8*9
second_number = 5*12

# We can insert a number into a string by also converting into a 
# string using the str() function
print 'first number first trial =' + str(first_number)

# Here, we assign a new value to our variable first_number. The whole point of
# variables is that you can assign new values to them whenever you please.
first_number = 5
print 'first_number second trial =' + str(first_number)
print first_number+second_number

# One of the most basic and useful data structures in Python are lists. They
# can be created as emtpy lists with the list() function for by specifying
# their members directly.
our_list = list()
our_list = ['Hello world', 12, list()]
print our_list

# We can also append to an existing list. This is at the same time the first
# instance of a method that we see. Methods are functions that belong to an
# object. You can recognise them easily as they always appear after the object
# name and a dot.
our_list.append(25)
print our_list

# It turns out that strings are also just lists (of characters). We can use
# the bracket notation to pick out an element of a list. Note that we start
# counting list positions from 0. In the commented line below we are thus 
# actually trying to access position 5. However, our_list only has four
# positions. Hence, this operation will result in an error.
hello_world = 'Hello world'
print hello_world[3]
# print our_list[4]

# Since the first (0th) element of our_list is a string, we can again immediately
# pick out one of its elements.
print our_list[0][6]

# Instead of just picking out one element we pick out a 'slice'. This is done
# by specifying a start and end index. If one of them is not specified the slice
# will just continue till the beginning or end of the list.
print hello_world[2:]
print hello_world[:10]
print hello_world[2:10]
print hello_world[:1]

# Lists can also be accessed from behind. -1 is the last position, -2 the second-to-last
# position and so on.
print hello_world[-1]

# List comprehension is a useful tool to build lists. Notice that here we use a variable
# i that is updated with the values in the range [0,11). If you just use variables for
# iteration and never use them again, then using single letters may be ok.
print [2**i for i in xrange(11)]

# Please always use xrange() instead of range() when doing iteration. The reason is that
# xrange() just gives you the numbers you need whereas range() produces an actual list
# which can result in a lot of time and memory overhead.
print range(10)

# Again, we can pick out specific elements from our list built using list comprehension.
print [2**i for i in xrange(11)][5]

# Note that we can also check how long our lists are using len().
print 'Our list has length ' + str(len(our_list))

# Moreover, we can concatenate lists, again by just using the plus symbol.
print our_list + [2**i for i in xrange(11)]


# We are now going to see our first control structure, the if-statement. The code inside
# an if-statement will only be executed if the condition of the if-statement is true.
# Otherwise it will be ignored. The else-statement provides a default for the if-statement
# that executes whenever the if-statement didn't. Notice that you can have an if without an
# else but not the other way around.

# The first line in a nested statement is called the head.
if first_number >= second_number:
    # The inner part is called the body.
    first_half = 'This is '
    second_half = 'true!'
    print first_half + second_half

else: 
    print 'False'
    
# If you want to compare strings, it is often advisable to lowercase them so that
# case differences won't matter. Notice that we use double equals signs for identity
# comparisons (this is true if the argument are the same and false otherwise).
if hello_world.lower()[0] == 'h':
    first_half = 'This is '
    second_half = 'true!'
    print first_half + second_half

# Before defaulting to else you can check more than one condition. This is done
# using elif (for else if).
elif hello_world[0] == 'x': 
    print 'False'
    
else: 
    print "'Whatever!'"
    
    
# We can ask the user for input using the raw_input() function.    
user_name = raw_input('What is your name? ')
user_age = raw_input('How old are you?')
# All user input will be read as a string. You may need to convert if for your
# purposes.
print type(user_age)
print 'Hello, ' + user_name + '. Nice to meet you.'

# There are a couple of important 'escape characters'. \t inserts a tab space into a
# string and \n produces a line break.
print "\"hello\"\t Paul.\nHow are you today?"


# The for-loop allows us to execute code repeatedly. It also updates an iterator variable
# for us that we can use in the code.
for i in xrange(10):
    print i

# Most of the time you will actually want to connect for and if loops. This essentially allows
# you to use an if-statement multiple times but with a different input value each time.
for i in xrange(10):
    if i %2 == 0:
        print "even"
    else:
        print 'odd'
        

# Finally, we can also obtain some system information lik what date it is. Notice that in
# order to do this we actually need to import another package called datetime. If you
# look at the very beginning of this code, you will see the statement 'import datetime' there.
today = datetime.datetime.now()

print today.year
print today.day
print today.month