'''
#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
  for row in matrix:
    for matrix_num in row:
      print("{:d}".format(matrix_num),end=' ')
    print()
'''

def print_matrix_integer(matrix=[[]]):
  """
  Prints a matrix of integers.
  Args:
    matrix: A list of lists of integers.
  Returns:
    None.
  """
  for row in matrix:
    for column in row:
      print(str(column), end=" ")
    print()