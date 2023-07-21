def fibonacci_sequence(n):
  number1 = 0 
  number2 = 1
  counter = 0
  fib_sequence = []
  while counter < n:
    fib_sequence.append(number1)
    nth = number1 + number2
    number1 = number2
    number2 = nth
    counter = counter + 1
  return fib_sequence
