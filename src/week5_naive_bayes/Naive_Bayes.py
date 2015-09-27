'''
Created on Sep 23, 2015

@author: Philip Schulz
'''
from collections import Counter
from math import log
from sys import float_info as fi

class Naive_Bayes(object):
    '''
    This class implements a naive bayes classifier.
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
        self.label_probs = Counter()
        # A dictionary that maps labels to Counters. Each of these Counters
        # contains the feature probabilities given the label.
        self.feature_probs = dict()
        self.labels_are_normalised = False
        self.features_are_normalised = False
        self.unknown_feature = "__UNK__"
        
    def train(self, data, label):
        '''
        Train the classifier by counting features in the data set.
        
        @param data: A stream of string data from which to extract features
        @param label: The label of the data 
        '''
        for line in data:
            self.add_feature_counts(line.split(), label)
    
    def add_feature_counts(self, features, label):
        '''
        Count the features in a feature list.
        
        @param features: a list of features.
        @param label: the label of the data file from which the features were extracted.
        '''
        # TODO: implement this!
        pass 
        
    def update_label_count(self,label):
        '''
        Increase the count for the supplied label by 1.
        
        @param label: The label whose count is to be increased.
        '''
        self.label_probs.update([label])
        
    def collapse_infrequent_words(self, threshold):
        '''
        Sum up the counts of all features whose individual counts are lower than
        the threshold. Then erase those features. Finally, assign the cumulative 
        count the unknown feature.
        
        @param threshold: The count under which a feature gets collapsed onto the unknown feature. 
        '''
        # TODO: Implement this!
            
        
    def log_normalise_label_probs(self):
        '''
        Normalize the label counts to probabilities and transform them to logprobs.
        '''
        # TODO: Implement this!
        pass
            
    def log_normalise_feature_probs(self):
        '''
        Normalize the feature counts for each label to probabilities and turn them into logprobs.
        '''
        # TODO: Implement this!
        pass
                
    def predict(self, data):
        ''' 
        Predict the most probable label according to the model on a stream of data.
        
        @param data: A stream of string data from which to extract features
        @return: the most probable label for the data
        '''
        # TODO: implement this!
        pass 
        