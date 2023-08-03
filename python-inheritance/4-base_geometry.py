#!/usr/bin/python3
class BaseGeometry:
    '''
    creating the Class name.
    '''
    def area(self, area):
        '''Method raises the exception message as stated below.'''
        self.area = area
        raise Exception("area() is not implemented")
        