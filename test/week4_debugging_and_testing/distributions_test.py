'''
Created on Sep 19, 2015

@author: Philip Schulz
'''
import unittest
from random import Random
from week4_debugging_and_testing.distributions import BinomialDistribution

class DistributionsTest(unittest.TestCase):
    
    random_generator = Random()
    binomial = BinomialDistribution(1,0)

    def test_binomial_constructor_valueError(self):
        '''
        Test whether the constructor correctly throws an error when n < 1
        '''
        neg_int = -self.random_generator.randint(0, 1000)
        
        with self.assertRaises(ValueError):
            BinomialDistribution(1, 0, neg_int)
        
    def test_set_n_valueError(self):
        '''
        Test whether set_n correctly throws an error when n < 1
        '''
        neg_int = -self.random_generator.randint(0, 1000)
        
        with self.assertRaises(ValueError):
            self.binomial.set_n(neg_int)
        
    def test_set_theta(self):
        '''
        Test whether set_theta correctly throws an error when theta is outside [0,1]
        '''
        pos_number = self.random_generator.random() + 1
        neg_number = self.random_generator.random() - 1
        
        with self.assertRaises(ValueError, msg= "No error is thrown when theta > 1."):
            self.binomial.set_theta(pos_number)
            
        with self.assertRaises(ValueError, msg="No error is thrown when theta < 0."):
            self.binomial.set_theta(neg_number)

    def test_compute_probability(self):
        '''
        Test whether success probabilities are correclty computed
        '''
        
        probs = [0.0009765625, 0.0097656250, 0.0439453125, 0.1171875000, 0.2050781250,
                 0.2460937500, 0.2050781250, 0.1171875000, 0.0439453125, 0.0097656250,
                 0.0009765625]
        
        successes = 0
        for prob in probs:
            # Allow for numerical deviance of up to 1/100.000
            self.assertTrue(abs(self.binomial.compute_probability(successes) - prob) < 0.00001)
            successes += 1
            
    def test_compute_probability_valueError(self):
        '''
        Test whether compute_probability correctly throws an error when k < 0 or k > n.
        '''
        pos_number = self.random_generator.randint(11, 10000)
        neg_number = -self.random_generator.randint(0, 1000)
        
        with self.assertRaises(ValueError, msg="No error is thrown when k < 0."):
            self.binomial.compute_probability(neg_number)
            
        with self.assertRaises(ValueError, msg="No error is thrown when k > n."):
            self.binomial.compute_probability(pos_number)
             
        
    def test_sample_with_k_successes(self):
        '''
        Test whether sample_sample_with_k_successes returns a list with k successes.
        '''
        
        for i in xrange(10000):
            k = self.random_generator.randint(0, 10)
            self.assertEqual(k, sum(self.binomial.sample_with_k_successes(k)))
            
    def test_sample_with_k_successes_valueError(self):
        '''
        Test whether sample_with_k_successes correctly throws an error when k < 0 or k > n.
        '''
        pos_number = self.random_generator.randint(11, 10000)
        neg_number = -self.random_generator.randint(0, 1000)
        
        with self.assertRaises(ValueError, msg="No error is thrown when k > n."):
            self.binomial.sample_with_k_successes(pos_number)
            
        with self.assertRaises(ValueError, msg="No error is thrown when k < 0."):
            self.binomial.sample_with_k_successes(neg_number)

    def test_sample(self):
        '''
        Test whether sample works correctly.
        '''
        
        for i in xrange(10000):
            sample_value = self.binomial.sample()
            length = len(sample_value)
            successes = sum(sample_value)
            self.assertEqual(length, 10, "Sampled sequence is not of correct length.")
            self.assertTrue(0 <= successes <= 10, "There are more or less successes than possible.")
            
    def test_sample_list(self):
        '''
        Test whether sample_list works correctly.
        '''
        
        for i in xrange(100):
            sample_length = self.random_generator.randint(1, 1000)
            sampled_list = self.binomial.sample_list(sample_length)
            
            for sample_value in sampled_list:
                length = len(sample_value)
                successes = sum(sample_value)
                self.assertEqual(length, 10, "Sampled sequence is not of correct length.")
                self.assertTrue(0 <= successes <= 10, "There are more or less successes than possible.")

if __name__ == "__main__":
    unittest.main()
