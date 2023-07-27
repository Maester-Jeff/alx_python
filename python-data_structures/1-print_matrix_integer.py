''''
def print_matrix_integer(matrix=[[]]):
  for row in matrix:
    for matrix_num in row:
      print("{:d}".format(matrix_num))
'''

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for num in row:
            print("{:d}".format(num), end=" ")
        print()