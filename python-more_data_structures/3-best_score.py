#!/usr/bin/python3
def best_score(a_dictionary):
  best_key = None
  best_score = None
  for value, key in a_dictionary.items():
    if best_score == None or value > best_score:
      best_score = value
      best_key = key
  return best_key
