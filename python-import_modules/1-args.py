#!/usr/bin/python3
if __name__ == "__main__":
  import sys
  num_argue = len(sys.argv)
  if num_argue == 1:
    print(0, "arguements.")
  elif num_argue == 2:
    print(num_argue - 1, "argument:")
    for i in range(1, len(sys.argv)):
      print (i, sys.argv[1], sep=": ")
  else:
    print(num_argue - 1, "arguments:")
    for i in range(1, len(sys.argv)):
      print(i, sys.argv[i], sep=": ")
