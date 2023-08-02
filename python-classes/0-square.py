#!/usr/bin/python3
'''
This program has a class square that defines a square with a private instance attribute named size
'''
''' delcaration of the class'''
class Square:
    '''defining and initializing the square object with a size arguement'''
    def __init__(self, size):
        '''making the size attribute private'''
        self.__size = size

