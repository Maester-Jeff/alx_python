#!/usr/bin/python3
'''This program creates a class base with the argument and function statement below'''
class Base:
    __nb_objects = 0
    def __init__(self, id=None):
        '''The init function initialzing the object'''
        self.id = id
        if id is not None:
            '''if statement checking whether the id attribute is none'''
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects