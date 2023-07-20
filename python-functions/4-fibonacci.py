def fib(n):
  if n == 0:
    return []
  elif n == 1:
    return [0]
  else:
    return [fib(n-1) + fib(n-2)]

print(fib(5))


