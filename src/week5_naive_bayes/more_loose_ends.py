'''
Created on Sep 28, 2015

@author: Philip Schulz
'''

# from sys import float_info
# import math
import argparse
# 
# 
# print (lambda hello : hello**2)(4)
# 
# my_list = range(19)
# print my_list
# 
# list_a = map(lambda y : y/0.8, map(lambda x : x**2, my_list))
# list_b = map(lambda x : (x**2)/0.8, my_list)
# 
# print list_a == list_b
# 
# print math.exp(float_info.min_exp)

def main():
    command_line_parser = argparse.ArgumentParser()
    
    #command_line_parser.add_help("This program demonstrates how to use argparse.")
    
    command_line_parser.add_argument("--some-argument", default="You have not entered anything."
                                     , help ="Showing how to add an argument.")
    
    args = vars(command_line_parser.parse_args())
    print args["some_argument"]
    
if __name__ == '__main__':
    main()