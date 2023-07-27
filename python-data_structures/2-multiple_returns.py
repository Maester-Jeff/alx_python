#!/usr/bin/python3
def multiple_returns(sentence):
  length = len(sentence)
  if sentence == "":
    print("Length: {:d} - First character: None".format(length))
  else:
    print("Length: {:d} - First character: {}".format(length, sentence[0]))
