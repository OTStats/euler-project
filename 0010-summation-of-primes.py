# Summation of primes
# 
# Problem 10
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# 
# Find the sum of all the primes below two million.

import math

def flag_prime(x):
  if x == 1:
    flag = False
  # Set the "base" prime numbers
  if x == 2 | x == 3:
    flag = True
  # 
  else:
    possible_factors = list(range(2, int(math.sqrt(x)) + 1))
    n_possible_factors = len(list(filter(lambda y: x % y == 0, possible_factors)))
    if n_possible_factors == 0:
      flag = True
    else: 
      flag = False
  return(flag)



sum(list(filter(flag_prime, range(2, 2000000))))
# 142913828922

# Resource:
# https://gist.github.com/yelluw/f24b0c4020b479b37eeb7ff7e44eca7e
