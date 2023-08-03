#!/usr/bin/python3
'''
This program has a class square that defines a square with a private instance attribute named size
'''
''' delcaration of the class'''
class Square:
    '''defining and initializing the square object with a size arguement'''
    def __init__(self, size=0):
        '''making the size attribute private'''
        self.__size = size
    '''Creating the loop for checking whether the size is an integer and not less than zero'''
    def check_size(self):
        if type(self.__size) != int:
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")

