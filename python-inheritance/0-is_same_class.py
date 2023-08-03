#!/usr/bin/python3
'''
function that returns true if object is exactly an instance of the specified class. Else it returns false.
'''
def is_same_class(obj, a_class):
    if type(obj) is a_class:
        return True
    else:
        return False
          