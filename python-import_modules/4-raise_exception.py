
def raise_exception():
  try:
    raise_exception()
  except TypeError as te:
    print("Exception raised")

'''
def safe_print_division(a, b):
  """
  Divides 2 integers and prints the result.
  Args:
    a: The first integer to divide.
    b: The second integer to divide by.
  Returns:
    The value of the division, otherwise: None
  Raises:
    ZeroDivisionError: If b is 0.
  """
  try:
    result = a / b
  except ZeroDivisionError:
    print("Division by zero")
  finally:
    print("Inside result: {}".format(result))
  return result
print(safe_print_division(2, 0))
'''
