#!/usr/bin/python3
'''
This script involves class square inheriting the previous rectangle class.
'''
from models.rectangle import Rectangle
'''Importing the previous rectangle script.'''

class Square(Rectangle):
    '''Class square created.'''
    def __init__(self, size, x=0, y=0, id=None):
        '''
        Class constructor initialized based on rectangle attributes. 
        Width and height replaced with size.
        '''
        self.width = size
        self.height = size
        self.x = size
        self.y = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        '''Getter method for the size attribute to represent both width and height.'''
        return self.height, self.y
    
    @size.setter
    def size(self, value):
        '''Corresponding setter method for size.'''
        self.width = value
        self.height = value
        self.x = value
        self.y = value

    def __str__(self):
        '''Overloading string method.'''
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.height}"

