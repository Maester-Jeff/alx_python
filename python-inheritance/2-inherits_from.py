#!/usr/bin/python3
'''module creates a function that checks instance of an object'''


def inherits_from(obj, a_class):
    '''
    The function returns true if the object is an isntance of a class directly or indirectly inheriting the specified class.Else it returns false.
    '''
    return issubclass(type(obj), a_class) and type(obj) != a_class
