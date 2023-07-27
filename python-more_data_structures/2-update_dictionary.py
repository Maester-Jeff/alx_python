#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
  for key in a_dictionary:
    a_dictionary[key] = value #key exits value is replaced
  else:
    a_dictionary[key] = value #where its not available then the key is created
  return a_dictionary