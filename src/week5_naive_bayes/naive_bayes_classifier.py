'''
Created on Sep 23, 2015

@author: Philip Schulz
'''

import sys
import argparse
from datetime import datetime
from Naive_Bayes import Naive_Bayes
from os import listdir, remove
from os.path import isfile, join

def train_model(corpus_dir, classifier, min_count):
    print 'Starting training at {}'.format(datetime.now())
    
    for directory in listdir(corpus_dir):
        print "Training on label {}".format(directory)
        directory_path = join(corpus_dir, directory)
        for text_file in listdir(directory_path):
            file_path = join(directory_path, text_file)
            classifier.update_label_count(directory)
            try:
                with open(file_path) as data_file:
                    classifier.train(data_file, directory)
            except IOError, e:
                print e 
                print "It seems that the text_file {} is damaged.".format(text_file)
                sys.exit(0)
        
    classifier.collapse_infrequent_features(min_count)
    classifier.log_normalise_label_probs()
    classifier.log_normalise_feature_probs()
    print "Finished training at {}".format(datetime.now())

def make_predictions(predictions_file, test_dir, classifier):
    if isfile(predictions_file):
        remove(predictions_file)
    
    for test_file in listdir(test_dir):
        try:
            with open(join(test_dir, test_file)) as test, open(predictions_file, "a") as out:
                prediction = classifier.predict(test)
                out.write(test_file + ": {}\n".format(prediction))
        except IOError, e:
            print e 
            print "Something went wrong while reading test file {}".format(test_file)
            sys.exit(0)

def main():
    
    commandline_parser = argparse.ArgumentParser("Add description.")
    
    commandline_parser.add_argument("--training-corpus-directory", nargs = 1, default=[""], help="Specifies the path to the directory where the corpus is stored.")
    commandline_parser.add_argument("--test-set-directory", nargs = 1, default=[""], help="Specifies the path to the directory where the test files are stored.")
    
    args = vars(commandline_parser.parse_args())
    corpus_dir = args["training_corpus_directory"][0]
    test_dir = args["test_set_directory"][0]
    
    nb_classifier = Naive_Bayes()
    
    if corpus_dir:
        train_model(corpus_dir, nb_classifier, 1)
    
    if test_dir:
        make_predictions("predictions.txt", test_dir, nb_classifier)

if __name__ == '__main__':
    main()
    
