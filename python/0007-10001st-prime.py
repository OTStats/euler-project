# 10001st prime
# 
# Problem 7
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?

# Use flag_prime() from question 3
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


candidates = range(1, 200000)

# Filter for prime numbers and select the 10001st element
filter(flag_prime, candidates)[10001]
# 104743

