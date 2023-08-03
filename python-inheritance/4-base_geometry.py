#!/usr/bin/python3
'''
creating the Class name.
'''
class BaseGeometry:
    def area(self, area):
        '''Method raises the exception message as stated below.'''
        self.area = area
        raise Exception("area() is not implemented")
        