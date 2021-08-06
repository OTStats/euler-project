# Largest prime factor
# 
# Problem 3
# The prime factors of 13195 are 5, 7, 13 and 29.
# 
# What is the largest prime factor of the number 600851475143?

# Prime numbers: Number whose only factors are 1 and the number itself
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


def max_prime_factor(num):
  possible_factors = list(range(2, int(math.sqrt(num)) + 1))
  factors = list(filter(lambda x: num % x == 0, possible_factors))
  if len(factors) == 0:
    output = print("Your input (", num, ") is a prime number, so the largest prime factor is itself!", sep="")
  else:
    max_prime = max(list(filter(flag_prime, factors)))
    output = print("The max prime factor of", "{:,}".format(num), "is:", "{:,}".format(max_prime))
  return(output)

# # Confirm that my function works on the test case
# max_prime_factor(13195)
# The max prime factor of 13,195 is: 29
# Confirmed!

max_prime_factor(600851475143)
# The max prime factor of 600,851,475,143 is: 6,857
