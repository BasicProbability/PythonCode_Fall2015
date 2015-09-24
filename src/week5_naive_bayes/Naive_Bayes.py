'''
Created on Sep 23, 2015

@author: Philip Schulz
'''
from collections import Counter
from math import log

class Naive_Bayes(object):
    '''
    This class implements a naive bayes classifier.
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
        self.label_probs = Counter()
        self.feature_probs = dict()
        self.labels_are_normalised = False
        self.features_are_normalised = True
        
    def train(self, data, label):
        for line in data:
            self.add_feature_counts(line.split(), label)
        
        self.log_normalise_label_probs()
        self.log_normalise_feature_probs()
    
    def add_feature_counts(self, data, label):
        current_feature_counter = None
        
        if self.label_probs.has_key(label):
            current_feature_counter = self.feature_probs[label]
        else:
            current_feature_counter= Counter()
            self.feature_counter[label] = current_feature_counter
            
        current_feature_counter.update(data)
        
    def update_label_count(self,label):
        self.label_probs.update([label])
        
    def collapse_infrequent_words(self, threshold):
        if not self.features_are_normalised:
            for feature_counter in self.feature_probs.values():
                for word, count in feature_counter.iteritems():
                    if count <= threshold:
                        del feature_counter[word]
                        feature_counter["__UNK__"] += count
            
        
    def log_normalise_label_probs(self):
        normaliser = float(sum(self.label_probs.values()))
        for label, count in self.label_probs.iteritems():
            self.label_probs[label] = log(count/normaliser)
            
    def log_normalise_feature_probs(self):
        #TODO: check whether it works when we only iterate over values
        for feature_counter in self.feature_probs.values():
            normaliser = float(sum(feature_counter()))
            for feature, count in feature_counter.iteritems():
                feature_counter[feature] = log(count/normaliser)
                
    def predict(self, data):
        label_scores = list()
        for label in xrange(self.label_probs):
            # this is the label prior
            current_label_score = self.label_probs[label]
            current_feature_probs = self.feature_probs[label]
            for line in data:
                for feature in line.split():
                    current_label_score += current_feature_probs[feature]
            
            label_scores.append(current_label_score)
        
        return label_scores.index(max(label_scores))
        