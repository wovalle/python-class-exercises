def IsPrime(number):
  for i in range(2, number-1):
    if number % i == 0:
      return False

  return True
  

def summationOfPrimes(primes):
  sum = 0
  for i in range (2, primes+1):
    if IsPrime(i):
      sum+= i
  return sum

print(summationOfPrimes(10))
print(summationOfPrimes(5))
print(summationOfPrimes(25000))
  
  
  
  
  
  
  
#test.assert_equals(summationOfPrimes(10), 17)
