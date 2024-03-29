# Highly divisible triangular number
# 
# Problem 12
# The sequence of triangle numbers is generated by adding the natural numbers. 
# So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first 
# ten terms would be:
# 
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# 
# Let us list the factors of the first seven triangle numbers:
# 
#  1: 1
#  3: 1,3
#  6: 1,2,3,6
# 10: 1,2,5,10
# 15: 1,3,5,15
# 21: 1,3,7,21
# 28: 1,2,4,7,14,28
# We can see that 28 is the first triangle number to have over five divisors.
# 
# What is the value of the first triangle number to have over five hundred divisors?


import math

number = 0
triangle_sum = 0
divisors = 0

while divisors <= 500:
    # Add one to our number list 
    number += 1
    # Cumulative sum of number list
    triangle_sum += number
    # Set number of divisors
    divisors = 0
    
    for i in range(1, int(math.sqrt(triangle_sum)) + 1):
      if triangle_sum % i == 0:
        divisors += 2

print(number, triangle_sum,  divisors)
