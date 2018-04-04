def hailstone(n, v = 0):
  print(n)
  if n == 1:
    return v
  
  if n % 2 == 0:
    return hailstone(n / 2, v + 1)
  else:
    return hailstone((3 * n) + 1, v + 1)

def fact(n):
  if n == 0:
    return 1
  
  return n * fact(n - 1)
