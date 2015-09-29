'''
Created on Sep 19, 2015

@author: Philip Schulz
'''

from random import Random, shuffle
from math import factorial

class BinomialDistribution(object):
    '''
    This class implements the binomial distribution with parameters n and theta, where n
    is the number i.i.d. random binary decisions and theta is the probability for a success.
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
        
        self.set_n(n)
        self.set_theta(theta)
        self.success = success
        self.failure = failure
        self.random_generator = Random()
    
    def set_n(self, n):
        '''
        Set a new value for the parameter n.
        
        @param n: the new value for n
        @raise ValueError: if n <= 0
        '''
        
        if n < 1:
            raise ValueError("The argument n needs to be strictly greater than 0.")
        
        self.n = n
            
        
    def set_theta(self, theta):
        '''
        Set a new value for the parameter theta.
        
        @param theta: the new value for the parameter theta
        @raise ValueError: if theta is outside [0,1]
        '''
        
        if theta < 0 or theta > 1:
            raise ValueError("The argument theta needs to lie in [0,1].")
    
        self.theta = theta
    
    def compute_probability(self, k):
        '''
        Compute the probability of obtaining exactly k successes.
        
        @param k: the number of successes
        @return The probability of obtaining exactly the specified number of successes
        @raise ValueError: if k > n or k < 0
        '''
        
        if k > self.n:
            raise ValueError("There cannot be more successes than draws. Decrease k!")
        elif k < 0:
            raise ValueError("The number of successes has to be positive.")
    
        binomial_coefficient = factorial(self.n)/(factorial(k)*factorial(self.n-k))
        return binomial_coefficient*(self.theta**k)*((1-self.theta)**(self.n-k))
    
    def sample_with_k_successes(self, k):
        '''
        Randomly sample an outcome with exactly k successes.
        
        @param k: the number of successes
        @return: A randomly sampled outcome with exactly k successes.
        @raise ValueError: if k > n or k < 0
        '''
        
        if k > self.n:
            raise ValueError("There cannot be more successes than draws. Decrease k!")
        elif k < 0:
            raise ValueError("The number of successes has to be positive.")
        
        sampled_value = list()
        for i in xrange(k):
            sampled_value.append(self.success)
        for i in xrange(self.n-k):
            sampled_value.append(self.failure)
            
        shuffle(sampled_value)
        return sampled_value
    
    def sample(self):
        '''
        Samples a random outcome from this distribution.
        
        @return A randomly sampled outcome from this distribution in form of a list.
        '''
        
        threshold = self.random_generator.random()
        total = 0
        for k in xrange(self.n+1):
            total += self.compute_probability(k)
            if total > threshold:
                return self.sample_with_k_successes(k)
    
    def sample_list(self, m):
        '''
        Samples m random outcomes from this distribution.
        
        @param m: The number of outcomes to be sampled
        @return A list of k random outcomes from this distribution.
        @raise ValueError: if m < 1
        '''
        
        result = list()
        
        for i in xrange(m):
            result.append(self.sample())
            
        return result