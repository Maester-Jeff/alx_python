#!/usr/bin/python3
'''
This script creates class that inherits the previous base class.
'''
from models.base import Base
'''importing the script of the previous parent class.'''

class rectangle(Base):
    '''creation and initialization of the inheriting class.'''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''class constructor with the necessary attributes.'''
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        self.id = id
        super().__init__(id)
        '''Calling the super class with id using the init logic.'''

    @property
    def width(self):
        '''The getter method for width attribute'''
        return self.__width
    @width.setter
    def width(self, value):
        '''The setter method for width attribute'''
        self.__width = value

    @property
    def height(self):
        '''The getter method for height attribute'''
        return self.__height
    @height.setter
    def height(self, value):
        '''The setter method for height attribute'''
        self.__height = value

    @property
    def x(self):
        '''The getter method for x attribute'''
        return self.__x
    @x.setter
    def x(self, value):
        '''The getter method for x attribute'''
        self.__x = value
    
    @property
    def y(self):
        '''The getter method for y attribute'''
        return self.__y
    @y.setter
    def y(self, value):
        '''The getter method for y attribute'''
        self.__y = value
