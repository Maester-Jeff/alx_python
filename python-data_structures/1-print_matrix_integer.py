#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
  for row in matrix:
    for mat_num in row:
      if mat_num != row[-1]:
        print("{}".format(mat_num),end=" ")
      else:
        print("{}".format(mat_num),end="")
    print()

