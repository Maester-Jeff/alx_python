#!/usr/bin/python3
'''
The function returns true if the object is an isntance of a class directly or indirectly inheriting the specified class.
'''
def inherits_from(obj, a_class):
    '''
    Else it returns false.
    '''
    return issubclass(type(obj), a_class) and type(obj) != a_class
