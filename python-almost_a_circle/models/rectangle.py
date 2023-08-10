#!/usr/bin/python3
'''
This script creates class that inherits the previous base class.
'''
from models.base import Base
'''importing the script of the previous parent class.'''

class Rectangle(Base):
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
        '''The getter method for width attribute.'''
        return self.__width
    
    @width.setter
    def width(self, value):
        '''The setter method for width attribute.'''
        self.__width = value
        if type(value) is not int:
            '''if statement validating width.'''
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")

    @property
    def height(self):
        '''The getter method for height attribute.'''
        return self.__height
    
    @height.setter
    def height(self, value):
        '''The setter method for height attribute.'''
        self.__height = value
        '''If statement validating height.'''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")

    @property
    def x(self):
        '''The getter method for x attribute.'''
        return self.__x
    
    @x.setter
    def x(self, value):
        '''The getter method for x attribute'''
        self.__x = value
        '''If statement validating x.'''
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
    
    @property
    def y(self):
        '''The getter method for y attribute'''
        return self.__y
    
    @y.setter
    def y(self, value):
        '''The getter method for y attribute'''
        self.__y = value
        '''If statement validating y.'''
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
    def area(self):
        '''Function for returning the area of rectangle.'''
        return self.__width * self.__height
    def display(self):
        '''The public instance method that prints in stdout 
        the rectangle with the character while considering x and y.
        '''
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " *self.__x + "#" *self.__width)
    def __str__(self):
        '''The overriding str method.'''
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args):
        '''Public method for assigning arguements to the attributes.'''
        self.id = self.args1
        self.width = self.args2
        self.height = self.args3
        self.x = self.args4
        self.y = self.args5

