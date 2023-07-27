def print_matrix_integer(matrix=[[]]):
  transposed_matrix = list(zip(*matrix))
  for row in transposed_matrix:
    for num in row:
      print("{:d}".format(num))
