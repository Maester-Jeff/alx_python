#!/usr/bin/python3
'''
This program has a class square that defines a square with a private instance attribute named size
'''
class Square:
    ''' delcaration of the class'''
    def __init__(self, size=0):
        '''defining and initializing the square object with a private size attribute'''
        self.__size = size 
    def get_size(self):
        '''defining the method for retrieving the size attribute'''
        return self.__size
    def set_size(self, value):
        '''
        Creating the loop for checking whether the size is an integer and not less than zero
        '''
        self.__size = value
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
    def area(self):
        '''defining the method to compute the current squared area'''
        self.area = self.__size**2
        return self.area
my_square = Square()
        