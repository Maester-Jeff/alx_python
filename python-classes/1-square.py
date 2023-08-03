#!/usr/bin/python3
'''
This program has a class square that defines a square with a private instance attribute named size
'''
class Square:
    ''' delcaration of the class'''
    def __init__(self, size=0):
        '''defining and initializing the square object with a private size attribute'''
        self.__size = size
        self.check_size()
    def check_size(self):
        '''
        Creating the loop for checking whether the size is an integer and not less than zero
        '''
        if type(self.__size) != int:
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0") 