#!/usr/bin/python3
def is_same_class(obj, a_class):
    '''
    Write a function that returns True if the object
    is exactly an instance of the specified class ; otherwise False.

    Parameters:
    - obj: The object to check.
    - a_class: The specified class.

    Returns:
    - True if obj is an instance of a_class, False otherwise.
    '''
    if type(obj) == a_class:
        return True
    else:
        return False
