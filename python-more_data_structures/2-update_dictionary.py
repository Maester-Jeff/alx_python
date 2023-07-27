#!/usr/bin/python3
'''
def update_dictionary(a_dicitonary, key, value):
    a_dicitonary[key] = value
'''
def update_dictionary(a_dictionary, key, value):
  """
  Replaces or adds key/value in a dictionary.
  Args:
    a_dictionary: The dictionary to be updated.
    key: The key to be updated or added.
    value: The value to be associated with the key.
  Returns:
    The updated dictionary.
  """
  if key in a_dictionary:
    a_dictionary[key] = value
  else:
    a_dictionary[key] = value
  return a_dictionary