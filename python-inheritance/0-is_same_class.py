#!/usr/bin/python3
def is_same_class(obj, a_class):
    '''
    function that returns true if object is exactly an instance of the specified class. Else it returns false.
    '''
    if isinstance(obj, a_class):
        return True
    else:
        return False

          