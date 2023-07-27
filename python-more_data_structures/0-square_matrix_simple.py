#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [] #new matrix to encompass the new one with sqaured figures
    for row in matrix:
      new_row = [] # new row as with the matrix when numbers are squared
      for number in row:
         new_number = number ** 2
         new_row.append(new_number) #appending the new row with new figures from the squared results
      new_matrix.append(new_row)
    return new_matrix
def display_new_matrix(matrix=[]):
    for row in matrix:
      print(", ".join(str(number)for number in row))
