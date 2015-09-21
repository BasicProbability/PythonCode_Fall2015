'''
Created on Sep 21, 2015

@author: Philip Schulz
'''

def give_me_a_positive_number(number):
    
    if number < 1:
        raise ValueError("You should not enter numbers smaller than 1.")
    
    print str(number)
    
give_me_a_positive_number(10)
#give_me_a_positive_number(-10)
        
try:
    my_list = list()
    # my_list[10]
    give_me_a_positive_number(-10)
    print 'hello'
except ValueError, e:
    print e
    give_me_a_positive_number(9)
    
print 'job done!'

try:
    with open("/home/philip/Desktop/test_file1.txt",'w') as writer:
        for i in xrange(100):
            writer.write(str(i)+'\n')
except:
    pass
    
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
        
        
def tail_factorial(number):
    if number == 0:
        return 1
    
    else:
        return helper_factorial(number-1, number)

def helper_factorial(number, accumulator):
    if number == 0:
        return accumulator
    
    else:
        accumulator *= number
        return helper_factorial(number-1, accumulator)

print tail_factorial(3)