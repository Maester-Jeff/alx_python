#!/usr/bin/python3
'''
creating a class with a method that raises an exception and another that validates value.
The module also contains a class rectangle tha inherits the main class.
'''
from 5-base_geometry import BaseGeometry
'''Importing the 5-base_geometry module.'''
class Rectangle(BaseGeometry):
    '''creation of the Class rectangle'''
    def __init__(self, width, height):
        '''initialization of the init definition to initialize width and height.'''
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
