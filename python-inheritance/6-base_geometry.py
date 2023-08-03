#!/usr/bin/python3
'''
creating a class with a method that raises an exception and another that validates value.
The module also contains a class rectangle tha inherits the main class.
'''
class BaseGeometryMetaClass(type):
    '''
    creating the meta Class to remove unwanted subclasses.
    '''
    def __dir__(cls):
        '''
        function method creats a list of all attributes for the class and excludes the init_subclass.
        '''
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']
class BaseGeometry(metaclass = BaseGeometryMetaClass):
    '''empty class created'''
    def __dir__(cls):
        '''
        function method creats a list of all attributes for the class and excludes the init_subclass.
        '''
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']
    pass
    def area(self):
        '''Method raises the exception message as stated below.'''
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        self.name = name
        self.value = value
        if type(self.value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif self.value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        
