'''
Created on Sep 23, 2015

@author: Philip Schulz
'''

import sys
import argparse
from datetime.datetime import now
from week5_naive_bayes.Naive_Bayes import Naive_Bayes
from os import listdir
from os.path import isfile, isdir, join

def train_model(corpus_dir, classifier):
    print 'Starting training at {}'.format(now())
    
    labels = list()
    
    label = 0
    for directory in listdir(corpus_dir):
        print "Training on label {}".format(label+1)
        labels.append(directory)
        directory_path = join(corpus_dir, directory)
        for text_file in listdir(dir):
            file_path = join(directory_path, text_file)
            classifier.update_label_count(label)
            try:
                with open(file_path) as data_file:
                    classifier.train(data_file, 0)
            except IOError, e:
                print e 
                print "It seems that the text_file {} is damaged.".format(text_file)
                sys.exit(0)
        label += 1
        
    print "Finished training at {}".now()
    return labels

def make_predictions(test_dir, classifier, labels):
    for test_file in listdir(test_dir):
        try:
            with open(join(test_dir, test_file)) as test, open("predictions.txt", "w") as out:
                prediction = classifier.predict(test)
                out.write(labels[prediction] +"\n")
        except IOError, e:
            print e 
            print "Something went wrong while reading test file {}".format(test_file)
            sys.exit(0)

def main(files):
    
    commandline_parser = argparse.ArgumentParser("Add description.")
    
    commandline_parser.add_argument("--corpus-directory", nargs =1, help="Specifies the path to the directory where the corpus is stored.")
    
    commandline_parser.add_argument("--test-set-directory", nargs=1, help="Specifies the path to the directory where the test files are stored.")
    
    args = vars(commandline_parser.parse_args())
    corpus_dir = args["corpus_directory"]
    test_dir = args["test-set-directory"]
    
    nb_classifier = Naive_Bayes()
    
    labels = train_model(corpus_dir, nb_classifier)
    
    make_predictions(test_dir, nb_classifier, labels)

if __name__ == '__main__':
    main()
    