#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
  for row in matrix:
    for matrix_num in row:
      print("{}".format(str(matrix_num)),end=" ")
    print()
