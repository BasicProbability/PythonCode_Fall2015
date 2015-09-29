'''
Created on Sep 19, 2015

@author: Philip Schulz
'''

from math import log1p, exp

def log_add(first_logarithm, second_logarithm):
    '''
    Add to real numbers in log-space. This function should preferebly be used with
    the logarithms of small real values.
    
    @param first_logarithm: The logarithm of the first number
    @param second_logarithm: The logarithm of the second number
    @return: The logarithm of the sum of the two numbers     
    ''' 
    
    if first_logarithm >= second_logarithm:
        return second_logarithm + log1p(exp(first_logarithm - second_logarithm))
    else:
        return first_logarithm + log1p(exp(second_logarithm - first_logarithm))

def log_difference(first_logarithm, second_logarithm):
    '''
    Calculate the difference of two real numbers in log-space. This function should
    preferably be used with the logarithms of small numbers.
    
    @param first_logarithm: The logarithm of the first number
    @param second_logarithm: The logarithm of the second number
    @return: The logarithm of the sum of the two numbers      
    @raise: ValueError: second_logarithm >= first_logarithm
    '''
    
    if second_logarithm >= first_logarithm:
        raise ValueError("The result of logarithmic differences must be positive in real space, "
                         "since the logaritm is not defined in (-inf, 0].")
        
    return first_logarithm + log1p(-exp(second_logarithm - first_logarithm))