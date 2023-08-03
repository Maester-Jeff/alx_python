#!/usr/bin/python3
'''declaring a function to check object instance'''
def is_same_class(obj, a_class):
    '''
    function that returns true if object is exactly an instance of the specified class. Else it returns false.
    '''
    return isinstance(obj, a_class)
