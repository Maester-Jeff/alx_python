#!/usr/bin/python3
'''creating an empty class script'''
class BaseGeometryMetaClass:
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
class BaseGeometry:
    '''empty class created'''
    pass