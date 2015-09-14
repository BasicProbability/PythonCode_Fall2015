'''
Created on Sep 14, 2015

@author: Philip Schulz
'''
import sys

# add2(3)
# x = None
def add2(some_number):
    """
    Adds 2 to the input number.
    
    @param some_number: The number you want to add 2 to
    @return: The sum of 2 and the input number
    """
     
    return some_number + 2
    
print add2(3)
# print x

def add(some_number, some_other_number = 1):
    """Put docstring here"""
    
    return some_number + some_other_number
    
print add(2,3)
print add(5)

def factorial(some_number):
    if some_number == 0:
        return 1
    elif some_number > 0:
        return factorial(some_number-1)*some_number
    else:
        print "Argument has to be a natural number."
        
print factorial(11)

def main():
    print factorial(6)
    
if __name__ == '__main__':
    main()