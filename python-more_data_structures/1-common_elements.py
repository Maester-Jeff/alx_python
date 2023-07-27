#!/usr/bin/python3
def common_elements(set_1, set_2):
  c_set = set()
  for number in set_1:
    if number in set_2:
        c_set.add((number))
  return c_set
