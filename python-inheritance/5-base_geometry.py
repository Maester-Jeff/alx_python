#!/usr/bin/python3
'''creating a class with a method that raises an exception and another that validates value'''
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
            raise TypeError("<name> must be an integer")
        elif self.value <= 0:
            raise ValueError("name must be greater than 0")
