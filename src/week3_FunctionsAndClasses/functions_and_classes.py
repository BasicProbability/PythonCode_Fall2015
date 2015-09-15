'''
Created on Sep 14, 2015

@author: Philip Schulz
'''

# If we want to be able to use the main function, we better import sys
import sys

# The variable add2 is unknown and we cannot use it here
# add2(3)

# This is our first function definition. ALWAYS remember to put in a docstring.
def add2(some_number):
    """
    Adds 2 to the input number.
    
    @param some_number: The number you want to add 2 to
    @return: The sum of 2 and the input number
    """
     
    # Most of our functions should return values
    return some_number + 2
  
# Now that we have defined add2() we can use it  
print add2(3)

# This is an example of default arguments. Notice that arguments with default values always have
# to be at the end of the argument list
def add(some_number, some_other_number = 1):
    """
    Add the two input numbers
    
    @param some_number: The first number to add
    @param some_other_number: The second number to add (default: 1)
    @return The sum of the two argument numbers 
    """
    
    return some_number + some_other_number
    
# Default values allow us to define functions of different arity in one go. In our case, add() can be
# used with one or two arguments.
print add(2,3)
print add(5)

# This is an example of a recursive function
def factorial(some_number):
    '''
    Compute the factorial of the input if the input is >= 0.
    
    @param some_number: Number of which the factorial should be computed
    @return Factorial of the input
    '''
    
    # Base case
    if some_number == 0:
        return 1
    # The recursive case, where the function calls itself
    elif some_number > 0:
        return factorial(some_number-1)*some_number
    else:
        print "Argument has to be a natural number."
       
# Yeah, it works 
print factorial(11)

# Here, we define our first main method. In your programs, everything should be operated through main.
def main():
    print factorial(6)
    
# This statement makes sure that a) Python knows there is a main method and b) Python executes that main method.
if __name__ == '__main__':
    main()