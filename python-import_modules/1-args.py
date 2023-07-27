#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
  def highlight_list(*argv):
    num_argue = len(argv)
    if num_argue == 0:
      print(num_argue, "arguments.")
    elif num_argue == 1:
      print(num_argue, "argument:")
    else:
      print(num_argue, "arguments:")
    for i, arg in enumerate(argv, 1):
      print(f"{i}: {arg}", sep=" ")
highlight_list()