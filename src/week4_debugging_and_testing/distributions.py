'''
Created on Sep 19, 2015

@author: Philip Schulz
'''

from random import Random, shuffle
from math import factorial

class BinomialDistribution(object):
    '''
    This class implements the binomial distribution with parameters n and theta, where n
    is the number of i.i.d. random binary decisions and theta is the probability for a success.
    Successes and failures can be arbitrary objects.
    '''

    success = None
    failure = None
    n = None
    theta = None
    random_generator = None

    def __init__(self, success, failure, n = 10, theta = 0.5):
        '''
        Constructor
        
        @param success: the value of a success
        @param failure: the value of a failure
        @param n: the value of the parameter n
        @param theta: the value of the parameter theta
        @raise ValueError: if theta is outside [0,1] or n <= 0 
        '''
        
        # It is crucial that you make sure that each instance of this class
        # has its own private random number generator!
        pass
    
    def set_n(self, n):
        '''
        Set a new value for the parameter n.
        
        @param n: the new value for n
        @raise ValueError: if n <= 0
        '''
        pass
        
    def set_theta(self, theta):
        '''
        Set a new value for the parameter theta.
        
        @param theta: the new value for the parameter theta
        @raise ValueError: if theta is outside [0,1]
        '''
        pass
    
    def compute_probability(self, k):
        '''
        Compute the probability of obtaining exactly k successes.
        
        @param k: the number of successes
        @return The probability of obtaining exactly the specified number of successes
        @raise ValueError: if k > n or k < 0
        '''
        pass
    
    def sample_with_k_successes(self, k):
        '''
        Randomly sample an outcome with exactly k successes.
        
        @param k: the number of successes
        @return: A randomly sampled outcome with exactly k successes.
        @raise ValueError: if k > n
        '''
        pass
    
    def sample(self):
        '''
        Samples a random outcome from this distribution.
        
        @return A randomly sampled outcome from this distribution in form of a list.
        '''
        
        # Use compute_probability and sample_with_k_successes here
        # Implement inverse transform sampling here
    
    def sample_list(self, m):
        '''
        Samples m random outcomes from this distribution.
        
        @param m: The number of outcomes to be sampled
        @return A list of k random outcomes from this distribution.
        @raise ValueError: if m < 1
        '''
        
        # use sample() here
        pass
