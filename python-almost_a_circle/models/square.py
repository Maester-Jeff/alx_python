#!/usr/bin/python3
from models.rectangle import Rectangle
'''
This script involves class square inheriting the previous rectangle class.
'''
class Square(Rectangle):
    '''Class square created.'''
    def __init__(self, size, x=0, y=0, id=None):
        '''
        Class constructor initialized based on rectangle attributes. 
        Width and height replaced with size.
        '''
        self.width = size
        self.height = size
        super().__init__(size, size, x, y, id)
    @property
    def size(self):
        '''Getter method for the size attribute to represent both width and height.'''
        return self.height, self.width
    @size.setter
    def size(self, value):
        '''Corresponding setter method for size.'''
        self.width = value
        self.height = value
    def __str__(self):
        '''Overloading string method.'''
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

