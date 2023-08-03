#!/usr/bin/python3
'''
Program creates a class with a method raising an exception
'''
class BaseGeometry:
    '''
    creating the Class name.
    '''
    def __dir__(cls) -> None:
        '''
        function method creats a list of all attributes for the class and excludes the init_subclass.
        '''
        attributes = super().__dir__()
        list_to_return = []
        for attr in attributes:
            if attr != "__init_subclass__":
                list_to_return.append(attr)
        return list_to_return
    
    def area(self, area):
        '''Method raises the exception message as stated below.'''
        self.area = area
        raise Exception("area() is not implemented")
        