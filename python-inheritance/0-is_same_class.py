#!/usr/bin/python3
'''declaring a function to check object instance ina specified class'''
def is_same_class(obj, a_class):
    '''
    return is either true or false based on the check.
    '''
    return type(obj) is a_class
