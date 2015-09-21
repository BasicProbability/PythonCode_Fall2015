'''
Created on Sep 21, 2015

@author: Philip Schulz
'''

def give_me_a_positive_number(number):
    '''
    Print input if input is positive.
    
    @param number: a positive number
    @raise ValueError: if the input is not positive
    ''' 
    if number < 1:
        # The keyword raise allows us to raise errors. We can supply each error with an optional message string.
        raise ValueError("You should not enter numbers smaller than 1.")
    
    print str(number)
    
give_me_a_positive_number(10)
# if we uncomment the line below the program will crash because of the ValueError
#give_me_a_positive_number(-10)
        
# To handle exceptions (errors) correctly, use the try-except statement. If anywhere in the try block an error occurs,
# it gets passed on to the except block and can be processed there. Note that the try block stops executing after the
# error has been thrown.
try:
    my_list = list()
    # if you uncomment this, an IndexError will be thrown
    # my_list[10]
    
    # This print statement always gets exectuted, independently of the error raised below.
    print 'hello'
    # This line will throw an error whenever the argument is not positive
    give_me_a_positive_number(-10)
    # This print statement only gets executed if no error is thrown in the line above.
    print 'goodbye'
# The except clause allows us to catch errors. It can optionally be supplied with the error type (always do this!) and 
# a variable to which the current error instance gets assigned (in this case e).
except ValueError, e:
    # print the opitional message of the error object if present
    print e
    # Do whatever else you want, after the error has been caught
    give_me_a_positive_number(9)
# You can have several except statements. If you expect different errors, this is what you should do!
# This except catches possible index errors.
except IndexError:
    print "Seems like your list is not as long as you thought."
    
# Once you exit the try-except statement, your code can proceed as usual.
print 'job done!'

# This is how you write to files. Substitute your_file_path with a valid path. The only difference to reading
# is that this time we add a second argument to open(), namely 'w'
try:
    with open("your_file_path",'w') as writer:
        for i in xrange(100):
            # Make sure to insert line breaks when you write to files.
            writer.write(str(i)+'\n')
# Every try needs at least one except. Here I decided to do nothing with except (this is not something you should do in your code).
except:
    pass
    
# Copy of the factorial function from week 3. The only difference is that this time we raise a ValueError when the argument is
# not a natural number.
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
        raise ValueError("Argument needs to be a natural number.")
        
# A tail recursive version of the factorial function.
def tail_factorial(number):
    if number == 0:
        return 1
    
    else:
        return helper_factorial(number-1, number)

# The main work in the tail recursive factorial is done by this helper function.
# Notice that most recursive functions can easily be made tail recursive by using an accumulator
# that keeps track of intermediary results.
def helper_factorial(number, accumulator):
    if number == 0:
        return accumulator
    
    else:
        accumulator *= number
        return helper_factorial(number-1, accumulator)

# Use the debugger to see how this function works on the argument 3 -- feel free to use other arguments.
print tail_factorial(3)