#!/usr/bin/python3
def multiple_returns(sentence):
  if sentence == "":
    return ("Length: {:d} - First character: {}".format(len(sentence), None))
  else:
    return ("Length: {:d} - First character: {}".format(len(sentence), sentence[0]))


'''
def multiple_returns(sentence):
  if sentence == "":
    return (0, None)
  else:
    return (len(sentence), sentence[0])

print(multiple_returns(""))
'''