def fibonacci_sequence(n):
  fib_terms = n
  counter = 0
  term_1 = 0
  term_2 = 1
  next_term = 0
  while counter <= fib_terms:
    next_term = term_1 + term_2
    term_1 = term_2
    term_2 = next_term
    counter = counter + 1


    


